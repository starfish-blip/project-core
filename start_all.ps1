Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "     STARTING ALL PROJECT SERVICES        " -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan

# 1. Start Hermes / Backend API
Write-Host "[+] Starting Hermes Backend API..." -ForegroundColor Yellow
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd C:\Users\terry\project-core\project-core; python api.py"

# 2. Start Node.js / OpenClaw (adjust path/command if your node app has a specific entry point)
Write-Host "[+] Starting Node.js / OpenClaw..." -ForegroundColor Yellow
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd C:\Users\terry\project-core\project-core; node index.js"

# 3. Start Automation Engine
Write-Host "[+] Starting Automation Engine..." -ForegroundColor Yellow
Start-Process powershell -ArgumentList "-NoExit", "-File", "C:\Users\terry\project-core\project-core\auto-engine.ps1"

Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "All core services initiated!" -ForegroundColor Green
