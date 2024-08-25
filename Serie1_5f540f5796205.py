#import re

# # Exercice 1
# name = input("Enter your name : ")
# print("Bienvenue " + name)
# print(f"Bienvenue, {name}!")
# print()
#
# # Exercice 2
# a = float(input("Enter the first nber: "))
# b = float(input("Enter the 2nd nber: "))
# somme = a + b
# print(f"The sum of those 2 numbers is : {somme}")
# print()
#
# # Exercice 3
# a = float(input("Enter the first nber: "))
# b = float(input("Enter the 2nd nber: "))
# if a > b:
#     print(f"{a} is the greatest ")
# else:
#     print(f"{b} is the greatest")
# print()
#
# # Exercice 4
# print("The 100 first integers are: ")
# for i in range(1, 101):
#     print(i)
# print()
#
# # Exercice 5
# n = int(input("Enter an integer: "))
# if n % 2 == 0:
#     print("Even number")
# else:
#     print("odd number")
# print()
#
# # Exercice 6
# age = float(input(" How old are you? "))
# if age >= 18:
#     print("You are a major")
# else:
#     print("You are a minor")
# print()
#
# # Exercice 7
# x = float(input("Enter your 1st number: "))
# y = float(input("Enter your 2nd number: "))
# z = float(input("Enter your 3rd number: "))
#
# if x > y:
#     if x > z:
#         print(f"{x} is the greatest")
#     else:
#         print(f"{z} is the greatest")
# else:
#     if y > z:
#         print(f"{y} is the greatest")
#     else:
#         print(f"{z} is the greatest")
# print()
#
# # Exercice 8
# n = int(input("Enter an integer: "))
# num_seq = 0
# for i in range(1, n+1):
#     num_seq = i + num_seq
# print(f"The value of this numerical sequence from 1 to {n} is: {num_seq}")
# print()
#
# # Exercice 9
# n = int(input("Enter an integer: "))
# facto = 1
# if n == 0 or n == 1:
#     print(f"Factorial {n} is 1 ")
# else:
#     for i in range(1, n+1):
#         facto = i * facto
#     print(f"Factorial {n} is {facto}")
# print()
#
# # Exercice 10
# r = float(input("Enter the ray of the circle: "))
# s = (r**2)*3.14
# p = 2*r*3.14
# print(f"The surface of this circle is {s}")
# print(f"The perimeter of this circle is {p}")
# print()
#
# # Exercice 11
# n = int(input("Enter an integer: "))
# listPositiveDivisors = []
# listNegativeDivisors = []
#
# if n < 0:
#     for i in range(n, 0):
#         if n % i == 0:
#             listNegativeDivisors.append(i)
#     for j in range(1, (-1*n)+1):
#         if n % j == 0:
#             listPositiveDivisors.append(j)
#     print(f"The list of divisors of {n} is : {listNegativeDivisors + listPositiveDivisors}")
# else:
#     for i in range(1, n+1):
#         if n % i == 0:
#             listPositiveDivisors.append(i)
#     for j in range((-1*n), 0):
#         print(j)
#         if n % j == 0:
#             listNegativeDivisors.append(j)
#     print(f"The list of divisors of {n} is: {listNegativeDivisors + listPositiveDivisors}")
# print()
#
# # Exercice 12
# n = int(input("Enter an integer: "))
#
# for i in range(0, 13):
#     product = n * i
#     print(f"{n} * {i} = {product}")
# print()
#
# for i in range(1,10):
#     for j in range(13):
#         product = i * j
#         print(f"{i} * {j} = {product}")
#     print()
# print()
#
# # Exercice 13
# a = int(input("Enter your 1st number: "))
# b = int(input("Enter your 2nd number: "))
#
# if b == 0 or a == 0:
#     print("La  division est impossible. Entrer un diviseur correct")
# elif a >= b:
#     q = a // b
#     r = a % b
#     print(f"le quotient de la division de {a} par {b} est {q}")
#     print(f"Le reste de la division de {a} par {b} est {r}")
# else:
#     a, b = b, a
#     q = a // b
#     r = a % b
#     print(f"le quotient de la division de {a} par {b} est {q}")
#     print(f"Le reste de la division de {a} par {b} est {r}")
#
# # Exercice 14
# n = int(input("Enter an integer: "))
#
# for i in range(n+1):
#     if i * i == n:
#         print(f"{n} est un carré parfait")
#         print(i)
#         break
# print()
#
# # Exercice 15
# n = int(input("Enter an integer: "))
# i = 2
# while i < n and n % i != 0:
#     i += 1
# if i == n:
#     print(f"{n} est un nombre premier ")
# else:
#     print(f"{n} n'est pas un nombre premier ")
#
# # Exercice 16
# char = input("Entrer votre chaîne de caractères: ")
# for x in char:
#     print(x)
#
# # Exercice 17
# char = input("Entrer votre chaîne de caractères: ")
# dict = {}
# for x in char:
#     if x in dict.keys():
#         dict[x] += 1
#     else:
#         dict[x] = 1
# for key in dict:
#     print(f'Le caractère : {key} figure {dict[key]} fois dans la chaine {char}')

