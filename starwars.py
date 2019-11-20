import operator

class Personnage:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def get__nom(self):
        return self.nom

    def get__prenom(self):
        return self.prenom

    def set__nom(self, nom):
        self.nom = nom

    def set__prenom(self, prenom):
        self.prenom = prenom

    def __str__(self):
        return "Le personnage s'appelle "+self.prenom+" "+self.nom+"."

class Acteur:
    def __init__(self, nom = "", prenom = "", listePersonnages = []):
        self.nom = nom
        self.prenom = prenom
        self.listePersonnages = listePersonnages

    def get__nom(self):
        return self.nom

    def get__prenom(self):
        return self.prenom

    def get_listePersonnages(self):
        i = 0
        while i < len(self.listePersonnages):
            print(self.listePersonnages[i].__str__())
            i += 1

    def set__nom(self, nom):
        self.nom = nom

    def set__prenom(self, prenom):
        self.prenom = prenom

    def set_listePersonnages(self, personnage):
        self.listePersonnages.append(personnage)

    def nbPersonnages(self):
        return len(self.listePersonnages)

    def __str__(self):
        return "L'acteur/actrice s'appelle "+self.prenom+" "+self.nom+"."

class Film:
    def __init__(self, titre = "", anneeSortie = 0, numeroEpisode = 0, cout = 0, recette = 0, listeActeurs = []):
        self.titre = titre
        self.anneeSortie = anneeSortie
        self.numeroEpisode = numeroEpisode
        self.cout = cout
        self.recette = recette
        self.listeActeurs = listeActeurs

    def get__titre(self):
        return self.titre

    def get__anneeSortie(self):
        return self.anneeSortie

    def get__numeroEpisode(self):
        return self.numeroEpisode

    def get__cout(self):
        return self.cout

    def get__recette(self):
        return self.recette

    def get_listeActeurs(self):
        i = 0
        while i < len(self.listeActeurs):
            print(self.listeActeurs[i].__str__())
            i += 1

    def set__titre(self, titre):
        self.titre = titre

    def set__anneeSortie(self, anneeSortie):
        self.anneeSortie = anneeSortie

    def set__numeroEpisode(self, numeroEpisode):
        self.numeroEpisode = numeroEpisode

    def set__cout(self, cout):
        self.cout = cout

    def set__recette(self, recette):
        self.recette = recette

    def set_listeActeurs(self, acteur):
        self.listeActeurs.append(acteur)

    def nbActeurs(self):
        return len(self.listeActeurs)

    def nbPersonnages(self):
        i = 0
        nb = 0
        while i < len(self.listeActeurs):
            nb += self.listeActeurs[i].nbPersonnages()
            i += 1
        return nb

    def calculBenefice(self):
        if self.cout > self.recette:
            return (self.cout - self.recette) * -1, False
        else:
            return (self.cout - self.recette) * -1, True

    def isBefore(self, annee):
        if self.anneeSortie < annee:
            return True
        else:
            return False

    def tri(self):
        self.listeActeurs.sort(key = operator.attrgetter("nom"))
        self.listeActeurs.sort(key=operator.attrgetter("prenom"))

    def __str__(self):
        return "Le film "+self.titre+" est l'épisode "+str(self.numeroEpisode)+" de Star Wars. Il est sorti en "+str(self.anneeSortie)+", a coûté "+str(self.cout)+" de dollars et a rapporté "+str(self.recette)+" de dollars."

def makeBackUp(films):
    for year, film in films.items():
        print(year, film.get__titre(), film.get__recette())

def main():
    film1 = Film("Un nouvel espoir", 1977, 4, 11500000, 530000000, [])
    #film3 = Film()
    film2 = Film("L'empire contre-attaque", 1980, 5, 20000000, 40000000, [])
    # print("Entrer un titre de film Star Wars :")
    # film2.set__titre(titre=input())
    # print("Entrer l'année de sa sortie :")
    # film2.set__anneeSortie(anneeSortie=int(input()))
    # print("Entrer le numéro de l'épisode:")
    # film2.set__numeroEpisode(numeroEpisode=int(input()))
    # print("Entrer le coût du film :")
    # film2.set__cout(cout=int(input()))
    # print("Entrer les recettes du film :")
    # film2.set__recette(recette=int(input()))
    act1 = Acteur("Ford", "Harrison", [])
    act2 = Acteur("Fisher", "Carrie", [])
    perso1 = Personnage("Solo", "Han")
    # list = [film1, film2, act1, perso1]
    # i = 0
    # while i < len(list):
    #     print(list[i].__str__())
    #     i += 1
    # print()
    # print()
    perso2 = Personnage("Jones", "Indiana")
    perso3 = Personnage("Organa", "Leia")
    act2.set_listePersonnages(perso3)
    act1.set_listePersonnages(perso1)
    act1.set_listePersonnages(perso2)
    film1.set_listeActeurs(act1)
    #film1.set_listeActeurs(act2)
    film2.set_listeActeurs(act1)
    film2.set_listeActeurs(act2)
    # act1.set_listePersonnages(perso1)
    # act1.set_listePersonnages(perso2)
    # act1.get_listePersonnages()
    # print("Nombre de personnages de ", act1.get__prenom(), act1.get__nom(), ":", act1.nbPersonnages())
    print("Nombre d'acteurs du film", film1.get__titre(), ":", film1.nbActeurs())
    print("Nombre de personnages du film ", film1.get__titre(), ":", film1.nbPersonnages())
    print("Nombre de personnages du film ", film2.get__titre(), ":", film2.nbPersonnages())
    # x, y = film2.calculBenefice()
    # print(x, y)
    # print()
    # print()
    # film2.set_listeActeurs(Acteur("Fisher", "Annie"))
    # film2.get_listeActeurs()
    # film2.tri()
    # print()
    # print("Acteurs triés")
    # film2.get_listeActeurs()
    # dict = {film1.get__anneeSortie() : film1, film2.get__anneeSortie() : film2, film3.get__anneeSortie() : film3}
    # makeBackUp(dict)

main()