class Persoon:

    def __init__(self, id, name, city):
        self.id = id
        self.name = name
        self.city = city
    def __str(self):
        return f"Naam:{self.name} Woonplaats:{self.city}"


p1 = Persoon("p1","Bert","Hasselt")
p2 = Persoon("p2","Karolien","Genk")
p3 = Persoon("p3","Mark","Hasselt")
p4 = Persoon("p4","Paulien","Genk")
p5 = Persoon("p5","Arne","Bilzen")
p6 = Persoon("p6","Ruben","Bilzen")
p7 = Persoon("p7","Axel","Genk")

list_personen = [p,p2,p3,p4,p5,p6,p7]
