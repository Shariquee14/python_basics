# 9. Given marks = [45, 78, 32, 90, 67], print every mark one by one. Print Pass if the mark is 40 or above; otherwise print Fail.

marks = [45, 78, 32, 90, 67]

for marks in marks:
    print(marks)
    if marks>= 40:
        print("PASS")
    else:
        print("FAIL")

###
###
###
###



stu = {"Sharique": 45, "Ani": 78, "Rohit": 32, "Rahul": 90, "Aman": 67}

if stu["Sharique"] >= 40:
    print("PASS")
    print(f"Sharique scored {stu['Sharique']} marks.")
else:
    print("FAIL")
