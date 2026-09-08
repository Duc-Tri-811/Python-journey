#Exercise 02: Calculate Revenue

order_groups = [
    [120, 250, 80],
    [450, 700, 320],
    [90, 150, 600]
]

total_revenue = 0
for group in order_groups:
    for order in group:
        total_revenue += order
        
print(f"Total revenue: {total_revenue:.2f} €")