# # Exercice 18
# s = input("Enter your string: ")
# liste = list(s)
# print(liste)
#
# for index, item in enumerate(liste):
# # Transforme la structure du tableau en un tableau de tuples : enumerate() returns a tuple containing a count (from start which defaults to 0) and the values obtained from iterating over iterable
#     if item == "a":
#         print(f"La lettre {item} se trouve à la position {index} ")
# print()
# print(list(enumerate(liste)))

# # Exercice 19
# list = ["laptop", "iphone", "tablet"]
# for x in list:
#      print(x, "est de longueur", len(x))

# Exercice 20
# char = input("Enter your string: ")
# liste_char = list(char)
# tmp = liste_char[0]
# liste_char[0] = liste_char[-1]
# liste_char[-1] = tmp
# print(liste_char)
# final_char = ''
# for x in liste_char:
#     final_char = final_char + x
# print(final_char)

# name = input("Enter your char: ")
# part1 = name[:1]
# part2 = name[1:-1]
# part3 = name[-1:]
# print(part3 + part2 + part1)

# txt = "apple#banana#cherry#orange"
# # setting the maxsplit parameter to 1, will return a list with 2 elements!
# x = txt.split("#", 1)
# print(x)

# # Exercice 21
# s = "anticonstitutionnellement"
# liste = list(s)
# vowels = ["a", "e", "i", "o", "u"]
# compteur = 0
# for index,item in enumerate(liste):
#     for x in item:
#         if x in vowels:
#             print(x)
#             compteur += 1
#
# print("La chaîne anticonstitutionnellement possède", compteur, "voyelles")

# Exercice 22
#text = input("Entrer votre texte: ")
# liste = t.split()
# print(liste)
# print(f"Le premier mot de votre texte est: {liste[0]}")

#text = input("Entrer votre texte: ")

# word = ""
# Trouve = False
# Mais cette méthode n'est pas conseillé en algo
# for character in text:
#     if character != " ":
#         word += character
#     else:
#         break
# print(word)

# word = ""
# Trouve = False
# i = 0
# while i < len(text) and not Trouve:
#     if text[i] != " ":
#         word += text[i]
#         i += 1
#     else:
#         Trouve = True
# print(f"Le permier mot de ce texte est: {word}")


# # Exercice 23
# nom_fichier = input("Saisissez le nom de votre fichier avec son extension: ")
# liste = nom_fichier.split('.')
# print(f"L'extension du fichier est .{liste[-1]}")

# nom_fichier = input("Saisissez le nom de votre fichier avec son extension: ")
# extension = ""
# i = len(nom_fichier) - 1
# Trouve = False

#print(len(nom_fichier))
# while i >= 0:
#     print(nom_fichier[i])
#     i = i - 1

# while i>=0 and not Trouve:
#     if nom_fichier[i] != ".":
#         # extension += nom_fichier[i]
#         extension = nom_fichier[i] + extension
#         i -= 1
#     else:
#         #extension = "." + extension[::-1] #La concaténation à l'inverse (Revoir le +=)
#         extension = "." + extension
#         Trouve = True
# print(f"L'extension est: {extension}")
# #print(f"L'extension est: .{extension[::-1]}")


# # Exercice 24
# test_palindrome = input("Enter your string and we will test if it is a palindrome: ")
# normal_liste = list(test_palindrome)
# reversed_list = normal_liste[::-1]
# if normal_liste == reversed_list:
#     print("Votre mot est un palindrome")
# else:
#     print("Votre mot n'est pas un palindrome")
# print()

# test_palindrome = input("Enter your string and we will test if it is a palindrome: ")
# Trouve = False
# i = 0
# j = len(test_palindrome) - 1
# while i <= j and not Trouve:
#     if test_palindrome[i] == test_palindrome[j]:
#         i += 1
#         j -= 1
#     else:
#         print(f"le mot {test_palindrome} n'est pas un palindrome")
#         Trouve = True
# print(f"le mot {test_palindrome} est un palindrome")

