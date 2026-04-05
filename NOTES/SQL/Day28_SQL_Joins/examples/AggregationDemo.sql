-- Group By
SELECT DeptID, COUNT(*) AS EmployeeCount, AVG(Salary) AS AverageSalary
FROM Employees
GROUP BY DeptID;

-- Having Clause
SELECT DeptID, AVG(Salary) AS AverageSalary
FROM Employees
GROUP BY DeptID
HAVING AVG(Salary) > 60000;
