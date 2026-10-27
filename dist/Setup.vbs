' =======================================================================
' AGENT PRAYATH v2.0 - ONE-CLICK ZERO-WARNING INSTALLER LAUNCHER
' Double-clicking this VBS script bypasses Windows SmartScreen warnings
' and immediately launches the verified installer with system elevation.
' =======================================================================

Set WshShell = CreateObject("WScript.Shell")
Set fso = CreateObject("Scripting.FileSystemObject")
currentDir = fso.GetParentFolderName(WScript.ScriptFullName)

' 1. Silently remove Windows Download Quarantine (Mark of the Web) from all files
unblockCmd = "powershell -NoProfile -ExecutionPolicy Bypass -Command ""Get-ChildItem -Path '" & currentDir & "' -Recurse | Unblock-File -ErrorAction SilentlyContinue"""
WshShell.Run unblockCmd, 0, True

' 2. Elevate and launch Install_AgentPrayath.bat
batPath = currentDir & "\Install_AgentPrayath.bat"

If fso.FileExists(batPath) Then
    Set objShell = CreateObject("Shell.Application")
    objShell.ShellExecute batPath, "", currentDir, "runas", 1
Else
    WScript.Echo "Error: Install_AgentPrayath.bat not found in " & currentDir
End If
