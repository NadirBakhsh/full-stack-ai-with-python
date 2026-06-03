# Professional Python Developer Skills with PEP 8 and The Zen

Sources:
- PEP 8: https://peps.python.org/pep-0008/
- PEP 20: https://peps.python.org/pep-0020/

## Goal

The goal is not only to write Python code that works. A professional Python
developer writes code that is readable, maintainable, testable, and easy for a
team to improve.

PEP 8 gives the style discipline. The Zen of Python gives the developer
mindset.

## Professional Python Mindset

A pro Python developer asks these questions while coding:

- Is this easy to read?
- Is the behavior explicit?
- Is the solution simple enough?
- Can another developer safely change this later?
- Are errors handled clearly?
- Does this follow the project's existing style?

Good code is not just correct today. Good code stays understandable tomorrow.

## Skill 1: Write Readable Code

Readability is the first professional skill in Python.

Readable code has:

- Clear names
- Small functions
- Consistent formatting
- Simple control flow
- Useful comments
- Predictable structure

Weak version:

```python
def p(u):
    if u.a and u.e:
        return True
    return False
```

Professional version:

```python
def can_send_email(user):
    return user.is_active and user.email
```

Why this is better:

- The function name explains the decision.
- The variable name has meaning.
- The code removes unnecessary `if`/`else`.

## Skill 2: Use Professional Naming

Names are documentation. A good name reduces the need for comments.

Use these habits:

- Functions: `snake_case`
- Variables: `snake_case`
- Classes: `CapWords`
- Constants: `UPPER_CASE`
- Internal helpers: `_leading_underscore`
- Exceptions: `SomethingError`

Weak names:

```python
def calc(x, y):
    return x * y
```

Professional names:

```python
def calculate_invoice_total(price, quantity):
    return price * quantity
```

Naming checklist:

- Does the name reveal purpose?
- Is it easy to pronounce?
- Is it specific enough?
- Is it consistent with nearby code?
- Does it avoid confusing single-letter names?

Short names are fine for very small scopes:

```python
for item in items:
    print(item)
```

For important business logic, use clear names:

```python
for overdue_invoice in overdue_invoices:
    send_payment_reminder(overdue_invoice)
```

## Skill 3: Format Code Consistently

Professional formatting makes code calm to read.

Use:

- 4 spaces for indentation
- Imports at the top
- One import per line
- Blank lines between logical sections
- Clean whitespace around operators
- Wrapped long lines with parentheses

Weak formatting:

```python
def create_user(name,email,is_admin=False): return {"name":name,"email":email,"admin":is_admin}
```

Professional formatting:

```python
def create_user(name, email, is_admin=False):
    return {
        "name": name,
        "email": email,
        "admin": is_admin,
    }
```

The second version is longer, but it is easier to review and change.

## Skill 4: Organize Imports Like a Maintainer

Imports show the dependency map of a file.

Use this order:

1. Standard library
2. Third-party packages
3. Local project modules

Example:

```python
from pathlib import Path
import json

import requests

from app.settings import BASE_URL
from app.users import User
```

Avoid wildcard imports:

```python
from helpers import *
```

Professional code makes dependencies visible:

```python
from helpers import format_price, send_email
```

## Skill 5: Build Small, Clear Functions

A function should have one main reason to exist.

Good functions:

- Have clear names
- Take clear inputs
- Return predictable outputs
- Avoid hidden side effects
- Stay short enough to understand quickly

Weak function:

```python
def handle(user):
    validate_user(user)
    save_user(user)
    send_email(user)
    print("done")
```

Professional function:

```python
def register_user(user):
    validate_user(user)
    save_user(user)
    send_welcome_email(user)
    log_registration(user)
```

This still has multiple steps, but the function name clearly describes the
workflow.

## Skill 6: Prefer Explicit Code

Explicit code shows what is happening.

Weak:

```python
def save(user, flag=True):
    ...
```

Professional:

```python
def save_user(user):
    save_to_database(user)


def save_user_and_notify(user):
    save_to_database(user)
    send_welcome_email(user)
```

Boolean flags often hide behavior. Separate functions can make intent clearer.

## Skill 7: Keep Logic Simple

The Zen favors simple code over complicated code.

Weak:

```python
def get_access(user):
    if user:
        if user.is_active:
            if user.role == "admin":
                return True
    return False
```

Professional:

```python
def has_admin_access(user):
    if user is None:
        return False
    if not user.is_active:
        return False
    return user.role == "admin"
```

Why this is better:

- Less nesting
- Clear failure cases
- Main decision is easy to see

## Skill 8: Handle Errors Clearly

Errors should not disappear silently.

Weak:

```python
try:
    payment.charge()
except:
    pass
```

Professional:

