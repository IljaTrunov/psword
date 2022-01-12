import random
users=["papikobi4niy","eestiInimene","spidermanfan2011"]
passws=["qwerty123","eesti1945","123456789"]
status=""
def randUser():
    str0=".,:;!_*-+()/#¤%&"
    str1 = '0123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    str3 = str2.upper()
    str4 = str0+str1+str2+str3
    ls = list(str4)
    print(ls)
    login = ''.join([random.choice(ls) for x in range(12)])
    passw = ''.join([random.choice(ls) for x in range(12)])
    print("Here is ur password and login")
    print("login: " ,login, "\npassword: " ,passw)
def repeat():
    print("Hello!")
    status=input("Are you a registered user? y/n/r (to create fast)? Press q to quit: ")  
    if status=="y":
        oldUser()
    elif status=="n":
        newUser()
    elif status=="r":
        randUser()
def newUser():
    createLogin=input("Create login name: ")
    if createLogin in users:
        print ("Login name already exist!")
    else:
        createPassw=input("Create password: ")
        users.append(createLogin)
        passws.append(createPassw)
        print("A new user has registered!")
        print("Login: ", createLogin)
        print("Password: *********")
        print("User created!")     
def oldUser():
    login=input("Enter login name: ")
    passw=input("Enter password: ")
    if login in users and users.index(login) == passws.index(passw): 
        print ("Login successful!")
        print("Welcome to the steam community!")
    else:
        print("User doesn't exist or wrong password!")
while status != "q":
      repeat()

    #alpha=digit=upper=special=0
#ls= list(str0)
#psword = list(passoword)
#for i in range (len(psword)):
#if psword[i].isupper():
#upper=1
#if psword[i].isalpha():
#alpha=1
#if psword[i].digit():
#digit=1
#if psword[i] in ls:
#special=1
#if alpha==1 and digit==1 and upper==1 and special==1 and len(psword)>7:
#passok=True
#else:
#passok=False
#return passok


import module1
users=["aboba228","eestiInimene","okaspodaini"]
passws=["aboba2005","eesti1945",""]
status=""
print("Hello!")
print("Are you a registered user? y/n/r(to create fast)? Press q to quit: ")
print("You may exit the programm, by typping 'q' ")
status=input("")
while 1:
	if status=="y":
		print("Great!")
	elif status=="n":
		print("Sad...")
	elif status=="r":
		print("Alright, we wil randomize it for you")
	elif status=="q":
		print("Bye!")
		quit
