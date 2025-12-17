# # 1. Write a program that takes two numbers as input from the user, and print their sum.


a = input("Enter first number: ")
b = input("Enter second number: ")

if a.isdigit() and b.isdigit():
    print("Sum =", float(a) + float(b))
else:
    print("Invalid input")
