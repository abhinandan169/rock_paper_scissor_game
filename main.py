import random

player_score = 0
computer_score = 0

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
            player_score += 1

        elif computer == "paper":
            print("computer", computer)
            print("player", player)
            print("You Lose!")
            computer_score += 1

    elif player == "paper":
        if computer == "scissors":
            print("computer", computer)
            print("player", player)
            print("You Lose!")
            computer_score += 1

        elif computer == "rock":
            print("computer", computer)
            print("player", player)
            print("You Win!")
            player_score += 1

    elif player == "scissors":
        if computer == "paper":
            print("computer", computer)
            print("player", player)
            print("You win!")
            player_score += 1

        elif computer == "rock":
            print("computer", computer)
            print("player", player)
            print("You Lose!")
            computer_score += 1


    print("\n----- Score -----")
    print(f"Player   : {player_score}")
    print(f"Computer : {computer_score}")
    print("-----------------\n")        

    try_again = input("Try again? (yes/no): ").lower()
    if try_again != "yes":
        break

print("\nFinal Score")
print(f"Player   : {player_score}")
print(f"Computer : {computer_score}")
print("Thanks for playing!")

print("Thanks for playing!")