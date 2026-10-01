# 11.  Create a function print_table(no) that prints the multiplication table of any number from 1 to 10.


def print_table(no):

    for i in range(1,11):
        print(no*i)
        print(f"{no} * {i} = {no*i}")

print_table(10)  # example usage