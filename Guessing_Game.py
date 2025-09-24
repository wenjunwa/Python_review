#Python number guessing game
import random

lowest = 1
highest = 100
number = random.randint(lowest,highest)

print(f"Python Number Guessing Game")
print(f"Select a number between {lowest} and {highest}")

while True:
    guess = input("Enter a number: ")
    if guess.isdigit():
        if int(guess) == number:
            break
        elif int(guess) < number:
            print("Your number is smaller than the answer!")
        else:
            print("Your number is larger than the answer!")
    else:
        print(f"Invalid input!Select a number between {lowest} and {highest}")

print("Congratulation! You got the correct number!")