student  = [40,34,32,43,98]
passed = 0
failed = 0

for i in student:
    if i > 40:
        passed = passed + 1
    else:
        failed = failed + 1

print("Total number of passed students:", passed)
print("Total number of failed students:", failed)
