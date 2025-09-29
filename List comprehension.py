# List comprehension = A concise way to create lists in Python
#                      compact and easier to read than traditional loops
#                      [expression for value in interable if condition]

# Traditional loop
doubles_traditional = []
for x in range(1,11):
    doubles_traditional.append(x * 2)
print(doubles_traditional)

#List comprehension
doubles_lc = [x * 2 for x in range(1,11)]
print(doubles_lc)

triples= [y * 3 for y in range(1,11)]
print(triples)

square = [z * z for z in range(1,11)]
print(square)

fruits =["apple", "orange", "banana", "coconut"]
fruits =[fruit.upper() for fruit in fruits]
print(fruits)

fruit_chars =[fruit[0] for fruit in fruits]
print(fruit_chars)

#List comprehension with condition
digits = [2, 87, -3, 6, 10, 9, -5, -2]
negative_digit = [digit for digit in digits if digit < 0]
print(negative_digit)
positive_digit = [digit for digit in digits if digit >= 0]
print(positive_digit)
even_digit = [digit for digit in digits if digit % 2 == 0]
print(even_digit)
odd_digit = [digit for digit in digits if digit % 2 == 1]
print(odd_digit)
grades = [85, 90, 55, 30, 61, 99]
pass_grade = [grade for grade in grades if grade >= 60]
print(pass_grade)