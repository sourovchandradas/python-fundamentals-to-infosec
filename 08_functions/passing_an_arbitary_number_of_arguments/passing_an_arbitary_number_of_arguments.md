# Passing an Arbitrary Number of Arguments in Python

## Overview

Sometimes you do not know ahead of time how many arguments a function needs to accept. Python allows a function to collect an arbitrary number of arguments from a calling statement using parameter packing. By using single asterisks (`*args`) for positional arguments and double asterisks (`**kwargs`) for keyword arguments, functions can flexibly handle varying inputs without requiring preset parameter counts.

This guide covers:

* **Arbitrary positional arguments (`*args`)** - collecting varying arguments into a tuple
* **Mixing positional and arbitrary arguments** - positioning parameter rules correctly
* **Arbitrary keyword arguments (`**kwargs`)** - collecting dynamic key-value pairs into a dictionary
* **Common mistakes and errors** - ordering parameters and parameter mapping bugs
* **Try It Yourself exercises** - practical labs applying flex-argument functions

---

## Table of Contents

1. [Arbitrary Positional Arguments (*args)](#arbitrary-positional-arguments-args)
2. [Mixing Positional and Arbitrary Arguments](#mixing-positional-and-arbitrary-arguments)
3. [Arbitrary Keyword Arguments (kwargs)](#arbitrary-keyword-arguments-kwargs)
4. [Common Mistakes and Errors](#common-mistakes-and-errors)
5. [Exercises](#exercises)
6. [Quick Reference](#quick-reference)
7. [Related Topics](#related-topics)
8. [Why This Matters](#why-this-matters)
9. [Additional Resources](#additional-resources)

---

## Arbitrary Positional Arguments (*args)

### Collecting Values into a Tuple

When you place an asterisk (`*`) before a parameter name, Python creates an empty tuple with that parameter's name and packs any received positional arguments into this tuple.

### Basic Syntax and Tuple Inspection

```python
def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
```

### Output

```python
('pepperoni',)
('mushrooms', 'green peppers', 'extra cheese')
```

Even if the function call passes only a single argument, Python packs it into a one-element tuple: `('pepperoni',)`.

### Iterating Over Arbitrary Arguments

You can replace simple printing with a loop to process each collected item individually:

```python
def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
```

### Output

```python
Making a pizza with the following toppings:
- pepperoni

Making a pizza with the following toppings:
- mushrooms
- green peppers
- extra cheese
```

---

## Mixing Positional and Arbitrary Arguments

### Ordering Rules for Parameters

When combining regular positional parameters with an arbitrary positional parameter, place the parameter accepting an arbitrary number of arguments **last** in the function definition.

Python matches explicit positional and keyword arguments first, then packs all remaining positional arguments into the final arbitrary parameter.

### Implementation Example

```python
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

### Output

```python
Making a 16-inch pizza with the following toppings:
- pepperoni

Making a 12-inch pizza with the following toppings:
- mushrooms
- green peppers
- extra chees
```

### Parameter Association

1. `make_pizza(16, 'pepperoni')`: Python stores `16` in `size` and packs `('pepperoni',)` into `toppings`.
2. `make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')`: Python stores `12` in `size` and packs `('mushrooms', 'green peppers', 'extra cheese')` into `toppings`.

---

## Arbitrary Keyword Arguments (kwargs)

### Collecting Key-Value Pairs into a Dictionary

When you need to accept an arbitrary number of key-value arguments, use double asterisks (`**`) before a parameter name. Python creates an empty dictionary with that parameter name and packs all unassigned keyword arguments into it.

### Implementation Example (user_profile.py)

```python
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile(
    'albert', 
    'einstein',
    location='princeton',
    field='physics'
)
print(user_profile)
```

### Output

```python
{'first_name': 'albert', 'last_name': 'einstein', 'location': 'princeton', 'field': 'physics'}
```

### Execution Flow

1. The arguments `'albert'` and `'einstein'` match the explicit parameters `first` and `last`.
2. The double asterisk before `**user_info` creates an empty dictionary `{}`.
3. The keyword arguments `location='princeton'` and `field='physics'` are packed into `user_info` as `{'location': 'princeton', 'field': 'physics'}`.
4. The loop iterates through `user_info.items()` and assigns each key-value pair to the output `profile` dictionary.

---

## Common Mistakes and Errors

### Mistake 1: Placing `*args` Before Explicit Positional Parameters

Placing an arbitrary positional parameter before standard positional parameters causes Python to pack intended positional values into the tuple, leading to missing argument errors.

```python
# Incorrect: *toppings consumes all positional arguments, leaving size empty
def make_pizza(*toppings, size):
    print(size)

# Raises TypeError: make_pizza() missing 1 required keyword-only argument: 'size'
make_pizza('pepperoni', 16)
```

**Solution:** Always place `*args` after fixed positional parameters unless specifically using keyword-only parameters.

### Mistake 2: Passing Positional Arguments to `**kwargs`

Passing values without explicit key names to a parameter prefixed with `**` produces a syntax error.

```python
# Incorrect: 'blue' is passed as a positional value, not a key-value pair
car = make_car('subaru', 'outback', 'blue') 
# TypeError: make_car() takes 2 positional arguments but 3 were given
```

**Solution:** Pass optional key-value pairs as keyword arguments: `color='blue'`.

### Mistake 3: Confusing Tuple Output (`*args`) with Dictionary Output (`**kwargs`)

Remember that single-asterisk `*args` collects items into an immutable **tuple**, whereas double-asterisk `**kwargs` collects items into a **dictionary**.

---

## Exercises

File naming convention: Use descriptive, lowercase names with underscores (e.g., `8-12.sandwiches.py`).

### Exercise 8-12: Sandwiches

Write a function that accepts a list of items a person wants on a sandwich. The function should have one parameter that collects as many items as the function call provides, and it should print a summary of the sandwich that is being ordered. Call the function three times, using a different number of arguments each time.

**Solution:** [Exercise 8-12: Sandwiches](labs/8-12.sandwiches.py)

### Exercise 8-13: User Profile

Start with a copy of `user_profile.py`. Build a profile of yourself by calling `build_profile()`, using your first and last names and three other key-value pairs that describe you.

**Solution:** [Exercise 8-13: User Profile](labs/8-13.user_profile.py)

### Exercise 8-14: Cars

Write a function that stores information about a car in a dictionary. The function should always receive a manufacturer and a model name. It should then accept an arbitrary number of keyword arguments. Call the function with the required information and two other name-value pairs, such as a color or an optional feature. Call the function like this:

```python
car = make_car('subaru', 'outback', color='blue', tow_package=True)
```

Print the returned dictionary to make sure all information was stored correctly.

**Solution:** [Exercise 8-14: Cars](labs/8-14.cars.py)

---

## Quick Reference

| Syntax Pattern | Data Type Created | Parameter Placement | Example Call |
| --- | --- | --- | --- |
| `def func(*args):` | `tuple` | After fixed positional args | `func('a', 'b', 'c')` |
| `def func(a, *args):` | Fixed + `tuple` | `*args` comes last among positional | `func(1, 'a', 'b')` |
| `def func(a, **kwargs):` | Fixed + `dict` | `**kwargs` placed at the very end | `func(1, color='red')` |
| `def func(a, *args, **kwargs):` | Mixed types | Order: Positional $\rightarrow$ `*args` $\rightarrow$ `**kwargs` | `func(1, 'x', color='red')` |

---

## Related Topics

* [Defining a Function](../defining_a_function/defining_a_function.md)
* [Passing Arguments](../passing_arguments/passing_arguments.md)
* [Return Values](../return_values/return_values.md)
* [Dictionaries](../../06_dictionaries/working_with_dictionaries/working_with_dictionaries.md)

---

## Why This Matters

Arbitrary argument packing enables software interfaces to accept flexible user inputs, optional flags, and configurable settings without requiring constant refactoring of function signatures. Learning `*args` and `**kwargs` is crucial for writing extensible wrapper functions, working with standard library utilities, and building scalable Python packages.

---

## Additional Resources

* [GeeksforGeeks: Python *args and **kwargs](https://www.geeksforgeeks.org/python/args-kwargs-python/)
* [Real Python: Python args and kwargs Demystified](https://realpython.com/python-kwargs-and-args/)

---

*Last Updated : October 5, 2026*

---

## Key Takeaways

* A single asterisk `*param` packs an arbitrary number of positional arguments into a `tuple`.
* Arbitrary positional parameters must be placed after fixed positional parameters.
* A double asterisk `**param` packs arbitrary keyword arguments into a `dictionary`.
* You can combine positional arguments, `*args`, and `**kwargs` in a single function when defined in the correct order.
* Always choose the simplest argument structure that meets your application's requirements.
