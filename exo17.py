def palindrome():
    print("Entrer un mot :")
    mot = input()
    i = 0
    j = len(mot) - 1
    while (i != len(mot)):
        if (mot[i] == mot[j]):
            palin = True
        else:
            palin = False
        i += 1
        j -= 1
    if palin:
        print("Le mot", mot, "est un palindrome")
    else:
        print("Le mot", mot, "n'est pas un palindrome")

palindrome()