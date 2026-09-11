#Exercise 04: Calculate revenue
file_path = r"C:\Users\Name\OneDrive\Tai lieu\Python\Python-journey\day10_File_Text_Processing/orders.txt"

with open(file_path, "r") as file:
    total_revenue = 0
    for line in file:
        parts = line.strip().split(",")
        amount = float(parts[1])
        total_revenue += amount

print(f"Total revenue :{total_revenue:.2f} €")



