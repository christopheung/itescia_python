def main():
    suspects = dict()
    suspects["Moutarde"] = "CCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAA"
    suspects["Rose"] = "CTCCTGATGCTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGGADN"
    suspects["Pervenche"] = "AAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGTACTCCGCGCGCCGGGACAGA"
    suspects["Leblanc"] = "CTGCAGGAACTTCTTCTGGAAGTACTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAG"
    print("Bonjour détective, veuillez entrer les deux brins d'ADN trouvés sur le lieu du crime.")
    print("Brin d'ADN n°1 : ")
    brin1 = input()
    print("Brin d'ADN n°2 : ")
    brin2 = input()
    for name, adn in suspects.items():
        if adn.find(brin1) >= 0:
            if adn.find(brin2, 0, adn.find(brin1)) >= 0 or adn.find(brin2, adn.find(brin1) + len(brin1)) >= 0:
                print("Les brins d'ADN correspondent à celui de", name, ". C'est donc le coupable !!!")

main()