#Exercise 03: Find the limit order

orders = [120, 250, 80, 450, 700, 90, 320]

for order in orders:
    print(f"Order : {order} €")
    
    if order >= 700:
        break