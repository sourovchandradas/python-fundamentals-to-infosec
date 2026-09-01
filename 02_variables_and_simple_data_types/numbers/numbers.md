# Numbers in Python

## Overview

Numbers are fundamental to programming. They are used to keep score in games, represent data in visualizations, store information in web applications, and perform countless calculations. Python treats numbers in several different ways depending on how they are being used.

This guide covers:
- **Integers** - whole numbers without decimal points
- **Floats** - numbers with decimal points
- **Type conversion** - converting between different data types
- **Python 2 vs Python 3** - historical differences in number handling

---

## Table of Contents

1. [Integers](#integers)
2. [Floats](#floats)
3. [Type Errors with str()](#type-errors-with-str)
4. [Python 2 Legacy](#python-2-legacy)
5. [Exercises](#exercises)

---

## Integers

### What are Integers?

An **integer** is a whole number without a decimal point. Python supports basic arithmetic operations on integers:

| Operation | Operator | Example | Result |
|-----------|----------|---------|--------|
| Addition | `+` | `2 + 3` | `5` |
| Subtraction | `-` | `3 - 2` | `1` |
| Multiplication | `*` | `2 * 3` | `6` |
| Division | `/` | `3 / 2` | `1.5` |

### Exponents

Python uses the `**` operator to represent exponents:

```python
>>> 3 ** 2
9
>>> 3 ** 3
27
>>> 10 ** 6
1000000
```

### Order of Operations

Python follows the standard order of operations (PEMDAS). You can use parentheses to modify the evaluation order:

```python
>>> 2 + 3*4
14
>>> (2 + 3) * 4
20
```

**Note:** Spacing has no effect on how Python evaluates expressions—it simply helps with readability.

---

## Floats

### What are Floats?

A **float** is any number with a decimal point. The term "float" refers to the fact that the decimal point can appear at any position in the number.

### Basic Float Operations

```python
>>> 0.1 + 0.1
0.2
>>> 0.2 + 0.2
0.4
>>> 2 * 0.1
0.2
>>> 2 * 0.2
0.4
```

### Floating-Point Precision Issues

Be aware that you may sometimes get an arbitrary number of decimal places in your results:

```python
>>> 0.2 + 0.1
0.30000000000000004
>>> 3 * 0.1
0.30000000000000004
```

**Why does this happen?**  
This occurs in all programming languages. Computers represent numbers internally using binary, which sometimes cannot represent decimal values exactly. Python tries to find the most precise representation possible.

**For now:** Simply ignore the extra decimal places. You'll learn how to handle them properly when working with projects later.

---

## Type Errors with str()

### The Problem

When working with numbers and strings together, you may encounter a `TypeError`. For example:

```python
age = 23
message = "Happy " + age + "rd Birthday!"
print(message)
```

**Error Output:**
```
Traceback (most recent call last):
  File "birthday.py", line 2, in <module>
    message = "Happy " + age + "rd Birthday!"
TypeError: Can't convert 'int' object to str implicitly
```

### Why This Happens

Python sees that you're trying to concatenate strings with an integer. It's unclear whether you want:
- The **numerical value** `23`, or
- The **string characters** `"23"`

### The Solution

Use the `str()` function to explicitly convert the integer to a string:

```python
age = 23
message = "Happy " + str(age) + "rd Birthday!"
print(message)
```

**Output:**
```
Happy 23rd Birthday!
```

### Key Takeaway

When working with numbers in Python, if you get unexpected results, check whether Python is interpreting your numbers correctly:
- As a **numerical value** (for calculations)
- As a **string value** (for display or concatenation)

---

## Python 2 Legacy

### Different Division Behavior

Python 2 handled integer division differently than Python 3:

```python
# Python 2.7
>>> 3 / 2
1

# Python 3.x
>>> 3 / 2
1.5
```

In Python 2, dividing two integers returns an integer with the remainder truncated (not rounded).

### Workaround in Python 2

To ensure float division in Python 2, make at least one operand a float:

```python
# Python 2.7
>>> 3 / 2
1
>>> 3.0 / 2
1.5
>>> 3 / 2.0
1.5
>>> 3.0 / 2.0
1.5
```

### Why This Matters

This is a common source of confusion when switching between Python 2 and Python 3. If you work with legacy code using Python 2, be careful when mixing integers and floats.

---

## Exercises

File naming convention: Use descriptive, lowercase names with underscores (e.g., `numbers_eight.py`)

### Exercise 2-8: Number Eight

Write addition, subtraction, multiplication, and division operations that each result in the number 8. Use `print()` statements to display the results.

**Expected output:**
```
8
8
8
8
```

**Example:**
```python
print(5 + 3)
```

### Exercise 2-9: Favorite Number

1. Store your favorite number in a variable
2. Create a message that reveals your favorite number
3. Print the message

**Example output:**
```
My favorite number is 7!
```

---

## Quick Reference

| Concept | Example | Result |
|---------|---------|--------|
| Integer | `42` | A whole number |
| Float | `3.14` | A decimal number |
| Exponent | `2 ** 3` | `8` |
| Convert to String | `str(23)` | `"23"` |
| Integer Division (Python 3) | `7 / 2` | `3.5` |
| Integer Division (Python 2) | `7 / 2` | `3` |

---

## Related Topics

- [Variables](../variables/variables.md) - Learn how to store and manage data
- [Strings](../strings/strings.md) - Learn about text data and string manipulation
- [Data Types](../../03_data_structures/) - Explore more complex data structures

---

## Additional Resources

- [Python Official Documentation: Numbers](https://docs.python.org/3/tutorial/introduction.html#numbers)
- [Real Python: Python Numbers](https://realpython.com/python-numbers/)

---

*Last Updated: 2026-09-01*
