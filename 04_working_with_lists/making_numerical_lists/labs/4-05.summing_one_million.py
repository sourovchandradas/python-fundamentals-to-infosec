# Exercise 4-05:  Summing One Million
# Generating a list of numbers from 1 to 1 million and printing them, find minimum number, find maximum number and calculate the total sum.

numbers = list(range(1, 1000001))

for number in numbers:
    print(number)

# Find minimum number in the list using min() function
print("Minimum number:", min(numbers))

# Find maximum number in the list using max() function 
print("Maximum number:", max(numbers))

# Calculate total sum in the list using sum() function
print("Total sum:", sum(numbers))
