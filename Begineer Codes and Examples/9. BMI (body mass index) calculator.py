# bmi calculator
bmi = round((float(input("Enter your weight in kgs: ")) /
            (float(input("Enter your height in m: ")) ** 2)), 2)

print(f"\nYour Body Mass Index (BMI) is {bmi}\n")
