#Day14: Exercise 05: Professional report

from openpyxl import load_workbook
from openpyxl.styles import Font, Alignment, Border, Side

def format_sales_report(filename, output_filename):

    file_path = rf"C:\Users\Name\OneDrive\Tai lieu\Python\Python-journey\day14_Ecel_Formating&Professional_Report/{filename}"

    workbook = load_workbook(file_path)
    sheet = workbook["Report"]

#Format title und column with
    for row in sheet["A1:B1"]:
        for cell in row:
            cell.font = Font(bold=True, size=20)
            cell.alignment = Alignment(horizontal="center")

    sheet.column_dimensions["A"].width = 35
    sheet.column_dimensions["B"].width = 50

# Format revenue cells
    cell_to_format = ["B3", "B5", "B6", "B9"]
    for cell_ref in cell_to_format:
        sheet[cell_ref].number_format = "#,##0.00 €"

# Bold KPI label
    for row in sheet.iter_rows(min_row=2):
        row[0].font = Font(bold=True)

# Add border for A3:B9
    thin = Side(style="thick")

    for row in sheet["A3:B9"]:
        for cell in row:
            cell.border = Border(
                top = thin,
                bottom = thin,
                left = thin,
                right =thin
            )



    new_file_path = rf"C:\Users\Name\OneDrive\Tai lieu\Python\Python-journey\day14_Ecel_Formating&Professional_Report/{output_filename}"
    workbook.save(new_file_path)

format_sales_report("sales_automated_report.xlsx", "sales_final_report.xlsx")