Clear-Host
Write-Host "==========================================" -ForegroundColor Yellow
Write-Host "     MASTER SYSTEM HEALTH & SUITE AUDIT   " -ForegroundColor Yellow
Write-Host "==========================================" -ForegroundColor Yellow

# 1. Check Python Core / Hermes Backend
$pythonProcs = Get-WmiObject Win32_Process -Filter "Name='python.exe'" -ErrorAction SilentlyContinue
$hermesRunning = $false
foreach ($p in $pythonProcs) {
    if ($p.CommandLine -like "*hermes*" -or $p.CommandLine -like "*api.py*") {
        $hermesRunning = $true
    }
}

if ($hermesRunning) {
    Write-Host "[+] Hermes / Backend API : ONLINE" -ForegroundColor Green
} else {
    Write-Host "[-] Hermes / Backend API : OFFLINE" -ForegroundColor Red
}

# 2. Check Node.js Services (OpenClaw / Servers)
$nodeProcs = Get-Process node -ErrorAction SilentlyContinue
if ($nodeProcs) {
    Write-Host "[+] Node.js / OpenClaw    : ONLINE ($($nodeProcs.Count) instance(s))" -ForegroundColor Green
} else {
    Write-Host "[-] Node.js / OpenClaw    : OFFLINE" -ForegroundColor Red
}

# 3. Check Automated Engine Loops (PowerShell background engines)
$powershellProcs = Get-WmiObject Win32_Process -Filter "Name='powershell.exe'" -ErrorAction SilentlyContinue
$engineRunning = $false
foreach ($p in $powershellProcs) {
    if ($p.CommandLine -like "*auto-engine*" -or $p.CommandLine -like "*session-runner*") {
        $engineRunning = $true
    }
}

if ($engineRunning) {
    Write-Host "[+] Automation Engine     : RUNNING" -ForegroundColor Green
} else {
    Write-Host "[-] Automation Engine     : STOPPED" -ForegroundColor Yellow
}

Write-Host "==========================================" -ForegroundColor Yellow
