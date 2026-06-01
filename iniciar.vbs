Set oShell = WScript.CreateObject("WScript.Shell")
Set oFSO = CreateObject("Scripting.FileSystemObject")

Dim sDir
sDir = oFSO.GetParentFolderName(WScript.ScriptFullName)

' Criar pasta de logs se nao existir
If Not oFSO.FolderExists(sDir & "\logs") Then
    oFSO.CreateFolder(sDir & "\logs")
End If

' Verificar se o servidor ja esta rodando na porta 5000
Dim oExec, sOutput
Set oExec = oShell.Exec("cmd /c netstat -an 2>nul")
sOutput = oExec.StdOut.ReadAll()

If InStr(sOutput, ":5000 ") > 0 Or InStr(sOutput, ":5000") > 0 Then
    ' Servidor ja esta rodando, apenas abrir o navegador
    oShell.Run "http://localhost:5000/gerenciar"
    WScript.Quit
End If

' Iniciar servidor Flask sem janela (modo silencioso)
' PYTHONPATH necessario pois a instalacao do Python esta dividida em dois diretorios
Dim sLogPath
sLogPath = sDir & "\logs\app.log"
oShell.Environment("Process")("PYTHONPATH") = "C:\Users\joaop\AppData\Local\Programs\Python\Python314\Lib\site-packages"
oShell.Run "cmd /c cd /d """ & sDir & """ && C:\Python314\python.exe app.py >> """ & sLogPath & """ 2>&1", 0, False

' Aguardar o servidor subir
WScript.Sleep 3000

' Abrir navegador na pagina de gerenciamento
oShell.Run "http://localhost:5000/gerenciar"
