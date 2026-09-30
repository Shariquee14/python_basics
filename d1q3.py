# 3. Ask for a temperature in Celsius and print it in Fahrenheit with one decimal, using an f-string. (F = C * 9/5 + 32)

cel = int(input("celsius: "))

fah = cel * 9/5 +32
print(fah)
print(type(fah))

# f-string
print(f"Temperature in Fahrenheit: {fah:.1f}°F")

