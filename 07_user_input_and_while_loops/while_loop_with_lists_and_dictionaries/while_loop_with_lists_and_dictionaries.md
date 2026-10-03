# while Loop with Lists and Dictionaries in Python

## Overview

While `for` loops are great for going through a sequence, you should never modify a list while looping over it with a `for` loop. Python keeps track of list positions using indexes. If you add or remove items during iteration, the index positions shift and you may skip elements or get unexpected behavior.

To safely move, remove, or organize items in a collection, use a `while` loop. Combining `while` loops with lists and dictionaries lets you collect, transform, and store user data dynamically.

This guide covers:
- moving items from one list to another
- removing all duplicate values from a list
- collecting user input in a dictionary
- using truthiness with collections

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
9. [Last Modified](#last-modified)

---

## Moving Items from One List to Another

### Why Use a while Loop?

Web applications often work with queues. For example, newly registered users may need to move from an `unconfirmed_users` list to a `confirmed_users` list. A `while` loop is a natural choice because it keeps running until a condition is no longer true.

### Truthy / Falsy List Evaluation

In Python, an empty list `[]` evaluates to `False`, while a list with elements evaluates to `True`. That means this works as expected:

```python
while unconfirmed_users:
    ...
```

The loop continues while the list still has items.

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

---

## Removing All Instances of Specific Values from a List

### Limitation of `list.remove()`

The `remove()` method removes only the first matching value. If a list contains repeated values, one call will remove only one instance.

### Solution Strategy

Use a `while` loop with a membership test:

```python
while 'value' in my_list:
    my_list.remove('value')
```

This continues until no more matching values remain.

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

Each time the loop runs, Python checks whether `'cat'` still exists in the list. If yes, it removes one instance. It continues until no `'cat'` remains.

---

## Filling a Dictionary with User Input

### Mapping Linked Inputs

A `while` loop can gather multiple related pieces of input and store them as key-value pairs in a dictionary.

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

---

## Common Mistakes

### Mistake 1: Modifying a List While Using a for Loop

```python
for item in items:
    items.remove(item)
```

This is unsafe because the list is changing while Python is still iterating over it.

### Mistake 2: Using `remove()` Without a Loop

```python
items.remove('cat')
```

This removes only the first match. If the list contains multiple `'cat'` entries, you need a `while` loop.

### Mistake 3: Forgetting to Update the Loop Condition

```python
while polling_active:
    ...
```

If you forget to change `polling_active` to `False`, the loop will run forever.

---

## Exercises

Use descriptive lowercase names with underscores, such as `deli.py`.

### Exercise 7-8: Deli

Make a list called `sandwich_orders` and fill it with sandwiches such as `'tuna'`, `'turkey'`, and `'cheese'`. Make an empty list called `finished_sandwiches`. Use a `while` loop to process each order and move it to the finished list. Print a message for each sandwich as it is completed, then print a summary of the finished sandwiches.

### Exercise 7-9: No Pastrami

Use the `sandwich_orders` list from Exercise 7-8. Ensure `'pastrami'` appears at least three times in the list. Add code at the start to print a message saying the deli has run out of pastrami. Then use `while 'pastrami' in sandwich_orders:` to remove all occurrences of `'pastrami'`. Make sure no pastrami sandwiches are processed or added to `finished_sandwiches`.

### Exercise 7-10: Dream Vacation

Write a polling program that asks users: "If you could visit one place in the world, where would you go?" Store the results in a dictionary where the name is the key and the destination is the value. Include a prompt to continue or stop entering responses. Then print a complete summary of all the results.

---

## Quick Reference

| Operation | Code Pattern | Description |
| --- | --- | --- |
| Check if list is non-empty | `while my_list:` | Runs while the list still contains values |
| Move items between lists | `item = source.pop(); destination.append(item)` | Transfers data from one list to another |
| Remove all duplicates of one value | `while 'item' in my_list: my_list.remove('item')` | Deletes every matching value |
| Save user input in a dictionary | `responses[name] = answer` | Stores key-value data from repeated prompts |

---

## Related Topics

- [Lists](../../03_introducing_list/lists/lists.md)
- [Dictionaries](../../06_dictionaries/working_with_dictionaries/working_with_dictionaries.md)
- [Introducing While Loops](../introducing_while_loops/introducing_while_loops.md)

---

## Why This Matters

While loops with lists and dictionaries are important because they let programs handle dynamic and changing input. In real applications, users often keep entering data, data queues keep changing, and lists need to be updated during processing. This is a core pattern in automation, data entry, and user-driven systems.

---

## Additional Resources

- [Python Official Documentation: Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
- [Real Python: Python Lists](https://realpython.com/python-lists/)
- [Real Python: Python Dictionaries](https://realpython.com/python-dicts/)

---

## Last Modified

**October 3, 2026**

---

## Key Takeaways

- Use a `while` loop when you need to modify a list while processing it.
- `while my_list:` is a clean way to keep looping until the list is empty.
- `while 'value' in my_list:` is useful for removing all duplicate occurrences.
- `while` loops work well for collecting repeated user input into dictionaries.
- This pattern is common in real-world data processing and user-driven programs.
