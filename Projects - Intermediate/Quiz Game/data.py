import random

dataBase = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
    {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
    {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
    {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
    {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
    {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
    {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
    {"text": "Google was originally called 'Backrub'.", "answer": "True"},
    {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
    {"text": "No piece of square dry paper can be folded in half more than 7 times.",
        "answer": "False"},
    {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"},
    {"text": "The HTML5 standard was published in 2014.", "answer": "True"},
    {"text": "The first computer bug was formed by faulty wires.", "answer": "False"},
    {"text": "FLAC stands for 'Free Lossless Audio Condenser'.", "answer": "False"},
    {"text": "All program codes have to be compiled into an executable file in order to be run. This file can then be executed on any machine.", "answer": "False"},
    {"text": "Linus Torvalds created Linux and Git.", "answer": "True"},
    {"text": "The programming language 'Python' is based off a modified version of 'JavaScript'.", "answer": "False"},
    {"text": "AMD created the first consumer 64-bit processor.", "answer": "True"},
    {"text": "'HTML' stands for Hypertext Markup Language.", "answer": "True"},
    {"text": "In most programming languages, the operator ++ is equivalent to the statement '+= 1'.", "answer": "True"},
    {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
    {"text": "The IBM PC used an Intel 8008 microprocessor clocked at 4.77 MHz and 8 kilobytes of memory.", "answer": "False"},
]

question_data = []
# creating a question Database of only 10 question's
for _ in range(10):
    Q = random.choice(dataBase)
    # to get unique Q each time
    while Q in question_data:
        Q = random.choice(dataBase)
    question_data.append(Q)