# def palindrome(text):
#     trouve = True
#     i = 0
#     j = len(text) - 1
#     while i <= j and trouve:
#         if text[i] == text[j]:
#             i += 1
#             j -= 1
#         else:
#             trouve = False
#     return trouve
#
#
# text = input("Enter a string: ")
# Result = palindrome(text)
# print(Result)


# # Exercice 25 (Revenir dessus!!!)
# char = input("Enter your string: ")
# liste = list(char)
# reversed_list = liste[::-1]
# reversed_char = ''
# for x in reversed_list:
#     reversed_char += x
# print("L'inverse de votre mot est:", reversed_char)

# Good
# char = input("Enter your string: ")
# Trouve = False
# i = len(char) - 1
# word = ''
# while i >= 0 and not Trouve:
#     word += char[i]
#     i -= 1
# print(word)

# # Exercice 26
# text = input("Enter your text: ")
# liste = text.split()
# print("Voici la liste des mots commençants par la lettre a:")
# for any_word in liste:
#     word = list(any_word)
#     if word[0] == 'a':
#         print(f"{any_word}\t")

# text = input("Saisir un texte: ")
# mots = []  # Une liste vide pour stocker tous les mots
# mot = ''   # Une chaîne vide pour construire chaque mot
#
# i = 0
#
# while i <= len(text)-1 :
#
#     if text[i] == ' ':
#         mots.append(mot)
#         mot = ''
#
#     elif i == len(text)-1:
#         mot = mot + text[i]
#         mots.append(mot)
#
#     else:
#         mot += text[i]
#         print(mot)
#     i += 1
#
# print(mots)
#
# mots_commencant_par_a = []
#
# for mot in mots:
#     if mot[0] == 'a':
#         mots_commencant_par_a.append(mot)
# print("Les mots commençant par la lettre a", mots_commencant_par_a)
#
# # optimiser la dernière compararaison

# # Exercice 27
# liste = []
# Trouve = True
# while Trouve:
#     user_input = input("Entrer vos nombres ('end' to finish): ")
#     if user_input != 'end':
#         user_input_number = float(user_input)
#         liste.append(user_input_number)
#     else:
#         Trouve = False
# print(liste)
#
#
# def sum_list(liste):
#     sum = 0
#     for i in liste:
#         sum += i
#     return sum
#
# def mul_list(liste):
#     produit = 1
#     for i in liste:
#         produit = produit * i
#     return produit
#
# somme_de_liste = sum_list(liste)
# produit_de_liste = mul_list(liste)
#
# print(f"La somme de cette liste est: {somme_de_liste}")
# print(f"Le produit de cette liste est: {produit_de_liste}")

# # Exercice 28
# list = []
# while True:
#     user_input = input("Input an item (type 'end' to finish): ")
#     if user_input == "end":
#         break
#     list.append(user_input)
#
# if bool(list) == True:
#     print("Votre liste n'est pas vide")
# else:
#     print("Votre liste est vide")

# liste = []
# trouve = True
#
# while trouve:
#     user_input = input("Enter an element('end' to finish: ")
#     if user_input != 'end':
#         liste.append(user_input)
#     else:
#         trouve = False
#
# print(len(liste))
#
# def test_list(liste):
#     if len(liste) == 0:
#         return False
#     else:
#         return True
# Resultat = test_list([])
# print(Resultat)


# # Exercice 29
# liste = []
# Tmp = True
# while Tmp:
#     user_input = input("Entrer les éléments des votre liste ('end' pour finir)): ")
#     if user_input == "end":
#        Tmp = False
#        break
#     liste.append(user_input)
# print(liste)
# set_liste = set(liste)
# print(set_liste)
# # Le set va d'abord prendre les élts uniques et revenir sur les doublons

# liste = []
# trouve = True
#
# while trouve:
#     user_input = input("Enter an element('end' to finish: ")
#     if user_input != 'end':
#         liste.append(user_input)
#     else:
#         trouve = False
#
#
# def suppression_doublons_de_liste(liste):
#     print(liste)
#     short_list = []
#     short_list.append(liste[0])
#
#     for element in liste:
#        if element not in short_list:
#              short_list.append(element)
#     return short_list
#
# resultat = suppression_doublons_de_liste(liste)
# print(resultat)


