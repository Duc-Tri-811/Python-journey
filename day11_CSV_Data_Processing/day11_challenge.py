#Challenge
import csv
file_path = r"C:\Users\Name\OneDrive\Tai lieu\Python\Python-journey\day11_CSV_Data_Processing/sales.csv" 

with open(file_path, "r") as file:
    reader = csv.DictReader(file)

#01: Calculate total orders
    total_orders = 0
    total_revenue = 0
    paid_orders = 0
    paid_revenue = 0
    largest_paid_order = 0
    
    for row in reader:
        amount = float(row["amount"])
        total_orders += 1
#02: Calcultate total revenue
        total_revenue += amount

#03: Calculate paid orders
        if row["status"] == "paid":
            paid_orders += 1

#04: Calculate paid revenue
            paid_revenue += amount
            if largest_paid_order < amount:
                largest_paid_order = amount
                top_customer = row["customer"]

print(f"Total orders: {total_orders}")
print(f"Total revenue: {total_revenue:.2f} €")
print(f"Paid orders: {paid_orders}")
print(f"Paid revenue: {paid_revenue:.2f} €")
print(f"Largest paid order : {top_customer} - {largest_paid_order} €")

#05: Function
def calculate_paid_revenue(filename):
    with open(filename,"r") as file:
        reader =csv.DictReader(file)

        paid_revenue = 0
        for row in reader:
            if row["status"] == "paid":
                paid_revenue += float(row["amount"])

    return paid_revenue

paid_revenue = calculate_paid_revenue(file_path)
print(f"Paid revenue : {paid_revenue:.2f} €")
