# def valide(x):
#     if x == 1 or 2 or 3:
#         print("bien")
#     else:
#         print("mal")
# valide(-5)
# print()


# # Exercice 4
# def valide(x):
#     if x == 1 or x == 2 or x == 3:
#         print("bien")
#     else:
#         print("mal")
#     return
#
#
# Resultat = valide(4)
# print("le programme affiche", Resultat)


# Exercice 5
def nand(a, b):
    if a == 0:
        return 1
    if b == 0:
        return 1
    return 0


def non(a):
    return nand(a, a)


def ou(a, b):
    return nand(non(a), non(b))


def et(a, b):
    return non(nand(a, b))


def xor(a, b):
    return et((ou(a, b)), non(et(a, b)))


def lambdan(a, b):
    return ou(a, et(a, b))


def table2(fonction):
    print("a", "b", "f(a,b)")
    for a in range(2):
        for b in range(2):
            print(a, b, fonction(a, b))
    return


print("Table de vérité de NAND:")
table2(nand)
print()

print("Table de vérité de OR:")
table2(ou)
print()

print("Table de vérité de ET:")
table2(et)
print()

print("Table de vérité de XOR:")
table2(xor)


# Il ne fallait plus redéfinir de cette façon
# def xor(a, b):
#     if a == 1 and b == 1:
#         return 0
#     if a == 1:
#         return 1
#     if b == 1:
#         return 1
#     return 0


def nand(a, b, c):
    if a == 1 and b == 1 and c == 1:
        return 0
    return 1


def table_verite_fonction_de_3_parametres(fonction):
    print("a, b, c, f(a,b,c)")
    for a in range(2):
         for b in range(2):
             for c in range(2):
                 print(a, b, c, fonction(a, b, c))
    return

print()
print("Table de vérité du NAND à 3 paramètres:")
table_verite_fonction_de_3_parametres(nand)