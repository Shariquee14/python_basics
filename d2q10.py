# 10. Given student = {'name': 'Rahul', 'python': 75, 'javascript': 62, 'html': 88}, print the student's name and then print all three subject marks using a loop.

student = {'name': 'Rahul', 'python': 75, 'javascript': 62, 'html': 88}

print(f"Student's name: {student['name']}")

for subject, mark in student.items():
    if subject != 'name':
        print(f"{subject.capitalize()}: {mark}")