# Exercise 7-03: Multiples of Ten

# User input take
number = int(input("Enter your number: "))

if number % 10 == 0:
    print(f"{number} is a multiple of 10.")
else:
    print(f"{number} is not a multiple of 10.")
