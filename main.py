import random

while True:
    
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper, or scissors: ").lower()

    if player == computer:
        print("computer", computer)
        print("player", player)
        print("It's a Tie!")

    elif player == "rock":
        if computer == "scissors":
            print("computer", computer)
            print("player", player) 
            print("You win!")
        if computer == "paper":
            print("computer", computer)
            print("player", player)
            print("You Lose!")

    elif player == "paper":
        if computer == "scissors":
            print("computer", computer)
            print("player", player)
            print("You win!")
        if computer == "rock":
            print("computer", computer)
            print("player", player)
            print("You Lose!")

    elif player == "scissors":
        if computer == "paper":
            print("computer", computer)
            print("player", player)
            print("You win!")
        if computer == "rock":
            print("computer", computer)
            print("player", player)
            print("You Lose!")

    # try_again = input("Try again? (yes/no):").lower()
    # if try_again != "yes":
    #            break

print("Thanks for playing!")



           