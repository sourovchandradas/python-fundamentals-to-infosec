# Exercise 6-05: Rivers

rivers = {
    'nile': 'egypt',
    'ganga': 'india',
    'amazon': 'brazil'
}

# 1. Loop to print a sentence about each river
for river,country in rivers.items():
    print(f"{river.title()} runs through the {country.title()}")

# 2. Loop to print the name of each river
print("\n--- Rivers ---")
for river in rivers.keys():
    print(river.title())

# 3. Loop to print the name of each counrty
print("\n--- Countries ---")
for country in rivers.values():
    print(country.title())
