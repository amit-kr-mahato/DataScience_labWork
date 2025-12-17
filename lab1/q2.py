 #2. Write a program that checks if a given string is palindrome.

s = input("Enter a string: ")
if len(s) == 0:
    print("Invalid input")
elif s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

