# Exercise 06: final price function

def calculate_final_price(price,discount_rate):
    discount = price * discount_rate
    final_price = price - discount
    return final_price

result = calculate_final_price(500, 0.1)

print(result)
