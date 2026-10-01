# 13. Given numbers = [10, 20, 30, 40, 50], find the sum of all numbers using a loop. Do not use sum().

numbers = [10, 20, 30, 40, 50]
total = 0

for num in numbers:
    total += num

print("Sum of all numbers:", total)