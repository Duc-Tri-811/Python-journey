#Exercise 01: Read CSV
import csv
file_path = r"C:\Users\Name\OneDrive\Tai lieu\Python\Python-journey\day11_CSV_Data_Processing/sales.csv"
with open(file_path, "r") as file:
    reader = csv.reader(file)

    next(reader)  # Skip the header row

    for row in reader:
        print(row)