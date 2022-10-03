## NoSQL

#### Q1. Which types of indexes are available in CosmosDB?

- [x] range and spatial
- [ ] secondary and primary key
- [ ] secondary and spatial
- [ ] range and primary key

#### Q2. You want to connect a DynamoDB stream to AWS Lambda function. Which one of these object do you create?

- [ ] DynamoDB table
- [x] DynamoDB trigger
- [ ] DynamoDB item
- [ ] DynamoDB index

#### Q3. To index a field that holds an array value in MongoDB, which index type do you create?

- [ ] partial
- [ ] sparse
- [ ] compound
- [x] multikey

#### Q4. You want to test HBASE on your laptop using the fewest number of steps. What do you do?

- [ ] Set up Hadoop in pseudo-distributed mode.
- [x] Set up HBASE in local mode.
- [ ] Set up HBASE in pseudo-distributed mode.
- [ ] Set up Hadoop in local mode.

#### Q5. You need to create a document database that supports database triggers. Which NoSQL database should you use?

- [x] DynamoDB
- [ ] BigTable
- [ ] Redis
- [ ] MongoDB

#### Q6. What is recommended size for Redis keys?

- [ ] medium
- [x] short
- [ ] single bit
- [ ] long

#### Q7. What does Redis use to sort the elements of a sorted set?

- [x] Scores
- [ ] Ids
- [ ] Values
- [ ] Keys

#### Q8. You need to change the shard key of an existing MongoDB collection. What do you do?

- [ ] Dump the collection data, drop the collection, create a new collection and shard key, import the data.
- [ ] Add second shard key and drop the first shard key.
- [x] Dump the collection data, drop the collection, presplit the data, create a new collection and shard key, import the data.
- [ ] Drop and recreate the shard key.

#### Q9. Polyglot storage means using multiple types of what in the same application?

- [ ] Security systems
- [ ] Database systems
- [x] Storage systems
- [ ] Query systems

#### Q10. You need to implement the simplest possible scalable, in-memory cache for your AWS application. Which service do you select?

- [ ] Elasticache using Memcached.
- [ ] DynamoDB.
- [ ] DynamoDB Accelerator (DAX).
- [x] Elasticache using Redis.

#### Q11. You are doing data modelling for Google BigTable. Which statement expresses if and when you should split entities across multiple rows?

- [ ] Keep all information for an entity in a single row. Store related entities in adjacent rows.
- [ ] Keep all information for an entity in a single row.
- [ ] Split entities across multiple rows if the entity data is over thousands of MBs, or if it does not need atomic updates and reads.
- [x] Split entities across multiple rows if the entity data is over hundreds of MBs, or if it does not need atomic updates and reads.

#### Q12. Which two characteristics define Amazon Quantum Ledger Database?

- [ ] Key-value data model; transactionally consistent with ACID semantics.
- [x] Document data model; transactionally consistent with ACID semantics.
- [ ] Key-value data model; transactions with tunable consistency.
- [ ] Document data model; transactions with tunable consistency.

#### Q13. You need to design the primary key for DynamoDB based on three attributes. What do you do?

- [ ] Designate all three fields as the primary key.
- [x] Concatenate all three fields into one new field, then designate that new field as the primary key.
- [ ] Designate two fields of the three fields as the primary key.
- [ ] Concatenate two fields into one new field, then designate that new field and the remaining field as the primary key.

#### Q14. Which of these data types should you avoid in designing a Google Bigtable row key?

- [ ] multi-valued identifiers
- [ ] string identifiers
- [ ] timestamps
- [x] frequently updated identifiers

#### Q15. Your startup is building a prototype that has an evolving schema. Your data will be eventually consistent. Your application is hosted in AWS. Which database do you choose?

- [ ] Neptune
- [ ] DocumentDB
- [x] DynamoDB
- [ ] Amazon Aurora

#### Q16. You need to create a scalable database that allows you to share documents across authorized mobile clients in real time. What Google NoSQL database should you use?

- [ ] Memorystore
- [ ] Datastore
- [x] Firebase
- [ ] Bigtable

#### Q17. You need to design security for DynamoDB to allow users read-only access to certain items and attributes in a table. What do you do?

- [ ] Use IAM roles.
- [x] Use IAM policy conditions.
- [ ] Use a VPC endpoint.
- [ ] Use IAM policies.

#### Q18. Which statement is preferred Cypher code for Neo4j?

- [ ] MATCH (:Person)-->(:Card)-->(:Company) RETURN count(vehicle)
- [ ] Match (:Person)-->(:Car):(vehicle:Car)-->(:Company) RETURN count(vehicle)
- [x] MATCH (:Person)-->(vehicle:Car)-->(:Company) RETURN count(vehicle)
- [ ] MATCH (:Person)-->(:Card), (vehicle:Car)-->(:Company) RETURN count(vehicle)

