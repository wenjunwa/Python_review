# Membership operator = used to test whether a value or variable is found in a sequence
#                       (string, list, tuple, set, or dictionary)
#                       1. in
#                       2. not in
#
# word = "APPLE"
# letter = input("Guess a letter in the secret word: ").upper()
# if letter in word:
#     print(f"There is a {letter}")
# else:
#     print(f"{letter} is not found.")

# #set
# students = {"Spongebob", "Patrick", "Sandy"}
# student = input("Enter a name: ")
# if student in students:
#     print(f"{student} is a student.")
# else:
#     print(f"{student} is not found.")

# #dictionary
# grades = {"Sandy": "A",
#           "Squidward": "B",
#           "Spongebob": "C",
#           "Patrick": "D"}
# student = input("Enter a name: ")
# if student in grades:
#     print(f"{student}'s grade is {grades[student]}")
# else:
#     print(f"{student} is not found.")

email = "BroaCode@gmail.com"
if "@" in email and "." in email:
    print(f"{email} is a email address.")
else:
    print(f"{email} is not a valid email address.")