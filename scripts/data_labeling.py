import pandas as pd
import re

# Load the scraped data from the CSV file
# Replace 'scraped_data.csv' with the actual path to your CSV file
df = pd.read_csv('telegram_scraped_data.csv')

# Function to preprocess and tokenize the text
def preprocess_text(text):
    # Convert non-string values to empty strings
    if not isinstance(text, str):
        text = ''
    
    # Tokenize and keep Amharic letters (U+1200 to U+137F), English letters, and numbers only
    tokens = re.findall(r'[ሀ-፿a-zA-Z0-9]+', text)
    return tokens


# Function to manually label tokens
def label_tokens(tokens):
    labeled_tokens = []
    
    print("Please label each token (B-Product, I-Product, B-LOC, I-LOC, B-PRICE, I-PRICE, O):")
    
    for token in tokens:
        print(f"Token: {token}")
        entity_label = input("Enter the label (B-Product, I-Product, B-LOC, I-LOC, B-PRICE, I-PRICE, O): ")
        labeled_tokens.append((token, entity_label))
    
    return labeled_tokens

# Function to save in CoNLL format
def save_to_conll_format(labeled_data, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        for message in labeled_data:
            for token, label in message:
                file.write(f"{token} {label}\n")
            file.write("\n")  # Blank line to separate messages

# Main process
labeled_dataset = []

# Iterate through each row in the DataFrame
for index, row in df.iterrows():
    message_text = row['Message Text']  # Use the correct column name
    tokens = preprocess_text(message_text)
    labeled_tokens = label_tokens(tokens)
    labeled_dataset.append(labeled_tokens)

# Save the labeled data to a CoNLL format file
save_to_conll_format(labeled_dataset, "labeled_dataset.conll")

print("Labeled data has been saved to labeled_dataset.conll")
