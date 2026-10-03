def marks_count(marks): 
    passed = 0
    failed = 0
    for i in marks:
        if i > 40:
            passed = passed + 1
        else:
            failed = failed + 1

    print("Total number of passed students:", passed) 
   # print(f"Total Number of students passed: {passed} ")
    print("Total number of failed students:", failed)
   # print(f"Total Number of students failed: {failed} ")
    print("Total number of students:", len(marks))


marks_count([40,34,32,43,98])