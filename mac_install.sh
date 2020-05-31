user=$(id -un)
mkdir /home/"$user"/KShell
sudo pip3 install pyinstaller
pyinstaller kshell.py
mv * /home/"$user"/KShell
echo "Successfully moved files to directory /home/$user/KShell/"
cd /home/"$user"/KShell
echo "You are now in the home directory of your KShell application!"
echo "export PATH=/home/$user/KShell/dist/kshell:$PATH" >> ~/.profile
echo "Launching KShell... to run, use the 'kshell' command from any directory in Terminal!"
source ~/.profile
"Sourced ~/.profile, beginning to run kshell..."
kshell
