#Exercise 05: Function

orders = [
    {"customer": "Anna", "amount": 450},
    {"customer": "Peter", "amount": 120},
    {"customer": "John", "amount": 700},
    {"customer": "Maria", "amount": 80},
    {"customer": "David", "amount": 320}
]

def calculate_large_order_revenue(order_list):
    large_order_revenue = 0
    for order in order_list:
        if order["amount"] >= 300:
            large_order_revenue += order["amount"]
    return large_order_revenue
    
result = calculate_large_order_revenue(orders)

print(f"Large order revenue: {result:.2f} €")