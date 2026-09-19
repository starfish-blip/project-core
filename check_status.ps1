Clear-Host
Write-Host '==========================================' -ForegroundColor Yellow
Write-Host '       SYSTEM HEALTH & PROCESS AUDIT      ' -ForegroundColor Yellow
Write-Host '==========================================' -ForegroundColor Yellow
$python = Get-Process python -ErrorAction SilentlyContinue
if ($python) { Write-Host '[+] Python Active: ' $python.Count 'instance(s)' -ForegroundColor Green } else { Write-Host '[-] Python Inactive' -ForegroundColor Red }
$node = Get-Process node -ErrorAction SilentlyContinue
if ($node) { Write-Host '[+] Node Active: ' $node.Count 'instance(s)' -ForegroundColor Green } else { Write-Host '[-] Node Inactive' -ForegroundColor Yellow }
Write-Host '==========================================' -ForegroundColor Yellow
