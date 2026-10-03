# while Loops in Python

## Overview

A `for` loop is useful when you already know how many times you want to iterate, or when you want to go through a collection of items one by one. A `while` loop is different: it keeps running as long as a condition remains true.

This makes `while` loops ideal for programs that need to keep running until a user chooses to quit, until a condition changes, or until a task is complete. They are especially useful in interactive programs, repeated input handling, and situations where the number of iterations is not known in advance.

This guide covers:
- the `while` loop syntax and basic behavior
- user-controlled termination using input and quit conditions
- using flags to manage loop state
- exiting loops with `break`
- skipping iterations with `continue`
- avoiding infinite loops

---

## Table of Contents

1. [The while Loop in Action](#the-while-loop-in-action)
2. [Letting the User Choose When to Quit](#letting-the-user-choose-when-to-quit)
3. [Using a Flag](#using-a-flag)
4. [Using break to Exit a Loop](#using-break-to-exit-a-loop)
5. [Using continue in a Loop](#using-continue-in-a-loop)
6. [Avoiding Infinite Loops](#avoiding-infinite-loops)
7. [Exercises](#exercises)
8. [Quick Reference](#quick-reference)
9. [Related Topics](#related-topics)
10. [Additional Resources](#additional-resources)

---

## The while Loop in Action

### What is a while Loop?

A `while` loop checks a condition before each iteration. If the condition evaluates to `True`, the code inside the loop runs. After each pass, Python checks the condition again. The loop continues until the condition becomes `False`.

This is different from a `for` loop, which is designed to iterate over a known collection or a fixed range.

### Basic Counting Example

```python
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
```

**Output:**

```python
1
2
3
4
5
```

### Execution Flow

1. The variable `current_number` is initialized to `1`.
2. Python checks whether `current_number <= 5`.
3. Because the condition is `True`, the loop body runs.
4. Inside the loop, `current_number += 1` increases the counter.
5. Python checks the condition again.
6. When `current_number` becomes `6`, the condition is `False`, and the loop ends.

### Why This Matters

While loops are used when the number of iterations depends on changing values, user choices, or runtime conditions rather than a fixed sequence.

---

## Letting the User Choose When to Quit

### Interactive Execution Loops

A common use of `while` loops is to keep a program running until the user chooses to stop. This is a simple way to build interactive tools and menus.

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

```python
Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program. Hello everyone!
Hello everyone!

Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program. quit
```

### Key Considerations

* **Variable Initialization:** `message = ""` gives the variable an initial value so Python can compare it on the first loop check.
* **Filtering Output:** The `if message != 'quit'` check prevents the word `'quit'` from being printed as if it were ordinary input.
* **User Control:** The user decides when the loop should end.

This structure is often used in chat programs, simple games, and menu systems.

---

## Using a Flag

### What is a Flag?

A flag is a boolean variable used to represent the current state of a program. It acts like a switch that tells the program whether it should keep running.

For example, a game may continue until the player's lives reach zero or the user quits. In that case, a flag such as `active = True` can control the loop.

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

* The loop condition is simple: `while active:`
* You can check multiple conditions inside the loop
* The program can stop because of different events, not just one comparison

Flags are especially useful when a program has more than one reason to stop.

---

## Using break to Exit a Loop

### Immediate Loop Termination

The `break` statement immediately exits a loop, even if the loop condition would still be true. It is useful when you want to stop the loop as soon as a specific event happens.

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

```python
Please enter the name of a city you have visited:
(Enter 'quit' when you are finished.) New York
I'd love to go to New York!

Please enter the name of a city you have visited:
(Enter 'quit' when you are finished.) quit
```

### Important Note

A loop written as `while True:` runs forever unless it encounters a `break` statement. This pattern is common in interactive programs, but it must be used carefully.

---

## Using continue in a Loop

### Skipping Current Iterations

The `continue` statement tells Python to skip the rest of the current loop iteration and start the next one immediately. It is useful when you want to ignore some values without ending the whole loop.

```python
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)
```

**Output:**

```python
1
3
5
7
9
```

### Why Use `continue`?

The loop still runs, but for even numbers the program skips the `print()` statement and moves to the next cycle. This is useful when filtering out unwanted values or processing only selected cases.

---

## Avoiding Infinite Loops

### Preventing Infinite Execution

Every `while` loop must eventually reach a point where the condition becomes `False` or it must hit a `break` statement. If that never happens, the loop runs forever.

**Incorrect Code (Infinite Loop):**

```python
# This loop runs forever because x is never incremented
x = 1
while x <= 5:
    print(x)
    # Missing: x += 1
```

### Common Fixes

* Update the variable used in the condition
* Use a `break` statement when a stopping condition is reached
* Make sure the loop condition can eventually become `False`

### Handling an Infinite Loop

If your loop gets stuck:

* Press **`Ctrl + C`** in the terminal to forcibly terminate execution.
* In some editors or embedded environments, close the terminal session or stop the running process.

---

## Exercises

File naming convention: Use descriptive, lowercase names with underscores (e.g., `pizza_toppings.py`).

### Exercise 7-4: Pizza Toppings

Write a loop that prompts the user to enter a series of pizza toppings until they enter a `'quit'` value. As each topping is entered, print a message stating that the topping will be added to their pizza.

**Expected Output**

```python
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

```python
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

The runtime output remains the same as the chosen exercise, but the program uses different loop-control techniques internally.

### Exercise 7-7: Infinity

Write a loop that never ends, run it, and terminate it using `Ctrl + C`.

**Expected Output**

```python
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
| Basic Loop | `while condition:` | Executes as long as the condition remains `True` |
| Infinite Loop | `while True:` | Runs continuously until a `break` statement executes |
| Flag Signal | `active = True` | Boolean state monitor for complex loop exits |
| Exit Loop | `break` | Immediately terminates the current loop |
| Skip Iteration | `continue` | Skips the rest of the current iteration |
| Counter Increment | `x += 1` | Updates the loop variable to prevent infinite loops |

---

## Related Topics

* [User Input](../how_the_input_function_works/how_the_input_function_works.md) - Accepting input using `input()`
* [if Statements](../../05_if_statements/if_statements/if_statements.md) - Conditional decision-making
* [Looping through an Entire List](../../04_working_with_lists/looping_through_an_entire_list/looping_through_an_entire_list.md) - Iterating over sequences and collections

---

## Additional Resources

* [Python Official Documentation: while Statements](https://docs.python.org/3/reference/compound_stmts.html)
* [Real Python: Python "while" Loops](https://realpython.com/python-while-loop/)

---

*Last Updated: 3rd October, 2026*
