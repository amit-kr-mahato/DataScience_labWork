n = input("Enter a number: ")

if n.isdigit():
    n = int(n)
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")
else:
    print("Invalid input")
