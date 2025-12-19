 # 3. CSV File Handling
# ● Read data from a CSV file containing student records (roll number, name, marks)
# ● Display all student records
# ● Handle file-related and data conversion errors using try-except


import csv

try:
    with open("student.csv", "r") as file:
        reader = csv.reader(file)
        print("Student Records:")
        for row in reader:
            try:
                roll_number, name, marks = row
                marks = int(marks)
                print(f"Roll: {roll_number}, Name: {name}, Marks: {marks}")
            except ValueError:
                pass
                #print("Invalid marks value.")
except FileNotFoundError:
    print("CSV file not found.")
except Exception as e:
    print("exception:", e)

