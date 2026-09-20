# Exercise 7-02: Restaurant Seating

# User input
people_number = input("How many people are in your dinner group? ")

# String input convert into integer value.
people_number = int(people_number) 

if people_number > 8:
    print("Your group wait for a table.")
else:
    print("Your group table is ready.")
