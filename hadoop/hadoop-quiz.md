## Hadoop

#### Q1. Partitioner controls the partitioning of what data?

- [ ] final keys
- [ ] final values
- [x] intermediate keys
- [ ] intermediate values

#### Q2. SQL Windowing functions are implemented in Hive using which keywords?

- [ ] UNION DISTINCT, RANK
- [x] OVER, RANK
- [ ] OVER, EXCEPT
- [ ] UNION DISTINCT, RANK

#### Q3. Rather than adding a Secondary Sort to a slow Reduce job, it is Hadoop best practice to perform which optimization?

- [ ] Add a partitioned shuffle to the Map job.
- [x] Add a partitioned shuffle to the Reduce job.
- [ ] Break the Reduce job into multiple, chained Reduce jobs.
- [ ] Break the Reduce job into multiple, chained Map jobs.

#### Q4. Hadoop Auth enforces authentication on protected resources. Once authentication has been established, it sets what type of authenticating cookie?

- [ ] encrypted HTTP
- [ ] unsigned HTTP
- [ ] compressed HTTP
- [x] signed HTTP

#### Q5. MapReduce jobs can be written in which language?

- [x] Java or Python
- [ ] SQL only
- [ ] SQL or Java
- [ ] Python or SQL

#### Q6. To perform local aggregation of the intermediate outputs, MapReduce users can optionally specify which object?

- [ ] Reducer
- [x] Combiner
- [ ] Mapper
- [ ] Counter

#### Q7. To verify job status, look for the value `___` in the `___`.

- [ ] SUCCEEDED; syslog
- [x] SUCCEEDED; stdout
- [ ] DONE; syslog
- [ ] DONE; stdout

#### Q8. Which line of code implements a Reducer method in MapReduce 2.0?

- [x] public void reduce(Text key, Iterator<IntWritable> values, Context context){…}
- [ ] public static void reduce(Text key, IntWritable[] values, Context context){…}
- [ ] public static void reduce(Text key, Iterator<IntWritable> values, Context context){…}
- [ ] public void reduce(Text key, IntWritable[] values, Context context){…}

#### Q9. To get the total number of mapped input records in a map job task, you should review the value of which counter?

- [ ] FileInputFormatCounter
- [ ] FileSystemCounter
- [ ] JobCounter
- [x] TaskCounter (NOT SURE)

#### Q10. Hadoop Core supports which CAP capabilities?

- [x] A, P
- [ ] C, A
- [ ] C, P
- [ ] C, A, P

#### Q11. What are the primary phases of a Reducer?

- [ ] combine, map, and reduce
- [x] shuffle, sort, and reduce
- [ ] reduce, sort, and combine
- [ ] map, sort, and combine

#### Q12. To set up Hadoop workflow with synchronization of data between jobs that process tasks both on disk and in memory, use the `___` service, which is `___`.

- [ ] Oozie; open source
- [ ] Oozie; commercial software
- [ ] Zookeeper; commercial software
- [x] Zookeeper; open source

#### Q13. For high availability, use multiple nodes of which type?

- [ ] data
- [x] name
- [ ] memory
- [ ] worker

#### Q14. DataNode supports which type of drives?

- [x] hot swappable
- [ ] cold swappable
- [ ] warm swappable
- [ ] non-swappable

#### Q15. Which method is used to implement Spark jobs?

- [ ] on disk of all workers
- [ ] on disk of the master node
- [ ] in memory of the master node
- [x] in memory of all workers

#### Q16. In a MapReduce job, where does the map() function run?

- [ ] on the reducer nodes of the cluster
- [x] on the data nodes of the cluster (NOT SURE)
- [ ] on the master node of the cluster
- [ ] on every node of the cluster

#### Q17. To reference a master file for lookups during Mapping, what type of cache should be used?

- [x] distributed cache
- [ ] local cache
- [ ] partitioned cache
- [ ] cluster cache

#### Q18. Skip bad records provides an option where a certain set of bad input records can be skipped when processing what type of data?

- [ ] cache inputs
- [ ] reducer inputs
- [ ] intermediate values
- [x] map inputs

#### Q19. Which command imports data to Hadoop from a MySQL database?

- [ ] spark import --connect jdbc:mysql://mysql.example.com/spark --username spark --warehouse-dir user/hue/oozie/deployments/spark
- [ ] sqoop import --connect jdbc:mysql://mysql.example.com/sqoop --username sqoop --warehouse-dir user/hue/oozie/deployments/sqoop
- [x] sqoop import --connect jdbc:mysql://mysql.example.com/sqoop --username sqoop --password sqoop --warehouse-dir user/hue/oozie/deployments/sqoop
- [ ] spark import --connect jdbc:mysql://mysql.example.com/spark --username spark --password spark --warehouse-dir user/hue/oozie/deployments/spark

#### Q20. In what form is Reducer output presented?

- [x] compressed (NOT SURE)
- [ ] sorted
- [ ] not sorted
- [ ] encrypted

#### Q21. Which library should be used to unit test MapReduce code?

- [ ] JUnit
- [ ] XUnit
- [x] MRUnit
- [ ] HadoopUnit

#### Q22. If you started the NameNode, then which kind of user must you be?

- [ ] hadoop-user
- [x] super-user
- [ ] node-user
- [ ] admin-user

#### Q23. State \_\_ between the JVMs in a MapReduce job

