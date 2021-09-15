import os.path

def checkvault():
    if os.path.exists("vault.txt"):
        pass
    else:
        vaultfile = open("vault.txt", 'w')
        vaultfile.close()


def fileappend():

    username = input('\n\nUsername:')
    password = input('Password:')
    website = input('Website:')

    web = "\n" + "Website:" + website + "\n" + "\n"
    usern = "Username:" + username + "\n"
    passw = "Password:" + password + 3*"\n"
    space = "---------------------------------------"
    
    file = open('vault.txt', 'a')
    file.write(space)
    file.write(web)
    file.write(usern)
    file.write(passw)
    file.write(space)
    file.close()

    print()
    print()

def menu():

    print()
    print("---------- PASSOWORD MANAGER ----------")
    print("[1] Save Password")
    print("[2] View Passwords")
    print("[3] Help")
    print("[4] Quit")
    print("---------------------------------------")

    global menuinput
    menuinput = int(input())

def readpassw():
    file = open('vault.txt', 'r')
    print(file.read())
    file.close()

def errormessage():
    print("Sorry an Error Occured, please try again")

def goodbyemessage():
    print("Thank you for using Python Password Manager!")

def helpmenu():
    print('''In the main menu enter the number that is next to the desired action. 1 for saving passwords. 2 for viewing passwords. 3 for viewing this message. 4 to quit the application ''')



#MAIN
checkvault()

while True:
    menu()

    if menuinput == 1:
        fileappend()

    elif menuinput == 2:
        readpassw()

    elif menuinput == 3:
        helpmenu()

    elif menuinput == 4:
        goodbyemessage()
        break
        

    else:
        errormessage()
        menu()
