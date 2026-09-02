# Exercise 05: Discount base order value

orders = [50, 120, 350, 80, 500]

for order in orders:
 if order < 100:
  print(f"Order: {order} € → Discount: 0%")
 elif order < 300:
  print(f"Order: {order} € → Discount: 5%")
 else:
  print(f"Order: {order} € → Discount: 10%")
  