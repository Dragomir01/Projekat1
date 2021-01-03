

def izbori():
    print("Izaberite sta želite da uradite")
    izbor = int(input("Za prijavu ukucajte 1, za registraciju ukucajte 2:"))
    if izbor == 1:
        return prijava()
    elif izbor == 2:
        return reg()
    else:
        return TypeError




def reg():
    print("Unesite")
    name = str(input("Ime:"))
    password = str(input("Lozinka:"))
    f = open("Nalozi.json")
    info = f.read()
    if name in info:
        return "Ime nije dostuno.Pokušajte ponovo"
    f.close()
    f = open("Nalozi.json",'w')
    info = info + " " +name +" " + password
    f.write(info)




def prijava():
    print("Unesite")
    name = str(input("Ime:"))
    password = str(input("Lozinka:"))
    f = open("Nalozi.json" , 'r')
    info = f.read()
    info = info.split()
    if name in info:
        index = info.index[index] + 1
        usr_password = info[index]
        if usr_password == password:
            return "Dobrodosli nazad," + name
        else:
            return "Uneta lozinka je netacna"


print(izbori())


