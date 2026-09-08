#Exercise 01: Basic nested list

order_groups = [
    [120, 250, 80],
    [450, 700, 320],
    [90, 150, 600]
]

for group in order_groups:
    for order in group:
        print(order)