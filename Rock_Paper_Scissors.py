import random


is_running = True

print("   Rock, Paper, Scissors    ")
print("----------------------------")

while is_running:
    choice = ("rock", "paper", "scissors")
    computer = random.choice(choice)
    player = None
    while player not in choice:
        player = input("Please enter a choice (rock, paper, scissors): ").lower()
    print(f"computer: {computer}")
    print(f"you     : {player}")
    if computer =="rock" and player =="scissors":
        print("You lost!")
    elif computer == "rock" and player =="paper":
        print("You won!")
    elif computer == "paper" and player =="rock":
        print("You lost!")
    elif computer == "pape" and player =="scissors":
        print("You won!")
    elif computer == "scissors" and player =="paper":
        print("You lost!")
    elif computer == "scissors" and player =="rock":
        print("You won!")
    else:
        print("Tie!")

    if not input("Play again? (y to continue)").lower() == 'y':
        is_running = False

print("Thanks for playing!")
