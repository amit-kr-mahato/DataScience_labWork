
# 2. Unique Words Collector
# Take a paragraph input from the user. Split it into words, remove duplicates, sort them
# alphabetically, and count the total number of unique words.

paragraph = input("Enter a paragraph: ")
paragraph = paragraph.lower()

import string
paragraph = paragraph.translate(str.maketrans('', '', string.punctuation))

words = paragraph.split()
unique_list = []

for w in words:
    if w not in unique_list:
        unique_list.append(w)

sorted_unique = sorted(unique_list)
total_unique = len(sorted_unique)

print("Unique Words (alphabetically sorted):", sorted_unique)
print("Total Number of Unique Words:", total_unique)
