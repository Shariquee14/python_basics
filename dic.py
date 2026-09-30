student = {"name" : "Sharique" , "roll" : 14 , "class" : "12" , "marks" : {"eng":80, 
            "math":90, "science":70 }}

print(student["name"])
print(student["class"])
print(student["roll"])
print(student["marks"]["eng"])
print(student["marks"]["math"])
print(student["marks"]["science"])

student["city"] = "Jamshedpur"                  # added new value or data
print(student["city"])

student["roll"] = 2002                          # update , we just updated the previous value or data
print(student["roll"])

del student["class"]                            # removes , its removes from the data or list or dic whatever its given 

print(student.keys())                           # dict_keys (['name', 'roll', 'marks', 'city'])

print(student.values())                         # dict_values(['Sharique', 2002, {'eng': 80, 'math': 90, 'science': 70}, 'Jamshedpur'])

print(student.get("age", 0))                    # 0 .get() gives a default instead of an error

point = (10 , 20)                               # tuple: like a list but cannot change. Used for fixed pairs

unique = {1, 2, 2, 3, 3}                        # set: no duplicates, no order
print(unique)                                   # {1, 2, 3}

print(len(set("marks")))                          # quick way to count unique values

