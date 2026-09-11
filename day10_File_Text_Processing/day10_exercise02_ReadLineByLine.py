# Exercise 02: Read line by line
file_path = r"C:\Users\Name\OneDrive\Tai lieu\Python\Python-journey\day10_File_Text_Processing/names.txt"

with open (file_path, "r") as file:
    for line in file: 
        print(line.strip())