Write-Output "removing output folder.."
Remove-Item -Recurse  output
Write-Output "Building.."
pelican content
Write-Output "Pelican server started.."
Set-Location output
python -m pelican.server