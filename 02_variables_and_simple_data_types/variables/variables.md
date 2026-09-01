# Variables in Python

## Overview

Variables are containers for storing data values. They are the foundation of programming, allowing us to store, retrieve, and manipulate information throughout our programs. A variable is simply a name that refers to a value stored in memory. In this guide, we'll learn how to create variables, follow naming conventions, understand how Python manages variables internally, and avoid common errors like NameErrors that occur from typos or undefined variables.

---

## Table of Contents

1. [Using Variables](#using-variables)
2. [Naming and Using Variables](#naming-and-using-variables)
3. [Avoiding Name Errors](#avoiding-name-errors-when-using-variables)
4. [Exercises](#exercises)

---

## Using Variables

### What is a Variable?

A **variable** holds a value, which is the information associated with that variable. When Python processes code, the interpreter associates the value with the variable name.

```python
message = "Hello Python world!"
print(message)
```

**Output:**
```
Hello Python world!
```

### Changing Variable Values

You can change the value of a variable at any time. Python will always keep track of its current value:

```python
message = "Hello Python world!"
print(message)

message = "My goal is to become a cybersecurity engineer."
print(message)
```

**Output:**
```
Hello Python world!
My goal is to become a cybersecurity engineer.
```

### Variables as Labels (Internal Representation)

**Important Concept:** Variables are often described as "boxes" to store values in, but this is misleading.

**Better Mental Model:** Think of variables as **labels** that you assign to values, or as **references** to a certain value.

**Why does this matter?**
- While this distinction may not matter in initial programs
- An accurate understanding helps when you encounter unexpected variable behavior later
- It's fundamental to understanding Python's memory model

---

## Naming and Using Variables

### Rules & Guidelines

Follow these rules when naming variables:

| Rule | Example | Invalid Example |
|------|---------|-----------------|
| **Letters, numbers, underscores only** | `message_1` | `message-1` |
| **Can start with letter or underscore** | `_message`, `message` | `1_message` |
| **No spaces in names** | `greeting_message` | `greeting message` |
| **Avoid Python keywords** | `my_print` | `print` |
| **Descriptive names** | `student_name` | `s_n` |
| **Lowercase convention** | `my_variable` | `MyVariable` |

### Detailed Guidelines

#### 1. Valid Characters
Variable names can contain only:
- Letters (a-z, A-Z)
- Numbers (0-9)
- Underscores (_)

```python
# Valid
message_1 = "Hello"
_private = "Secret"
name = "John"

# Invalid - will cause SyntaxError
message-1 = "Hello"      # Hyphen not allowed
1_message = "Hello"      # Cannot start with number
```

#### 2. Spacing
Underscores can separate words, but spaces cannot:

```python
# Valid
greeting_message = "Hello"
full_name = "John Doe"

# Invalid - SyntaxError
greeting message = "Hello"
```

#### 3. Reserved Keywords
Avoid using Python keywords and function names:

```python
# Invalid - these are reserved
print = "text"           # print is a built-in function
if = "condition"         # if is a keyword
class = "MyClass"        # class is a keyword
```

#### 4. Descriptive Names
Use clear, descriptive names that explain what the variable stores:

| Better | Worse |
|--------|-------|
| `student_name` | `s_n` |
| `age` | `a` |
| `total_price` | `tp` |
| `is_logged_in` | `log` |

#### 5. Ambiguous Characters
Be careful with lowercase `l` and uppercase `O` - they look like `1` and `0`:

```python
# Confusing - avoid
l = 10           # Is this lowercase L or number 1?
O = 20           # Is this uppercase O or number 0?

# Better
length = 10
count = 20
```

#### 6. Convention
Variables should be written in **lowercase**:

```python
# Preferred
my_variable = "value"

# Works but not recommended
MyVariable = "value"
my_Variable = "value"
```

---

## Avoiding Name Errors When Using Variables

### What is a Traceback?

A **traceback** is a record of where the interpreter ran into trouble when trying to execute your code. It helps you identify and fix errors.

### Common Error: Typos

```python
message = "My goal is to become a cybersecurity engineer."
print(mesage)           # Typo: 'mesage' instead of 'message'
```

**Error Output:**
```
Traceback (most recent call last):
  File "hello_world.py", line 2, in <module>
    print(mesage)
NameError: name 'mesage' is not defined
```

### Understanding the Error

| Part | Meaning |
|------|---------|
| **File "hello_world.py", line 2** | Location of error |
| **print(mesage)** | The problematic code |
| **NameError** | Type of error |
| **name 'mesage' is not defined** | Reason - Python doesn't know this variable |

### Common Causes

| Cause | Example | Solution |
|-------|---------|----------|
| Typo in name | `mesage` | Check spelling carefully |
| Using before defining | `print(x)` before `x = 5` | Define variable first |
| Case sensitivity | `Name` vs `name` | Variables are case-sensitive |

### Case Sensitivity

Python treats `message` and `Message` as different variables:

```python
message = "Hello"
print(Message)          # NameError: name 'Message' is not defined
```

**Python is case-sensitive!**

### Spelling Consistency

Interestingly, if you misspell a variable name *consistently*, the code still runs:

```python
mesage = "My goal is to become a cybersecurity engineer."
print(mesage)           # No error - both use same (misspelled) name
```

**Output:**
```
My goal is to become a cybersecurity engineer.
```

The code works, but the variable name is wrong. This is why careful naming is important!

### Quick Troubleshooting Guide

If you get a `NameError`:

1. **Check spelling** - Is the variable name spelled correctly?
2. **Check case** - Is it `message` or `Message`?
3. **Check definition** - Have you defined the variable before using it?
4. **Check typos** - Did you accidentally press a nearby key?

### Learning Tip

✨ **Typos happen to all programmers!** Don't get frustrated. Even experienced developers make these mistakes. The key is learning to read error messages carefully to identify and fix them.

---

## Exercises

File naming convention: Use descriptive, lowercase names with underscores (e.g., `simple_message.py`)

### Exercise 2-1: Simple Message

**Task:**
1. Store a message in a variable
2. Print that message

**Example:**
```python
message = "Python is awesome!"
print(message)
```

**Output:**
```
Python is awesome!
```

### Exercise 2-2: Simple Messages

**Task:**
1. Store a message in a variable
2. Print that message
3. Change the value to a new message
4. Print the new message

**Example:**
```python
message = "Hello, Python!"
print(message)

message = "I'm learning to code!"
print(message)
```

**Output:**
```
Hello, Python!
I'm learning to code!
```

---

## Quick Reference

| Concept | Example | Notes |
|---------|---------|-------|
| Assign variable | `name = "John"` | Creates a variable |
| Use variable | `print(name)` | References the value |
| Change value | `name = "Jane"` | Reassigns variable |
| Valid name | `first_name` | Letters, numbers, underscores |
| Invalid name | `first-name` | Hyphens not allowed |
| Case sensitive | `name` ≠ `Name` | Different variables |

---

## Common Mistakes to Avoid

```python
# ❌ Starting with number
1_name = "John"

# ❌ Using spaces
first name = "John"

# ❌ Using reserved keyword
print = "text"

# ❌ Using hyphens
first-name = "John"

# ❌ Forgetting to define before use
print(age)              # NameError
age = 25

# ✅ Correct approaches
name_1 = "John"
first_name = "John"
my_print = "text"
first_name = "John"
age = 25
print(age)
```

---

## Related Topics

- [Numbers](../numbers/numbers.md) - Learn about integers and floats
- [Strings](../strings/strings.md) - Learn about text data and string manipulation
- [Data Types](../../03_data_structures/) - Explore more complex data structures

---

## Additional Resources

- [Python Official Documentation: Variables](https://docs.python.org/3/tutorial/introduction.html#an-informal-introduction-to-python)
- [Real Python: Variables in Python](https://realpython.com/python-variables/)
- [PEP 8: Python Naming Conventions](https://www.python.org/dev/peps/pep-0008/#naming-conventions)

---

*Last Updated: 2026-09-01*
