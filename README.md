# kshell
The Official KShell Repository for KShell Installations

This is the Official KShell Repo which contains all source code and
installer scripts that create binary executables for your operating
system. Please note that KShell is currently still in ***development***!
So any bugs can be reported on the KShell repo page or reported to
the creator's email: ***microbitsarecool@gmail.com***. Thank you!

First off, if you are not reading this from a cloned version of this
repo, to download/clone this repo, type in a terminal (provided that
you have Git) *git clone https://github.com/microbitsarecool/kshell.git*.
If you do not have Git, you can download the ZIP file directly from
Github. Once you've gotten this done, change directories into your
*kshell* directory and use *sh* to execute the corresponding installer
script for your system. For example, here's a sample process of an
installation:

First step: *git clone https://github.com/microbitsarecool/kshell.git* or *Download direct from Github*   
Second step: *cd kshell*   
Third step: *ls*, you will see four different shell scripts:   
Script Name | System
----------- | ------
linux_deb_install.sh | For Debian/Ubuntu based systems
linux_rpm_install.sh | For RedHat/Fedora/CentOS systems
linux_suse_install.sh | For openSUSE based systems
mac_install.sh | For macOS systems
No installer script (follow instructions below) | For Windows systems

***\*Please note, for macOS and Windows users, that you must 
have Python 3 (you can get it at https://www.python.org/downloads/)
before you can run the installer script!***

***Installing using installer scripts***  *(Not for Windows users)!!!*

Fourth step: *bash {scriptname.sh}*, obviously replace *scriptname* with that of the corresponding shell script   
Fifth step: **Make sure you have your KShell home directory set in your path! To do this: use *echo $PATH*. If  
you see something like: */home/{username}/KShell* in the resulting string, you're set! Otherwise, please report
it to *microbitsarecool@gmail.com* or comment on the KShell repo page. Also, please report any failed installations
to the said email address as well. Or, comment on the repo page.**   
Sixth step: Run this command to start KShell: *kshell*. Report any bugs to the creator's email address or
comment on the repo page. If you need help on commands, type a single question mark: *'?'* for a simple list or
read the documentation.txt file for a more detailed documentation.

***For Windows users***

To install, simply download the ZIP or clone using git and then create a home directory (has to be *c:\\Users\\[user]\\KShell*). 
Then, move all the files and subdirectories from the KShell repo into your home repository. Next, open a command 
prompt window and navigate to your home directory for KShell. Then, type these commands (in order and make sure you 
have python installed):

1. ***pip install pyinstaller***
2. ***pyinstaller kshell.py***
3. ***cd dist\\kshell*** (This navigates into the executable's directory)
4. ***kshell.exe*** (This runs kshell)

Next, you can repeat the steps 3-4 to run kshell.exe. Or, if you'd rather add this directory to your path environment:   
***[home-directory]\dist\kshell***, you can then simply run ***kshell.exe*** from anywhere.

***\*Note for Windows users: the path for your home directory has to be: c:\\Users\\[user]\\KShell or KShell
won't work!***
