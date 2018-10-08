
Remove-Item -r out
pelican content
Start-Process -FilePath "powershell" -ArgumentList "-File runserver.ps1"