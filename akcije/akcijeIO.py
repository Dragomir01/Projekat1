import json

datoteka = 'C:/Users/drago/Desktop/Faks/Programiranje/Projekat1/Projekat/datoteke/akcije.json'


def ucitaj_akcije():
    with open(datoteka, "r") as f:
        return json.load(f)


def sacuvaj_akcije(korisnici):
    with open(datoteka, "w") as f:
        json.dump(korisnici, f, indent=10)