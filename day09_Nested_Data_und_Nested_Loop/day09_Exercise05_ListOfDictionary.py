#Exercise 05: List of Dictionary

employees = [
    {
        "name": "Anna",
        "department": "Sales",
        "salary": 3500
    },
    {
        "name": "Peter",
        "department": "IT",
        "salary": 4200
    },
    {
        "name": "John",
        "department": "Sales",
        "salary": 3900
    },
    {
        "name": "Maria",
        "department": "IT",
        "salary": 4500
    }
]


#01: Print the name and department of each employee
for employee in employees:
    print(f"{employee['name']} - {employee['department']}")



#02: Only print IT employee

for employee in employees:
    if employee["department"] == "IT":
        print(f"{employee['name']} - {employee['department']}")
        

#03: Calculate the total salary of IT employee
 
total_IT_salary = 0
for employee in employees:
    if employee["department"] == "IT":
        total_IT_salary += employee["salary"]

print(f"IT salary total : {total_IT_salary:.2f} €")