- [ ] can be configured to be shared
- [ ] is partially shared
- [ ] is shared
- [x] is not shared (https://www.lynda.com/Hadoop-tutorials/Understanding-Java-virtual-machines-JVMs/191942/369545-4.html)

#### Q24. To create a MapReduce job, what should be coded first?

- [ ] a static job() method
- [x] a Job class and instance (NOT SURE)
- [ ] a job() method
- [ ] a static Job class

#### Q25. To connect Hadoop to AWS S3, which client should you use?

- [x] S3A
- [ ] S3N
- [ ] S3
- [ ] the EMR S3

#### Q26. HBase works with which type of schema enforcement?

- [ ] schema on write
- [ ] no schema
- [ ] external schema
- [x] schema on read

#### Q27. HDFS file are of what type?

- [ ] read-write
- [ ] read-only
- [ ] write-only
- [x] append-only

#### Q28. A distributed cache file path can originate from what location?

- [ ] hdfs or top
- [ ] http
- [x] hdfs or http
- [ ] hdfs

#### Q29. Which library should you use to perform ETL-type MapReduce jobs?

- [ ] Hive
- [x] Pig
- [ ] Impala
- [ ] Mahout

#### Q30. What is the output of the Reducer?

- [ ] a relational table
- [ ] an update to the input file
- [ ] a single, combined list
- [x] a set of <key, value> pairs

`map function processes a certain key-value pair and emits a certain number of key-value pairs and the Reduce function processes values grouped by the same key and emits another set of key-value pairs as output.`

#### Q31. To optimize a Mapper, what should you perform first?

- [ ] Override the default Partitioner.
- [ ] Skip bad records.
- [ ] Break up Mappers that do more than one task into multiple Mappers.
- [ ] Combine Mappers that do one task into large Mappers.

#### Q32. When implemented on a public cloud, with what does Hadoop processing interact?

- [x] files in object storage
- [ ] graph data in graph databases
- [ ] relational data in managed RDBMS systems
- [ ] JSON data in NoSQL databases

#### Q33. In the Hadoop system, what administrative mode is used for maintenance?

- [ ] data mode
- [x] safe mode
- [ ] single-user mode
- [ ] pseudo-distributed mode

### Q34. In what format does RecordWriter write an output file?

- [x] <key, value> pairs
- [ ] keys
- [ ] values
- [ ] <value, key> pairs

### Q35. To what does the Mapper map input key/value pairs?

- [ ] an average of keys for values
- [ ] a sum of keys for values
- [x] a set of intermediate key/value pairs
- [ ] a set of final key/value pairs

### Q36. Which Hive query returns the first 1,000 values?

- [ ] SELECT…WHERE value = 1000
- [x] SELECT … LIMIT 1000
- [ ] SELECT TOP 1000 …
- [ ] SELECT MAX 1000…

### Q37. To implement high availability, how many instances of the master node should you configure?

- [ ] one
- [ ] zero
- [ ] shared
- [ ] two or more

### Q38. Hadoop 2.x and later implement which service as the resource coordinator?

- [ ] kubernetes
- [ ] JobManager
- [ ] JobTracker
- [x] YARN

### Q39. In MapReduce, _______ have ____

- [ ] tasks; jobs
- [ ] jobs; activities
- [x] jobs; tasks
- [ ] activities; tasks

### Q40. What type of software is Hadoop Common?

- [ ] database
- [x] distributed computing framework
- [ ] operating system
- [ ] productivity tool

### Q41. If no reduction is desired, you should set the numbers of ____ tasks to zero

- [ ] combiner
- [x] reduce
- [ ] mapper
- [ ] intermediate

### Q42. MapReduce applications use which of these classes to report their statistics?

- [ ] mapper
- [ ] reducer
- [ ] combiner
- [x] counter

### Q43. ____ is the query language, and ____ is storage for NoSQL on Hadoop

- [ ] HDFS; HQL
- [x] HQL; HBase
- [ ] HDFS; SQL
- [ ] SQL; HBase

### Q44. MapReduce 1.0 ___ YARN

- [x] does not include
- [ ] is the same thing as
- [ ] includes
- [ ] replaces

### Q45. Which type of Hadoop node executes file system namespace operations like opening, closing, and renaming files and directories?
- [ ] ControllerNode
- [ ] DataNode
- [ ] MetadataNode
- [x] NameNode

### Q46. HQL queries produce which job types?

- [ ] Impala
- [ ] MapReduce
- [ ] Spark
- [ ] Pig

### Q47 Suppose you are trying to finish a Pig script that converts text in the input string to uppercase. What code is needed on line 2 below?
	1 data = LOAD '/user/hue/pig/examples/data/midsummer.txt'...
	2
	
- [ ] as (text:CHAR[]); upper_case = FOREACH data GENERATE org.apache.pig.piggybank.evaluation.string.UPPER(TEXT);
- [x] as (text:CHARARRAY); upper_case = FOREACH data GENERATE org.apache.pig.piggybank.evaluation.string.UPPER(TEXT);
- [ ] as (text:CHAR[]); upper_case = FOREACH data org.apache.pig.piggybank.evaluation.string.UPPER(TEXT);
- [ ] as (text:CHARARRAY); upper_case = FOREACH data org.apache.pig.piggybank.evaluation.string.UPPER(TEXT);

### Q48. In a MapReduce job, which phase runs after the Map phase completes?

- [x] Combiner
- [ ] Reducer
- [ ] Map2
- [ ] Shuffle and Sort

### Q49. Where would you configure the size of a block in a Hadoop environment?

- [x] dfs.block.size in hdfs-site.xmls
- [ ] orc.write.variable.length.blocks in hive-default.xml
- [ ] mapreduce.job.ubertask.maxbytes in mapred-site.xml
- [ ] hdfs.block.size in hdfs-site.xml

### Q50. Hadoop systems are ______ RDBMS systems.

- [ ] replacements for
- [ ] not used with
- [ ] substitutes for
- [x] additions for 

### Q51. Which object can be used to distribute jars or libraries for use in MapReduce tasks?

- [x] distributed cache
- [ ] library manager
- [ ] lookup store
- [ ] registry 