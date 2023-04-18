from herhalingOOP import *

def toon_menu():
    print("1:Toon_data")
    print("2:Crud")

def toon_menu_data():
    print("1: Toon alle personen")
    print("2: alle voertuigen")
    print("3: alle verhuringen")
    print("x: terug naar hoofdmenu")

def toon_menu_crud():
    print("1: voer een persoon in")
    print("2: voer auto/moto in")
    print("3: voeg een verhuring toe")

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
    nieuwe_verhuring = Verhuring(id,voertuig_object,persoons_object)
    lijst_verhuringen.append(nieuwe_verhuring)






########################################

toon_menu()
invoer = input("geef invoer")
while invoer != "stop":
    toon_menu()
    if invoer == "1":
        toon_menu_data()
        invoer = input("geef keuze")
        while invoer != "stop":
            if invoer == "1":
                toon_alle_personen()
            elif invoer == "2":
                toon_alle_voertuigen()
            elif invoer == "3":
                toon_alle_verhuringen()
            elif invoer == "x":
                toon_menu()
                break
            invoer = input("geef nieuwe keuze in")

    elif invoer == "2":
        toon_menu_crud()
        invoer = input("geef invoer voor crud")
        while invoer != "stop":
            if invoer == "1":
                voeg_persoon_toe()
            elif invoer == "2":
                voeg_voertuig_toe()
            elif invoer == "3":
                voeg_verhuring_toe()
            elif invoer == "x":
                toon_menu()
                break
            invoer = input("geef een nieuwe invoer het de crud opties")

    ### invoer voor het hoofdmenu
    invoer = input("geef nieuwe invoer")


