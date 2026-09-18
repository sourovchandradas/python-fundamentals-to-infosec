# Exercise 6-07: People

# Create dictionaries representing individual people
person_01 = {
        'first_name': 'shreyas',
        'last_name': 'iyer',
        'age': 32,
        'city': 'mumbai',
}

person_02 = {
        'first_name': 'abhishek',
        'last_name': 'sharma',
        'age': 26,
        'city': 'amritshar',
}

person_03 = {
        'first_name': 'sanju',
        'last_name': 'samson',
        'age': 31,
        'city': 'thiruvananthapuram'
}

# Store all three dictionaries in a list named 'people'
people = [person_01, person_02, person_03]

for person in people:
    full_name = f"{person['first_name']} {person['last_name']}"
    age = person['age']
    city = person['city']
    print(f"Name\t: {full_name.title()}")
    print(f"Age\t: {age}")
    print(f"City\t: {city.title()}\n")
