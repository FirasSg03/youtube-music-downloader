@echo off
mkdir mp3_output

for %%F in (*.webm) do (
    ffmpeg -i "%%F" -vn -ab 192k -ar 44100 -y "mp3_output\%%~nF.mp3"
)

echo Conversion complete.
pause
