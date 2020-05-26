Set oShell = CreateObject ("Wscript.Shell") 
Dim strArgs
strArgs = "cmd /c clipboardscript.bat"
oShell.Run strArgs, 0, false