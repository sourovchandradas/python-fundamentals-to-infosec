# while Loop with Lists and Dictionaries in Python

## Overview

A `for` loop is useful when you want to iterate over a collection without changing it. But when the collection itself must be modified while you are processing it, a `while` loop is often the better choice.

This is especially important with lists and dictionaries, which often change as user input is collected, items are validated, or data is moved between containers. In Python, modifying a list during a `for` loop can cause skipped or repeated items because Python keeps track of indexes internally. A `while` loop avoids that problem by checking a condition each time before continuing.

This guide covers:
- moving items from one list to another
- removing repeated values from a list safely
- collecting user input in a dictionary
- using truthiness with lists and dictionaries
- common mistakes to avoid when working with `while` loops

---

## Table of Contents

1. [Moving Items from One List to Another](#moving-items-from-one-list-to-another)
2. [Removing All Instances of Specific Values from a List](#removing-all-instances-of-specific-values-from-a-list)
3. [Filling a Dictionary with User Input](#filling-a-dictionary-with-user-input)
4. [Common Mistakes](#common-mistakes)
5. [Exercises](#exercises)
6. [Quick Reference](#quick-reference)
7. [Related Topics](#related-topics)
8. [Additional Resources](#additional-resources)

---

## Moving Items from One List to Another

### Why Use a while Loop?

In many real programs, data is processed in batches. For example, a user registration system may keep a list of unconfirmed users and move each one to a confirmed list after verification. Because the size of the list changes during processing, a `while` loop is a natural fit.

A `while` loop keeps running as long as a condition is true. This makes it ideal when the loop depends on the current state of a list rather than a fixed number of iterations.

### Truthy / Falsy List Evaluation

In Python, empty collections are considered falsy, while non-empty collections are truthy. This means:

```python
while unconfirmed_users:
    ...
```

works because the loop runs only while the list still contains items. When the list becomes empty, the condition becomes `False` and the loop ends.

This idea also applies to dictionaries:

```python
responses = {}
while responses:
    ...
```

The loop runs only while the dictionary has entries.

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

### Output

```python
Verifying user: Candace
Verifying user: Brian
Verifying user: Alice

The following users have been confirmed:
Candace
Brian
Alice
```

### Detailed Execution Trace

1. Initial state: `unconfirmed_users = ['alice', 'brian', 'candace']`, `confirmed_users = []`
2. Iteration 1: `.pop()` removes `'candace'` and stores it in `current_user`
3. Iteration 2: `.pop()` removes `'brian'`
4. Iteration 3: `.pop()` removes `'alice'`
5. The list becomes empty, so the condition is `False` and the loop stops

### Why `.pop()` Works Here

The `.pop()` method removes the last item from a list and returns it. This is called LIFO behavior (Last In, First Out). It is useful when you want to process the newest item first.

For example, if a user queue is stored in a list, popping the last item often means the most recently added item is processed next.

---

## Removing All Instances of Specific Values from a List

### Limitation of `list.remove()`

The `remove()` method removes only the first matching value. If a list contains repeated values, one call removes only one instance.

```python
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
pets.remove('cat')
print(pets)
```

This would leave one or more `'cat'` values still in the list.

### Solution Strategy

Use a `while` loop with a membership test:

```python
while 'value' in my_list:
    my_list.remove('value')
```

This continues until no matching values remain.

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

### Output

```python
Original list:
['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']

Updated list:
['dog', 'dog', 'goldfish', 'rabbit']
```

### Why This Works

Each time the loop runs, Python checks whether `'cat'` still exists in the list. If it does, the code removes one instance. The loop keeps running until no `'cat'` values remain.

This pattern is helpful when cleaning data, removing rejected values, or filtering user submissions.

---

## Filling a Dictionary with User Input

### Mapping Linked Inputs

A `while` loop can gather multiple related pieces of input and store them as key-value pairs in a dictionary.

This is useful for creating a survey, poll, or record of user responses. Instead of storing a single answer in a variable, you can save each answer under a unique key.

### Implementation Example

```python
responses = {}

# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    # Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # Store the response in the dictionary.
    responses[name] = response

    # Ask whether another person should respond.
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat.lower() == 'no':
        polling_active = False

# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name.title()} would like to climb {response.title()}.")
```

### Output

```python
What is your name? Eric
Which mountain would you like to climb someday? Denali
Would you like to let another person respond? (yes/no) yes

What is your name? Lynn
Which mountain would you like to climb someday? Devil's Thumb
Would you like to let another person respond? (yes/no) no

--- Poll Results ---
Eric would like to climb Denali.
Lynn would like to climb Devil's Thumb.
```

### Why This Is Useful

This pattern is perfect for:
- polling apps
- survey systems
- short registrations
- building dictionaries from repeated user input
- storing dynamic user-generated data

A dictionary lets you map one piece of information to another. In this case, the person's name is the key and their mountain choice is the value.

---

## Common Mistakes

### Mistake 1: Modifying a List While Using a `for` Loop

```python
for item in items:
    items.remove(item)
```

This is unsafe because the list is changing while Python is still iterating over it. The loop may skip items or behave unexpectedly.

### Mistake 2: Using `remove()` Without a Loop

```python
items.remove('cat')
```

This removes only the first match. If the list contains multiple `'cat'` entries, you need a `while` loop to remove all of them.

### Mistake 3: Forgetting to Update the Loop Condition

```python
while polling_active:
    ...
```

If you forget to change `polling_active` to `False`, the loop will run forever.

### Mistake 4: Forgetting to Change the Loop Variable

```python
x = 1
while x <= 5:
    print(x)
```

This creates an infinite loop because `x` never changes. In most loops, you need to update the variable inside the loop so the condition eventually becomes `False`.

---

## Exercises

Use descriptive lowercase names with underscores, such as `deli.py`.

### Exercise 7-8: Deli

Make a list called `sandwich_orders` and fill it with sandwiches such as `'tuna'`, `'turkey'`, and `'cheese'`. Make an empty list called `finished_sandwiches`. Use a `while` loop to process each sandwich order, moving each item from `sandwich_orders` to `finished_sandwiches` as it is completed.

### Exercise 7-9: No Pastrami

Use the `sandwich_orders` list from Exercise 7-8. Ensure `'pastrami'` appears at least three times in the list. Add code at the start to print a message saying the deli has run out of pastrami. Then use a `while` loop to remove all occurrences of `'pastrami'` from `sandwich_orders`.

### Exercise 7-10: Dream Vacation

Write a polling program that asks users: "If you could visit one place in the world, where would you go?" Store the results in a dictionary where the name is the key and the destination is the value. Keep asking until the user decides to stop.

---

## Quick Reference

| Operation | Code Pattern | Description |
| --- | --- | --- |
| Check if list is non-empty | `while my_list:` | Runs while the list still contains values |
| Move items between lists | `item = source.pop(); destination.append(item)` | Transfers data from one list to another |
| Remove all duplicates of one value | `while 'item' in my_list: my_list.remove('item')` | Deletes every matching value |
| Save user input in a dictionary | `responses[name] = answer` | Stores key-value data from repeated prompts |
| Check if a dictionary is non-empty | `while responses:` | Continues while the dictionary has entries |

---

## Related Topics

- [Lists](../../03_introducing_list/lists/lists.md)
- [Dictionaries](../../06_dictionaries/working_with_dictionaries/working_with_dictionaries.md)
- [Introducing While Loops](../introducing_while_loops/introducing_while_loops.md)

---

## Additional Resources

- [Python Official Documentation: Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
- [Real Python: Python Lists](https://realpython.com/python-lists/)
- [Real Python: Python Dictionaries](https://realpython.com/python-dicts/)

---


*Last Modified: 3rd October, 2026*

