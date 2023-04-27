'''
This is the scoring criteria:-
Scores 91 - 100: Grade = "Outstanding"
Scores 81 - 90: Grade = "Exceeds Expectations"
Scores 71 - 80: Grade = "Acceptable"
Scores 70 or lower: Grade = "Fail"
'''

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

# to avoid Runtime error: 'Dict size changed during execution'
# we convert the Dict ==> List using list(Dict_Name) func.
for score in list(student_scores):
    if score >= '91':
        student_scores[score] = "Outstanding"
    elif score >= '81' and score <= '90':
        student_scores[score] = "Exceeds Expectations"
    elif score >= '71' and score <= '80':
        student_scores[score] = "Acceptable"
    elif score <= '70':
        student_scores[score] = "Fail"

print(student_scores)
