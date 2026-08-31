# challenge

orders = [120, 250, 80, 450, 320, 150, 90, 600, 200, 350]

# Dem so don hang 
print(f" Number of orders: {len(orders)}")

# Tinh tong doanh thu
total = 0
for order in orders:
    total = total + order
print(f"Total revenue: {total} €")

# In tung don hang
for order in orders:
    print(f"Order: {order} €")

# Tim don hang lon nhat
max_order = orders[0]
for order in orders:
    if order > max_order:
        max_order = order

print(f"Largest order: {max_order} €")
