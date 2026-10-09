# Week 1 Learning Report

**Period:** October 2026  
**Purpose:** Record completed work, evidence, strengths, current limitations, and open items from Week 1.

## Executive summary

Week 1 helped me identify both what I can already do and where I need structured practice. I completed the Python foundations and file-operation study, learned the names-and-values model, studied Day 3 Python topics, wrote and tested a CSV validator, practiced SQL window functions, attempted the planned DSA problems, compared streaming and in-memory CSV processing, and documented my career timeline and first URL-shortener design.

My clearest strength this week was SQL: I solved the planned SQL problems and felt confident doing so. In DSA, I often found a plausible approach, but some implementations took significant effort or required hints/coding help. My main learning need is Python fluency: understanding references and generators, recognizing which built-in capability or pattern to use, and writing syntax confidently. I want to address this by mastering basic operations first, then solving problems with consistent rigor.

## Work completed

### Day 0 — Python foundations and data types

- Completed the Python foundations warm-up.
- Created and completed a separate notebook covering commonly used operations across Python data types.
- Created a separate file-operations notebook covering text, CSV, and JSON.
- Starting confidence recorded earlier: Python internals **1–2/5**, SQL **3/5**, DSA **1/5**.

### Day 1 — Baseline diagnostic

- Attempted the Python output-prediction problems before studying. The saved baseline shows correct initial understanding of the mutable default example, but incorrect or incomplete predictions for several other examples.
- Solved SQL #184, Department Highest Salary, on the second attempt. Reported **215 ms, Beats 97.19%**.
- Revisited S1–S4 after learning names and values and later reported being able to predict them correctly.

### Day 2 — Names, values, and DSA

- Studied names, object references, aliasing, and mutability using the Python sources in the plan.
- Solved LeetCode #1 Two Sum and #125 Valid Palindrome without help.
- Correctly predicted S1–S4 after studying. I also reported completing S2 and S3. The saved baseline notes contain explanations, though some are brief and S5 still needs a clearer explanation.

### Day 3 — Scope, errors, modules, packages, and P1

- Studied scopes and namespaces, error handling, modules/packages, virtual environments, and pytest using separate notebooks.
- Built the CSV-to-JSONL validation/conversion exercise and changed validation to collect multiple field errors for a row.
- Wrote tests for valid input, invalid amount, invalid date, and missing customer. After correcting the import, duplicate test name, expected cleaned types, and date format, reported that all tests passed.
- Encountered PowerShell's script-execution-policy block when trying to activate `.venv`; used the environment's Python directly as a workaround.

### Day 4 — SQL windows and DSA

- Studied SQL window functions, including partitioning, ranking ties, `LAG`/`LEAD`, running totals, and rolling windows.
- Solved SQL #178 Rank Scores and #185 Department Top Three Salaries. Reported completing the SQL problems quickly and with strong confidence.
- Created a Day 4 SQL notebook with practice cells and an answer key.
- Completed the DSA #49 Group Anagrams and #347 Top K Frequent Elements exercises and shared implementations. The assistance level and timing for these two are not recorded.

### Day 5 — URL-shortener design

- Sketched a first high-level design with users, APIs, CDN/cache, load balancer, application servers, database replicas, and a URL mapping.
- Identified five initial gaps: selecting storage and explaining trade-offs; detailing backend services; reasoning about load balancing and server capacity; defining requirements, estimates, and idempotency; and improving the diagram.
- Discussed the two flows (create and redirect), cache placement, code generation/collision handling, 301 versus 302, average request rates, and asynchronous analytics.
- Documented the first draft and refinement checklist in `week1/day_05_url_shortener_design.md`.
- The final redraw and a completed comparison with the Primer's Bitly/Pastebin solution are not recorded.

### Day 6 — DSA, DP1, and career timeline

- Solved #238 Product of Array Except Self using prefix and suffix products. I took a hint about running products.
- Solved #15 3Sum, but struggled and used coding help.
- Built naive and streaming CSV processing scripts and compared them with `tracemalloc` on one million rows:

  | Version | Peak traced memory | Time |
  |---|---:|---:|
  | Streaming | 225.1 KiB (~0.22 MiB) | 36.26 sec |
  | Naive list materialization | 375,177.2 KiB (~366.38 MiB) | 77.17 sec |

