#13. Write a function that accepts a student dict and prints two lines: Student Name: Aniket and Age: 19.

def student_info(student):
    print("Student Name:", student["name"])
    print("Age:", student["age"])


student = {
    "name": "Aniket",
    "age": 19
}

student_info(student)