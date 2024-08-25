# a = float(input("Entrer votre 1er nbre: "))
# b = float(input("entrer votre 2e nbre: "))
# sum = a + b
# print(f"La somme de ces 2 nombres est : {sum}")

# a = float(input("Entrer votre 1er nbre: "))
# b = float(input("entrer votre 2e nbre: "))
# if a < b:
#     print(f"{b} est le maximum")
# else:
#     print(f"{a} est le maximum")

# x = float(input("Entrer le 1er nbre: "))
# y = float(input("Entrer le 2er nbre: "))
# z = float(input("Entrer le 3e nbre: "))
#
# if x > y:
#     if x > z:
#         print (f"{x} est le maximum")
#     else:
#         print (f" {z} est le maximum")
# else:
#     if y > z:
#         print(f"{y} est la maximum")
#     else:
#         print(f"{z} est le maximum")

# n = int(input("Entrer un nbre: "))
# sum = 0
# for i in range(n+1):
#     sum = i + sum
# print(f"La valeur de cette suite est: {sum}")

n = int(input("Entrer un nbre: "))
facto = 1
if n == 0 or n == 1:
    print(f"le factoriel de {n} est 1")
else:
    for i in range(1, n+1):
        facto = i * facto
    print(f"Le factoriel de ce nombre est: {facto}")

# Taf: working with strings in Python

# Demander à l'utilisateur de saisir un texte
texte = input("Veuillez saisir un texte : ")

# Initialiser une liste pour stocker les mots
mots = []
mot = ""
lettres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-"

# Parcourir chaque caractère du texte
for char in texte:
    if char in lettres:
        mot += char
    else:
        if mot:
            mots.append(mot)
            mot = ""

# Ajouter le dernier mot si le texte ne se termine pas par un caractère non alphanumérique
if mot:
    mots.append(mot)

# Initialiser une liste pour stocker les mots commençant par 'a'
mots_commencant_par_a = []

# Parcourir la liste des mots et ajouter ceux qui commencent par 'a' (en ignorant la casse)
for mot in mots:
    if len(mot) > 0 and (mot[0] == 'a' or mot[0] == 'A'):
        mots_commencant_par_a.append(mot)

# Afficher les mots qui commencent par 'a'
print("Les mots commençant par 'a' sont :")
for mot in mots_commencant_par_a:
    print(mot)