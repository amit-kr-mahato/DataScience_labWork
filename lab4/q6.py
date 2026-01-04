# 6. Given a list of student names and a list of their corresponding scores, use the zip()
# function to pair them together and then apply the reduce() function from the
# functools module to calculate the total sum of all scores.

from functools import reduce

names = ["Amit", "Ravi", "Sita", "Gita"]
scores = [80, 75, 90, 85]

paired = list(zip(names, scores))
total_score = reduce(lambda x, y: x + y, scores)
print(paired)
print(total_score)