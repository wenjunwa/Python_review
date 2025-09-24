#shopping cart program

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.upper() == 'Q':
        break
    else:
        price = float(input("Enter the price: "))
        foods.append(food)
        prices.append(price)

print("------ Your Shopping cart ----")
for food in foods:
    print(food, end=" ")

for price in prices:
    total += price
print()
print(f"Your total is : {total}")