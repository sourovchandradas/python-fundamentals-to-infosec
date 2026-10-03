# while Loop with Lists and Dictionaries in Python

## Overview

While `for` loops are ideal for stepping through a sequence, you should **never modify a list** (adding or removing items) while iterating over it with a `for` loop. Because Python uses element index positions to keep track of progress, modifying the list during iteration causes Python to miscalculate indices, leading to skipped elements or runtime errors.

To safely alter, move, or clean up items in a collection, use a `while` loop. Combining `while` loops with lists and dictionaries allows you to collect, process, and organize structured user data dynamically.

This guide covers:
- **Transferring list elements** - moving items safely between queues using `pop()` and `append()`
- **Purging duplicate values** - using `while` loops with membership tests (`in`) to remove all instances of a value
- **Populating dictionaries** - building key-value pairs from continuous user prompts
- **Truthiness in collections** - leveraging empty list evaluation (`while list:`) as loop conditions

---

## Table of Contents

1. [Moving Items from One List to Another](#moving-items-from-one-list-to-another)
2. [Removing All Instances of Specific Values from a List](#removing-all-instances-of-specific-values-from-a-list)
3. [Filling a Dictionary with User Input](#filling-a-dictionary-with-user-input)
4. [Exercises](#exercises)

---

## Moving Items from One List to Another

### Why Use a while Loop?

Web applications frequently use queues—such as verifying newly registered users or processing items in a shopping cart. A `while` loop allows you to extract items from an unprocessed list one at a time and move them to a processed list until the source list is empty.

### Truthy / Falsy List Evaluation

In Python, an empty list `[]` evaluates to `False` in a boolean context, while a list containing at least one item evaluates to `True`. Therefore, `while unconfirmed_users:` runs automatically as long as items remain in the list.

### Implementation Example

```python
# Start with users that need to be verified,
# and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
```

**Output:**

```
Verifying user: Candace
Verifying user: Brian
Verifying user: Alice

The following users have been confirmed:
Candace
Brian
Alice
```

### Detailed Execution Trace

1. **Initial State:** `unconfirmed_users = ['alice', 'brian', 'candace']`, `confirmed_users = []`
2. **Iteration 1:** `.pop()` extracts `'candace'`. `current_user = 'candace'`. Appended to `confirmed_users`.
3. **Iteration 2:** `.pop()` extracts `'brian'`. `current_user = 'brian'`. Appended to `confirmed_users`.
4. **Iteration 3:** `.pop()` extracts `'alice'`. `current_user = 'alice'`. Appended to `confirmed_users`.
5. **Iteration 4:** `unconfirmed_users` is now `[]` (`False`). The `while` loop terminates.

---

## Removing All Instances of Specific Values from a List

### Limitation of list.remove()

The standard `list.remove('value')` method removes **only the first occurrence** of a specified value. If duplicate items exist across the list, calling `.remove()` once leaves the rest intact.

### Solution Strategy

Combine a `while` loop with the `in` operator (`while 'value' in list:`). On each iteration, Python checks if the value exists in the list and deletes the first instance found, continuing until zero instances remain.

### Implementation Example

```python
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print("Original list:")
print(pets)

# Remove all occurrences of 'cat' from the list
while 'cat' in pets:
    pets.remove('cat')

print("\nUpdated list:")
print(pets)
```

**Output:**

```
Original list:
['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']

Updated list:
['dog', 'dog', 'goldfish', 'rabbit']
```

---

## Filling a Dictionary with User Input

### Mapping Linked Inputs

You can prompt for multiple related pieces of information inside each iteration of a `while` loop and store them as key-value pairs (`dictionary[key] = value`).

### Implementation Example

```python
responses = {}

# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    # Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # Store the response in the dictionary:
    responses[name] = response

    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat.lower() == 'no':
        polling_active = False

# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name.title()} would like to climb {response.title()}.")
```

**Output:**

```
What is your name? Eric
Which mountain would you like to climb someday? Denali
Would you like to let another person respond? (yes/ no) yes

What is your name? Lynn
Which mountain would you like to climb someday? Devil's Thumb
Would you like to let another person respond? (yes/ no) no

--- Poll Results ---
Eric would like to climb Denali.
Lynn would like to climb Devil's Thumb.
```

---

## Exercises

File naming convention: Use descriptive, lowercase names with underscores (e.g., `deli.py`).

### Exercise 7-8: Deli

Make a list called `sandwich_orders` containing various sandwich names. Make an empty list called `finished_sandwiches`. Loop through `sandwich_orders` using a `while` loop, printing a message for each made order, and transfer it to `finished_sandwiches`. Print a summary of completed sandwiches.

**Expected output:**

```
I made your tuna sandwich.
I made your turkey sandwich.
I made your cheese sandwich.

The following sandwiches have been made:
- Tuna
- Turkey
- Cheese
```

### Exercise 7-9: No Pastrami

Using `sandwich_orders` from Exercise 7-8, ensure `'pastrami'` appears at least three times. Print a message saying the deli has run out of pastrami, then use a `while 'pastrami' in sandwich_orders:` loop to remove all instances of `'pastrami'`. Ensure no pastrami ends up in `finished_sandwiches`.

**Expected output:**

```
Sorry, the deli has run out of pastrami!

I made your tuna sandwich.
I made your turkey sandwich.
I made your cheese sandwich.

The following sandwiches have been made:
- Tuna
- Turkey
- Cheese
```

### Exercise 7-10: Dream Vacation

Write a program that polls users about their dream vacation destination. Store the poll results in a dictionary where user names are keys and dream places are values. Include a prompt to end the poll, then print the survey results.

**Expected output:**

```
What is your name? Sarah
If you could visit one place in the world, where would you go? Japan
Would you like to let another person respond? (yes/ no) no

--- Poll Results ---
Sarah would like to visit Japan.
```

---

## Quick Reference

| Operation | Code Pattern | Description |
| --- | --- | --- |
| Check Non-Empty List | `while my_list:` | Runs as long as `my_list` contains elements |
| Transfer Elements | `item = src.pop()` <br>

<br> `dest.append(item)` | Moves elements from `src` to `dest` queue |
| Purge All Occurrences | `while 'item' in my_list:` <br>

<br> `    my_list.remove('item')` | Deletes all instances of `'item'` from `my_list` |
| Dictionary Input | `my_dict[key] = value` | Maps user input pairs inside a `while` loop |

---

## Related Topics

* [Lists](../../03_introducing_list/lists/lists.md) - Learn about list methods like `.pop()` and `.remove()`
* [Dictionaries](../../06_dictionaries/working_with_dictionaries/working_with_dictionaries.md) - Store linked key-value pair records
* [While Loops](../introducing_while_loops/introducing_while_loops.md) - Master loop control with `break` and `continue`

---

## Additional Resources

* [Python Official Documentation: Data Structures](https://www.google.com/search?q=https://docs.python.org/3/tutorial/datastructures.html)
* [Real Python: Python's list.remove() and list.pop()](https://www.google.com/search?q=https://realpython.com/python-pop-list-element/)

---

*Last Updated: 2026-10-03*
