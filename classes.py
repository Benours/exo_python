class MaClasse:
    def __init__(self, x=23):
        self.x = x
        self.y = x + 5

    def affiche(self, z=42):
        print("x =", self.x, "y =", self.y, "z =", z)


class Vecteur2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def affiche(self):
        print("x =", self.x, "y =", self.y)
