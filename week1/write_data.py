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