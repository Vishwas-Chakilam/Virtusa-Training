-- Select all
SELECT * FROM Users;

-- Select specific columns
SELECT Username, Email FROM Users;

-- Filtering
SELECT Username FROM Users WHERE LastLogin IS NULL;
