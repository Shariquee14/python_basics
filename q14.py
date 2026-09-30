# 14. Create student = {'name': 'Raj', 'python': 80, 'math': 35}. If Python marks are at least 40 and Math marks are at least 40, print Passed all subjects; otherwise print Failed.

stu = {'name': 'Raj', 'python': 80, 'math': 45}

if stu['python'] >= 40 and stu['math']>=40:
    print("Passed in all")
else: print("failed")