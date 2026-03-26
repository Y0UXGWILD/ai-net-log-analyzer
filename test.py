import os
from dotenv import load_dotenv

# This tells Python: "Look for .env in the SAME folder as this script"
current_dir = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(current_dir, ".env")

print(f"[*] Searching for .env at: {env_path}")

if os.path.exists(env_path):
    load_dotenv(env_path)
    token = os.getenv('TELEGRAM_TOKEN')
    chat_id = os.getenv('TELEGRAM_CHAT_ID')
    
    if token and chat_id:
        print(f"✅ SUCCESS! Token found: {token[:10]}...")
        print(f"✅ SUCCESS! Chat ID found: {chat_id}")
    else:
        print("❌ FAILED: File exists, but TELEGRAM_TOKEN or TELEGRAM_CHAT_ID is missing inside it.")
        print("Check your .env file content. It should look like: TELEGRAM_TOKEN=123:ABC")
else:
    print("❌ FAILED: The .env file does not exist in this folder.")
    print(f"Files I actually see here: {os.listdir(current_dir)}")