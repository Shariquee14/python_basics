marks = [45, 67, 89, 34, 78]

for m in marks:
    print(m)

for i in range (5):
    print(i)

for i, m in enumerate(marks):
    print(i,m)

#for subject, mark in student["marks"].items():
#    print(f"{subject}: {mark}")

count = 0 
while count < 3:
    count = count + 1




#List comprehensions: a loop that builds a new list in one line

doubled = [m * 2 for m in marks]              # [90, 134, 178, 68, 156]
passed  = [m for m in marks if m >= 40]       # [45, 67, 89, 78]   only some
grades  = ["P" if m >= 40 else "F" for m in marks]   # ['P','P','P','F','P']
