# taking input list of str separated by spaces
student_scores = input("\nInput a list of student scores ").split()

Highest = 0
# converting list and find out highest value present
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
    if student_scores[n] >= Highest:
        Highest = student_scores[n]

print(f"\nThe highest value from {student_scores} is: {Highest}\n")
