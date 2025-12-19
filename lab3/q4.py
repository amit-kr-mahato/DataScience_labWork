# 4. Writing and Reading JSON Data
# ● Stores student details (ID, name, and marks) in a JSON file
# ● Reads the JSON file and displays the student information
# ● Handles exceptions related to file access and JSON decoding

import json

students = [
    {"id": 1, "name": "Amit", "marks": 80},
    {"id": 2, "name": "Rita", "marks": 90},
    {"id": 3, "name": "Suman", "marks": 75}
]

try:
    with open("amit.json", "w") as f:
        json.dump(students, f, indent=4)
    print("Data written successfully.")
except IOError:
    print("Cannot write to file.")


try:
    with open("amit.json", "r") as f:
        data = json.load(f)
        print("\nStudent Records:")
        for s in data:
            print(f"ID: {s['id']}, Name: {s['name']}, Marks: {s['marks']}")
except FileNotFoundError:
    print("File not found.")
except json.JSONDecodeError:
    print("Error decoding JSON.")
except IOError:
    print("Cannot read file.")
