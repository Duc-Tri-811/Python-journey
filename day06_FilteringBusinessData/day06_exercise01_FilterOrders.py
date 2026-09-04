#Exercise 01: Filter orders

orders = [
    {"customer": "Anna", "amount": 450},
    {"customer": "Peter", "amount": 120},
    {"customer": "John", "amount": 700},
    {"customer": "Maria", "amount": 80},
    {"customer": "David", "amount": 320}
]

large_orders = []
for order in orders:
    if order["amount"] >= 300:
        large_orders.append(order)

for order in large_orders:
    print(order)