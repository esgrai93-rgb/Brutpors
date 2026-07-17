import time
import requests

# Configuration placeholders
URL = "https://checkton.online/backend/spam"
API_KEY = "qxy9l0lOhwTFwgCukA66O8KW4tYUeYYXyXObMvuBEH8"
DEVICE_ID = "and_cd9e459ea708a948d5c2f5a6ca8838cfa40a0e4a87b12e8ca93fbfc5-2518-47f9-965d-bd99221f9cc2"

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
