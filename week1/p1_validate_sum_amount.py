import csv
import json
import math
from datetime import date


def validate(row):
    """Return (clean_row, None) if valid, else (None, list_of_errors)."""
    errors = []

    order_id_text = row.get("order_id")
    try:
        if order_id_text is None or not str(order_id_text).strip():
            raise ValueError
        order_id = int(str(order_id_text).strip())
    except (TypeError, ValueError):
        order_id = None
        errors.append("order_id is required and must be an integer")

    customer_id_value = row.get("customer_id")
    if customer_id_value is None or not str(customer_id_value).strip():
        customer_id = None
        errors.append("customer_id must be non-empty")
    else:
        customer_id = str(customer_id_value).strip()

    amount_value = row.get("amount")
    try:
        amount = float(amount_value)
    except (TypeError, ValueError):
        amount = None
        errors.append("amount must be numeric and at least 0")
    else:
        if not math.isfinite(amount) or amount < 0:
            amount = None
            errors.append("amount must be numeric and at least 0")

    order_date_value = row.get("order_date")
    try:
        order_date = date.fromisoformat(str(order_date_value).strip())
    except (TypeError, ValueError):
        order_date = None
        errors.append("order_date must be a valid ISO date")

    if errors:
        return None, errors

    clean_row = {
        "order_id": order_id,
        "customer_id": customer_id,
        "amount": amount,
        "order_date": order_date.isoformat(),
    }
    return clean_row, None


def convert(src, out_path, reject_path):
    """Stream CSV rows to JSON Lines and record rejected rows in a CSV file."""
    total_rows = 0
    valid_rows = 0
    rejected_rows = 0
    total_amount=0.0

    with (
        open(src, "r", newline="", encoding="utf-8") as source,
        open(out_path, "w", encoding="utf-8") as valid_file,
        open(reject_path, "w", newline="", encoding="utf-8") as reject_file,
    ):
        reader = csv.DictReader(source)
        reject_writer = csv.DictWriter(
            reject_file,
            fieldnames=["line_number", "reason", "raw_row"],
        )
        reject_writer.writeheader()

        for row in reader:
            total_rows += 1
            clean_row, reason = validate(row)

            if reason is None:
                valid_file.write(json.dumps(clean_row, ensure_ascii=False) + "\n")
                valid_rows += 1
                total_amount += clean_row["amount"]
            else:
                reject_writer.writerow(
                    {
                        "line_number": reader.line_num,
                        "reason": "; ".join(reason),
                        "raw_row": json.dumps(row, ensure_ascii=False),
                    }
                )
                rejected_rows += 1

    print(f"Total rows: {total_rows}")
    print(f"Valid rows: {valid_rows}")
    print(f"Rejected rows: {rejected_rows}")
    print(f"Total amount: {total_amount}")




        

if __name__ == "__main__":
    import tracemalloc
    import time
    start_time = time.perf_counter()

    tracemalloc.start()
    
    convert("orders.csv", "valid.jsonl", "rejects.csv")
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Current traced memory: {current / 1024:.1f} KiB")
    print(f"Peak traced memory:    {peak / 1024:.1f} KiB")
    end_time = time.perf_counter()  
    print(f"Total Execution Time in Seconds: {end_time - start_time}")
    '''
    Total rows: 1000000
    Valid rows: 998478
    Rejected rows: 1522
    Total amount: 250225354.42998952
    Current traced memory: 6.1 KiB
    Peak traced memory:    225.1 KiB
    Total Execution Time in Seconds: 36.25924409995787
    '''
