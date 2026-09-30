#14. Using a list comprehension, make a list of only the marks above 50 from [45, 67, 89, 34, 78]. Then make a list of grades "P" / "F" for each mark.

marks = [45, 67, 89, 34, 78]

# List of marks above 50
above_50 = [mark for mark in marks if mark > 50]
print(above_50)

# List of grades P / F for each mark
grades = ["P" if mark >= 40 else "F" for mark in marks]
print(grades)