-- Non-Correlated
SELECT EmpName, Salary
FROM Employees
WHERE Salary > (SELECT AVG(Salary) FROM Employees);

-- Correlated: Find employees whose salary is above their department's average
SELECT e.EmpName, e.Salary
FROM Employees e
WHERE e.Salary > (
    SELECT AVG(Salary) 
    FROM Employees d 
    WHERE d.DeptID = e.DeptID
);
