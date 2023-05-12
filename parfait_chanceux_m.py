def somDiv(n):
    diviseurs = []
    for i in range(1, n):
        if n % i == 0:
            diviseurs.append(i)
    return sum(diviseurs)


def estParfait(n):
    somDiv = sum([i for i in range(1, n) if n % i == 0])
    return somDiv == n


def estPremier(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def estChanceux(n):
    liste = list(range(1, n + 1))
    index = 1
    while len(liste) > index:
        del liste[index::index+1]
        index += 1
    return n in liste


print(somDiv(12))
print(estParfait(6))
print(estPremier(31))
print(estChanceux(11))
