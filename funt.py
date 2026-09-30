def find_sum(a,b):
    return a,b

total = find_sum(3,4)
print(total)

def average(numbers):
    return sum(numbers)/ len(numbers)

def result(student):
    avg = average(student["marks"])
    if avg >= 40:
        return "Pass"
    return "Fail"

def greet(name, greeting="Hello"): 
    return f"{greeting}, {name}!"

print(greet("Ami"))        
print(greet("Ami", "Namaste"))



x= 10 

def show():
    y = 5
    print(x)

show()
class y:
   ...
print(y)