- Both runs processed **1,000,000 rows**: **998,478 valid** and **1,522 rejected**. The streaming script reported a valid-row amount total of `250225354.42998952`.
- Documented the DP1 comparison and takeaways in `notes/dp1.md`.
- Created `notes/career_timeline.md` from my career history, and preserved my original wording in its raw-notes section.

### Day 7 — Exit test and reflection

- Completed the Day 7 test problems in the notebook, including the Python prediction exercises and SQL review. The notebook is `week1/day_07_week1_exit_test.ipynb`.
- Recorded a raw Week 1 reflection in `notes/week01_review.md`.
- The full exit-test checklist has not been audited item by item, so Week 1 should be described as substantially completed, with some plan items still open or undocumented.

## Strengths demonstrated

- **SQL problem solving:** Solved SQL #184 on the second attempt and completed #178 and #185 confidently. I reported solving the Day 4 SQL problems quickly.
- **Approach recognition:** Even when DSA implementation was difficult, I could identify a likely direction for most problems.
- **Learning discipline:** I followed a structured sequence, studied from referenced sources, wrote code, corrected test failures, and revisited areas of confusion.
- **Testing and debugging:** Persisted through pytest import/discovery/expectation issues and got all validator tests passing.
- **Python data processing:** Implemented streaming validation and aggregation, then compared its memory and runtime with a naive implementation.
- **System and platform experience:** My career timeline records work spanning WebMethods integrations, Spark/Glue, AWS messaging, RAG assistants, and pipeline migrations.
- **Reflection:** I identified concrete weaknesses and a practical change for future learning: understand basic operations first, then attempt problems.

## Limitations and areas to improve

- **Python capabilities and syntax fluency:** I do not always know which Python feature or built-in operation to use, and writing syntax can slow me down.
- **References and object behavior:** Names, aliases, mutability, shallow/deep copies, and mutation versus rebinding need repeated practice.
- **Generators and iteration:** Generator behavior and one-pass consumption need more review.
- **Problem implementation:** Recognizing an approach does not always translate quickly into working code. #15 required coding help; #238 required a hint.
- **Pattern selection:** I am learning to use pattern names as a review aid after attempting a problem, rather than as a recipe before attempting it.
- **System design:** The URL-shortener design was a useful first draft, but storage trade-offs, capacity reasoning, idempotency, and communicating architecture clearly remain growth areas.
- **Documentation:** Some baseline explanations and the final Day 5 comparison/redraw are incomplete or not recorded.

## Open items / not confirmed complete

- Review and document S5 (`nonlocal`) more clearly; improve the S1–S4 explanations from brief notes into explanations I can give aloud.
- Complete the original Day 1 debugging diagnostic (mutable default set, missing-key total, and unintended mutation) with tests/fixes, or confirm where that work was completed.
- Confirm whether all six DSA problems meet the plan's “without reading the solution” criterion. #1 and #125 were explicitly solved without help; #238 used a hint; #15 used coding help; assistance details for #49 and #347 were not recorded.
- Record the complexity and attempt time/outcome for each DSA problem in an error log. Complexity was studied and understood, but a complete per-problem log was not found in the Week 1 notes.
- Redraw the URL-shortener architecture and compare it against the Primer solution; fill the five post-comparison gaps in `week1/day_05_url_shortener_design.md`.
- Confirm whether the planned Big-O/Python Time Complexity study was completed.
- Complete the principal-lens note (`notes/week01_lens.md`) and general Week 1 review prompts if still desired.
- Total Week 1 hours and final confidence ratings were not recorded.

## Carry-forward plan

1. Start the next phase with a short Python operations review: strings, lists, dictionaries, sets, comprehensions, iteration, and common built-ins.
2. Practice references, generators, and syntax in small runnable examples before using them in larger problems.
3. Continue DSA attempts independently first. Record the approach, time, help used, complexity, and retry date; consult pattern notes after the attempt.
4. Keep the SQL strength active with periodic timed review.
5. Revisit the URL-shortener design and fill its remaining comparison/reflection items.

