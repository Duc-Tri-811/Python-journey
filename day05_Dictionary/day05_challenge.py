# Challenge

orders = [{"customer": "Anna", "price": 120, "quantity": 2},{"customer": "Peter","price": 80,"quantity": 3},{"customer": "John","price": 250, "quantity": 1}]

for order in orders:
    print(f"Customer: {order['customer']}-Total: {order['price'] * order['quantity']} €")

# total revenue
def calculate_total_revenue(order_list):
    total_revenue = 0
    for order in order_list:
        total_revenue +=  order["price"]*order["quantity"]
    return total_revenue

result_total_revenue = calculate_total_revenue(orders)

print(f"Total revenue: {result_total_revenue:.0f} €")

# find the largest order
def find_largest_order(order_list):
    largest_order = order_list[0]["price"] * order_list[0]["quantity"]
    for order in order_list:
        order_revenue = order["price"]*order["quantity"]
        if largest_order < order_revenue:
            largest_order = order_revenue
    return largest_order

result_largest_order = find_largest_order(orders)
print(f"Largest order: {result_largest_order:.0f} €")

