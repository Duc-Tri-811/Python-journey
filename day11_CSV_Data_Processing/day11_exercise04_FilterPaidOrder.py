#Exercise 04: Filter Paid Orders
import csv
file_path = r"C:\Users\Name\OneDrive\Tai lieu\Python\Python-journey\day11_CSV_Data_Processing/sales.csv"

with open(file_path, "r") as file:
    reader = csv.reader(file)

    next(reader)  # Skip the header row

    paid_revenue = 0
    for row in reader:
        customer = row[0]
        amount = float(row[1])
        status = row[2]
        if status == "paid":
            print(f"{customer} - {amount} €")
            paid_revenue += amount

print(f"Paid revenue: {paid_revenue:.2f} €")

