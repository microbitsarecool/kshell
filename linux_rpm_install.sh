mkdir /home/"$USER"/KShell
sudo dnf install python3
sudo dnf install python3-tk
sudo dnf install python3-pip
pip3 install pyinstaller
pyinstaller kshell_base.py
mv * /home/"$USER"/KShell
echo "Successfully moved files to directory /home/$USER/KShell/"
cd /home/"$USER"/KShell/
echo "You are now in the home directory of your KShell application!"
echo "export PATH=/home/$USER/KShell/dist/kshell_base:$PATH" >> ~/.bashrc
echo "Launching KShell... to run, use the 'kshell_base' command from any directory in Terminal!"
kshell_base