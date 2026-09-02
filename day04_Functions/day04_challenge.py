# Challenge 

orders = [120, 450, 80, 700, 250, 90, 320, 150, 600, 50]

# Total revenue
def calculate_total_revenue(order_list):
    total_revenue = 0
    for order in order_list:
        total_revenue += order  
    return total_revenue

total_revenue = calculate_total_revenue(orders)
print(f"Total revenue: {total_revenue} €")


# Count large orders
def count_large_orders(order_list):
    count = 0
    for order in order_list:
        if order >= 300:
            count += 1
    return count 

large_orders = count_large_orders(orders)
print(f"Large orders: {large_orders}")

# Calculate large order revenue

def calculate_large_order_revenue(order_list):
    large_order_revenue = 0
    
    for order in order_list:
        if order >= 300:
            large_order_revenue += order
    return large_order_revenue

result_large_order_revenue = calculate_large_order_revenue(orders)

print(f"Large order revenue: {result_large_order_revenue} €")
        
# Average oder value  

def calculate_average_order_value (order_list):
    total_orders = len(order_list)
    total_revenue = calculate_total_revenue(order_list)
    average_order_value = total_revenue/ total_orders
    return average_order_value

result_average_order_value = calculate_average_order_value(orders)

print(f"Average order value: {result_average_order_value:.2f} €")
