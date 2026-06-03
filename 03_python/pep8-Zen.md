# PEP 8 and The Zen of Python

Sources:
- PEP 8: https://peps.python.org/pep-0008/
- PEP 20: https://peps.python.org/pep-0020/

## Quick Summary

PEP 8 is Python's style guide. It explains how Python code should be
formatted so that other developers can read it easily.

PEP 20, also called The Zen of Python, is Python's design philosophy. It
explains how Python code should feel: clear, simple, explicit, and readable.

Together, they teach one big lesson:

> Write code for humans first, and for the computer second.

The computer only needs valid syntax. Developers need code that is easy to
read, debug, review, test, and improve.

## PEP 8 vs The Zen of Python

| Topic | PEP 8 | The Zen of Python |
| --- | --- | --- |
| Main purpose | Coding style rules | Coding philosophy |
| Focus | Formatting, naming, imports, comments | Simplicity, clarity, explicit design |
| Example question | "How should I name this function?" | "Is this solution clear enough?" |
| Best use | Daily coding and code review | Design decisions and problem solving |

PEP 8 gives the practical habits. The Zen gives the judgment behind those
habits.

## Why These Rules Matter

Clean Python code matters because most professional work is not writing brand
new code. Most work is reading, fixing, extending, and reviewing existing code.

Good style helps with:

- Faster debugging
- Easier teamwork
- Cleaner code reviews
- Fewer misunderstandings
- Better long-term maintenance
- More professional project structure

If code is clever but hard to explain, it is usually not professional code.

## The Most Important Rule

Consistency matters more than personal preference.

PEP 8 explains that consistency with a project is more important than blindly
following every rule. If a project already uses a specific style, follow the
project style unless there is a good reason to improve it.

Use this priority:

1. Make the code correct.
2. Make the code readable.
3. Make the code consistent with the project.
4. Make the code shorter only when it stays clear.

## Code Layout

### Indentation

Use 4 spaces per indentation level.

Good:

```python
def greet_user(name):
    if name:
        print(f"Hello, {name}")
```

Avoid mixing tabs and spaces. Python can raise indentation errors when both are
used together.

### Line Length

PEP 8 recommends short lines. The classic limit is 79 characters for code and
72 characters for comments or docstrings. Many modern teams use up to 88 or 99
characters, but the goal is the same: keep code readable without horizontal
scrolling.

Bad:

```python
total = calculate_final_price(product_price, customer_discount, shipping_fee, sales_tax, coupon_value)
```

Better:

```python
total = calculate_final_price(
    product_price,
    customer_discount,
    shipping_fee,
    sales_tax,
    coupon_value,
)
```

### Blank Lines

Use blank lines to separate ideas.

- Two blank lines before top-level functions and classes
- One blank line between methods inside a class
- Small blank spaces inside a function when the logic has separate sections

Good:

```python
class Invoice:
    def __init__(self, amount):
        self.amount = amount

    def total(self):
        return self.amount


def print_invoice(invoice):
    print(invoice.total())
```

## Imports

Imports should be placed at the top of the file after the module docstring.

Use this order:

1. Standard library imports
2. Third-party imports
3. Local project imports

Good:

```python
import os
from pathlib import Path

import requests

from app.users import get_user
```

Avoid:

```python
import os, sys
from math import *
```

Why?

- One import per line is easier to scan.
- Grouped imports show where code dependencies come from.
- Wildcard imports hide which names are available.

## Whitespace

Whitespace should make code easier to read, not noisier.

Good:

```python
total = price + tax
items = [1, 2, 3]
user = get_user(user_id)
```

Avoid:

```python
total=price+tax
items = [ 1, 2, 3 ]
user = get_user (user_id)
```

Common whitespace habits:

- Use one space around assignment and comparison operators.
- Do not add extra spaces inside parentheses, brackets, or braces.
- Do not align assignments with many spaces.
- Remove trailing whitespace.

Bad:

```python
name        = "Ali"
age         = 21
profession  = "Developer"
```

Good:

```python
name = "Ali"
age = 21
profession = "Developer"
```

## Naming Rules

Names should describe meaning, not just data type.

| Item | Style | Example |
| --- | --- | --- |
| Module | lowercase | `payment.py` |
| Package | lowercase | `users` |
| Function | snake_case | `calculate_total()` |
| Variable | snake_case | `user_name` |
| Class | CapWords | `PaymentGateway` |
| Constant | UPPER_CASE | `MAX_RETRIES` |
| Exception | CapWords + Error | `PaymentError` |
| Internal name | leading underscore | `_cache` |

Poor names:

```python
def calc(x, y):
    return x * y
```

Better names:

```python
def calculate_total(price, quantity):
    return price * quantity
```

A professional name answers:

- What is this?
- Why does it exist?
- What does the function return or change?

## Functions

A good function should do one clear job.

Good:

```python
def is_adult(age):
    return age >= 18
```

Too much responsibility:

```python
def process_user(user):
    validate_user(user)
    save_user(user)
    send_welcome_email(user)
    create_audit_log(user)
```

Better:

```python
def register_user(user):
    validate_user(user)
    save_user(user)
    send_welcome_email(user)
    create_audit_log(user)
```

The second version still performs several steps, but the function name explains
the larger action clearly.

## Comments and Docstrings

Comments should explain why something exists, not repeat what the code already
says.

Bad:

```python
# Add one to count
count += 1
```

Better:

```python
# The API uses page numbers starting from 1.
page_number = index + 1
```

Use docstrings for public modules, classes, and functions.

Good:

```python
def calculate_discount(price, discount_percent):
    """Return the discounted price for a percentage discount."""
    discount = price * discount_percent / 100
    return price - discount
```

