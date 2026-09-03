# Lists in Python

## Overview

A list is a collection of items in a particular order. You can include letters, digits, or names in a list. The items do not have to be related in any particular way. Because a list usually contains more than one element, it is best practice to make the name of your list plural (e.g., `letters`, `digits`, `bicycles`).

---

## Table of Contents

1. [What is a List?](#what-is-a-list)
2. [Accessing Elements in a List](#accessing-elements-in-a-list)
3. [Index Positions Start at 0, Not 1](#index-positions-start-at-0-not-1)
4. [Using Individual Values from a List](#using-individual-values-from-a-list)
5. [Avoiding Index Errors](#avoiding-index-errors)
6. [Try It Yourself Exercises](#try-it-yourself-exercises)
7. [Quick Reference](#quick-reference)

---

## What is a List?

Square brackets (`[]`) indicate a list, and individual elements are separated by commas.

```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
# Output: ['trek', 'cannondale', 'redline', 'specialized']

```

> **Note:** Printing a list directly returns its raw representation, including square brackets and quotes.

---

## Accessing Elements in a List

Lists are ordered collections. You access any element by providing its position or index inside square brackets. String methods (like `.title()`, `.upper()`, `.lower()`) can be applied directly to list elements.

```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']

# Accessing first item
print(bicycles[0])
# Output: trek

# Applying string formatting
print(bicycles[0].title())
# Output: Trek

```

---

## Index Positions Start at 0, Not 1

Python considers the first item in a list to be at position `0`, not `1`.

* **Zero-Based Indexing:**
* First item: Index `0`
* Second item: Index `1`
* $N^{\text{th}}$ item: Index $N-1$


* **Negative Indexing:**
* Last item: Index `-1`
* Second item from end: Index `-2`
* Third item from end: Index `-3`



```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']

print(bicycles[1])   # cannondale
print(bicycles[3])   # specialized
print(bicycles[-1])  # specialized

```

---

## Using Individual Values from a List

Individual list items can be used just like any other variable (e.g., in string concatenation or f-strings).

```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']

# Building a message using list element
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)
# Output: My first bicycle was a Trek.

```

---

## Avoiding Index Errors

An `IndexError` occurs when you request an index that does not exist in the list. This is often caused by off-by-one errors.

```python
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles[3])
# Traceback (most recent call last):
#   File "motorcycles.py", line 2, in <module>
#     print(motorcycles[3])
# IndexError: list index out of range

```

### Key Edge Cases & Troubleshooting

* **Empty Lists:** Using index `-1` on an empty list (`[]`) causes an `IndexError`.
* **Debugging Tip:** Print the actual list or `len(list)` to verify its current size before accessing elements.

---

## Try It Yourself Exercises

File naming standard: Use descriptive, lowercase `snake_case` names.

* **3-1. Names (`names.py`):** Store friends' names in a list `names`. Print each person's name by accessing each element individually.
* **3-2. Greetings (`greetings.py`):** Send a personalized greeting message to each person using the `names` list.
* **3-3. Your Own List (`your_own_list.py`):** Create a list of preferred modes of transportation and print statements about them.
* **3-11. Intentional Error (`intentional_error.py`):** Modify an index in a program to intentionally trigger an `IndexError`, then correct it.

---

## Quick Reference

| Concept | Syntax Example | Description |
| --- | --- | --- |
| **List Declaration** | `items = ['a', 'b']` | Creates a list with elements |
| **First Element** | `items[0]` | Accesses the 1st item |
| **Last Element** | `items[-1]` | Accesses the last item safely |
| **String Method** | `items[0].title()` | Applies string method to item |
| **String Formatting** | `f"{items[0]}"` | Embeds element in f-string |

---

## Related Topics

* [Modifying Lists](../modifying_elements/modifying_elements.md) - Adding, inserting, and deleting list items
* [Organizing Lists](../organizing_lists/organizing_lists.md) - Sorting, reversing, and counting elements

---

## Additional Resources

* [Python Official Documentation: Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
* [Real Python: Lists in Python](https://realpython.com/python-lists-tuples/)

---

*Last Updated: 2026-09-03*

---

*Last Updated: 2026-09-03*
*Last Updated: 2026-09-03*
