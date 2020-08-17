mysql Assessment
---------------------
#### Q1. When you have a subquery inside of the main query, which query is executed first?
- [ ] The subquery is never executed. Only the main query is executed.
- [ ] They are executed at the same time
- [ ] the main query
- [x] the subquery

#### Q2. You need to export the entire database, including the database objects, in addition to the data. Which command-line tool do you use?
- [ ] mysqlexport
- [ ] mysqladmin
- [x] mysqldump
- [ ] mysqld

#### Q3. You must ensure the accuracy and reliability of the data in your database. You assign some constraints to limit the type of data that can go into a table. What type of constraints are you assigning?
- [ ] row level
- [ ] database level
- [x] column level
- [ ] function leve

#### Q4. Which option of most MySQL command-line programs can be used to get a description of the program's different options?
- [ ] --options
- [ ] ?
- [x] --help
- [ ] -h

#### Q5. MySQL uses environment variables in some of the programs and command-line operations. Which variable is used by the shell to find MySQL programs?
- [ ] DIR
- [ ] HOМЕ
- [x] PATH
- [ ] MYSQL_HOME

#### Q6. How can you create a stored procedure in MySQL?
- [ ] `-`
```
1 CREATE PROCEDURE P () AS 
2 BEGIN 
3 END;
```
- [x] `-`
```
1 CREATE PROCEDURE P ()
2 BEGIN 
3 END
```
- [ ] `-`
```
1 CREATE PROCP 
2 BEGIN 
3 END;
```
- [ ] `-`
```
1 CREATE PROC P AS O 
2 BEGIN
3 END;
```

#### Q7. If you were building a table schema to store student grades as a letter (A, B, C, D, or F) which column type would be the best choice?
- [x] ENUM
- [ ] OTEXT
- [ ] VARCHAR
- [ ] LONGTEXT

#### Q8. Management has requested that you build an employee database. You start with the employee table. What is the correct syntax?
- [ ] `-`
```
    1 CREATE TABLE employee (
    2 employee ID char(10), 
    3 firstName varchar(50), 
    4 lastName varchar(50), 
    5 phone varchar(20), 
    6 address varchar(50), 
    7 PRIMARY KEY ON employeeID 
    8 );
```
- [ ] `-`
```
    1 CREATE TABLE employee (
    2 employee ID char(10), 
    3 firstName varchar(50), 
    4 lastName varchar(50), 
    5 phone varchar(20),
    6 address varchar(50), 
    7 PRIMARY KEY employeeID 
    8 );
```
- [ ] `-`
```
    1 CREATE TABLE IF EXISTS employee ( 
    2 employee ID char(10), 
    3 firstName varchar(50), 
    4 lastName varchar(50), 
    5 phone varchar(20), 
    6 address varchar(50), 
    7 PRIMARY KEY (employeeID) 
    8 );
```
- [x] `-`
```
    1 CREATE TABLE IF NOT EXISTS employee (
    2 employee ID char(10), 
    3 firstName varchar(50), 
    4 lastName varchar(50), 
    5 phone varchar(20), 
    6 address varchar(50), 
    7 PRIMARY KEY (employeeID) 
    8 );
```

#### Q9. You are working with the tables as shown in this diagram. You need to generate the list of customers who purchased certain car models. Which SQL clause do you use?
- [ ] LIKE
- [x] IN
- [ ] BETWEEN
- [ ] HAVING

#### Q10. Which query would NOT be used to administer a MySQL server?
- [ ] USE db
- [x] SELECT column FROM tbl
- [ ] SHOW COLUMNS FROM tb1
- [ ] SHOW TABLES

#### Q11. What is the product of the database designing phase?
- [ ] system definition
- [x] logical model
- [ ] physical model
- [ ] normalized database
NOT SURE THE QUESTION IS CORRECT. Logical, physical and normalised are all products of the designing phase in this order.

#### Q12. MySQL server can operate in different SQL modes, depending on the value of the sql_mode system variable. Which mode changes syntax and behavior to conform more closely to standard SQL?
- [ ] TRADITIONAL
- [x] ANSI
- [ ] MSSQL
- [ ] STRICT

#### Q13. MySQL programs are a set of command-line utilities that are provided with typical MySQL distributions. MySQL is designed to be a database.
- [ ] database and programming
- [ ] user and administrator
- [x] client and server
- [ ] syntax and objects

#### Q14. Which MySQL command shows the structure of a table?
- [ ] INFO table;
- [ ] SHOW table;
- [ ]  STRUCTURE table;
- [x]  DESCRIBE table;

#### Q15. MySQL uses security based on_____for all connections, queries, and other operations that users can attempt to perform.
- [x]  administrator schema
- [ ] encrypted algorithms
- [ ] user settings
- [x] access control lists

#### Q16. Which MySQL command modifies data records in a table?
- [x] UPDATE
- [ ] MODIFY
- [ ] CHANGE
- [ ] ALTER

#### Q17. What is the best type of query for validating the format of an email address in a MySQL table?
- [ ] a SQL query using partitions
- [ ] a SQL query using IS NULL
- [x] a SQL query using a regular expression
- [ ] a SQL query using LTRIM Or RTRIM

