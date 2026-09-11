#Exercise 03: Calculate Revenue
import csv
file_path = r"C:\Users\Name\OneDrive\Tai lieu\Python\Python-journey\day11_CSV_Data_Processing/sales.csv"

with open(file_path, "r") as file:

    reader = csv.reader(file)

    next(reader)  # Skip the header row

    total_revenue = 0
    for row in reader:
        amount = float(row[1])
        total_revenue += amount

print(f"Total revenue: {total_revenue:.2f} €")