#### Q19. You need multi-item ACID transactions with snapshot isolation within a partition for your cloud-based application. Which NoSQL databse do you choose?

- [ ] Bigtable
- [ ] GraphDB
- [ ] DynamoDB
- [x] Cosmos DB

#### Q20. You need to control your application's batch updates destination for your Bigtable multinode cluster. Which action do you take?

- [ ] Create a custom app profile to route batch updates.
- [ ] Create a custom app profile to route the batch update from that client.
- [x] Update the default app profile to route the natch update from that client.
- [ ] Use the default app profile to route batch updates.

#### Q21. Your query to verify that your Redis key is configured to support expiring user information on a defined interval returns -2, What does this value indicate?

- [ ] The queried key value expired in the last two seconds.
- [ ] The queried key value exists, but has no associated expire value.
- [x] The queried key value does not exist.
- [ ] There are two expired keys with this value.

#### Q22. You are designing a MongoDB schema to support queries that will include lookups. What should you do?

- [ ] Create an index on the key value used as the primary key.
- [ ] Create an index on the key value used as the foreign key.
- [x] Create a multicolumn index on the key value used as the foreign key and the most unique column in the document.
- [ ] Create a multicolumn index on the key value used as the primary and also the foreign key.

#### Q23. What is the aggregation operator for a join concept in MongoDB?

- [ ] \$group
- [ ] \$match
- [x] \$lookup
- [ ] \$project

#### Q24. For your mobile application, you need to select a Google cloud databse that can support compound, filtered document queries. Which do you choose?

- [ ] Cloud SQL
- [ ] Cloud Spanner
- [x] Cloud Firestore
- [ ] Cloud Firebase

#### Q25. To bulk load data into Amazon Neptune, what do you do?

- [x] Upload data to S3 VPC endpoint, Use the Neptune loader to load from s3 into your Neptune instance
- [ ] Ad data to a Kinesis stream, and use the Neptune loader to load from S# into your Neptune instance.
- [ ] Add data to a Kinesis stream, and create a Kinesis stream VPC endpoint. Use the Neptune loader to load from S3 into your Neptune instance.
- [ ] Upload data to S Use the Neptune loader to load from S3 into your Neptune instance.

#### Q26. You need to create a pub/sub server. Which database do you use?

- [ ] Neo4j
- [ ] Cassandra
- [x] Redis
- [ ] MyS#### QL

#### Q27. SQL databases and NoSQL are which types of scalable?

- [ ] horizontally, infinitely
- [x] vertically, horizontally
- [ ] vertically, infinitely
- [ ] horizontally, vertically

#### Q28. You need to create a scalable database that allows you to query data nodes and edges efficiently. What do you use?

- [ ] a relational database
- [ ] a columnstore database
- [ ] a document database
- [x] a graph database

#### Q29. You are developing a model for a graph database. Your data will be moved from a relational database into Neo4j. Which of these transformations apply?

- [ ] Rows become labels: bales become nodes.
- [x] Tables become labels: rows become nodes.
- [ ] Tables become collections: rows become items.
- [ ] Rows become collections: tables become items.

#### Q30. You need to execute a command for MongoDB that does NOT load values from the `.mongorc.js` file. What do you do ?

- [ ] Delete the .monorc.js file and restart mongo shell.
- [ ] Use the mongo shell to create a command with --norc option
- [ ] Rem all lines in the .mongorc.js file ad restart mongo shell.
- [x] Use the mongo shell to create a command with --nodedefault option.

#### Q31. You need to store an unordered collection of name-value pairs with differing data types in DynamoDB. Which data type should you choose?

- [x] map
- [ ] set
- [ ] list
- [ ] stack

#### Q32. Which statement retrieves an item from the MusicCollection table in DynamoDB?

- [ ] aws dynamodb query --table-name MusicCollection --key file://key.json
- [x] aws dynamodb get-item --table-name MusicCollection --key file://key.json
- [ ] aws dynamodb select --table-name MusicCollection --key file://key.json
- [ ] aws dynamodb put-item --table-name MusicCollection --key file://key.json

#### Q33. Database availability is measured by which metric?

- [ ] the amount of service calls
- [ ] the number of minutes
- [ ] the amount of service costs
- [x] the number of nines

#### Q34. You need to encrypt data at rest in DynamoDB. Which action do you take?

- [ ] You assign a default AWS encryption key to your table to encrypt data.
- [ ] You create an AWS encryption key and assign it to your table to encrypt data.
- [x] None. Data is encrypted by default.
- [ ] You create an AWS encryption key and assign it to your database to encrypt data.

#### Q35. You need to generate a unique, sequential identifier for each value stored in a Redis cluster. What do you do?

- [ ] Implement a SortedSet object to generate a value.
- [ ] Use the GUID keyword to generate a value.
- [ ] Implement a List object to generate a value.
- [x] Use the INCR keyword to generate a value

