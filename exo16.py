def distance_hamming():
    print("Entrer un mot :")
    mot1 = input()
    print("Entrer un deuxième mot de même longueur")
    mot2 = input()
    if len(mot1) == len(mot2):
        i = 0
        diff = 0
        while i != len(mot1):
            if (mot1[i] != mot2[i]):
                diff += 1
            i += 1
        print("La distance de Hamming est égale à", diff)
    else:
        print("Les deux mots ne sont pas de la même longueur !")

distance_hamming()