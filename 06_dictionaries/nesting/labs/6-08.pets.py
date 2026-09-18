# Exercise 6-08: Pets

# Create dictionaries for each pet
tommy = {
    'kind': 'dog',
    'owner': 'ankit',
}

lucky = {
    'kind' : 'cat',
    'owner': 'manish',
}

milo = {
    'kind': 'parrot',
    'owner': 'sameer',
}

# Store dictionaries in a list named 'pets'
pets = [tommy, lucky, milo]

# Loop through the list and print details about each pet
for pet in pets:
    animal_kind = pet['kind']
    owner_name = pet['owner']

    print(f"Animal Kind : {animal_kind.title()}")
    print(f"Owner name : {owner_name.title()}\n")
