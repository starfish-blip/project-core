import json
import os
from datetime import datetime

class ResonatorLogger:
    def __init__(self, log_dir="logs", log_file="resonator.json"):
        self.log_dir = log_dir
        self.log_path = os.path.join(log_dir, log_file)
        
        # Ensure log directory exists
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)

    def record_frequency(self, base_freq, multiplier, note):
        record = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "base_freq": base_freq,
            "multiplier": multiplier,
            "note": note
        }
        with open(self.log_path, "a") as f:
            f.write(json.dumps(record) + "\n")
        print(f"[+] Logged telemetry: {base_freq} Hz")

if __name__ == "__main__":
    logger = ResonatorLogger()
    logger.record_frequency(272.0, 1.0, "Manual test log entry")
