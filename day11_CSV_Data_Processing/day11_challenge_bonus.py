#Challenge bonus
import csv
file_path = r"C:\Users\Name\OneDrive\Tai lieu\Python\Python-journey\day11_CSV_Data_Processing/sales.csv"

def generate_sales_report(filename):
    with open(filename, "r") as file:
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

#02: Calculate total revenue
            total_revenue += amount

#03: Calculate paid orders
            if row["status"] == "paid":
                paid_orders += 1    
                paid_revenue += amount 

#04: Largest paid order   
                if largest_paid_order < amount: 
                    largest_paid_order = amount
                    largest_paid_customer = row["customer"]   

    return {
        "total_orders": total_orders,
        "total_revenue": total_revenue,
        "paid_orders": paid_orders,
        "paid_revenue": paid_revenue,
        "largest_paid_customer": largest_paid_customer,
        "largest_paid_order": largest_paid_order
    }


report = generate_sales_report(file_path)     

print("Sales Report")
print("============")   
print(f"Total orders: {report['total_orders']}")
print(f"Total revenue: {report['total_revenue']:.2f} €")
print(f"Paid orders: {report['paid_orders']}")
print(f"Paid revenue: {report['paid_revenue']:.2f} €")
print(f"Largest paid order: {report['largest_paid_customer']} - {report['largest_paid_order']:.2f} €")

