from Login.korisnici import prijava, sort, registracija
from Knjige.Knjige  import sortirane_knjige, pretrazi_knjige,brisanje_knjige, registracija_knjiga,izmena_knjiga
from racun.racun import prodaja_knjige, izvestaj
from akcije.akcije import ucitaj_akcije,registracija_akcija,pretrazi_akcija


def meni_administrator():
    while True:
        print("\n===[Administrator]===")
        print(" \n 1. Sortiranje knjiga")
        print(" 2. Pretraga knjiga")
        print(" 3. Prikaz akcija")
        print(" 4. Pretraga akcija")
        print(" 5. Registracija korisnika")
        print(" 6. Lista korisnika")
        print(" 7. Dodaj knjigu")
        print(" 8. Izmeni knjigu")
        print(" 9. Obrisi knjigu")
        print(" 0. Log out")
        stavka = int(input("\nIzaberite stavku: "))

        if stavka == 1:
            sortirane_knjige()
        elif stavka == 2:
            pretrazi_knjige()
        elif stavka == 3:
            pretrazi_akcija()
        elif stavka == 4:
            pretrazi_akcija()
        elif stavka == 5:
            registracija()
        elif stavka == 6:
            sort()
        elif stavka == 7:
            registracija_knjiga()
        elif stavka == 8:
            izmena_knjiga()
        elif stavka == 9:
            brisanje_knjige()
        elif stavka == 0:
            prijava()
        else:
            print("Pokusajte ponovo!")


def meni_menadzer():
    while True:
        print("\n===[Menadzer]===")
        print(" \n 1. Sortiranje knjiga")
        print(" 2. Pretraga knjiga")
        print(" 3. Prikaz akcija")
        print(" 4. Registracija akcija")
        print(" 5. Registracija korisnika")
        print(" 6. Lista korisnika")
        print(" 7. Dodaj knjigu")
        print(" 8. Izmeni knjigu")
        print(" 9. Obrisi knjigu")
        print(" 0. Log Out")
        stavka = int(input("\nIzaberite stavku: "))

        if stavka == 1:
            sortirane_knjige()
        elif stavka == 2:
            pretrazi_knjige()
        elif stavka == 3:
            ucitaj_akcije()
        elif stavka == 4:
            registracija_akcija()
        elif stavka == 5:
            registracija()
        elif stavka == 6:
            sort()
        elif stavka == 7:
            registracija_knjiga()
        elif stavka == 8:
            izmena_knjiga()
        elif stavka == 9:
            brisanje_knjige()
        elif stavka == 0:
            prijava()
        else:
            print("Pokusajte ponovo!")


def meni_prodavac():
    while True:
        print("\n===[Prodavac]===")
        print("\n 1. Sortiranje knjiga")
        print("2. Pretraga knjiga")
        print("3. Prikaz akcija")
        print("4. Pretraga akcija")
        print("5. Prodaj knjigu")
        print("6. Dodaj knjigu")
        print("7. Izmeni knjigu")
        print("8. Obrisi knjigu")
        print("0. Log Out")
        stavka = int(input("\nIzaberite stavku: "))

        if stavka == 1:
            sortirane_knjige()
        elif stavka == 2:
            pretrazi_knjige()
        elif stavka == 3:
            print("Pristup zabranjen")
            meni_prodavac()
        elif stavka == 4:
            pretrazi_akcija()
        elif stavka == 5:
            print("Pristup zabranjen")
            meni_prodavac()
        elif stavka == 6:
            registracija_knjiga()
        elif stavka == 7:
            izmena_knjiga()
        elif stavka == 8:
            brisanje_knjige()
        elif stavka == 0:
            prijava()
        else:
            print("Pogresno uneta funckija!")


def main():
    for i in range(4):
        if i == 3 and ulogovani_korisnik == None:
            print("Pristup zabranjen! Prijatan dan :)")
            exit()

        ulogovani_korisnik = prijava()
        if ulogovani_korisnik != None :
            print("Uspesna prijava!")
            if ulogovani_korisnik['tip_korisnika'] == 'Administrator':
                meni_administrator()
            elif ulogovani_korisnik['tip_korisnika'] == 'Menadzer':
                meni_menadzer()
            elif ulogovani_korisnik['tip_korisnika'] == 'Prodavac':
                meni_prodavac()
        if ulogovani_korisnik == None and i == 0:
                print("Nepostojeci korisnik. Imate jos 2 pokusaja!")
        if ulogovani_korisnik == None and i == 1:
                print("Nepostojeci korisnik. Imate jos 1 pokusaj!")



main()


