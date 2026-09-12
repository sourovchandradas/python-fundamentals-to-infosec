# if Statements in Python

## Overview

When you understand conditional tests, you can start writing **`if` statements** to make decisions in your code. Python provides several control flow structures using `if`, `else`, and `elif` keywords. Your choice of structure depends on the number of conditions you need to evaluate:

- **Simple `if` Statement**: Tests one condition and performs an action if `True`.
- **`if-else` Statement**: Performs one action if `True` and a fallback action if `False`.
- **`if-elif-else` Chain**: Evaluates multiple mutually exclusive conditions in sequential order.
- **Independent `if` Statements**: Evaluates multiple non-exclusive conditions where more than one can be `True`.

### Architectural Flow: Decision Structure Execution

```text
                                   +---------------------------------------+
                                   |       Evaluate Conditional Test       |
                                   +---------------------------------------+
                                                       |
                                                       v
                                            /---------------------\
                                           /     Is Condition      \
                                          <      True or False?     >
                                           \                       /
                                            \---------------------/
                                               /               \
                                        True  /                 \  False
                                             /                   \
                                            v                     v
                                 +--------------------+   +--------------------+
                                 |  Execute Indented  |   | Skip Block / Check |
                                 |   Code Block(s)    |   |  Next elif / else  |
                                 +--------------------+   +--------------------+
                                            |                     |
                                            +----------+----------+
                                                       |
                                                       v
                                            +----------------------+
                                            | Continue Execution   |
                                            +----------------------+
```

This guide covers:
- **Simple `if` Statements** - single condition testing and block indentation rules
- **`if-else` Statements** - handling two mutually exclusive branches
- **The `if-elif-else` Chain** - testing multiple conditions with short-circuit evaluation
- **Multiple `elif` Blocks & Omitting `else`** - defensive programming and explicit bounds checking
- **Testing Multiple Conditions** - running series of independent `if` statements

---

## Table of Contents

