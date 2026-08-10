#Expense Tracker
expenses=[250,1200,450,800,150,2000,350]
total_expenses=sum(expenses)
average_expense=total_expenses/len(expenses)
highest_expenses=max(expenses)
lowest_expenses=min(expenses)
above_500=0
below_equal_500=0
for expense in expenses:
    if expense>500:
        above_500=above_500+1
    else:
        below_equal_500=below_equal_500+1
print("Total Expenses: ",total_expenses)
print("Average Expense: ",average_expense)
print("Highest Expense: ",highest_expenses)
print("Lowest Expense: ",lowest_expenses)
print("Above 500: ",above_500)
print("Below Equal to 500: ",below_equal_500)
print("Expenses Above Average:")
for expense in expenses:
    if expense>average_expense:
        print(expense)
