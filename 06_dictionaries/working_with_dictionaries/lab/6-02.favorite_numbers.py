# 6-02: Favorite Numbers

favorite_numbers = {
    'rahul': 1,
    'dhoni': 7,
    'milar': 10,
    'russel':12,
    'du plesis':13
}

# Iterate through each key-value pair and print the formatted message
for name, number in favorite_numbers.items():
    print(f"{name.title()}'s favorite number is {number}.")
