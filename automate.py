def initialize_system():
    \"\"\"Core execution entry point.\"\"\"
    return True

if __name__ == '__main__':
    print('System initialized:', initialize_system())
"| Out-File -Encoding utf8 src\core.py

# Create corresponding unit test
@"
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from core import initialize_system

def test_initialize_system():
    assert initialize_system() is True
"| Out-File -Encoding utf8 tests\test_core.py

Write-Host "==> Core modules and test suites populated."
.\run.ps1
# Fix nested directory path if needed and update automation script to use python module execution for pytest
Set-Location "C:\Users\terry\project-core\project-core"

# Update automate.py to use python -m pytest to avoid path/executable resolution issues
@"
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
