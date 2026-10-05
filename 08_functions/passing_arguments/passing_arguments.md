# Passing Arguments in Python

## Overview

Because a function definition can have multiple parameters, a function call may require multiple arguments. Python offers several ways to pass arguments to your functions: positional arguments (matched in the order written), keyword arguments (where each argument consists of a parameter name and value), default values, and passing collections like lists and dictionaries.

This guide covers:

* **Positional arguments** - matching arguments based on parameter order
* **Keyword arguments** - explicitly pairing argument names with values
* **Default values** - defining fallback values for parameters
* **Equivalent function calls** - mixing calling styles for flexibility
* **Common mistakes and errors** - preventing order mix-ups and reading tracebacks

---

## Table of Contents

1. [Positional Arguments](#positional-arguments)
2. [Keyword Arguments](#keyword-arguments)
3. [Default Values](#default-values)
4. [Equivalent Function Calls](#equivalent-function-calls)
5. [Common Mistakes and Errors](#common-mistakes-and-errors)
6. [Exercises](#exercises)
7. [Quick Reference](#quick-reference)
8. [Related Topics](#related-topics)
9. [Why This Matters](#why-this-matters)
10. [Additional Resources](#additional-resources)

---

## Positional Arguments

### What are Positional Arguments?

When calling a function, Python must match each argument in the function call with a parameter in the function definition. The simplest way to do this is based on the order of the arguments provided. Values matched this way are called **positional arguments**.

### Syntax and Implementation

```python
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# Calling with positional arguments
describe_pet('hamster', 'harry')

```

### Output

```python
I have a hamster.
My hamster's name is Harry.

```

### Multiple Function Calls

You can call a function as many times as needed. Calling a function multiple times is an efficient way to work: the logic is written once inside the function, and any new item can be processed with a single line of code.

```python
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

```

### Output

```python
I have a hamster.
My hamster's name is Harry.

I have a dog.
My dog's name is Willie.

```

### Order Matters in Positional Arguments

You can get unexpected results if you mix up the order of arguments when using positional arguments.

```python
# Order mixed up: pet_name first, animal_type second
describe_pet('harry', 'hamster')

```

### Output

```python
I have a harry.
My harry's name is Hamster.

```

---

## Keyword Arguments

### What are Keyword Arguments?

A **keyword argument** is a name-value pair that you pass to a function. You directly associate the parameter name and the value within the argument call, eliminating positional confusion.

### Implementation Example

```python
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# Passing keyword arguments
describe_pet(animal_type='hamster', pet_name='harry')

```

### Output

```python
I have a hamster.
My hamster's name is Harry.

```

### Order Independence

The order of keyword arguments does not matter because Python knows explicitly where each value should go based on the parameter names.

```python
# Both of these function calls are equivalent:
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')

```

> **Note:** When using keyword arguments, be sure to use the exact names of the parameters as defined in the function header.

---

## Default Values

### Defining Default Values

When writing a function, you can define a default value for each parameter. If an argument for a parameter is provided in the function call, Python uses the argument value. If omitted, Python uses the parameter's default value.

### Parameter Placement Rule

When using default values, any parameter with a default value **must be listed after** all parameters that do not have default values. This allows Python to continue interpreting positional arguments correctly.

### Implementation Example

```python
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# Calling with default animal_type ('dog')
describe_pet('willie')

# Overriding the default value
describe_pet(pet_name='harry', animal_type='hamster')

```

### Output

```python
I have a dog.
My dog's name is Willie.

I have a hamster.
My hamster's name is Harry.

```

---

## Equivalent Function Calls

### Combining Argument Styles

Because positional arguments, keyword arguments, and default values can all be used together, you often have several equivalent ways to call a function.

Given the function definition:

```python
def describe_pet(pet_name, animal_type='dog'):

```

### Equivalent Function Call Examples

```python
# Describing a dog named Willie:
describe_pet('willie')
describe_pet(pet_name='willie')

# Describing a hamster named Harry:
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')

```

All of these calls produce identical, expected outputs. Use the calling style that makes your code easiest to read and maintain.

---

## Common Mistakes and Errors

### Mistake 1: Misplacing Parameters with Default Values

Defining default parameters before required parameters causes a syntax error.

```python
# Incorrect: Default parameter listed first
def describe_pet(animal_type='dog', pet_name):
    print(f"{pet_name} is a {animal_type}")

```

**Correction:** Place required parameters first, followed by default parameters:

```python
def describe_pet(pet_name, animal_type='dog'):
    print(f"{pet_name} is a {animal_type}")

```

### Mistake 2: Missing Required Positional Arguments

Calling a function without providing required arguments produces a `TypeError`.

```python
describe_pet()

```

### Traceback Error Analysis

```python
Traceback (most recent call last):
  File "pets.py", line 6, in <module>
    describe_pet()
TypeError: describe_pet() missing 2 required positional arguments: 'animal_type' and 'pet_name'

```

* **File and Line Number:** Points directly to where the improper call occurred (`line 6`).
* **Offending Code:** Displays the exact call (`describe_pet()`).
* **Error Description:** Explains that 2 positional arguments are missing and lists their parameter names (`'animal_type'` and `'pet_name'`).

### Mistake 3: Misspelling Keyword Argument Names

Passing a keyword argument name that does not match the parameter in the definition header throws an unexpected keyword argument error.

```python
# Parameter is 'pet_name', but passed 'name'
describe_pet(name='harry', animal_type='hamster')

```

---

## Exercises

File naming convention: Use descriptive, lowercase names with underscores (for example, `make_shirt.py`).

### Exercise 8-3: T-Shirt

Write a function called `make_shirt()` that accepts a `size` and the `text` of a message that should be printed on the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it.

Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.

### Exercise 8-4: Large Shirts

Modify the `make_shirt()` function so that shirts are large by default with a message that reads `"I love Python"`. Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.

### Exercise 8-5: Cities

Write a function called `describe_city()` that accepts the name of a city and its country. The function should print a simple sentence, such as `"Reykjavik is in Iceland."` Give the parameter for the country a default value. Call your function for three different cities, at least one of which is not in the default country.

---

## Quick Reference

| Concept | Syntax / Pattern | Description |
| --- | --- | --- |
| Positional Arguments | `describe_pet('hamster', 'harry')` | Binds values to parameters in sequential order |
| Keyword Arguments | `describe_pet(pet_name='harry', animal_type='hamster')` | Binds values using explicit parameter names; order independent |
| Default Value | `def describe_pet(pet_name, animal_type='dog'):` | Provides a fallback value if argument is omitted |
| Default Placement Rule | Non-default parameters must precede default parameters | Preserves positional argument matching logic |
| Unmatched Argument Error | `TypeError: missing required positional arguments` | Raised when mandatory parameter values are omitted |

---

## Related Topics

* [Defining a Function](../defining_a_function/defining_a_function.md)
* [Introducing While Loops](../../07_user_input_and_while_loops/introducing_while_loops/introducing_while_loops.md)
* [Working with Dictionaries](../../06_dictionaries/working_with_dictionaries/working_with_dictionaries.md)

---

## Why This Matters

Understanding argument passing mechanisms empowers you to write adaptable and clean code interfaces. Positional arguments keep simple calls brief, keyword arguments clarify intent in complex calls, and default values minimize repetition. Mastered together, these patterns reduce call site errors and make functions easier to extend over time.

---

## Additional Resources

* [Python Official Documentation: More on Defining Functions](https://docs.python.org/3/tutorial/controlflow.html)
* [Real Python: Python Function Arguments](https://realpython.com/defining-your-own-python-function/)

---

*Last Updated : October 5, 2026*

---

## Key Takeaways

* Positional arguments rely on the order of arguments matching parameter definitions.
* Keyword arguments explicitly link parameter names and values, making calls order-independent.
* Parameters with default values must always follow required parameters without defaults.
* Multiple equivalent calling styles can be created by combining positional, keyword, and default values.
* Python tracebacks specify exact missing argument names, simplifying error resolution.
