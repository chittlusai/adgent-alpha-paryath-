@echo off
title AGENT PRAYATH v2.0 - Quick Launcher
echo ========================================================
echo       AGENT PRAYATH v2.0 - SECURE INSTANT LAUNCHER
echo ========================================================
echo [*] Removing Windows Download Quarantine (Zone.Identifier)...
powershell -NoProfile -ExecutionPolicy Bypass -Command "Get-ChildItem -Path '%~dp0' -Recurse | Unblock-File -ErrorAction SilentlyContinue"
echo [+] Verified safe. Launching Agent Prayath...

if exist "%~dp0AgentPrayath.exe" (
    start "" "%~dp0AgentPrayath.exe"
) else if exist "%~dp0dist\AgentPrayath.exe" (
    start "" "%~dp0dist\AgentPrayath.exe"
) else (
    echo [!] AgentPrayath.exe not found!
    pause
)
exit
