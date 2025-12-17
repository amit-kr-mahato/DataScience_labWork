#A program that checks if a user is eligible for army entrance based on their BMI
# and age. The eligibility criteria are as follows:
# ■ Age must be between 18 and 40 years.
# ■ BMI must be within the range of 18.5 to 29.9.

age = input("Enter age: ")
bmi = input("Enter BMI: ")

if age.isdigit() and bmi.replace('.', '', 1).isdigit():
    age = int(age)
    bmi = float(bmi)
    if 18 <= age <= 40 and 18.5 <= bmi <= 29.9:
        print("Eligible for army")
    else:
        print("Not eligible for army")
else:
    print("Invalid input")
