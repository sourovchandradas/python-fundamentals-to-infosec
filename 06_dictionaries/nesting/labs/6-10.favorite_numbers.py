# Exercise 6-10: Favorite Numbers

# Dictionaries with multiple numbers stored as lists
favorite_numbers = {
    'rahul': [1,18,45],
    'dhoni': [7],
    'miller': [10,17],
    'russell': [12,47,55],
    'du plessis': [13,32,63]
}

# Iterate through each person and their list of numbers
for name, numbers in favorite_numbers.items():
    if len(numbers) == 1:
        print(f"\n{name.title()}'s favorite number is:")
    else:
        print(f"\n{name.title()}'s favorite numbers are:")

    for number in numbers:
        print(f" - {number}")
