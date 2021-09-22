import random

list_moves = ["Rock", "Paper", "Scissors"]
print("Start !!!\n")
rounds = input("Numbers of rounds: ")
computer_points = 0
user_points = 0
i=1
while i <= int(rounds):
    move_user = input("Make a move : ")
    move_computer=random.choice(list_moves)
    print("The computer chose :", move_computer)
    if (move_user == "Rock" and move_computer == "Scissors") or (move_user=="Scissors" and move_computer == "Paper") or (move_user=="Paper" and move_computer == "Rock"):
        user_points += 1
        print("You win")
        i+=1
        move_user=input("Make a move : ")
        print("The computer chose :", move_computer)
    elif move_user == move_computer :
        print("It's a draw\n")
        i+=1
        move_user=input("Make a move : ")
        print("The computer chose :", move_computer)
    else:
        computer_points +=1
        i+=1

print("\nFinal score\nUser:",user_points,"\nComputer:",computer_points)
if user_points > computer_points:
    print("You're the winner!!")
print("Sorry you loose, you sucks!!")

