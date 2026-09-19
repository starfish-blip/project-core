# Project Bioneer: Local State Persistence Manager
import json
import os

class BioneerStateManager:
    def __init__(self, state_file="bioneer_state.json"):
        self.state_file = state_file

    def save_state(self, state_data):
        with open(self.state_file, "w", encoding="utf-8") as f:
            json.dump(state_data, f, indent=4)
        print(f"[State Manager] State successfully persisted to {self.state_file}")

    def load_state(self):
        if os.path.exists(self.state_file):
            with open(self.state_file, "r", encoding="utf-8") as f:
                return json.load(f)
        return {"status": "No existing state found."}

if __name__ == "__main__":
    mgr = BioneerStateManager()
    mgr.save_state({"active_atlas": "AROHA 3-Zone", "sync_status": "Clean"})
    print("Loaded State:", mgr.load_state())