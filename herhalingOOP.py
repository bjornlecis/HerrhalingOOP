class Persoon:

    def __init__(self,id,naam,leeftijd):
        self.id = id
        self.naam = naam
        self.leeftijd = leeftijd

    def __str__(self):
        return f"id:\t{self.id}\nnaam:\t{self.naam}\nleeftijd\t{self.leeftijd}"
    def toon_naam(self):
        return self.naam


class Voertuig:

    aantal_voertuigen = 0
    def __init__(self,dagprijs):
        self.id = "V"+str(Voertuig.aantal_voertuigen+1)
        self.dagprijs = dagprijs
        Voertuig.aantal_voertuigen += 1
    def __str__(self):
        return f"id:\t{self.id}\ndagprijs:\t{self.dagprijs}"
        return
    def toon_info(self):
        return self.id
class Motorbike(Voertuig):

    def __init__(self, dagprijs, merk, model, bouwjaar):
        super().__init__(dagprijs)
        self.merk = merk
        self.model = model
        self.bouwjaar = bouwjaar

    def __str__(self):
        return super.__str__()+f"Merk:\t{self.merk}\nModel:\t{self.model}\n" \
                               f"Bouwjaar:\t{self.bouwjaar}"
    def toon_info(self):
        return f"{super().toon_info()} {self.merk} {self.model}"

class Auto(Voertuig):

    def __init__(self, dagprijs, merk, model, bouwjaar):
        super().__init__(dagprijs)
        self.merk = merk
        self.model = model
        self.bouwjaar = bouwjaar

    def __str__(self):
        return super.__str__()+f"Merk:\t{self.merk}\nModel:\t{self.model}\n" \
                               f"Bouwjaar:\t{self.bouwjaar}"
    def toon_info(self):
        return f"{super().toon_info()} {self.merk} {self.model}"

class Verhuring:

    def __init__(self,verhuur_id,voertuig,persoon,dagen):
        self.verhuur_id = verhuur_id
        self.voertuig = voertuig
        self.persoon = persoon
        self.dagen = dagen
    def __str__(self):
        return f"Verhuur_id:\t{self.verhuur_id}\nvoortuig:\t{self.voertuig.toon_info()}\nPersoon:\t{self.persoon.naam}"




p1 = Persoon("p01","Barjte",25)
p2 = Persoon("p02","Flipke",27)
v1 = Auto(70,"Fiat","Punto",2004)
v2 = Auto(60,"Citroen","Cactus",2005)
v3 = Auto(65,"Fiat","Mulitpla",2007)
v4 = Motorbike(50,"Ducati","Streetfighter",2004)
v5 = Motorbike(75,"Harley","Davidson",2010)
v6 = Auto(65,"Suzuki","Wagon",2004)

vh1 = Verhuring("ver1",v4,p1,5)
vh2 = Verhuring("ver2",v5,p2,3)
vh3 = Verhuring("ver3",v3,p2,4)
vh4 = Verhuring("ver4",v1,p1,3)
vh5 = Verhuring("ver5",v6,p2,2)
vh6 = Verhuring("ver6",v2,p1,3)

lijst_per = [p1,p2]
lijst_voertuigen = [v1,v2,v3,v4,v5,v6]
lijst_verhuringen = [vh1,vh2,vh3,vh4,vh5,vh6]




