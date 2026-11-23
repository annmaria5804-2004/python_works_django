# SQL(structured query lanaguage)=======19th nov 2026========================
#=====================================================================================================
"""
SQL----
> used to communicate with the database to store and process the data.
> SQL (Structured Query Language) is a standard programming language used to communicate with relational databases.
> It is used to store, retrieve, insert, update and delete data.
>Example: We can use SQL to manage student details, employee records, product information, etc.
>data is the facts or values that can be stores or processed
-----------------------------------------------------------------------------------------------------------------------------------

2. What is a Database?
A database is an organized collection of data that can be easily accessed, managed and updated.
Examples: Student database, Employee database.
---------------------------------------------------------------------------------------------------------------------------------------------

3. What is a Table?
A table stores data in the form of rows and columns.
> record means one complete student record
> column and row means one atttribute like name... 
Example:
ID	Name	  Age
-------------------------
1	Ann    	  22
2	Anu	      23
3	Arun	  24
-----------------------------------------------------------------------------

4. Important SQL Commands
SQL commands are divided into five categories:
Category	          Full form	               Purpose
===========================================================================
DDL	          Data Definition Language	    Defines database structure
DML     	  Data Manipulation Language	Modifies data
DQL	          Data Query Language	        Retrieves data
DCL	          Data Control Language	        Controls permissions
TCL	          Transaction Control Language	Manages transactions
--------------------------------------------------------------------------------------------------

5. Important SQL Commands
DDL
- CREATE - Creates a table or database.
- ALTER - Modifies table structure.
- DROP - Deletes a table or database.
- TRUNCATE - Deletes all records from a table.
DML
- INSERT - Adds new records.
- UPDATE - Modifies existing records.
- DELETE - Deletes records.
DQL

- SELECT - Retrieves data.

DCL
- GRANT - Gives permissions.
- REVOKE - Removes permissions.
TCL
- COMMIT - Saves changes.
- ROLLBACK - Reverts uncommitted changes.
- SAVEPOINT - Creates a point to which a transaction can be rolled back.
---------------------------------------------------------------------------------------------------------------

# 6. Basic SQL Examples
# Create a table:
CREATE TABLE students (
    id INT,
    name VARCHAR(50),
    age INT
);


# Insert data:
INSERT INTO students
VALUES (1, 'Ann', 22);


# Display all records:
SELECT * FROM students;


# Display only names:
SELECT name FROM students;


# Update a record:
UPDATE students
SET age = 23
WHERE id = 1;


# Delete a record:
DELETE FROM students
WHERE id = 1;
==============================================================================================

1. Structured Data:
Structured data is data that is organized in a fixed format of rows and columns, usually stored in tables or relational databases.
Examples:
- Student details
- Employee records
- Bank transactions
- Customer information
Features:
- Organized in rows and columns.
- Has a predefined structure (schema).
- Easy to search, filter and analyze.
- Commonly stored in SQL databases such as MySQL.

2. Unstructured Data
Unstructured data is data that does not follow a fixed format or predefined structure.
Examples:
- Images
- Videos
- Audio files
- Emails
- PDF documents
- Social media posts
Features:
- No fixed rows and columns.
- Does not follow a predefined table structure.
- More difficult to organize and analyze.
- Often stored in file systems, data lakes and other storage systems.

4. What about Semi-Structured Data?
There is also a third type called Semi-Structured Data.
It does not follow a strict table format but contains some organizational elements, such as tags or key-value pairs.
Examples:
- JSON
- XML
- HTML

===============================================================================================================================================
DBMS - Database Management System
1. What is DBMS?
DBMS stands for Database Management System.
A DBMS is software that helps users create, store, manage, retrieve, update and delete data in a database.
In simple words, DBMS acts as an interface between the user and the database.

Examples:
- MySQL
- Oracle Database
- PostgreSQL
- Microsoft SQL Server
- SQLite

2. Why do we use DBMS?
- To store data systematically.
- To retrieve data easily.
- To update and delete records.
- To maintain data security.
- To reduce data duplication.
- To maintain data consistency.

3. How does DBMS work?
1. User sends a request.
2. DBMS processes the request.
3. DBMS communicates with the database.
4. Database returns the requested information.

4. Types of DBMS
There are four major types:
Type	Explanation
Hierarchical DBMS	Stores data in a tree-like structure
Network DBMS	Stores data using interconnected relationships
Relational DBMS (RDBMS)	Stores data in tables (rows and columns)
Object-Oriented DBMS	Stores data as objects

Examples:
- Hierarchical - IBM IMS
- Network - IDMS
- Relational - MySQL, Oracle, PostgreSQL
- Object-oriented - ObjectDB
5. Difference between DBMS and RDBMS
DBMS	RDBMS
Database Management System	Relational Database Management System
Manages databases	Manages relational databases
May not use tables	Uses tables
Relationships are not mandatory	Relationships are maintained using keys
Example: XML-based database systems	MySQL, Oracle, PostgreSQL

6. Difference between DBMS and SQL
This is an important interview question.
- DBMS: Software used to manage databases.
- SQL: Language used to communicate with relational databases.

Remember for interview
- SQL = Language
- DBMS = Software to manage databases
- RDBMS = Relational database management software
- MySQL = RDBMS
- Database = Organized collection of data
- Table = Collection of rows and columns
==================================================================================================

3. RDBMS – Relational Database Management System
Meaning: RDBMS is a type of DBMS that stores data in tables (rows and columns) and allows relationships between tables.
Example:
Imagine two tables:
Student Table
Student_ID	Name
1	       Ann
2	       Anu

Course Table
Course_ID	Student_ID	Course
101	            1       Python
102          	2	    Java
Here, Student_ID connects the two tables.
Examples: MySQL, PostgreSQL, Oracle.
Remember: RDBMS stores data in related tables.
===============================================================================================================
4. MySQL
Meaning: MySQL is an RDBMS used to store, organize and manage data in tables.
For example, an online shopping application can use MySQL to store:
- Customer details.
- Product details.
- Orders.
- Payment information.
Remember: MySQL is database management software that uses SQL.
============================================================================================

1. MySQL
MySQL is an open-source Relational Database Management System (RDBMS) used to store, organize and manage data in tables (rows and columns).
- Uses SQL to communicate with the database.
- Commonly used in web applications.
- Example: Storing customer and product details in an e-commerce website.
Remember: MySQL is an RDBMS used to manage relational databases.

2. PostgreSQL
PostgreSQL is an open-source Object-Relational Database Management System (ORDBMS) used to store, manage and retrieve data.
- Uses SQL to communicate with the database.
- Supports complex queries and advanced data types.
- Commonly used in web applications and large-scale systems.
Remember: PostgreSQL is an advanced relational database system used to manage structured data.

3. MySQL vs PostgreSQL:
MySQL	                             PostgreSQL
-------------------------------------------------------------------------------
RDBMS	                               ORDBMS
Easy to learn and use	               Offers more advanced features
Popular for web applications	       Popular for complex applications
Open-source	                           Open-source


"""



