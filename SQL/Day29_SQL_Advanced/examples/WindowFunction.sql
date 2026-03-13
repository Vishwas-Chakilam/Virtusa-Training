SELECT EmployeeName, Salary,
RANK() OVER (ORDER BY Salary DESC) as SalaryRank
FROM Employees;