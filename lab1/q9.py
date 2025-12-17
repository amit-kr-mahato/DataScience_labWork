# 9. Write a program that takes a temperature in Celsius, and converts it to Fahrenheit and Kelvin, based on the choice of user.
c = input("Enter temperature in Celsius: ")

if c.replace('.', '', 1).isdigit():
    c = float(c)
    choice = input("Convert to (F/K): ")

    if choice.upper() == "F":
        print("Fahrenheit =", (c * 9/5) + 32)
    elif choice.upper() == "K":
        print("Kelvin =", c + 273.15)
    else:
        print("Invalid choice")
else:
    print("Invalid input")
