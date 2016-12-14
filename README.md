# mass_ptc_password_changer
Automatic mass password changer for PTC accounts.

## Description
This tool changes password on PTC accounts by creating an invisible chrome session and automatically entering data in the required fields.

You basically enter the accounts that you want to change the password on in accounts.txt. At the end of the process, you will be able to track which accounts had their password successfully changed in accounts_success.txt and the ones that did not in fail_accounts.txt.

One account per line and in the following format `account:password`.

## Note
If you are using this tool, chances are that you have your hands on multiple PoGo accounts. I'd like to point out that you can **sell your accounts in bulk** on the market-leading https://www.flameaccounts.com website. We offer 20% of the account's worth on the website to you once it's sold. (_i.e. You get 7$ on a account worth 35$_ )

You can track all your accounts on a **real-time page** where you can see which were sold, which are still for sale and which you got payed for. We also, rarely, buy bulk accounts.

We have several sellers who made more than 1K with us...

Please contact me on Discord by adding thierbig #6081 or by sending me an email to pogoheaven@gmail.com.

## Installation

Works on Python 3 and tested on a Ubuntu 16.04 environnement. It might work on Windows also, but I'm offering a tutorial from scratch on how to set it up on a virtual machine running Ubuntu 16.04.


### OPTIONAL - Set up Ubuntu 16.04 64 bit on VmWare

1. Download the latest Ubuntu 16.04 64 bit version on http://releases.ubuntu.com/16.04/ubuntu-16.04-desktop-amd64.iso.

2. Run the "New Virtual Machine Wizard" on VMWare and select to install the latest iso you just downloaded.

3. Click "Next" and go through the wizard like a normal human being. Please allow atleast 2 GB of RAM to the virtual machine.

4. Run the virtual machine and follow the Ubuntu installation wizard.


### Install dependencies and set up project for Ubuntu 16.04

If none of the steps below ring a bell for you, please just blindly follow the instructions and type the code in the Terminal.

**YOU CAN PASTE USING CTRL+SHIFT+V ON THE TERMINAL**

* Open terminal ( CTRL-T ) and install the latest Google Chrome release.

`sudo -s` Type in your password....

`wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb`

`sudo dpkg -i --force-depends google-chrome-stable_current_amd64.deb`

* Install the lastest chromedriver release.

`LATEST=$(wget -q -O - http://chromedriver.storage.googleapis.com/LATEST_RELEASE)`

`wget http://chromedriver.storage.googleapis.com/$LATEST/chromedriver_linux64.zip`

* Link the chromedriver to PATH.

`unzip chromedriver_linux64.zip && sudo ln -s $PWD/chromedriver /usr/local/bin/chromedriver`

* Install the following dependencies

`sudo apt-get update`

`sudo apt-get install xvfb python3-venv git`

`sudo apt-get -f install`

`sudo apt-get install xvfb python3-venv git`

* Set up a python 3 virtual environment

`pyvenv py3env`

`source py3env/bin/activate`

* Install the mass_ptc_password_changer

`git clone https://github.com/thierbig/mass_ptc_password_changer`

`cd mass_ptc_password_changer`

`chmod -R o+rw .`

`pip install -r requirements.txt`

### Run the tool
* (I expect you guys to use the Graphical interface for this part) 
Go ahead and find the folder mass_ptc_password_changer on your machine. Open it. Modify the accounts.txt file and enter all the accounts you want to change password with the format `acc:pass` on each line. Modify the __init__.py file and enter the new password at the top where it says `new_pass=""`. Just put the new password inside the "". Close accounts.txt and __init__.py and make sure to save the modification.

* Open a new terminal (CTRL+T), enter these lines and follow the console to follow the changes made to PTC accounts.

`sudo -s` type in your password..

`source py3env/bin/activate`

`cd mass_ptc_password_changer`

`python __init__.py`

* At the end of the process, you will be able to track which accounts had their password successfully changed in accounts_success.txt and the ones that did not in fail_accounts.txt.
