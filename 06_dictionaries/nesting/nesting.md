# Nesting in Python

## Table of Contents
- [Overview](#overview)
- [Learning Objectives](#learning-objectives)
- [Content](#content)
- [Common Mistakes](#common-mistakes)
- [Practice Exercises](#practice-exercises)
- [Related Topics](#related-topics)
- [Additional Resources](#additional-resources)
- [Last Modified](#last-modified)

---

## Overview

Nesting allows you to store complex data structures by placing collections inside other collections. This is essential when modeling real-world data like user profiles, product catalogs, or inventory systems.

**Three main types of nesting:**
- **List of dictionaries** - managing multiple similar objects
- **List in a dictionary** - storing multiple values for a single key
- **Dictionary in a dictionary** - organizing hierarchical data

---

## Learning Objectives

By the end of this section, you should:
- understand what nesting means
- create a list of dictionaries
- store lists inside dictionary values
- nest dictionaries inside dictionaries
- loop through nested data structures correctly
- solve problems using nested data

---

## Content

### 1. A List of Dictionaries

#### Concept
Storing multiple dictionaries inside a single list is useful when managing many similar items with multiple attributes.

#### Example 1: Simple List of Dictionaries

```python
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
```

Output:
```
{'color': 'green', 'points': 5}
{'color': 'yellow', 'points': 10}
{'color': 'red', 'points': 15}
```

#### Example 2: Generating Dictionaries Dynamically

```python
aliens = []

# Create 30 green aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Change the first 3 aliens
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

# Display the first 5
for alien in aliens[:5]:
    print(alien)
```

Output:
```
{'color': 'yellow', 'points': 10, 'speed': 'medium'}
{'color': 'yellow', 'points': 10, 'speed': 'medium'}
{'color': 'yellow', 'points': 10, 'speed': 'medium'}
{'color': 'green', 'points': 5, 'speed': 'slow'}
{'color': 'green', 'points': 5, 'speed': 'slow'}
```

#### When to Use
- Storing multiple records with the same structure
- Managing game objects, user accounts, or product listings
- Batch processing similar items

---

### 2. A List in a Dictionary

#### Concept
Store a list as a value in a dictionary when one key needs to hold multiple related values.

#### Example 1: Pizza Order

```python
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

print("You ordered a " + pizza['crust'] + "-crust pizza with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)
```

Output:
```
You ordered a thick-crust pizza with the following toppings:
    mushrooms
    extra cheese
```

#### Example 2: Multiple Values Per Key

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

Output:
```
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

#### When to Use
- Storing multiple selections or preferences per person
- Keeping related items grouped together
- Managing one-to-many relationships

---

### 3. A Dictionary in a Dictionary

#### Concept
Nest dictionaries to organize hierarchical data with unique identifiers as top-level keys.

#### Example: User Profiles

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

Output:
```
Username: aeinstein
    Full name: Albert Einstein
    Location: Princeton

Username: mcurie
    Full name: Marie Curie
    Location: Paris
```

#### When to Use
- Storing user profiles with detailed information
- Organizing data by unique identifiers (ID, username, etc.)
- Managing hierarchical relationships in data

---

## Common Mistakes

### Mistake 1: Incorrect Indexing
```python
# Wrong - forgetting the key
favorite_languages[0]  # IndexError!

# Correct - use the person's name
favorite_languages['jen'][0]
```

### Mistake 2: Forgetting Nested Loops
```python
# Wrong - only prints the list
for name, languages in favorite_languages.items():
    print(languages)  # Prints the whole list at once

# Correct - iterate through each language
for name, languages in favorite_languages.items():
    for language in languages:
        print(language)
```

### Mistake 3: Assuming All Records Have the Same Keys
```python
# Can cause KeyError if not careful
users['someone']['age']  # Error if 'age' doesn't exist!

# Better - check first or use .get()
if 'age' in users['someone']:
    print(users['someone']['age'])
```

---

## Practice Exercises

### Exercise 6-7: People
Create dictionaries for three different people. Store them in a list called `people`. Loop through and print all information about each person.

### Exercise 6-8: Pets
Create dictionaries for several pets (include animal type and owner). Store in a list called `pets`. Print all pet information.

### Exercise 6-9: Favorite Places
Create a dictionary called `favorite_places`. Store 1-3 favorite places for each person. Loop and print the results.

### Exercise 6-10: Favorite Numbers
Modify a previous exercise so each person has multiple favorite numbers. Print names and their numbers.

### Exercise 6-11: Cities
Create a dictionary called `cities` with city information: country, population, and one fact. Print each city's details.

### Exercise 6-12: Extensions
Take one of the chapter examples and extend it by adding new keys, changing the context, or improving formatting.

---

## Quick Reference

| Structure | Example | Use Case |
|-----------|---------|----------|
| List of dicts | `[{'id': 1}, {'id': 2}]` | Multiple records |
| List in dict | `{'names': ['Alice', 'Bob']}` | Multiple values per key |
| Dict in dict | `{'user1': {'age': 30}}` | Hierarchical data |

---

## Related Topics

- Dictionaries - basic key-value operations
- Lists - storing collections of items
- Loops - iterating through data structures
- Conditional statements - filtering data
- Functions - reusing code with nested data
- JSON - working with nested real-world data formats

---

## Why This Matters

Nesting is one of the most important Python concepts because:
- Real-world data is rarely flat or simple
- Most applications work with complex, structured information
- Understanding nesting prepares you for JSON, databases, and APIs
- It's essential for building practical programs

---

## Additional Resources

- [Python Official Docs: Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- [Real Python: Working with JSON](https://realpython.com/python-json/)
- [Python Crash Course by Eric Matthes](https://nostarch.com/pythoncrashcourse2e)

---

## Last Modified

**October 2, 2024**
