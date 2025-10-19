## MySQL

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
- [ ] function level

#### Q4. Which option of most MySQL command-line programs can be used to get a description of the program's different options?

- [ ] --options
- [ ] ?
- [x] --help
- [ ] -h

#### Q5. MySQL uses environment variables in some of the programs and command-line operations. Which variable is used by the shell to find MySQL programs?

- [ ] DIR
- [ ] HOME
- [x] PATH
- [ ] MYSQL_HOME

#### Q6. How can you create a stored procedure in MySQL?

- [ ] A

```
1 CREATE PROCEDURE P () AS
2 BEGIN
3 END;
```

- [x] B

```
1 CREATE PROCEDURE P ()
2 BEGIN
3 END
```

- [ ] C

```
1 CREATE PROCP
2 BEGIN
3 END;
```

- [ ] D

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

- [ ] A

```sql
    CREATE TABLE employee (
    employeeID char(10),
    firstName varchar(50),
    lastName varchar(50),
    phone varchar(20),
    address varchar(50),
    PRIMARY KEY ON employeeID
    );
```

- [ ] B

```sql
    CREATE TABLE employee (
    employeeID char(10),
    firstName varchar(50),
    lastName varchar(50),
    phone varchar(20),
    address varchar(50),
    PRIMARY KEY employeeID
    );
```

- [ ] C

```sql
    CREATE TABLE IF EXISTS employee (
    employeeID char(10),
    firstName varchar(50),
    lastName varchar(50),
    phone varchar(20),
    address varchar(50),
    PRIMARY KEY (employeeID)
    );
```

- [x] D

```sql
    CREATE TABLE IF NOT EXISTS employee (
    employeeID char(10),
    firstName varchar(50),
    lastName varchar(50),
    phone varchar(20),
    address varchar(50),
    PRIMARY KEY (employeeID)
    );
```

#### Q9. You are working with the tables as shown in this diagram. You need to generate the list of customers who purchased certain car models. Which SQL clause do you use?

![mysql Q09](images/mysql_q09.jpg?raw=true)

- [ ] LIKE
- [x] IN
- [ ] BETWEEN
- [ ] HAVING

#### Q10. Which query would NOT be used to administer a MySQL server?

- [ ] USE db
- [x] SELECT column FROM tbl
- [ ] SHOW COLUMNS FROM tbl
- [ ] SHOW TABLES

#### Q11. MySQL server can operate in different SQL modes, depending on the value of the sql_mode system variable. Which mode changes syntax and behavior to conform more closely to standard SQL?

- [ ] TRADITIONAL
- [x] ANSI
- [ ] MSSQL
- [ ] STRICT

#### Q12. MySQL programs are a set of command-line utilities that are provided with typical MySQL distributions. MySQL is designed to be a database.

- [ ] database and programming
- [ ] user and administrator
- [x] client and server
- [ ] syntax and objects

#### Q13. Which MySQL command shows the structure of a table?

- [ ] INFO table;
- [ ] SHOW table;
- [ ] STRUCTURE table;
- [x] DESCRIBE table;

#### Q14. MySQL uses security based on \_ for all connections, queries, and other operations that users can attempt to perform. or How are permissions implemented in MySQL?

- [ ] administrator schema
- [ ] encrypted algorithms
- [ ] user settings
- [x] access control lists

