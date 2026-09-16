#Day 14: Exercise 01: Format report title

from openpyxl import load_workbook
from openpyxl.styles import Font, Alignment

file_path = r"C:\Users\Name\OneDrive\Tai lieu\Python\Python-journey\day14_Ecel_Formating&Professional_Report/sales_automated_report.xlsx"

workbook = load_workbook(file_path)

sheet = workbook["Report"]

sheet["A1"].font = Font(bold=True, size=16)
sheet["A1"].alignment = Alignment(horizontal="center")

workbook.save(file_path)


