import re
import json
import os
import pandas as pd

def amharic_tokenize(text):
    return text.split()

def normalize_amharic(text):
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def preprocess_message(msg):
    text = msg.get('text', '')
    norm_text = normalize_amharic(text)
    tokens = amharic_tokenize(norm_text)
    return {
        'id': msg['id'],
        'date': msg['date'],
        'sender_id': msg['sender_id'],
        'views': msg.get('views'),
        'tokens': tokens,
        'text': norm_text,
        'media_path': msg.get('media_path')
    }

def process_channel_file(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        messages = json.load(f)
    processed = [preprocess_message(msg) for msg in messages if msg.get('text')]
    df = pd.DataFrame(processed)
    df.to_csv(output_path, index=False, encoding='utf-8')
    print(f"Processed data saved to {output_path}")

if __name__ == "__main__":
    raw_dir = 'data/raw'
    processed_dir = 'data/processed'
    os.makedirs(processed_dir, exist_ok=True)
    for fname in os.listdir(raw_dir):
        if fname.endswith('_messages.json'):
            input_path = os.path.join(raw_dir, fname)
            output_path = os.path.join(processed_dir, fname.replace('.json', '.csv'))
            process_channel_file(input_path, output_path) 