[Reference](https://dev.mysql.com/doc/refman/8.0/en/security-guidelines.html)

#### Q15. Which MySQL command modifies data records in a table?

- [x] UPDATE
- [ ] MODIFY
- [ ] CHANGE
- [ ] ALTER

#### Q16. What is the best type of query for validating the format of an email address in a MySQL table?

- [ ] a SQL query using partitions
- [ ] a SQL query using IS NULL
- [x] a SQL query using a regular expression
- [ ] a SQL query using LTRIM Or RTRIM

#### Q17. In MySQL, queries are always followed by what character?

- [ ] line break
- [ ] colon
- [x] semicolon
- [ ] period

#### Q18. How can you remove a record using MySQL?

- [ ] DELETE
- [x] DELETE FROM
- [ ] REMOVE
- [ ] REMOVE FROM

#### Q19. Which choice is NOT a statement you would use to filter data?

- [x] GROUP BY
- [ ] WHERE
- [ ] LIMIT
- [ ] LIKE

#### Q20. What does the following SQL statement return?

`SELECT * FROM Employees WHERE EmployeeName LIKE 'a%'`

- [ ] It records in the Employees table where the value in the EmployeeName column doesn't have an "a".
- [x] It records in the Employees table where the value in the EmployeeName column starts with "a".
- [ ] It records in the Employees table where the value in the EmployeeName column has an "a".
- [ ] It records in the Employees table where the value in the EmployeeName column ends with "a".

#### Q21. In `SELECT * FROM clients;` what does clients represent?

- [ ] a SQL query
- [ ] a SQL statement
- [ ] a database
- [x] a table

#### Q22. How does MySQL differ from SQL?

- [ ] SQL is a standard language for retrieving and manipulating data from structured databases. MySQL is a nonrelational database management system that is used to manage SQL databases.
- [x] SQL is a standard language for retrieving and manipulating data from structured databases. MySQL is a relational database management system that is used to manage SQL databases.
- [ ] They are not different. MySQL and SQL refer to the same thing.
- [ ] My SQL is a language, and SQL is a software application.

#### Q23. If you need to order a table of movies by name, which query will work?

- [ ] SELECT \* FROM movies GROUP BY name
- [x] SELECT \* FROM movies ORDER BY name
- [ ] SELECT \* FROM movies ORDER TABLE by name
- [ ] SELECT \* FROM movies FILTER BY name

#### Q24. A trigger is a database object that is associated with a table, and that activates when a particular event occurs for the table. Which three events are these?

- [x] INSERT, UPDATE, DELETE
- [ ] CREATE, ALTER, DROP
- [ ] OPEN, FETCH, CLOSE
- [ ] DECLARE, SET, SELECT

[Reference](https://dev.mysql.com/doc/refman/5.7/en/triggers.html)

#### Q25. You are working with very large tables in your database. Which SQL clause do you use to prevent exceedingly large query results?

- [ ] UNIQUE
- [x] LIMIT
- [ ] DISTINCT
- [ ] CONSTRAINT

#### Q26. What is the default port for MySQL Server?

- [ ] 25
- [ ] 990
- [ ] 0
- [x] 3306

#### Q27. How can you filter duplicate data while retrieving records from a table?

- [x] DISTINCT
- [ ] WHERE
- [ ] LIMIT
- [ ] AS

#### Q28. What is the difference between DROP and TRUNCATE?

- [ ] They both refer to the same operation of deleting the table completely.
- [ ] They both refer to the same operation of clearing the table, but keeping its definition intact.
- [ ] TRUNCATE deletes table completely, removing its definition as well. DROP clears the table but does not delete the definition.
- [x] DROP deletes table completely, removing its definition as well. TRUNCATE clears the table but does not delete the definition.

#### Q29. How do you select every row in a given table named "inventory"?

- [ ] SELECT all FROM inventory;
- [ ] FROM inventory SELECT all;
- [ ] FROM inventory SELECT \*;
- [x] SELECT \* FROM inventory;

#### Q30. In an efficiently designed relational database, what does every table have?

- [ ] set of triggers
- [ ] sequential id field
- [ ] minimum of three columns
- [x] primary key

#### Q31. MySQL option files provide a way to specify commonly used options so that they need not be entered on the command line each time you run a program. What is another name for the option files?

- [ ] variable settings
- [x] configuration files
- [ ] help files
- [ ] default settings

[Reference](https://dev.mysql.com/doc/refman/8.0/en/option-files.html)

#### Q32. After installing MySQL, it may be necessary to initialize the \_ which may be done automatically with some MySQL installation methods.

- [ ] storage engine
- [ ] user accounts
- [ ] grant tables
- [x] data directory

#### Q33. You need to export the data in the customers table into a CSV file, with columns headers in the first row. Which clause do you add to your MySQL command?

- [ ] JOIN
- [ ] WITH HEADERS
- [x] UNION
- [ ] WITH COLUMNS

[Sample](https://stackoverflow.com/questions/5941809/include-headers-when-using-select-into-outfile)

#### Q34. One form of backup, replication, enables you to maintain identical data on multiple servers, as a \_ configuration.

- [ ] remote-local
- [ ] parent-child
- [x] master-slave
- [ ] logical-physical

#### Q35. What is the requirement for using a subquery in the SELECT clause?

- [ ] the subquery must use an aggregate function.
- [ ] the subquery must refer to the same table as the main query.
- [x] the subquery must return a single value.
- [ ] the subquery must return at least one value.

#### Q36. Each time MySQL is upgraded, it is best to execute mysql_upgrade, which looks for incompatibilities with the upgraded MySQL server. What does this command do, upon finding a table with a possible incompatibility?

- [x] it performs a table check and, if problems are found, attempts a table repair.
- [ ] it stops and notifies the server administrator that the upgrade cannot complete until the incompatibility issue are resolved.
- [ ] it provides a full report of the table specifications and the incompatibilities to the server administrator.
- [ ] it performs a table check and, if problems are found, displays the information for the server administrator to take action.

#### Q37. What mysql statement is used to check which accounts have specific privileges?

- [x] show grants (displays the privileges and roles that are assigned to a MySQL user account or role)
- [ ] show privileges (shows the list of system privileges that the MySQL server supports)
- [ ] show access
- [ ] show user permissions

#### Q38. What cannot have a trigger associated with it?

- [x] temporary table
- [ ] system table
- [ ] large table
- [ ] new table

[Reference](https://dev.mysql.com/doc/refman/5.7/en/create-trigger.html)

#### Q39. later versions of mysql support the native json data type for storing json documents. What is a drawback of json columns?

- [ ] inefficient for storing json documents
- [x] cannot be indexed directly
- [ ] documents cannot be validated when stored in json columns
- [ ] cannot be normalized

#### Q40. Which statement is true for the diagram below

![mysql Q41](images/mysql_q41.jpg?raw=true)

- [ ] carid is the primary key for purchases
- [ ] carid is the foreign key for cars.carid
- [x] customerid is the foreign key for customers.id
- [ ] customerid is the primary key for purchases

#### Q41. Which statement can you use to load data from a file into the table?

- [ ] `cat file | mysql`
- [x] `LOAD DATA INFILE`
- [ ] `LOAD DATA LOCAL INFILE`
- [ ] `extended INSERT statement`

#### Q43. Which is the correct syntax of an extended insert statement?

- [ ] insert into cars (make, model, year) values ('Ford', 'Mustang', 2002)
      ('Mercedes', 'C', 2003)

- [ ] insert into cars (make, model, year) values ('Ford', 'Mustang', 2002)
      values ('Mercedes', 'C', 2003)

- [ ] insert into cars (make, model, year) extended ('Ford', 'Mustang', 2002),
      ('Mercedes', 'C', 2003)

- [x] insert into cars (make, model, year) values ('Ford', 'Mustang', 2002),
      ('Mercedes', 'C', 2003)

#### Q44. You need to make an exact copy of a table, with all columns and indexes. How can you get all of the information needed to accomplish this?

- [ ] create table
- [ ] clone table
- [ ] insert into
- [x] show create table

Note that the question is about _getting_ the data and not about the _duplicating_ operation itself. And actually there is no need to run `SHOW CREATE TABLE` at all. [To duplicate the table](https://popsql.com/learn-sql/mysql/how-to-duplicate-a-table-in-mysql) structure you can `CREATE TABLE new_table LIKE original_table;`.

#### Q45. you need to make your mysql system secure against attackers. What are you _not_ supposed to do?

- [ ] Run MySQL server as a normal user.
- [ ] Grant PROCESS or SUPER privilege to other users.
- [x] Run MySQL server as the unix root user.
- [ ] Use the compressed protocol.

#### Q46. You are managing a database with a table called customers. You created a temporary table also called customers with which you are working for the duration of your session. You need to re-create the temporary table with different specifications. Which command do you need to run first?

- [ ] `CREATE TEMPORARY TABLE customers;`
- [ ] `DROP TEMP TABLE customers;`
- [ ] `DROP TABLE customers;`
- [x] `DROP TEMPORARY TABLE customers;`

1. [reference](https://dev.mysql.com/doc/refman/8.0/en/drop-table.html)
2. [reference](https://www.mysqltutorial.org/mysql-temporary-table)

#### Q47. You need to run a complex query with recursive subqueries, but without creating a stored procedure or a function. Which command or clause do you use?

- [ ] COLLATE
- [ ] UNION
- [ ] FULL JOIN
- [x] WITH

This is exactly what [WITH clause](https://dev.mysql.com/doc/refman/8.0/en/with.html) is designed for

#### Q48. Which choice is not a processing algorithm for database views?

- [ ] merge
- [x] updatable
- [ ] temptable
- [ ] undefined

[Reference](https://dev.mysql.com/doc/refman/8.0/en/view-algorithms.html)

#### Q49. What is the MySQL `perror` command-line utility used for?

- [ ] to display your version of MySQL
- [ ] to display operating system error codes
- [ ] to display default settings that are in error
- [x] to display storage error codes

Note: perror prints a description for a system error code or for a storage engine (table handler) error code -
[link](<https://dev.mysql.com/doc/refman/5.7/en/perror.html#:~:text=2%20perror%20%E2%80%94%20Display%20MySQL%20Error%20Message%20Information,-For%20most%20system&text=You%20can%20find%20out%20what,(table%20handler)%20error%20code>)

#### Q50. How can you list all columns for a given table?

- [ ] SHOW table COLUMNS;
- [x] SHOW COLUMNS FROM table;
- [ ] LIST table COLUMNS;
- [ ] SELECT COLUMNS FROM table;

Note: `DESCRIBE tablename` is a shortcut for this command

#### Q51. How would you list the full set of tables in the currently selected database?

- [ ] SELECT \* FROM DATABASE;
- [x] SHOW TABLES;
- [ ] LIST TABLES;
- [ ] SELECT ALL TABLES;

#### Q52. Which choice is not one of the table maintenance statements?

- [ ] CHECK TABLE;
- [x] CREATE TABLE;
- [ ] ANALYZE TABLE;
- [ ] OPTIMIZE TABLE;

#### Q53. In which table does MySQL store passwords for user accounts?

- [ ] mysql.accounts;
- [ ] mysql.passwords;
- [ ] mysql.admin;
- [x] mysql.user;

#### Q54. Management has requested that you build an employee database. You need to include each employee's current position and salary, as well as all prior positions and salaries with the company. You decide to use a one-to-many structure: an employee table with the main information such as name and address, and an employment table with position and salary history. You can use the employeeID field to connect them. What is employment.employeeID an example of?

- [ ] primary key;
- [ ] secondary key;
- [x] foreign key;
- [ ] alternate key;

#### Q55. In recent versions of MySQL (8.0+), what's the correct syntax to declare a CTE (Common Table Expression)?

- [ ] WITH (SELECT id FROM users) as cte, SELECT ...
- [ ] WITH (SELECT id FROM users) as cte SELECT ...
- [ ] WITH cte as (SELECT id FROM users), SELECT ...
- [x] WITH cte as (SELECT id FROM users) SELECT ...

#### Q56. What is one reason to introduce data redundancy into a normalized database design?

- [x] to reduce corruption in data
- [ ] to reduce storage space
- [x] to make the system faster
- [ ] to prevent data anomalies

Note: "to make the system faster" can also be correct. For example we can calculate some heavy query in advance and store its result in some column (use it as a cache). So if "system" means "application which uses mysql" then it's correct too.

#### Q57. The code snippet below is used to read data from an XML file into a table. Which XML structure is \_not\_ supported by the statement?

```mysql
LOAD XML LOCAL INFILE 'cars.xml'
INTO TABLE cars
ROWS IDENTIFIED BY `<car>`;
```

- [ ] A

```xml
<car>
   <field name="make"> Lexus </field>
   <field name="model"> IS300 </field>
   <field name="make"> 2016 </field>
</car>
```

- [x] B

```xml
<car name="make"> Dodge </car>
<car name="model"> Ram </car>
<car name="year"> 2000 </car>
```

- [ ] C

```xml
<car make="Ford" model="Mustang" year="2002"/>
```

- [ ] D

```xml
<car year="2010">
    <make>Mercedes</make> <model> C-Class</model>
</car>
```

#### Q58. You are loading data into a table. Which command can you use to make sure that all data is inserted and duplicates rows are discarded?

- [x] `INSERT IGNORE`
- [ ] `INSERT UNIQUE`
- [ ] `INSERT INTO`
- [ ] `INSERT DISTINCT`

#### Q59. Which statement about the `TRUNCATE TABLE` statement is true?

- [ ] It will stop and issue an error when it encounters a row that is referenced by a row in a child table.
- [x] It always first drops, then re-creates a new table.
- [ ] It deletes rows one by one on tables with foreign key constraints.
- [x] It does not invoke the `DELETE` triggers associated with the table.

Note: both answers are correct - see [TRUNCATE TABLE Statement](https://dev.mysql.com/doc/refman/8.0/en/truncate-table.html) in MySQL manual

#### Q60. You are working with the tables as shown in this diagram. You need to get the number of cars sold per the home state of each customer's residence. How can you accomplish this?

![mysql Q61](images/mysql_q61.png?raw=true)

- [ ] `SELECT state, COUNT(*) FROM customers WHERE ID IN (SELECT customerID FROM purchases) GROUP BY state;`
- [ ] `SELECT state, COUNT(*) FROM customers c LEFT JOIN purchases p ON c.ID = p.customerID GROUP BY state;`
- [x] `SELECT state, COUNT(*) FROM customers c, purchases p WHERE c.ID = p.customerID GROUP BY state;`
- [ ] `SELECT state, COUNT(*) FROM customers GROUP BY state;`

Explanation: THe difference between 2 and 3 is that LEFT JOIN will return 1 row per customer before grouping. If replaced with RIGHT JOIN it would return the correct info.

#### Q61. In data migration, there is often a need to delete duplicate rows as part of data cleanup. Which statement works best?

- [ ] `DELETE DUPS`
- [ ] `DELETE DISTINCT`
- [x] `DELETE JOIN`
- [ ] `DELETE WITH`

#### Q62. When working with MySQL cursor, what must you also declare?

- [ ] `DEFAULT` value
- [ ] `RETURN` variable
- [ ] `SQLEXCEPTION` routine
- [x] `NOT FOUND` handler

#### Q63. Which type of backup includes all the changes made to the data since the last full backup was performed?

- [ ] snapshot
- [ ] logical
- [x] differential
- [ ] incremental

#### Q64. You need to restore a MySQL database from a backup file. Which command-line tool do you use for the actual data import, after re-creating the database?

- [ ] `mysqld`
- [x] `mysql`
- [ ] `mysqladmin`
- [ ] `mysqldump`

#### Q65. You are importing data as JSON into a new table. You run CREATE TABLE json_data ( city JSON ); and insert rows into this table. What is the correct syntax to see the list of cities?

- [ ] `SELECT city FROM json_data;`
- [x] `SELECT city->>'$.name' city FROM json_data;`
- [ ] `SELECT city.name city FROM json_data;`
- [ ] `SELECT city->'$.name' city FROM json_data;`

Note: the last option is valid too but the results will be enclosed with quotation marks

#### Q66. If you want to use MyISAM instead of InnoDB, which option do you need to specify in the CREATE TABLE statement?

- [x] ENGINE
- [ ] PARTITION
- [ ] STORAGE
- [ ] TABLESPACE

#### Q67. You are working with the table in this diagram. You want to use full-text search to find the customers who live on a street or a drive. What is the command to do that?

Table name: **customers**

| ID   | lastname | firstname | phone        | address             | city        | state | zip   |
| ---- | -------- | --------- | ------------ | ------------------- | ----------- | ----- | ----- |
| A001 | Smith    | Bob       | 212-555-1212 | 1001 1st Street     | New York    | NY    | 10001 |
| A002 | Chang    | John      | 213-555-5678 | 888 Rodeo Drive     | Los Angeles | CA    | 90210 |
| A003 | Smith    | Mary      | 999-999-9999 | 123 Main Street     | Anytown     | VA    | 12345 |
| A004 | Johnson  | Jack      | 312-312-3120 | 1111 Chicago Avenue | Chicago     | IL    | 60606 |
| A005 | Lopez    | Linda     | 737-777-3333 | 123 Main Street     | Austin      | TX    | 73344 |

- [ ] A

```sql
SELECT *
FROM customers
WHERE address MATCH 'Street' OR 'Drive';
```

- [ ] B

```sql
SELECT *
FROM customers
WHERE MATCH(address) IN ('street, drive');
```

- [ ] C

```sql
SELECT *
FROM customers
WHERE address MATCH 'Street' OR address MATCH 'Drive';
```

- [x] D

```sql
SELECT *
FROM customers
WHERE MATCH(address) AGAINST ('street, drive');
```

#### Q68. Which query lists the databases on the current server?

- [x] SHOW DATABASES;
- [ ] LIST ALL DATABASES;
- [ ] LIST DATABASES;
- [ ] SHOW DB;

#### Q69. What is the product of the database designing phase?

- [ ] all tables, columns, data types, indexes and their relationships
- [ ] a list of entities, their relationship, and constraints
- [ ] all tables and their names, which are needed to implement the logical model
- [x] a list of entities, their relationship, constraints, data types, and cardinalities

#### Q70. Which choice is _not_ a valid model for a stored procedure parameter?

- [ ] INOUT
- [ ] IN
- [ ] OUT
- [x] IN OUT

#### Q71. What is the advantage of using a temporary table instead of a heap table?

- [ ] The temporary table will be dropped when the database is restarted.
- [ ] Temporary tables can be shared among clients, which makes them more usable in group development environments.
- [x] The temporary table will be dropped as soon as your session disconnects.
- [ ] Creating a temporary table does not require any special privileges.

#### Q72. What is the maximum number of columns that can be used by a single table index?

- [ ] 2
- [ ] 4
- [ ] 8
- [x] 16

#### Q73. Which command will return a list of triggers in the current database?

- [ ] `DISPLAY TRIGGERS;`
- [x] `SHOW TRIGGERS;`
- [ ] `SELECT ALL TRIGGERS;`
- [ ] `SELECT * FROM information_schema.triggers;`

#### Q74. Which statement is true about TIMESTAMP and DATETIME data types?

- [ ] TIMESTAMP values require more bytes for storage than DATETIME values.
- [ ] TIMESTAMP is stored without timezone, and DATETIME is stored in UTC values.
- [x] TIMESTAMP and DATETIME are both stored without time zone.
- [ ] TIMESTAMP is stored in UTC values, and DATETIME is stored in without time zone.

#### Q75. What is the equivalent of the mysqladmin reload command?

- [ ] `mysqladmin flush-threads`
- [ ] `mysqladmin flush-tables`
- [x] `mysqladmin flush-privileges`
- [ ] `mysqladmin flush-all`

#### Q76. Explain the security aspect of stored procedures

- [ ] Stored procedures are not secure, because they can be executed from the command line as the root user
- [ ] Stored procedures are secure, because the owner of the stored procedure can decide to whom access is granted
- [x] Stored procedures are secure, because applications can be given access to stored procedures and not any underlying tables
- [ ] Stored procedures are not secure, because they can execute statements to drop tables or bulk delete data

#### Q77. How would you retrieve data on all the customers where no phone number is stored?

- [ ] `SELECT * FROM customers WHERE PhoneNumber = NULL;`
- [ ] `SELECT * FROM customers WHERE PhoneNumber IS NOT VALID;`
- [x] `SELECT * FROM customers WHERE PhoneNumber IS NULL;`
- [ ] `SELECT * FROM customers WHERE PhoneNumber IS UNKNOWN;`

#### Q78. In the diagram below, the price field is declared as type DECIMAL. What would be a more efficient declaration for this field?

![mysql picture](images/mysql_q80.png?raw=true)

- [ ] FLOAT
- [x] DECIMAL(10,2)
- [ ] NUMERIC
- [ ] DOUBLE

#### Q79. Which choice is `not` an available string type for a column?

- [ ] `ENUM`
- [ ] `SET`
- [x] `BIT`
- [ ] `CHAR`

Explnation: BIT is not a string type

#### Q80. This diagram shows what type of relationship between customers and cars?

![mysql picture](images/mysql_q80.png?raw=true)

- [ ] one-to-many
- [ ] parent-child
- [x] many-to-many
- [ ] many-to-one

#### Q81. A stored routine is a set of SQL statements stored on the server and takes form as either a procedure or a function. Which statement cannot be used inside stored routines?

- [ ] `SELECT`
- [x] `USE`
- [ ] `SET`
- [ ] `DECLARE`

Explanation: Both `SET` and `DECLARE` are used to create variables. Reference: [MySQL STORED PROCEDURE Tutorial With Examples](https://www.softwaretestinghelp.com/mysql-stored-procedure/)

#### Q82. When a new student is added to a new database, you want new records to be created in the related tables such as Exam, Score and Attendance. How would you accomplish this?

- [x] trigger
- [ ] regular expression
- [ ] view
- [ ] index

#### Q83. In the diagram below, the ID fields are declared as type CHAR instead of INT . Which is NOT one of the possible reasons behind that decision?

![mysql picture](images/mysql_q85.png?raw=true)

- [ ] The ID field needs to include letters and not just numbers.
- [ ] You can have a consistent format across all of the tables that require ID fields.
- [ ] The ID field needs to have leading 0s, which the INT data type would truncate.
- [x] The `CHAR(10)` data type is more efficient and space-saving.

#### Q84. Why would you use a common table expression (CTE)?

- [ ] To define queries for later reuse for the duration of the current session
- [ ] To create temporary tables that can be used to pre-select often-used result sets.
- [ ] To calculate a new single value from a result set and return it to the query parser.
- [x] To break down complex queries and allow reuse within a query.

Explanation: CTEs do not create temporary tables, they only work within a signle query. Reference: [13.2.15 WITH (Common Table Expressions)](https://dev.mysql.com/doc/refman/8.0/en/with.html).

#### Q85. Which option modifier tells a program not to exit with an error if it does not recognize the option, but instead to issue a warning?

- [ ] --verbose
- [ ] --skip
- [ ] --skip-error
- [x] --loose

Reference: [4.2.2.4 Program Option Modifiers](https://dev.mysql.com/doc/refman/8.0/en/option-modifiers.html)

#### Q86. What does this SQL statement return?

```
SELECT name FROM students WHERE name REGEXP '^to';
```

- [x] all names starting with "to," such as Tommy or Tony
- [ ] all names with "to," such as Roberto and Tommy
- [ ] all names without "to," such as Samantha or Kathryn
- [ ] all names ending with "to," such as Roberto

#### Q87. You are working with the tables as shown in the diagram. You need to generate the list of price totals for each make and model of car, with subtotals for each make, and the grand total of all prices. Which SQL clause do you use?

![mysql picture](images/mysql_q92.png?raw=true)

- [ ] UNION
- [ ] SHOW TOTALS
- [ ] UNION ALL
- [x] WITH ROLLUP

#### Q88. The left and right joins are also known as \_.

- [ ] Inner Join
- [ ] Natural Join
- [x] Outer Join
- [ ] Cartesian Join

#### Q89. What is the valid way to create a database view in MySQL?

- [ ] `CREATE VIEW v1 SELECT * FROM t1 WHERE col1 > 10;`
- [ ] `CREATE VIEW v1 AS BEGIN SELECT * FROM t1 END;`
- [ ] `CREATE VIEW v1 BEGIN SELECT * FROM t1 END;`
- [x] `CREATE VIEW v1 AS SELECT * FROM t1;`

#### Q90. Inside a transaction, several operations need to be performed. What would you do if an exception happens during that transaction?

- [ ] `UNDO`
- [ ] `UNCOMMIT`
- [x] `ROLLBACK`
- [ ] `REVERSE`

#### Q91. What function finds the current time or date in MySQL?

- [ ] DATE()
- [ ] GETDATE()
- [x] CURDATE()
- [ ] CURRENT()

#### Q92. What is the correct usage of ENUM in MySQL?

- [ ] `Create table size (ENUM ('Small','Medium','Large'));`
- [ ] `Create table ENUM (name ('Small','Medium','Large'));`
- [ ] `Create table size (name: ENUM['Small','Medium','Large']);`
- [x] `Create table size (name ENUM('Small','Medium','Large'));`

#### Q93. The mysqldump command cannot generate output in **\_**.

- [x] JSON
- [ ] CSV
- [ ] XML
- [ ] TXT

#### Q94. You are working with the tables shown below. You need to generate the list of all cars, whether or not they had been sold. Which statement accomplishes that?

![mysql picture](images/mysql_q98.png?raw=true)

- [ ] A

```
SELECT cars.*, purchases.date
FROM cars RIGHT JOIN purchases
ON cars.ID = purchases.carID;
```

- [ ] B

```
SELECT cars.*, purchases.date
FROM cars INNER JOIN purchases
ON cars.ID = purchases.carID;
```

- [ ] C

```
SELECT cars.*, purchases.date
FROM cars JOIN purchases
ON cars.ID = purchases.carID;
```

- [x] D

```
SELECT cars.*, purchases.date FROM cars LEFT JOIN purchases ON cars.ID = purchases.carID;
```

#### Q95. Which code snippet from a stored procedure should be rewritten as a CASE statement?

- [ ] A

```
    IF var1 THEN SET varA = var1;
    ELSEIF var2 THEN SET varA = var2;
    ELSEIF var3 THEN SET varA = var3;
    ELSE SET varA = var4;
    END IF;
```

- [ ] B

```
    IF var1 = var2 THEN SET varA = var1;
    ELSEIF var2 = var3 THEN SET varA = var2;
    ELSEIF var3 = var4 THEN SET varA = var3;
    ELSE SET varA = var4;
    END IF;
```

- [ ] C

```
    IF var1 = 1 THEN SET varA = var1;
    ELSEIF var2 = 2 THEN SET varA = var2;
    ELSEIF var3 = 3 THEN SET varA = var3;
    ELSE SET varA = var4;
    END IF;
```

- [x] D

```
    IF var1 = 1 THEN SET varA = var1;
    ELSEIF var1 = 2 THEN SET varA = var2;
    ELSEIF var1 = 3 THEN SET varA = var3;
    ELSE SET varA = var4;
    END IF;
```

#### Q96. Why would you use stored functions?

- [x] for formulas and business rules that you want to apply to columns in an SQL query
- [ ] for formulas and business rules that should be applied on a specific trigger event like on inserts
- [ ] to automatically modify the data of a table based on a query
- [x] for reusing recurring queries

#### Q97. What steps do you need to take to normalize the table from this diagram?

Table name: superheroes
| name | alias | power1 | power2 | power3 |
| ---- | ----- | ------ | ------ | ------ |
| Superman | Clark Kent | Flight | X-Ray Vision | Super Strength |
| Wonder Woman | Diana Prince | Force Fields | Reflexes | Telepathy |
| Spider-man | Peter Parker | Walcrawling | Web-making | Enhanced Senses |
| Aquaman | Arthur Curry | Underwater Breathing | Enhanced Sight | Stamina |
| Hulk | Bruce Banner | Super Strength | Radiation Immunity | Invulnerability |

- [x] Create another table to serve as a lookup for powers with fields for code and description, as well as a junction table with superhero names and power codes.
- [ ] Add a column to this table to serve as a record identifier, and make it the primary key.
- [ ] Extend this table to have additional columns "power4," "power5," and so on, to allow additional powers for each superhero.
- [ ] Convert this table to have column called "power," and add one record for each superhero-power combination, for a total of 15 records in this example.

#### Q98. A table Item has a Boolean field endOfLife and a field makeYear of type YEAR(4). How can you set the Boolean to true for all Items that have been made before 2019?

- [ ] UPSERT Item SET endOfLife = true WHERE makeYear < 2019
- [ ] CHANGE Item SET endOfLife = true WHERE makeYear < 2019
- [ ] ALTER Item SET endOfLife = true WHERE makeYear < 2019
- [x] UPDATE Item SET endOfLife = true WHERE makeYear < 2019

#### Q99. Which choice is an example of an aggregate function?

- [ ] NOW()
- [ ] MID()
- [ ] FORMAT()
- [x] COUNT()

[Reference](https://www.sqltutorial.org/sql-aggregate-functions/)

#### Q100. You are working on UPDATE trigger on the employee tablein this diagram. How can you access the new value for the address inside the trigger?

![mysql picture](images/mysql_q116.png?raw=true)

- [x] Use NEW.address
- [ ] Use INSERTED.address
- [ ] Use DELETED.address
- [ ] USE OLD.address

[Reference](https://dev.mysql.com/doc/refman/8.0/en/trigger-syntax.html)

#### Q101. You are working with the tables as shown in this diagram. You need to generate the list of customers who purchased certain car models. Which SQL clause do you use?

![Q104](https://github.com/Ebazhanov/linkedin-skill-assessments-quizzes/assets/22109189/5c73a5c5-3e8b-4110-8068-dca25b323e57)

- [ ] UNION ALL
- [x] UNION
- [ ] SHOW TOTALS
- [ ] WITH ROLLUP

#### Q102. How would you make a case-insensitive query in MySQL?

- [ ] `SELECT * FROM customers WHERE UPPEERCASE(LastName) = 'POTTER';`
- [ ] `SELECT * FROM customers WHERE LOWERCASE(LastName) = 'potter';`
- [x] `SELECT * FROM customers WHERE UPPER(LastName) = 'POTTER';`
- [ ] `SELECT * FROM customers WHERE UPPER(LastName) = 'Potter';`

#### Q103. "COUNT" keyword belongs to which categories in Mysql?

- [x] Aggregate functions
- [ ] Operators
- [ ] Clauses
- [ ] All of the mentioned`

#### Q104. What is the meaning of "HAVING" clause in Mysql?

- [ ] To filter out the column values
- [x] To filter out the row values
- [ ] To filter out the row and column values
- [ ] None of the mentioned

#### Q105. Which clause is similar to "HAVING" clause in Mysql?

- [ ] SELECT
- [ ] FROM
- [x] WHERE
- [ ] None of the mentioned

#### Q106. What will be the output of the following MySQL command?

      SELECT emp_id, fname, lname
      FROM employee
      WHERE title=’HEAD TELLER’ AND start_date&gt;2008-11-23;

- [ ] All columns
- [ ] Only those columns which are mention with "SELECT" clause
- [x] Columns mention with "SELECT" clause and only those rows which contain 'HEAD TELLER' as a "title"
- [ ] None of the mentioned

#### Q107. Is there any error in the following MySQL statement?

      SELECT e.emp_id, e.fname,e.lname,d.name
      FROM employee e INNER JOIN department d
      ON e.dept_id=e.dept_id;

- [x] NO
- [ ] YES
- [ ] DEPEND
- [ ] None of the mentioned

#### Q108. With MySQL, how do you select all the records from a table named "Persons" where the "LastName" is alphabetically between (and including) "Hansen" and "Pettersen"?

- [ ] `SELECT LastName>'Hansen' AND LastName<'Pettersen' FROM Persons`
- [x] `SELECT * FROM Persons WHERE LastName BETWEEN 'Hansen' AND 'Pettersen'`
- [ ] `SELECT * FROM Persons WHERE LastName>'Hansen' AND LastName<'Pettersen'`
- [ ] `None of the above.`

[Reference](https://www.w3schools.com/mysql/mysql_between.asp)

#### Q109. Consider the set of relations given below and the SQL query that follows

        Students : (Roll number, Name, Date of birth)
        Courses: (Course number, Course name, instructor)
        Grades: (Roll number, Course number, Grade)
        SELECT DISTINCT Name
        FROM Students, Courses, Grades
        WHERE Students.Roll_number = Grades.Roll_number
        AND Courses.Instructor =Sriram
        AND Courses.Course_number = Grades.Course_number
        AND Grades.Grade = A

(Which of the following sets is computed by the above query?)

- [ ] Names of Students who have got an A grade in all courses taught by Sriram
- [ ] Names of Students who have got an A grade in all courses
- [x] Names of Students who have got an A grade in at least one of the courses taught by Sriram
- [ ] None of the above

#### Q110. You are working with the tables shown below. You need to make sure that any record added to the purchases table consists of a customerlD, which already exists in the customers table, and a carlD, which already exists in the cars table. You decide to use a trigger to do the validation. Which one do you use?

![mysql picture](images/mysql_q85.png?raw=true)

- [ ] IF EXISTS
- [ ] CROSS JOIN
- [x] BEFORE INSERT
- [ ] AFTER INSERT]

`IF EXISTS` and `CROSS JOIN` are not valid for a trigger.

#### Q111. Current versions of MySQL support the full-text search feature on some storage engines, as an alternative to using the LIKE operator and regular expressions. Which statement would you run to enable a full-text index for the column description in the table Car?

- [x] ALTER TABLE car ADD FULL TEXT(description);
- [ ] MERGE TABLE car ADD FULL TEXT(description)
- [ ] ENABLE FULL TEXT(description) car
- [ ] SEARCH FULL TEXT(description) car

#### Q112. Which statement would you _not_ use to filter data?

![image](https://github.com/Ebazhanov/linkedin-skill-assessments-quizzes/assets/22109189/9cb0ae9d-1f6b-4f85-9d2f-44b6a7afd00c)

- [x] GROUP_BY
- [ ] MATCH
- [ ] WHERE
- [ ] LIKE

#### Q113. In MySQL, which JOIN type returns all rows from the left table and the matching rows from the right table, and fills in with NULL values if there is no match on the right side?

- [ ] INNER JOIN
- [x] LEFT JOIN (or LEFT OUTER JOIN)
- [ ] RIGHT JOIN (or RIGHT OUTER JOIN)
- [ ] FULL JOIN (or FULL OUTER JOIN)

#### Q114. What does SQL stand for in MySQL?

- [x] Structured Query Language
- [ ] Simple Query Language
- [ ] System Query Language
- [ ] Structured Question Language

#### Q115. Which MySQL statement is used to select data from a database?

- [ ] Extract
- [x] select
- [ ] get
- [ ] Open

#### Q116. What is the purpose of the `PRIMARY KEY` in a MySQL table?

- [x] To create a unique index on a table
- [ ] To define a column as an integer
- [ ] To define the data type of a column
- [ ] To specify a foreign key reference

[Reference](<https://www.w3schools.com/mysql/mysql_primarykey.asp#:~:text=The%20PRIMARY%20KEY%20constraint%20uniquely,or%20multiple%20columns%20(fields).>)

#### Q117. Which of the following is a valid SQL query to insert a new row into the users table?

- [x] `INSERT INTO users (name, email) VALUES ('John Doe', 'john.doe@example.com')`
- [ ] `ADD users (name, email) VALUES ('John Doe', 'john.doe@example.com')`
- [ ] `CREATE users (name, email) VALUES ('John Doe', 'john.doe@example.com')`
- [ ] `UPDATE users (name, email) VALUES ('John Doe', 'john.doe@example.com')`

#### Q118. Which of the following is a valid SQL query to delete the row with the id of 2 from the users table?

- [x] `DELETE FROM users WHERE id = 2`
- [ ] `REMOVE FROM users WHERE id = 2`
- [ ] `DROP users WHERE id = 2`
- [ ] `TRUNCATE users WHERE id = 2`

#### Q119. MySQL programs are a set of command-line utilities that are provided with typical MySQL distributions. MySQL is designed to be a database.

- [ ] database and programming
- [ ] user and administrator
- [x] client and server
- [ ] syntax and objects

#### Q120. Which MySQL command shows the structure of a table?

- [ ] INFO table;
- [ ] SHOW table;
- [ ] STRUCTURE table;
- [x] DESCRIBE table;

#### Q121. The left and right joins are also known as \_.

- [ ] Inner Join
- [ ] Natural Join
- [x] Outer Join
- [ ] Cartesian Join

#### Q122. What is the valid way to create a database view in MySQL?

- [ ] `CREATE VIEW v1 SELECT * FROM t1 WHERE col1 > 10;`
- [ ] `CREATE VIEW v1 AS BEGIN SELECT * FROM t1 END;`
- [ ] `CREATE VIEW v1 BEGIN SELECT * FROM t1 END;`
- [x] `CREATE VIEW v1 AS SELECT * FROM t1;`

#### Q123. In a database with a "Students" table containing information about students, which SQL statement is used to retrieve the names of all students who scored higher than 90 in their exams?

- [ ] A

```
SELECT student_name FROM Students WHERE score > 90;
```

- [x] B

```
SELECT name FROM Students WHERE score > 90;
```

- [ ] C

```
SELECT student_name FROM Students WHERE exam_score > 90;
```

- [ ] D

```
SELECT name FROM Students WHERE exam_score > 90;
```

#### Q124 Which SQL command is used to retrieve data from a database?

- [ ] FETCH
- [ ] SEARCH
- [x] SELECT
- [ ] EXTRACT

#### Q125. Which MySQL function would you use to get the current date and time?

- [ ] GETDATE()
- [ ] CURRENTTIME()
- [x] NOW()
- [ ] DATETIME()

#### Q126. In MySQL, which statement is used to add a new column to an existing table?

- [ ] MODIFY TABLE
- [ ] UPDATE TABLE
- [x] ALTER TABLE
- [ ] CHANGE TABLE

#### Q127. What is the purpose of the LIMIT clause in a MySQL SELECT statement?

- [ ] To limit the number of tables that can be joined
- [x] To restrict the number of rows returned by the query
- [ ] To limit the number of columns that can be selected
- [ ] To restrict the query execution time

#### Q128. Which MySQL command is used to show all databases on the server?

- [ ] LIST DATABASES;
- [ ] DISPLAY DATABASES;
- [x] SHOW DATABASES;
- [ ] SELECT DATABASES;

#### Q129. What does the UNSIGNED keyword do when used in a column definition?

- [ ] It makes the column accept only positive numbers
- [ ] It makes the column accept only whole numbers
- [x] It doubles the maximum value that can be stored in the column
- [ ] It makes the column accept only text data

#### Q130. Which MySQL function would you use to find the length of a string?

- [ ] SIZE()
- [x] LENGTH()
- [ ] LEN()
- [ ] STRLEN()

#### Q131. What is the purpose of the AUTO_INCREMENT attribute in MySQL?

- [ ] To automatically update the column value when the row is modified
- [ ] To automatically decrease the column value by 1 for each new row
- [x] To automatically generate a unique identity for new rows
- [ ] To automatically set the column to the current timestamp

#### Q132. Which MySQL statement is used to remove a table from a database?

- [ ] REMOVE TABLE
- [ ] DELETE TABLE
- [x] DROP TABLE
- [ ] ERASE TABLE

#### Q133. What does the LIKE operator do in a WHERE clause?

- [ ] It compares two values for exact equality
- [x] It searches for a specified pattern in a column
- [ ] It checks if a value is NULL
- [ ] It performs mathematical comparisons

#### Q134. Which MySQL function returns the number of rows affected by an INSERT, UPDATE, or DELETE statement?

- [ ] AFFECTED_ROWS()
- [ ] COUNT_CHANGES()
- [ ] ROW_COUNT()
- [x] FOUND_ROWS()

#### Q135. What is the purpose of the HAVING clause in MySQL?

- [ ] To join multiple tables
- [ ] To sort the result set
- [x] To specify a search condition for a group or an aggregate
- [ ] To limit the number of rows returned

#### Q136. Which MySQL statement is used to grant privileges to a user?

- [ ] ADD PRIVILEGES
- [ ] SET PRIVILEGES
- [x] GRANT
- [ ] ALLOW

#### Q137. What does the IFNULL() function do in MySQL?

- [ ] It checks if a value is not NULL
- [x] It returns a specified value if the expression is NULL
- [ ] It sets a column value to NULL
- [ ] It removes NULL values from a result set

#### Q138. Which MySQL command is used to show the current user and host?

- [ ] SHOW USER;
- [ ] CURRENT_USER();
- [ ] WHO AM I;
- [x] SELECT USER();

#### Q139. What is the purpose of the EXPLAIN statement in MySQL?

- [ ] To provide documentation for a stored procedure
- [ ] To show the structure of a table
- [x] To show the execution plan of a SELECT statement
- [ ] To explain the meaning of an error message

#### Q140. Which MySQL function would you use to round a number to the nearest integer?

- [ ] CEIL()
- [ ] FLOOR()
- [x] ROUND()
- [ ] INT()

#### Q141. What does the UNIQUE constraint do in MySQL?

- [ ] It ensures that the column cannot contain NULL values
- [x] It ensures that all values in the column are different
- [ ] It automatically increments the value for each new row
- [ ] It sets a default value for the column

#### Q142. Which MySQL statement is used to create an index on a table?

- [ ] ADD INDEX
- [x] CREATE INDEX
- [ ] MAKE INDEX
- [ ] INDEX TABLE

#### Q143. What is the purpose of the COALESCE() function in MySQL?

- [ ] To combine multiple columns into one
- [ ] To check if all values in a list are equal
- [x] To return the first non-NULL value in a list
- [ ] To count the number of non-NULL values in a list

#### Q144. Which MySQL command is used to start a transaction?

- [ ] BEGIN TRANSACTION
- [ ] START TRANSACTION
- [ ] INIT TRANSACTION
- [x] BEGIN

#### Q145. What does the CONCAT() function do in MySQL?

- [ ] It adds numbers together
- [x] It joins two or more strings together
- [ ] It combines multiple rows into one
- [ ] It merges two tables

#### Q146. Which MySQL statement is used to create a stored procedure?

- [ ] MAKE PROCEDURE
- [ ] ADD PROCEDURE
- [x] CREATE PROCEDURE
- [ ] DEFINE PROCEDURE

#### Q147. What is the purpose of the REGEXP operator in MySQL?

- [ ] To perform mathematical operations
- [ ] To join multiple tables
- [x] To perform pattern matching using regular expressions
- [ ] To check if a value exists in a subquery

#### Q148. Which MySQL function would you use to get the current user's username?

- [ ] CURRENT_USER()
- [ ] USERNAME()
- [x] USER()
- [ ] SYSTEM_USER()

#### Q149. What does the DISTINCT keyword do in a SELECT statement?

- [ ] It sorts the result set in ascending order
- [ ] It limits the number of rows returned
- [x] It removes duplicate rows from the result set
- [ ] It selects only specific columns from the table

#### Q150. Which MySQL statement is used to delete all rows from a table without deleting the table itself?

- [ ] DELETE TABLE
- [ ] REMOVE ALL FROM
- [ ] DROP TABLE
- [x] TRUNCATE TABLE


#### Q151. What is the purpose of the `UNION` operator in MySQL?

- [ ] To combine the results of multiple `SELECT` statements into a single result set, removing duplicate rows.
- [ ] To perform a logical OR operation on the results of multiple `SELECT` statements.
- [x] To combine the results of multiple `SELECT` statements into a single result set, including duplicate rows.
- [ ] To perform a logical AND operation on the results of multiple `SELECT` statements.

**Explanation:**
The `UNION` operator in MySQL is used to combine the results of multiple `SELECT` statements into a single result set. The key difference between `UNION` and `UNION ALL` is that `UNION` removes duplicate rows, while `UNION ALL` includes all rows, including duplicates.

#### Q152. What is the purpose of the `HAVING` clause in a MySQL query?

- [ ] To filter the rows in the result set based on the values in the columns.
- [ ] To sort the rows in the result set in ascending or descending order.
- [x] To filter the groups in the result set based on the values of aggregate functions.
- [ ] To limit the number of rows returned in the result set.

**Explanation:**
The `HAVING` clause in a MySQL query is used to filter the groups in the result set based on the values of aggregate functions, such as `SUM`, `AVG`, `COUNT`, etc. This is different from the `WHERE` clause, which is used to filter the rows in the result set based on the values in the columns.

The `HAVING` clause is typically used in conjunction with the `GROUP BY` clause, which groups the rows in the result set based on the values in one or more columns.
