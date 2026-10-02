# User Input and While Loops

## Overview

Most programs are written to solve an end user's problem, which usually requires accepting input from the user. Python provides the `input()` function to pause program execution and receive text entered via the terminal. Because Python reads all user input as strings, specialized functions like `int()` and operators like `%` are necessary to handle numerical logic.

This guide covers:
- **The `input()` function** - pausing execution to accept text input
- **Clear prompts** - formatting single-line and multi-line instructions
- **Numerical input with `int()`** - converting string input to numbers for comparison
- **The modulo operator (`%`)** - determining remainders and divisibility
- **Python 2 vs Python 3** - historical security and function differences

---

## Table of Contents

1. [How input() Works](#how-input-works)
2. [Writing Clear Prompts](#writing-clear-prompts)
3. [Numerical Input with int()](#numerical-input-with-int)
4. [The Modulo Operator](#the-modulo-operator)
5. [Python 2 Legacy](#python-2-legacy)
6. [Exercises](#exercises)

---

## How input() Works

### What is input()?

The `input()` function pauses your program and waits for the user to enter text in the terminal. Once input is received, Python assigns that value to a variable as a string.

| Parameter | Type | Description |
|-----------|------|-------------|
| `prompt` | String | The message or instructions displayed to the user |

### Basic Usage

```python
message = input("Tell me something, and I will repeat it back to you: ")
print(message)
```

**Output:**

```
Tell me something, and I will repeat it back to you: Hello everyone!
Hello everyone!
```

### Note on Text Editors

Some text editors (like Sublime Text) or basic execution environments do not support interactive terminal input. Programs containing `input()` must be executed directly from a terminal or command prompt window.

---

## Writing Clear Prompts

### Adding Trailing Spaces

Always include a trailing space at the end of your prompt (after colons or question marks) to separate the prompt text from the user's typed response.

```python
name = input("Please enter your name: ")
print("Hello, " + name + "!")
```

**Output:**

```
Please enter your name: Eric
Hello, Eric!
```

### Multi-Line Prompts

When a prompt requires more than one line of instructions, store the message in a variable and build it across multiple lines using the `+=` operator:

```python
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print("\nHello, " + name + "!")
```

**Output:**

```
If you tell us who you are, we can personalize the messages you see.
What is your first name? Eric

Hello, Eric!
```

---

## Numerical Input with int()

### The Problem

Python interprets **everything** passed into `input()` as a string value. Comparing string input to numerical values causes a `TypeError`.

```python
age = input("How old are you? ")
# User enters 21
print(age >= 18)
```

**Error Output:**

```
Traceback (most recent call last):
  File "age_check.py", line 2, in <module>
    print(age >= 18)
TypeError: unorderable types: str() >= int()
```

### Why This Happens

Python stores the user input as `'21'` (a string) rather than `21` (an integer). Python cannot directly compare string characters to numerical values.

### The Solution

Use the `int()` function to explicitly convert the string input into an integer before performing comparisons or arithmetic:

```python
height = input("How tall are you, in inches? ")
height = int(height)

if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")
```

**Output:**

```
How tall are you, in inches? 71

You're tall enough to ride!
```

---

## The Modulo Operator

### What is the Modulo Operator?

The modulo operator (`%`) divides one number by another and returns **only the remainder**:

```python
>>> 4 % 3
1
>>> 5 % 3
2
>>> 6 % 3
0
>>> 7 % 3
1
```

### Practical Application: Even or Odd Check

When one number is evenly divisible by another, the remainder is `0`. Since even numbers are always divisible by `2`, `number % 2 == 0` evaluates to `True` for even numbers and `False` for odd numbers:

```python
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")
```

**Output:**

```
Enter a number, and I'll tell you if it's even or odd: 42

The number 42 is even.
```

---

## Python 2 Legacy

### raw_input() vs input()

In Python 2.7, prompting for user input differed significantly from Python 3:

```python
# Python 2.7 Standard Input
user_input = raw_input("Enter your name: ")
```

### Why This Matters

* **`raw_input()` (Python 2.7):** Converts all user input to a string (identical to Python 3's `input()`).
* **`input()` (Python 2.7):** Evaluated user input as live Python code. This caused unexpected runtime errors and created severe security vulnerabilities.

---

## Exercises

File naming convention: Use descriptive, lowercase names with underscores (e.g., `rental_car.py`)

### Exercise 7-1: Rental Car

Write a program that asks the user what kind of rental car they would like. Print a message about that car.

**Expected output:**

```
What kind of rental car would you like? Subaru
Let me see if I can find you a Subaru.
```

### Exercise 7-2: Restaurant Seating

Write a program that asks the user how many people are in their dinner group. If the answer is more than eight, print a message saying they'll have to wait. Otherwise, report that their table is ready.

**Expected output:**

```
How many people are in your dinner group? 9
I'm sorry, you'll have to wait for a table.
```

### Exercise 7-3: Multiples of Ten

Ask the user for a number, and then report whether the number is a multiple of 10 or not.

**Expected output:**

```
Enter a number to see if it is a multiple of 10: 50
The number 50 is a multiple of 10.
```

---

## Quick Reference

| Concept | Example | Result |
| --- | --- | --- |
| Accept String Input | `name = input("Name: ")` | Stores user response as `str` |
| Convert to Integer | `age = int(input("Age: "))` | Stores converted response as `int` |
| Multi-line Prompt | `p += "\nLine 2: "` | Appends text to prompt string |
| Modulo Operator | `7 % 3` | `1` (Remainder) |
| Even Check | `num % 2 == 0` | `True` if number is even |
| Python 2 String Input | `raw_input("Prompt: ")` | Legacy string input |

---

## Related Topics

* [Variables](https://www.google.com/search?q=../variables/variables.md) - Learn how to store and manage user data
* [If Statements](https://www.google.com/search?q=../if_statements/if_statements.md) - Make decisions based on user input
* [While Loops](https://www.google.com/search?q=./while_loops.md) - Run programs continuously using user input

---

## Additional Resources

* [Python Official Documentation: input()](https://www.google.com/search?q=https://docs.python.org/3/library/functions.html%23input)
* [Real Python: Basic Input and Output](https://www.google.com/search?q=https://realpython.com/python-input-output/)

---

*Last Updated: 2026-10-02*

```

```
