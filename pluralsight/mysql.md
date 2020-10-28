Q1 What is the default size of buffer for client server communication ?

- [] No default
- [] 500 mb
- [] 1 gb
- [x] 16 mb

Q2 Which is a valid storage engine for mysql?

- [] utf-8
- [] localdb
- [x] myIsam
- [] ANSI

Q3 Which utility is used to generate compressed, read-only myISAM tables?

- [x] myisampack
- [] myisamchk
- [] myisamlog
- [] myisam_ftdump 

Q4 How would you select the first non-null value from either column B or column A in that order?

- [x] coalesce(b,a)
- [] coalesce(a,b)
- [] b if a is not null
- [] a if b is not null

Q5 Which privilege is required in order to set the gobal or session binlog_format value?

- [] show databases
- [] replication client
- [x] super
- [] replication slave

Q6 Which feature relates to isolation in InnoDb?

- [] doublewrite buffer
- [] battery-backed cache
- [x] locking
- [] commit

Q7 You do a single insert statement for a table with auto_increment turned on for the primary key. How do you get the primary key?

- [] You can't, key constraint error
- [] select last_insert_id();
- [] select last_key_inc();
- [] get_auto_id();

Q8 Which feature relates to atomicity in InnoDb?

- [] Battery-backed cache
- [] Replication
- [x] Doublewrite Buffer
- [] Locking

Q9 Which sets the current session's transaction isolation level to serializable?

- [] set session isolation level serializable;
- [x] set global transaction isolation level serializable;
- [] set session transaction isolation level serializable;
- [] set global isolation level serializable;

Q10 Which MySQL property controls transaction behavior between reads and writes?

- [] Restore
- [] Backup
- [x] Isolation
- [] Durability

Q11 What is a stored program that is attached to a table or a view?

- [] Embedded setect statement
- [x] Trigger
- [] Pseudofile

Q12 You want the table data to be cached in the InnoDB buffer pool. Which option
will you use to specify the size of the buffer pool?

- [] innodb_buffer_size

- [] innodb_pool_size

- [x] innodb_buffer_pool_size

- [] innodb_internal_buffer_pool_size

Q13 In a multi-instance MySQL setup, parameters and environment variables
values used by a given instance can be found using which of the following statement?

- [] VARIABLES
- [x] SHOW VARIABLES
- [] SHOW_VARTABLES
- [] SHOW ALL VARTABLES

Q14 Assume, you have a table inventory(id int, description text, price int) . How can you change the type of price from int to decimal(10,2)?

- [] MODIFY TABLE inventory ALTER price decimal(10,2)

- [x] ALTER TABLE inventory MODIFY price decimal(1@,2)

- [] ALTER TABLE inventory CHANGE column price decimal(1@,2)

- [] ALTER TABLE inventory price decimal(10,2)

Q15 Which assigns the custom value ‘bar’ to the variable foo ?

- [x] SET @foo = 'bar';

- [] $foo = 'bar';

- [] VAR @foo = 'bar';

- [] SET $foo= 'bar';

Q16 What is the default replication format used from MySQL 5.7.7 and later?

- [] Statement-based replication (SBR)
- [x] Row-based replication (RBR)

- [] Mixed-format replication

Q17 What does the following command output?
SELECT 1;

- [] '1'
- [] "1"
- [x] 1

After a query is executed, which of the following is used to cycle through each row of a result set while in memory?

- [] Trigger
- [x] Cursor
- [] view
- [] index