#student = {'name': 'Aman', 'age': 19, 'marks': [75, 82, 91]} 
# Without using a loop, check the student's age and third mark. 
# If age is 18+ and the third mark is 90+, print Eligible for scholarship. 
# Otherwise print Not eligible.



student = {'name': 'Aman', 'age': 19, 'marks': [75, 82, 91]} 

if student['age'] > 18 and student['marks'][2] > 90:
    print(" Eligible for scholarship")
else: 
    print("Not eligible")