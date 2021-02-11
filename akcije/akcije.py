from akcije.akcijeIO import ucitaj_akcije, sacuvaj_akcije
from Knjige.Knjige import ucitaj_knjige, sacuvaj_knjige
from datetime import date

akcije = ucitaj_akcije()
n = len(akcije)
knjige = ucitaj_knjige()

k = ['nasalov', 'autor', 'kategorija','sifra','datum_vazenja','nova_cena']

def ispis_table(akcije, show_valid):
    glavno =    f"{'sifra':<10}" \
                f"{'naslov':<20}" \
                f"{'stara cena':^20}" \
                f"{'nova cena':^20}" \
                f"{'datum vazenja':^20}"
    print(glavno)
    print("-"*len(glavno))
    for i in range(0, len(akcije)):
        if akcije[i]["datum"]>str(date.today()) or show_valid == false:

            for j in range(0, len(akcije[i]['artikli'])):
                    f"{akcije[i]['artikli'][j]['naslov']:<20}" \
                    f"{akcije[i]['artikli'][j]['cena']:^20}" \
                    f"{akcije[i]['artikli'][j]['nova cena']:^20}" \
                    f"{akcije[i]['datum_vazenja']:^20}"

                    print(za_ispis)

def pretraga_akcije(k, vrednost):
    akcije = ucitaj_knjige()
    filtrirane_akcije = []
    if kljuc=='sifra' or kljuc=='nova cena' or kljuc =='datum_vazenja':

        for akcija in akcije:
            if vrednost.lower() in akcija[kljuc].lower():
                filtrirane_akcije.append(akcija)

        else:
            for akcija in akcije:
                for artikal in akcija['artikli']:
                    if artikal[kljuc].lower() == vrednost.lower():
                                 filtrirane_akcije.append(akcija)

        return filtrirane_akcije

def pretraga_akcija(k, vrednost):

    akcija = ucitaj_akcije()
    filtrirane_akcije = []

    for akcija in akcije:
            if vrednost == akcija(kljuc):
                filtrirane_akcije.append(akcija)

    return filtrirane_akcije

def sortiranje_akcija(k):
    for i in range(len(akcije)):
        for j in range(len(akcije)):
            if akcije[i][kljuc] < akcije[j][kljuc]:
                privremeno = akcije[i]
                akcije[i] = akcije[j]
                akcije[j] = privremeno

def sortirane_akcije():
    while Treu:
        print("Pretrazi prema:"
              "\n1. Sifri:"
              " 2. Datum vazenja:"
              " 0. back")
        if stavka == 1 :
            sortirane_akcije('sifra')
        elif stavka == 2:
            sortiranje_akcija('datum_vazenja')
        elif stavka == 0:
            return False
        else:
            print("Nepostojeci unos")
        ispis_table(akcije, show_valid=false)

def pretraga_akcija():

    nova_akcija = {"sifra": 1,
                   "artikli": [],
                   "datum_vazenja": "31.12.2021.",}
    sifra = akcije[-1]['sifra']
    nova_akcija['sifra'] = sifra + 1

    dodavanje_knjige = True
    while dodavanje_knjige:
        sifra=unos_sa_preverom("Unesite sifru knjige(x za izlazak)")
        if sifra == 'x':
            dodavanje_knjige = False

    else:
        for knjiga in knjige:
            if knjiga['sifra']==int(sifra):
                if knjiga['brisanje']== False:
                    nova_cena = float(input("Unesite cenu akcije"))
                    knjiga['nova cena'] = nova_cena
                    nova_akcija['artikli'].append(knjiga)
        else:
            print("Trazena knjiga ne postoji u sistemu!")

    datum_vazenja = input("Unesite vreme trajanje akcije:")
    nova_akcija['datum_vazenja'] = datum_vazenja
    akcije.append(nova_akcija)
    if len(nova_akcija['artikli'])>0:
        sacuvaj_akcije(akcije)
        print('Akcije je uspesno dodata. Sifra=[%s]' % (nova_akcija['sifra']))

    else:
        for knjiga in knjige:
            if knjiga['sifra'] == int(sifra):
                if knjiga['brisanje'] == False:
                    nova_cena = float(input("\nUnesi novu cenu knjige: "))
                    knjiga['nova cena'] = nova_cena
                    nova_akcija['artikli'].append(knjiga)
                else:
                    print('knjiga ne postoji!')
    datum_vazenja = input("\nUnesi datum vazenja akije: ")
    nova_akcija['datum_vazenja'] = datum_vazenja
    akcije.append(nova_akcija)
    if len(nova_akcija['artikli']) > 0:
        sacuvaj_akcije(akcije)
        print('Nova akcija je dodata u bazu podataka. Sifra akcije=[%s]' % (nova_akcija['sifra']))
