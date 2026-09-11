#Exercise 05: Filter Large Orders
file_path = r"C:\Users\Name\OneDrive\Tai lieu\Python\Python-journey\day10_File_Text_Processing/orders.txt"

with open (file_path, "r") as file:
    for line in file:
        parts = line.strip().split(",")
        customer = parts[0]
        amount = float(parts[1])
        if amount >= 300: 
            print(f"{customer} - {amount:.2f} €")