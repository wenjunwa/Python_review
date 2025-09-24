# while loop = execute some code WHILE some condition is true
# logical condition
# while something is not true, keep on executing

# while something is true, keep on execution

# name = input("Enter your name: ")
#
# while name == "":
#     print("You did not enter your name")
#     name = input("Enter you name: ")
# print(f"Hello {name}!")

# age =  int(input("Enter your age: "))
#
# while age < 0:
#     print("Age can not be negative.")
#     age = int(input("Enter your age: "))
# print(f"You are {age} years old.")

#Keep execution WHILE some condition is not true
# fruit = input("Enter the fruit you like/q to exit: ")
# print(f"Yor like {fruit}.")
# while not fruit == "q":
#     fruit = input("Enter another fruit: ")
#     print(f"Yor like {fruit}.")
# print("Bye!")

#Use logical condition
num = int(input("Enter a number between 10 and 20: "))
while num < 10 or num > 20:
    num = int(input(F"{num} is invalid.Enter another number: "))
print(f"Your number is {num}")



