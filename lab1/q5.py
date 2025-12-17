# 5. Define a function that takes two numbers as arguments, and returns their greatest common divisor (GCD).
a = input("Enter first number: ")
b = input("Enter second number: ")

if a.isdigit() and b.isdigit():
    a = int(a)
    b = int(b)
    while b != 0:
        a, b = b, a % b
    print("GCD =", a)
else:
    print("Invalid input")
