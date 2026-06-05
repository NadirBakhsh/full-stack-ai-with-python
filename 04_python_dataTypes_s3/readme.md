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
