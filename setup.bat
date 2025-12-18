@echo off
echo updating pip...
python.exe -m pip install --upgrade pip
echo pip updated.
echo Installing Python modules...
pip install pillow
pip install rich
echo Module installation complete.
pause
