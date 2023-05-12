'''liste = [17, 38, 10, 25, 72]
print(sorted(liste))
liste.append(12)
print(liste)
liste.reverse()
print(liste)
print(liste.index(17))
liste.remove(38)
print(liste)
sous_liste = liste[1:3]
print(sous_liste)
sous_liste = liste[:2]
print(sous_liste)
print(liste[-1])
sous_liste = liste[2:]
print(sous_liste)
sous_liste = liste.copy()
print(sous_liste)
print(sous_liste[-1])'''

'''
truc = []
machin = [0.0, 0.0, 0.0, 0.0, 0.0]

print(truc)
print(machin)

for i in range(4):
    print(i)

for i in range(4, 8):
    print(i)

for i in range(2, 9, 2):
    print(i)

chose = [0, 1, 2, 3, 4, 5]

for i in chose:
    for j in range(3, 7):
        if i == j:
            print(str(j) + " est dans chose")

choseComprehension = [i + 3 for i in chose]
print(choseComprehension)
choseComprehension = [i + 3 for i in chose if i >= 2]
print(choseComprehension)

listeComprehension = [a + b for a in "abc" for b in "de"]
print(listeComprehension)
liste2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
somme = sum([i for i in liste2])
print(somme)'''

x = {"a", "b", "c", "d"}
y = {"s", "b", "d"}

print(x, y)
print("c" in x)
print("a" in y)
print(x & y)
print(x | y)
print(x - y)
print(y - x)
print(x ^ y)
print(x <= y)
print(x >= y)
print(x < y)
print(x > y)
print(x == y)
print(x != y)
