# Exercise 7-10: Dream Vacation

# Dictionary to store user responses (Name: Destination)
responses = {}

# Set a flag to indicate that polling is active
polling_active = True

while polling_active:
    # Prompt the user for their name and dream vacation spot
    name = input("\nWhat is your name? ")
    response = input("If you could visit one place in the world, where would yo go? ")

    # Store the response in the dictionary
    responses[name] = response

    # Find out if anyone else is going to take the poll
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat.lower() == 'no':
        polling_active = False

# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, place in responses.items():
    print(f"{name.title()} would like to visit {place.title()}.")
