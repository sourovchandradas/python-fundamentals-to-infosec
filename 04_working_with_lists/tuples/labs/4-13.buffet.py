# Exercise 4-13: Buffet

# Define original menu tuple
menu =('fried chicken', 'steamed rice', 'pasta', 'salad', 'soup')

print("Original Menu:")
for food in menu:
    print(f"- {food.title()}")

# Attempting to modify an item raises TypeError (uncommenting demonstrates rejection)
# menu [0] = 'roast chicken

# Rewrite the tuple variable with a revised menu

menu = ('fried chicken', 'steamed rice', 'pasta', 'salad' 'roast chicken', 'ice cream')

print("\nRevised Menu:")
for food in menu:
    print(f"- {food.title()}")
