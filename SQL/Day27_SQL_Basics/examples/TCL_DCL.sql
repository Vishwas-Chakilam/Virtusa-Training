-- DCL commands
GRANT SELECT, INSERT ON Users TO 'readonly_user'@'localhost';
REVOKE INSERT ON Users FROM 'readonly_user'@'localhost';

-- TCL commands
START TRANSACTION;
INSERT INTO Users (Username) VALUES ('TransactionUser');
SAVEPOINT sp1;
UPDATE Users SET Username = 'ModifiedUser' WHERE Username = 'TransactionUser';
ROLLBACK TO sp1; -- Reverts the UPDATE
COMMIT; -- Saves the INSERT permanently