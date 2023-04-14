# taking input a str of height values separated by spaces
student_heights = input("\n\nInput a list of student heights ").split()

Sum = 0  # initializing sum
# converting the input to a list and calculating average
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    Sum += student_heights[n]

print(
    f"\nThe Average of {student_heights} is {round(Sum/len(student_heights))}\n")
