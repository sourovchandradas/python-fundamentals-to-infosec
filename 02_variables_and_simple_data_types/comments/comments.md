# Comments in Python

## Overview

Comments are notes added directly into code to explain its purpose and logic. They are completely ignored by the Python interpreter during execution. Writing clean, meaningful comments is an essential habit for professional software development and team collaboration.

This guide covers:

* **Writing Comments** - using the `#` symbol for inline and block notes
* **Best Practices** - writing meaningful comments versus redundant notes
* **Collaborative Standards** - meeting developer expectations in professional repositories

---

## Table of Contents

1. [Writing Comments](#writing-comments)
2. [Best Practices](#best-practices)
3. [Exercises](#exercises)
4. [Quick Reference](#quick-reference)
5. [Related Topics](#related-topics)
6. [Additional Resources](#additional-resources)

---

## Writing Comments

### What is a Comment?

In Python, any text following the hash mark (`#`) on a line is treated as a comment and ignored at runtime.

```python
# Say hello to everyone.
print("Hello Python people!")

```

**Execution Behavior:**

* Line 1 (`# Say hello...`): Ignored by Python.
* Line 2 (`print(...)`): Executed, producing the output `Hello Python people!`.

---

## Best Practices

### What Makes a Good Comment?

The primary purpose of comments is to summarize your approach and explain **why** code was written in a certain way, not just **what** it does.

| Practice Type | Example Code | Reason |
| --- | --- | --- |
| **Redundant (Bad)** | `print("Hello")  # Prints Hello` | Restates the obvious code behavior. |
| **Meaningful (Good)** | `# Display greeting to authenticated users` | Explains the intent and context. |

### When to Write Comments

> **Developer Decision Rule:**
> If you had to evaluate multiple solutions before picking one, write a comment explaining your final choice. It is always easier to clean up unnecessary comments later than to document a sparsely commented codebase from scratch.

---

## Exercises

File naming convention: Use descriptive, lowercase names with underscores (e.g., `adding_comments.py`)

### Exercise 2-10: Adding Comments

1. Select two programs you have previously written.
2. Add at least one descriptive comment to each file.
3. If the code is too simple, include your name, the current date at the top, and one sentence explaining the script's core functionality.

**Example:**

```python
# Author: Developer
# Date: 2026-09-02
# Description: Demonstrates basic string formatting with f-strings.

name = "Ada"
print(f"Hello, {name}!")

```

---

## Quick Reference

| Concept | Syntax | Description |
| --- | --- | --- |
| Single-Line Comment | `# Comment text` | Ignored by Python execution |
| Inline Comment | `code  # Inline comment` | Explains specific line logic |
| Header Metadata | `# Author / Date / Objective` | Provides file context at the top |

---

## Related Topics

* ![Variables](variables/variables.md) - Storing values efficiently
* ![Strings](strings/strings.md) - Formatting text output

---

## Additional Resources

* [Python Official Docs: Comments](https://www.google.com/search?q=https://docs.python.org/3/tutorial/introduction.html%23first-steps-towards-programming)
* [PEP 8 Style Guide: Comments](https://www.google.com/search?q=https://peps.python.org/pep-0008/%23comments)

---

*Last Updated: 2026-09-02*

---
