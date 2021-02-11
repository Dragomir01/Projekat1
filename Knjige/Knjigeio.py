import json

datoteka = 'C:/Users/drago/Desktop/Faks/Programiranje/Projekat1/Projekat/datoteke/knige.json'



def sacuvaj_knjige(knjige):
    with open(datoteka, "w") as f:
        json.dump(knjige, indent=2)


def ucitaj_knjige():
    with open(datoteka, "r") as f:
        return json.load(f)

