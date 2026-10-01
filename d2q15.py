# 15. Create a function that accepts a list of marks. 
# The function should loop through the marks, print each student's result as Pass or Fail, 
# and finally print the total number of passed and failed students.


def analyze_marks(marks_list):
    passed = 0
    failed = 0

    for mark in marks_list:
        if mark >= 40:
            print(f"Student with mark {mark}: Pass")
            passed += 1
        else:
            print(f"Student with mark {mark}: Fail")
            failed += 1

    print(f"Total passed students: {passed}")
    print(f"Total failed students: {failed}")