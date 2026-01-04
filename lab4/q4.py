# 4. Write a Python script that takes a list of six student names and uses the
# random.sample() function to randomly select exactly three "Volunteers" for a
# presentation, ensuring that no student is picked more than once in the selection.


import random

students = ["Amit", "Ravi", "Sita", "Gita", "Hari", "Nabin"]
random.seed(1)
volunteers = random.sample(students, 3)
print("volunteers:",volunteers)