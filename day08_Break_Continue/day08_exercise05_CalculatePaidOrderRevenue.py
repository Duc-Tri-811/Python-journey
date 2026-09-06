#Exercise 05: Calculate paid order revenue

orders = [
    {"customer": "Anna", "amount": 450, "status": "paid"},
    {"customer": "Peter", "amount": 120, "status": "cancelled"},
    {"customer": "John", "amount": 700, "status": "paid"},
    {"customer": "Maria", "amount": 80, "status": "cancelled"},
    {"customer": "David", "amount": 320, "status": "paid"},
]


paid_revenue = 0
for order in orders:
    if order["status"] != "paid":
        continue
    
    paid_revenue += order["amount"]
    
print(f"Paid revenue: {paid_revenue} €")
