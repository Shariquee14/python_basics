# Idex order always start from 0.

marks = [45 , 65 , 89 , 34 , 78]

print(marks[0])     # 45

print(marks[-1])    # 78 (when we use -1 negative index count from the end )

print(marks[1:3])   # [67 , 89] ( slice : from 1 upto (not including) 3.)

print(len(marks))   # 5  (len (basically count how many number are there and if there is string then how many alphabets are there))

marks[1] = 90       # update the value of  inder given in the [] .
print(marks)

marks.append(55)    # adds to the end
print(marks)

marks.remove(34)    # remove a value
print(marks)


print(sum(marks), max(marks) , min(marks))    # built -ins that just work (when sum is used its take out the sum of all value given in the list , when max is used its find the max value and give it , when mon is used its find the minimum value given in the list and give)


print(sorted(marks)) # new stored copy (in these its arrage there order )