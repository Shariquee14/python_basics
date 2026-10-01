# 4. Take a student's marks and print: 80+ = Excellent, 60-79 = Good, 40-59 = Pass, below 40 = Fail.

marks = int(input("marks: "))

if marks >80 :
    print("Excellent")
elif marks> 60:
    print("Good")
elif marks>40:
    print("Try hard")
else: 
    print("Fail")