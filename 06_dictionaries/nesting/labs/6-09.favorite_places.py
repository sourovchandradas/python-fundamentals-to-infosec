# Exercise 6-09: Favorite Places

# Create a dictionary with names as keys and a list of favorite places as values
favorite_places = {
    'deepti': ['ahemedabad', 'kanpur', 'jaipur'],
    'mitali': ['hyderabad', 'kolkata', 'dehradun'],
    'smrity': ['bengalore', 'guwahati', 'lucknow']
}

# Loop through the dictionary
for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")
    for place in places:
        print(f"- {place.title()}")
