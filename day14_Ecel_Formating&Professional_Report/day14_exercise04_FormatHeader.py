#Day 14: Exercise 04: Format Header

from openpyxl import load_workbook
from openpyxl.styles import Font, Alignment

file_path = r"C:\Users\Name\OneDrive\Tai lieu\Python\Python-journey\day14_Ecel_Formating&Professional_Report/sales_automated_report.xlsx"

workbook = load_workbook(file_path)
sheet = workbook["Report"]

sheet["A1"].font = Font(bold=True, size=16)
sheet["A1"].alignment = Alignment(horizontal="center")
sheet.column_dimensions["A"].width = 30

sheet["B1"] = "Values"
sheet["B1"].font = Font(bold=True, size=16)
sheet["B1"].alignment = Alignment(horizontal="center")
sheet.column_dimensions["B"].width = 30


workbook.save(file_path)


