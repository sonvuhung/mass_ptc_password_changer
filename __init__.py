from ptc import random_account,login_account,change_password
import os
import time
import names
import random




randomPw=True



#ENTER NEW PASSWORD FOR ALL ACCOUNTS HERE
###########################################################
new_pass=""
###########################################################



def randomNumber():
    return random.randint(0,9).__str__()

def addSuccessAcc(acc):
    with open('accounts_success.txt', 'a') as f1:
        f1.write(acc.username + ":" + acc.new_password + os.linesep)


def addFailAcc(acc):
    with open('accounts_fail.txt', 'a') as f1:
        f1.write(acc.username + ":" + acc.password + os.linesep)

def addAllPw(pw):
    with open('passwords.txt','a') as f1:
        f1.write(pw+os.linesep)

class Account():
    def __init__(self,username,password,new_password):
        self.username=username
        self.password=password
        self.new_password=new_password
succc = os.path.join(os.path.expanduser('~'), 'mass_ptc_password_changer', 'passwords.txt')

with open("accounts.txt", "r") as ins:
    accounts = []
    for line in ins:
        username=line.split(":")[0]
        password=line.split(":")[1].split("\n")[0]

        if(randomPw):
            new_pass="$"+names.get_first_name(gender="female")
            count_name=len(new_pass)
            if(len(new_pass)>8):
                new_pass=new_pass[0:8]
            while(len(new_pass)<9):
                new_pass+=randomNumber()
        addAllPw(new_pass)
        accounts.append(Account(username,password,new_pass))

succc = os.path.join(os.path.expanduser('~'), 'mass_ptc_password_changer', 'accounts_success.txt')
failll = os.path.join(os.path.expanduser('~'),'mass_ptc_password_changer','accounts_fail.txt')

try:
    os.remove(succc)
except OSError:
    pass
try:
    os.remove(failll)
except OSError:
    pass


sucess_account=[]
fail_accounts=[]
for i in range(len(accounts)):
    j=1
    sucess=False
    while (sucess==False and j<5):
        print("Changing password of account - " + accounts[i].username)
        sucess=change_password(accounts[i].username,accounts[i].password,accounts[i].new_password)
        if(sucess):
            print("SUCCESS:Changed password of account - "+accounts[i].username+" after "+j.__str__()+" try/ies")
            sucess_account.append(accounts[i])
            addSuccessAcc(accounts[i])
        elif(sucess=="invalidPassword"):
            print("Invalid password case for account - " + accounts[i].username+". Going to next.")
        else:
            print("FAIL:Failed to change password of account because of http errors...- " + accounts[i].username + " after " + j.__str__() + " try/ies")
            time.sleep(10+j*2)
        j+=1
    if(sucess==False):
        fail_accounts.append(accounts[i])
        addFailAcc(accounts[i])

print("Done changing passwords of all accounts")