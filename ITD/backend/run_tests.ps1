# Save the current content of the .env file
$envFile = "C:\Users\Utente\OneDrive\Desktop\SE2_Project\GribaldoRosa\ITD\backend\.env"
$backupFile = "C:\Users\Utente\OneDrive\Desktop\SE2_Project\GribaldoRosa\ITD\backend\.env.bak"

# Backup the .env file
Copy-Item -Path $envFile -Destination $backupFile

# Replace DATABASE path in the .env file
(Get-Content $envFile) -replace 'DATABASE = app/db/SC.db', 'DATABASE = app/db/test1_SC.db' | Set-Content $envFile

# Run the tests
python -m unittest discover -s .

# Restore the original .env file
Move-Item -Path $backupFile -Destination $envFile -Force