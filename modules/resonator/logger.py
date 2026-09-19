import json, os
from datetime import datetime

LOG_FILE = 'logs/resonator.json'

def log_event(e, d):
    os.makedirs('logs', exist_ok=True)
    logs = []
    if os.path.exists(LOG_FILE) and os.path.getsize(LOG_FILE) > 0:
        try:
            logs = json.load(open(LOG_FILE))
        except json.JSONDecodeError:
            logs = []
    logs.append({'timestamp': datetime.utcnow().isoformat(), 'event_type': e, 'details': d})
    json.dump(logs, open(LOG_FILE, 'w'), indent=4)
