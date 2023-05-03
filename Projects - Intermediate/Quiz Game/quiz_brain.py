class QuizBrain():

    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def display_question(self):
        """Displays Q and Takes in User's Answer
        and Increments Q_num by 1 each time it is called"""
        Q = self.question_list[self.question_number]

        user_ans = input(
            f"\nQ{self.question_number + 1}. {Q.text}. (True/False?): ").lower()

        if user_ans == "t" or user_ans == "true":
            user_ans = "True"
        if user_ans == "f" or user_ans == "false":
            user_ans = "False"

        if user_ans == Q.answer:
            self.score += 1
            print("You got it right!")
        elif user_ans != Q.answer:
            print("That's wrong.")

        self.question_number += 1
        print(f"The correct answer was: {Q.answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