#### Q36. You want to return a list of all elements in two Redis sets. Which keyword do you use?

- [x] smembers
- [ ] returnall
- [ ] sunion
- [ ] sismember

#### Q37. Which method shows you whether MongoDB uses any indexes when running a query, and how the indexes are used?

- [ ] detailQueryExecution()
- [ ] showPlan()
- [x] explain()
- [ ] describe()

#### Q38. Which statement accurately describes global secondary indexes in DynamoDB?

- [ ] The global secondary indexes in DynamoDB are consistent, and are not guaranteed to return correct results.
- [ ] The global secondary indexes in DynamoDB are transactionally consistent, and are guaranteed to return correct results.
- [ ] The global secondary indexes in DynamoDB are partially consistent, and are not guaranteed to return correct results.
- [x] The global secondary indexes in DynamoDB are eventually consistent, and are not guaranteed to return correct results.

[reference link:](https://stackoverflow.com/questions/35414372/dynamodb-consistent-reads-for-global-secondary-index)

#### Q39. Which command do you use to add a value to a Redis stream named mystream?

- [ ] ADD mystream \* sensor-id 1234 temperature 19.8 1518951480106-1
- [ ] UPDATE mystream \* sensor-id 1234 temperature 19.8 1518951480106-3
- [x] XADD mystream \* sensor-id 1234 temperature 9.8 1518951480106-0
- [ ] INSERT mystream \* sensor-d 1234 temperature 19.8 15181480106-2

#### Q40. Which code example completes this statement and creates an index for a MongoDB object named restaurants, sorted ascending by the field name?

```
var indexCollection = function(db) {return co(function*() {...});};
```

- [ ] `const results = yield db.table('restaurants').createIndex({"name": 1}, null); return results;`
- [ ] `const results = yield db.collection('restaurants').createIndex({"name": 0}, null); return results;`
- [x] `const results = yield db.collection('restaurants').createIndex({"name": 1}, null); return results;`
- [ ] `const results = yield db.table('restaurants').createIndex({"name": 0}, null); return results;`

#### Q41. Which Cypher code executes the multiquery block?

- [ ] A

```
MATCH (c:Company {name: 'Neo4j'}) RETURN c, MATCH (p:Person) WHERE p.name = 'Jennifer' RETURN p,
MATCH (t:Technology)-[:LIKES]-(a:Person {name: 'Jennifer'}) RETURN t.type;
```

- [ ] B

```
MATCH (c:Company {name: 'Neo4j'}) RETURN c, MATCH (p:Person) WHERE p.name = 'Jennifer' RETURN p,
MATCH (t:Technology)-[:LIKES]-(a:Person {name: 'Jennifer'}) RETURN t.type
```

- [ ] C

```
MATCH (c:Company {name: 'Neo4j'}) RETURN c AND MATCH (p:Person) WHERE p.name = 'Jennifer' RETURN p,
AND MATCH (t:Technology)-[:LIKES]-(a:Person {name: 'Jennifer'}) RETURN t.type;
```

- [ ] D

```
MATCH (c:Company {name: 'Neo4j'}) RETURN c;MATCH (p:Person) WHERE p.name = 'Jennifer' RETURN p;
MATCH (t:Technology)-[:LIKES]-(a:Person {name: 'Jennifer'}) RETURN t.type;
```

#### Q42. You need to create a scalable database that supports immutable writes. What do you use?

- [x] A ledger database
- [ ] A graph database
- [ ] A key-value database
- [ ] A columnstore database

#### Q43. You need to create a data store for the catalog for your new ecommerce application. Your company is a startup, so the catalog schema may evolve. Which do you choose?

- [ ] Neo4j
- [ ] Redis
- [ ] MySQL
- [x] MongoDB

#### Q44. You need to select a NoSQL database for heavy aggregate query workloads. Which type do you choose?

- [ ] graph
- [ ] key-value
- [ ] document
- [x] columnstore

#### Q45. You need to select a columnstore database that enforce built-in data types. You want to add indexes to improve performance for known workloads. Which do you choose?

- [ ] Cassandra
- [ ] Bigtable
- [x] Redis
- [ ] HBase

#### Q46. In DynamoDB, the partition key and sort key are also known as which type of attributes?

- [ ] range, hash
- [ ] primary, range
- [x] hash, range
- [ ] range, secondary

#### Q47. What is a popular, open-source key-value store database?

- [ ] MongoDB
- [x] Redis
- [ ] MySQL
- [ ] Cassandra

#### Q48. You need to create a scalable database to store and query JSON data. What do you use?

- [ ] a relational database
- [x] a document database
- [ ] a graph database
- [ ] a ledger database

[store and query JSON](https://aws.amazon.com/nosql/document/#:~:text=The%20document%20database%20defined,use%20in%20their%20application%20code.)
