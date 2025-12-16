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
