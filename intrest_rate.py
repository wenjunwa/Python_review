#compound interest calculator in python
principle = 0
rate = 0
time = 0

while True:
    principle = int(input("Enter principle:"))
    if principle <= 0:
        print("Principle can't be less than or equal to 0.")
    else:
        break

while True:
    rate = int(input("Enter interest rate:"))
    if rate <= 0:
        print("Interest rate can't be less than or equal to 0.")
    else:
        break

while True:
    time = int(input("Enter time in years:"))
    if time <= 0:
        print("time can't be less than or equal to 0.")
    else:
        break


print(f"Principle is {principle}")
print(f"Interest rate is {rate}")
print(f"Time is {time}")

compound = principle*pow((1 + rate/100),time)
print(f"Compound is {compound}!")