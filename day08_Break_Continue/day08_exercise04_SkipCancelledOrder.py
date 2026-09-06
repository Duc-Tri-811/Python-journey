#Exercise 04: Skip cancelled order

orders = [
    {"customer": "Anna", "amount": 450, "status": "paid"},
    {"customer": "Peter", "amount": 120, "status": "cancelled"},
    {"customer": "John", "amount": 700, "status": "paid"},
    {"customer": "Maria", "amount": 80, "status": "cancelled"},
    {"customer": "David", "amount": 320, "status": "paid"},
]


for order in orders:
    if order["status"] == "cancelled":
        continue
        
    print(f"{order['status']} - {order['amount']} €")