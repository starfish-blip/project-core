Write-Host "==> Restoring and launching all project services..." -ForegroundColor Cyan
if (Test-Path ".\run.ps1") {
    Start-Process powershell -ArgumentList "-NoExit", "-Command", ".\run.ps1"
}
Write-Host "==> Startup sequences completed." -ForegroundColor Cyan
