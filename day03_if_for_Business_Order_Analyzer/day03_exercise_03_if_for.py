# Exercise 03: count large orders

orders = [50, 120, 350, 80, 500, 220, 450, 90]

count = 0
for order in orders:
    if order >= 300:
        count += 1


print(f"Large orders: {count}")