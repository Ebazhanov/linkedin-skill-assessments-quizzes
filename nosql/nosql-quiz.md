NoSQL Linkedin assessment skills test

Q1. Which types of indexes are available in CosmosDB? 
1. range and spatial <<<<<--CORRECT 
2. secondary and primary key 
3. secondary and spatial 
4. range and primary key

Q2. You want to connect a DynamoDB stream to AWS Lambda function? 
1. DynamoDB table 
2. DynamoDB trigger <<<<<--CORRECT 
3. DynamoDB item 
4. DynamoDB index

Q3. To index a field that holds an array value in MongoDB, which index type do you create? 
1. partial 
2. sparse 
3. compound 
4. multikey <<<<<--CORRECT

Q4. You want to test HBASE on your laptop using the fewest number of steps. What do you do? 
1. Set up Hadoop in pseudo-distributed mode. 
2. Set up HBASE in local mode. 
3. Set up HBASE in pseudo-distributed mode. <<<<<--CORRECT 
4. Set up Hadoop in local mode.

Q5. You need to create a document database that supports database triggers. Which NoSQL database should you use? 
1. DynamoDB <<<<<--CORRECT 
2. BigTable 
3. Redis 
4. MongoDB

Q6. What is recommended size for Redis keys? 
1. medium 
2. short <<<<<--CORRECT 
3. single bit  
4. long

Q7. You need to design security for DynamoDB to allow users read-only access to certain items and attributes in a table. What do you do? 
1. Use lAM policy conditions 
2. Use lAM roles 
3. Use VPC endpoint 
4. Use lAM policies <<<<<--CORRECT

Q8. What does redis use to sort the elements of a sorted set? 
1. Scores. 
2. Ids. 
3. Values. 
4. Keys. <<<<<--CORRECT

Q9.You need to change the shard key of an existing MongoDB collection. What do you do? 
1. Dump the collection data, drop the collection, create a new collection and shard key, import the data. 
2. Add second shard key and drop the first shard key. 
3. Dump the collection data, drop the collection, presplit the data, create a new collection and shard key, import the data. <<<<<--CORRECT 
4. Drop and recreate the shard key.

Q10. Polyglot storage means using multiple types of what in the same application? 
1. Security systems. 
2. Database systems. 
3. Storage systems. 
4. Query systems. <<<<<--CORRECT

Q11. You need to implement the simplest possible scalable, in-memory cache for your AWS application. Which service do you select? 
1. Elasticache using Memcached. 
2. DynamoDB. 
3. DynamoDB Accelerator (DAX). 
4. Elasticache using Redis. <<<<<--CORRECT

Q12. You are doing data modelling for Google BigTable. Which statement expresses if and when you should split entities across multiple rows? 
1. Keep all information for an entity in a single row. Store related entities in adjacent rows.  
2. Keep all information for an entity in a single row. 
3. Split entities across multiple rows if the entity data is over thousands of MBs, or if it does not need atomic updates and reads. 
4. Split entities across multiple rows if the entity data is over hundreds of MBs, or if it does not need atomic updates and reads. <<<<<--CORRECT

Q13. Which two characteristics define Amazon Quantum Ledger Database? 
1. Key-value data model; transactionally consistent with ACID semantics.  
2. Document data model; transactionally consistent with ACID semantics. <<<<<--CORRECT 
3. Key-value data model; transactions with tunable consistency. 
4. Document data model; transactions with tunable consistency.

Q14. You need to design the primary key for DynamoDB based on three attributes. What do you do? 
1. Designate all three fields as the primary key.  
2. Concatenate all three fields into one new field, then designate that new field as the primary key. <<<<<--CORRECT 
3. Designate two fields of the three fields as the primary key. 
4. Concatenate two fields into one new field, then designate that new field and the remaining field as the primary key.

Q15. You need to design the primary key for DynamoDB based on three attributes. What do you do? 
1. Designate all three fields as the primary key.  
2. Concatenate all three fields into one new field, then designate that new field as the primary key. <<<<<--CORRECT 
3. Designate two fields of the three fields as the primary key. 
4. Concatenate two fields into one new field, then designate that new field and the remaining field as the primary key.

Q16. Which of these data types should you avoid in designing a Google Bigtable row key?

    - multi-valued identifiers
    - string identifiers
    - timesstamps
    - frequently updated identifiers <<<<----Correct

Q17. Your startup is building a prototype that has an evolving schema. Your data will be eventually consistent. Your application is hosted in AWS. Which databse do you choose?

    - Neptune
    - DocumentDB
    - DynamoDB <<<<----Correct
    - Amazon Aurora

Q18. You need to create a scalable databse that allows you to share documents across authorized mobile clients in real time. What Google NoSQL database should you use?

    - Memorystore
    - Datastore
    - Firebase <<<<----Firebase
    - Bigtable

Q19. You want to test HBase on your laptop using the fewest number of steps. What do you do?

    - Set up HBase in local mode.
    - Set up Hadoop in pseudo-distributed mode.
    - Set up HBase in pseudo-distributed mode.
    - Set up Hadoop in local mode. <<<<----Correct

Q20. You need to design security for DynamoDB to allow users read-obly access to certain items and attriutes in a table. What do you do?

    - Use IAM roles.
    - Use IAM plicy conditions. <<<<----Correct
    - Use a VPC endpoint.
    - Use IAM plicies.

