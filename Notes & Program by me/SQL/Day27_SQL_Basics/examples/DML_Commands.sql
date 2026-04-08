-- Insert Records
INSERT INTO Users (Username, Email) VALUES ('Alice', 'alice@test.com');
INSERT INTO Users (Username, Email) VALUES ('Bob', 'bob@test.com');

-- Update Record
UPDATE Users SET Username = 'Bob_updated' WHERE Email = 'bob@test.com';

-- Delete Record
DELETE FROM Users WHERE Username = 'Alice';
