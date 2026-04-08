-- Cross Join: Returns Cartesian product (Every employee matched with every department)
SELECT e.EmpName, d.DeptName
FROM Employees e
CROSS JOIN Departments d;

-- Self Join: Joining a table to itself
CREATE TABLE Staff (
    StaffID INT PRIMARY KEY,
    Name VARCHAR(50),
    ManagerID INT
);

-- Find the manager of each staff member
SELECT e.Name AS Employee, m.Name AS Manager
FROM Staff e
LEFT JOIN Staff m ON e.ManagerID = m.StaffID;