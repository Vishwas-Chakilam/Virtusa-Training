# Day 28: SQL Joins and Aggregation

## Joins
A `JOIN` clause is used to combine rows from two or more tables, based on a related column between them.
- **INNER JOIN**: Returns records that have matching values in both tables.
- **LEFT (OUTER) JOIN**: Returns all records from the left table, and the matched records from the right table.
- **RIGHT (OUTER) JOIN**: Returns all records from the right table, and the matched records from the left table.
- **FULL (OUTER) JOIN**: Returns all records when there is a match in either left or right table.
- **CROSS JOIN**: Returns the Cartesian product of the sets of records from the two joined tables.

## Group By and Aggregate Functions
The `GROUP BY` statement groups rows that have the same values into summary rows.
Usually used with aggregate functions (`COUNT()`, `MAX()`, `MIN()`, `SUM()`, `AVG()`).
The `HAVING` clause is used with filter conditions on aggregated values (since `WHERE` doesn't work on aggregates).
