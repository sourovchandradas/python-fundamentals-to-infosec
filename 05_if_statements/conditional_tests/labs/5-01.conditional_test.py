# Exercise 5-1: Conditional Tests

car = 'mercedes-benz'
print("Is car == 'mercedes-benz'? I predict True.")
print(car == 'mercedes-benz')

print("Is car == 'nissan'? I predict False.")
print(car == 'nissan')

# Test 3: String equality (True)
food = 'pizza'
print("\nIs food == 'pizza'? I predict True.")
print(food == 'pizza')

# Test 4: String equality (False)
print("Is food == 'burger'? I predict False.")
print(food == 'burger')

# Test 5: Case sensitivity (False)
city = 'Melbourne'
print("\nIs city == 'melbourne'? I predict False.")
print(city == 'melbourne')

# Test 6: Case sensitivity with .lower() (True)
print("Is city.lower() == 'melbourne'? I predict True.")
print(city.lower() == 'melbourne')

# Test 7: Numerical comparison (True)
age = 94
print("\nIs age >= 20? I predict True.")
print(age >= 20)

# Test 8: Numerical comparison (False)
print("Is age < 20? I predict False.")
print(age < 20)

# Test 9: List membership (True)
fruits = ['apple', 'banana', 'mango']
print("\nIs 'apple' in fruits? I predict True.")
print('apple' in fruits)

# Test 10: List membership (False)
print("Is 'grape' in fruits? I predict False.")
print('grape' in fruits)