```python
try:
    payment.charge()
except PaymentError as error:
    logger.warning("Payment failed: %s", error)
    raise
```

Error handling checklist:

- Catch specific exceptions.
- Keep `try` blocks small.
- Log useful context.
- Re-raise when the caller must know.
- Silence errors only when there is a clear reason.

## Skill 9: Use Pythonic Conditions

Professional Python uses the language naturally.

Use `is None`:

```python
if user is None:
    return "guest"
```

Use truthiness for empty collections:

```python
if not orders:
    return []
```

Use `startswith()` and `endswith()`:

```python
if filename.endswith(".json"):
    load_json(filename)
```

Use `isinstance()` for type checks:

```python
if isinstance(value, int):
    return value * 2
```

Avoid:

```python
if user == None:
    return "guest"

if len(orders) == 0:
    return []

if filename[-5:] == ".json":
    load_json(filename)

if type(value) is int:
    return value * 2
```

## Skill 10: Use Context Managers

Use `with` when working with resources such as files, locks, connections, or
transactions.

Professional:

```python
from pathlib import Path


def read_report(path):
    report_path = Path(path)

    with report_path.open(encoding="utf-8") as file:
        return file.read()
```

This makes cleanup automatic and reliable.

## Skill 11: Write Useful Comments

A professional comment explains the reason behind code.

Weak:

```python
# Check if user is active
if user.is_active:
    send_email(user)
```

Professional:

```python
# Trial users receive onboarding emails only after activation.
if user.is_active:
    send_email(user)
```

Comment rules:

- Explain why, not obvious what.
- Delete comments that repeat the code.
- Update comments when behavior changes.
- Use docstrings for public functions and classes.

## Skill 12: Design Better Interfaces

A public function, class, or module is a promise to other developers.

Professional API habits:

- Keep public names clear.
- Prefix internal helpers with `_`.
- Avoid exposing unnecessary details.
- Make return values predictable.
- Raise meaningful exceptions.
- Avoid surprising side effects.

Weak:

```python
def run(data):
    ...
```

Professional:

```python
def import_customer_records(records):
    ...
```

The second function tells the caller what kind of data it expects and what the
operation does.

## Skill 13: Review Code Like a Professional

When reviewing Python code, do not only ask, "Does it work?"

Ask:

- Is the code readable?
- Does it follow the project style?
- Are names clear?
- Is there unnecessary complexity?
- Are errors handled properly?
- Are edge cases tested?
- Could this be changed safely later?

Good review comments are specific:

```text
Can we rename `data` to `customer_records`? That would make the import logic
easier to follow.
```

Avoid vague comments:

```text
This looks bad.
```

Professional reviews improve the code and respect the developer.

## Skill 14: Refactor Without Changing Behavior

Refactoring means improving code structure while keeping the same behavior.

Safe refactoring habits:

- Rename unclear variables.
- Extract repeated logic into functions.
- Reduce deep nesting.
- Split large functions.
- Add tests before changing risky code.
- Keep each change small enough to review.

Before:

```python
def price(p, q, d):
    t = p * q
    if d:
        t = t - (t * d / 100)
    return t
```

After:

```python
def calculate_price(price, quantity, discount_percent=0):
    subtotal = price * quantity
    discount = subtotal * discount_percent / 100
    return subtotal - discount
```

The behavior is the same, but the meaning is clearer.

## Skill 15: Know When to Break a Rule

Professional developers do not follow rules blindly.

It can be acceptable to ignore a PEP 8 guideline when:

- The project has a different established convention.
- Changing style would break compatibility.
- The rule makes the specific code harder to read.
- Existing surrounding code already follows another style.

But breaking a rule should be a conscious decision, not an accident.

## Daily Developer Checklist

Before you finish Python code, check:

- Code is formatted consistently.
- Imports are grouped and unused imports are removed.
- Names explain intent.
- Functions are small and focused.
- Long lines are wrapped clearly.
- Errors are handled with specific exceptions.
- `None` uses `is` or `is not`.
- Empty lists, strings, and dictionaries use truthiness.
- Comments explain why.
- Public functions/classes have useful docstrings.
- Tests or examples cover important behavior.

## Pro Skill Levels

### Beginner

- Writes code that runs.
- Learns syntax and basic formatting.
- Starts using clear variable names.

### Intermediate

- Writes reusable functions.
- Follows PEP 8 consistently.
- Handles common errors.
- Uses modules and imports cleanly.

### Professional

- Designs code for future readers.
- Chooses simple solutions first.
- Makes behavior explicit.
- Reviews code with care.
- Refactors safely.
- Understands when consistency matters more than preference.

## Final Principle

A professional Python developer writes code that another developer can trust.

Use PEP 8 to make code clean.

Use The Zen of Python to make code thoughtful.

Use practice, reviews, and refactoring to turn both into real skill.
