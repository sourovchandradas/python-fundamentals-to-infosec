# while Loops in Python

## Overview

While `for` loops take a collection of items and execute a block of code once for each item, `while` loops run continuously as long as a specified condition remains true. They are essential for building interactive applications, game loops, and programs that need to execute until explicitly stopped by the user.

This guide covers:
- **The `while` loop syntax** - controlling repetition using conditional statements
- **User-controlled termination** - accepting exit commands like `'quit'`
- **Flags** - managing complex program states with boolean signals
- **Control flow statements** - interrupting loops using `break` and `continue`
- **Infinite loops** - preventing and handling non-terminating code execution

---

## Table of Contents

1. [The while Loop in Action](#the-while-loop-in-action)
2. [Letting the User Choose When to Quit](#letting-the-user-choose-when-to-quit)
3. [Using a Flag](#using-a-flag)
4. [Using break to Exit a Loop](#using-break-to-exit-a-loop)
5. [Using continue in a Loop](#using-continue-in-a-loop)
6. [Avoiding Infinite Loops](#avoiding-infinite-loops)
7. [Exercises](#exercises)

---

## The while Loop in Action

### What is a while Loop?

A `while` loop tests a condition before executing the loop body. If the condition evaluates to `True`, the code inside executes. This process repeats until the condition evaluates to `False`.

### Basic Counting Example

```python
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
```

**Output:**

```
1
2
3
4
5
```

### Execution Flow

1. The variable `current_number` is initialized to `1`.
2. The `while` loop evaluates `current_number <= 5`.
3. Inside the loop, `current_number += 1` increments the counter (shorthand for `current_number = current_number + 1`).
4. Once `current_number` becomes `6`, the loop condition evaluates to `False` and program execution halts.

---

## Letting the User Choose When to Quit

### Interactive Execution Loops

By wrapping an `input()` prompt inside a `while` loop, you can make a program run continuously until the user inputs a specific quit value.

```python
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
```

**Output:**

```
Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program. Hello everyone!
Hello everyone!

Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program. quit
```

### Key Considerations

* **Variable Initialization:** `message = ""` gives the variable an initial value so Python can perform the comparison `message != 'quit'` on the very first iteration.
* **Filtering Output:** The `if message != 'quit'` check prevents the program from printing the word `'quit'` as if it were regular input.

---

## Using a Flag

### What is a Flag?

For complex programs where many different events could cause execution to stop (such as a game ending when time runs out, lives reach zero, or a player quits), checking all conditions in a single `while` statement becomes unmaintainable.

A **flag** is a boolean variable that acts as a signal to determine whether the entire program is active.

### Implementation Example

```python
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)
```

### Benefits of Flags

* Simplifies the `while` statement condition down to checking `while active:`.
* Allows multiple condition checks (`if`, `elif`) inside the loop body to set `active = False` cleanly.

---

## Using break to Exit a Loop

### Immediate Loop Termination

The `break` statement immediately stops execution of a `while` or `for` loop without executing any remaining code inside the loop.

```python
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")
```

**Output:**

```
Please enter the name of a city you have visited:
(Enter 'quit' when you are finished.) New York
I'd love to go to New York!

Please enter the name of a city you have visited:
(Enter 'quit' when you are finished.) quit
```

**Note:** A loop starting with `while True` will run indefinitely unless it encounters a `break` statement.

---

## Using continue in a Loop

### Skipping Current Iterations

The `continue` statement skips the remaining code in the loop for the current iteration and jumps directly back to evaluating the loop condition.

```python
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)
```

**Output:**

```
1
3
5
7
9
```

---

## Avoiding Infinite Loops

### Preventing Infinite Execution

Every `while` loop requires a mechanism to make its condition evaluate to `False` or reach a `break` statement.

**Incorrect Code (Infinite Loop):**

```python
# This loop runs forever because x is never incremented
x = 1
while x <= 5:
    print(x)
    # Missing: x += 1
```

### Handling an Infinite Loop

* Press **`Ctrl + C`** in the terminal to forcibly terminate execution.
* If running inside certain embedded editor windows, close the terminal session or editor process.

---

## Exercises

File naming convention: Use descriptive, lowercase names with underscores (e.g., `pizza_toppings.py`).

### Exercise 7-4: Pizza Toppings

Write a loop that prompts the user to enter a series of pizza toppings until they enter a `'quit'` value. As each topping is entered, print a message stating that the topping will be added to their pizza.

**Expected Output**
```
Enter a pizza topping (or 'quit' to finish): pepperoni
I'll add pepperoni to your pizza!

Enter a pizza topping (or 'quit' to finish): mushrooms
I'll add mushrooms to your pizza!

Enter a pizza topping (or 'quit' to finish): quit
```

### Exercise 7-5: Movie Tickets

A movie theater charges different ticket prices depending on age:

* Under 3: Free
* Age 3 to 12: $10
* Over 12: $15

**Expected Output**
```
Please enter your age (or 'quit' to exit): 2
Your ticket is free!

Please enter your age (or 'quit' to exit): 8
Your ticket is $10.

Please enter your age (or 'quit' to exit): 25
Your ticket is $15.

Please enter your age (or 'quit' to exit): quit
```

Write a loop that prompts users for their age and displays their ticket cost.

### Exercise 7-6: Three Exits

Write different versions of Exercise 7-4 or 7-5 that achieve termination by:

1. Using a conditional test in the `while` statement.
2. Using an `active` variable (flag).
3. Using a `break` statement.

**Expected Output:**

(The runtime output remains identical to Exercise 7-4 or 7-5 depending on the version implemented, demonstrating different loop control mechanisms under the hood.)

### Exercise 7-7: Infinity

Write a loop that never ends, run it, and terminate it using `Ctrl + C`.

**Expected Output**
```
Looping forever...
Looping forever...
Looping forever...
^C
Traceback (most recent call last):
  File "infinity.py", line 2, in <module>
KeyboardInterrupt
```
---

## Quick Reference

| Concept | Code Pattern | Description |
| --- | --- | --- |
| Basic Loop | `while condition:` | Executes as long as condition evaluates to `True` |
| Infinite Loop | `while True:` | Runs continuously until a `break` statement executes |
| Flag Signal | `active = True` | Boolean state monitor for complex loop exits |
| Exit Loop | `break` | Immediately terminates the loop |
| Skip Iteration | `continue` | Jumps to the start of the next iteration |
| Counter Increment | `x += 1` | Updates loop variable to prevent infinite loops |

---

## Related Topics

* [User Input](../how_the_input_function_works/how_the_input_function_works.md) - Accepting input using `input()`
* [if Statements](../../05_if_statements/if_statements/if_statements.md) - Conditional decision-making
* [Looping through an entire list](../../04_working_with_lists/looping_through_an_entire_list/looping_through_an_entire_list.md) - Iterating over sequences and collections

---

## Additional Resources

* [Python Official Documentation: while Statements](https://docs.python.org/3/reference/compound_stmts.html)
* [Real Python: Python "while" Loops](https://realpython.com/python-while-loop/)

---

*Last Updated: 3rd October, 2026*
