mkdir /home/$USER/KShell
sudo zypper install python3
sudo zypper install python3-tk
sudo zypper install python3-pip
pip3 install pyinstaller
pyinstaller kshell.py
mv * /home/$USER/KShell
echo "Successfully moved files to directory /home/$USER/KShell/"
cd /home/$USER/KShell/
echo "You are now in the home directory of your KShell application!"
echo "export PATH=/home/$USER/KShell/dist/kshell:$PATH" >> ~/.bashrc
echo "Launching KShell... to run, use the 'kshell' command from any directory in Terminal!"
kshell