# # Exercice 30
# def compare_list(liste1,liste2):
#     liste1 = []
#     liste2 = []
#     trouve = True
#     valeur_commune = False
#
#     while trouve:
#         user_input = input("Entrer les éléments de la liste 1('end' to finish: ")
#         if user_input != 'end':
#             liste1.append(user_input)
#         else:
#             trouve = False
#
#     while not trouve:
#         user_input = input("Entrer les éléments de la liste 2('end' to finish: ")
#         if user_input != 'end':
#             liste2.append(user_input)
#         else:
#             trouve = True
#     print(f"la liste 1 : {liste1}")
#     print(f"la liste 2 : {liste2}")
#
#
#     for valeur1 in liste1:
#         for valeur2 in liste2:
#             if valeur1 == valeur2:
#                 valeur_commune = True
#     return valeur_commune
#
# Result = compare_list ([],[])
# print(Result)
# # Si je mets directement les listes liste1 et liste2 en paramètre, on dit qu'elles ne sont pas définies. Je crois que c'est du fait qu'elles soient désormais des variables locales.
#
#
# # Exercice 31
# liste = []
# while True:
#     user_input = input("Entrer les nombres qui constituent votre liste ('end' pour clôturer): ")
#     if user_input == 'end':
#         break
#     user_input_nber = int(user_input)
#     liste.append(user_input_nber)
# print(liste)
#
# liste_nbresPairs = []
# liste_nbresImpairs = []
#
# for i in liste:
#     if i % 2 == 0:
#         liste_nbresPairs.append(i)
#     else:
#         liste_nbresImpairs.append(i)
# print("La liste des nombres pairs est:", liste_nbresPairs)
# print("La liste des nombres impairs est:", liste_nbresImpairs)

# # Exercice 32
# liste = []
# while True:
#     user_input = input("Entrer les éléments de votre liste ('end' pour clôturer): ")
#     if user_input == 'end':
#         break
#     liste.append(user_input)
# print(liste)
# print()
#
# for i in liste:
#     print(i)
#     normal_liste = list(i)
#     reversed_liste = normal_liste[::-1]
#     print(reversed_liste)
#    print()

# # Exercice 33
# char = input("Saisissez votre chaîne de carcatères: ")
# chaine_paire = ''
# for i in range(0,len(char),2):
#     chaine_paire += char[i]
# print(f"Les caractères d'indice pair sont: {chaine_paire}")


# # Exercice 34
# notes = [12, 4, 14, 11, 18, 13, 7, 10, 5, 9, 15, 8, 14, 16]
# good_notes = []
# for note in notes:
#     if note >= 10:
#         good_notes.append(note)
# print("Les notes au dessus de la moyenne sont:", good_notes)

# # Exercice 35 ??????
# #http = 'http://www.regisatemengue.com'
# adresse_url = input('Saisir une adresse url: ')
# adresse_http = 'http://' + adresse_url
# print(adresse_http)

# # Exercice 36
# text = input("Enter your text: ")
# i = 0
# mot_final =''
#
# while i <= len(text)-1:
#     if text[i] != ' ':
#         mot_final += text[i]
#     else:
#         mot_final += text[i+1]
#     i += 1
# print(mot_final)

# # Exercice 37
# s1 = input("Enter your text: ")
# s2 = input("Enter your text: ")
#
# liste1 = s1.split()
# liste = []
#
# for element in liste1:
#     if element in s2:
#         liste.append(element)
# print(liste)

# # Exercice 38
# text = input("Saisir un texte: ")
# i = 0
# word = ''
# mots = []
#
# while i <= len(text)-1:
#     if text[i] != ' ':
#         word += text[i]
#     elif text[i] == ' ':
#         mots.append(word)
#         word = ''
#         word += text[i+1]
#     else:
#         word += text[i]
#     i += 1

#  une fonction quui détermine le maximum d'une liste de nombres
# def longest_word(liste):
#     max = liste[0]
#     for element in liste:
#         if len(max) < len(element):
#             max = element
#     return max
#
# Result = longest_word(['ab','cb','abcg'])
# print(Result)

# # Exercice 39
# s1 = input("Enter your text: ")
# liste = s1.split()
# print(liste)
# print("Le nombre de mots de ce texte est de :", len(liste))

# Exercice 40
# s = input("Enter your text: ")
# list1 = s.split()
# list1.index[0], list1.index[-1] = list1.index[-1], list1.index[0]
# print(list1)

def somme():
    a = float(input("Entrer la valeur de votre 1er nombre:"))
    b = float(input("Entrer la valeur de votre 2er nombre:"))
    sum = a + b
    return sum
resultat = somme()


# print(f"La somme de {a} et {b} est {resultat}") ici, pb de portée
print(f" La somme de ces 2 nombres est {resultat}")
