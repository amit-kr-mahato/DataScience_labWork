# 4. Write a python program that prints the Fibonacci series up to n terms.

n = input("Enter number of terms: ")

if n.isdigit():
    n = int(n)
    a, b = 0, 1
    for _ in range(n):
        print(a)
        a, b = b, a + b
else:
    print("Invalid input")
