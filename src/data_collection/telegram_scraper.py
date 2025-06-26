import os
import json
from telethon.sync import TelegramClient

API_ID = 'YOUR_API_ID'
API_HASH = 'YOUR_API_HASH'
SESSION_NAME = 'amharic_ecommerce'
CHANNELS = [
    'https://t.me/ethio_mart',
    # Add at least 5 channels
]

OUTPUT_DIR = 'data/raw'
os.makedirs(OUTPUT_DIR, exist_ok=True)

def download_media(message, output_dir):
    if message.media:
        file_path = message.download_media(file=output_dir)
        return file_path
    return None

def main():
    with TelegramClient(SESSION_NAME, API_ID, API_HASH) as client:
        for channel in CHANNELS:
            print(f"Fetching messages from {channel}")
            all_messages = []
            for message in client.iter_messages(channel, limit=1000):
                msg_data = {
                    'id': message.id,
                    'date': str(message.date),
                    'sender_id': getattr(message.sender_id, 'user_id', None),
                    'text': message.text,
                    'views': message.views,
                    'media_path': None,
                }
                if message.media:
                    media_path = download_media(message, OUTPUT_DIR)
                    msg_data['media_path'] = media_path
                all_messages.append(msg_data)
            channel_name = channel.split('/')[-1]
            with open(os.path.join(OUTPUT_DIR, f'{channel_name}_messages.json'), 'w', encoding='utf-8') as f:
                json.dump(all_messages, f, ensure_ascii=False, indent=2)
            print(f"Saved {len(all_messages)} messages from {channel}")

if __name__ == "__main__":
    main() 