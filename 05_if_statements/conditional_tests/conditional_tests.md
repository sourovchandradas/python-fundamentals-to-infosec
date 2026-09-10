# Conditional Tests in Python

## Overview

At the heart of every `if` statement is an expression that can be evaluated as either `True` or `False`. This expression is called a **conditional test**. Python uses these Boolean values to decide whether the code inside an `if` statement should be executed:

- If a conditional test evaluates to **`True`**, Python executes the code following the `if` statement.
- If the test evaluates to **`False`**, Python ignores the code following the `if` statement.
- Architectural Flow: Conditional Test Execution

                                         +---------------------------------------+
                                         |       Evaluate Expression             |
                                         +---------------------------------------+
                                                             |
                                                             v
                                                 /-----------------------\
                                                /     Is Test Result      \
                                               <      True or False?      >
                                                \                         /
                                                 \-----------------------/
                                                     /               \
                                           True     /                 \     False
                                                   /                   \
                                                  v                     v
                                    +-----------------------+   +-----------------------+
                                    | Execute Indented Block|   | Bypasses/Skips Block  |
                                    +-----------------------+   +-----------------------+
                                                   |                     |
                                                   +----------+----------+
                                                              |
                                                              v
                                                  +----------------------+
                                                  | Continue Execution   |
                                                  +----------------------+

  
This guide covers:
- **Checking for Equality & Case Sensitivity** - comparing values with `==` and normalizing strings with `.lower()`
- **Checking for Inequality & Numerical Comparisons** - using `!=`, `<`, `<=`, `>`, and `>=`
- **Checking Multiple Conditions** - combining expressions using `and` and `or`
- **Checking Membership** - testing for presence or absence in lists using `in` and `not in`
- **Boolean Expressions** - tracking program state using Boolean flags (`True` / `False`)

---

## Table of Contents

