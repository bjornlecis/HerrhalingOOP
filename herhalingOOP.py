class Persoon:

    def __init__(self,id,naam,leeftijd):
        self.id = id
        self.naam = naam
        self.leeftijd = leeftijd

    def __str__(self):
        return f"id:\t{self.id}\nnaam:\t{self.naam}\nleeftijd\t{self.leeftijd}"

class Voertuig:

    aantal_voertuigen = 0
    def __init__(self,id,dagprijs):
        self.id = "V"+str(Voertuig.aantal_voertuigen+1)
        self.dagprijs = dagprijs
        Voertuig.aantal_voertuigen += 1
    def __str__(self):
        return f"id:\t{self.id}\ndagprijs:\t{self.dagprijs}"





