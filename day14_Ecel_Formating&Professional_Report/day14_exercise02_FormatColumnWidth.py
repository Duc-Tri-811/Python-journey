#Day 14: Exercise 02: Format column width

from openpyxl import load_workbook
from openpyxl.styles import Alignment

file_path = r"C:\Users\Name\OneDrive\Tai lieu\Python\Python-journey\day14_Ecel_Formating&Professional_Report/sales_automated_report.xlsx"

workbook = load_workbook(file_path)
sheet = workbook["Report"]

sheet.column_dimensions["A"].width = 25
sheet.column_dimensions["B"].width = 20

workbook.save(file_path)