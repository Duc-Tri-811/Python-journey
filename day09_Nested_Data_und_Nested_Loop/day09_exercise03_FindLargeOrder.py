#Exercise 03: Find large order (>= 300)

order_groups = [
    [120, 250, 80],
    [450, 700, 320],
    [90, 150, 600]
]

for group in order_groups:
    for order in group:
        if order >= 300:
            print(f"{order} €")
