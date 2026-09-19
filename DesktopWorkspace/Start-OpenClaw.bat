@echo off
start cmd /k "openclaw gateway run"
timeout /t 60
start cmd /k "openclaw dashboard"
