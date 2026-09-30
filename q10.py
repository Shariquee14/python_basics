# 10. Create marks = 82. Use if / elif / else: 90+ = A, 75-89 = B, 50-74 = C, below 50 = Fail.

marks = int(input("Enter the marks:"))

if marks > 89:
    print("A")
elif marks > 74:
    print("B")
elif marks > 49:
    print("C")
else:
    print("failed")