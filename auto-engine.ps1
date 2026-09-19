Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "   COSMIC RESONATOR AUTOMATION ENGINE     " -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan

while ($true) {
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Write-Host "[$timestamp] [+] Triggering scheduled resonator cycle..." -ForegroundColor Yellow
    
    # Execute the master resonator cycle as a module
    python -m modules.resonator.run_resonator
    
    Write-Host "[-] Cycle complete. Waiting for next interval..." -ForegroundColor DarkGray
    
    # Interval delay between automated pulses (adjust seconds as needed)
    Start-Sleep -Seconds 60
}
