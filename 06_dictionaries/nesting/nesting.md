# Nesting in Python

## Overview

Nesting allows you to store more complex data structures by putting collections inside other collections. In real programs, data is often not flat. You may need to store:

- a list of dictionaries
- a list inside a dictionary
- a dictionary inside another dictionary

This is especially useful when you are working with user data, product information, game states, inventory systems, or other structured records.

This guide covers:
- **List of dictionaries**
- **List in a dictionary**
- **Dictionary in a dictionary**
- **Common mistakes and exercises**

---

## Table of Contents

1. [A List of Dictionaries](#a-list-of-dictionaries)
2. [A List in a Dictionary](#a-list-in-a-dictionary)
3. [A Dictionary in a Dictionary](#a-dictionary-in-a-dictionary)
4. [Common Mistakes](#common-mistakes)
5. [Exercises](#exercises)
6. [Quick Reference](#quick-reference)
7. [Related Topics](#related-topics)
8. [Additional Resources](#additional-resources)
9. [Last Modified](#last-modified)

---

## A List of Dictionaries

### What is it?

A list of dictionaries is a list where each item is a dictionary. This is useful when you want to store multiple records that share the same structure.

### Example

```python
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
```

### Output

```python
{'color': 'green', 'points': 5}
{'color': 'yellow', 'points': 10}
{'color': 'red', 'points': 15}
```

### Generating Items Dynamically

```python
aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

for alien in aliens[:5]:
    print(alien)
```

### Output

```python
{'color': 'yellow', 'points': 10, 'speed': 'medium'}
{'color': 'yellow', 'points': 10, 'speed': 'medium'}
{'color': 'yellow', 'points': 10, 'speed': 'medium'}
{'color': 'green', 'points': 5, 'speed': 'slow'}
{'color': 'green', 'points': 5, 'speed': 'slow'}
```

### Why this is useful

This pattern is great when you want to store many objects that have similar properties but different values.

Examples:
- multiple game characters
- student records
- product listings
- employee profiles

---

## A List in a Dictionary

### What is it?

A dictionary can store a list as a value. This is useful when one key should be linked to multiple values.

### Example

```python
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

print("You ordered a " + pizza['crust'] + "-crust pizza with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)
```

### Output

```python
You ordered a thick-crust pizza with the following toppings:
    mushrooms
    extra cheese
```

### Another Example

```python
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())
```

### Output

```python
Jen's favorite languages are:
    Python
    Ruby

Sarah's favorite languages are:
    C

Edward's favorite languages are:
    Ruby
    Go

Phil's favorite languages are:
    Python
    Haskell
```

### Why this is useful

This pattern lets you associate more than one value with a single key.

Examples:
- favorite languages per user
- multiple hobbies for one person
- multiple toppings for a pizza
- several tags for a blog post

---

## A Dictionary in a Dictionary

### What is it?

This is a dictionary whose values are themselves dictionaries. It is useful when storing structured information under unique identifiers.

### Example

```python
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())
```

### Output

```python
Username: aeinstein
    Full name: Albert Einstein
    Location: Princeton

Username: mcurie
    Full name: Marie Curie
    Location: Paris
```

### Why this is useful

This is one of the best ways to organize data with a unique top-level key.

Examples:
- user profiles
- product records
- student information
- company employee data

---

## Common Mistakes

### Mistake 1: Forgetting the key

```python
favorite_languages[0]
```

This will fail because the outer structure is a dictionary, not a list.

The correct version is:

```python
favorite_languages['jen']
```

### Mistake 2: Not using nested loops

```python
for name, languages in favorite_languages.items():
    print(languages)
```

This prints the whole list, not each item inside the list.

Correct version:

```python
for name, languages in favorite_languages.items():
    for language in languages:
        print(language)
```

### Mistake 3: Using wrong access patterns

```python
users['someone']['age']
```

This will raise a `KeyError` if `'age'` is not available.

Safer approach:

```python
if 'age' in users['someone']:
    print(users['someone']['age'])
```

---

## Exercises

File naming convention: Use descriptive lowercase snake_case names such as `people.py`.

### Exercise 6-7: People
Start with the program you wrote for Exercise 6-1. Make two new dictionaries representing different people, and store all three dictionaries in a list called `people`. Loop through the list and print everything you know about each person.

### Exercise 6-8: Pets
Create several dictionaries where each dictionary stores the name of a pet, the type of animal, and the owner's name. Store these dictionaries in a list called `pets`. Then loop through the list and print everything you know about each pet.

### Exercise 6-9: Favorite Places
Create a dictionary called `favorite_places`. Think of three names to use as keys in the dictionary, and store one to three favorite places for each person. Loop through the dictionary and print each person's name and favorite places.

### Exercise 6-10: Favorite Numbers
Modify your program from Exercise 6-2 so each person can have more than one favorite number. Then print each person's name along with their favorite numbers.

### Exercise 6-11: Cities
Create a dictionary called `cities`. Use the names of three cities as keys in the dictionary. Create a dictionary of information about each city, including the country, approximate population, and one fact about the city. Print the name of each city and all the information you have stored about it.

### Exercise 6-12: Extensions
Use one of the example programs from this chapter and extend it by adding more keys, changing the context, or improving the formatting of the output.

---

## Quick Reference

| Structure | Example | Common Use |
| --- | --- | --- |
| List of dictionaries | `[{'color': 'green'}, {'color': 'red'}]` | Multiple similar records |
| List in a dictionary | `{'pizza': ['cheese', 'pepperoni']}` | Multiple values for one key |
| Dictionary in a dictionary | `{'user1': {'name': 'Alice'}}` | Structured, hierarchical data |

---

## Related Topics

- Dictionaries
- Lists
- Loops
- Conditionals
- Functions
- JSON data handling

---

## Why This Matters

Nesting is important because real-world data is often not flat. Most applications store data in structured ways, such as:

- user profiles
- shopping carts
- product lists
- medical records
- employee databases

Without nesting, it would be much harder to organize and access complex data efficiently.

---

## Additional Resources

- [Python Official Documentation: Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- [Python Official Documentation: Lists](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations)
- [Real Python: Dictionaries](https://realpython.com/python-dicts/)
- [Python Crash Course by Eric Matthes](https://nostarch.com/pythoncrashcourse2e)

---

## Last Modified

**October 2, 2024**

---

## Key Takeaways

- Nesting means placing one collection inside another.
- A list of dictionaries stores multiple similar records.
- A list inside a dictionary stores multiple values under one key.
- A dictionary inside a dictionary stores structured, hierarchical data.
- Nesting is a core skill for real-world Python programming.
