#Day 13: Exercise 04: Create new Excel file

from openpyxl import Workbook

new_file_path = r"C:\Users\Name\OneDrive\Tai lieu\Python\Python-journey\day13_Write_And_Modify_Excel/sales_report.xlsx"

workbook = Workbook()
sales_report_sheet = workbook.create_sheet("Sales Report")

sales_report_sheet.append(["Sales Report"])
sales_report_sheet.append(["'============"])
sales_report_sheet.append(["Total Orders:",7])
sales_report_sheet.append(["Total Revenue:","2420 €"])
sales_report_sheet.append(["Paid Orders:",4])
sales_report_sheet.append(["Paid Revenue:","1620 €"])



workbook.save(new_file_path)