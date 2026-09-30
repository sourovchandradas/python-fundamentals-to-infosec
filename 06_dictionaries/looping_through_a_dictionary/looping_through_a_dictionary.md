# Looping Through a Dictionary in Python

## Overview

A single Python dictionary can contain just a few key-value pairs or millions of pairs. Because dictionaries can store large amounts of data, Python allows you to loop through them efficiently. Dictionaries can be used to store information in a variety of ways; therefore, several different ways exist to loop through them.

This guide covers:
- **Looping through key-value pairs** - accessing both keys and values simultaneously using `.items()`
- **Looping through keys** - iterating over dictionary keys using `.keys()` or default loop behavior
- **Sorting keys** - organizing keys in alphabetical order during iteration using `sorted()`
- **Looping through values** - extracting all values using `.values()` and eliminating duplicates with `set()`

---

## Table of Contents

1. [Looping Through All Key-Value Pairs](#looping-through-all-key-value-pairs)
2. [Looping Through All Keys](#looping-through-all-keys)
3. [Looping Through Keys in Order](#looping-through-keys-in-order)
4. [Looping Through All Values](#looping-through-all-values)
5. [Exercises](#exercises)

---

## Looping Through All Key-Value Pairs

### The items() Method

When you need to work with both the key and its corresponding value, use the `.items()` method inside a `for` loop. This method returns a list-like view of key-value pairs, which are unpacked into two separate loop variables.

```python
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
```

**Output:**

```text
Key: username
Value: efermi

Key: first
Value: enrico

Key: last
Value: fermi
```

### Using Descriptive Variable Names

You can choose any names for the loop variables. Using descriptive names makes the code significantly easier to read when iterating over real-world data structures.

```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")
```

**Output:**

```text
Jen's favorite language is Python.
Sarah's favorite language is C.
Edward's favorite language is Ruby.
Phil's favorite language is Python.
```

---

## Looping Through All Keys

### The keys() Method

When you only need the keys from a dictionary, use the `.keys()` method.

```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name in favorite_languages.keys():
    print(name.title())
```

**Output:**

```text
Jen
Sarah
Edward
Phil
```

**Note:** Looping through keys is the default behavior in Python. Writing `for name in favorite_languages:` gives the exact same result as `for name in favorite_languages.keys():`.

### Accessing Values Within a Key Loop

You can access the value associated with the current key inside the loop by using standard dictionary lookup syntax `dictionary[key]`.

```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

friends = ['phil', 'sarah']

for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print(f"  Hi {name.title()}, I see your favorite language is {favorite_languages[name].title()}!")
```

**Output:**

```text
Jen
Sarah
  Hi Sarah, I see your favorite language is C!
Edward
Phil
  Hi Phil, I see your favorite language is Python!
```

### Checking Key Membership

The `.keys()` method is also useful for checking whether a specific key exists in a dictionary using the `in` or `not in` operators.

```python
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")
```

**Output:**

```text
Erin, please take our poll!
```

---

## Looping Through Keys in Order

### Sorting Keys with sorted()

Dictionaries preserve key connections, but you may want to present keys in a sorted order. Wrap the `sorted()` function around `dictionary.keys()` to iterate through keys alphabetically or numerically.

```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
```

**Output:**

```text
Edward, thank you for taking the poll.
Jen, thank you for taking the poll.
Phil, thank you for taking the poll.
Sarah, thank you for taking the poll.
```

---

## Looping Through All Values

### The values() Method

If you only care about the values stored in a dictionary, use the `.values()` method.

```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
```

**Output:**

```text
The following languages have been mentioned:
Python
C
Ruby
Python
```

### Removing Duplicates with set()

To extract unique values without repetitions, wrap `set()` around `dictionary.values()`. A set is an unordered collection of unique elements.

```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
```

**Output:**

```text
The following languages have been mentioned:
Python
C
Ruby
```

---

## Exercises

File naming convention: Use descriptive, lowercase names with underscores (e.g., `glossary_2.py`)

### Exercise 6-4: Glossary 2

Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 by replacing your series of `print()` statements with a loop that runs through the dictionary's keys and values. When you're sure that your loop works, add five more Python terms to your glossary. When you run your program again, these new words and meanings should automatically be included in the output.

### Exercise 6-5: Rivers

Make a dictionary containing three major rivers and the country each river runs through (e.g., `'nile': 'egypt'`).

* Use a loop to print a sentence about each river, such as *"The Nile runs through Egypt."*
* Use a loop to print the name of each river included in the dictionary.
* Use a loop to print the name of each country included in the dictionary.

### Exercise 6-6: Polling

Use the code in `favorite_languages.py`.

* Make a list of people who should take the favorite languages poll. Include some names that are already in the dictionary and some that are not.
* Loop through the list of people who should take the poll. If they have already taken the poll, print a message thanking them for responding. If they have not yet taken the poll, print a message inviting them to take the poll.

---

## Quick Reference

| Concept | Example Syntax | Description |
| --- | --- | --- |
| **Loop Pairs** | `for k, v in d.items():` | Iterates through key-value pairs simultaneously |
| **Loop Keys** | `for k in d.keys():` | Iterates through keys (default behavior) |
| **Sorted Loop** | `for k in sorted(d.keys()):` | Iterates through keys in alphabetical order |
| **Loop Values** | `for v in d.values():` | Iterates through values (includes duplicates) |
| **Unique Values** | `for v in set(d.values()):` | Iterates through unique values using a set |

---

## Related Topics

* [Working with dictionaries](../working_with_dictionaries/working_with_dictionaries.md) - Basic key-value pair creation and access
* [Nesting](../nesting/nesting.md)
* [Introducing while loops](../../07_user_input_and_while_loops/introducing_while_loops/introducing_while_loops.md)

---

## Additional Resources

* [Python Official Documentation: Dictionaries](https://www.google.com/search?q=https://docs.python.org/3/tutorial/datastructures.html%23dictionaries)
* [Real Python: Defining and Using Dictionaries](https://www.google.com/search?q=https://realpython.com/python-dicts/)

---

*Last Updated: 2026-09-29*
