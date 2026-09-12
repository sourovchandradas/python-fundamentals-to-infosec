# Exercise 5-11: Ordinal Numbers

# Store numbers 1 through 9 in a list
numbers = list(range(1, 10))

# Loop through the list to attach appropriate ordinal endings
for number in numbers:
    if(number == 1):
        print("1st")
    elif(number == 2):
        print("2nd")
    elif(number == 3):
        print("3rd")
    else:
        print(f"{number}th")
