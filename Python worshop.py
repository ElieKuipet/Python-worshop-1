# # Exercice 1
# print("Exercice 1")
#
# def est_un_nombre_premier(n):
#     trouve = False
#     i = 2
#     while i < n and n % i != 0:
#         if i == n - 1:
#             trouve = True
#         i += 1
#     return trouve
#
#
# result = est_un_nombre_premier(7)
# print(result)

# # Exercice 3
# print("Exercice 3")
# def nombresEntiers():
#     print(" The 10 first integers are:")
#     for i in range(1, 11):
#         print(i)
#     return
#
#
# result_nombresEntiers = nombresEntiers()
# print()

# # Exercice 4
# print("Exercice 3")
# def sommeDesEntiers():
#     somme = 0
#     for i in range(11):
#         somme += i
#         return somme
#
# result_sommeDesEntiers = sommeDesEntiers()
# print()

# Exercice 5
#print("Exercice 4")

# def sommeEtMoyenne():
#     nombres = []
#
#     i = 1
#     while i < 11:
#         nombre = float(input(f"Entrer les nombres : "))
#         nombres.append(nombre)
#         i += 1
#
#     somme = sum(nombres)
#     moyenne = somme / len(nombres)
#
#     return somme, moyenne

# def sommeEtMoyenne(nombres):
#     return sum(nombres), sum(nombres)/len(nombres)
# somme, moyenne = sommeEtMoyenne([1,2,3,4,5,6,7,8,9,10])
# print(f"La somme des nombres est: {somme}")
# print(f"La moyenne des nombres est: {moyenne}")
# print()

# # Fonction flèche avec Python
# sommeEtMoyenne = lambda nombres: [sum(nombres), sum(nombres)/len(nombres)]
# print(sommeEtMoyenne([1,2,3,4,5,6,7,8,9,10]))


# # Exercice 6
# print("Exercice 6")
# nombre = int(input("Entrer un nombre: "))
# print(f"Les carrés des entiers de 1 à {nombre} sont: ")
# for i in range(1, nombre+1):
#     print(f"{i}^2 = {i**2}")
# print()

# # Exercice 7
# print("Exercice 7")
# def tableDeMul():
#     n = int(input("Entrer votre entier : "))
#     for i in range(0, 11):
#         product = n * i
#         print(f"{n} * {i} = {product}")
#     return
#
#
# resultat_tableDeMul = tableDeMul()
# print()

# # Exercice 8
# print("Exercice 8")
# hauteur_g = int(input("Entrer la hauteur du triangle aligné à gauche: "))
# for i in range(1, hauteur_g + 1):
#     print('*' * i)
#
# hauteur_d = int(input("Entrer la hauteur du triangle aligné à droite: "))
# for i in range(1, hauteur_d + 1):
#     print(' ' * (hauteur_d - i) + '*' * i)


# # Exercice 9
# print("Exercice 9")
#
# # Entrer les informations de l'étudiant
# num_matricule = input("Entrez le numéro de matricule de l'étudiant : ")
# nom = input("Entrez le nom de l'étudiant : ")
# notes = input("Entrez les notes de physique, de chimie et d'informatique (séparées par des espaces) : ")
#
# # Ramener les notes à une liste et convertir en entiers
# notes_list = notes.split()
# print(notes_list)
#
# # Calcul du total et du pourcentage
# total_notes = sum(notes_list)
#
# # Afficher les résultats
# print(f"Numéro de matricule : {num_matricule}")
# print(f"Nom de l'étudiant : {nom}")
# print(f"Notes en physique : {notes_list[0]}")
# print(f"Notes en chimie : {notes_list[1]}")
# print(f"Notes en informatique : {notes_list[2]}")
# print(f"Total des notes = {total_notes}")

# Exercice 10
print("Exercice 10")

def suivre_taux_occupation_journaliere():
    insertion_journaliere = []
    jours_de_pointe = []
    nombre_jours = 7
    somme_insertion_journaliere = 0
    taille_du_refuge = 100
    jour_de_pointe = []
    i = 1
    personnes_cherchant_abri = 0
    personnes_en_surplus = 0


    # 1er scénario: les refugiés quittent le camp après la nuitée
    while i <= nombre_jours:
        personnes_cherchant_abri = int(input(f"Entrer le nombre de personnes cherchant un abri le jour {i}: "))
        print(f"les personnes en surplus sont de: {personnes_en_surplus}")
        if personnes_cherchant_abri > 100:
            insertion_journaliere.append(100)
            personnes_en_surplus = personnes_cherchant_abri - 100
        else:
            if personnes_cherchant_abri + personnes_en_surplus > 100:
                insertion_journaliere.append(100)
                personnes_en_surplus = personnes_cherchant_abri + personnes_en_surplus - 100
            else:
                insertion_journaliere.append(personnes_cherchant_abri + personnes_en_surplus)
                personnes_en_surplus = 0
        i = i + 1

    print(insertion_journaliere)

    # Calcul de l'occupation moyenne:
    occupation_moyenne = (sum(insertion_journaliere)*100) / (7 * taille_du_refuge)

    # Jours de pointe
    for personnes in insertion_journaliere:
        if personnes >= occupation_moyenne:
            jours_de_pointe.append(personnes)
    print(jours_de_pointe)

    # Inventaire des banques alimentaires
    stock = {'PaquetsBiscuitsNRJ': 100, 'cerealesKG': 50, 'litres_de_lait': 30, 'litres_HuileVegetale': 60}
    print("Voulez-vous entrer de nouvelles denrées? Saisissez 'True' pour Oui ou 'False' pour non")

    Trouve = False
    if True:
        while not Trouve:
            nouvelle_denree = ''
            nouvelle_denree = input("Entrer les nouvelles denrées et leur quantité en insérant un espace à chaque fois('end' pour finir): ")
#for elt in nouvelle_denree:
# if nouvelle_denree[-1] ='end':
#     Trouve = True

                    



                #Trouve = True


    return occupation_moyenne, jours_de_pointe

result = suivre_taux_occupation_journaliere()
print(result)