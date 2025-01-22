from telethon import TelegramClient
from telethon.tl.types import MessageMediaPhoto, MessageMediaDocument, DocumentAttributeFilename
import pandas as pd
import re
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

api_id = os.getenv('api_id')
api_hash = os.getenv('api_hash')
phone_number = os.getenv('phone_number')
channel_usernames = [
        'ZemenExpress', 'sinayelj', 'MerttEka', 'yebatochmregagroup', 
        'helloomarketethiopia', 'Leyueqa', 'kstoreaddis', 'Fashiontera'
    ] 

# Initialize the client
client = TelegramClient('session_name', api_id, api_hash)

# Create a list to hold the dataset
data = []


def preprocess_text(text):
    # Keep only Amharic letters (Unicode range for Amharic is 0x1200 - 0x137F) and numbers
    text = re.sub(r'[^\u1200-\u137F0-9 ]+', '', text)  # Keep Amharic letters and numbers
    tokens = text.split()  # Tokenize by spaces
    return tokens

# Function to scrape data from Telegram and store in a dataset
async def scrape_telegram_data():
    for channel_username in channel_usernames:
        channel = await client.get_entity(channel_username)
        
        async for message in client.iter_messages(channel):
            message_text = message.text or ""
            media_type = None
            media_path = None

            if message.media:
                media_type = type(message.media).__name__

                if isinstance(message.media, MessageMediaDocument):
                    document = message.media.document
                    media_path = next((attr.file_name for attr in document.attributes if isinstance(attr, DocumentAttributeFilename)), "No file name")
                elif isinstance(message.media, MessageMediaPhoto):
                    media_path = "Photo not saved"  
                else:
                    media_path = "Other media type"

            # Preprocess the message text
            tokens = preprocess_text(message_text)

            # Append the data to the list
            data.append({
                "Message Text": " ".join(tokens),  # Join tokens back to string if needed
                "Media Type": media_type,
                "Media Path": media_path,
                "Timestamp": message.date
            })

    # Convert the list into a DataFrame
    df = pd.DataFrame(data)

    # Save the DataFrame to a CSV file
    df.to_csv('telegram_scraped_data.csv', index=False)
    print("Data has been saved to telegram_scraped_data.csv")

# Authenticate and scrape data
with client:
    client.loop.run_until_complete(scrape_telegram_data())
