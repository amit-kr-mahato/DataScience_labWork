# 5. Menu-Driven File Operations
# ● Write data to a file
# ● Read data from a file
# ● Append data to a file
# ● Handle invalid user input and file errors using exception handling

def write_file():
    
    try:
        data = input("Enter data to write: ")
        with open("data.txt", "w") as f:
            f.write(data + "\n")
        print("Data written successfully.")
    except IOError:
        print("not write to file.")

def read_file():
    
    try:
        with open("data.txt", "r") as f:
            content = f.read()
            print("\nFile Content:\n" + content)
    except FileNotFoundError:
        print("File not found.")
    except IOError:
        print("Could not read file.")

def append_file():
    
    try:
        data = input("Enter data to append: ")
        with open("data.txt", "a") as f:
            f.write(data + "\n")
        print("Data appended successfully.")
    except IOError:
        print(" not append to file.")

def menu():
    while True:
        print("\nMenu:")
        print("1. Write to file")
        print("2. Read from file")
        print("3. Append to file")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            write_file()
        elif choice == "2":
            read_file()
        elif choice == "3":
            append_file()
        elif choice == "4":
            print("program bata hatnu")
            break
        else:
            print(" Please enter 1-4 number.")


menu()
