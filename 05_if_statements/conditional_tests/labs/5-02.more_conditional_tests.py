# Exercise 5-02: More Conditional Tests

# 1. Tests for equality and inequality with strings
language = 'Python'
print("String Equality Test (True):", language == 'Python')
print("String Inequality Test (True):", language != 'Java')
print("String Equality Test (False):", language == 'Java')

# 2. Tests using the lower() function
username = 'JohnDoe'
print("\nLower Method Test (True):", username.lower() == 'johndoe')
print("Lower Method Test (False):", username.lower() == 'JohnDoe')

# 3. Numerical tests involving equality, inequality, >, <, >=, <=
score = 85
print("\nNumerical == Test (True):", score == 85)
print("Numerical != Test (True):", score != 100)
print("Numerical > Test (True):", score > 80)
print("Numerical < Test (False):", score < 50)
print("Numerical >= Test (True):", score >= 85)
print("Numerical <= Test (False):", score <= 80)

# 4. Tests using 'and' and 'or' keywords
a = 10
b = 20
print("\nLogical AND Test (True):", (a > 5) and (b > 15))
print("Logical AND Test (False):", (a > 5) and (b < 15))
print("Logical OR Test (True):", (a > 15) or (b > 15))
print("Logical OR Test (False):", (a > 15) or (b < 15))

# 5. Test whether an item is in a list
toppings = ['mushrooms', 'extra cheese', 'jalapenos']
print("\nList 'in' Test (True):", 'mushrooms' in toppings)
print("List 'in' Test (False):", 'pepperoni' in toppings)

# 6. Test whether an item is not in a list
print("\nList 'not in' Test (True):", 'pepperoni' not in toppings)
print("List 'not in' Test (False):", 'mushrooms' not in toppings)
