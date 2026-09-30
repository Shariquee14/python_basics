#4. Ask for marks and print Distinction (80+), Pass (40-79) or Fail using if / elif / else.

marks = int(input("Marks: "))

if marks > 80:
    print("Excellent")
elif marks > 40:
    print("Pass")
else:
    print("Fail")
    