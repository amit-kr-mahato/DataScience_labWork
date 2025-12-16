age = input("Enter your age: ")

if age.isdigit():
    age = int(age)
    year = 2025 - age
    print("Birth year:", year)
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print("Birth year was a leap year")
    else:
        print("Birth year was not a leap year")
else:
    print("Invalid input")
