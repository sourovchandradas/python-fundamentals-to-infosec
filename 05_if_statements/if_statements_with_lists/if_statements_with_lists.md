# Using if Statements with Lists

## Overview

You can do powerful and interesting work when you combine **lists** and **`if` statements**. Combining these concepts allows your programs to:
- Watch for special values that need to be treated differently from other items in a list.
- Manage changing real-world conditions efficiently (such as ingredient availability in a restaurant).
- Ensure your code behaves predictably across all edge cases, including empty input handling and external data validation.

---

## Table of Contents

1. [Checking for Special Items](#checking-for-special-items)
2. [Checking That a List Is Not Empty](#checking-that-a-list-is-not-empty)
3. [Using Multiple Lists](#using-multiple-lists)
4. [Exercises](#exercises)
5. [Quick Reference](#quick-reference)

---

## Checking for Special Items

When looping through a list, you may need to apply custom logic to specific items while handling remaining items normally.

### Simple Iteration Baseline

Consider a pizzeria program that announces each topping as it is added to a pizza:

```python
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!")
```

**Output:**
```text
Adding mushrooms.
Adding green peppers.
Adding extra cheese.

Finished making your pizza!
```

### Handling Out-of-Stock Items Inside a Loop

If the restaurant runs out of an ingredient (e.g., green peppers), you can intercept that specific value inside the loop using an `if` statement:

```python
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!")
```

**Output:**
```text
Adding mushrooms.
Sorry, we are out of green peppers right now.
Adding extra cheese.

Finished making your pizza!
```

### Execution Logic Breakdown

1. The `for` loop inspects each element in `requested_toppings` sequentially.
2. The `if requested_topping == 'green peppers':` condition evaluates whether the current item is `'green peppers'`.
3. If `True`, Python skips adding the topping and prints an apology message.
4. The `else` clause guarantees that all other available toppings continue to be processed normally.

---

## Checking That a List Is Not Empty

In real-world applications, user inputs or database queries dictate list contents. You cannot always assume a list contains elements before executing a loop.

### Python Truthiness for Lists

Python automatically evaluates list conditions based on their content length:
- **Non-empty list** $\rightarrow$ Evaluates to `True`
- **Empty list (`[]`)** $\rightarrow$ Evaluates to `False`

Checking a list's existence before iteration ensures empty lists are handled gracefully without executing unnecessary loop operations.

### Example Script: Validating Order Presence

```python
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
```

**Output:**
```text
Are you sure you want a plain pizza?
```

### Execution Logic Breakdown

1. The variable `requested_toppings` is assigned an empty list `[]`.
2. `if requested_toppings:` checks the truthiness of the collection. Because it is empty, the evaluation yields `False`.
3. Python completely skips the indented `for` loop.
4. Control passes directly to the `else` block, prompting the customer if they intended to order a plain pizza.

---

## Using Multiple Lists

Customers may request items that are not available in a business's inventory. Using multiple lists allows you to validate requested inputs against valid options before processing actions.

> **Design Tip:** If your selection of available options remains fixed during execution, storing available items in a **tuple** instead of a list ensures immutability.

### Example Script: Validating Requests Against Inventory

```python
available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")

print("\nFinished making your pizza!")
```

**Output:**
```text
Adding mushrooms.
Sorry, we don't have french fries.
Adding extra cheese.

Finished making your pizza!
```

### Execution Logic Breakdown

1. **`available_toppings`**: Serves as the authoritative source list of valid items.
2. **`requested_toppings`**: Holds customer inputs (including invalid requests like `'french fries'`).
3. **`for requested_topping in requested_toppings:`**: Iterates through each customer request.
4. **`if requested_topping in available_toppings:`**: Uses the membership operator `in` to check if the requested item exists in the valid inventory.
5. If the test passes, the topping is added. Otherwise, the `else` block triggers, notifying the user that the item is unavailable.

---

## Exercises

### Exercise 5-8: Hello Admin
Make a list of five or more usernames, including the name `'admin'`. Imagine you are writing code that will print a greeting to each user after they log in to a website. Loop through the list, and print a greeting to each user:
- If the username is `'admin'`, print a special greeting, such as *Hello admin, would you like to see a status report?*
- Otherwise, print a generic greeting, such as *Hello Eric, thank you for logging in again.*

### Exercise 5-9: No Users
Add an `if` test to `hello_admin.py` to make sure the list of users is not empty.
- If the list is empty, print the message *We need to find some users!*
- Remove all of the usernames from your list, and make sure the correct message is printed.

### Exercise 5-10: Checking Usernames
Do the following to create a program that simulates how websites ensure that everyone has a unique username.
- Make a list of five or more usernames called `current_users`.
- Make another list of five usernames called `new_users`. Make sure one or two of the new usernames are also in the `current_users` list.
- Loop through the `new_users` list to see if each new username has already been used. If it has, print a message that the person will need to enter a new username. If a username has not been used, print a message saying that the username is available.
- Make sure your comparison is case insensitive. If `'John'` has been used, `'JOHN'` should not be accepted. (Hint: Remember to make a lowercased copy of `current_users` for comparisons.)

### Exercise 5-11: Ordinal Numbers
Ordinal numbers indicate their position in a list, such as `1st` or `2nd`. Most ordinal numbers end in *th*, except 1, 2, and 3.
- Store the numbers 1 through 9 in a list.
- Loop through the list.
- Use an `if-elif-else` chain inside the loop to print the proper ordinal ending for each number. Your output should read `"1st 2nd 3rd 4th 5th 6th 7th 8th 9th"`, and each result should be on a separate line.

---

## Quick Reference

| Pattern | Code Pattern | Evaluation Purpose |
| --- | --- | --- |
| **Special Value Check** | `if item == 'special_value':` | Intercepts single specific list elements for unique processing |
| **Empty List Check** | `if list_name:` | Evaluates collection truthiness before iterating |
| **Cross-List Validation** | `if item in master_list:` | Validates input existence against a reference collection |
