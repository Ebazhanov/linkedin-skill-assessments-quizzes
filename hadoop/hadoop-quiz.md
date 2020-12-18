## Hadoop Assessment

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

#### Q7. To verify job status, look for the value **\_** in the **\_**.

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

#### Q12. To set up Hadoop workflow with synchronization of data between jobs that process tasks both on disk and in memory, use the **\_** service, which is **\_**.

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
