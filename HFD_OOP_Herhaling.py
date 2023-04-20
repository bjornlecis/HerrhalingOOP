from herhalingOOP import *

def toon_menu():
    print("1:Toon_data")
    print("2:Crud")

def toon_menu_data():
    print("1: Toon alle personen")
    print("2: alle voertuigen")
    print("3: alle verhuringen")
    print("4: Toon alle verhuringen met prijs en totaalprijs")
    print("5: Toon alle voertuigen gehuurd door persoon x")
    print("6: Toon alle personen die voertuig x huurde")
    print("x: terug naar hoofdmenu")

def toon_menu_crud():
    print("1: voer een persoon in")
    print("2: voer auto/moto in")
    print("3: voeg een verhuring toe")
    print("4: verwijder een voertuig")
    print("5: verwijder een persoon")
    print("6: sorteer op merk")
    print("7: sorteer op bouwjaar")


def toon_alle_personen():
    for per in lijst_per:
        print(per)
def toon_alle_voertuigen():
    #uitbreiding if instanceof(type,variable/instantie)
    for voertuig in lijst_voertuigen:
        print(voertuig.id,voertuig.merk,voertuig.model,voertuig.bouwjaar)
def toon_alle_verhuringen():
    for verhuur in lijst_verhuringen:
        print(verhuur)
def voeg_persoon_toe():
    id = input("geef het id")
    naam = input("geef naam")
    leeftijd = int(input("geef de leeftijd"))
    p = Persoon(id,naam,leeftijd)
    lijst_per.append(p)
def voeg_voertuig_toe():
    type = input("auto of motorbike")
    dagprijs = int(input("geef de dagprijs"))
    merk = input("geef het merk")
    model = input("geef het model")
    bouwjaar = int(input("geef het bouwjaar in"))
    if type.upper() == "AUTO":
        voertuig = Auto(dagprijs,merk,model,bouwjaar)
        lijst_voertuigen.append(voertuig)
    elif type.upper() == "MOTORBIKE":
        voertuig = Motorbike(dagprijs,merk,model,bouwjaar)
        lijst_voertuigen.append(voertuig)
    else:
        print("voertuig kan niet toegevoegd worden")
def voeg_verhuring_toe():
    id = input("geef het id van de verhuring")
    toon_alle_voertuigen()
    id_voertuig = input("geef het id van het voertuig")
    for voertuig in lijst_voertuigen:
        if voertuig.id == id_voertuig:
            voertuig_object = voertuig
            break
    toon_alle_personen()
    id_persoon = input("geef het id van de Persoon")
    for persoon in lijst_per:
        if persoon.id == id_persoon:
            persoons_object = persoon
            break
    aantal_dagen = int(input("hoeveel dagen huren"))
    nieuwe_verhuring = Verhuring(id,voertuig_object,persoons_object,aantal_dagen)
    lijst_verhuringen.append(nieuwe_verhuring)
def functies_toon_menu():
    toon_menu_data()
    invoer = input("geef keuze")
    while invoer != "stop":
        if invoer == "1":
            toon_alle_personen()
        elif invoer == "2":
            toon_alle_voertuigen()
        elif invoer == "3":
            toon_alle_verhuringen()
        elif invoer == "4":
            toon_verhuringen_prijzen()
        elif invoer == "5":
            toon_voertuigen_gehuurd_door()
        elif invoer == "6":
            toon_persoon_gehuurd()
        elif invoer == "x":
            toon_menu()
            break
        invoer = input("geef nieuwe keuze in")
def functies_crud_menu():
    toon_menu_crud()
    invoer = input("geef invoer voor crud")
    while invoer != "stop":
        if invoer == "1":
            voeg_persoon_toe()
        elif invoer == "2":
            voeg_voertuig_toe()
        elif invoer == "3":
            voeg_verhuring_toe()
        elif invoer == "4":
            verwijder_voertuig()
        elif invoer == "5":
            verwijder_persoon()
        elif invoer == "6":
            sorteer_op_merk()
        elif invoer == "7":
            sorteer_op_bouwjaar()
        elif invoer == "x":
            toon_menu()
            break
        invoer = input("geef een nieuwe invoer het de crud opties")
def toon_verhuringen_prijzen():
    prijzen = []
    for verhuur in lijst_verhuringen:
        prijzen.append(verhuur.voertuig.dagprijs*verhuur.dagen)
        verhuur_tekst = f"ID\t{verhuur.verhuur_id}\nVoortuig Info\t{verhuur.voertuig.toon_info()}\n" \
                        f"Persoon:\t{verhuur.persoon}\nPrijs: € \t{verhuur.dagen*verhuur.voertuig.dagprijs}"
        print(verhuur_tekst)
    print("Totaal: € ",sum(prijzen))
def verwijder_voertuig():
    toon_alle_voertuigen()
    voertuig_id = input("geef het id")
    for voertuig in lijst_voertuigen:
        if voertuig_id == voertuig.id:
            lijst_voertuigen.remove(voertuig)
            print("voertuig verwijderd")
            break
def verwijder_persoon():
    toon_alle_personen()
    persoon_id = input("geef het id")
    for persoon in lijst_per:
        if persoon.id == persoon_id:
            lijst_per.remove(persoon)
            print("Persoon verwijderd")
            break
def sorteer_op_merk():
    lijst_voertuigen.sort(key=lambda x:x.merk)
    toon_alle_voertuigen()
def sorteer_op_bouwjaar():
    lijst_voertuigen.sort(key=lambda x:x.bouwjaar)
    toon_alle_voertuigen()
def toon_voertuigen_gehuurd_door():
    toon_alle_personen()
    filter_voertuigen_persoon = []
    persoon_id = input("geef het id van de person")
    for verhuring in lijst_verhuringen:
        if persoon_id == verhuring.persoon.id:
            filter_voertuigen_persoon.append(verhuring)
    for voertuig in filter_voertuigen_persoon:
        print(voertuig)
def toon_persoon_gehuurd():
    toon_alle_voertuigen()
    voertuig_id = input("geef het id")
    filter_personen = []
    for verhuring in lijst_verhuringen:
        if voertuig_id == verhuring.voertuig.id:
            filter_personen.append(verhuring)
    for persoon in filter_personen:
        print(persoon.persoon)




########################################

toon_menu()
invoer = input("geef invoer")
while invoer != "stop":
    toon_menu()
    if invoer == "1":
        functies_toon_menu()
    elif invoer == "2":
        functies_crud_menu()

    ### invoer voor het hoofdmenu
    invoer = input("geef nieuwe invoer")


