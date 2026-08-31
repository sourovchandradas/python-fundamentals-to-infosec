# Strings & String Manipulations

---

## 1. What is a String?

* **Definition:** A string is simply a series of characters.
* **Syntax:** Anything inside single (`'...'`) or double (`"..."`) quotes is considered a string in Python.
* **Quote Flexibility:** Using different quote types allows incorporating quotation marks and apostrophes inside strings without causing syntax errors.

**Code Example:**
```python
string_1 = "This is a string."
string_2 = 'This is also a string.'
quote_1 = 'I told my friend, "Python is my favorite language!"'
quote_2 = "One of Python's strengths is its diverse community."

```

---

## 2. Changing Case in a String with Methods

* **Method Definition:** A method is an action that Python performs on a piece of data.
* **Syntax Notation:** The dot (`.`) after a variable tells Python to make the method act on that variable. Parentheses `()` follow method names to pass arguments if required.
* **Methods Overview:**
* `.title()`: Capitalizes the first letter of every word (Title Case). Useful for name normalization.
* `.upper()`: Converts all characters in the string to uppercase.
* `.lower()`: Converts all characters in the string to lowercase.



**Code Example:**

```python
name = "information technology"
print(name.title())
print(name.upper())
print(name.lower())

```

**Output:**

```text
Information Technology
INFORMATION TECHNOLOGY
information technology

```

> **Practical Use Case (Data Sanitization):** User input often varies in capitalization (e.g., `'Information'`, `'INFORMATION'`, `'information'`). Using `.lower()` before storing or comparing data ensures consistency across system databases and login checks.

---

## 3. Combining or Concatenating Strings

* **Concatenation:** Combining two or more strings using the plus (`+`) operator.
* **Modern Standard Note:** While Python uses `+` for concatenation, Python 3.6+ **f-strings** (`f"{var}"`) are preferred in industry standards for better readability and performance.
* **Application:** Useful for stitching together data stored in separate variables into complete messages.

**Code Example:**

```python
first_name = "information"
last_name = "technology"
full_name = first_name + " " + last_name
message = "Hello, " + full_name.title() + "!"
print(message)

```

**Output:**

```text
Hello, Information Technology!

```

---

## 4. Adding Whitespace to Strings with Tabs or Newlines

* **Whitespace:** Refers to non-printing characters such as spaces, tabs, and line break symbols used to organize output clearly.
* **Escape Sequences:**
* `\t`: Adds a tab space (indentation).
* `\n`: Inserts a newline break.
* `\n\t`: Moves text to a new line and indents it with a tab.



**Code Example:**

```python
print("Languages:\n\tPython\n\tC\n\tJavaScript")

```

**Output:**

```text
Languages:
    Python
    C
    JavaScript

```

---

## 5. Stripping Whitespace

* **Concept:** To Python, `'python'` and `'python '` are two distinct strings due to trailing whitespace.
* **Application:** Essential for cleaning up user inputs (e.g., usernames, passwords, form fields) before evaluation or database storage.
* **Methods Overview:**
* `.rstrip()`: Removes trailing whitespace (right side).
* `.lstrip()`: Removes leading whitespace (left side).
* `.strip()`: Removes whitespace from both sides simultaneously.


* **Temporary vs. Permanent Change:**
* Calling a stripping method returns the modified string value temporarily.
* To make the change permanent, reassign the stripped value back to the variable.



**Code Example:**

```python
favorite_language = "  python  "

# Temporary removal
print("Right stripped:", favorite_language.rstrip())
print("Left stripped:", favorite_language.lstrip())
print("Both stripped:", favorite_language.strip())

# Permanent removal via reassignment
favorite_language = favorite_language.strip()
print("Permanently cleaned:", favorite_language)

```

**Output:**

```text
Right stripped: '  python'
Left stripped: 'python  '
Both stripped: 'python'
Permanently cleaned: 'python'

```

---

## 6. Avoiding Syntax Errors with Strings

* **Syntax Error:** Occurs when the Python interpreter cannot recognize a section of code as valid Python syntax.
* **Common Cause:** Improper quote nesting (e.g., using an apostrophe inside single quotes).

**Incorrect Code Example:**

```python
message = 'One of Python's strengths is its diverse community.'
print(message)

```

**Traceback Output:**

```text
File "apostrophe.py", line 1
  message = 'One of Python's strengths is its diverse community.'
                          ^
SyntaxError: invalid syntax

```

* **Fix:** Wrap strings containing single quotes/apostrophes in double quotes, or use proper escape characters (`\'`).

---

## 7. Try It Yourself Exercises

*File naming standard: Use descriptive, lowercase snake_case names (e.g., `personal_message.py`).*

* **2-3. Personal Message:** Store a person's name in a variable and print a personalized message (e.g., *"Hello Eric, would you like to learn some Python today?"*).
* **2-4. Name Cases:** Store a person's name in a variable, then print that name in lowercase, uppercase, and titlecase.
* **2-5. Famous Quote:** Find a quote from a famous person. Print the quote and author name, including quotation marks in the output.
* **2-6. Famous Quote 2:** Repeat Exercise 2-5, but store the author's name in a variable `famous_person` and the quote in a variable `message`. Print the message.
* **2-7. Stripping Names:** Store a person's name with leading/trailing whitespace using `\t` and `\n`. Print the name with whitespace, then print it using `.lstrip()`, `.rstrip()`, and `.strip()`.
