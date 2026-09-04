#Exercise 04: Calculate filtered revenue

orders = [
    {"customer": "Anna", "amount": 450},
    {"customer": "Peter", "amount": 120},
    {"customer": "John", "amount": 700},
    {"customer": "Maria", "amount": 80},
    {"customer": "David", "amount": 320}
]

large_order_revenue = 0
for order in orders:
    if order["amount"] >= 300:
        large_order_revenue += order["amount"]
        
print(f"Large order revenue: {large_order_revenue:.2f} €")