# Day 29: Advanced SQL Concepts

## Subqueries (Nested Queries)
A subquery is a SQL query nested inside a larger query.
It can be used in `SELECT`, `FROM`, `WHERE`, and `HAVING` clauses.
- **Correlated Subquery**: A subquery that uses values from the outer query. It's evaluated once for each row processed by the outer query.
- **Non-Correlated Subquery**: Can be evaluated independently of the outer query.

## Window Functions
Perform calculations across a set of table rows that are somehow related to the current row. Does not collapse the rows like `GROUP BY`.
- `ROW_NUMBER()`: Assigns a sequential row number starting with 1 to each row.
- `RANK()`: Assigns a rank to every row within a partition. Leaves gaps.
- `DENSE_RANK()`: Ranks items without leaving gaps in ranking values.
- Supported clauses: `OVER(PARTITION BY col1 ORDER BY col2)`.
