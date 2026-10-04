# Defining a Function in Python

## Overview

Functions are named blocks of code designed to perform one specific job. When you want to execute a task defined inside a function, you call that function by name. Writing functions allows you to divide your program into organized, reusable components that execute whenever invoked.

This guide covers:
- **Function syntax** - defining functions using the `def` keyword
- **Docstrings** - documenting function behavior using triple quotes
- **Function calls** - executing code stored inside a function
- **Dynamic inputs** - passing information into functions
- **Parameters vs. Arguments** - understanding the technical distinction

---

## Table of Contents

1. [Defining a Function](#defining-a-function)
2. [Passing Information to a Function](#passing-information-to-a-function)
3. [Arguments and Parameters](#arguments-and-parameters)
4. [Exercises](#exercises)

---

## Defining a Function

### What is a Function?

A function definition establishes the function's name and specifies what information, if any, the function needs to do its job. 

### Syntax Rules

- **The `def` keyword:** Informs Python that a function definition is starting.
- **Function name:** Placed immediately after `def` (e.g., `greet_user`).
- **Parentheses `()`:** Hold information the function needs. Even if no information is required, empty parentheses are strictly required.
- **Colon `:`:** Ends the function definition header line.
- **Function body:** Any indented lines following the definition header make up the body of the function.

### Docstrings

A comment enclosed in triple quotes (`"""..."""`) placed at the beginning of a function body is called a **docstring**. It describes what the function does, and Python looks for docstrings when generating automated documentation for your programs.

### Implementation Example

```python
def greet_user():
    """Display a simple greeting."""
    print("Hello!")

greet_user()
```

**Output:**

```
Hello!
```

### Execution Flow

Defining a function only creates the instructions; it does not execute them. To execute the code inside the function body, you must call the function by writing its name followed by parentheses: `greet_user()`.

---

## Passing Information to a Function

### Customizing Function Output

By modifying a function to accept input, you can pass different values to produce customized output every time the function is called.

### Adding a Parameter

Entering a variable name (e.g., `username`) inside the parentheses of the function definition header allows the function to accept any value you specify when calling it.

### Implementation Example

```python
def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")

greet_user('jesse')
greet_user('sarah')
```

**Output:**

```
Hello, Jesse!
Hello, Sarah!
```

---

## Arguments and Parameters

### Technical Distinction

* **Parameter:** A variable listed inside the parentheses of a function's definition header (e.g., `username`). It represents a piece of information the function needs to perform its task.
* **Argument:** The actual value passed from a function call into the function (e.g., `'jesse'`).

```python
# 'username' is the PARAMETER
def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")

# 'jesse' is the ARGUMENT
greet_user('jesse')
```

### Usage Note

In casual programming context, developers often use the terms "parameter" and "argument" interchangeably. However, maintaining the distinction helps clarify whether you are referring to the variable in the function definition or the value passed in a function call.

---

## Exercises

File naming convention: Use descriptive, lowercase names with underscores (e.g., `message.py`).

### Exercise 8-1: Message

Write a function called `display_message()` that prints one sentence telling everyone what you are learning about in this chapter. Call the function, and make sure the message displays correctly.

**Expected output:**

```
In this chapter, I am learning how to define and call functions in Python.
```

### Exercise 8-2: Favorite Book

Write a function called `favorite_book()` that accepts one parameter, `title`. The function should print a message, such as `"One of my favorite books is Alice in Wonderland."` Call the function, making sure to include a book title as an argument in the function call.

**Expected output:**

```
One of my favorite books is Alice in Wonderland.
```

---

## Quick Reference

| Concept | Syntax / Pattern | Description |
| --- | --- | --- |
| Function Header | `def function_name():` | Declares a new function using the `def` keyword |
| Docstring | `"""Display a greeting."""` | Documents function purpose inside triple quotes |
| Function Call | `function_name()` | Executes the code inside the named function |
| Parameter | `def greet(username):` | Variable inside function header expecting input |
| Argument | `greet('jesse')` | Concrete value passed into a function call |

---

## Related Topics

* [While Loops](https://www.google.com/search?q=../while_loops/while_loops.md) - Repetitive execution and control flow
* [Dictionaries](https://www.google.com/search?q=../dictionaries/dictionaries.md) - Storing key-value pairs
* [Passing Arguments](https://www.google.com/search?q=./passing_arguments.md) - Positional and keyword arguments

---

## Additional Resources

* [Python Official Documentation: Defining Functions](https://www.google.com/search?q=https://docs.python.org/3/tutorial/controlflow.html%23defining-functions)
* [Real Python: Defining Your Own Python Function](https://www.google.com/search?q=https://realpython.com/defining-your-own-python-function/)

---

*Last Updated: 2026-10-04*
