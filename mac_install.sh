user=$(id -un)
mkdir /home/"$user"/KShell
xcode-select --install
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew install python3
brew install pip3
pip3 install tkinter
pip3 install pyinstaller
pyinstaller kshell.py
mv * /home/"$user"/KShell
echo "Successfully moved files to directory /home/$USER/KShell/"
cd /home/"$user"/KShell
echo "You are now in the home directory of your KShell application!"
echo "export PATH=/home/$USER/KShell/dist/kshell:$PATH" >> ~/.profile
echo "Launching KShell... to run, use the 'kshell' command from any directory in Terminal!"
kshell
