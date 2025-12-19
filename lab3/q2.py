# File Processing with Exception Handling
# ● Reads numbers from a text file (one number per line)
# ● Ignores invalid entries using exception handling
# ● Calculates and displays the sum and average of valid numbers


total = 0
count = 0

try:
    with open("amit.txt", "r") as file:
        for line in file:
            try:
                num = float(line)
                total += num
                count += 1
            except ValueError:
             print("ignore the text:",line)

    if count > 0:
        average = total / count
        print("Sum:", total)
        print("Average:", average)
    else:
        print("No valid numbers found.")

except FileNotFoundError:
    print("Error: File not found.")
except IOError:
    print("Error: Unable to read file.")
    