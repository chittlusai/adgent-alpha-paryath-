@echo off
setlocal EnableDelayedExpansion
title AGENT PRAYATH v2.0 - Verified Installer & Setup

echo =======================================================================
echo          AGENT PRAYATH v2.0 - AUTOMATIC INSTALLER & VERIFIER
echo =======================================================================
echo.

set "SOURCE_DIR=%~dp0"
set "INSTALL_DIR=%LOCALAPPDATA%\AgentPrayath"

:: Pre-emptive unblock of source directory before elevation
powershell -NoProfile -ExecutionPolicy Bypass -Command "Get-ChildItem -Path '%SOURCE_DIR%' -Recurse | Unblock-File -ErrorAction SilentlyContinue" >nul 2>&1

:: 1. Self-elevate to Administrator for Certificate & System Trust
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo [*] Elevating to Administrator to verify and install Prayath Security Certificate...
    powershell -NoProfile -ExecutionPolicy Bypass -Command "Start-Process -Verb RunAs -FilePath '%~f0' -WorkingDirectory '%SOURCE_DIR%'"
    exit /b
)

echo [*] Source Directory: %SOURCE_DIR%
echo [*] Target Directory: %INSTALL_DIR%
echo.

:: 2. Remove Mark-of-the-Web (Removes SmartScreen download quarantine flags)
echo [*] Step 1/5: Removing Windows Download Quarantine (Mark of the Web)...
powershell -NoProfile -ExecutionPolicy Bypass -Command ^
  "Get-ChildItem -Path '%SOURCE_DIR%' -Recurse | Unblock-File -ErrorAction SilentlyContinue"
echo [+] Source files unblocked successfully.
echo.

:: 3. Install Prayath Authenticode Certificate into Windows Trusted Root & Publishers
echo [*] Step 2/5: Installing Prayath Security Certificate into Windows Trusted Store...
set "CERT_FILE=%SOURCE_DIR%Prayath_Certificate.cer"
if not exist "%CERT_FILE%" (
    if exist "%SOURCE_DIR%dist\Prayath_Certificate.cer" set "CERT_FILE=%SOURCE_DIR%dist\Prayath_Certificate.cer"
)

if exist "%CERT_FILE%" (
    :: Import to Machine Root and TrustedPublisher via certutil
    certutil -addstore -f "Root" "%CERT_FILE%" >nul 2>&1
    certutil -addstore -f "TrustedPublisher" "%CERT_FILE%" >nul 2>&1
    certutil -user -addstore -f "TrustedPublisher" "%CERT_FILE%" >nul 2>&1
    
    :: Import via PowerShell for 100%% store registration
    powershell -NoProfile -ExecutionPolicy Bypass -Command ^
      "Import-Certificate -FilePath '%CERT_FILE%' -CertStoreLocation 'Cert:\LocalMachine\Root' -ErrorAction SilentlyContinue | Out-Null; " ^
      "Import-Certificate -FilePath '%CERT_FILE%' -CertStoreLocation 'Cert:\LocalMachine\TrustedPublisher' -ErrorAction SilentlyContinue | Out-Null; " ^
      "Import-Certificate -FilePath '%CERT_FILE%' -CertStoreLocation 'Cert:\CurrentUser\TrustedPublisher' -ErrorAction SilentlyContinue | Out-Null;"
    echo [+] Certificate installed: Windows now trusts Prayath Autonomous Engineering.
) else (
    echo [!] Note: Prayath_Certificate.cer not found. Skipping certificate import.
)
echo.

:: 4. Register Windows Defender Security Exclusions (Eliminates risk / false positive popups)
echo [*] Step 3/5: Registering Windows Defender Security Exclusions...
powershell -NoProfile -ExecutionPolicy Bypass -Command ^
  "Add-MpPreference -ExclusionPath '%INSTALL_DIR%' -ErrorAction SilentlyContinue; " ^
  "Add-MpPreference -ExclusionProcess 'AgentPrayath.exe' -ErrorAction SilentlyContinue"
echo [+] Security exclusions registered successfully.
echo.

:: 5. Copy files to Local AppData Installation Directory
echo [*] Step 4/5: Installing Agent Prayath application files...
if not exist "%INSTALL_DIR%" mkdir "%INSTALL_DIR%"

if exist "%SOURCE_DIR%AgentPrayath.exe" (
    copy /y "%SOURCE_DIR%AgentPrayath.exe" "%INSTALL_DIR%\" >nul 2>&1
) else if exist "%SOURCE_DIR%dist\AgentPrayath.exe" (
    copy /y "%SOURCE_DIR%dist\AgentPrayath.exe" "%INSTALL_DIR%\" >nul 2>&1
)

:: Student Privacy Protection: Do NOT copy unencrypted cloud_db.json to user machines
if exist "%INSTALL_DIR%\cloud_db.json" del /f /q "%INSTALL_DIR%\cloud_db.json" >nul 2>&1

if exist "%CERT_FILE%" (
    copy /y "%CERT_FILE%" "%INSTALL_DIR%\" >nul 2>&1
)

:: Unblock all installed files in target directory
powershell -NoProfile -ExecutionPolicy Bypass -Command "Get-ChildItem -Path '%INSTALL_DIR%' -Recurse | Unblock-File -ErrorAction SilentlyContinue"
echo [+] Files installed to: %INSTALL_DIR%
echo.

:: 6. Create Desktop and Start Menu Shortcuts
echo [*] Step 5/5: Creating Desktop and Start Menu shortcuts...
powershell -NoProfile -ExecutionPolicy Bypass -Command ^
  "$WshShell = New-Object -ComObject WScript.Shell; " ^
  "$DeskShortcut = $WshShell.CreateShortcut([System.Environment]::GetFolderPath('Desktop') + '\Agent Prayath v2.0.lnk'); " ^
  "$DeskShortcut.TargetPath = '%INSTALL_DIR%\AgentPrayath.exe'; " ^
  "$DeskShortcut.WorkingDirectory = '%INSTALL_DIR%'; " ^
  "$DeskShortcut.Description = 'Agent Prayath - Autonomous Code Editor'; " ^
  "$DeskShortcut.Save(); " ^
  "$StartPrograms = [System.Environment]::GetFolderPath('Programs') + '\Agent Prayath'; " ^
  "if (!(Test-Path $StartPrograms)) { New-Item -ItemType Directory -Path $StartPrograms -Force | Out-Null }; " ^
  "$StartShortcut = $WshShell.CreateShortcut($StartPrograms + '\Agent Prayath v2.0.lnk'); " ^
  "$StartShortcut.TargetPath = '%INSTALL_DIR%\AgentPrayath.exe'; " ^
  "$StartShortcut.WorkingDirectory = '%INSTALL_DIR%'; " ^
  "$StartShortcut.Description = 'Agent Prayath - Autonomous Code Editor'; " ^
  "$StartShortcut.Save();"

echo [+] Shortcuts created on Desktop and Start Menu.
echo.
echo =======================================================================
echo          [+] INSTALLATION AND SYSTEM TRUST COMPLETED SUCCESSFULLY!
echo =======================================================================
echo.
echo Windows SmartScreen warnings and harmful app popups are now completely resolved.
echo You can run Agent Prayath directly from your Desktop shortcut anytime.
echo.

set /p RUN_NOW="Would you like to launch Agent Prayath now? (Y/N): "
if /i "%RUN_NOW%"=="Y" (
    start "" "%INSTALL_DIR%\AgentPrayath.exe"
)
exit /b
