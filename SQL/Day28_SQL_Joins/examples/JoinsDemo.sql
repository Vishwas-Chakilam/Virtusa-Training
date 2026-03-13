-- INNER JOIN
SELECT e.EmpName, d.DeptName 
FROM Employees e
INNER JOIN Departments d ON e.DeptID = d.DeptID;

-- LEFT JOIN
SELECT e.EmpName, d.DeptName 
FROM Employees e
LEFT JOIN Departments d ON e.DeptID = d.DeptID;
