# Exercise 04: total revenue from large orders (>= 300)

orders = [50, 120, 350, 80, 500, 220, 450, 90]
total = 0
for order in orders:
    if order >= 300:
        total += order

print(f"Large orders revenue : {total} €")


