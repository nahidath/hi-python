import random

def guessingGame(n1,n2):
    random_nb= random.randint(n1,n2)
    print(random_nb)
    nb_ask=input("A number was chosen randomly\nGuess the number:")
    while int(nb_ask) != random_nb:
        print("Wrong! Try again.\nHint: the number is between",n1, "and",n2)
        input("Guess the number :")
    if int(nb_ask) == random_nb:
        print("Yeahhhhh you win!!!")