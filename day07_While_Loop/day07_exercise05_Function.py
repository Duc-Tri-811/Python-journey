#Exercise 05: Business example

budget = 1000
expense = 150

def calculate_expense_count(budget, expense):
    
    number_expenses = 0
    while budget >= expense:
        number_expenses += 1
        budget -= expense
    return number_expenses
    
result = calculate_expense_count(budget, expense)

print(f"Number of expenses: {result}")
