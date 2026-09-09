# Exercise 4-11: My Pizzas Your Pizzas

my_pizzas = ['pepperoni', 'margherita', 'hawaiin', 'veggie', 'bbq chicken']

# Mak a copy of the list of pizzas by slicing the entire list
friend_pizzas = my_pizzas[:]

# Append new pizzas to each list
my_pizzas.append('meat lovers')
friend_pizzas.append('four cheese')

print('My favorite pizzas are:')
for pizza in my_pizzas:
    print(f'- {pizza}')

print('\nMy friend\'s favorite pizzas are:')
for pizza in friend_pizzas:
    print(f'- {pizza}')
