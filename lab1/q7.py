# 7. Write a program that takes a list of numbers as input, and returns the largest number in the list.

nums = input("Enter numbers separated by space: ").split()

valid = True
for x in nums:
    if not x.isdigit():
        valid = False
        break

if valid:
    nums = list(map(int, nums))
    print("Largest =", max(nums))
else:
    print("Invalid input")
