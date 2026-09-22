# Exercise 7-09: No Pastrami 

# List of sandwich oders with 'pastrami' appearing at least three times
sandwich_orders = ['pastrami','tuna', 'pastrami','turkey', 'club', 'chicken','pastrami', 'veggie']

# Empty list for finished sandwiches
finished_sandwiches = []

# Notify customers that pastrami is out of stock
print("Deli Notice: Sorry, the deli has run out of pastrami today!\n")

# Remove all occurrences of 'pastrami' from sanwich_orders
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# Process the remaining sandwich orders
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich.")

# Print all finished sandwiches
print("\nThe following sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich.title()} sandwich")
