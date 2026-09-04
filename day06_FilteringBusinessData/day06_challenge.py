#Exercise 06: Challenge

orders = [
    {"customer": "Anna", "amount": 450, "status": "paid"},
    {"customer": "Peter", "amount": 120, "status": "pending"},
    {"customer": "John", "amount": 700, "status": "paid"},
    {"customer": "Maria", "amount": 80, "status": "cancelled"},
    {"customer": "David", "amount": 320, "status": "paid"},
    {"customer": "Lisa", "amount": 600, "status": "pending"}
]

# Number of paid orders
def count_paid_orders(order_list):
    count = 0
    for order in order_list:
        if order["status"] == "paid":
            count += 1
    return count
    
result_count = count_paid_orders(orders)

print(f"Number of paid orders: {result_count}")

# Paid revenue
def calculate_paid_revenue(order_list):
    paid_revenue = 0
    for order in order_list:
        if order["status"] == "paid":
            paid_revenue += order["amount"]
    return paid_revenue

result_paid_revenue = calculate_paid_revenue(orders)

print(f"Paid revenue: {result_paid_revenue:.2f} €")

# Find largest paid order
def find_largest_paid_order(order_list):
    largest_paid_order = None

    for order in order_list:
        if order["status"] == "paid":
            if largest_paid_order is None:
                largest_paid_order = order
            elif order["amount"] > largest_paid_order["amount"]:
                largest_paid_order = order

    return largest_paid_order
    
result_largest_paid_order = find_largest_paid_order(orders)

print(f"Largest_paid_order: {result_largest_paid_order['customer']}" " - " f"{result_largest_paid_order['amount']:.2f} €")