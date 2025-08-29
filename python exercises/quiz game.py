# Exercise — “Classic Quiz Game”

import random   # to shuffle the data from the dictionary — for looping
import time     # to create a short delay each question interval

question_1 = "What is the output of print(2**3)?"
option_1 = """
    A: 6
    B: 8
    C: 9
    D: 12
    """
answer_1 = "b"

question_2 = "Which keyword is used to define a function in Python?"
option_2 = """
    A: func
    B: def
    C: function
    D: lambda
    """
answer_2 = "b"

question_3 = "What data type is the result of 5 / 2 in Python 3?"
option_3 = """    
    A: int  
    B: float
    C: double
    D: string
    """
answer_3 = "b"

question_4 = "What keyword is used to create a class in Python?"
option_4 = """
    A: define
    B: new
    C: class
    D: object   
    """
answer_4 = "c"

# Create a dictionary from the questions
quiz = [
    {"question": question_1, "options": option_1, "answer": answer_1},
    {"question": question_2, "options": option_2, "answer": answer_2},
    {"question": question_3, "options": option_3, "answer": answer_3},
    {"question": question_4, "options": option_4, "answer": answer_4}
]

random.shuffle(quiz)

name = input("Enter Name: ").title()
print("""
      You will answer a set of questions.
      """)
time.sleep(3)

readyness = input("Are you ready? (y/n): ").lower()

while readyness != "y":
    print("""
          Take your time!
          """)
    time.sleep(3)
    readyness = input("Are you ready? (y/n): ").lower()

print("""
      Here are your questions...
      """)
time.sleep(3)

right_ans = 0
wrong_ans = 0

for q in quiz:
    print(q["question"])
    print(q["options"])
    ans = input("Enter Answer: ").lower()
    if ans == q["answer"]:
        right_ans += 1
    else:
        wrong_ans += 1
    print()
    time.sleep(3)

print("""
      Evaluating Answers...
      """)

grade = (right_ans / len(quiz)) * 100

print("----- RESULTS -----")
print(f"Name of player: {name}")
print(f"Number of Correct Answers: {right_ans}")
print(f"Number of Wrong Answers: {wrong_ans}")
print(f"Grade: {grade:.2f}%")
