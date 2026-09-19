# AROHA & Bioneer: Master System Supervisor Harness
import subprocess
import sys

def verify_environment():
    print("[Supervisor] Running system environment health check...")
    print(f"  -> Python Executable: {sys.executable}")
    print(f"  -> Python Version: {sys.version.split()[0]}")
    try:
        import pyperclip
        print("  -> Clipboard Agent Dependency (pyperclip): OK")
    except ImportError:
        print("  -> WARNING: pyperclip not found. Run 'pip install pyperclip'")

if __name__ == "__main__":
    verify_environment()