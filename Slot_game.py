# Slot game
import random
import time

def spin():
    symbols = [
        "\U0001F352",
        "\U0001F349",
        "\U0001F34B",
        "\U0001F514",
        "\u2B50"
    ]
    return [random.choice(symbols) for num in range(3)]


def printing(results):
    print(" | ".join(results))

def reward(results, bet):
    reward = 0
    bet = int(bet)
    if results[0] == results[1] ==results[2]:
        if results[0] == "\U0001F352":
            reward += bet * 3
        elif results[0] == "\U0001F349":
            reward += bet * 5
        elif results[0] == "\U0001F34B":
            reward += bet * 10
        elif results[0] == "\U0001F514":
            reward += bet * 20
        elif results[0] == "\u2B50":
            reward += bet * 100
    else:
        print("You lost this bet.")

    return reward

def main():
    balance = 100
    print("************************")
    print("Welcome to python slots ")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐️")
    print("************************")

    while balance > 0:
        print(f"Current balance: ${balance}.")
        bet = input("place your bet amount: ")
        if not bet.isdigit():
            print("Please enter a number!")
        elif int(bet) > balance:
            print("Insufficient fund!")
        elif  int(bet) <= 0 :
            print("Bet should great than 0.")
        else:
            balance -=int(bet)
            print("Spinning")
            time.sleep(1)
            results = spin()
            printing(results)
            balance += reward(results, bet)
        if balance > 0:
            stop_play = input("Continue play (Y/N): ").upper()
            if not stop_play == 'Y':
                break

    print("Thanks for playing!")

if __name__ == '__main__':
    main()




