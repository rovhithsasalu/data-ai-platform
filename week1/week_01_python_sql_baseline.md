# Week 1: Baseline, Python Mental Model, SQL Windows

*Phase 1 · Capstone stage 1 · 20 hours · every resource below is free (no subscriptions, LeetCode free tier only)*

**By the end of this week you can:** explain how Python names, references, and mutability behave; write window-function SQL from memory; solve basic hashing and two-pointer problems under time pressure; sketch a URL shortener design in 45 minutes; and you have a measured baseline for everything that follows.

---

## The week at a glance

| Day | Hours | What you do |
|---|---:|---|
| 1 | 3.0 | Setup + baseline diagnostic |
| 2 | 3.0 | Python data model and names + 2 DSA problems |
| 3 | 3.0 | Scope, exceptions, modules, venv + build exercise P1 |
| 4 | 3.5 | SQL window functions + 2 SQL problems + 2 DSA problems |
| 5 | 3.0 | System design: URL shortener |
| 6 | 3.5 | 2 DSA problems + exercise DP1 + complexity + career timeline |
| 7 | 1.0 | Exit test and review |
| **Total** | **20.0** | |

**Problems this week:** DSA #1, #125, #49, #347, #238, #15 · SQL #178, #185 · Diagnostic only: DSA #75, SQL #184 · Exercises P1, DP1

---

## Before you start (inside Day 1's 30 minutes)

**Install (all free):**
- Python 3.12 or newer (python.org), VS Code, Git, a free GitHub account
- DuckDB for local SQL practice: `pip install duckdb` (or use PostgreSQL if you already have it)
- pytest: `pip install pytest`

**Create an error log** in Google Sheets (or LibreOffice). Columns:
`Date | Problem | Pattern | Minutes | Outcome (solved / hint / solution) | Why I missed it | Retry +2d | Retry +7d | Retry +21d`

**Create the capstone repo** on GitHub: `data-ai-platform`, with folders `week01/` and `notes/`. Commit after each day.

**How to run any timed problem (use it all plan long):**
1. 2 min: restate the problem and write 2 examples, including an edge case.
2. 3 min: state the brute force and its complexity.
3. 5 min: find the optimization and say why it works.
4. 15 min: code it, talking out loud.
5. 5 min: test with your examples, then state time and space complexity.
Stuck at 20 minutes: read one hint, then finish. Re-solve it from scratch tomorrow. Log every miss.

---

## Day 1 (3.0 hrs): Setup and baseline diagnostic

**Goal:** a measured starting point. Do not study first. Struggling here is the point.

**1. Setup (30 min).** Do the "Before you start" list.

**2. Predict-the-output, cold (30 min).** Without running anything, write your predicted output and a one-line reason for each. Then save your predictions in `notes/baseline_python.md`.

