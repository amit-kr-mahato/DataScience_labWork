# 5. Word Reverser Game
# Ask the user for a list of words. Reverse each word only if its length is even. Print the new list of
# words after processing.



words = input("Enter words separated by spaces: ").split()
result = [word[::-1] if len(word) % 2 == 0 else word for word in words]
print("Processed words:", result)
