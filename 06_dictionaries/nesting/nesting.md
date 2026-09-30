# NESTING in Pyhton

## OVERVIEW

1. A LIST OF DICTIONARIES
-----------------------------------------------------------------------------------------------------------------------------------------------------
* Definition: Storing multiple dictionaries inside a single list. This is useful when you have many similar items with multiple attributes.

Code Example:
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

Output:
{'color': 'green', 'points': 5}
{'color': 'yellow', 'points': 10}
{'color': 'red', 'points': 15}

* Generating Items Dynamically: You can use range() to create a fleet of dictionaries automatically and modify specific items later.

Code Example:
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

Output:
{'color': 'yellow', 'points': 10, 'speed': 'medium'}
{'color': 'yellow', 'points': 10, 'speed': 'medium'}
{'color': 'yellow', 'points': 10, 'speed': 'medium'}
{'color': 'green', 'points': 5, 'speed': 'slow'}
{'color': 'green', 'points': 5, 'speed': 'slow'}


2. A LIST IN A DICTIONARY
-----------------------------------------------------------------------------------------------------------------------------------------------------
* Definition: Storing a list as a value inside a dictionary. Useful when an item needs to be associated with multiple values or traits.

Code Example:
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }

print("You ordered a " + pizza['crust'] + "-crust pizza with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)

Output:
You ordered a thick-crust pizza with the following toppings:
	mushrooms
	extra cheese

* Multiple Values Per Key: Storing multiple responses or traits per person in a dictionary.

Code Example:
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

Output:
Jen's favorite languages are:
	Python
	Ruby

Sarah's favorite languages are:
	C


3. A DICTIONARY IN A DICTIONARY
-----------------------------------------------------------------------------------------------------------------------------------------------------
* Definition: Nesting a dictionary inside another dictionary. Useful for organizing structured data with unique identifiers as keys.

Code Example:
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

Output:
Username: aeinstein
	Full name: Albert Einstein
	Location: Princeton

Username: mcurie
	Full name: Marie Curie
	Location: Paris


4. TRY IT YOURSELF EXERCISES
-----------------------------------------------------------------------------------------------------------------------------------------------------
File naming standard: Use descriptive, lowercase snake_case names (e.g., people.py).

- 6-7. People:
  Start with the program you wrote for Exercise 6-1. Make two new dictionaries representing different people, and store all three dictionaries in 
  a list called people. Loop through your list of people. As you loop through the list, print everything you know about each person.

- 6-8. Pets:
  Make several dictionaries, where the name of each dictionary is the name of a pet. In each dictionary, include the kind of animal and the 
  owner's name. Store these dictionaries in a list called pets. Next, loop through your list and as you do print everything you know about each pet.

- 6-9. Favorite Places:
  Make a dictionary called favorite_places. Think of three names to use as keys in the dictionary, and store one to three favorite places 
  for each person. Loop through the dictionary, and print each person's name and their favorite places.

- 6-10. Favorite Numbers:
  Modify your program from Exercise 6-2 so each person can have more than one favorite number. Then print each person's name along with 
  their favorite numbers.

- 6-11. Cities:
  Make a dictionary called cities. Use the names of three cities as keys in your dictionary. Create a dictionary of information about each city 
  and include the country that the city is in, its approximate population, and one fact about that city. Print the name of each city and all 
  of the information you have stored about it.

- 6-12. Extensions:
  We're now working with examples that are complex enough that they can be extended in any number of ways. Use one of the example programs from 
  this chapter, and extend it by adding new keys and values, changing the context, or improving the formatting of the output.

```

---

### ২. `markdownfile.md` (Master Standard Markdown Format)

```markdown
# Nesting in Python

## Overview

Sometimes you will want to store a set of dictionaries inside a list, or a list of items inside a dictionary. This process is known as **nesting**. You can nest a list of dictionaries, a list of values inside a dictionary, or even a dictionary inside another dictionary. Nesting provides a powerful structure for modeling complex, real-world data.

This guide covers:
- **List of dictionaries** - managing collections of similar objects with individual attributes
- **List in a dictionary** - associating multiple items or values with a single key
- **Dictionary in a dictionary** - structuring hierarchical data under unique identifiers

---

## Table of Contents

1. [A List of Dictionaries](#a-list-of-dictionaries)
2. [A List in a Dictionary](#a-list-in-a-dictionary)
3. [A Dictionary in a Dictionary](#a-dictionary-in-a-dictionary)
4. [Exercises](#exercises)

---

## A List of Dictionaries

### Managing Collections of Dictionaries

When you have multiple objects that share similar properties, store each object as a dictionary and combine them into a list.

```python
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

```

**Output:**

```text
{'color': 'green', 'points': 5}
{'color': 'yellow', 'points': 10}
{'color': 'red', 'points': 15}

```

### Generating Dictionaries Dynamically

For large datasets, generate dictionaries automatically using `range()` and modify specific subsets during iteration.

```python
aliens = []

# Make 30 green aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Upgrade the first 3 aliens
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

# Display the first 5 aliens
for alien in aliens[:5]:
    print(alien)

```

**Output:**

```text
{'color': 'yellow', 'points': 10, 'speed': 'medium'}
{'color': 'yellow', 'points': 10, 'speed': 'medium'}
{'color': 'yellow', 'points': 10, 'speed': 'medium'}
{'color': 'green', 'points': 5, 'speed': 'slow'}
{'color': 'green', 'points': 5, 'speed': 'slow'}

```

---

## A List in a Dictionary

### Associating Multiple Values with a Key

Instead of assigning a single value to a key, assign a list when a key needs to store multiple pieces of information.

```python
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")
for topping in pizza['toppings']:
    print(f"\t{topping}")

```

**Output:**

```text
You ordered a thick-crust pizza with the following toppings:
	mushrooms
	extra cheese

```

### Iterating Over Lists Inside Dictionaries

When looping through a dictionary containing nested lists, use nested `for` loops to access individual items inside each list.

```python
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")

```

**Output:**

```text
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

---

## A Dictionary in a Dictionary

### Hierarchical Data Modeling

Nested dictionaries are useful when organizing structured records indexed by unique keys (such as usernames or IDs).

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
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")

```

**Output:**

```text
Username: aeinstein
	Full name: Albert Einstein
	Location: Princeton

Username: mcurie
	Full name: Marie Curie
	Location: Paris

```

---

## Exercises

File naming convention: Use descriptive, lowercase names with underscores (e.g., `people.py`)

### Exercise 6-7: People

Start with the program you wrote for Exercise 6-1. Make two new dictionaries representing different people, and store all three dictionaries in a list called `people`. Loop through your list of people. As you loop through the list, print everything you know about each person.

### Exercise 6-8: Pets

Make several dictionaries, where the name of each dictionary is the name of a pet. In each dictionary, include the kind of animal and the owner's name. Store these dictionaries in a list called `pets`. Next, loop through your list and as you do print everything you know about each pet.

### Exercise 6-9: Favorite Places

Make a dictionary called `favorite_places`. Think of three names to use as keys in the dictionary, and store one to three favorite places for each person. Loop through the dictionary, and print each person's name and their favorite places.

### Exercise 6-10: Favorite Numbers

Modify your program from Exercise 6-2 so each person can have more than one favorite number. Then print each person's name along with their favorite numbers.

### Exercise 6-11: Cities

Make a dictionary called `cities`. Use the names of three cities as keys in your dictionary. Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city. Print the name of each city and all of the information you have stored about it.

### Exercise 6-12: Extensions

We're now working with examples that are complex enough that they can be extended in any number of ways. Use one of the example programs from this chapter, and extend it by adding new keys and values, changing the context, or improving the formatting of the output.

---

## Quick Reference

| Nesting Type | Syntax Example | Common Use Case |
| --- | --- | --- |
| **List of Dictionaries** | `[{}, {}, {}]` | Storing a collection of similar objects with multiple fields |
| **List in Dictionary** | `{'key': [val1, val2]}` | Associating multiple values or traits with a single key |
| **Dictionary in Dictionary** | `{'key': {'inner_key': val}}` | Structuring nested data under unique main keys |

---

## Related Topics

* [Working with Dictionaries](https://www.google.com/search?q=../working_with_dictionaries/working_with_dictionaries.md) - Basic key-value pair creation and lookup syntax
* [Looping Through a Dictionary](https://www.google.com/search?q=../looping_through_a_dictionary/looping_through_a_dictionary.md) - Iterating through dictionary keys, values, and items
* [User Input and While Loops](https://www.google.com/search?q=../../07_user_input_and_while_loops/introducing_while_loops/introducing_while_loops.md) - Combining nested data structures with dynamic user input

---

## Additional Resources

* [Python Official Documentation: Nested Data Structures](https://www.google.com/search?q=https://docs.python.org/3/tutorial/datastructures.html%23dictionaries)
* [Real Python: Defining and Using Dictionaries in Python](https://www.google.com/search?q=https://realpython.com/python-dicts/)

---

*Last Updated: 2026-09-30*

```

```
