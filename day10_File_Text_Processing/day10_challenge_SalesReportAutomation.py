#Challenge: Sales report automation
file_path = r"C:\Users\Name\OneDrive\Tai lieu\Python\Python-journey\day10_File_Text_Processing/sales.txt"

with open(file_path, "r") as file:
    total_orders = 0
    total_revenue = 0
    large_orders = 0
    large_order_revenue = 0
    for line in file:
        total_orders += 1
        parts = line.strip().split(",")
        customer = parts[0]
        amount = float(parts[1])
        total_revenue += amount
        if amount >= 300:
            large_orders += 1
            large_order_revenue += amount
    average_order_value = total_revenue / total_orders


# Total orders
print(f"Total orders :{total_orders}")
# Total revenue
print(f"Total revenue : {total_revenue:.2f} €")
# Large orders
print(f"Large orders : {large_orders}")
# Large order revenue
print(f"Large order revenue : {large_order_revenue:.2f} €")
# Average order value
print(f"Average order value : {average_order_value:.2f} €")