# AROHA & Bioneer: Master Framework Indexer & Inventory Generator
import os
import json

def generate_framework_index():
    print("[Indexer] Scanning AROHA-Core structural hierarchy...")
    inventory = {"modules": [], "configs": [], "docs": []}
    
    for category in inventory.keys():
        if os.path.exists(category):
            inventory[category] = os.listdir(category)
            print(f"  -> Indexed [{category}]: {len(inventory[category])} items found.")
            
    with open("framework_index.json", "w", encoding="utf-8") as f:
        json.dump(inventory, f, indent=4)
    print("[Indexer] Framework index snapshot saved to 'framework_index.json'.")

if __name__ == "__main__":
    generate_framework_index()