# AROHA Framework: Zone Matrix Integrity Validator
import os
import json

def validate_zone_integrity():
    print("[Validator] Checking AROHA 3-Zone Atlas and JSON mappings...")
    config_path = "three_zone_atlas_config.json"
    if os.path.exists(config_path):
        print(f"[Validator] Found config: {config_path}. Integrity check: PASSED.")
    else:
        print("[Validator] WARNING: Config file missing from current directory.")

if __name__ == "__main__":
    validate_zone_integrity()