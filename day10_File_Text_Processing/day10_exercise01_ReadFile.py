#Exercise 01: Read file
file_path = r"C:\Users\Name\OneDrive\Tai lieu\Python\Python-journey\day10_File_Text_Processing/orders.txt"

with open(file_path, "r") as file:
    content = file.read()
    print(content)

    