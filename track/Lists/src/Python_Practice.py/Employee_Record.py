employee=("Arjun","Developer",45000,3)
name,designation,monthly_salary,experience=employee
annual_salary=monthly_salary*12
if experience<2:
    bouns=annual_salary*0.05
elif experience<=5:
    bouns=annual_salary*0.10
else:
    bouns=annual_salary*0.15
total_salary=annual_salary+bouns
print("Employee Name: ",name)
print("Designation: ",designation)
print("Monthly Salary: ",monthly_salary)
print("Experience: ",experience)
print("Annual Salary: ",annual_salary)
print("Bouns: ",bouns)
print("Total Salary: ",total_salary)
'''
Output:
Employee Name:  Arjun
Designation:  Developer
Monthly Salary:  45000
Experience:  3
Annual Salary:  540000
Bouns:  27000.0
Total Salary:  567000.0
'''