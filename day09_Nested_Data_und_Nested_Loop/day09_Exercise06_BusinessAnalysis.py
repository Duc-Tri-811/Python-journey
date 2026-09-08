# Exercise 06: Business Analysis

company = {
    "name": "ABC GmbH",
    "departments": [
        {
            "name": "Sales",
            "employees": [
                {"name": "Anna", "salary": 3500},
                {"name": "John", "salary": 3900}
            ]
        },
        {
            "name": "IT",
            "employees": [
                {"name": "Peter", "salary": 4200},
                {"name": "Maria", "salary": 4500}
            ]
        }
    ]
}

#01: Print all staffs

for department in company["departments"]:
    for employee in department["employees"]:
        print(f"{department['name']} - {employee['name']} - {employee['salary']} €")


#02: Calculate the total salary of company

total_salary = 0
for department in company["departments"]:
    for employee in department["employees"]:
        total_salary += employee["salary"]
        
print(f"Total salary: {total_salary:.2f} €")


#03: Find employees with salary >= 4000 €
for department in company["departments"]:
    for employee in department["employees"]:
        if employee["salary"] >= 4000:
            print(f"{employee['name']} - {employee['salary']} €")


#04: Calculate the total salary of employees with salary >= 4000 €
total_high_salary = 0
for department in company["departments"]:
    for employee in department["employees"]:
        if employee["salary"] >= 4000:
            total_high_salary += employee["salary"]

print(f"High salary total: {total_high_salary:.2f} €")