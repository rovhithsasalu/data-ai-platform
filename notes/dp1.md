# Day 6 DP1: Large-file parsing and memory

## Goal

Compare a naive implementation that loads all CSV rows into a list with a streaming implementation that processes one row at a time. Both validate the rows, write valid records to JSON Lines, write rejects to CSV, and sum the amount for valid rows.

## Results

Measurements recorded from the two scripts on the same `orders.csv` input:

| Version | Approach | Peak traced memory | Execution time |
|---|---|---:|---:|
| Streaming (`p1_validate_sum_amount.py`) | Iterates over `csv.DictReader` one row at a time | 225.1 KiB (~0.22 MiB) | 36.26 sec |
| Naive (`p1_validate_sum_amount_naive.py`) | Materializes all rows with `list(csv.DictReader(...))` | 375,177.2 KiB (~366.38 MiB) | 77.17 sec |

The naive version used roughly **1,667 times** the peak traced memory and took about **2.13 times** as long in this run.

Both runs reported 1,000,000 total rows, 998,478 valid rows, and 1,522 rejected rows. The streaming script printed a valid-row amount total of `250225354.42998952`.

## What I learned

- `list(csv.DictReader(...))` creates and retains a dictionary (and its field strings) for every row. Its memory use grows with the input size: approximately **O(n)** in the number of rows.
- The streaming loop keeps only the current row and a few running counters/totals. Its extra memory remains approximately **O(1)** as the file grows, excluding output buffering and fixed-size state.
- In this run, retaining one million parsed rows also made the naive implementation slower, likely due to allocation and memory-management overhead. Exact elapsed time varies with disk, machine load, and cache state.
- `tracemalloc` measures Python-tracked allocations rather than all process memory, so these are comparable Python-allocation measurements, not total RAM usage.

## Small correctness note

The naive script currently records `i` as the rejected row's line number. Since the data index starts at zero and the CSV includes a header, use `i + 2` to report the physical file line number. The streaming script's `reader.line_num` already accounts for the header.

## Scripts

- Streaming: `week1/p1_validate_sum_amount.py`
- Naive: `week1/p1_validate_sum_amount_naive.py`

