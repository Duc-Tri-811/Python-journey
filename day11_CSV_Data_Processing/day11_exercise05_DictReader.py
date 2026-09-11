#Exercise 05: DictReader
import csv
file_path = r"C:\Users\Name\OneDrive\Tai lieu\Python\Python-journey\day11_CSV_Data_Processing/sales.csv"

with open(file_path, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(f"{row['customer']} - {row['status']} - {row['amount']} €")

        
       
