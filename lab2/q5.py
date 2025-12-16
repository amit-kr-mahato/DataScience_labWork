words = input("Enter words separated by spaces: ").split()
result = [word[::-1] if len(word) % 2 == 0 else word for word in words]
print("Processed words:", result)
