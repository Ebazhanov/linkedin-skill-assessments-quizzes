Hadoop Assessment
-------------

#### Q1. Partitioner controls the partitioning of what data?

- [ ] final keys
- [ ] final values
- [ ] intermediate keys
- [ ] intermediate values


#### Q2. SQL Windowing functions are implemented in Hive using which keywords?

- [ ] UNION DISTINCT, RANK
- [ ] OVER, RANK
- [ ] OVER, EXCEPT
- [ ] UNION DISTINCT, RANK


#### Q3. Rather than adding a Secondary Sort to a slow Reduce job, it is Hadoop best practice to perform which optimization?

- [ ] Add a partitioned shuffle to the Map job.
- [ ] Add a partitioned shuffle to the Reduce job.
- [ ] Break the Reduce job into multiple, chained Reduce jobs.
- [ ] Break the Reduce job into multiple, chained Map jobs.


#### Q4. Hadoop Auth enforces authentication on protected resources. Once authentication has been established, it sets what type of authenticating cookie?

- [ ] encrypted HTTP
- [ ] unsigned HTTP
- [ ] compressed HTTP
- [ ] signed HTTP


#### Q5. MapReduce jobs can be written in which language?

- [ ] Java or Python
- [ ] SQL only
- [ ] SQL or Java
- [ ] Python or SQL


#### Q6. To perform local aggregation of the intermediate outputs, MapReduce users can optionally specify which object?

- [ ] Reducer
- [ ] Combiner
- [ ] Mapper
- [ ] Counter


#### Q7. To verify job status, look for the value _____ in the _____.

- [ ] SUCCEEDED; syslog
- [ ] SUCCEEDED; stdout
- [ ] DONE; syslog
- [ ] DONE; stdout


#### Q8. Which line of code implements a Reducer method in MapReduce 2.0?

- [ ] public void reduce(Text key, Iterator<IntWritable> values, Context context){…}
- [ ] public static void reduce(Text key, IntWritable[] values, Context context){…}
- [ ] public static void reduce(Text key, Iterator<IntWritable> values, Context context){…}
- [ ] public void reduce(Text key, IntWritable[] values, Context context){…}


#### Q9. To get the total number of mapped input records in a map job task, you should review the value of which counter?

- [ ] FileInputFormatCounter
- [ ] FileSystemCounter
- [ ] JobCounter
- [ ] TaskCounter


#### Q10. Hadoop Core supports which CAP capabilities?

- [ ] A, P
- [ ] C, A
- [ ] C, P
- [ ] C, A, P


#### Q11. What are the primary phases of a Reducer?

- [ ] combine, map, and reduce
- [ ] shuffle, sort, and reduce
- [ ] reduce, sort, and combine
- [ ] map, sort, and combine


#### Q12. To set up Hadoop workflow with synchronization of data between jobs that process tasks both on disk and in memory, use the _____  service, which is _____.

- [ ] Oozie; open source
- [ ] Oozie; commercial software
- [ ] Zookeeper; commercial software
- [ ] Zookeeper; open source


#### Q13. For high availability, use multiple nodes of which type?

- [ ] data
- [ ] name
- [ ] memory
- [ ] worker


#### Q14. DataNode supports which type of drives?

- [ ] hot swappable
- [ ] cold swappable
- [ ] warm swappable
- [ ] non-swappable


#### Q15. Which method is used to implement Spark jobs?

- [ ] on disk of all workers
- [ ] on disk of the master node
- [ ] in memory of the master node
- [ ] in memory of all workers

