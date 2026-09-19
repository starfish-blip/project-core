# Project Bioneer: Local Execution & Monitoring Harness
import os
import sys

def initialize_bioneer_node():
    print("[Bioneer Node] Initializing serverless structural repository...")
    workspace_path = os.path.dirname(os.path.abspath(__file__))
    print(f"[Bioneer Node] Active directory locked to: {workspace_path}")
    
    # Verify core atlas integration
    atlas_file = os.path.join(workspace_path, "aroha_core_atlas.md")
    if os.path.exists(atlas_file):
        print("[Bioneer Node] AROHA Core Atlas verified in workspace.")
    else:
        print("[Bioneer Node] Warning: Core Atlas file not found. Run sync.")

if __name__ == "__main__":
    initialize_bioneer_node()