import random
users=["aboba228","eestiInimene","okaspodaini"]
passws=["aboba2005","eesti1945",""]
status=""
def repeat():
    status=input("Are you a registered user? y/n/r(to create fast)? Press q to quit: ")  
    if status=="y":
        oldUser()
    elif status=="n":
        newUser()
    elif status=="r":
        randUser()
def newUser():
    print("Do you want to randomize your login and password?")
    print("y/n? Press q to quit: ")
    if answer=="n":
        login=''.join([random.choice(ls) for x in range(12)])
        passws=''.join([random.choice(ls) for x in range(12)])
    createLogin=input("Create login name: ")
    if createLogin in users:
        print ("Login name already exist!")
    else:
        createPassw=input("Create password: ")
        users.insert(createPassw,createLogin) 
        print("User created!")     
def oldUser():
    login=input("Enter login name: ")
    passw=input("Enter password: ")
    if login in users and users.index(login) == passws.index(passw): 
        print ("Login successful!")
    else:
        print("User doesn't exist or wrong password!")
def randUser():
    login=random.choice(ls)
    passw=random.choice(ls)
    print(login,passw)
    print("Here is ur password and login")
def autothorzation():
    str0=".,:;!_*-+()/#¤%&"
    str1 = '0123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    str3 = str2.upper()
    str4 = str0+str1+str2+str3	
    ls = list(str4)
    random.shuffle(ls)
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
answer=str(input(""))
while 1:
	if answer==y:
		print("Great!")
	elif answer==n:
		print("Sad...")
	elif answer==r:
		print("Alright, we wil randomize it for you")
		print("You may exit the programm, by typping 'exit' or you can register by typping 'reg'")
		a=input("")
		if a=="exit":
			break
