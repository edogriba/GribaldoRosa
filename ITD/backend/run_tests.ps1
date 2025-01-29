# Save the current content of the .env file
$envFile = ".env"
$backupFile = ".env.bak"

# Backup the .env file
Copy-Item -Path $envFile -Destination $backupFile

# Replace DATABASE path in the .env file
(Get-Content $envFile) -replace 'DATABASE = app/db/SC.db', 'DATABASE = app/db/test1_SC.db' | Set-Content $envFile
(Get-Content $envFile) -replace 'DEBUG = True', 'DEBUG = False' | Set-Content $envFile

# Run the tests
python -m unittest discover -s .

# Restore the original .env file
Move-Item -Path $backupFile -Destination $envFile -Force