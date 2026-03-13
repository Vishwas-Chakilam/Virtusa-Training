# Day 30: DB Design and Normalization

## Normalization
Database normalization is the process of structuring a relational database to reduce data redundancy and improve data integrity.

### 1NF (First Normal Form)
- A table is in 1NF if it contains no repeating groups and all columns hold atomic values.
- There must be a Primary Key.

### 2NF (Second Normal Form)
- Must be in 1NF.
- Contains no partial dependencies (i.e., no non-prime attribute depends on a part of a composite primary key).

### 3NF (Third Normal Form)
- Must be in 2NF.
- Contains no transitive dependencies (i.e., non-prime attributes must depend directly on the primary key).

### BCNF (Boyce-Codd Normal Form)
- Must be in 3NF.
- For any dependency `A -> B`, `A` should be a super key.

## Creating ER Diagram Modeling
- **Entities**: Represented by rectangles (e.g., Student, Course).
- **Attributes**: Represented by ellipses (e.g., Name, ID).
- **Relationships**: Represented by diamond shapes indicating relationships between entities (e.g., Enrolls).
