#Challenge

balance = 1000
monthly_expense = 180

def calculate_months_covered(balance, monthly_expense):
    number_monthly_expenses = 0
    while balance >= monthly_expense:
        number_monthly_expenses += 1
        balance -= monthly_expense
    return number_monthly_expenses, balance

months_covered, remaining_balance = calculate_months_covered(balance, monthly_expense)

print(f"Months covered: {months_covered}")
print(f"Remaining balance: {remaining_balance:.2f} €")