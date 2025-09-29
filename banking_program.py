# banking program
# function: show balance
#           deposit
#           withdraw

def show_options():
    print("Banking program")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

def show_balance(balance):
    print(f"Your balance is ${balance: .2f}!")

def deposit_withdraw():
    amount = input("Enter the deposit number: ")
    if (not amount.isdigit()) and float(amount) < 0:
        print("That is not a valid number.")
        return 0
    else:
        return float(amount)

def withdraw(balance):
    amount = input("Enter the withdraw number: ")
    if (not amount.isdigit()) and float(amount) < 0:
        print("That is not a valid number.")
        return 0
    elif float(amount) > balance:
        print("Not suffician amount in your accout.")
        return 0
    else:
        return float(amount)

def main():
    balance = 0
    is_running = True
    is_not_digit = True
    choice = 0


    while is_running:
        while is_not_digit:
            show_options()
            choice = input("Enter your choice(1-4): ")
            if not choice.isdigit():
                print("Not a valid option.")
            else:
                choice = int(choice)
                is_not_digit = False

            match choice:
                case 1:
                    show_balance(balance)
                    is_not_digit = True
                case 2:
                    balance += deposit_withdraw()
                    show_balance(balance)
                    is_not_digit = True
                case 3:
                    balance -= withdraw(balance)
                    show_balance(balance)
                    is_not_digit = True
                case 4:
                    is_running = False
                case _:
                    #print("Not a valid input.")
                    is_not_digit = True
    print("Thank you! Have a nice day!")

    pass

if __name__ == '__main__':
    main()