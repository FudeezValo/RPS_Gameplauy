import random

def get_choices():
    player_choice = input("Enter your choice(rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")
    if player == computer:
        return "Its a Tie!!"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors!You win Awesome!"
        else:
            return "Paper covers rock! You lose!!"
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock! You WON!!"
        else:
            return "Scissors cut paper! Haha You Lose!!"
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cut paper,Haha You Won!!"
        else:
            return "Rock smashes scissors!You win Awesome!"

choices= get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)