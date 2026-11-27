# MYSQL
#-------------------
# database Name
# table Name
# column

"""
creta database <databasename>
students (# table name)
ID name age email course status
int char decimal bool..



"""
# code:
# -- 1. Create database
# CREATE DATABASE details;

# -- 2. Select database
# USE details;

# -- 3. Create students table
# CREATE TABLE students (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(100) not null,
#     age INT check(age > 18) not null,
#     gender enum("male", "female", "others") not null,
#     email VARCHAR(100) unique not null,
#     course varchar(100) default "django",
#     place VARCHAR(100) not null,
#     status enum("active", "dropped") default "active"
# );
# show tables from details;


# Explanation (simple):
# SQL statement	Meaning
# CREATE DATABASE details;	Creates a database named details
# USE details;	Selects the database
# CREATE TABLE students	Creates a table named students
# id INT	ID stores integer values
# AUTO_INCREMENT	Automatically increases ID (1, 2, 3...)
# PRIMARY KEY	Makes ID unique; no duplicate or NULL IDs
# VARCHAR(100)	Stores text up to 100 characters
#----------------------------------------------------------------------------------

# 2. Explanation of each constraint
# Constraint	Simple meaning
# PRIMARY KEY	Doesn't allow duplicate or NULL IDs
# AUTO_INCREMENT	Automatically generates ID numbers
# NOT NULL	Cannot leave the value empty
# CHECK(age > 18)	Age must be greater than 18

#===============================================================================================================================
#======================================================================================================================
# 1. Explanation of your SQL code
# Column	Meaning
# id INT AUTO_INCREMENT PRIMARY KEY	Automatically generates a unique ID for each student.
# name VARCHAR(100) NOT NULL	Student name is mandatory. Maximum 100 characters.
# age INT CHECK(age > 18) NOT NULL	Age must be greater than 18. Cannot be NULL.
# gender ENUM(...) NOT NULL	Only male, female or others are allowed.
# email VARCHAR(100) UNIQUE NOT NULL	Email is mandatory and cannot be repeated.
# course VARCHAR(100) DEFAULT 'django'	If no course is provided, Django is automatically assigned.
# place VARCHAR(100) NOT NULL	Student's place is mandatory.
# status ENUM(...) DEFAULT 'active'	Default status is active. Can be active or dropped.

# ----------------------------------------------------------------------------------------------------------------------
# 2. Important SQL concepts used
# Concept	Simple meaning
# PRIMARY KEY	Uniquely identifies each row.
# AUTO_INCREMENT	Automatically increases the ID.
# NOT NULL	Cannot leave the value empty (NULL).
# UNIQUE	Does not allow duplicate values.
# CHECK	Applies a condition to the value.
# ENUM	Allows only specified values.
# DEFAULT	Automatically assigns a value if nothing is provided.

# ------------------------------------------------------------------------------------------
# Interview tip: Remember these three differences:
# - PRIMARY KEY = Unique + NOT NULL.
# - UNIQUE = No duplicate values.
# - NOT NULL = Value is compulsory.
#Explanation:
# - SHOW TABLES – Displays all tables in a database.
# - FROM details – Specifies the database name.
# Expected output:
#=============================vvimp=========================================================

# select : To fetch specific columns from a table

# where: to apply a condition

# and : to satisfy multiple condiiton

# or :to satisfy any condition

# in : to satisfy from any given

# between : used to get the elements from a range

# order by asc > to sort the result in ascending

# order by dese >> sort in descending

# limit >> limit the number of rows displaying

# ================================================================================================

# aggregate functions
#---------------------------------------
# count(),>> count the records
# avg(),>REturn the average
# min(),>>return the record has
# minimum value
# max()>>return the record has
# maximum value
# sum()>> return the sum of
# values

#groupby
#-------------------------------
# used to group records
# based on a common
# column value

#====================================================================================================
"""
Keyword	Meaning	Use
SELECT	Selects columns	Specifies which columns to display.
department	Column name	Displays the department name.
MAX()	Aggregate function	Finds the highest value.
salary	Column name	Finds the highest salary.
AS	Alias	Gives a temporary name to a column.
maximum_salary	Alias name	Displays MAX(salary) under this name.
FROM	Table selection	Specifies the table from which data is retrieved.
employee	Table name	Retrieves data from the employee table.
GROUP BY	Grouping	Groups employees department-wise.
;	Statement terminator	Indicates the end of the SQL query.
---------------------------------------------------------------------------------------------------
Keyword	Meaning	Use
SELECT	Selects columns	Specifies what to display.
place	Column name	Displays employee locations.
COUNT()	Aggregate function	Counts the number of records.
*	All rows	Counts all rows in each group.
AS	Alias	Gives a temporary name.
employee_count	Alias name	Displays the count under this name.
FROM	Table selection	Specifies the source table.
employee	Table name	Retrieves employee records.
GROUP BY	Grouping	Groups employees according to their place.
ORDER BY	Sorting	Arranges the result.
DESC	Descending	Sorts from highest to lowest.

--------------------------------------------------------------------------------------------------------
Important SQL keywords to remember
Keyword	Full meaning / purpose
MAX()	Highest value
MIN()	Lowest value
SUM()	Total value
AVG()	Average value
COUNT()	Number of records
GROUP BY	Groups similar values
ORDER BY	Sorts the results
ASC	Ascending order
DESC	Descending order
AS	Temporary column/table name
WHERE	Filters individual rows
HAVING	Filters grouped results


"""
# structure of databse means database name table name then what inside the table and what functions we create.
