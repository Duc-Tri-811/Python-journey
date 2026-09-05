#Exercise 04: Business example

budget = 1000
expense = 150
number_expenses = 0
remaining_budget = budget

while remaining_budget > expense:
    number_expenses += 1
    remaining_budget -= expense
    
print(f"Number of expenses: {number_expenses}")
print(f"Remaining budget: {remaining_budget:.2f} €")