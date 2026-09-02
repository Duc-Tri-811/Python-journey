# Exercise 04: print vs return

# Function A
def show_total(price, quantity):
    print(price * quantity)

show_total(35, 20)

# Function B

def calculate_total(price, quantity):
    total = price * quantity
    return total

result = calculate_total(35, 20)

print(result)
