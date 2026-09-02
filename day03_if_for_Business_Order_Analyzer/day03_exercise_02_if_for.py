# Exercise 02: sort multiple orders

orders = [50, 120, 350, 80, 500, 220]

for order in orders:
    if order < 100:
        print(f"Order: {order} € - Small")
    elif order < 300:
        print(f"Order: {order} € - Medium")
    else:
        print(f"Order: {order} € - Large")

        