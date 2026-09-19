import json
import os

def view_telemetry():
    log_path = "logs/resonator.json"
    if not os.path.exists(log_path):
        print("[-] No telemetry logs found yet.")
        return
    
    print("=== COSMIC RESONATOR TELEMETRY LOGS ===")
    with open(log_path, "r") as f:
        for line in f:
            try:
                record = json.loads(line.strip())
                print(f"[{record.get('timestamp')}] Base: {record.get('base_freq')} Hz | Multiplier: {record.get('multiplier')} | Note: {record.get('note')}")
            except Exception:
                pass
    print("=======================================")

if __name__ == "__main__":
    view_telemetry()
