# Challenge: Mini business automation
company = {
    "name": "ABC GmbH",
    "departments": [
        {
            "name": "Sales",
            "employees": [
                {
                    "name": "Anna",
                    "salary": 3500,
                    "orders": [120, 450, 80]
                },
                {
                    "name": "John",
                    "salary": 3900,
                    "orders": [700, 250, 320]
                }
            ]
        },
        {
            "name": "IT",
            "employees": [
                {
                    "name": "Peter",
                    "salary": 4200,
                    "orders": [90, 150]
                },
                {
                    "name": "Maria",
                    "salary": 4500,
                    "orders": [600, 900, 200]
                }
            ]
        }
    ]
}

#01: Print all orders by employee
for department in company["departments"]:
    for employee in department["employees"]:
        print(f"{employee['name']}")
        for order in employee["orders"]:
            print(f"{order} €")
            

#02: Calculate total orders per employee
for department in company["departments"]:
    for employee in department["employees"]:
        total_order = 0
        for order in employee["orders"]:
            total_order += order
        print(f"{employee['name']} : {total_order} €")


#03: Find the employee with the highest order revenue
highest_revenue = 0

for department in company["departments"]:
    for employee in department["employees"]:
        order_revenue = 0
        for order in employee["orders"]:
            order_revenue += order
        
        if order_revenue > highest_revenue:
            highest_revenue = order_revenue
            top_employee = employee["name"]

print(f"Top employee : {top_employee}")
print(f"Revenue : {highest_revenue}")

#04: Calculate the total revenue of company
total_revenue = 0

for department in company["departments"]:
    for employee in department["employees"]:
        employee_revenue = 0
        for order in employee["orders"]:
            employee_revenue += order
        total_revenue += employee_revenue

print(f"Total company revenue : {total_revenue:.2f} €")

#05:Using function (def) to calculate employee revenue, then use it to calculate the total revenue of company

def calculate_employee_revenue(employee):
    employee_revenue = 0
    for order in employee["orders"]:
        employee_revenue += order
    return employee_revenue
    
total_revenue = 0

for department in company["departments"]:
    for employee in department["employees"]:
        employee_revenue = calculate_employee_revenue(employee)
        total_revenue += employee_revenue

print(f"Total company revenue : {total_revenue:.2f} €")

