import subprocess
import sys
import os

def run_command(command):
    print(f"==> Executing: {command}")
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        print(f"Error: Command failed with exit code {result.returncode}")
        sys.exit(result.returncode)

def main():
    print("==> Initializing Local Workflow Automation...")
    if os.path.exists("requirements.txt"):
        run_command(f"{sys.executable} -m pip install --upgrade -r requirements.txt")
    if os.path.exists("tests"):
        run_command(f"{sys.executable} -m pytest -v")
    else:
        print("==> Environment verified successfully.")

if __name__ == "__main__":
    main()
