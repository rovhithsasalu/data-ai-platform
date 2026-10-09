# Day 0: Python Foundations (Quick Start)

**Purpose:** Build enough comfort with Python syntax to make the Week 1 exercises readable. This is a guided warm-up, not a test. Use the project virtual environment when running code: `\.venv\Scripts\Activate.ps1` in PowerShell.

**Time:** About 90 minutes. Go slowly; it is fine to split this into two sessions.

**How to use this page:** For each section, read the short explanation, predict what the code does, then run it and write what you noticed. Don't worry about memorizing syntax yet.

---

## 1. Running Python and reading code (5 min)

Python runs statements from top to bottom. Indentation groups statements into blocks. A `#` begins a comment, which Python ignores.

```python
print("First")
# This line is a comment.
print("Second")
```

**In your words, what happens when this runs?**

> Write here.

---

## 2. Values, types, and names (15 min)

A **value** is a piece of data. Its **type** describes what kind of value it is. A variable name is a label you can use to refer to a value. `=` assigns a name; it does not mean “is equal to” as in algebra.

Common types:

| Type | Example | Used for |
|---|---|---|
| `int` | `7` | Whole numbers |
| `float` | `2.5` | Decimal numbers |
| `str` | `"hello"` | Text |
| `bool` | `True`, `False` | Yes/no conditions |
| `NoneType` | `None` | No value / not set |

```python
name = "Maya"
years = 3
rating = 4.5
is_ready = True
missing_value = None

print(name, type(name))
print(years, type(years))
print(rating, type(rating))
print(is_ready, type(is_ready))
print(missing_value, type(missing_value))
```

**Predict one output line:**

> Write here.

**Run it. What does `type(...)` tell you?**

> Write here.

### Reassignment and simple arithmetic

```python
count = 2
count = count + 1
print(count)

print(7 + 2)
print(7 / 2)
print(7 // 2)
print(7 % 2)
print(2 ** 3)
```

**Explain `=`, `//`, `%`, and `**` in your own words:**

> Write here.

---

## 3. Strings and f-strings (10 min)

Strings are text in quotes. An f-string lets you put a value inside text using `{}`.

```python
first_name = "Asha"
score = 8
print("Hello, " + first_name)
print(f"{first_name} scored {score} points")
```

**Write an f-string that prints your name and a number you choose:**

```python

```

---

## 4. Conditions and comparisons (10 min)

`if` runs its indented block only when its condition is true. `elif` checks another condition; `else` runs if none above matched. Comparisons include `==`, `!=`, `<`, `>`, `<=`, and `>=`.

```python
temperature = 18

if temperature >= 25:
    print("warm")
elif temperature >= 15:
    print("mild")
else:
    print("cold")
```

**Predict the output, then change `temperature` to 10 and predict again:**

> Write here.

**What does indentation tell Python here?**

> Write here.

---

## 5. Lists and loops (15 min)

A list stores items in order and can be changed. Indexes start at `0`. A `for` loop repeats its indented block for each item.

```python
colors = ["red", "green", "blue"]
print(colors[0])

for color in colors:
    print(color)

colors.append("purple")
print(colors)
```

**What does `append` do?**

> Write here.

**Write a loop that prints each number in `[2, 4, 6]`:**

```python

```

### `range` and `while`

```python
for number in range(3):
    print(number)

step = 0
while step < 3:
    print(step)
    step += 1
```

**What numbers does `range(3)` produce? When does the `while` loop stop?**

> Write here.

---

## 6. Dictionaries and sets (10 min)

A dictionary stores **key → value** pairs. A set stores unique items and is useful for checking whether something has been seen.

```python
person = {"name": "Maya", "age": 30}
print(person["name"])
person["age"] = 31
print(person)

seen = {"A", "B", "A"}
print(seen)
print("A" in seen)
```

**In your words, how is a dictionary different from a list? What happened to the repeated `"A"`?**

> Write here.

---

## 7. Functions, parameters, and return values (15 min)

`def` defines a function. Parameters are names a function receives. `return` sends a result back to the caller. `print` displays something; it does not return that value to your code.

```python
def double(number):
    result = number * 2
    return result

answer = double(5)
print(answer)
```

**What is the parameter? What value is passed in? What does the function return?**

> Write here.

### Positional and keyword arguments

```python
def describe(item, quantity=1):
    return f"{quantity} x {item}"

print(describe("book"))
print(describe("pen", 3))
print(describe("mug", quantity=2))
```

**What does `quantity=1` mean in the function definition?**

> Write here.

---

## 8. A tiny data exercise (10 min)

Read each order, keep a running total, and print the result. This combines a list, dictionaries, a loop, and arithmetic.

```python
orders = [
    {"customer": "Asha", "amount": 12},
    {"customer": "Ben", "amount": 8},
    {"customer": "Asha", "amount": 5},
]

total = 0
for order in orders:
    total = total + order["amount"]

print(total)
```

**Predict the printed total and explain how the loop reaches it:**

> Write here.

### Your turn: total by customer

Try writing a function that returns a dictionary of total amount per customer for the orders above. You can use `dict.get(key, 0)` to get the current total or `0` if the key is new.

```python
def totals_by_customer(orders):
    # Your code here
    pass
```

**What did you try? What part felt unclear?**

> Write here.

---

## 9. Checkpoint before Day 1

Mark each item `comfortable`, `need another example`, or `not yet`.

- [ ] I can assign names to values and check a value's type.
- [ ] I can read `if` / `elif` / `else` and understand indentation.
- [ ] I can loop through a list and use `append`.
- [ ] I can get a value from a dictionary by key.
- [ ] I can define a function with `def`, pass arguments, and return a result.
- [ ] I can follow a small loop that updates a running total.

**The three things I want to review before Day 1:**

1. Write here.
2. Write here.
3. Write here.

**Confidence after Day 0 (1–5):** ___ / 5

**Day 1 note:** Keep your original S1–S5 predictions as your cold baseline. After Day 0, revisit each example and add an explanation in `notes/baseline_python.md`; don't erase the first attempt.
