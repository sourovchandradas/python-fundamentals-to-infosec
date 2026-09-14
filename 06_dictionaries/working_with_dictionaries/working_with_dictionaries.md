# Dictionaries in Python

## Overview

A **dictionary** in Python is a collection of key-value pairs. Each key is connected to a specific value, allowing you to quickly retrieve, modify, or store information. A key's value can be a number, string, list, or even another dictionary.

This guide covers:

* **Key-Value Pairs** - defining and understanding dictionary structures
* **Accessing Values** - retrieving data using specific keys
* **Adding & Modifying** - dynamically updating dictionary contents
* **Removing Items** - permanently deleting key-value pairs using `del`
* **Formatting** - writing clean, multi-line dictionaries

---

## Table of Contents

1. [What is a Dictionary?](#what-is-a-dictionary)
2. [Accessing Values in a Dictionary](#accessing-values-in-a-dictionary)
3. [Adding & Modifying Key-Value Pairs](#adding--modifying-key-value-pairs)
4. [Removing Key-Value Pairs](#removing-key-value-pairs)
5. [Dictionaries of Similar Objects](#dictionaries-of-similar-objects)
6. [Exercises](#exercises)

---

## What is a Dictionary?

### Definition

In Python, a dictionary is wrapped in curly braces `{}` containing a series of **key-value pairs**. Every key is connected to its value by a colon (`:`), and individual pairs are separated by commas.

```python
alien_0 = {'color': 'green', 'points': 5}

```

* **Key:** `'color'` $\rightarrow$ **Value:** `'green'`
* **Key:** `'points'` $\rightarrow$ **Value:** `5`

---

## Accessing Values in a Dictionary

### Basic Retrieval

To get the value associated with a key, specify the dictionary name followed by the key inside square brackets `[]`:

```python
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])   # Output: green

new_points = alien_0['points']
print(f"You just earned {new_points} points!")

```

**Output:**

```
green
You just earned 5 points!

```

---

## Adding & Modifying Key-Value Pairs

### Dynamic Addition

Dictionaries are dynamic structures. You can add new key-value pairs at any time by assigning a value to a new key:

```python
alien_0 = {'color': 'green', 'points': 5}

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

```

**Output:**

```python
{'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 25}

```

### Starting with an Empty Dictionary

Empty dictionaries are useful when collecting user input or generating data programmatically:

```python
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5

```

### Modifying Values

To change an existing value, reassign a new value to the corresponding key:

```python
alien_0 = {'color': 'green'}
alien_0['color'] = 'yellow'  # Updates color from green to yellow

```

### Practical Example: Tracking Position

```python
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}

# Determine movement based on current speed
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

# Update x_position
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New x-position: {alien_0['x_position']}")

```

**Output:**

```
New x-position: 2

```

---

## Removing Key-Value Pairs

### The `del` Statement

Use the `del` statement with the dictionary name and key to permanently remove a key-value pair:

```python
alien_0 = {'color': 'green', 'points': 5}

del alien_0['points']
print(alien_0)

```

**Output:**

```python
{'color': 'green'}

```

> **Note:** Deleted key-value pairs are removed permanently.

---

## Dictionaries of Similar Objects

### Multi-Line Formatting

When storing one kind of information across many objects (e.g., poll results), format the dictionary across multiple lines for readability:

```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

sarah_lang = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {sarah_lang}.")

```

**Output:**

```
Sarah's favorite language is C.

```

---

## Exercises

File naming convention: Use descriptive, lowercase names with underscores (e.g., `person_info.py`).

### Exercise 6-1: Person

Store information about a person (first name, last name, age, city) in a dictionary and print each piece of information.

```python
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 28,
    'city': 'New York'
}

print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])

```

### Exercise 6-2: Favorite Numbers

Store five people's names as keys and their favorite numbers as values. Print each person's name and their number.

### Exercise 6-3: Glossary

Create a programming glossary using a dictionary. Store 5 terms as keys and their definitions as values, then print them formatted neatly with newlines (`\n`).

---

## Quick Reference

| Action | Syntax Example | Result |
| --- | --- | --- |
| **Create Dictionary** | `data = {'a': 1, 'b': 2}` | Defines key-value pairs |
| **Access Value** | `data['a']` | Returns `1` |
| **Add / Modify** | `data['c'] = 3` | Adds or updates key `'c'` |
| **Delete Pair** | `del data['a']` | Removes key `'a'` and its value |
| **Empty Dictionary** | `empty_dict = {}` | Initializes empty structure |

---

## Related Topics

- [Lists](../03_lists/lists.md) - Learn about ordered, mutable sequences
- [If Statements](../05_if_statements/if_statements.md) - Learn how to execute conditional blocks of code
- [Looping through Dictionaries](../06_dictionaries/looping.md) - Learn how to iterate through keys, values, and items

---

## Additional Resources

- [Python Official Documentation: Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- [Real Python: Python Dictionaries](https://realpython.com/python-dicts/)

*Last Updated: 2026-09-14*
