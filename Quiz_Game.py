#create a quiz to show the questions, options. let students choose the options.
#compare the guesses and answers, give the percentage of correct ones.

# tuple of the questions
questions = ("How many elements are in the periodic table?",
             "which animal lays the largest eggs?",
             "What is the most abundant gas in Earth's atmosphere?",
             "How many bones are in the human body?",
             "Which planet in the solar system is the hottest?"
             )

# tuple of the options
options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Whale", "B. Crocodile", "C. Elephant", "D, Ostrich"),
           ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))
# tuple of the answers
answers= ("C", "D", "A", "A", "B")

# list of the guess
guesses = []
# number of the questions
question_number = 0
# number of correct guess
correct_guesses = 0
# score
score = 0


for question in questions:
    print("--------------------------------------------")
    print(question)
    for option in options[question_number]:
        print(option)
    guess = input("Answer: ").upper()
    guesses.append(guess)
    if guess.upper() == answers[question_number]:
        print("correct!")
        score += 1
    else:
        print(f"Incorrect! The right answer is {answers[question_number]}")
    question_number += 1

print("--------------------------------------------")
print("             RESULTS                        ")
print("--------------------------------------------")
print("Answer:", end=" ")
for answer in answers:
    print(answer, end = " ")
print()
print("Guess:", end="  ")
for guess in guesses:
    print(guess, end = " ")
print()
score = int(score/question_number*100)
print(f"Your score is: {score}%")