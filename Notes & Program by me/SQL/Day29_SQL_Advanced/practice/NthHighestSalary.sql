-- Using Subquery for 2nd highest:
SELECT MAX(Salary)
FROM Employees
WHERE Salary < (SELECT MAX(Salary) FROM Employees);

-- Using DENSE_RANK()
SELECT result.Salary 
FROM (
    SELECT Salary, DENSE_RANK() OVER (ORDER BY Salary DESC) as rnk 
    FROM Employees
) result
WHERE result.rnk = 2;
