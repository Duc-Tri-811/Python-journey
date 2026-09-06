#Exercise 06: Challenge Business Automation Logic 

orders = [
    {"customer": "Anna", "status": "paid", "amount": 450},
    {"customer": "Peter", "status": "cancelled", "amount": 120},
    {"customer": "John", "status": "paid", "amount": 700},
    {"customer": "Maria", "status": "pending", "amount": 250},
    {"customer": "David", "status": "paid", "amount": 320},
    {"customer": "Lisa", "status": "paid", "amount": 900},
    {"customer": "Tom", "status": "paid", "amount": 150},
]


paid_revenue = 0
for order in orders:
    if order["status"] != "paid":
            continue
            
    paid_revenue += order["amount"]   
    
    if order["amount"] >= 700:
        break
        
print(f"Paid revenue : {paid_revenue} €")

# Function

def calculate_paid_revenue_until_large_order(order_list):

    paid_revenue = 0
    for order in order_list:
        if order["status"] != "paid":
            continue
        
        paid_revenue += order["amount"]
        
        if order["amount"] >= 700:
            break
    return paid_revenue
    
result_paid_revenue = calculate_paid_revenue_until_large_order(orders)

print(f"Paid revenue: {result_paid_revenue} €")