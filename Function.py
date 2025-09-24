# function = A block of reusable code
#           place () after the function name to invoke it
# return = statement used to end a function
#           and send a result back to the caller

def birth_day_song (name, age):
    print(f"Happy birthday {name}!")
    print(f"You are {age} years old!")
    print()

names =[('Bob', 20), ('Ben',9), ('mimi', 7)]


for name in names:
    birth_day_song(name[0], name[1])

# practices of return
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    return num1 / num2
z = add(2,3)

print(subtract(10,2))

def creat_name(first, last):
    first = str(first).capitalize()
    last = str(last).capitalize()
    return first + " " + last
print(creat_name("wEnjuN", "wAng"))

