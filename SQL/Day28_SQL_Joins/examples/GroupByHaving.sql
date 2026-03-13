SELECT Department, COUNT(*) as EmployeeCount
FROM Employees
GROUP BY Department
HAVING COUNT(*) > 5;