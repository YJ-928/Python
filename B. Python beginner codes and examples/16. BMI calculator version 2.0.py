# BMI calculator
# taking inputs and calulating bmi
bmi = round((float(input("Enter your weight in kgs: ")) /
            (float(input("Enter your height in m: ")) ** 2)), 2)

# printing out the correct BMI based on result using multiple if/elif/else.
print(f"Your BMI is {bmi}, you are clinically obese") if (bmi >= 35) else print(f"Your BMI is {bmi}, you are obese") if (bmi >= 30 and bmi < 35) else print(f"Your BMI is {bmi}, you are overweight") if (
    bmi >= 25 and bmi < 30) else print(f"Your BMI is {bmi}, you are normal weight") if (bmi >= 18.5 and bmi < 25) else print(f"Your BMI is {bmi}, you are under weight")
