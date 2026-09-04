# Exercise 05: Multiply product

products = [{"name":"T-Shirt", "price": 19.90, "quantity":3}, {"name":"Hoodie", "price": 49.90, "quantity": 3}, {"name":"Cap", "price":14.90, "quantity":5}]


for product in products:
    print(f"{product['name']}: {product['price']} € x {product['quantity']}")