#### Q18. In MySQL, queries are always followed by what character?
- [ ] line break
- [ ] colon
- [x] semicolon
- [ ] period

#### Q19. How can you remove a record using MySQL?
- [ ] DELETE
- [x] DELETE FROM
- [ ] REMOVE
- [ ] REMOVE FROM

#### Q20. Which choice is NOT a statement you would use to filter data?
- [x] GROUP_BY
- [ ] WHERE
- [ ] LIMIT
- [ ] LIKE

#### Q21. What does the following SQL statement return?
  `SELECT * FROM Employees WHERE EmployeeName LIKE 'a%'`
- [ ] It records in the Employees table where the value in the EmployeeName column doesn't have an "a".
- [x] It records in the Employees table where the value in the EmployeeName column starts with "a".
- [ ] It records in the Employees table where the value in the EmployeeName column has an "a".
- [ ] It records in the Employees table where the value in the EmployeeName column ends with "a".

#### Q22. In `SELECT * FROM clients;` what does clients represent?
- [ ] a SQL query
- [ ] a SQL statement
- [ ] a database
- [x] a table

#### Q23. How does MySQL differ from SQL?
- [ ] SQL is a standard language for retrieving and manipulating data from structured databases. MySQL is a nonrelational database management system that is used to manage SQL databases.
- [x] SQL is a standard language for retrieving and manipulating data from structured databases. MySQL is a relational database management system that is used to manage SQL databases.
- [ ] They are not different. MySQL and SQL refer to the same thing.
- [ ] My SQL is a language, and SQL is a software application.

#### Q24. If you need to order a table of movies by name, which query will work?
- [ ] SELECT * FROM movies GROUP BY name
- [x] SELECT * FROM movies ORDER BY name
- [ ] SELECT * FROM movies ORDER TABLE by name
- [ ] SELECT * FROM movies FILTER BY name

#### Q25. A trigger is a database object that is associated with a table, and that activates when a particular event occurs for the table. Which three events are these?
- [x] INSERT, UPDATE, DELETE
- [ ] CREATE, ALTER, DROP
- [ ] OPEN, FETCH, CLOSE
- [ ] DECLARE, SET, SELECT

#### Q26. You are working with very large tables in your database. Which SQL clause do you use to prevent exceedingly large query results?
- [ ] UNIQUE
- [x] LIMIT
- [ ] DISTINCT
- [ ] CONSTRAINT

#### Q27. What is the default port for MySQL Server?
- [ ] 25
- [ ] 990
- [ ] 0
- [x] 3306

#### Q28. How can you filter duplicate data while retrieving records from a table?
- [x] DISTINCT
- [ ] WHERE
- [ ] LIMIT
- [ ] AS

#### Q29. What is the difference between DROP and TRUNCATE?
- [ ] They both refer to the same operation of deleting the table completely.
- [ ] They both refer to the same operation of clearing the table, but keeping its definition intact.
- [ ] TRUNCATE deletes table completely, removing its definition as well. DROP clears the table but does not delete the definition.
- [x] DROP deletes table completely, removing its definition as well. TRUNCATE clears the table but does not delete the definition.

#### Q30. How do you select every row in a given table named "inventory"?
- [ ] SELECT all FROM inventory;
- [ ] FROM inventory SELECT all;
- [ ] FROM inventory SELECT *;
- [x] SELECT * FROM inventory;

#### Q31. In an efficiently designed relational database, what does every table have?
- [ ] set of triggers
- [ ] sequential id field
- [ ] minimum of three columns
- [x] primary key

#### Q32. MySQL option files provide a way to specify commonly used options so that they need not be entered on the command line each time you run a program. What is another name for the option files?
- [ ] variable settings
- [x] configuration files
- [ ] help files
- [ ] default settings

#### Q33. After installing MySQL, it may be necessary to initialize the __ which may be done automatically with some MySQL installation methods.
- [ ] storage engine
- [ ] user accounts
- [ ] grant tables
- [x] data directory

#### Q34. You need to export the data in the customers table into a CSV file, with columns headers in the first row. Which clause do you add to your MySQL command? 
- [ ] JOIN
- [ ] WITH HEADERS
- [x] UNION
- [ ] WITH COLUMNS

#### Q35. One form of backup, replication, enables you to maintain identical data on multiple servers, as a ___ configuration. 
- [ ] remote-local
- [ ] parent-child
- [x] master-slave
- [ ] logical-physical

#### Q36. What is the requirement for using a subquery in the SELECT clause? 
- [ ] the subquery must use an aggregate function.
- [ ] the subquery must refer to the same table as the main query.
- [x] the subquery must return a single value.
- [ ] the subquery must return at least one value.

#### Q37. Each time MySQL is upgraded, it is best to execute mysql_upgrade, which looks for incompatibilities with the upgraded MySQL server. What does this command do, upon finding a table with a possible incompatibility? 
- [x] it performs a table check and, if problems are found, attempts a table repair.
- [ ] it stops and notifies the server administrator that the upgrade cannot complete until the incompatibility issue are resolved.
- [ ] it provides a full report of the table specifications and the incompatibilities to the server administrator.
- [ ] it performs a table check and, if problems are found, displays the information for the server administrator to take action.
