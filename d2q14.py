# 14. Create a list containing marks of 5 students. Using a loop, find how many students passed and how many failed. Passing marks = 40.

marks = [35, 67, 42, 28, 90]

passed = 0
failed = 0

for mark in marks:
    if mark >= 40:
        passed = passed + 1
    else:
        failed = failed + 1

print("Passed:", passed)
print("Failed:", failed)