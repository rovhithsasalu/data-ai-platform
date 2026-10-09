# Day 1 Python Baseline

Work through this cold, before running any code or checking an answer key. Write your prediction and reasoning first; then run the examples and record what happened.

## Predict the output

### S1 — Mutable default argument

```python
def add(item, bucket=[]):
    bucket.append(item)
    return bucket

print(add(1)); print(add(2)); print(add(3, []))
```

**My predicted output:**

```text
[1] 
[1,2]
[3]
```

**My reasoning / understanding:**

> First time add runs for add(1), bucket initialised to [], post run bucket added value 1, then 2, but in add(3,[]) bucket is initialised with empty again, so answer would be [3]

**Actual output (after running):**

```text
[1]
[1, 2]
[3]
```

**What I learned / what I would explain:**

> my understanding is correct

### S2 — Repeated references in nested lists

```python
a = [[0] * 2] * 2
a[0][0] = 1
print(a)

b = [[0] * 2 for _ in range(2)]
b[0][0] = 1
print(b)
```

**My predicted output:**

```text
a: [[1,0],[0,0]]
b: [[1,0],[0,0]]
```

**My reasoning / understanding:**

> list [0]*2 = [0,0]*2 => [[0,0],[0,0]] => replace a[0][0]=1 => [[1,0],[0,0]]

Similar for b as well

**Actual output (after running):**

```text
a= [[1,0],[1,0]] => I see when list is multiplied each item just references to the existing list so upate to a[0][0] would update everything

b=[[1,0],[0,0]] => I see for each iteration new list item is created an dappended to list which is different from  multiplying list
```

**What I learned / what I would explain:**

> I understood about Names and Values, 2names reffering to same value same situratin in case1 so updating a[0][0] would update both

### S3 — Late-binding closures

```python
funcs = [lambda: i for i in range(3)]
print([f() for f in funcs])

funcs = [lambda i=i: i for i in range(3)]
print([f() for f in funcs])
```

**My predicted output:**

```text
Unable to understand syntax
```

**My reasoning / understanding:**

> Write here.

**Actual output (after running):**

```text
[2,2,2]

[0,1,2]
```

**What I learned / what I would explain:**

> i understand in first case lambda as a funbction is returned and final index is 2, so in print f() is called lambda always giving 2

> In second use case lambda is assigned i in each iteration so for each f() correspondong lambda value is returned

### S4 — Augmented assignment inside a tuple

```python
t = (1, [2, 3])
try:
    t[1] += [4]
except TypeError:
    print("error")
print(t)
```

**My predicted output:**

```text
(1,[2,3,4])
```

**My reasoning / understanding:**

> Appending 4 to tuple postition 1 which is list

**Actual output (after running):**

```text
tuple doesnt support item assigment
```

**What I learned / what I would explain:**

> tuple is immutable, collection inside tuple can be updated so t[1].append would work

### S5 — `nonlocal` and scope

```python
x = "global"

def outer():
    x = "outer"

    def inner():
        nonlocal x
        x = "inner"

    inner()
    return x

print(outer(), x)
```

**My predicted output:**

```text
inner, inner
```

**My reasoning / understanding:**

> not sure what does nonlocal x does, last assigned value fo rx is inner so I feel output is inner and inner for both because we are printing x as second so by the time outer would have executed and value of x has changed

**Actual output (after running):**

```text
inner, global
```

**What I learned / what I would explain:**

> I understood that it is related to scope of variables but I will have to explore/study more 

## Python debugging diagnostic

The functions below contain three bugs. For each bug, first describe the observed or expected failure, write a test that exposes it, then fix the code and record what the bug taught you. Keep your attempted fixes in the sections below.

```python
def dedupe_orders(orders, seen=set()):
    result = []
    for o in orders:
        if o["id"] not in seen:
            seen.add(o["id"])
            result.append(o)
    return result


def totals_by_customer(orders):
    totals = {}
    for o in orders:
        totals[o["customer"]] += o["amount"]
    return totals


def apply_discount(orders, pct):
    for o in orders:
        o["amount"] = o["amount"] * (1 - pct)
    return orders
```

### Bug 1 — `dedupe_orders`

**What I think is wrong / when it appears:**

> Im unable to find bug

**Failing pytest test:**

```python

```

**My fix:**

```python

```

**What this bug teaches me:**

> Write here.

### Bug 2 — `totals_by_customer`

**What I think is wrong / when it appears:**

> Write here.

**Failing pytest test:**

```python

```

**My fix:**

```python

```

**What this bug teaches me:**

> Write here.

### Bug 3 — `apply_discount`

**What I think is wrong / when it appears:**

> Write here.

**Failing pytest test:**

```python

```

**My fix:**

```python

```

**What this bug teaches me:**

> Write here.

## Baseline reflection

**What I got right:**

> Write here.

**What surprised me:**

> Write here.

**Confidence (1–5) before studying:**

- Python internals: ___ / 5
- SQL windows: ___ / 5
- DSA: ___ / 5

**Questions I want to revisit:**

> Write here.

