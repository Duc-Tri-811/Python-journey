# challenge Bonus

orders = [120, 250, 80, 450, 320, 150, 90, 600, 200, 350]

# Xac dinh bao nhieu don hang co gia tri tren 300
count = 0   
for order in orders:
    if order > 300:
        count += 1  

print(f"Number of orders over 300: {count}")


