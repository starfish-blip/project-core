import json, os
from datetime import datetime

LOG_FILE = 'logs/resonator.json'

def log_event(e, d):
    os.makedirs('logs', exist_ok=True)
    logs = json.load(open(LOG_FILE)) if os.path.exists(LOG_FILE) else []
    logs.append({'timestamp': datetime.utcnow().isoformat(), 'event_type': e, 'details': d})
    json.dump(logs, open(LOG_FILE, 'w'), indent=4)
