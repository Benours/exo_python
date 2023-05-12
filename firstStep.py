# Cours n°1
import easygui
import math
from easygui import *

# 1

temps, distance = 6.892, 19.7
vitesse = temps * distance
print(vitesse)
print("{:.1f}".format(vitesse))

# 2

nom = input("Comment vous appelez-vous ?\n")
age_str = input("Quel age avez-vous ?\n")
age = int(age_str)

print("Vous êtes " + nom + " et vous avez " + str(age) + " ans.")

# Cours n°2

# 1

flt_str = input("Choisissez un nombre décimal :\n")
flt = float(flt_str)

if flt >= 0:
    print(math.sqrt(flt))
else:
    print("Error: " + str(flt) + " is under 0.")

# 2

mot1 = input("Choisissez un mot :\n")
mot2 = input("Choisissez un autre mot:\n")

if mot1 < mot2:
    print(mot1 + " est plus petit que " + mot2)
else:
    print(mot2 + " est plus petit que " + mot1)

plus_petit = mot1 if mot1 < mot2 else mot2

print("le plus petit des mots est " + plus_petit)

# 3

pSeuil, vSeuil = 2.3, 7.41

pCurrent_str = input("Quel est la pression courante :\n")
vCurrent_str = input("Quel est le volume courant :\n")
pCurrent = float(pCurrent_str)
vCurrent = float(vCurrent_str)

if pCurrent > pSeuil and vCurrent > vSeuil:
    print(" /!\ ARRET IMMEDIAT /!\ ")
elif pCurrent > pSeuil:
    print("DANGER : Veuillez augmenter le volume de l'enceinte.")
elif vCurrent > vSeuil:
    print("DANGER : Veuillez diminuer la pression de l'enceinte.")
else:
    print("INFO : Tout est okay.")

# 4

a, b = 0, 10

print("BOUCLE A :")

while a < b:
    print(a)
    a = a + 1

print("FIN BOUCLE A")

print("BOUCLE B")

while b > 0:
    if b % 2 == 1:
        print(b)
    b = b - 1

print("FIN BOUCLE B")

# 5

while True:
    valeur = input("Entrez un nombre entier positif entre 1 et 10 : ")
    if 0 < int(valeur) and int(valeur) < 11:
        break
    print("Veuillez entrer un nombre entier positif entre 1 et 10.")

# 6

mot = input("Veuillez choisir un mot :\n")

print("AFFICHAGE DU MOT CHOISIT")

for x in mot:
    print(x)

liste = ["al", "pha", "bet"]

print("AFFICHAGE D'UNE LISTE")

for x in liste:
    print(x)

# 7

print("AFFICHAGE D'UNE BOUCLE FOR DE 0 A 15 (pas de 3)")

for x in range(0, 15, 3):
    print(x)

# 8

print("AFFICHAGE D'UNE BOUCLE ET UTILISATION DU BREAK")

for x in range(11):
    print(x)
    if x == 5:
        break

# 9

print("AFFICHAGE D'UNE BOUCLE DE 1 A 10 SANS LE 5")

for x in range(1, 11):
    if x == 5:
        continue
    else:
        print(x)

# 10


for x in range(-3, 4):
    try:
        valeur = math.sin(x) / x
    except ZeroDivisionError:
        print("Error division by 0")
    else:
        print("Pour x = " + str(x) + " le resultat est : " + str(valeur))

# 11

liste = [6, 9, 22, 8, 29]

number = easygui.integerbox(msg="Entrez un nombre", title="Nombre",
                            lowerbound=0, upperbound=100)

if (number in liste):
    easygui.msgbox("Le nombre est dans la liste")
else:
    easygui.msgbox("Le nombre n'est pas dans la liste")
