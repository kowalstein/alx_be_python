# This script calculates user's monthly savings.

monthly_income = eval (input ("Enter your monthly income: "))
monthly_expenses = eval (input ("Enter your total monthly expenses: "))
# user input

monthly_savings = monthly_income - monthly_expenses
# monthly savings

projected_savings = int(monthly_savings * 12 + (monthly_savings * 12 * 0.05))
# projected savings given an interest rate of 5%

print ("Your monthly savings are $" + str(monthly_savings))
print ("Projected savings after one year, with interest, is: $" + str(projected_savings))
