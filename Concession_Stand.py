# Concession stand program

menu = {"pizza" : 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries": 2.50,
        "chips": 1.00,
        "pretzel": 3.50,
        "soda": 3.00,
        "lemonade": 4.25}
cart = {}
total = 0

print("--------- MENU ------------")
for key, value in menu.items():
    print(f"{key:20}", end=" ")
    print(f"${value:<.2f}")
print("----------------------------")

while True:
    food = input("Choose an item (q to quit): ").lower()
    if food == 'q':
        break
    elif menu.get(food) is not None:
        cart.update({food:menu.get(food)})
        total += menu.get(food)
    else:
        print(f"Sorry, we don't have {food}!")
        print("please choose another one.")
print("----------Your Order-----------")

for key, value in cart.items():
    print(f"{key:20}", end=" ")
    print(f"${value:<.2f}")
print("----------------------------")
print(f"Total:                  {total}")



