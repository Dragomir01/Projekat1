password_fname = "Nalozi.txt"

def izbori():
    print("Izaberite sta želite da uradite")
    izbor = int(input("Za prijavu ukucajte 1, za registraciju ukucajte 2:"))
    if izbor == 1:
        return prijava()
    elif izbor == 2:
        return reg()
    else:
        return nazad

def nazad():
    print("Error")



def reg():
    print("Unesite")
    name = str(input("Ime:"))
    password = str(input("Lozinka:"))
    f = open("Nalozi.txt")
    info = f.read()
    if name in info:
        return "Ime nije dostuno.Pokušajte ponovo"
    f.close()
    f = open("Nalozi.txt",'w')
    info = info + " " +name +" " + password
    f.write(info)




def prijava():
    print("Unesite")
    name = str(input("Ime:"))
    password = str(input("Lozinka:"))
    f = open("Nalozi.txt" , 'r')
    info = f.read()
    info = info.split()
    if name in info:
        index = info.index(name) + 1
        usr_password = info[index]
        if usr_password == password:
            return "Dobrodosli nazad," + name
        else:
            for i in range(3, 0, -1):
                print("Lozinka netačna, probajte ponovo!")
                name = str(input("Ime:"))
                password = str(input("Lozinka:"))
                f = open("Nalozi.txt", 'r')
                info = f.read()
                info = info.split()
                if name in info:
                    index = info.index(name) + 1
                    usr_password = info[index]
                    if usr_password == password:
                        return "Dobrodosli nazad," + name
            if i == 1:
                     print("Pristup Zabranjen :), Prijatan dan!")

    else:
        return "Uneto Ime ne postoji"













print(izbori())

