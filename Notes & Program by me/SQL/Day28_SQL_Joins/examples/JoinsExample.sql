SELECT e.FirstName, d.DepartmentName 
FROM Employees e 
INNER JOIN Departments d ON e.DepartmentID = d.DepartmentID;
