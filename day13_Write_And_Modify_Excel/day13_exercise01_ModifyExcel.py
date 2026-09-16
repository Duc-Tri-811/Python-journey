#Day 13: Exercise 01: Modify Excel
from openpyxl import load_workbook

file_path = r"C:\Users\Name\OneDrive\Tai lieu\Python\Python-journey\day13_Write_And_Modify_Excel/sales.xlsx"

workbook = load_workbook(file_path)
sheet = workbook["Sales"]

sheet["D1"] = "Revenue Category"

new_file_path = r"C:\Users\Name\OneDrive\Tai lieu\Python\Python-journey\day13_Write_And_Modify_Excel/sales_updated.xlsx"
workbook.save(new_file_path)
