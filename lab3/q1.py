#  1. Basic File Read & Write
# ● Create a text file and write multiple lines into it
# ● Read the contents of the file and display them on the screen
# ● Handle the case where the file does not exist using try-except


try:
    with open("amit.txt", "w") as file:
        file.write("Hello, I am Amit Kumar Mahato.\n")
        file.write("I belong to Kathmandu.\n")
        file.write("I graduated in IT from Pokhara University.\n")
    print("File written successfully.")
except IOError:
    print("File lekhan paydaina | file write garna paudaina")

try:
    with open("amit.txt", "r") as file:
        print("\nFile Content:\n")
        print(file.read())
except FileNotFoundError:
    print("File does not exist.")



