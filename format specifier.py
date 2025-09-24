# format specifiers = {value: flags} format a value based on what flags are inserted

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocated and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# :  = insert a space before positive numbers
# :, =comma separator

price1 = 3000.14159
price2 = -9870.65
price3 = 120.34

#round to a specified decimal place
print(f"Price 1 is ${price1:.3f}")
print(f"Price 2 is ${price2:.3f}")
print(f"Price 3 is ${price3:.3f}")

#allocate spaces
print(f"Price 1 is ${price1:10}")
print(f"Price 2 is ${price2:10}")
print(f"Price 3 is ${price3:10}")

#padding
print(f"Price 1 is ${price1:010}")
print(f"Price 2 is ${price2:010}")
print(f"Price 3 is ${price3:010}")

# left justify
print(f"Price 1 is ${price1:<10}")
print(f"Price 2 is ${price2:<10}")
print(f"Price 3 is ${price3:<10}")

#right justify
print(f"Price 1 is ${price1:>10}")
print(f"Price 2 is ${price2:>10}")
print(f"Price 3 is ${price3:>10}")

#center justify
print(f"Price 1 is ${price1:^10}")
print(f"Price 2 is ${price2:^10}")
print(f"Price 3 is ${price3:^10}")

# + sign for positive number
print(f"Price 1 is ${price1:+}")
print(f"Price 2 is ${price2:+}")
print(f"Price 3 is ${price3:+}")

# space for positive number, so the numbers aligns evenly
print(f"Price 1 is ${price1: }")
print(f"Price 2 is ${price2: }")
print(f"Price 3 is ${price3: }")

# add comma in digits
print(f"Price 1 is ${price1: ,}")
print(f"Price 2 is ${price2: ,}")
print(f"Price 3 is ${price3: ,}")

# add comma in digits with 2 decimal places
print(f"Price 1 is ${price1: ,.2f}")
print(f"Price 2 is ${price2: ,.2f}")
print(f"Price 3 is ${price3: ,.2f}")