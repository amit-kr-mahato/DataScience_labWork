n = input("Enter n: ")

if n.isdigit():
    n = int(n)
    for num in range(2, n + 1):
        prime = True
        for i in range(2, num):
            if num % i == 0:
                prime = False
                break
        if prime:
            print(num)
else:
    print("Invalid input")
