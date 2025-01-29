items = [
    ("Apple", 1.2),
    ("Banana", 0.5),
    ("Orange", 0.75),
    ("Grapes", 2.5),
]

print(f"{'Item':<10} {'Price ($)':>10}")
print("-" * 22)

for item, price in items:
    print(f"{item:<10} {price:>10.2f}")
