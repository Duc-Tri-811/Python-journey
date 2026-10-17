#Day 15: Exercise 05: API - Excel

import openpyxl
import requests

url = "https://dummyjson.com/carts"

try:
    # Send Get requests with a timeout of 10 seconds to avoid infinite waiting if connetion hang 
    response = requests.get(url, timeout=10)
    # Raise an exception of the HTTP status is in the 4xx or 5xx error rang
    response.raise_for_status()
    # Convert response to a Python dictionary safety inside the try block
    data = response.json()

    # Safety extract the carts list, fallback to an empty list if key doesn't exist
    carts_list = data.get("carts", [])

    #01: Create a new Excel workbook(wb) and worksheet(ws) using openpyxl
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Carts Report"

    #02: Create Header row for the Excel file
    ws.append(["Cart ID", "User ID", "Total Amount ($)", "Total Products"])

    #03: Loop through each cart and write data into Excel
    for cart in carts_list:
        # Use .get() to prevent KeyError if 'total', 'id', or 'userId' is missing from API
        cart_id = cart.get("id", "N/A")
        user_id = cart.get("userId", "N/A")
        total_amount = cart.get("total", 0.0)
        total_products = cart.get("totalProducts", 0.0)

        # Append each cart's information as a new row in Excel file
        ws.append([cart_id, user_id, total_amount, total_products])

        #04: Save the workbook to an Excel file
        file_name = "day15_API_Fundamentals/carts_report.xlsx"
        wb.save(file_name)

except requests.exceptions.RequestException as e:
    print("An error occurred: {e}")




    