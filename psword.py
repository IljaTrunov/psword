users=["aboba228","eestiInimene","okaspodaini"]
passw=["aboba2005","eesti1945",""]
status=""

def repeat(status):
    status=input("Are you a registered user? y/n? Press q to quit: ")  
    if status=="y":
        oldUser()
    elif status=="n":
        newUser()
def newUser():
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
    if login in users and users[login] == passw: 
        print ("Login successful!")
    else:
        print("User doesn't exist or wrong password!")
while status != "q":
    try:
        type=input(repeat(status))
    except ValueError:
        print()

