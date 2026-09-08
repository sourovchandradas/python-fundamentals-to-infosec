# Tuples in Python

## Overview

Lists work well for storing sets of items that can change throughout the life of a program. However, when you need a collection of items that should never change during execution, Python provides **tuples**. Python refers to values that cannot change as *immutable*, making a tuple an immutable list structure.

This guide covers:
- **Defining Tuples** - syntax using parentheses `()` and accessing items by index
- **Immutability & Errors** - preventing item modification and handling single-element tuples
- **Looping Through Tuples** - iterating over tuple elements using standard `for` loops
- **Writing Over a Tuple** - reassigning tuple variables safely when values need updating

---

## Table of Contents

1. [Defining a Tuple](#defining-a-tuple)
2. [Looping Through All Values in a Tuple](#looping-through-all-values-in-a-tuple)
3. [Writing Over a Tuple](#writing-over-a-tuple)
4. [Exercises](#exercises)
5. [Quick Reference](#quick-reference)

---

## Defining a Tuple

### Parentheses Syntax & Accessing Elements

A tuple looks just like a list except you use parentheses `()` instead of square brackets `[]`. Once defined, individual elements are accessed using zero-based indexing.

```python
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

```

**Output:**

```text
200
50

```

### Immutability & Item Assignment Error

Tuples are immutable, meaning Python prohibits modifying individual elements after creation. Attempting to assign a new value to an index raises a `TypeError`.

```python
dimensions = (200, 50)
dimensions[0] = 250

```

**Output:**

```text
Traceback (most recent call last):
  File "dimensions.py", line 2, in <module>
    dimensions[0] = 250
TypeError: 'tuple' object does not support item assignment

```

> **Note:** Raising an error on item assignment is intentional—it ensures that values defined as fixed dimensions or settings cannot be accidentally mutated elsewhere in your code.

### Defining Single-Element Tuples

To define a tuple containing only one element, you **must include a trailing comma**. Without the comma, Python treats the parentheses as a standard mathematical grouping operator rather than a tuple object.

```python
# Correct single-element tuple
my_tuple = (3,)

# Incorrect (evaluates to integer 3)
not_a_tuple = (3)

```

---

## Looping Through All Values in a Tuple

You can iterate through all items in a tuple using a standard `for` loop, exactly as you would with a list.

```python
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

```

**Output:**

```text
200
50

```

---

## Writing Over a Tuple

Although individual tuple elements cannot be altered, you can assign a completely new tuple to a variable that holds an existing tuple.

```python
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

# Reassigning the variable with a new tuple object
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

```

**Output:**

```text
Original dimensions:
200
50

Modified dimensions:
400
100

```

### When to Use Tuples vs. Lists

* Use **Lists** when storing collections of data that will grow, shrink, or undergo element-level modifications throughout the program (e.g., user profiles, shopping carts).
* Use **Tuples** when defining fixed collections of values that should remain constant throughout the application lifecycle (e.g., screen dimensions, database connection parameters, GPS coordinates).

---

## Exercises

File naming convention: Use descriptive, lowercase snake_case names (e.g., `buffet.py`)

### Exercise 4-13: Buffet

A buffet-style restaurant offers only five basic foods. Store them in a tuple and perform the following:

1. Print each food using a `for` loop.
2. Attempt to modify one item to verify that Python raises an assignment error.
3. Rewrite the tuple variable with a revised menu (replacing two items) and print the new menu items using a `for` loop.

**Example script:** `buffet.py`

---

## Quick Reference

| Concept | Syntax Example | Behavior |
| --- | --- | --- |
| Define Tuple | `dimensions = (200, 50)` | Creates an immutable sequence of elements |
| Single-Element Tuple | `my_tuple = (3,)` | Requires trailing comma to instantiate as a tuple |
| Access Element | `dimensions[0]` | Returns element at the specified zero-based index |
| Immutability Rule | `dimensions[0] = 100` | Raises `TypeError: 'tuple' object does not support item assignment` |
| Overwrite Variable | `dimensions = (400, 100)` | Reassigns variable pointer to an entirely new tuple object |

---

## Related Topics

* [Introducing Lists](https://www.google.com/search?q=../../03_introducing_list/lists/lists.md) - Working with mutable list collections
* [Looping Through Lists](https://www.google.com/search?q=../looping_through_an_entire_list/looping_through_an_entire_list.md) - Standard `for` loop iteration syntax
* [Slicing Lists](https://www.google.com/search?q=../working_with_part_of_a_list/slicing_a_list.md) - Sub-section extraction and independent list copying

---

## Additional Resources

* [Python Documentation: Tuples and Sequences](https://www.google.com/search?q=https://docs.python.org/3/tutorial/datastructures.html%23tuples-and-sequences)
* [Real Python: Understanding Tuples in Python](https://www.google.com/search?q=https://realpython.com/python-lists-tuples/%23python-tuples)

---

*Last Updated: 8th September, 2026*
