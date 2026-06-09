def load_expenses(filename):
    expenses = []
    try:
        with open(filename, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    category, amount = line.split(",")
                    expenses.append((category, float(amount)))
    except FileNotFoundError:
        print(f"{filename} not found. Starting with empty list.")
    return expenses


def add_expense(filename, category, amount):
    if amount <= 0:
        raise ValueError("Amount must be a positive number.")
    with open(filename, "a") as f:
        f.write(f"{category},{amount}\n")


def category_totals(expenses):
    totals = {}
    for cat, amount in expenses:
        totals[cat] = totals.get(cat, 0) + amount

    print(f"{'Category':<16} {'Total'}")
    print("─" * 23)
    for cat, total in totals.items():
        print(f"{cat:<16}: ${total:.2f}")
    print("─" * 23)

    grand_total = sum(totals.values())
    print(f"{'Grand Total':<16}: ${grand_total:.2f}")


def above_threshold(expenses, limit):
    return [(c, a) for c, a in expenses if a > limit]


filename = "expenses.txt"
expenses = load_expenses(filename)

print()
category_totals(expenses)

limit = 100
results = above_threshold(expenses, limit)
print(f"\nExpenses above ${limit}:")
for cat, amount in results:
    print(f"  {cat:<14}→ ${amount:.2f}")