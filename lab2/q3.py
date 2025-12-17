# 3. Student Marks Manager
# Store student names as keys and marks (list of integers) as values in a dictionary. Compute
# each student’s average and grade (A/B/C/D). Print the top 2 students based on average marks.


students = {}
count = int(input("How many students? "))

for i in range(count):
    name = input("Name: ")
    marks = input("Marks (space separated): ").split()
    marks = [int(m) for m in marks]
    students[name] = marks

results = {}
for name in students:
    avg = sum(students[name]) / len(students[name])
    if avg >= 90:
        grade = "A"
    elif avg >= 75:
        grade = "B"
    elif avg >= 60:
        grade = "C"
    else:
        grade = "D"
    results[name] = (avg, grade)

first = ("", 0, "")
second = ("", 0, "")

for name, (avg, grade) in results.items():
    if avg > first[1]:
        second = first
        first = (name, avg, grade)
    elif avg > second[1]:
        second = (name, avg, grade)

top = [first, second]

print("Top 2 Students:")
for name, avg, grade in top:
    print(name, round(avg, 2), grade)
