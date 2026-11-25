"""
Foreign Key in MySQL
A Foreign Key is a key used to create a relationship between two tables.

It refers to the Primary Key of another table.

In simple words, a foreign key connects two tables and maintains referential integrity.
1. Example
Suppose we have two tables:

Department table (Parent table)
dept_id (PK)	department
1	               IT
2	               HR
3	               Sales

Employee table (Child table)
emp_id (PK)	name	dept_id (FK)
101	         Ann	1
102	         Rahul	2
103        	 Manu	1

Here:
- dept_id in the Department table is the Primary Key.
- dept_id in the Employee table is the Foreign Key.
- The foreign key connects the employee with their department.

2. How to create a Foreign Key?
-- Create parent table
CREATE TABLE department (
    dept_id INT PRIMARY KEY,
    department VARCHAR(50)
);

-- Create child table
CREATE TABLE employee (
    emp_id INT PRIMARY KEY,
    name VARCHAR(50),
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES department(dept_id)
);


3. Explanation of each keyword
Keyword	Meaning
FOREIGN KEY	Defines a foreign key.
REFERENCES	Specifies the parent table.
department	Parent table name.
dept_id	Column being referenced.
PRIMARY KEY	Uniquely identifies each record.

4. Important rules
1. A foreign key can contain duplicate values.
2. A foreign key can contain NULL values unless NOT NULL is specified.
3. A foreign key must reference a primary key or a suitable unique key.
4. You cannot insert a foreign key value that does not exist in the referenced parent key (unless it is NULL).
5. One table can have multiple foreign keys.
5. Difference between Primary Key and Foreign Key
Primary Key	Foreign Key
Uniquely identifies each row.	Connects two tables.
Cannot contain NULL.	Can contain NULL (if allowed).
Cannot contain duplicates.	Can contain duplicates.
Identifies records in its own table.	References a key in another table.

Remember for exam
Primary Key = Unique identification

Foreign Key = Relationship between tables

Would you like to learn ON DELETE CASCADE and ON UPDATE CASCADE too? These are commonly asked in MySQL practical exams.




===========================================================================================================================================

-- JOIN:
-- JOIN is used to combine rows from two or more tables
-- based on a related column (Primary Key and Foreign Key).

-- 1. INNER JOIN:
-- Displays only matching records from both tables.
-- Example: Employee name and department name.

-- 2. LEFT JOIN:
-- Displays all records from the left table and matching
-- records from the right table. If no match, NULL is displayed.

-- 3. RIGHT JOIN:
-- Displays all records from the right table and matching
-- records from the left table. If no match, NULL is displayed.

-- 4. FULL OUTER JOIN:
-- Displays all records from both tables, including matching
-- and non-matching records.
-- MySQL uses LEFT JOIN + RIGHT JOIN with UNION.

-- 5. CROSS JOIN:
-- Displays all possible combinations of records from both tables.

-- 6. SELF JOIN:
-- Joins a table with itself.




"""