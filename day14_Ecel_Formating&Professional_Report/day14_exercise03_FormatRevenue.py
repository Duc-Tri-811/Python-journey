#Day 14: Exercise 03: Format revenue

from openpyxl import load_workbook

file_path = r"C:\Users\Name\OneDrive\Tai lieu\Python\Python-journey\day14_Ecel_Formating&Professional_Report/sales_automated_report.xlsx"

workbook = load_workbook(file_path)
sheet = workbook["Report"]

cell_to_format = ["B3", "B5", "B6", "B9"]

for cell_ref in cell_to_format:
    sheet[cell_ref].number_format = "#,##0.00 €"

workbook.save(file_path)