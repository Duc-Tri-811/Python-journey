#Exercise 03: Count filtered orders

orders = [
    {"customer": "Anna", "amount": 450},
    {"customer": "Peter", "amount": 120},
    {"customer": "John", "amount": 700},
    {"customer": "Maria", "amount": 80},
    {"customer": "David", "amount": 320}
]

count = 0
for order in orders:
    if order["amount"] >= 300:
        count += 1
        
print(f"Number of large orders: {count}")