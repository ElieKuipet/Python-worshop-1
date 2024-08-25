n = int(input("Saisissez votre nombre entier : "))
if n>=0:
    ListeDiviseurs=[]
    for i in range (1,n+1):
        if n % i == 0:
            ListeDiviseurs.append(i)
    print (f"L'ensemble des diviseurs de {n} est: {ListeDiviseurs}")
else:
    n = - n
    ListeDiviseursPositifs = []
    ListeDiviseursNegatifs = []
    for i in range(1, n + 1):
        if n % i == 0:
            ListeDiviseursPositifs.append(i)
    ListeDiviseursNegatifs = - 1 * ListeDiviseursPositifs
    print(f"L'ensemble des diviseurs de {-n} est: {ListeDiviseursNegatifs + ListeDiviseursPositifs}")



#Ex1
nom = input ("Entrez votre nom : ")
print(f"Bienvenue, {nom}!")
#Passage de variable en paramètre dans une  chhaine

#Ex2
a = float(input("Entrer le premier nombre: "))
b = float(input("Entrer le deuxième nombre: "))
somme = a + b
print(f"La somme de {a} et {b} est: {somme}")

# Ex3
a = float(input("Entrer le  premier nombre: "))
b = float(input("Entrer le  deuxième nombre: "))

c=max(a,b)
print(f"Le maximum de ces 2 nombres est: {c}")

#Ex4
print("Les 100 permiers nombres entiers sont:")
for i in range (1,101):
    print (i)

#Ex5
nombre = int(input("Saisissez votre nombre entier : "))

if nombre%2==0 :
    print(f" Le nombre {nombre} est pair")
else:
    print(f" Le nombre {nombre} est impair")

#Ex6
age=int(input("Saisissez votre âge: "))

if age>=18:
    print("Vous êtes majeur")
else:
    print("Vous êtes mineur")

#Ex 7
x = float(input ("Saisissez le 1er nombre: "))
y = float(input ("Saisissez le 2er nombre: "))
z = float(input ("Saisissez le 3er nombre: "))

maximum = max (x,y,z)
print(f"Le maximum de {x},{y} et {z} est: {maximum}")

#Ex8
nombre = int(input("Saisissez votre nombre entier : "))
somme = 0
for i in range (1,nombre+1):
    somme = somme + i
print (f"La somme de cette suite est: {somme}")

# Ex 9
n = int(input("Saisissez votre nombre entier : "))
facto = 1
if n==0 or n==1 :
    print(f"Le factoriel de {n} est : 1.")
else:
    for i in range(1, n + 1):
        facto = facto* i
    print(f"Le factoriel de {n} est: {facto}")

# Ex 10
r = float(input("Saisissez le rayon du cercle : "))
s = (r**2)*3.14
p = r*2*3.14
print (f"La surface de ce cercle est: {s}")
print (f"Le périmètre de ce cercle est: {p}")

#Ex11
n = int(input("Saisissez votre nombre entier : "))
if n>=0:
    liste.diviseurs=[]
    for i in range (1,n+1):
        if n % i == 0:
            liste.diviseurs.append(i)
    print ("L'ensemble des diviseurs de {n} est: {liste.diviseurs}")
else:
    n = - n
    ListeDiviseursPositifs = []
    ListeDiviseursNegatifs = []
    for i in range(1, n + 1):
        if n % i == 0:
            ListeDiviseursPositifs.append(i)
    ListeDiviseursNegatifs = - 1 * ListeDiviseursPositifs
    print(f"L'ensemble des diviseurs de {-n} est: {ListeDiviseursNegatifs + ListeDiviseursPositifs}")

#Ex12
n = int(input("Saisissez votre nombre entier: "))

for i in range (0,13):
    produit  = n*i
    print (f" {n} * {i} = {produit}")
    print()

for i in range (1,10):
    for j in range(0,13):
        produit = i * j
        print (f" {i} * {j} = {produit}")
    print()

#Ex13
a = int(input("Saisissez votre 1er nombre entier a: "))
b = int(input("Saisissez votre 2e nombre entier b: "))
if b==0:
    print ("Impossible d'effectuer une division par zéro")
else:
    quotient  = a//b
    reste = a%b
    print (f"Le quotient de la divison de {a} par {b} est: {quotient}")
    print(f"Le reste de la divison de {a} par {b} est: {reste}")