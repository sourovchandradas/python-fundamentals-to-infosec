# Exercise 7-03: Multiples of Ten

# User input take
number = int(input("Enter a number to see if it is a multiple of 10: "))

if number % 10 == 0:
    print(f"{number} is a multiple of 10.")
else:
    print(f"The number {number} is not a multiple of 10.")
