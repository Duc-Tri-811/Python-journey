# Day03: Challenge

orders = [120, 450, 80, 700, 250, 90, 320, 150, 600, 50]

# Total orders
print(f"Total orders: {len(orders)}")

# Total revenue
total = 0

for order in orders:
 total += order
 
print(f"Total revenue: {total}")

# Large orders
count = 0

for order in orders:
 if order >= 300:
  count += 1
  
print(f"Large orders: {count}")

# Large orders revenue
total = 0

for order in orders:
 if order >= 300:
  total += order
  
print(f"Large orders revenue: {total}")

# Small orders
count = 0

for order in orders:
 if order < 100:
  count += 1

print(f"Small orders: {count}")

# Small orders revenue
total = 0

for order in orders:
 if order < 100:
  total += order
  
print(f"Small orders revenue: {total}") 

# Average order value

total_orders = len(orders)

total_revenue = 0

for order in orders:
 total_revenue += order
 
average = total_revenue / total_orders

print(f"Average order value: {average:.2f}")

