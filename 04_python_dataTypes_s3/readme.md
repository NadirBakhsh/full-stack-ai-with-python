# Objects - Mutable and Immutable in Python

## 1. What is an Object?

In Python, almost everything is an object.
An object has a **value**, a **type**, and an **identity** (memory location).

> **Key point:** We can check the identity of an object using the `id()` function.

---

## 2. Immutable Objects

Immutable objects **cannot** be changed after they are created.
Any operation that seems to change the value actually creates a **new object**.

**Examples:** `int`, `float`, `complex`, `bool`, `str`, `tuple`, `frozenset`, `bytes`

```python
a = 10
b = a
print(id(a))  # suppose 1001
a = a + 5     # creates new object
print(id(a))  # suppose 2002
print(id(b))  # 1001 (unchanged)
```

> Here, a new object is created when the value changes.

---

## 3. Mutable Objects

Mutable objects **can** be changed after they are created.
The changes are made to the **same object** (same identity).

**Examples:** `list`, `dict`, `set`, `bytearray`

```python
l = [10, 20, 30]
print(id(l))  # suppose 3001
l.append(40)  # modifies the same object
print(id(l))  # 3001 (same)
```




> Here, the object is modified in place. Identity remains the same.

---

## 4. Summary

| Immutable | Mutable |
|-----------|---------|
| Cannot be changed after creation | Can be changed after creation |
| Operations create new object | Operations modify the same object |
| Examples: `int`, `str`, `tuple`, etc. | Examples: `list`, `dict`, `set`, etc. |

> **Remember:** Use mutable objects when you need to modify data.
> Use immutable objects when data should not change.

![Objects in Python](./object.png)

---

## interger


In Python, integers (`int`) are a fundamental data type used to represent whole numbers (positive, negative, or zero) without any decimal point.

### Example: Integer Operations

Let's see how we can work with integers in Python:

```python
# Declare integer variables
black_tea_grams = 100
ginger_grams = 3

# Addition
total_ingredients = black_tea_grams + ginger_grams
print(f"Total ingredients: {total_ingredients} grams")  # Output: 103 grams

# Subtraction
remaining = black_tea_grams - ginger_grams
print(f"Remaining ingredients: {remaining} grams")      # Output: 97 grams

# Basic arithmetic operations
number_a = 10
number_b = 20

sum = number_a + number_b           # Addition: 30
difference = number_a - number_b    # Subtraction: -10
product = number_a * number_b       # Multiplication: 200
quotient = number_a / number_b      # Division: 0.5 (Note: result is float)
remainder = number_a % number_b     # Modulus: 10 (remainder after division)
power = number_a ** number_b        # Exponentiation: 10 to the power of 20

# Print results
print(f"Sum: {sum}")
print(f"Difference: {difference}")
print(f"Product: {product}")
print(f"Quotient: {quotient}")
print(f"Remainder: {remainder}")
print(f"Power: {power}")
```

**Key Points:**
- Integer objects are **immutable** in Python.
- All basic arithmetic operations can be performed using operators like `+`, `-`, `*`, `/`, `%`, and `**`.
- Division (`/`) of two integers returns a float. Use `//` (floor division) if you need an integer result.

```python
print(10 // 3)  # Output: 3
```

Integers are widely used in programs for counting, indexing, and whenever whole numbers are needed.

---