#==============================================================================================================================
"""
1. Primary Key (PK)
Meaning: A Primary Key is a column (or combination of columns) that uniquely identifies each record in a table.

In simple words, it is a unique ID given to each person or record.

Example: Student Table
Student_ID (PK)	Name	Age
101	          Ann      22
102	          Anu      23
103	          Arun	   24

Here, Student_ID is the Primary Key.

Why?
- Every student has a different ID.
- Duplicate IDs are not allowed.
- NULL values are not allowed.
Remember: Primary Key = Unique identification of each record.

2. Foreign Key (FK)
Meaning: A Foreign Key is a column in one table that refers to the Primary Key of another table.
In simple words, it connects two tables.

Let's take two tables.

Student Table
Student_ID (PK)	Name
101	Ann
102	Anu
103	Arun

Course Table
Course_ID (PK)	Student_ID (FK)	Course
1	101	Python
2	102	Java
3	103	Django

Here:
- Student_ID in the Student table is the Primary Key.
- Student_ID in the Course table is the Foreign Key.
- It connects the Course table with the Student table.
Remember: Foreign Key = Connects two tables.

3. Unique Key
Meaning: A Unique Key ensures that all values in a column are different.

Example:
ID	Email(Unique Key)
1	ann@gmail.com
2	anu@gmail.com
3	arun@gmail.com
Here, email addresses cannot be duplicated.
Remember: Unique Key = Does not allow duplicate values.

Difference from Primary Key:
- A table can have only one Primary Key constraint.
- A table can have multiple Unique constraints.
- A Primary Key cannot contain NULL.
- A Unique constraint generally allows NULL, depending on the database system.

4. NOT NULL Constraint
Meaning: NOT NULL ensures that a column cannot have an empty NULL value.

Example:
ID	Name
1	Ann
2	Anu
3	NULL (Not allowed)

If we apply NOT NULL to the Name column, every record must have a name.
Remember: NOT NULL = Value is compulsory.

5. DEFAULT Constraint
Meaning: DEFAULT automatically assigns a predefined value if the user does not provide a value.
Example:
Suppose every new student has the default status "Active".
Student_ID	Name	Status
101	Ann	Active
102	Anu	Active

If we don't provide the status, the database automatically inserts Active.
Remember: DEFAULT = Automatically assigns a predefined value.

6. CHECK Constraint
Meaning: CHECK ensures that the values entered into a column satisfy a specified condition.
Example:
A student's age must be greater than or equal to 18.
CREATE TABLE students (
    id INT,
    name VARCHAR(50),
    age INT CHECK (age >= 18)
);

- Age 22 → Allowed.
- Age 16 → Not allowed.
Remember: CHECK = Checks whether a condition is satisfied.
7. Composite Key
Meaning: A Composite Key is a key created using two or more columns together to uniquely identify a record.

Example:
Student_ID	Course_ID
101	1
101	2
102	1

Here, Student_ID alone may repeat, and Course_ID alone may repeat.

But the combination of both can uniquely identify each record.

Remember: Composite Key = Combination of two or more columns used as a key.

8. Quick Comparison – Important for Interviews
Key / Constraint	Purpose
Primary Key	Uniquely identifies a record
Foreign Key	Connects two tables
Unique Key	Prevents duplicate values
NOT NULL	Prevents NULL values
DEFAULT	Assigns a default value
CHECK	Checks a condition
Composite Key	Combines multiple columns

9. Practical SQL Example
Let's create a student table using these concepts.
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    age INT CHECK (age >= 18),
    status VARCHAR(20) DEFAULT 'Active'
);


Here is what each constraint does:
- PRIMARY KEY → Student ID must be unique.
- NOT NULL → Name is compulsory.
- UNIQUE → Email cannot be duplicated.
- CHECK → Age must be 18 or above.
- DEFAULT → Status becomes Active if not provided.

"""