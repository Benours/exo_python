class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        self.nom = "rectangle"

    def affiche(self):
        print(self.nom + " de largeur " + str(self.width) +
              " et de hauteur " + str(self.height))

    def aire(self):
        return self.width * self.height


class Carre(Rectangle):

    def __init__(self, width=0):
        super().__init__(width, width)
        self.nom = "carré"