Keep comments updated. An old comment is worse than no comment because it gives
the reader wrong information with confidence.

## Programming Recommendations

### Compare None with is

Good:

```python
if user is None:
    create_guest_user()
```

Avoid:

```python
if user == None:
    create_guest_user()
```

`None` is a singleton, so identity comparison is the correct habit.

### Use is not

Good:

```python
if user is not None:
    send_email(user)
```

Avoid:

```python
if not user is None:
    send_email(user)
```

Both can work, but the first version is easier to read.

### Use Specific Exceptions

Good:

```python
try:
    user = users[user_id]
except KeyError:
    user = None
```

Avoid:

```python
try:
    user = users[user_id]
except:
    user = None
```

Bare `except` can hide serious problems and make debugging harder.

### Keep try Blocks Small

Good:

```python
try:
    user = users[user_id]
except KeyError:
    return None

return format_user(user)
```

Avoid:

```python
try:
    user = users[user_id]
    return format_user(user)
except KeyError:
    return None
```

The second version may accidentally catch an error from `format_user()`, not
only from the dictionary lookup.

### Use with for Resources

Good:

```python
with open("report.txt", "w", encoding="utf-8") as file:
    file.write("Monthly report")
```

This closes the file automatically, even if an error happens.

### Use startswith and endswith

Good:

```python
if filename.endswith(".csv"):
    import_csv(filename)
```

Avoid:

```python
if filename[-4:] == ".csv":
    import_csv(filename)
```

The method version is clearer and safer.

### Use Truthiness for Empty Sequences

Good:

```python
if not users:
    print("No users found")
```

Avoid:

```python
if len(users) == 0:
    print("No users found")
```

Python code usually reads better when it uses the natural truth value of empty
lists, tuples, strings, and dictionaries.

## The Zen of Python in Practice

The Zen is not a list of formatting rules. It is a way to make better coding
decisions.

### Readability Counts

Readable code is code that another developer can understand without asking the
original author.

Ask:

- Can I explain this function in one sentence?
- Are the names clear?
- Is the logic direct?
- Would a beginner understand the main flow?

### Explicit Is Better Than Hidden

Avoid hiding important behavior.

Unclear:

```python
def save(data, notify=True):
    ...
```

Clearer:

```python
def save_user(user):
    save_to_database(user)
    send_welcome_email(user)
```

The clearer version shows the important steps.

### Simple Is Better Than Over-Engineered

Do not create a class, decorator, factory, or abstraction unless it solves a
real problem.

Simple:

```python
def apply_tax(price, tax_rate):
    return price * (1 + tax_rate)
```

Too much for a small problem:

```python
class TaxCalculationStrategy:
    def execute(self, price, tax_rate):
        return price * (1 + tax_rate)
```

Use advanced patterns when the project needs them, not to make simple code look
more advanced.

### Flat Is Better Than Deeply Nested

Deep nesting makes code harder to follow.

Harder to read:

```python
def get_discount(user):
    if user:
        if user.is_active:
            if user.orders:
                return 10
    return 0
```

Better:

```python
def get_discount(user):
    if user is None:
        return 0
    if not user.is_active:
        return 0
    if not user.orders:
        return 0
    return 10
```

Early returns can make the normal path easier to see.

### Handle Errors Intentionally

Do not ignore errors silently.

Bad:

```python
try:
    send_email(user)
except EmailError:
    pass
```

Better:

```python
try:
    send_email(user)
except EmailError as error:
    logger.warning("Could not send welcome email: %s", error)
```

If you silence an error, make that choice obvious and intentional.

### Do Not Guess in Ambiguous Situations

When input is unclear, validate it.

Good:

```python
def set_role(role):
    allowed_roles = {"admin", "editor", "viewer"}

    if role not in allowed_roles:
        raise ValueError(f"Unknown role: {role}")

    return role
```

Professional code fails clearly instead of guessing silently.

## Sorted Checklist

Use this checklist when writing or reviewing Python code.

### 1. Structure

- Is the file organized clearly?
- Are imports at the top?
- Are imports grouped correctly?
- Are functions and classes separated by blank lines?

### 2. Names

- Do functions and variables use `snake_case`?
- Do classes use `CapWords`?
- Do constants use `UPPER_CASE`?
- Do names explain purpose?

### 3. Formatting

- Are indentation levels 4 spaces?
- Is whitespace clean and consistent?
- Are long lines wrapped clearly?
- Are trailing commas used when they help multiline code?

### 4. Logic

- Is the code simple enough to explain?
- Is nesting limited?
- Are special cases handled clearly?
- Are errors handled intentionally?

### 5. Comments

- Do comments explain why?
- Are docstrings added for public functions/classes?
- Are outdated comments removed?

### 6. Pythonic Habits

- Is `None` checked with `is` or `is not`?
- Are empty sequences checked with truthiness?
- Are resources opened with `with`?
- Are specific exceptions caught?
- Are `startswith()` and `endswith()` used where suitable?

## Before and After Example

Before:

```python
import sys,os

def DoWork(x,y):
    if x!=None:
        if len(y)>0:
            return x+y[0]
    return None
```

After:

```python
import os
import sys


def add_first_item(value, items):
    if value is None:
        return None
    if not items:
        return None
    return value + items[0]
```

What improved:

- Imports are separated.
- Function name uses `snake_case`.
- Parameters have clearer names.
- `None` is checked with `is`.
- Empty list handling uses truthiness.
- Early returns remove deep nesting.

## Final Notes

PEP 8 teaches discipline. The Zen of Python teaches taste.

A professional Python developer uses both:

- PEP 8 for consistent code style
- The Zen for clear design choices
- Project conventions for teamwork
- Good judgment when rules conflict

Clean code is not about showing how smart you are. It is about making the next
developer's job easier.
