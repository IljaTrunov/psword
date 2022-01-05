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
using System;

namespace EPICBATTLE
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] heroes = { "Mario", "Chinese woman", "Donkey", "Shrek", "Bomj", "Patrick", "Deadpool", "Garry Snail", "150kg Pudge" };
            string[] villian = { "Kim Jong-Un", "Putin", "Hitler", "Stalin", "Jew", "Hitman", "Street cleaner", "Lenin", "Trevor from gta 5", "your mother" };
            string[] weapon = { "gaming mouse", "wooden chain", "some random motherfucker", "super mega powers", "atom bomb", "universe explosion", "fingers", "fist", "fly","gravity control","your mothers phone","No u", "Uno reverse card" };

            string randomHero = GetRandomcharacter(heroes);
            string randomVillian = GetRandomcharacter(villian);
            string Heroweapon = GetWeapon(weapon);
            string Villianweapon = GetRandomcharacter(weapon);
            Console.WriteLine($"Your random Hero is {randomHero}");
            Console.WriteLine($"Your random Hero weapon is {Heroweapon}");
            Console.WriteLine($"Your random Villian is {randomVillian}");
            Console.WriteLine($"Your random Villian weapon is {Villianweapon}");
        }

        public static string GetRandomcharacter(string[] someArray)
        {
            Random rnd = new Random();
            int randomIndex = rnd.Next(0, someArray.Length);

            return someArray[randomIndex];

        }
         public static string GetWeapon(string[] someArray)
        {
            Random rnd = new Random();
            int randomIndexOne = rnd.Next(0, someArray.Length);

            return someArray[randomIndexOne];

        }


     
    }
}
    a=b
    b=abi
    return a,b

def generaator(n:int,loend:list,a:int,b:int):
    """ генерирует числа от а до b в значении n
    :param int n: количество чисел
    :param int a: минимальное
    :param int b: максимальное
    :param list loend: список сгенерируемых чисел
    """
    for i in range (n):
        loend.append(randint(a,b))
    

def jagamine(loend:list,p:list,n:int,nol:list):
    """сортирует положительные и отрицательные числа
    :param list loend: список всех чисел
    :param list p: положительные
    :param list n: отрицательные
    :param list nol: нули
    """
    for el in loend:
        if el>0:
            p.append(el)
        elif el<0:
            n.append(el)
        else:
            nol.append(el)

def keskmine(loend:list):
    """ищет среднее число
    :param list loend:
    """
    n=len(loend)
    if n==0:
        kesk=0
    else:
        sum=0
        for i in loend:
            sum+=i
        kesk=round(sum/n,2) #округление до целового числа 
    return kesk

def lisamine(loend:list,el:float):
    """ добавляет число в список
    :param list loend:
    :param el float:
    """
    loend.append(el)
    loend.sort()

arvud_loendis()

