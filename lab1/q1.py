a = input("Enter first number: ")
b = input("Enter second number: ")

if a.isdigit() and b.isdigit():
    print("Sum =", float(a) + float(b))
else:
    print("Invalid input")
