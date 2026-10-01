# 7. Create a function check_even(number) that prints whether the given number is even or odd.

def check_even(number):

    if number % 2 == 0:
        print(f"{number} is even.")
        print("This is an even number.", number)
    else:
        print(f"{number} is odd.")

check_even(10)  # Example usage