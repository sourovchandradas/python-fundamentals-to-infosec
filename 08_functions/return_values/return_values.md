# Return Values in Python

## Overview

A function does not always have to display its output directly using `print()`. Instead, it can process data and then return a value or set of values back to the line that called it using a `return` statement. Return values allow you to move much of your program's grunt work into functions, simplifying your main program body and separating logic from presentation.

This guide covers:
- **Returning simple values** - passing formatted strings or values back to the caller
- **Making arguments optional** - using empty string default values to handle optional inputs
- **Returning dictionaries** - packaging data into structured key-value pairs
- **Using functions with loops** - integrating returning functions into interactive `while` loops
- **Common mistakes and errors** - preventing implicit `None` returns, unreachable code, and discarded return values

---

## Table of Contents

1. [Returning a Simple Value](#returning-a-simple-value)
2. [Making an Argument Optional](#making-an-argument-optional)
3. [Returning a Dictionary](#returning-a-dictionary)
4. [Using a Function with a while Loop](#using-a-function-with-a-while-loop)
5. [Common Mistakes and Errors](#common-mistakes-and-errors)
6. [Exercises](#exercises)
7. [Quick Reference](#quick-reference)
8. [Related Topics](#related-topics)
9. [Why This Matters](#why-this-matters)
10. [Additional Resources](#additional-resources)

---

## Returning a Simple Value

### What is a Return Value?

The `return` statement takes a value from inside a function and sends it back to the line that called the function. When calling a function that returns a value, you need to provide a variable where the return value can be stored.

### Syntax and Implementation

```python
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
```

### Output

```python
Jimi Hendrix
```

### Execution Flow

1. The function `get_formatted_name()` is called with `'jimi'` and `'hendrix'`.
2. The function combines the two names, adds a space between them, and stores the result in `full_name`.
3. The `.title()` method converts the string to title case, and `return` sends this string back to the calling line.
4. The returned value is stored in the variable `musician` and then printed.

---

## Making an Argument Optional

### Why Make Arguments Optional?

Sometimes it makes sense to make an argument optional so that people using the function can choose to provide extra information only if they want to. Default values allow parameters to be optional.

### Step 1: Initial Attempt (Requires 3 Arguments)

If you define a function expecting three parameters (e.g., middle name), calling it with only two arguments causes an error.

```python
def get_formatted_name(first_name, middle_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)
```

### Output

```python
John Lee Hooker

```

### Step 2: Making Middle Name Optional

To make `middle_name` optional, set its default value to an empty string `''` and move it to the end of the parameter list.

```python
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

# Call with first and last name only
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# Call with first, last, and middle name
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)
```

### Output

```python
Jimi Hendrix
John Lee Hooker

```

> **Note:** Python evaluates non-empty strings as `True`. If a `middle_name` argument is passed, `if middle_name:` evaluates to `True` and builds the three-part name. If omitted, `middle_name` remains `''` (`False`), executing the `else` block.

---

## Returning a Dictionary

### Packaging Data into Data Structures

A function can return any data structure, including lists and dictionaries. Returning a dictionary allows you to organize simple inputs into a meaningful, labeled structure.

### Step 1: Returning a Basic Dictionary

```python
def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)
```

### Output

```python
{'first': 'jimi', 'last': 'hendrix'}

```

### Step 2: Extending the Function with Optional Parameters

You can easily extend dictionary-returning functions to store optional details like age.

```python
def build_person(first_name, last_name, age=''):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)
```

### Output

```python
{'first': 'jimi', 'last': 'hendrix', 'age': 27}

```

---

## Using a Function with a while Loop

### Integrating Functions into Interactive Scripts

Functions can be combined with control structures like `while` loops to format user input dynamically.

### Step 1: Initial Attempt (Infinite Loop Risk)

Without a quit condition, a user prompt inside a `while True` loop will run forever.

```python
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

# Infinite loop - lacks a break/quit condition!
while True:
    print("\nPlease tell me your name:")
    f_name = input("First name: ")
    l_name = input("Last name: ")
    
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")
```

### Step 2: Adding an Explicit Exit Condition

Use `break` statements at each prompt so users can exit easily at any time.

```python
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    
    f_name = input("First name: ")
    if f_name == 'q':
        break
        
    l_name = input("Last name: ")
    if l_name == 'q':
        break
        
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")
```

### Interactive Output

```python
Please tell me your name: 
(enter 'q' at any time to quit) 
First name: eric 
Last name: matthes 

Hello, Eric Matthes! 

Please tell me your name: 
(enter 'q' at any time to quit) 
First name: q
```

---

## Common Mistakes and Errors

### Mistake 1: Not Assigning the Return Value

Calling a function that returns a value without storing or printing it discards the returned value.

```python
# Incorrect: Output is calculated but lost
get_formatted_name('jimi', 'hendrix')

# Correct: Save return value in a variable
musician = get_formatted_name('jimi', 'hendrix')
```

### Mistake 2: Missing `return` Keyword

If you omit the `return` statement, Python implicitly returns `None`.

```python
def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    # Missing return full_name.title()

result = get_formatted_name('jimi', 'hendrix')
print(result)
```

**Output:**

```python
None

```

### Mistake 3: Unreachable Code Post-Return

Python exits the function immediately when it encounters `return`. Any code placed after `return` within the same control path will never execute.

```python
def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()
    print("This line will never run!")  # Unreachable code
```

---

## Exercises

File naming convention: Use descriptive, lowercase names with underscores (for example, `city_names.py`).

### Exercise 8-6: City Names

Write a function called `city_country()` that takes in the name of a city and its country. The function should return a string formatted like this:

```python
"Santiago, Chile"
```

Call your function with at least three city-country pairs, and print the value that's returned.

### Exercise 8-7: Album

Write a function called `make_album()` that builds a dictionary describing a music album. The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information. Use the function to make three dictionaries representing different albums. Print each return value to show that the dictionaries are storing the album information correctly.

Add an optional parameter to `make_album()` that allows you to store the number of tracks on an album. If the calling line includes a value for the number of tracks, add that value to the album's dictionary. Make at least one new function call that includes the number of tracks on an album.

### Exercise 8-8: User Albums

Start with your program from Exercise 8-7. Write a `while` loop that allows users to enter an album's artist and title. Once you have that information, call `make_album()` with the user's input and print the dictionary that's created. Be sure to include a quit value in the `while` loop.

---

## Quick Reference

| Concept | Syntax / Pattern | Description |
| --- | --- | --- |
| Simple Return | `return full_name.title()` | Sends a value back to the caller |
| Optional Argument | `def name(first, last, middle=''):` | Empty string default value makes argument optional |
| Returning Dictionary | `return {'first': first, 'last': last}` | Packs simple strings into structured dictionary data |
| Implicit Return | Function without `return` | Returns `None` automatically |
| Early Return | `return` inside `if` block | Returns value early depending on conditional evaluation |

---

## Related Topics

* [Defining a Function](../defining_a_function/defining_a_function.md)
* [Passing Arguments](../passing_arguments/passing_arguments.md)
* [Working with Dictionaries](../../06_dictionaries/working_with_dictionaries/working_with_dictionaries.md)
* [Introducing While Loops](../../07_user_input_and_while_loops/introducing_while_loops/introducing_while_loops.md)

---

## Why This Matters

Return values disconnect internal computation from display logic. By returning processed data rather than printing it immediately inside the function, you make your functions reusable across diverse contexts—such as web APIs, GUI widgets, automated tests, or secondary data pipelines.

---

## Additional Resources

* [Python Official Documentation: The return Statement](https://docs.python.org/3/reference/simple_stmts.html)
* [Real Python: Defining Your Own Python Function (Return Values)](https://www.google.com/search?q=https://realpython.com/defining-your-own-python-function/%23the-return-statement)

---

*Last Updated : October 5, 2026*

---

## Key Takeaways

* Functions use the `return` statement to send processed data back to the line that called them.
* Storing the return value in a variable allows you to work with that data throughout your script.
* Giving a parameter an empty default value (`''`) allows arguments to be optional.
* Functions can return complex types like dictionaries to structure data logically.
* Omitting a `return` statement in Python yields `None`, and code written after a `return` statement is unreachable.
