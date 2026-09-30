# 2. Ask the user for two numbers with input(). Print their sum. (Why does "10" + "20" give 1020? Write the answer as a comment.)

a = input("a:")
b = input("b:")

print(a + b)

# "10" + "20" gives "1020" because input() returns strings,
# and + joins (concatenates) strings instead of doing numerical addition.

print(int(a)+int(b))