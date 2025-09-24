# iterables = an object/collection that can return its elements one at a time
#             allowing it to be iterated over in a loop
#             list, tuple, set, string

numbers = [1,2,3,4,5,]
for number in numbers:
    print(number, end=" ")

print()

fruits = {"apple", "pear", "banana", "pineapple", "peach"}
for fruit in fruits:
    print(fruit, end=" ")

print()

name = "Bro Code"
for char in name:
    print(char, end="")
print()

my_dictionary = {"A": 1, "B": 2, "C": 3}
for key in my_dictionary:
    print(key, end=" ")
