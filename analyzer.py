import os
import requests
from dotenv import load_dotenv

# 1. Load the credentials from the .env in the same folder
current_dir = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(current_dir, ".env"))

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_telegram_alert(message):
    """Sends a real-time message to your Telegram app"""
    if not TOKEN or not CHAT_ID:
        print("[!] Error: Credentials missing. Automation will continue without alerts.")
        return

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID, 
        "text": f"🚨 **NET-AI ALERT** 🚨\n\n{message}"
    }
    
    try:
        requests.post(url, json=payload)
        print("[+] Telegram alert sent to your phone!")
    except Exception as e:
        print(f"[#] Telegram Error: {e}")

# --- Example of how to use it in your code ---
if __name__ == "__main__":
    print("--- NetAI Monitoring System Active ---")
    
    # Simulate a network error detection
    error_detected = "Interface GigabitEthernet0/1 is DOWN (Line protocol flap)"
    
    print(f"[*] Detected: {error_detected}")
    send_telegram_alert(error_detected)