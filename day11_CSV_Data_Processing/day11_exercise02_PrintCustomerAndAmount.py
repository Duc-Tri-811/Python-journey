#Exercise 02: Print customer + amount
import csv
file_path = r"C:\Users\Name\OneDrive\Tai lieu\Python\Python-journey\day11_CSV_Data_Processing/sales.csv"

with open(file_path, "r") as file:
    reader = csv.reader(file)

    next(reader) # Skip the header row
    for row in reader:
        customer = row[0]
        amount = float(row[1])
        print(f"{customer} - {amount} €")
        