```python
# S1
def add(item, bucket=[]):
    bucket.append(item)
    return bucket
print(add(1)); print(add(2)); print(add(3, []))

# S2
a = [[0] * 2] * 2
a[0][0] = 1
print(a)
b = [[0] * 2 for _ in range(2)]
b[0][0] = 1
print(b)

# S3
funcs = [lambda: i for i in range(3)]
print([f() for f in funcs])
funcs = [lambda i=i: i for i in range(3)]
print([f() for f in funcs])

# S4
t = (1, [2, 3])
try:
    t[1] += [4]
except TypeError:
    print("error")
print(t)

# S5
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

**3. Python debugging diagnostic (30 min).** This code has 3 bugs. Find them, write a failing pytest for each, then fix them. Write what each bug teaches in `notes/baseline_python.md`.

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

**4. DSA baseline (45 min).** LeetCode **#75 Sort Colors** (medium). Use the timed method above, but without a hint. Record the minutes and outcome.

**5. SQL baseline (30 min).** LeetCode SQL **#184 Department Highest Salary**. Record the minutes and outcome.

**6. Baseline notes (15 min).** In `notes/baseline.md`, write: what you got right, what surprised you, and your honest confidence (1-5) in Python internals, SQL windows, and DSA.

**Done when:** all five parts are done, predictions and results are saved, and the first error-log rows exist.

---

## Day 2 (3.0 hrs): Python data model and names

**Goal:** understand that Python variables are names bound to objects, and that this explains most "weird" behavior.

**Study (1 hr):**
- Ned Batchelder, "Facts and myths about Python names and values" (PyCon 2015 talk on YouTube, or the article on nedbatchelder.com). About 30 minutes. This is the single best resource for aliasing and mutability.
- Python Tutorial, section 9.1 "A Word About Names and Objects" (docs.python.org/3/tutorial).
- Language Reference, Data model, section 3.1 "Objects, values and types" (docs.python.org/3/reference/datamodel.html). Read for the ideas, skim the rest.

**Lab (1 hr):**
1. Open **Python Tutor** (pythontutor.com), paste S1 through S4, and step through each one. Watch which names point to which objects.
2. Re-run S1-S5 in a real interpreter. For each, write 2-3 sentences in `notes/python_names.md` explaining *why* the output happens, using the words "name", "object", "mutable", and "binding".
3. Write the one-line rule for each: mutable default arguments, aliasing with `*` on nested lists, late-binding closures, augmented assignment on tuples containing lists.

**DSA (1 hr):** timed method, log both.
- **#1 Two Sum (E):** target O(n) time with a hash map.
- **#125 Valid Palindrome (E):** target O(n) time, O(1) space with two pointers.

Hint ladder (only after 20 minutes): #1 store `value → index` as you scan and look up `target - x`. #125 skip non-alphanumerics from both ends, compare lowercased.

**Done when:** you can explain S1-S4 aloud without notes, and both problems are solved and logged.

---

## Day 3 (3.0 hrs): Scope, exceptions, modules, and exercise P1

**Study (1.25 hrs):**
- Python Tutorial, section 9.2 "Python Scopes and Namespaces" (LEGB, `global`, `nonlocal`).
- Real Python, "Python Scope & the LEGB Rule" (free article).
- Python Tutorial, section 8 "Errors and Exceptions" (try/except/else/finally, raising, custom exceptions).
- Python Tutorial, sections 6 "Modules" and 12 "Virtual Environments and Packages" (imports, `venv`).
- pytest "Get started" (docs.pytest.org): fixtures not needed yet, just `assert` tests and parametrize.

**Build P1 (1.75 hrs): streaming CSV to JSON Lines converter.**

First generate test data. Save as `make_data.py` and run it (creates about 1M rows, a tiny fraction deliberately bad):

```python
import csv, random, datetime
random.seed(42)
start = datetime.date(2025, 1, 1)
with open("orders.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["order_id", "customer_id", "amount", "order_date"])
    for i in range(1, 1_000_001):
        cust = f"C{random.randint(1, 50000):05d}"
        amount = round(random.uniform(1, 500), 2)
        date = (start + datetime.timedelta(days=random.randint(0, 364))).isoformat()
        r = random.random()
        if r < 0.0005:
            amount = "abc"
        elif r < 0.0010:
            cust = ""
        elif r < 0.0015:
            date = "2025-13-45"
        w.writerow([i, cust, amount, date])
```

Then write `p1_convert.py` with this shape:

```python
def validate(row):
    """Return (clean_row, None) if valid, else (None, reason)."""

def convert(src, out_path, reject_path):
    """Stream src row by row. Write valid rows to out_path as JSON Lines.
    Write rejects to reject_path with line number and reason."""
```

**Requirements:**
- Read with the `csv` module, one row at a time. Do not load the file into a list.
- Rules: `order_id` is an integer; `customer_id` is non-empty; `amount` is a number and at least 0; `order_date` is a valid ISO date (use `datetime.date.fromisoformat`).
- Rejects file columns: `line_number, reason, raw_row`.
- Print a summary: total, valid, rejected.
- Write at least 4 pytest tests for `validate` (valid row, bad amount, missing customer, bad date).

**Done when:** valid + rejected = 1,000,000; rejects are about 1,500 (roughly 1,350 to 1,650); pytest passes; peak memory measured with `tracemalloc` is under about 50 MB. Commit it.

---

## Day 4 (3.5 hrs): SQL window functions + DSA

**SQL study (1.25 hrs):**
- PostgreSQL docs, Tutorial section 3.5 "Window Functions" (postgresql.org/docs/current/tutorial-window.html).
- Mode, "SQL Window Functions" tutorial (mode.com/sql-tutorial).
- Optional if rusty: SQLBolt lessons on joins and aggregates (sqlbolt.com).
- Optional practice: PGExercises, "Aggregates" section (includes window functions) at pgexercises.com.

**What you must be able to explain:**
- `PARTITION BY` vs `GROUP BY` (windows keep every row; GROUP BY collapses them).
- `ROW_NUMBER` vs `RANK` vs `DENSE_RANK` on tied values.
- `LAG` / `LEAD`, and a running total with `SUM(...) OVER (ORDER BY ...)`.

**SQL problems (45 min), LeetCode SQL (free):**
- **#178 Rank Scores:** think `DENSE_RANK() OVER (ORDER BY score DESC)`.
- **#185 Department Top Three Salaries:** think `DENSE_RANK()` partitioned by department, filtered to rank 3 or less, joined to the department table.

**DSA (1.5 hrs):** timed method, log both.
- **#49 Group Anagrams (M):** target O(n·k). Hint: build a canonical key per word (sorted letters, or a 26-count tuple).
- **#347 Top K Frequent Elements (M):** target O(n) with bucket sort, or O(n log k) with a heap. Hint: count first, then group by frequency.

**Done when:** you can explain ROW_NUMBER vs RANK vs DENSE_RANK on a tie example aloud, and all four problems are logged.

---

## Day 5 (3.0 hrs): System design, URL shortener

**Goal:** practice the full design structure on a small, well-known problem.

**Study (45 min):**
- System Design Primer (github.com/donnemartin/system-design-primer): read the "Index of system design topics" intro and skim the "Scalability" lecture link.
- "Latency Numbers Every Programmer Should Know" (free, search for the GitHub gist).

**Design (1 hr), on paper, no looking things up.** Use these four groups:
- **Frame:** requirements (functional and non-functional), scale and estimates, APIs, data model.
- **Build:** architecture, storage, caching, partitioning, replication, ID generation.
- **Operate:** failure modes, availability, observability, security and abuse.
- **Evolve:** analytics, custom aliases, expiry, migration, alternatives.

Use these assumptions to check your estimates: 100 million new URLs per month, a 100:1 read-to-write ratio, 5-year retention, about 500 bytes per record. Your numbers should land near: about 39 writes/sec, about 3,900 reads/sec, about 6 billion URLs, and about 3 TB of storage.

**Questions your design must answer:** how do you generate short IDs (base62 counter, hashing, distributed ID service) and what about collisions? Why 301 vs 302 redirects? What do you cache and how? Which database fits a key-value read pattern? How do you handle a hot link?

**Compare (45 min):** read the Primer's "Design Pastebin.com (or Bit.ly)" solution. Write the 5 biggest gaps between your design and theirs in `notes/url_shortener_gaps.md`. Optional: Hello Interview's free "Bit.ly" breakdown, if available.

**Redo (30 min):** on a fresh page, redo the design fast, fixing the gaps. Time yourself and aim for 45 minutes total next time.

**Done when:** you have a one-page design covering all four groups and a list of 5 gaps.

---

## Day 6 (3.5 hrs): DSA, exercise DP1, complexity, career timeline

**DSA (1.5 hrs):** timed method, log both.
- **#238 Product of Array Except Self (M):** target O(n) time, O(1) extra space (excluding output), no division. Hint: a prefix pass, then a suffix pass.
- **#15 3Sum (M):** target O(n²). Hint: sort, fix one number, use two pointers on the rest, skip duplicates.

**DP1 (30 min): memory-safe large-file parsing.** Using `orders.csv` from Day 3:
1. Naive version: `rows = list(csv.DictReader(open("orders.csv")))`, then sum `amount` for valid rows.
2. Generator version: same result with a streaming loop.
3. Measure peak memory for both with `tracemalloc`. Record a 3-row table in `notes/dp1.md`: version, peak MB, seconds.

**Complexity and Python internals (45 min):**
- Big-O Cheat Sheet (bigocheatsheet.com).
- Python wiki "TimeComplexity" page (search `python wiki TimeComplexity`). Memorize: list append/pop (end) vs insert/pop (front), dict and set lookups, `in` on a list vs a set, sorting.
- Optional, free for you: the first complexity and basic-algorithms lessons in Udacity's Data Structures and Algorithms Nanodegree.

**Career timeline (45 min):** write `notes/career_timeline.md`, one page: your path from webMethods EAI to data engineering to AWS to AI agents. For each role or project, include at least one number (data volume, number of pipelines or systems, users, cost, time saved). Mark the 3 pieces of work you are most proud of. This seeds your story bank.

**Done when:** both problems and DP1 are logged, and the timeline has at least 5 numbers.

---

## Day 7 (1.0 hr): Exit test and review

1. **Python (20 min).** Cold, predict and explain these three, then re-explain S1-S5 from memory:

```python
# S6
d = {}
d[[1, 2]] = "x"

# S7
g = (x * x for x in range(3))
print(list(g))
print(list(g))

# S8
import copy
a = {"k": [1, 2]}
b = dict(a)
c = copy.deepcopy(a)
a["k"].append(3)
print(b["k"], c["k"])
```

2. **SQL (15 min).** From memory: explain ROW_NUMBER vs RANK vs DENSE_RANK, and write "top 2 salaries per department" using a window function.
3. **Review (25 min).** Fill in every error-log row. Write 5 lines in `notes/week01_review.md`: your weakest area, your slowest problem, what you would do differently, and what to carry into Week 2.

---

## Exit test (pass criteria)

You pass Week 1 if **all** are true:

- [ ] S1-S8 explained correctly, using the words "name", "object", "mutable"
- [ ] The 3 diagnostic bugs found, tested, and fixed
- [ ] At least 4 of the 6 DSA problems solved without reading the solution (within about 45 minutes each), and every miss is in the error log with a pattern and a reason
- [ ] You can state time and space complexity for all 6
- [ ] SQL #178 and #185 solved, and the ROW_NUMBER/RANK/DENSE_RANK tie example explained
- [ ] P1 passes its tests and the memory and count checks
- [ ] URL shortener one-pager done, with 5 gaps listed
- [ ] Career timeline has at least 5 numbers

If you miss a box, tell me which one when you come back. We'll fix it inside Week 2 instead of moving on blind.

---

## Principal lens (write 5-10 lines in `notes/week01_lens.md`)

> What business decision does a URL shortener enable, and what metric would prove it worked?

Think about who uses click data (marketing, product), what they decide with it, and how you'd tell that the system is actually helping, not just running.

---

## Answer key (check after you've tried)

**S1:** `[1]`, `[1, 2]`, `[3]`. The default list is created once and reused; passing your own list avoids it.
**S2:** `[[1, 0], [1, 0]]`, then `[[1, 0], [0, 0]]`. The `*` repeats a reference to the same inner list; the comprehension creates a new list each time.
**S3:** `[2, 2, 2]`, then `[0, 1, 2]`. Closures look up `i` when called; a default argument captures the value at definition time.
**S4:** prints `error`, then `(1, [2, 3, 4])`. The list is mutated in place first, then the tuple assignment fails.
**S5:** `inner global`. `nonlocal` rebinds `x` in `outer`, and the global `x` is untouched.
**S6:** `TypeError: unhashable type: 'list'`. Dict keys must be hashable; mutable lists are not.
**S7:** `[0, 1, 4]`, then `[]`. A generator is consumed once.
**S8:** `[1, 2, 3] [1, 2]`. `dict(a)` is a shallow copy and shares the inner list; `deepcopy` does not.

**Debug diagnostic bugs:** (1) the mutable default `seen=set()` persists between calls; (2) `totals[o["customer"]] += ...` raises `KeyError` for a new key (use `.get` or `defaultdict`); (3) `apply_discount` mutates the caller's data in place (copy first), and floats are risky for money (consider `Decimal` or integer cents).

---

## Free resources used this week (nothing here costs money)

| Area | Resource |
|---|---|
| Python names/mutability | Ned Batchelder, "Facts and myths about Python names and values"; Python Tutorial 9.1, 9.2; Data model 3.1; Python Tutor |
| Python scope/exceptions/modules | Python Tutorial sections 6, 8, 12; Real Python LEGB article; pytest docs |
| SQL windows | PostgreSQL Tutorial 3.5; Mode SQL window tutorial; PGExercises; SQLBolt (optional); LeetCode SQL free problems |
| DSA | LeetCode free tier; NeetCode roadmap videos for Arrays & Hashing and Two Pointers (watch only after your own attempt); Big-O Cheat Sheet; Python wiki TimeComplexity |
| System design | System Design Primer (GitHub); Latency Numbers gist; Hello Interview free breakdowns (optional) |
| Tools | Python, VS Code, Git/GitHub, DuckDB, pytest, Google Sheets (all free) |
| Optional (free to you) | Udacity Data Structures and Algorithms Nanodegree, first lessons |

---

## When you come back, send me

1. Your Day 1 baseline (how you did on S1-S5, the debug task, #75, #184, with times).
2. Which Week 1 problems you missed or needed hints for.
3. How the exit-test boxes went.
4. How many hours it really took.

I'll use that to adjust Week 2 (Python engineering and concurrency, plus sliding window, stack, and binary search problems) to your actual level.
