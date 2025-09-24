import csv
quizes = []
guesses = []
score = 0
question_numbers = 0

with open("/Users/wenj/PycharmProjects/Python_review/Quiz.csv", newline='', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    for row in reader:
        quizes.append(row)

print("                  QUESTIONS                                ")


for quiz in quizes:
    print("-----------------------------------------------------------")
    print(quiz[0])
    print(f"A. {quiz[1]}")
    print(f"B. {quiz[2]}")
    print(f"C. {quiz[3]}")
    print(f"D. {quiz[4]}")

    guess = input("Answer: ").upper()
    if guess == quiz[5]:
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect. Answer is {quiz[5]}")
    question_numbers += 1
    guesses.append(guess)

print("-----------------------------------------------------------")
print("                    RESULTS                                ")
print("-----------------------------------------------------------")
print(f"Answer:  ", end='')
for quiz in quizes:
    print(quiz[5], end=' ')
print()
print(f"Guesses: ", end='')
for guess in guesses:
    print(guess, end=' ')
print()
score = int (score / question_numbers *100)
print(f"Your score is {score}%")

