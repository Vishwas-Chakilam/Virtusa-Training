# Day 26: RDBMS Concepts

## Introduction to Database Systems
A database is an organized collection of structured information, or data, typically stored electronically in a computer system. 
A DBMS controls the data. A Relational Database Management System (RDBMS) is a DBMS that is based on the relational model.

## Core Concepts
1. **Tables/Relations**: Collections of related data entries structured as rows and columns.
2. **ACID Properties**: 
   - **Atomicity**: All or nothing transaction.
   - **Consistency**: The database must remain in a consistent state before and after the transaction.
   - **Isolation**: Concurrent transactions shouldn't interfere with each other.
   - **Durability**: Once a transaction has been committed, it will remain so, even in the event of power loss.

## Keys
Using keys, a database management system can guarantee referential integrity and uniqueness.
- **Primary Key**: Unique identifier for a given record.
- **Foreign Key**: A column or group of columns that provides a link between data in two tables.
- **Unique Key**: Evaluates to true if all the values corresponding to that constraint are unique.
- **Composite Key**: Consists of multiple columns acting together as the primary identifier.
