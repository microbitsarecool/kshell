mkdir /home/"$USER"/KShell/
sudo apt install python3
sudo apt install python3-tk
sudo apt install python3-pip
sudo pip3 install pyinstaller
pyinstaller kshell.py
mv * /home/"$USER"/KShell/
echo "Successfully moved files to directory /home/$USER/KShell/"
cd /home/"$USER"/KShell/
echo "You are now in the home directory of your KShell application!"
echo -e "export PATH=\x22$PATH\x22:/home/$USER/KShell/dist/kshell" >> ~/.bashrc
echo "Launching KShell... to run, use the 'kshell' command from any directory in Terminal!"
kshell
