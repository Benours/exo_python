import guessNumber
import hangman

while True:
    reponse = input("A quoi veux-tu jouer ?\n1 - pendu\n2 - devine le nombre\nAutre - quitter\nTu choisit : ")
    if reponse.isdigit() and int(reponse) == 1:
        hangman.hangmanGame()
    elif reponse.isdigit() and int(reponse) == 2:
        guessNumber.guessTheNumber()
    else:
        print("Au revoir !")
        break


