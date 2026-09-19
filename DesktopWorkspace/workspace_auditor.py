# AROHA & Bioneer: Workspace Health & Integrity Auditor
import os

def audit_workspace():
    print("[Auditor] Scanning local workspace structure...")
    expected_dirs = ["modules", "configs", "docs"]
    for d in expected_dirs:
        exists = os.path.exists(d)
        status = "FOUND" if exists else "MISSING"
        print(f"  -> Directory '{d}': {status}")

if __name__ == "__main__":
    audit_workspace()