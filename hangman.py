import random

mots = ["bonjour", "chat", "chien", "voiture", "maison", "pomme", "arbre", "ordinateur", "soleil", "jardin",
                "cafe", "livre", "musique", "jouet", "cadeau", "pere", "mere", "fleur", "mer", "ecole", "amour",
                "argent", "paris", "ville", "film", "photo", "vacances", "travail", "sport", "voyage", "musee",
                "eglise", "restaurant", "oiseau", "nuit", "journee", "enfant", "famille", "chapeau", "montagne",
                "velo", "train", "bouteille", "chemin", "table", "chambre", "fenetre", "lumiere", "bureau", "crayon"]

def hangmanGame():
    while True:
        x = 1
        wordToGuess = mots[random.randint(0, 49)]
        wordToSee = "_" * len(wordToGuess)
        print("Bienvenue ! J'ai choisi un mot, à toi de le deviner en 6 vie !")
        while x < 7:
            print(wordToSee)
            findLetter = False
            letter = input("Choisit une lettre : ")
            for i in range(len(wordToGuess)):
                if letter == wordToGuess[i]:
                    findLetter = True
                    wordToSee = wordToSee[:i] + letter + wordToSee[i+1:]
            if findLetter == False:
                x = x + 1
                print("Une vie en moins, il t'en reste " + str(7 - x) + ".")
            if wordToSee == wordToGuess:
                print(wordToSee)
                print("Bravo tu as trouvé ! Et il te reste " + str(7 - x) + " vie(s).")
                break
        if x > 5:
            print("Dommage, tu n'as pas réussi ! Le mot était " + wordToGuess + ".")
        reponse = input("Veux-tu recommencer ? (o/n) ")
        if reponse == "o":
            continue
        else:
            print("A bientot !")
            break


