# 7. Create x = 12 outside a function and x = 20 inside it. Print both and explain the scope in a comment.

x = 12

def show_x():
    x = 20
    print("Inside function:", x)

show_x()
print("Outside function:", x)

# The x inside the function is local to that function,
# while the x outside is a global variable.