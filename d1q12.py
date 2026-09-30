#12. Create student = {"name": "Aniket", "marks": {"english": 30, "maths": 40, "science": 20}}. Calculate and print the total marks using a loop over .values().

stu = {"name": "Aniket", "marks": {"english": 30, "maths": 40, "science": 20}}

total = 0

for mark in stu["marks"].values():
    total += mark

print("Total marks:", total)