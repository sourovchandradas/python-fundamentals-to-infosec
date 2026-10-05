# Passing a List in Python

## Overview

Passing a list to a function gives the function direct access to the contents of that list. Functions can iterate over lists to display information, modify the original list in place, or work with copies of a list to keep original data intact. Modularizing list operations into dedicated functions makes code cleaner, reusable, and easier to maintain.

This guide covers:

* **Passing a list to a function** - iterating over and processing list items inside a function
* **Modifying a list in a function** - mutating original lists across function boundaries
* **Preventing a function from modifying a list** - using slice notation (`[:]`) to pass list copies
* **Single Responsibility Principle** - organizing complex workflows into specialized functions
* **Common mistakes and errors** - avoiding loop iteration bugs and memory overheads

---

## Table of Contents

1. [Passing a List to a Function](#passing-a-list-to-a-function)
2. [Modifying a List in a Function](#modifying-a-list-in-a-function)
3. [Preventing a Function from Modifying a List](#preventing-a-function-from-modifying-a-list)
4. [Common Mistakes and Errors](#common-mistakes-and-errors)
5. [Exercises](#exercises)
6. [Quick Reference](#quick-reference)
7. [Related Topics](#related-topics)
8. [Why This Matters](#why-this-matters)
9. [Additional Resources](#additional-resources)

---

## Passing a List to a Function

### Direct Access to List Elements

When you pass a list to a function, the function receives direct access to the contents of the list. The function stores the list in its parameter and can loop through it to perform operations on each item individually.

### Implementation Example

```python
def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
```

### Output

```python
Hello, Hannah!
Hello, Ty!
Hello, Margot!
```

### Execution Flow

1. The list `usernames` containing three string elements is defined.
2. The function call `greet_users(usernames)` passes the list to the parameter `names`.
3. The `for` loop inside `greet_users()` iterates through each item in `names`.
4. A personalized greeting is constructed using `.title()` and printed for each user.

---

## Modifying a List in a Function

### Permanent In-Place Modifications

When you pass a list to a function, any changes made to the list inside the function's body are permanent. Modifying lists directly inside functions allows you to work efficiently with large datasets without returning new objects.

### Step 1: Sequential Version (Without Functions)

Consider a 3D printing workflow where designs to be printed are stored in a list, and moved to a completed list after printing:

```python
# Start with some designs that need to be printed.
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simulate printing each design, until none are left.
# Move each design to completed_models after printing.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    
    # Simulate creating a 3D print from the design.
    print("Printing model: " + current_design)
    completed_models.append(current_design)

# Display all completed models.
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)
```

### Output

```python
Printing model: dodecahedron
Printing model: robot pendant
Printing model: iphone case

The following models have been printed:
dodecahedron
robot pendant
iphone case
```

### Step 2: Refactoring into Functions

We can reorganize this code by creating two functions, each performing one specific job:

1. `print_models()` handles simulating the printing process and moving designs between lists.
2. `show_completed_models()` displays the final summary of completed models.

```python
def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        
        # Simulate creating a 3D print from the design.
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
```

> **Design Principle:** Every function should have **one specific job**. If you notice a function doing too many different tasks, split the code into separate functions.

---

## Preventing a Function from Modifying a List

### Passing a Copy Using Slice Notation

Sometimes you want to prevent a function from modifying your original list. For example, you may want to keep the original `unprinted_designs` list for record-keeping.

To preserve the original list, pass a copy of the list to the function using slice notation `[:]`.

### Syntax

```python
function_name(list_name[:])
```

### Implementation Example

```python
def print_models(unprinted_designs, completed_models):
    """Simulate printing each design using a copy of unprinted_designs."""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Pass a copy of unprinted_designs using [:]
print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)

# Verify original list remains intact
print("\nOriginal unprinted_designs list:", unprinted_designs)
```

### Output

```python
Printing model: dodecahedron
Printing model: robot pendant
Printing model: iphone case

The following models have been printed:
dodecahedron
robot pendant
iphone case

Original unprinted_designs list: ['iphone case', 'robot pendant', 'dodecahedron']
```

> **Performance Note:** Pass original lists unless you have a specific reason to pass a copy. Working with existing lists avoids the time and memory overhead needed to clone large datasets.

---

## Common Mistakes and Errors

### Mistake 1: Modifying a List During `for` Loop Iteration

Removing elements from a list while iterating over it using a `for` loop skips elements due to index shifting.

```python
# Incorrect: Modifying list during a for loop skips elements
numbers = [1, 2, 3, 4]
for num in numbers:
    numbers.remove(num)
```

**Solution:** Use a `while` loop with `.pop()`, or iterate over a copy of the list: `for num in numbers[:]:`.

### Mistake 2: Forgetting `[:]` When Preserving Original Data

Passing `unprinted_designs` without slice notation modifies the caller's list directly, leaving `unprinted_designs` completely empty (`[]`).

```python
# Empties caller's list:
print_models(unprinted_designs, completed_models)

# Preserves caller's list:
print_models(unprinted_designs[:], completed_models)
```

### Mistake 3: Passing Non-Iterable Data Types

Passing a single string or integer to a function expecting a list causes unexpected character-by-character iteration or `TypeError`.

```python
def greet_users(names):
    for name in names:
        print("Hello, " + name.title() + "!")

# Passing a single string instead of a list iterates letter by letter!
greet_users('hannah')
```

---

## Exercises

File naming convention: Use descriptive, lowercase names with underscores (for example, `8-09.magicians.py`).

### Exercise 8-09: Magicians

Make a list of magician's names. Pass the list to a function called `show_magicians()`, which prints the name of each magician in the list.

**Solution:** [Exercise 8-09: Magicians](labs/8-09.magicians.py)

### Exercise 8-10: Great Magicians

Start with a copy of your program from Exercise 8-9. Write a function called `make_great()` that modifies the list of magicians by adding the phrase `"the Great"` to each magician's name. Call `show_magicians()` to see that the list has actually been modified.

**Solution:** [Exercise 8-10: Great Magicians](labs/8-10.great_magicians.py)

### Exercise 8-11: Unchanged Magicians

Start with your work from Exercise 8-10. Call the function `make_great()` with a copy of the list of magicians' names. Because the original list will be unchanged, return the new list and store it in a separate list. Call `show_magicians()` with each list to show that you have one list of the original names and one list with `"the Great"` added to each magician's name.

**Solution:** [Exercise 8-11: Unchanged Magicians](labs/8-11.unchanged_magicians.py)

---

## Quick Reference

| Operation | Code Snippet | Description |
| --- | --- | --- |
| Pass Original List | `greet_users(usernames)` | Function accesses and can mutate the caller's original list |
| Pass List Copy | `print_models(designs[:], done)` | Slice notation `[:]` passes an independent copy, protecting original data |
| In-Place Mutation | `unprinted_designs.pop()` | Permanently removes and returns the last element from the list |
| Modifying Elements | `magicians[i] = "Great " + magicians[i]` | Overwrites list items directly via index |

---

## Related Topics

* [Defining a Function](../defining_a_function/defining_a_function.md)
* [Return Values](../return_values/return_values.md)
* [Modifying, Adding, and Removing Elements](../../03_introducing_lists/modifying_adding_and_removing_elements/modifying_adding_and_removing_elements.md)
* [Slicing a List](../../04_working_with_lists/slicing_a_list/slicing_a_list.md)

---

## Why This Matters

Passing lists to functions allows programs to handle data processing in bulk without duplicating iteration logic. Knowing whether to mutate an existing list in place or protect it by passing a copy is fundamental for managing state, preventing unintended side effects, and writing maintainable Python applications.

---

## Additional Resources

* [Python Official Documentation: More on Lists](https://docs.python.org/3/tutorial/datastructures.html)
* [Real Python: Pass-by-Reference vs Pass-by-Value in Python](https://www.google.com/search?q=https://realpython.com/python-pass-by-value/)

---

*Last Updated : October 5, 2026*

---

## Key Takeaways

* Passing a list to a function grants direct access to inspect and iterate through its elements.
* Any modifications made to a list inside a function body permanently alter the caller's list.
* Use slice notation `list_name[:]` to pass a copy when you must preserve the original list contents.
* Keep code modular by designing functions to fulfill a single responsibility.
* Working with original lists is more memory- and time-efficient than passing copies for large datasets.
