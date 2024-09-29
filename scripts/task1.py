from telethon.sync import TelegramClient
import spacy
import re
import pymongo

# --- Configuration ---
api_id = '22603249'
api_hash = '51a0980b933520481783246cd0c70189'
bot_token = '7862282736:AAHW6muxQS5A3oplNBo84Oj7QR33qtaGY2A'

# Initialize Telegram client
client = TelegramClient('session_name', api_id, api_hash).start(bot_token=bot_token)

# MongoDB connection
mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
db = mongo_client["ecom_database"]
collection = db["telegram_messages"]

# NLP model for Amharic language
nlp = spacy.blank("am")

# --- Helper Functions ---

def normalize_text(text):
    """
    Normalize Amharic text by removing special characters and lowercasing.
    """
    text = re.sub(r'[^\w\s]', '', text)  # Remove special characters
    return text.lower()

def clean_data(text):
    """
    Clean text data by removing URLs, emojis, and unnecessary content.
    """
    text = re.sub(r'http\S+', '', text)  # Remove URLs
    text = re.sub(r'[\U00010000-\U0010ffff]', '', text)  # Remove emojis
    return text.strip()

def extract_metadata(message):
    """
    Extract metadata such as sender ID, timestamp, and message ID from the message.
    """
    return {
        "sender": message.sender_id,
        "timestamp": message.date,
        "message_id": message.id
    }

async def fetch_messages(channel_name):
    """
    Fetch messages from a given Telegram channel, process text and media.
    """
    channel = await client.get_entity(channel_name)
    async for message in client.iter_messages(channel, limit=100):
        # Process message text
        text = message.text if message.text else ''
        cleaned_text = clean_data(normalize_text(text))

        # Process tokens for Amharic
        doc = nlp(cleaned_text)
        tokens = [token.text for token in doc]

        # Download media if available
        media_path = None
        if message.media:
            media_path = await message.download_media()

        # Extract metadata
        metadata = extract_metadata(message)

        # Store message in MongoDB
        store_message_in_db(cleaned_text, media_path, metadata)

def store_message_in_db(content, media_path, metadata):
    """
    Store preprocessed message data in MongoDB.
    """
    message_document = {
        "content": content,
        "media": media_path,
        "metadata": metadata
    }
    collection.insert_one(message_document)

# --- Main Execution ---

async def main():
    """
    Main function to fetch and process messages from multiple channels.
    """
    channels = [
        'ZemenExpress', 'sinayelj', 'MerttEka', 'yebatochmregagroup', 
        'helloomarketethiopia', 'Leyueqa', 'kstoreaddis', 'Fashiontera'
    ]
    
    for channel_name in channels:
        await fetch_messages(channel_name)

# Run the main function
with client:
    client.loop.run_until_complete(main())
