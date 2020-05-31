mkdir c:\Users\%username%\KShell
pip install pyinstaller
pyinstaller kshell.py
move * c:\Users\%username%\KShell
echo "Successfully installed in your home directory (C:\Users\[user]\KShell)!"
cd c:\Users\%username%\KShell
echo "You are in the home directory of KShell! Do not move it or its files."
echo "You can add it to your path environment to enable KShell access from anywhere."
echo "If you don't, you have to go to this directory: C:\Users\<user>\KShell\dist\kshell"
echo "Then run 'kshell.exe'"
echo "If you do add it, add the said directory: C:\Users\<user>\KShell\dist\kshell"
echo "Have fun!"
