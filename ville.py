class Ville:
    def __init__(self, nom, nbHabitants = 0):
        self.nom = nom
        self.nbHabitants = nbHabitants

    def get_nom(self):
        return self.nom

    def get_nbHabitants(self):
        return self.nbHabitants

    def set_nom(self, nom):
        self.nom = nom

    def set_nbHabitants(self, nbHabitants):
        if nbHabitants < 0:
            self.nbHabitants = 0
        else:
            self.nbHabitants = nbHabitants

    def categorie(self):
        if self.nbHabitants == 0:
            return "?"
        if self.nbHabitants < 500000:
            return "A"
        elif self.nbHabitants > 500000:
            return "B"

    def __str__(self):
        return "La ville "+self.nom+" possède "+str(self.nbHabitants)+" habitants."

class Capitale(Ville):
    def __init__(self, pays, nom, nbHabitants = 0):
        Ville.__init__(self, nom, nbHabitants)
        self.pays = pays

    def categorie(self):
        return "C"

    def __str__(self):
        return "La ville "+self.get_nom()+" possède "+str(self.get_nbHabitants())+" habitants. Elle est la capitale de "+self.pays+"."

def main():
    town1 = Ville("TOULOUSE")
    town2 = Ville("STRASBOURG", 272975)
    town3 = Capitale("FRANCE", "PARIS", 2181371)
    town4 = Capitale("ITALIE", "ROME", 1000000)
    print(town1.__str__(), town1.categorie())
    print(town2.__str__(), town2.categorie())
    print(town3.__str__(), town3.categorie())
    print(town4.__str__(), town4.categorie())

main()