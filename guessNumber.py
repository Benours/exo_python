import random

def guessTheNumber():

    while True:
        x = 1
        numberToGuess = random.randint(1, 30)
        print("Bienvenue ! J'ai choisi un nombre entre 1 et 30, à toi de le deviner en 5 tentatives !")
        while x < 6:
            print("Essai n°" + str(x))
            guess_str = input("Votre proposition : ")
            guess = int(guess_str)
            if guess > numberToGuess:
                print("Trop grand !")
            elif guess < numberToGuess:
                print("Trop petit")
            else:
                print("Bravo tu as trouvé en " + str(x) + " tentatives.")
                break
            x = x + 1
        if x > 5:
            print("Dommage, tu n'as pas réussi ! Le nombre était " + str(numberToGuess) + ".")
        else:
            reponse = input("Veux-tu recommencer ? (o/n) ")
            if reponse == "o":
                continue
            else:
                print("A bientot !")
                break



