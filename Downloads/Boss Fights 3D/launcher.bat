@echo off
:: this script updates the launcher
:: main launcher script download (direct):  https://drive.google.com/uc?export=download&confirm=yTib&id=1JsiSP4n3ssFd5meBzBWu4UywJbWdT4ey
:: launcher version download (direct):  https://drive.google.com/uc?export=download&confirm=yTib&id=1VNYeS3w6PyKPzLYHO4T3dajGAglyry2W
call:CreateDirs
call:GetVersions


:CreateDirs
if not exist "Data" mkdir "Data"
if not exist "Data/Game" mkdir "Data/Game"
goto:eof

:GetVersions
if exist "Data/launcherVersion.txt" (
set /p storedLauncherVersion=<"Data/launcherVersion.txt"
) else (
set storedLauncherVersion=0
)
echo Stored version: %storedLauncherVersion%
echo Checking online version
cd wget
wget --no-check-certificate -q --show-progress -O "../Data/launcherVersion.txt" "https://drive.google.com/uc?export=download&confirm=yTib&id=1VNYeS3w6PyKPzLYHO4T3dajGAglyry2W"
cd ..
set /p onlineLauncherVersion=<"Data/launcherVersion.txt"
echo Online version: %onlineLauncherVersion%
if not %storedLauncherVersion% == %onlineLauncherVersion% (
echo Updating launcher script
cd wget
wget --no-check-certificate -q --show-progress -O "../main.bat" "https://drive.google.com/uc?export=download&confirm=yTib&id=1JsiSP4n3ssFd5meBzBWu4UywJbWdT4ey"
cd ..
)
echo Running launcher
call main.bat
goto:eof

