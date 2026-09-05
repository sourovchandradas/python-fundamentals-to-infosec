# Organizing Lists in Python

## Overview

Lists are often created in an unpredictable order because you cannot always control how data is provided by users or systems. Python offers several built-in methods and functions to arrange, sort, reverse, and measure your list elements depending on whether you need permanent or temporary changes.

This guide covers:
- **Permanent Sorting (`sort()`)** - Alphabetical and reverse sorting that modifies the original list
- **Temporary Sorting (`sorted()`)** - Displaying sorted order without altering the underlying sequence
- **Reversing Lists (`reverse()`)** - Flipping element positions permanently
- **Measuring Length (`len()`)** - Counting the number of elements in a list

---

## Table of Contents

1. [Sorting Permanently with sort()](#sorting-permanently-with-sort)
2. [Sorting Temporarily with sorted()](#sorting-temporarily-with-sorted)
3. [Reversing a List with reverse()](#reversing-a-list-with-reverse)
4. [Finding List Length with len()](#finding-list-length-with-len)
5. [Exercises](#exercises)

---

## Sorting Permanently with sort()

### Basic Alphabetical Sorting

The `sort()` method modifies the list order permanently in alphabetical order. Once applied, you cannot revert to the original sequence.

```python
cities = ['sydney', 'delhi', 'paris', 'california']
cities.sort()
print(cities)

```

**Output:**

```
['california', 'delhi', 'paris', 'sydney']

```

### Reverse Alphabetical Sorting

You can sort in reverse alphabetical order by passing `reverse=True` as an argument to `sort()`:

```python
cities = ['sydney', 'delhi', 'paris', 'california']
cities.sort(reverse=True)
print(cities)

```

**Output:**

```
['sydney', 'paris', 'delhi', 'california']

```

### Capitalization Sensitivity

> **Note:** Sorting mixed-case strings is more complex because uppercase letters are prioritized differently in ASCII/Unicode order. For simple sorting, keep string elements in lowercase.

---

## Sorting Temporarily with sorted()

### Temporary Alphabetical Sorting

To present a list in alphabetical order without modifying the original data structure, use the `sorted()` function:

```python
cities = ['sydney', 'delhi', 'paris', 'california']

print("Here is the original list:")
print(cities)

print("\nHere is the sorted list:")
print(sorted(cities))

print("\nHere is the original list again:")
print(cities)

```

**Output:**

```
Here is the original list:
['sydney', 'delhi', 'paris', 'california']

Here is the sorted list:
['california', 'delhi', 'paris', 'sydney']

Here is the original list again:
['sydney', 'delhi', 'paris', 'california']

```

### Temporary Reverse Sorting

Pass `reverse=True` to `sorted()` to temporarily display reverse alphabetical order:

```python
print(sorted(cities, reverse=True))

```

**Output:**

```
['sydney', 'paris', 'delhi', 'california']

```

---

## Reversing a List with reverse()

### Reversing Order

The `reverse()` method flips the positions of elements in a list permanently. It does not sort alphabetically; it simply reverses the physical order:

```python
cities = ['sydney', 'delhi', 'paris', 'california']
cities.reverse()
print(cities)

```

**Output:**

```
['california', 'paris', 'delhi', 'sydney']

```

### Restoring Original Order

To revert back to the original order, call `reverse()` a second time on the same list:

```python
cities.reverse()
print(cities)

```

**Output:**
```
['sydney', 'delhi', 'paris', 'california']

```

---

## Finding List Length with len()

### Finding Item Count

Use the `len()` function to count the total number of items in a list:

```python
cities = ['sydney', 'delhi', 'paris', 'california']
print(len(cities))

```

**Output:**

```
4

```

> **Note:** Python counts items starting with one (1-based counting) when determining list length, avoiding off-by-one errors.

### Practical Applications

The `len()` function is essential when tracking items dynamically, such as counting active game targets, database records, or registered users on a website.

---

## Exercises

File naming convention: Use descriptive, lowercase names with underscores (e.g., `seeing_the_world.py`).

### Exercise 3-8: Seeing the World

1. Store at least five locations in a list in non-alphabetical order.
2. Print the list in original order.
3. Use `sorted()` to print the list alphabetically without modifying it.
4. Show original order is preserved by printing it again.
5. Use `sorted()` with `reverse=True` to print in reverse alphabetical order.
6. Show original order is preserved by printing it again.
7. Use `reverse()` to change list order permanently and print.
8. Use `reverse()` again to restore original order and print.
9. Use `sort()` to order list alphabetically permanently and print.
10. Use `sort(reverse=True)` to order list in reverse alphabetical order permanently and print.

### Exercise 3-9: Dinner Guests

Use `len()` to print a message stating the number of guests invited in Exercises 3-4 through 3-7.

### Exercise 3-10: Every Function

Create a list of items (e.g., rivers, countries, languages) and write a program using every function/method introduced in this chapter (`append()`, `insert()`, `del`, `pop()`, `remove()`, `sort()`, `sorted()`, `reverse()`, `len()`).

---

## Quick Reference

| Function / Method | Change Type | Description | Example |
| --- | --- | --- | --- |
| `list.sort()` | Permanent | Sorts items alphabetically in-place | `cities.sort()` |
| `list.sort(reverse=True)` | Permanent | Sorts items in reverse alphabetical order in-place | `cities.sort(reverse=True)` |
| `sorted(list)` | Temporary | Returns a new alphabetically sorted list | `sorted(cities)` |
| `sorted(list, reverse=True)` | Temporary | Returns a new reverse alphabetically sorted list | `sorted(cities, reverse=True)` |
| `list.reverse()` | Permanent | Flips the physical order of list elements in-place | `cities.reverse()` |
| `len(list)` | Read-only | Returns total count of items in the list | `len(cities)` |

---

## Related Topics

* [Introducing Lists](../introducing_lists/introducing_lists.md) - List creation, indexing, and access
* [Modifying Lists](../modifying_lists/modifying_lists.md) - Adding, inserting, and removing items
* [Working with Lists](../working_with_lists/working_with_lists.md) - Looping and numerical lists

---

## Additional Resources

* [Python Official Documentation: Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
* [Real Python: Python Lists and Tuples](https://realpython.com/python-lists-tuples/)

---

*Last Updated: 2026-09-05*
