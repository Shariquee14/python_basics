# 8. Take a number from the user and print its multiplication table from 1 to 10 using a for loop.

num = int(input("Enter a Number :"))

for i in range(1 , 11):
    #print(num*i)
    print(f"{num} * {i} = {num*i}")   # how to write in f string
