-- UNION: Combines results, removing duplicates
SELECT City FROM Customers
UNION
SELECT City FROM Suppliers;

-- UNION ALL: Combines results, keeping duplicates
SELECT City FROM Customers
UNION ALL
SELECT City FROM Suppliers;

-- INTERSECT: Returns only common records (supported in some dialects like Postgres/SQL Server)
SELECT City FROM Customers
INTERSECT
SELECT City FROM Suppliers;