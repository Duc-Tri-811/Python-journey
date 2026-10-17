# Day 15: Challenge: API Sales Report Automation

import openpyxl
from openpyxl import load_workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
import requests

# Fetch data from API endpoint
url = "https://dummyjson.com/carts"

try:
    # Send Get request with a timeout of 10 seconds to avoid infinite waiting if connection hangs
    response = requests.get(url, timeout=10)

    # Raise an exception if the HTTP status is in the 4xx or 5xx error range
    response.raise_for_status()

    # Convert response to an Python dictonary safely inside the try block
    data = response.json()

    # Safety extract the cart list, fallback to an empty list if key doesn't exist
    carts_list = data.get("carts", [])

    # Defensive check: Handle empty list case gracefully
    if not carts_list:
        print("Warning: API returned an empty carts list.")
    else:
        #01. Create variables for calculation
        total_carts = len(carts_list)
        total_revenue = 0
        largest_order = 0

        # Loop through each cart and calculation KPIs safely
        for cart in carts_list:
            # Use .get() to prevent KeyError if 'total' is missing from API
            cart_total = cart.get("total", 0.0)
            total_revenue += cart_total

            # Find the largest order
            if cart_total > largest_order:
                largest_order = cart_total

        # Print summary metrics to console for quick verification
        print(f"Total Carts: {total_carts}")
        print(f"Total Revenue: ${total_revenue:,.2f}")
        print(f"Largest Order: ${largest_order:,.2f}")

        #02. Create a new Excel workbook(wb) and worksheet(ws) using openpyxl
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Sales Summary"

        # Add Report Title & Header with clean structure
        ws.append(["API SALE REPORT AUTOMATION", "Value"])
        ws.append(["Total Carts", total_carts])
        ws.append(["Total Revenue ($)", total_revenue])
        ws.append(["Largest Order ($)", largest_order])

        #03. Save the workbook to an Excel file using relative path inside the folder
        file_name = "day15_API_Fundamentals/api_sales_report.xlsx"
        wb.save(file_name)

        #04. Professional formatting for the Excel file
        workbook = load_workbook(file_name)
        sheet = workbook["Sales Summary"]

        # Format header row (Row 1)
        for row in sheet["A1:B1"]:
            for cell in row:
                cell.font = Font(name="Calibri", size=12, bold=True, color="FFFFFF")
                cell.fill = PatternFill(
                    start_color="1F4E78", end_color="1F4E78", fill_type="solid"
                )
                cell.alignment = Alignment(horizontal="center", vertical="center")

        # Format data rows (Row 2 to 4)
        for row in sheet.iter_rows(min_row=2, min_col=1, max_col=2):
            for cell in row:
                cell.font = Font(name="Calibri", size=11)
                cell.alignment = Alignment(vertical="center")

            # Apply number formating for currency rows (Row 3 and 4 in column B)
            sheet["B3"].number_format = "$#,##0.00"
            sheet["B4"].number_format = "$#,##0.00"   

        # Adjust column widths automatically for clean presentation
        sheet.column_dimensions["A"].width = 30
        sheet.column_dimensions["B"].width = 25

        # Save the polished workbook
        workbook.save(file_name)
        print(f"Successfully generated and formatted sales report: {file_name}")

except requests.exceptions.RequestException as e:
    print(f"An error occoured: {e}")



