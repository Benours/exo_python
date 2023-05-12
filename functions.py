import math


def table(base, debut, fin, inc):
    for i in range(debut, fin, inc):
        print(base[i])


def cube(arg):
    return arg ** 3


def volumeSphere(r):
    return 4 / 3 * math.pi * cube(r)


def volMasseEllipsoide(a=1, b=1, c=1, masseVol=1):
    volume = 4 / 3 * math.pi * a * b * c
    masse = volume * masseVol
    return volume, masse


def somme(*args):
    total = 0
    for nombre in args:
        total += nombre
    return total


def somme2(a, b, c):
    return a + b + c


def unDictionnaire(**dico):
    print(dico)


def Pile(*args):
    return list(args)


def Empile(pile, element):
    pile.append(element)


def Depile(pile):
    if len(pile) == 0:
        raise IndexError("La pile est vide")
    return pile.pop()


queue = []


def ajouter_element():
    element = input("Entrez l'élément à ajouter à la queue: ")
    queue.append(element)
    print("L'élément", element, "a été ajouté à la queue.")


def supprimer_element():
    if not queue:
        print("La queue est vide.")
    else:
        element = queue.pop(0)
        print("L'élément", element, "a été supprimé de la queue.")


def afficher_queue():
    if not queue:
        print("La queue est vide.")
    else:
        print("Contenu de la queue:", queue)


def controlQueue():
    while True:
        print("\nMenu:")
        print("1. Ajouter un élément à la queue")
        print("2. Supprimer le premier élément de la queue")
        print("3. Afficher le contenu de la queue")
        print("4. Quitter")

        choix = input("Entrez votre choix: ")

        if choix == '1':
            ajouter_element()
        elif choix == '2':
            supprimer_element()
        elif choix == '3':
            afficher_queue()
        elif choix == '4':
            print("Fin du programme.")
            break
        else:
            print("Choix invalide.")
