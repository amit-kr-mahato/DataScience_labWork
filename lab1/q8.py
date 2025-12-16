year = input("Enter year: ")

if year.isdigit():
    year = int(year)
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print("Leap year")
    else:
        print("Not leap year")
else:
    print("Invalid input")
