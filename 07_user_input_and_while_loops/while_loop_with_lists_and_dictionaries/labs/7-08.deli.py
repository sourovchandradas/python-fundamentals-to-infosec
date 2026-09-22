# Exercise 7-8: Deli

# List of sandwich orders
sandwich_orders = ['tuna', 'turkey', 'club', 'chicken', 'veggie']

# Empty list for finished sandwiches
finished_sandwiches = []

# Process each sandwich order
while sandwich_orders:
    current_finished = sandwich_orders.pop(0)
    print(f"I made your {current_finished} sandwich.")
    finished_sandwiches.append(current_finished)

# Print all finished sandwiches
print("\nThe following sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich.title()} sandwich")