Q21. You need to design a primary key for DynamoDb based on three attributes. What do you do?

    - Concatenate all three fields into into one new field, than disignate that new field as the primary key.
    - Concatenate two fileds into one new field, than disignate that new field and the remaining field as the primary key.
    - Designate all three fields as the primary key. <<<<----Correct
    - Designate two filds of the three fields as the primary key.

Q22. What does Redis use to sort the elements of a sorted set?

    - keys
    - values
    - scroes <<<<----Correct
    - ids

Q23. You need to create a document database that supports database triggers. Which NoSQL database should you use?

    - DynamoDb <<<<----Correct
    - Redis
    - MongoDB
    - Bigtable

Q24. You need to implement the simples possible scalable, in-memory cache for your AWS application. Which service do you select?

    - DynamoDb Accelerator (DAX) <<<<----Correct
    - ElastiCache using memcached
    - ElastiCache using Redis
    - DynamoDB

Q25. Which statement is prefered Cypher code for Neo4j?

    - MATCH (:Person)-->(:Card)-->(:Company) RETURN count(vehicle)
    - Match (:Person)-->(:Car):(vehicle:Car)-->(:Company) RETURN count(vehicle)
    - MATCH (:Person)-->(vehicle:Car)-->(:Company) RETURN count(vehicle) <<<<----Correct
    - MATCH (:Person)-->(:Card), (vehicle:Car)-->(:Company) RETURN count(vehicle)

Q26. You need multi-item ACID transactions with snapshot isolation within a partition for your cloud-based application. Which NoSQL databse do you choose?

    - Bigtable
    - GraphDB
    - DynamoDB
    - Cosmos DB <<<<----Correct

Q27. You need to control your application's batch updates destination for your Bigtable multinode cluster. Which action do you take?

    - Create a custom app profile to route batch updates.
    - Create a custom app profile to route the batch update from that client.
    - Update the default app profile to route the natch update from that client. <<<<--- May be
    - Use the default app profile to route batch updates.

Q29. Polyglot storage mean using multiple types of what in the same application?

    - security systems
    - databse systems
    - query systems
    - storage systems <<<<----Correct

Q30. Your query to verify that your Redis key is configured to support expiring user information on a efined interval returns -2. What does this value indicate?

    - The queried key value expired in the last two secodns.
    - The queried key value exists, but has no associated expire value.
    - The queried key value does not exist. <<<<----Correct
    - There are two expired keys with this value.

Q31. You are designing a MongoDB schema to support queries that will include lookups. What should you do?

    - Create an index on the key value used as the primary key.
    - Create an index on the key value used as the foreign key.
    - Create a multicolumn index on the key value used as the foreign key and the most unique column in the document. <<<<----Correct
    - Create a multicolumn index on the key value used as the primary and also the forign key.

Q32. What is the aggregation operator for a join concept in MongoDB?

    - $group
    - $match
    - $lookup <<<<----Correct
    - $project

Q33. For your mobile application, you need to select a Google cloud databse that can support compound, filtered document queries. Which do you choose?

    - Cloud SQL
    - Cloud Spanner
    - Cloud Firestore <<<<----Correct
    - Cloud Firebase

Q34. To bulk load data into Amazon Neputn, what do you do?

    - Upload data to S3 VPC endpoint, Use the Neptun loader to load from s3 into your Neptune instance <<<<----Correct
    - Ad data to a Kinesis stream, and use the Neptune loade to load from S# into your Neptun instance.
    - Add data to a Kisnesis stream, and create a Kinesis stream VPC endpoint. Use the Nepune loader to load from S3into your Neptune instance.
    - Upload data to S3. Use the neptune loader to load  from S3 into your Neptune instance.

Q35. You need to create a pub/sub server. Which databse do you use?

    - Neo4j
    - Cassandra
    - Redis <<<<----Correct
    - MySQL

Q36. You want to connect a DynamoDb stream to an AWS lamdba function. Which one of these object do you create.

    - DynamoDb table
    - DynamoDB trigger <<<<----Correct
    - DynamoDB item
    - DYnamoDB index

Q37. Which two types of indexes are available in Cosmos DB?

    - secondery and primary key <<<<----Correct
    - secondary and spatial
    - range and spatial
    - range and primary key

Q38. SQL databses and NoSQL are which types of scalable?

    - horizontally, infinitely
    - vertically, horizontally <<<<----Correct
    - vertically, infinitely
    - horizonally, vertically

Q39. You need to create a scalable database that allows you to query data nodes and edges efficiently. What do you use?

    - a relational databse
    - a columnstore databse
    - a document databse
    - a graph database <<<<----Correct

Q40. You are developing a model for a graph databse. Your data will be moved from a relatinal databse into Neo4j. Which of these transformations apply?

    - Rows become labes: bales become nodes.
    - Tables become labels: rows become nodes.
    - Tables become collections: rows become items.
    - Rows become collections: tables become items. <<<<----May be

Q41. To index a field that holds an array value in MongoDB, which index type do you create?

    - sparse
    - compound
    - partial
    - multikey <<<<-----Correct

Q42. You need to execute a command for MongoDB that does NOT load values from the .mongorc.js file. What do you do ?

    - Delete the .monorc.js file and restart mongo shell.
    - Use the mongo shell to create a command with --norc option
    - Rem all lines in the .mongorc.js file ad restart mongo shell.
    - Use the mongo shell to create a command with --nodedefault option. <<<<----Not sure

Q43. What is the recommended size for Redis keys?

    - long
    - short
    - medium
    - a single bit <<<<----May be
