import os
from time import sleep
from os import path
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
from art import logo


# empty list, which will contain all our Q and Ans
question_bank = []

# loop for accesing data from question_data and
# creating Question objects from it
for question in question_data:
    Q = Question(question["text"], question["answer"])
    question_bank.append(Q)

# giving the quizbrain total number of Q from Q_Bank
Quiz = QuizBrain(question_bank)

# displaying Q for the quiz using QuizBrain function
for _ in range(len(question_bank)):
    # printing our ASCII ART Logo
    print(logo)
    Quiz.display_question()
    print("\n\nMoving on to the next Question.")
    sleep(1)
    os.system('cls')

# printing feddback and player final score at end of Quiz
print(logo)
print("\nYou've completed the quiz")
print(f"Your final score is: {Quiz.score}/{Quiz.question_number}")
