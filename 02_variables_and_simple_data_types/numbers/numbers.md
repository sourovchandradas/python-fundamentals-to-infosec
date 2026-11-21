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
5. [Common Mistake](#common-mistake)
6. [Exercises](#exercises)
7. [Quick Reference](#quick-reference)
8. [Related Topics](#related-topics)
9. [Additional Resources](#additional-resources)
10. [Key Takeaway](#key-takeaway)

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
print(3 ** 2)
print(3 ** 3)
print(10 ** 6)
```
## Outpur
```python
9
27
1000000
```

### Order of Operations

Python follows the standard order of operations (PEMDAS). You can use parentheses to modify the evaluation order:

```python
print(2 + 3 * 4)
print((2 + 3) * 4)
```
## Outcome
```python
14
20
```

**Note:** Spacing has no effect on how Python evaluates expressions—it simply helps with readability.

---

## Floats

### What are Floats?

A **float** is any number with a decimal point. The term "float" refers to the fact that the decimal point can appear at any position in the number.

### Basic Float Operations

```python
print(0.1 + 0.1)
print(0.2 + 0.2)
print(2 * 0.1)
print(2 * 0.2)
```
## Outcome
```python
0.2
0.4
0.2
0.4
```

### Floating-Point Precision Issues

Be aware that you may sometimes get an arbitrary number of decimal places in your results:

```python
print(0.2 + 0.1)
print(3 * 0.1)
```
## Outcome
```python
0.30000000000000004
0.30000000000000004
```

**Why does this happen?**  
This occurs in all programming languages. Computers represent numbers internally using binary, which sometimes cannot represent decimal values exactly. Python tries to find the most precise representation possible.

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

### Key Points

When working with numbers in Python, if you get unexpected results, check whether Python is interpreting your numbers correctly:
- As a **numerical value** (for calculations)
- As a **string value** (for display or concatenation)

---

## Python 2 Legacy

### Different Division Behavior

Python 2 handled integer division differently than Python 3:

```python
# Python 2.7
print(3 / 2)

# Python 3.x
print(3 / 2)
```
### Outcome
```python
1
1.5
```

> In Python 2, dividing two integers returns an integer with the remainder truncated (not rounded).
>
> 

### Workaround in Python 2

To ensure float division in Python 2, make at least one operand a float:

```python
# Python 2.7
print(3 / 2)
print(3.0 / 2)
print(3 / 2.0)
print(3.0 / 2.0)
```
### Outcome
```python
1
1.5
1.5
1.5
```

### Why This Matters

This is a common source of confusion when switching between Python 2 and Python 3. If you work with legacy code using Python 2, be careful when mixing integers and floats.

---

## Common Mistake

* **Mixing text and numbers:** You cannot combine text (strings) and numbers directly.
* **Code that crashes:** `print("I am " + 25 + " years old.")` (Python gets confused because it can't add math to words).
* **The easy fix:** Always use `str()` to turn the number into text first.
* **Correct code:** `print("I am " + str(25) + " years old.")`

---

## Exercises

File naming convention: Use descriptive, lowercase names with underscores (e.g., `numbers_eight.py`)

### Exercise 2-8: Number Eight

Write addition, subtraction, multiplication, and division operations that each result in the number 8. Use `print()` statements to display the results.

* **Solution:** [Exercise 2-8: Number Eight](labs/2.8_number_eight.py)

### Exercise 2-9: Favourite Number

1. Store your favorite number in a variable
2. Create a message that reveals your favorite number
3. Print the message

* **Solution:** [Exercise 2-9: Favorite Number](labs/2.9_favourite_number.py)

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

- [Variables](../variables/variables.md)
- [Strings](../strings/strings.md)
- [Data Types](../../03_data_structures/)

---

## Additional Resources

- [Python Official Documentation: Numbers](https://docs.python.org/3/tutorial/introduction.html#numbers)
- [Real Python: Python Numbers](https://realpython.com/python-numbers/)

---

## Key Takeaway
* **Text vs. Math:** Python treats numbers (for math) and strings (for text) as two completely different things.
* **Use `str()` for sentences:** Whenever you want to print a number inside a sentence, you must wrap it in `str()`.
* **Weird decimals are normal:** If you add decimals (floats) and get a answer like `0.30000000000000004`. It is not an error. This is just how computers calculate decimal numbers behind the scenes.

---

*Last Updated: November 20, 2026*
