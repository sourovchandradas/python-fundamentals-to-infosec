# Defining a Function in Python

## Overview

Functions are named blocks of code designed to perform a specific task. When you want to run that task, you call the function by name. Writing functions helps you organize code, avoid repetition, and make programs easier to read and maintain.

This guide covers:
- **Function syntax** - creating functions with the `def` keyword
- **Docstrings** - documenting a function's purpose
- **Function calls** - executing a function
- **Passing information** - using parameters and arguments
- **Best practices** - writing clear and reusable functions

---

## Table of Contents

1. [Defining a Function](#defining-a-function)
2. [Passing Information to a Function](#passing-information-to-a-function)
3. [Arguments and Parameters](#arguments-and-parameters)
4. [Common Mistakes](#common-mistakes)
5. [Exercises](#exercises)
6. [Quick Reference](#quick-reference)
7. [Related Topics](#related-topics)
8. [Additional Resources](#additional-resources)

---

## Defining a Function

### What is a Function?

A function is a reusable block of code that performs one job. Instead of writing the same logic multiple times, you define it once and call it whenever needed.

### Syntax Rules

- The `def` keyword tells Python that a function is being defined.
- The function name goes immediately after `def`.
- Parentheses `()` may contain parameters.
- A colon `:` ends the header line.
- The function body is indented underneath.

### Docstrings

A docstring is a short description written inside triple quotes at the beginning of the function body. It explains what the function does.

### Implementation Example

```python
def greet_user():
    """Display a simple greeting."""
    print("Hello!")

# Call the function
greet_user()
```

### Output

```python
Hello!
```

### Execution Flow

Defining a function does not run the code immediately. The function only stores the instructions. To execute it, you must call it using its name followed by parentheses.

---

## Passing Information to a Function

### Customizing Function Output

Functions are much more useful when they accept input. You can pass different values each time the function is called to produce different results.

### Adding a Parameter

A parameter is a variable declared inside the parentheses of a function definition.

### Implementation Example

```python
def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")

greet_user('jesse')
greet_user('sarah')
```

### Output

```python
Hello, Jesse!
Hello, Sarah!
```

### Why This Is Useful

Functions become reusable and flexible when they accept inputs instead of being hardcoded.

---

## Arguments and Parameters

### Technical Distinction

- **Parameter:** A variable listed in the function definition header.
- **Argument:** The actual value passed when the function is called.

```python
# 'username' is the parameter
def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")

# 'jesse' is the argument
greet_user('jesse')
```

### Usage Note

In casual conversation, programmers often use the terms “parameter” and “argument” interchangeably. However, keeping the distinction helps clarify the difference between the function definition and the function call.

---

## Common Mistakes

### Mistake 1: Calling the Function Without Parentheses

```python
greet_user
```

This references the function object, but it does not execute it. You must call it like this:

```python
greet_user()
```

### Mistake 2: Forgetting the Colon

```python
def greet_user()
    print("Hello!")
```

This will cause a syntax error because a function definition must end with a colon.

### Mistake 3: Using the Wrong Variable Name

```python
def greet_user(username):
    print(f"Hello, {user_name.title()}!")
```

This will fail because `user_name` is not the parameter name used by the function.

---

## Exercises

File naming convention: Use descriptive, lowercase names with underscores (for example, `message.py`).

### Exercise 8-1: Message

Write a function called `display_message()` that prints one sentence describing what you are learning in this chapter. Call the function so the message appears correctly.

### Exercise 8-2: Favorite Book

Write a function called `favorite_book(title)` that prints a message such as:

```python
One of my favorite books is Alice in Wonderland.
```

Call the function with a value for `title`.

---

## Quick Reference

| Concept | Syntax / Pattern | Description |
| --- | --- | --- |
| Function header | `def function_name():` | Starts a new function |
| Docstring | `"""Describe the function."""` | Explains what the function does |
| Function call | `function_name()` | Runs the function |
| Parameter | `def greet(username):` | Variable used inside the function |
| Argument | `greet('jesse')` | Actual value passed to the function |

---

## Related Topics

- [Introducing While Loops](../../07_user_input_and_while_loops/introducing_while_loops/introducing_while_loops.md)
- [Working with Dictionaries](../../06_dictionaries/working_with_dictionaries/working_with_dictionaries.md)
- [Passing Arguments](../passing_arguments/passing_arguments.md)

---

## Why This Matters

Functions are one of the most important ideas in Python. They allow you to break large programs into smaller, reusable pieces. This makes your code easier to understand, easier to test, and easier to extend. In real programs, functions help organize logic such as calculations, input handling, file processing, and data validation.

---

## Additional Resources

- [Python Official Documentation: Defining Functions](https://docs.python.org/3/tutorial/controlflow.html)
- [Real Python: Defining Your Own Python Function](https://realpython.com/defining-your-own-python-function/)

---

*Last Updated : 4th October, 2026*

---

## Key Takeaways

- A function is a reusable block of code that does a specific job.
- Use the `def` keyword to define a function.
- A function does not run until it is called.
- Parameters are variables inside the function definition.
- Arguments are the values you pass into the function when calling it.
- Functions make programs more organized and reusable.
