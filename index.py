salary = float(input("Enter the employee's salary: "))

insurance = salary * 0.07
tax = salary * 1/100
final_salary = salary - insurance - tax

print("Employee's Salary: $", final_salary)
