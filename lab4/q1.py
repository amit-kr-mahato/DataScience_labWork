# 1. Write a Python script that takes a list of student marks and sorts them in descending
# order (highest to lowest) using either the sorted() function or the .sort() method.

# .sort() method.

marks = [78, 92, 85, 64, 90, 88]
marks.sort(reverse=True)
print(marks)



# use the sorted() function

marks = [78, 92, 85, 64, 90, 88]
mark_sort=sorted(marks,reverse=True)
print("mark_sort",mark_sort)