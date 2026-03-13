-- View: A virtual table based on a query
CREATE VIEW v_EmployeeDetails AS
SELECT e.EmpName, d.DeptName, e.Salary
FROM Employees e
JOIN Departments d ON e.DeptID = d.DeptID;

-- Stored Procedure: Reusable SQL code block
DELIMITER //
CREATE PROCEDURE GetEmployeesByDept(IN p_DeptID INT)
BEGIN
    SELECT * FROM Employees WHERE DeptID = p_DeptID;
END //
DELIMITER ;

-- Call Procedure
CALL GetEmployeesByDept(2);