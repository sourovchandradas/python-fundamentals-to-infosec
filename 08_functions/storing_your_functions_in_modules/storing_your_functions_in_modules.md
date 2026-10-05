# Storing Your Functions in Modules in Python

## Overview

Storing functions in separate files called **modules** allows you to separate the higher-level logic of your main program from the detailed implementation of individual tasks. An `import` statement tells Python to make the code inside a module available in your currently running program file.

Using modules offers several distinct advantages:

* **Clarity:** Keeps main program scripts concise and easy to follow.
* **Reusability:** Enables functions to be reused across multiple projects without duplicating code.
* **Shareability:** Allows you to share function libraries with other developers without exposing your entire application.
* **Library Ecosystem:** Provides access to the vast Python standard library and third-party packages.

---

## Table of Contents

1. [Importing an Entire Module](#importing-an-entire-module)
2. [Importing Specific Functions](#importing-specific-functions)
6. [Using `as` to Give a Function an Alias](#using-as-to-give-a-function-an-alias)
7. [Using `as` to Give a Module an Alias](#using-as-to-give-a-module-an-alias)
8. [Importing All Functions in a Module](#importing-all-functions-in-a-module)
9. [Styling Functions (PEP 8 Guidelines)](#styling-functions-pep-8-guidelines)
10. [Common Mistakes and Errors](#common-mistakes-and-errors)
11. [Exercises](#exercises)
12. [Quick Reference](#quick-reference)
13. [Related Topics](#related-topics)
14. [Why This Matters](#why-this-matters)
15. [Additional Resources](#additional-resources)

---

## Importing an Entire Module

A **module** is simply a file ending in `.py` containing Python code. To import an entire module, both the module file and your main program file should reside in the same directory (or within Python's module search path).

### Step 1: Create the Module File (`pizza.py`)

```python
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
```

### Step 2: Import and Call Functions (`making_pizzas.py`)

To use functions from an imported module, use **dot notation**: `module_name.function_name()`.

```python
import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

### Output

```text
Making a 16-inch pizza with the following toppings:
- pepperoni

Making a 12-inch pizza with the following toppings:
- mushrooms
- green peppers
- extra cheese
```

### General Syntax

```python
import module_name

module_name.function_name()
```

---

## Importing Specific Functions

If you only need specific functions from a module, you can import them directly. This allows you to call the function by its name without using dot notation.

### Syntax

```python
from module_name import function_name
```

To import multiple functions, separate their names with commas:

```python
from module_name import function_0, function_1, function_2
```

### Implementation Example

```python
from pizza import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

---

## Using `as` to Give a Function an Alias

If an imported function's name conflicts with an existing name in your program, or if the function name is long, you can give it a short, unique **alias** (a nickname) during import using the `as` keyword.

### Syntax

```python
from module_name import function_name as f
```

### Implementation Example

```python
from pizza import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')
```

---

## Using `as` to Give a Module an Alias

You can also assign an alias to an entire module. Giving a module a concise alias (such as `p` for `pizza`) makes calling functions quicker and redirects attention to the descriptive function names.

### Syntax

```python
import module_name as mn
```

### Implementation Example

```python
import pizza as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

---

## Importing All Functions in a Module

You can tell Python to import every function from a module into your local namespace using the asterisk (`*`) operator.

### Syntax

```python
from module_name import *
```

### Implementation Example

```python
from pizza import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

> **Warning:** Avoid using `from module_name import *` in larger projects or with modules you did not write. If the imported module contains function or variable names that match existing names in your project, Python will silently overwrite your local definitions without warning.

---

## Styling Functions (PEP 8 Guidelines)

Adhering to standard Python styling guidelines makes your code clean, readable, and professional.

### 1. Naming Conventions

* Function and module names should use **lowercase letters** with **underscores** separating words (`snake_case`).
* Names should be descriptive of the action performed.

### 2. Docstring Formatting

* Every function must include a docstring formatted comment immediately following the `def` line.
* Docstrings should concisely explain what the function does, its required arguments, and its return values.

```python
def calculate_total(price, tax_rate):
    """Calculate and return the final price including tax."""
    return price * (1 + tax_rate)
```

### 3. Parameter Defaults and Keyword Arguments

Do **not** use spaces around the `=` sign when specifying default parameter values or passing keyword arguments:

```python
# Correct
def greet_user(username, greeting='Hello'):
    ...

greet_user('hannah', greeting='Welcome')

# Incorrect
def greet_user(username, greeting = 'Hello'):
    ...
```

### 4. Line Length and Multi-Line Parameters

* PEP 8 recommends limiting code lines to **79 characters**.
* If a function's parameters exceed this length, press Enter after the opening parenthesis. Indent additional parameter lines by two tabs (8 spaces) to distinguish parameters from the function body:

```python
def function_name(
        parameter_0, parameter_1, parameter_2,
        parameter_3, parameter_4, parameter_5):
    """Concise docstring explaining the function."""
    print("Function body goes here.")
```

### 5. Spacing and Imports Placement

* Separate function definitions in a file or module using **two blank lines**.
* All `import` statements must be placed at the **top of the file** (directly below any module-level docstrings or header comments).

---

## Common Mistakes and Errors

### Mistake 1: Module Naming Collisions

Naming a script with the same name as a built-in Python module or standard library (e.g., naming your file `math.py` or `random.py`) causes local import shadow bugs.

```python
# File named math.py attempting to import built-in math module
import math  # Error: Tries to import itself recursively!
```

**Solution:** Always give local modules custom, unique names (e.g., `my_math_utils.py`).

### Mistake 2: `ModuleNotFoundError`

Occurs when Python cannot locate the specified module file.

```text
ModuleNotFoundError: No module named 'pizza'
```

**Solution:** Ensure `pizza.py` is located in the exact same directory as the script calling `import pizza`.

### Mistake 3: Unintentional Function Overwriting via Wildcard Import

Using `from module import *` replaces local functions if a imported function shares the exact same name.

```python
def make_pizza():
    print("Custom local function")

from pizza import *  # Overwrites local make_pizza() with pizza.py's make_pizza()
```

---

## Exercises

File naming convention: Use descriptive, lowercase names with underscores (e.g., `8-15.printing_models.py`).

### Exercise 8-15: Printing Models

Put the functions for the `print_models.py` example into a separate file called `printing_functions.py`. Write an `import` statement at the top of `print_models.py`, and modify the file to use the imported functions.

**Solution:** [Exercise 8-15: Printing Models](labs/8-15.printing_models.py)

### Exercise 8-16: Imports

Using a program you wrote that has one function in it, store that function in a separate file. Import the function into your main program file, and call the function using each of these five approaches:

1. `import module_name`
2. `from module_name import function_name`
3. `from module_name import function_name as fn`
4. `import module_name as mn`
5. `from module_name import *`

**Solution:** [Exercise 8-16: Imports](labs/8-16.imports.py)

### Exercise 8-17: Styling Functions

Choose any three programs you wrote for this chapter, and ensure they strictly follow the styling guidelines described in this section (lowercase module/function names, docstrings, no spaces around parameter `=`, max line length 79 characters, two blank lines between functions).

**Solution:** [Exercise 8-17: Styling Functions](labs/8-17.styling_functions.py)

---

## Quick Reference

| Import Strategy | Syntax | Function Calling Syntax | Primary Use Case |
| --- | --- | --- | --- |
| Entire Module | `import module_name` | `module_name.func()` | Clear source origin, avoids name collisions. |
| Specific Function | `from module_name import func` | `func()` | Concise calls when importing few specific functions. |
| Function Alias | `from module_name import func as fn` | `fn()` | Resolves local function name conflicts. |
| Module Alias | `import module_name as mn` | `mn.func()` | Shortens long module namespace prefixes. |
| All Functions (Wildcard) | `from module_name import *` | `func()` | Quick interactive tests; avoid in production code. |

---

## Related Topics

* [Defining a Function](../defining_a_function/defining_a_function.md)
* [Passing Arguments](../passing_arguments/passing_arguments.md)
* [Return Values](../return_values/return_values.md)
* [Python Standard Library](../../09_classes/standard_library.md)

---

## Why This Matters

Modules are the foundation of code organization in professional software development. By breaking complex applications down into discrete modules, code becomes easier to read, test, maintain, and share. Mastering `import` mechanics prepares you to leverage Python's vast package ecosystem, including frameworks like Django, Flask, Pandas, and NumPy.

---

## Additional Resources

* [Python Documentation: Modules](https://docs.python.org/3/tutorial/modules.html)
* [PEP 8: Style Guide for Python Code](https://www.google.com/search?q=https://peps.python.org/pep-0008/)

---

*Last Updated : October 6, 2026*

---

## Key Takeaways

* Store helper functions in separate `.py` module files to keep main programs clean.
* Import entire modules with `import module_name` and access functions via dot notation (`module_name.function()`).
* Import individual functions directly using `from module_name import function_name`.
* Assign aliases with `as` to shorten long module names or resolve naming conflicts.
* Avoid `from module_name import *` in production scripts to prevent variable shadowing and unexpected overwrites.
* Place all `import` statements at the top of your Python files.