1. [Simple if Statements](#simple-if-statements)
2. [if-else Statements](#if-else-statements)
3. [The if-elif-else Chain](#the-if-elif-else-chain)
4. [Using Multiple elif Blocks](#using-multiple-elif-blocks)
5. [Omitting the else Block](#omitting-the-else-block)
6. [Testing Multiple Conditions](#testing-multiple-conditions)
7. [Exercises](#exercises)
8. [Quick Reference](#quick-reference)

---

## Simple if Statements

The simplest kind of `if` statement has one condition test and one action block:

```python
if conditional_test:
    do_something
```

If the conditional test evaluates to `True`, Python executes the indented code block. If it evaluates to `False`, Python ignores the block and moves to the next line of code.

### Example Script: `voting.py`

```python
age = 19
if age >= 18:
    print("You are old enough to vote!")
```

**Output:**
```text
You are old enough to vote!
```

### Indentation and Multiple Actions

Indentation defines code blocks in Python. All indented lines following an `if` statement execute when the test passes:

```python
age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
```

**Output:**
```text
You are old enough to vote!
Have you registered to vote yet?
```

> **Note:** If `age` were less than `18`, this program would produce no output because both `print()` calls are inside the indented block.

---

## if-else Statements

Use an `if-else` structure when you want to execute one action when a test passes and a different action when it fails.

```python
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")
```

**Output:**
```text
Sorry, you are too young to vote.
Please register to vote as soon as you turn 18!
```

### Execution Behavior

1. Python checks `age >= 18`. Because `17 >= 18` is `False`, the first indented block is skipped.
2. Control transfers directly to the `else` block, executing its indented statements.
3. In an `if-else` chain, **exactly one** of the two blocks will always execute.

---

## The if-elif-else Chain

To test more than two possible outcomes, use Python's `if-elif-else` syntax. Python executes tests in sequence until one passes, then executes its block and **skips all remaining tests**.

### Example Script: `amusement_park.py`

Pricing rules:
- Under age 4: Free ($0)
- Ages 4 to 17: $5
- Age 18 or older: $10

```python
age = 12

if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")
```

**Output:**
```text
Your admission cost is $5.
```

### Refactoring for Efficiency and Maintainability

Instead of calling `print()` inside every block, set a single `price` variable inside the chain and use one `print()` statement at the end:

```python
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10

print(f"Your admission cost is ${price}.")
```

**Output:**
```text
Your admission cost is $5.
```

> **Tip:** Refactoring code this way reduces duplication. To change the output format later, you only need to update a single line of code.

---

## Using Multiple elif Blocks

You can chain as many `elif` blocks as needed to handle complex business logic.

Adding a senior discount (ages 65 and older pay $5):

```python
age = 68

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5

print(f"Your admission cost is ${price}.")
```

**Output:**
```text
Your admission cost is $5.
```

---

## Omitting the else Block

Python does not require an `else` block at the end of an `if-elif` chain. An explicit `elif` block is often safer than a general `else` statement.

```python
age = 68

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5

print(f"Your admission cost is ${price}.")
```

**Output:**
```text
Your admission cost is $5.
```

### Why Omit `else`? (Defensive Programming)

* The `else` clause is a **catchall**. It executes for any condition not matched by prior checks—including unexpected, invalid, or corrupted data values.
* Using an explicit final `elif` ensures that code executes **only** when specific logic boundaries pass.

---

## Testing Multiple Conditions

An `if-elif-else` chain stops running as soon as one test passes. When you need to check **every** condition of interest (where multiple conditions can be `True` simultaneously), use a series of independent `if` statements.

### Example Script: `toppings.py`

```python
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")
```

**Output:**
```text
Adding mushrooms.
Adding extra cheese.

Finished making your pizza!
```

### Why `if-elif-else` Fails for Multiple Conditions

If rewritten as an `if-elif-else` chain:

```python
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
```

**Output:**
```text
Adding mushrooms.
```

Because `'mushrooms'` passes first, Python short-circuits the rest of the chain, ignoring `'extra cheese'`.

> **Summary Rule:**
> - To execute **only one** block of code: Use an `if-elif-else` chain.
> - To execute **multiple independent** blocks of code: Use separate `if` statements.

---

## Exercises

### Exercise 5-3: Alien Colors #1
Imagine an alien was just shot down in a game. Create a variable called `alien_color` and assign it a value of `'green'`, `'yellow'`, or `'red'`.
- Write an `if` statement to test whether the alien's color is green. If it is, print a message that the player just earned 5 points.
- Write one version of this program that passes the `if` test and another that fails. (The version that fails will have no output.)

### Exercise 5-4: Alien Colors #2
Choose a color for an alien as you did in Exercise 5-3, and write an `if-else` chain.
- If the alien's color is green, print a statement that the player just earned 5 points for shooting the alien.
- If the alien's color isn't green, print a statement that the player just earned 10 points.
- Write one version of this program that runs the `if` block and another that runs the `else` block.

### Exercise 5-5: Alien Colors #3
Turn your `if-else` chain from Exercise 5-4 into an `if-elif-else` chain.
- If the alien is green, print a message that the player earned 5 points.
- If the alien is yellow, print a message that the player earned 10 points.
- If the alien is red, print a message that the player earned 15 points.
- Write three versions of this program, making sure each message is printed for the appropriate color alien.

### Exercise 5-6: Stages of Life
Write an `if-elif-else` chain that determines a person's stage of life. Set a value for the variable `age`, and then:
- If the person is less than 2 years old, print a message that the person is a baby.
- If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
- If the person is at least 4 years old but less than 13, print a message that the person is a kid.
- If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
- If the person is at least 20 years old but less than 65, print a message that the person is an adult.
- If the person is age 65 or older, print a message that the person is an elder.

### Exercise 5-7: Favorite Fruit
Make a list of your favorite fruits, and then write a series of independent `if` statements that check for certain fruits in your list.
- Make a list of your three favorite fruits and call it `favorite_fruits`.
- Write five `if` statements. Each should check whether a certain kind of fruit is in your list. If the fruit is in your list, the `if` block should print a statement, such as *You really like bananas!*

---

## Quick Reference

| Structure | Purpose | Behavior | Best Use Case |
| --- | --- | --- | --- |
| **Simple `if`** | Single condition check | Executes block if `True`, skips if `False` | Triggering isolated actions |
| **`if-else`** | Dual-branch fallback | Guarantees execution of exactly one block | Handling binary choices |
| **`if-elif-else`** | Mutually exclusive checks | Evaluates sequentially; stops at first `True` | Multi-category pricing or grading |
| **Explicit `elif` (No `else`)** | Strict boundary checking | Omits catchall block to avoid handling invalid data | Defensive programming |
| **Independent `if`s** | Non-exclusive evaluations | Evaluates every test regardless of prior results | Applying cumulative choices/filters |

---

## Related Topics

* [Conditional Tests in Python](../conditional_tests/conditional_tests.md) - Expressions evaluating to `True` or `False`
* [Using if Statements with Lists](../if_statements_with_lists/if_statements_with_lists.md) - Truthiness, empty lists, and cross-referencing collections
* [Styling Your Code](../../04_working_with_lists/styling_code/styling_code.md) - PEP 8 indentation guidelines for logical blocks

---

## Additional Resources

* [Python Documentation: Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html)
* [Real Python: Conditional Statements in Python](https://realpython.com/python-conditional-statements/)

---

*Last Updated: 11th September, 2026*