1. [Checking for Equality](#checking-for-equality)
2. [Ignoring Case When Checking for Equality](#ignoring-case-when-checking-for-equality)
3. [Checking for Inequality](#checking-for-inequality)
4. [Numerical Comparisons](#numerical-comparisons)
5. [Checking Multiple Conditions](#checking-multiple-conditions)
6. [Checking Whether a Value Is in a List](#checking-whether-a-value-is-in-a-list)
7. [Checking Whether a Value Is Not in a List](#checking-whether-a-value-is-not-in-a-list)
8. [Boolean Expressions](#boolean-expressions)
9. [Exercises](#exercises)
10. [Quick Reference](#quick-reference)

---

## Checking for Equality

Most conditional tests compare the current value of a variable to a specific value of interest. The simplest test checks whether the value of a variable is equal to the value of interest using the double equal sign (`==`).

### Variable Assignment vs. Equality Testing

- **Single Equal Sign (`=`)**: A statement that assigns a value (e.g., "Set the value of `car` equal to `'bmw'`").
- **Double Equal Sign (`==`)**: A question that compares values (e.g., "Is the value of `car` equal to `'bmw'`?"). Returns `True` if values on the left and right match, and `False` if they do not match.

```python
car = 'bmw'
print(car == 'bmw')
```

**Output:**
```
True
```

When the value of `car` is anything other than `'bmw'`, the equality test returns `False`:

```python
car = 'audi'
print(car == 'bmw')
```

**Output:**
```
False
```

> **Note:** Most programming languages use single and double equal signs in this exact manner.

---

## Ignoring Case When Checking for Equality

Testing for equality is **case sensitive** in Python. Values with different capitalization are not considered equal:

```python
car = 'Audi'
print(car == 'audi')
```

**Output:**
```
False
```

If case matters for your logic, this behavior is advantageous. However, if case does not matter and you simply want to test the value of a variable, you can convert the variable's value to lowercase using `.lower()` before performing the comparison:

```python
car = 'Audi'
print(car.lower() == 'audi')
print(car)
```

**Output:**
```
True
Audi
```

### Key Behaviors

1. The test `car.lower() == 'audi'` returns `True` no matter how the original string `'Audi'` is capitalized.
2. Calling `.lower()` does **not** change the original value stored in `car`.

### Real-World Application: Website Usernames

Websites enforce data validation rules using this exact pattern to ensure unique usernames:

* When a user submits a new username (e.g., `'John'`), the site converts it to lowercase and compares it against lowercase versions of all existing usernames.
* If `'john'` already exists in the system, any capitalized variation like `'John'` or `'JOHN'` will be rejected to prevent duplicate registrations.

---

## Checking for Inequality

When you want to determine whether two values are **not equal**, combine an exclamation point and an equal sign (`!=`). The exclamation point (`!`) represents **not**, as it does across many programming languages.

### Example Script: `toppings.py`

```python
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")
```

**Output:**

```text
Hold the anchovies!
```

**Execution Step:**

1. The line `if requested_topping != 'anchovies':` compares the variable `'mushrooms'` to `'anchovies'`.
2. Because they do not match, the test evaluates to `True`, and Python executes the indented `print()` statement.
3. If the values matched (`requested_topping = 'anchovies'`), the test would return `False`, and Python would skip the code block.

> **Tip:** Most conditional expressions test for equality, but testing for inequality is often more efficient when filtering out unwanted items.

---

## Numerical Comparisons

Testing numerical values in Python supports direct equality, inequality, and standard mathematical comparison operators.

### Equality and Inequality Tests

Checking if a person is 18 years old:

```python
age = 18
print(age == 18)
```

**Output:**
```
True
```
Testing if a numerical answer is incorrect:


```python
answer = 20

if answer != 94:
    print("That is not the correct answer. Please try again!")
```

**Output:**

```text
That is not the correct answer. Please try again!
```

Because `answer` (`17`) is not equal to `42`, the test passes (`True`) and the indented block executes.

### Mathematical Comparisons

Mathematical comparison operators can detect exact threshold conditions inside `if` statements:

```python
age = 19
print(age < 21)

print(age <= 21)

print(age > 21)

print(age >= 21)
```

**Output:**
```
True
True
False
False
```
---

## Checking Multiple Conditions

You can check multiple conditions simultaneously using the logical keywords `and` and `or`.

### Using `and` to Check Multiple Conditions

To require two conditions to be `True` simultaneously, combine them with `and`.

* Evaluates to **`True`** only if **each individual test passes**.
* Evaluates to **`False`** if **either test fails or if both tests fail**.

```python
age_0 = 22
age_1 = 18
print (age_0 >= 21 and age_1 >= 21)

age_1 = 22
age_0 >= 21 and age_1 >= 21
```

**Output:**
```
False
True
```

**Step-by-Step Logic:**

1. First test: `age_0` (`22`) passes `>= 21`, but `age_1` (`18`) fails `>= 21`. The overall expression evaluates to `False`.
2. Second test: `age_1` is updated to `22`. Now both sub-tests pass, evaluating the overall expression to `True`.

> **Readability Tip:** You can use optional parentheses around individual tests to improve clarity:
> `(age_0 >= 21) and (age_1 >= 21)`

### Using `or` to Check Multiple Conditions

The `or` keyword passes when **either or both** individual tests pass.

* Evaluates to **`True`** if at least one condition passes.
* Evaluates to **`False`** **only when both individual tests fail**.

```python
age_0 = 22
age_1 = 18
print(age_0 >= 21 or age_1 >= 21)

age_0 = 18
print(age_0 >= 21 or age_1 >= 21)
```

**Output:**
```
True
False
```
**Step-by-Step Logic:**

1. First test: `age_0` (`22`) passes `>= 21`, so the overall expression immediately evaluates to `True`.
2. Second test: `age_0` is reduced to `18`. Now both individual tests fail, so the overall expression evaluates to `False`.

---

## Checking Whether a Value Is in a List

Checking whether a list contains a specific value before taking action is common in applications:

* Checking if a new username exists in a list of current usernames before finishing registration.
* Checking if a location exists in a list of known locations in a mapping project.

To test for item existence in a list, use the keyword **`in`**:

```python
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)
'pepperoni' in requested_toppings
```

**Output:**
```
True
False
```

This technique allows you to define a list of essential values and easily verify whether a candidate value matches any item in the list.

---

## Checking Whether a Value Is Not in a List

To test if a value does **not** appear in a list, combine the keywords **`not in`**.

### Example Script: `banned_users.py`

Checking if a user is banned before allowing them to post a forum comment:

```python
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")
```

**Output:**

```text
Marie, you can post a response if you wish.
```

Because `'marie'` is not in `banned_users`, the condition evaluates to `True` and the indented message is printed.

---

## Boolean Expressions

A **Boolean expression** is simply another term for a conditional test. A Boolean value evaluates strictly to either **`True`** or **`False`**.

Boolean values are widely used as **flags** to track state or permissions within a program:

```python
game_active = True
can_edit = False
```

Boolean flags provide an efficient way to monitor program states (such as whether a game loop is running) or user authorization privileges (such as whether a user can edit web content).

---

## Exercises

File naming standard: Use descriptive, lowercase snake_case names (e.g., `conditional_tests.py`).

### Exercise 5-1: Conditional Tests

Write a series of conditional tests. Print a statement describing each test and your prediction for the results of each test.

Your code should follow this structure:

```python
car = 'subaru'
print("Is car == 'mercedes-benz'? I predict True.")
print(car == 'mercedes-benz')

print("\nIs car == 'nissan'? I predict False.")
print(car == 'nissan')

```

**Requirements:**

* Look closely at your results and understand why each line evaluates to `True` or `False`.
* Create at least 10 tests (at least 5 evaluating to `True` and 5 evaluating to `False`).

### Exercise 5-2: More Conditional Tests

You don't have to limit your tests to 10. Write more tests and add them to `conditional_tests.py`. Have at least one `True` and one `False` result for each of the following:

1. **Tests for equality and inequality with strings**
2. **Tests using the `lower()` function**
3. **Numerical tests** involving:
* Equality (`==`) and inequality (`!=`)
* Greater than (`>`) and less than (`<`)
* Greater than or equal to (`>=`) and less than or equal to (`<=`)


4. **Tests using logical keywords**:
* The `and` keyword
* The `or` keyword


5. **Test whether an item is in a list** using `in`
6. **Test whether an item is not in a list** using `not in`

---

## Quick Reference

| Operator / Keyword | Description | Code Example | Evaluates To |
| --- | --- | --- | --- |
| `==` | Equality test | `'bmw' == 'bmw'` | `True` |
| `!=` | Inequality test | `17 != 42` | `True` |
| `.lower()` | Case-insensitive matching | `'Audi'.lower() == 'audi'` | `True` |
| `<`, `<=` | Numerical less than / less than or equal | `19 < 21` | `True` |
| `>`, `>=` | Numerical greater than / greater than or equal | `19 > 21` | `False` |
| `and` | Logical AND (all conditions must pass) | `(22 >= 21) and (18 >= 21)` | `False` |
| `or` | Logical OR (at least one condition passes) | `(22 >= 21) or (18 >= 21)` | `True` |
| `in` | Membership presence check | `'mushrooms' in toppings` | `True` |
| `not in` | Membership absence check | `'marie' not in banned_users` | `True` |

---

## Related Topics

* [Making Numerical Lists](../../04_working_with_lists/making_numerical_lists/making_numerical_lists.md) - Using range() and working with numbers in loops
* [Tuples](../tuples/tuples.md) - Immutable sequence structures and membership testing
* [If Statements](../if_statements/if_statements.md) - Implementing `if-else` and `if-elif-else` control flow blocks

---

## Additional Resources

* [Python Documentation: Truth Value Testing](https://www.google.com/search?q=https://docs.python.org/3/library/stdtypes.html%23truth-value-testing)
* [Python Documentation: Comparisons](https://www.google.com/search?q=https://docs.python.org/3/library/stdtypes.html%23comparisons)
* [Real Python: Python Conditional Statements](https://www.google.com/search?q=https://realpython.com/python-conditional-statements/)

---

*Last Updated: 10th September, 2026*
