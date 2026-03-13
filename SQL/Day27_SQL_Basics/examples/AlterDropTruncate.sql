-- Add a new column
ALTER TABLE Users ADD COLUMN PhoneNumber VARCHAR(15);

-- Modify an existing column
ALTER TABLE Users MODIFY COLUMN PhoneNumber VARCHAR(20);

-- Drop a column
ALTER TABLE Users DROP COLUMN PhoneNumber;

-- Truncate Table (Removes all records but keeps structure)
TRUNCATE TABLE Users;