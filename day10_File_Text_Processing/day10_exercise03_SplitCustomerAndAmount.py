# Exercise 03: Split customer & amount
file_path = r"C:\Users\Name\OneDrive\Tai lieu\Python\Python-journey\day10_File_Text_Processing/orders.txt"

with open(file_path, "r") as file:
    for line in file:
        parts = line.strip().split(",")
        customer = parts[0]
        amount = parts[1]
        print(f"{customer} - {amount} €")
        