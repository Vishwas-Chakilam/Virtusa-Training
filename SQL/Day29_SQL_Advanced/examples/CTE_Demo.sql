-- CTE (Common Table Expression): Temporary named result set
WITH HighEarners AS (
    SELECT EmpID, EmpName, Salary
    FROM Employees
    WHERE Salary > 75000
)
SELECT * FROM HighEarners;