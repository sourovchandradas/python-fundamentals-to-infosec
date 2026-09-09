# Exercise 4-10: Slices

pizzas = ['pepperoni', 'margherita', 'hawaiin', 'veggie', 'bbq chicken']

# Print the first three pizzas in the list
print("The first three pizzas in the list are:")
for pizza in pizzas[:3]:
    print(pizza)

# Print three pizzas from the middle of the list
print("\nThree pizzas from the middle of the list are:")
for pizza in pizzas[1:4]:
    print(pizza)

# Print the last three pizzas in the list are
print("\nThe last three pizzas in the list are:")
for pizza in pizzas[-3:]:
    print(pizza)
