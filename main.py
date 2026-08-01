import time
import requests

# Configuration placeholders
URL = "https://checkton.online/backend/spam"
API_KEY = "and_cd9e459ea708a948d5c2f5a6ca8838cfd1df4dd3b4c6ab60057b62c4-f123-470f-8132-4955194b3fae"
DEVICE_ID = "and_cd9e459ea708a948d5c2f5a6ca8838cf94c7610e9c13d46bdf9be2b5-2ba1-4f28-8fa6-8616a2052f1"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36",
    "X-Api-Key": API_KEY
}

payload = {
    "device_id": DEVICE_ID,
    "server": "global"
}

print("Starting request loop. Press Ctrl+C to stop.")

while True:
    try:
        response = requests.post(URL, json=payload, headers=headers)
        print(f"Status Code: {response.status_code} | Response: {response.text}")
        
        # Pause to prevent resource exhaustion and respect rate limits
        time.sleep(1.0)
    except requests.exceptions.RequestException as e:
        print(f"Network error encountered: {e}")
        time.sleep(2.0)
