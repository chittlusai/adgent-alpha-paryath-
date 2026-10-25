# 🚀 AGENT PRAYATH v2.0 - Automatic Code Editor

> Autonomous Human-Cadence Code Injector & Engineering Assistant

**AGENT PRAYATH** is an autonomous desktop engineering assistant engineered to bypass online testing clipboard blockers, auto-generate code from screenshots or prompts using AI, and inject code directly into code editors.

---

## 🌟 Key Features

- 🔥 **Firebase Realtime Cloud Database**: Securely connected to Google Firebase Realtime Database for all user authentication, profiles, and password updates.
- ⚡ **Cyberpunk Boot Intro**: Dynamic welcome animation with typewriter text, boot stream telemetry, and progress bar.
- 🟢 **Live User Presence Telemetry (Admin Only)**: Real-time dashboard showing all active users online, last ping, role, and branch.
- 🛡️ **Zero-Bypass Keystroke Typing Engine**: Injects code using hardware-level simulated keystrokes, completely bypassing browser and IDE paste blockers.
- 🌐 **Multi-Language Support**: Python, C++, Java, JavaScript, C, SQL, Rust, Go.

---

## 💻 How to Run & Install

### 1. Verified One-Click Installer (Recommended for All Users)
Run the automated installer inside the `dist` folder:
```cmd
dist\Install_AgentPrayath.bat
```
* **Bypasses Windows SmartScreen**: Automatically strips download quarantine flags (`Zone.Identifier`).
* **Registers Digital Security Certificate**: Installs the Prayath Authenticode certificate to Windows Trusted Publishers so the publisher is recognized as verified.
* **Creates Desktop & Start Menu Shortcuts**: Ready to launch in one click with zero warnings.

### 2. Instant Portable Launcher (No Installation)
If running directly from the unzipped folder without full installation:
```cmd
dist\Unblock_And_Run.bat
```
or double-click `dist\AgentPrayath.exe`.
*(If Windows SmartScreen displays "Windows protected your PC", click **More info** -> **Run anyway**, or use `Unblock_And_Run.bat` to eliminate the popup).*

### 3. Developer Launch (Python Source)
Run via Command Prompt:
```cmd
launch.bat
```
or PowerShell:
```powershell
powershell -ExecutionPolicy Bypass -File .\launch.ps1
```

---

## 📦 Requirements (If running via Python)
- Python 3.10+
- `customtkinter`
- `pynput`
- `Pillow`
- `google-genai`
