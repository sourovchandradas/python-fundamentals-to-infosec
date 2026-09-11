# Using if Statements with Lists

## Overview

Combining **lists** and **`if` statements** unlocks dynamic decision-making in Python. It allows your code to respond flexibly to real-world scenarios, such as handling out-of-stock items, validating empty input, or cross-referencing collections.

- **Item Interception**: Watch for specific values during iteration and handle them uniquely.
- **Input Validation**: Safely check if a list contains data before attempting operations.
- **Cross-Collection Lookup**: Compare items across multiple lists or collections efficiently.

### Architectural Flow: List Validation & Processing

```text
                     +-----------------------------------+
                     |      Input List Evaluation        |
                     +-----------------------------------+
                                       |
                                       v
                            /---------------------\
                           /    Is List Non-Empty? \
                          <     (Implicit Boolean)  >
                           \                       /
                            \---------------------/
                               /               \
                        True  /                 \  False
                             /                   \
                            v                     v
                 +--------------------+   +--------------------+
                 | Iterate List via   |   | Execute Fallback   |
                 | 'for' Loop         |   | (else Block)       |
                 +--------------------+   +--------------------+
                            |
                            v
                 /---------------------\
                /   Does Item Match     \
               <   Filter Condition?    >
                \  (e.g., 'in' lookup)  /
                 \---------------------/
                    /               \
             True  /                 \  False
                  /                   \
                 v                     v
      +--------------------+   +--------------------+
      |  Special Handling  |   | Standard Processing|
      |   (if Branch)      |   |   (else Branch)    |
      +--------------------+   +--------------------+
```

---

## Table of Contents

1. [Checking for Special Items](#checking-for-special-items)
2. [Checking That a List Is Not Empty](#checking-that-a-list-is-not-empty)
3. [Using Multiple Lists](#using-multiple-lists)
4. [Exercises](#exercises)
5. [Quick Reference](#quick-reference)
6. [Related Topics](#related-topics)
7. [Additional Resources](#additional-resources)

---

## Checking for Special Items

When iterating through a list, you may need to apply special logic to certain elements while treating others normally.

### Example Script: `toppings.py`

```python
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")
```

**Output:**
```text
Adding mushrooms.
Sorry, we are out of green peppers right now.
Adding extra cheese.

Finished making your pizza!
```

### Execution Step-by-step

1. The `for` loop evaluates elements sequentially.
2. The `if` statement intercepts `'green peppers'` and triggers the apology notice.
3. The `else` block handles all remaining available items normally.

---

## Checking That a List Is Not Empty

In real-world applications, user inputs or API responses can return empty lists. Checking a list's content before looping prevents unexpected behavior.

### Implicit Truthiness in Python

Python treats empty and non-empty collections as boolean values:
- An **empty list** (`[]`) evaluates to `False`.
- A **non-empty list** evaluates to `True`.

> **PEP 8 Best Practice:** Do not use `if len(my_list) > 0:` to check for an empty list. Use implicit truthiness (`if my_list:`) as it is more readable and Pythonic.

### Example Script: Empty List Check

```python
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
```

**Output:**
```text
Are you sure you want a plain pizza?
```

---

## Using Multiple Lists

You can cross-reference elements across collections using the `in` operator. This is common when matching customer requests against internal system inventory.

### Example Script: Order Inventory Check

```python
available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")
```

**Output:**
```text
Adding mushrooms.
Sorry, we don't have french fries.
Adding extra cheese.

Finished making your pizza!
```

> **Performance Tip:** If `available_toppings` is fixed and won't change, store it as a **tuple** or **set** for faster lookup speeds when working with large datasets.

---

## Exercises

### Exercise 5-8: Hello Admin
Make a list of five or more usernames, including the name `'admin'`. Imagine you are writing code that will print a greeting to each user after they log in to a website. Loop through the list, and print a greeting to each user:
- If the username is `'admin'`, print a special greeting, such as *Hello admin, would you like to see a status report?*
- Otherwise, print a generic greeting, such as *Hello Eric, thank you for logging in again.*

### Exercise 5-9: No Users
Add an `if` test to `hello_admin.py` to make sure the list of users is not empty.
- If the list is empty, print the message *We need to find some users!*
- Remove all of the usernames from your list, and make sure the correct message is printed.

### Exercise 5-10: Checking Usernames
Do the following to create a program that simulates how websites ensure that everyone has a unique username.
- Make a list of five or more usernames called `current_users`.
- Make another list of five usernames called `new_users`. Make sure one or two of the new usernames are also in the `current_users` list.
- Loop through the `new_users` list to see if each new username has already been used. If it has, print a message that the person will need to enter a new username. If a username has not been used, print a message saying that the username is available.
- Make sure your comparison is case insensitive. If `'John'` has been used, `'JOHN'` should not be accepted. (Hint: Remember to make a lowercased copy of `current_users` for comparisons.)

### Exercise 5-11: Ordinal Numbers
Ordinal numbers indicate their position in a list, such as `1st` or `2nd`. Most ordinal numbers end in *th*, except 1, 2, and 3.
- Store the numbers 1 through 9 in a list.
- Loop through the list.
- Use an `if-elif-else` chain inside the loop to print the proper ordinal ending for each number. Your output should read `"1st 2nd 3rd 4th 5th 6th 7th 8th 9th"`, and each result should be on a separate line.

---

## Quick Reference

| Technique | Syntax Pattern | Primary Use Case |
| --- | --- | --- |
| **Special Value Filter** | `if item == 'value':` | Handling out-of-stock items or exceptions inside loops |
| **List Truthiness** | `if list_name:` | Safely validating empty inputs before running loops |
| **Cross-Collection Lookup** | `if item in reference_list:` | Checking customer requests against valid inventory |

---

## Related Topics

* [if Statements in Python](../if_statements/if_statements.md) - Fundamentals of conditional checks and branch decisions
* [Conditional Tests](../conditional_tests/conditional_tests.md) - Boolean values, logical operators, and comparison expressions
* [Dictionaries in Python](../../06_dictionaries/introduction/introduction.md) - Mapping key-value pairs for faster data lookups

---

## Additional Resources

* [Python Documentation: Truth Value Testing](https://docs.python.org/3/library/stdtypes.html#truth-value-testing)
* [Real Python: Python's `in` Operator](https://realpython.com/python-in-operator/)
 
---

*Last Updated: 11th September, 2026*
