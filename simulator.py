import requests
import time
import random
from datetime import datetime

URL = "http://127.0.0.1:8000/api/biometrics"

print("🚀 VitalGuard Data Simulator Started")
print("Sending fake biometric data every 5 seconds...\n")

try:
    while True:
        # Generate realistic fake data
        heart_rate = random.randint(65, 105)   # Normal range with some variation
        spo2 = random.randint(95, 99)          # Normal SpO2
        respiration_rate = random.randint(14, 20)

        # Occasionally create abnormal data (for testing anomaly later)
        if random.random() < 0.15:  # 15% chance of abnormal reading
            heart_rate = random.choice([45, 48, 120, 135])
            spo2 = random.randint(88, 93)

        payload = {
            "heart_rate": heart_rate,
            "spo2": spo2,
            "respiration_rate": respiration_rate
        }

        try:
            response = requests.post(URL, json=payload, timeout=5)
            if response.status_code == 200:
                data = response.json()
                print(f"✅ Sent at {datetime.now().strftime('%H:%M:%S')} | "
                      f"HR: {heart_rate} | SpO2: {spo2}% | Resp: {respiration_rate}")
            else:
                print(f"❌ Error: {response.status_code}")
        except Exception as e:
            print(f"❌ Connection error: {e}")

        time.sleep(5)   # Send data every 5 seconds

except KeyboardInterrupt:
    print("\n\n🛑 Simulator stopped by user.")