# Looping Through an Entire List in Python : Core Concepts & Best Practice

## Overview

You will often want to run through all entries in a list, performing the same task with each item. For example, in a game you might want to move every element on the screen by the same amount, or in a list of numbers you might want to perform statistical operations on every element. When you want to perform the same action with every item in a list, you can use Python’s `for` loop to manage these tasks internally without writing repetitive code.

This guide covers:
- **Basic `for` Loop Syntax** - how to iterate through elements
- **Naming Conventions** - writing clean, intent-revealing variable names
- **Multi-line Loops** - performing multiple operations inside a loop
- **Post-Loop Execution** - running unindented code after a loop completes
- **Indentation Errors** - identifying and fixing syntax and logical bugs

---

## Table of Contents

1. [Basic `for` Loop Syntax](#basic-for-loop-syntax)
2. [Naming Conventions](#naming-conventions)
3. [Doing More Work Within a Loop](#doing-more-work-within-a-loop)
4. [Doing Something After a Loop](#doing-something-after-a-loop)
5. [Avoiding Indentation Errors](#avoiding-indentation-errors)
6. [Exercises](#exercises)

---

## Basic `for` Loop Syntax

### What is a `for` Loop?

A `for` loop pulls each value from a list sequentially and stores it in a temporary variable so you can perform actions on it.

```python
developers = ['alice', 'bob', 'charlie', 'david']
for developer in developers:
    print(developer)

```

**Output:**

```text
alice
bob
charlie
david

```

**How It Works:**
Python reads `for developer in developers:`, pulls the first item `'alice'`, assigns it to `developer`, and executes `print(developer)`. It repeats this cycle for `'bob'`, `'charlie'`, and `'david'` until no elements remain in the list.

---

## Naming Conventions

Using explicit plural and singular variable pairs makes your code readable and self-documenting.

| Collection (Plural) | Single Item (Singular) | Loop Example |
| --- | --- | --- |
| `developers` | `developer` | `for developer in developers:` |
| `active_users` | `user` | `for user in active_users:` |
| `cats` | `cat` | `for cat in cats:` |
| `dogs` | `dog` | `for dog in dogs:` |

```python
# Clear, descriptive loop structure
developers = ['alice', 'bob', 'charlie','david']
for developer in developers:
    print(developer)

```

---

## Doing More Work Within a Loop

You can write as many lines of code as you like inside a `for` loop. Every indented line following the `for` statement is executed once for each item in the list.

```python
developers = ['alice', 'bob', 'charlie', 'david']
for developer in developers:
    print(f"Hello, {developer.title()}! Welcome to the team.")
    print(f"{developer.title()}, we are excited to have you on board!\n")

```

**Output:**

```text
Hello, Alice! Welcome to the team.
Alice, we are excited to have you on board!

Hello, Bob! Welcome to the team.
Bob, we are excited to have you on board!

Hello, Charlie! Welcome to the team.
Charlie, we are excited to have you on board!

Hello, David! Welcome to the team.
David, we are excited to have you on board!

```

---

## Doing Something After a Loop

Any block of code written after a `for` loop that is **not indented** will execute only once after all iterations complete.

```python
developers = ['alice', 'bob', 'charlie', 'david']
for developer in developers:
    print(f"Hello, {developer.title()}! Welcome to the team.")
    print(f"{developer.title()}, we are excited to have you on board!\n")

print("All developers have been welcomed!")

```

**Output:**

```text
Hello, Alice! Welcome to the team.
Alice, we are excited to have you on board!

Hello, Bob! Welcome to the team.
Bob, we are excited to have you on board!

Hello, Charlie! Welcome to the team.
Charlie, we are excited to have you on board!

Hello, David! Welcome to the team.
David, we are excited to have you on board!

All developers have been welcomed!

```

---

## Avoiding Indentation Errors

Python uses whitespace and indentation to determine code block structure. Mistakes in indentation lead to either syntax errors or logical bugs.

### 1. Forgetting to Indent

Always indent the line following a `for` statement.

```python
developers = ['alice', 'bob', 'charlie', 'david']
for developer in developers:
print(developer)

```

**Error Output:**

```text
  File "for_loop_developers.py", line 3
    print(developer)
    ^^^^^
IndentationError: expected an indented block after 'for' statement on line 2

```

### 2. Forgetting to Indent Additional Lines

If you fail to indent secondary lines inside a loop, Python runs them once after the loop finishes, causing a logical error.

```python
developers = ['alice', 'bob', 'charlie', 'david']
for developer in developers:
    print(f"Hello, {developer.title()}! Welcome to the team.")
print(f"{developer.title()}, we are excited to have you on board!\n")

```

**Logical Error Output:**

```text
Hello, Alice! Welcome to the team.
Hello, Bob! Welcome to the team.
Hello, Charlie! Welcome to the team.
Hello, David! Welcome to the team.
David, we are excited to have you on board!

```

### 3. Indenting Unnecessarily

Indenting code outside of a block raises an unexpected indent error.

```python
message = "I love scripting in Python!"
    print(message)

```

**Error Output:**

```text
  File "for_loop.py", line 2
    print(message)
IndentationError: unexpected indent

```

### 4. Indenting Unnecessarily After Loop

Indenting summary statements causes them to repeat unnecessarily on every pass of the loop.

```python
developers = ['alice', 'bob', 'charlie', 'david']
for developer in developers:
    print(f"Hello, {developer.title()}! Welcome to the team.")
    print(f"{developer.title()}, we are excited to have you on board!\n")
    print("All developers have been welcome to the team!")

```

### 5. Forgetting the Colon

Omitting the colon (`:`) at the end of a `for` statement triggers a `SyntaxError`.

```python
developers = ['alice', 'bob', 'charlie', 'david']
for developer in developers
    print(developer)

```

**Error Output:**

```text
  File "for_loop_developers.py", line 2
    for developer in developers
                               ^
SyntaxError: expected ':'

```

---

## Exercises

File naming convention: Use descriptive, lowercase snake_case names (e.g., `favorite_pizzas.py`)

### Exercise 4-1: Pizzas

Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and then use a `for` loop to print the name of each pizza.

1. Modify your `for` loop to print a sentence using the name of the pizza.
2. Add a line at the end of your program, outside the `for` loop, stating how much you like pizza.

**Example script:** `favorite_pizzas.py`

### Exercise 4-2: Animals

Think of at least three different animals that have a common characteristic. Store the names in a list, and use a `for` loop to print each animal name.

1. Modify your program to print a statement about each animal.
2. Add a line at the end of your program stating what these animals have in common.

**Example script:** `animals.py`

---

## Quick Reference

| Concept | Syntax Example | Behavior |
| --- | --- | --- |
| `for` Loop | `for item in items:` | Iterates over each element in `items` |
| Variable Naming | `for user in users:` | Singular variable stores current item |
| Indented Block | `    print(item)` | Code executed on every pass of loop |
| Post-Loop Code | `print("Done")` | Unindented code runs once after loop completes |
| Colon Requirement | `for x in list_name:` | Trailing colon indicates loop block start |

---

## Related Topics

* [Lists Overview](../lists/lists.md) - Fundamentals of list data structures
* [Modifying Elements](../modifying_elements/modifying_elements.md) - Adding, modifying, and removing list items
* [Numerical Lists](./numerical_lists.md) - Using `range()` and working with numbers in loops

---

## Additional Resources

* [Python Documentation: for Statements](https://www.google.com/search?q=https://docs.python.org/3/tutorial/controlflow.html%23for-statements)
* [Real Python: Python "for" Loops](https://www.google.com/search?q=https://realpython.com/python-for-loop/)

---

*Last Updated: 7th September, 2026*
