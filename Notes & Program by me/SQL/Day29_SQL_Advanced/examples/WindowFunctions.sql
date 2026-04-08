SELECT 
    EmpName, 
    DeptID, 
    Salary,
    ROW_NUMBER() OVER(PARTITION BY DeptID ORDER BY Salary DESC) as Rank_Row,
    RANK() OVER(PARTITION BY DeptID ORDER BY Salary DESC) as Rank_Rank
FROM Employees;
