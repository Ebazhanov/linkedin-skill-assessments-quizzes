## NoSQL

#### Q1. Which types of indexes are available in CosmosDB?

- [x] range and spatial
- [ ] secondary and primary key
- [ ] secondary and spatial
- [ ] range and primary key

#### Q2. You want to connect a DynamoDB stream to AWS Lambda function?

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
- [ ] Set up HBASE in local mode.
- [x] Set up HBASE in pseudo-distributed mode.
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

#### Q7. You need to design security for DynamoDB to allow users read-only access to certain items and attributes in a table. What do you do?

- [ ] Use lAM policy conditions
- [ ] Use lAM roles
- [ ] Use VPC endpoint
- [x] Use lAM policies

#### Q8. What does redis use to sort the elements of a sorted set?

- [ ] Scores.
- [ ] Ids.
- [ ] Values.
- [x] Keys.

#### Q9.You need to change the shard key of an existing MongoDB collection. What do you do?

- [ ] Dump the collection data, drop the collection, create a new collection and shard key, import the data.
- [ ] Add second shard key and drop the first shard key.
- [x] Dump the collection data, drop the collection, presplit the data, create a new collection and shard key, import the data.
- [ ] Drop and recreate the shard key.

#### Q10. Polyglot storage means using multiple types of what in the same application?

- [ ] Security systems.
- [ ] Database systems.
- [ ] Storage systems.
- [x] Query systems.

#### Q11. You need to implement the simplest possible scalable, in-memory cache for your AWS application. Which service do you select?

- [ ] Elasticache using Memcached.
- [ ] DynamoDB.
- [ ] DynamoDB Accelerator (DAX).
- [x] Elasticache using Redis.

#### Q12. You are doing data modelling for Google BigTable. Which statement expresses if and when you should split entities across multiple rows?

- [ ] Keep all information for an entity in a single row. Store related entities in adjacent rows.
- [ ] Keep all information for an entity in a single row.
- [ ] Split entities across multiple rows if the entity data is over thousands of MBs, or if it does not need atomic updates and reads.
- [x] Split entities across multiple rows if the entity data is over hundreds of MBs, or if it does not need atomic updates and reads.

#### Q13. Which two characteristics define Amazon Quantum Ledger Database?

- [ ] Key-value data model; transactionally consistent with ACID semantics.
- [x] Document data model; transactionally consistent with ACID semantics.
- [ ] Key-value data model; transactions with tunable consistency.
- [ ] Document data model; transactions with tunable consistency.

#### Q14. You need to design the primary key for DynamoDB based on three attributes. What do you do?

- [ ] Designate all three fields as the primary key.
- [x] Concatenate all three fields into one new field, then designate that new field as the primary key.
- [ ] Designate two fields of the three fields as the primary key.
- [ ] Concatenate two fields into one new field, then designate that new field and the remaining field as the primary key.

#### Q15. You need to design the primary key for DynamoDB based on three attributes. What do you do?

- [ ] Designate all three fields as the primary key.
- [x] Concatenate all three fields into one new field, then designate that new field as the primary key.
- [ ] Designate two fields of the three fields as the primary key.
- [ ] Concatenate two fields into one new field, then designate that new field and the remaining field as the primary key.

#### Q16. Which of these data types should you avoid in designing a Google Bigtable row key?

- [ ] multi-valued identifiers
- [ ] string identifiers
- [ ] timesstamps
- [x] frequently updated identifiers

#### Q17. Your startup is building a prototype that has an evolving schema. Your data will be eventually consistent. Your application is hosted in AWS. Which databse do you choose?

- [ ] Neptune
- [ ] DocumentDB
- [x] DynamoDB
- [ ] Amazon Aurora

#### Q18. You need to create a scalable databse that allows you to share documents across authorized mobile clients in real time. What Google NoSQL database should you use?

- [ ] Memorystore
- [ ] Datastore
- [x] Firebase
- [ ] Bigtable

#### Q19. You want to test HBase on your laptop using the fewest number of steps. What do you do?

- [ ] Set up HBase in local mode.
- [ ] Set up Hadoop in pseudo-distributed mode.
- [ ] Set up HBase in pseudo-distributed mode.
- [x] Set up Hadoop in local mode.

#### Q20. You need to design security for DynamoDB to allow users read-obly access to certain items and attriutes in a table. What do you do?

- [ ] Use IAM roles.
- [x] Use IAM plicy conditions.
- [ ] Use a VPC endpoint.
- [ ] Use IAM plicies.

#### Q21. You need to design a primary key for DynamoDb based on three attributes. What do you do?

- [ ] Concatenate all three fields into into one new field, than disignate that new field as the primary key.
- [ ] Concatenate two fileds into one new field, than disignate that new field and the remaining field as the primary key.
- [x] Designate all three fields as the primary key.
- [ ] Designate two filds of the three fields as the primary key.

#### Q22. What does Redis use to sort the elements of a sorted set?

- [ ] keys
- [ ] values
- [x] scroes
- [ ] ids

#### Q23. You need to create a document database that supports database triggers. Which NoSQL database should you use?

- [x] DynamoDb
- [ ] Redis
- [ ] MongoDB
- [ ] Bigtable

#### Q24. Which statement is prefered Cypher code for Neo4j?

- [ ] MATCH (:Person)-->(:Card)-->(:Company) RETURN count(vehicle)
- [ ] Match (:Person)-->(:Car):(vehicle:Car)-->(:Company) RETURN count(vehicle)
- [x] MATCH (:Person)-->(vehicle:Car)-->(:Company) RETURN count(vehicle)
- [ ] MATCH (:Person)-->(:Card), (vehicle:Car)-->(:Company) RETURN count(vehicle)

#### Q25. You need multi-item ACID transactions with snapshot isolation within a partition for your cloud-based application. Which NoSQL databse do you choose?

- [ ] Bigtable
- [ ] GraphDB
- [ ] DynamoDB
- [x] Cosmos DB

#### Q26. You need to control your application's batch updates destination for your Bigtable multinode cluster. Which action do you take?

- [ ] Create a custom app profile to route batch updates.
- [ ] Create a custom app profile to route the batch update from that client.
- [x] Update the default app profile to route the natch update from that client.
- [ ] Use the default app profile to route batch updates.

#### Q27. Polyglot storage mean using multiple types of what in the same application?

- [ ] security systems
- [ ] databse systems
- [ ] query systems
- [x] storage systems

#### Q28. Your query to verify that your Redis key is configured to support expiring user information on a defined interval returns -2, What does this value indicate?

- [ ] The queried key value expired in the last two secodns.
- [ ] The queried key value exists, but has no associated expire value.
- [x] The queried key value does not exist.
- [ ] There are two expired keys with this value.

#### Q29. You are designing a MongoDB schema to support queries that will include lookups. What should you do?

- [ ] Create an index on the key value used as the primary key.
- [ ] Create an index on the key value used as the foreign key.
- [x] Create a multicolumn index on the key value used as the foreign key and the most unique column in the document.
- [ ] Create a multicolumn index on the key value used as the primary and also the forign key.

#### Q30. What is the aggregation operator for a join concept in MongoDB?

- [ ] \$group
- [ ] \$match
- [x] \$lookup
- [ ] \$project

#### Q31. For your mobile application, you need to select a Google cloud databse that can support compound, filtered document queries. Which do you choose?

- [ ] Cloud SQL
- [ ] Cloud Spanner
- [x] Cloud Firestore
- [ ] Cloud Firebase

#### Q32. To bulk load data into Amazon Neputn, what do you do?

- [x] Upload data to S3 VPC endpoint, Use the Neptun loader to load from s3 into your Neptune instance
- [ ] Ad data to a Kinesis stream, and use the Neptune loade to load from S# into your Neptun instance.
- [ ] Add data to a Kisnesis stream, and create a Kinesis stream VPC endpoint. Use the Nepune loader to load from S3into your Neptune instance.
- [ ] Upload data to S Use the neptune loader to load from S3 into your Neptune instance.

#### Q33. You need to create a pub/sub server. Which databse do you use?

- [ ] Neo4j
- [ ] Cassandra
- [x] Redis
- [ ] MyS#### QL

#### Q34. You want to connect a DynamoDb stream to an AWS lamdba function. Which one of these object do you create.

- [ ] DynamoDb table
- [x] DynamoDB trigger
- [ ] DynamoDB item
- [ ] DYnamoDB index

#### Q35. Which two types of indexes are available in Cosmos DB?

- [x] secondery and primary key
- [ ] secondary and spatial
- [ ] range and spatial
- [ ] range and primary key

#### Q36. SQL databses and NoSQL are which types of scalable?

- [ ] horizontally, infinitely
- [x] vertically, horizontally
- [ ] vertically, infinitely
- [ ] horizonally, vertically

#### Q37. You need to create a scalable database that allows you to query data nodes and edges efficiently. What do you use?

- [ ] a relational databse
- [ ] a columnstore databse
- [ ] a document databse
- [x] a graph database

#### Q38. You are developing a model for a graph database. Your data will be moved from a relational database into Neo4j. Which of these transformations apply?

- [ ] Rows become labes: bales become nodes.
- [ ] Tables become labels: rows become nodes.
- [ ] Tables become collections: rows become items.
- [x] Rows become collections: tables become items.

#### Q39. To index a field that holds an array value in MongoDB, which index type do you create?

- [ ] sparse
- [ ] compound
- [ ] partial
- [x] multikey

#### Q40. You need to execute a command for MongoDB that does NOT load values from the `.mongorc.js` file. What do you do ?

- [ ] Delete the .monorc.js file and restart mongo shell.
- [ ] Use the mongo shell to create a command with --norc option
- [ ] Rem all lines in the .mongorc.js file ad restart mongo shell.
- [x] Use the mongo shell to create a command with --nodedefault option.

#### Q41. What is the recommended size for Redis keys?

- [ ] long
- [ ] short
- [ ] medium
- [x] a single bit

#### Q42. You need to store an unordered collection of name-value pairs with differing data types in DynamoDB. Which data type should you choose?

- [x] map
- [ ] set
- [ ] list
- [ ] stack

#### Q43. Which statement retrieves an item from the MusicCollection table in DynamoDB?

- [ ] aws dynamodb query --table-name MusicCollection --key file://key.json
- [x] aws dynamodb get-item --table-name MusicCollection --key file://key.json
- [ ] aws dynamodb select --table-name MusicCollection --key file://key.json
- [ ] aws dynamodb put-item --table-name MusicCollection --key file://key.json

#### Q44. Database availability is measured by which metric?

- [ ] the amount of service calls
- [ ] the number of minutes
- [ ] the amount of service costs
- [x] the number of nines

#### Q45. You need to encrypt data at rest in DynamoDB. Which action do you take?

- [ ] You assign a default AWS encryption key to your table to encrypt data.
- [ ] You create an AWS encryption key and assign it to your table to encrypt data.
- [x] None. Data is encrypted by default.
- [ ] You create an AWS encryption key and assign it to your database to encrypt data.

#### Q46. You need to generate a unique, sequential identifier for each value stored in a Redis cluster. What do you do?

- [ ] Implement a SortedSet object to generate a value.
- [ ] Use the GUID keyword to generate a value.
- [ ] Implement a List object to generate a value.
- [x] Use the INCR keyword to generate a value

#### Q47. You want to return a list of all elements in two Redis sets. Which keyword do you use?

- [x] smembers
- [ ] returnall
- [ ] sunion
- [ ] sismember

#### Q48. Which method shows you whether MongoDB uses any indexes when running a query, and how the indexes are used?

- [ ] detailQueryExecution()
- [ ] showPlan()
- [x] explain()
- [ ] describe()

#### Q49. Which statement accurately describes global secondary indexes in DynamoDB?

- [ ] The global secondary indexes in DynamoDB are consistent, and are not guaranteed to return correct results.
- [ ] The global secondary indexes in DynamoDB are transactionally consistent, and are guaranteed to return correct results.
- [ ] The global secondary indexes in DynamoDB are partially consistent, and are not guaranteed to return correct results.
- [x] The global secondary indexes in DynamoDB are eventually consistent, and are not guaranteed to return correct results.

[reference link:](https://stackoverflow.com/questions/35414372/dynamodb-consistent-reads-for-global-secondary-index)

#### Q50. Which command do you use to add a value to a Redis stream named mystream?

- [ ] ADD mystream \* sensor-id 1234 temperature 19.8 1518951480106-1
- [ ] UPDATE mystream \* sensor-id 1234 temperature 19.8 1518951480106-3
- [x] XADD mystream \* sensor-id 1234 temperature 9.8 1518951480106-0
- [ ] INSERT mystream \* sensor-d 1234 temperature 19.8 15181480106-2

#### Q51. Which code example completes this statement and creates an index for a MongoDB object named restaurants, sorted ascending by the field name?

```
var indexCollection = function(db) {return co(function*() {...});};
```

- [ ] `const results = yield db.table('restaurants').createIndex({"name": 1}, null); return results;`
- [ ] `const results = yield db.collection('restaurants').createIndex({"name": 0}, null); return results;`
- [x] `const results = yield db.collection('restaurants').createIndex({"name": 1}, null); return results;`
- [ ] `const results = yield db.table('restaurants').createIndex({"name": 0}, null); return results;`

#### Q52. Which Cypher code executes the multiquery block?

- [ ]

```
MATCH (c:Company {name: 'Neo4j'}) RETURN c, MATCH (p:Person) WHERE p.name = 'Jennifer' RETURN p,
MATCH (t:Technology)-[:LIKES]-(a:Person {name: 'Jennifer'}) RETURN t.type;
```

- [ ]

```
MATCH (c:Company {name: 'Neo4j'}) RETURN c, MATCH (p:Person) WHERE p.name = 'Jennifer' RETURN p,
MATCH (t:Technology)-[:LIKES]-(a:Person {name: 'Jennifer'}) RETURN t.type
```

- [ ]

```
MATCH (c:Company {name: 'Neo4j'}) RETURN c AND MATCH (p:Person) WHERE p.name = 'Jennifer' RETURN p,
AND MATCH (t:Technology)-[:LIKES]-(a:Person {name: 'Jennifer'}) RETURN t.type;
```

- [ ]

```
MATCH (c:Company {name: 'Neo4j'}) RETURN c;MATCH (p:Person) WHERE p.name = 'Jennifer' RETURN p;
MATCH (t:Technology)-[:LIKES]-(a:Person {name: 'Jennifer'}) RETURN t.type;
```

### Q53. You need to create a scalable database that supports immutable writes. What do you use?

- [x] A ledger database
- [ ] A graph database
- [ ] A key-value database
- [ ] A columnstore database

#### Q54. You need to create a data store for the catalog for your new ecommerce application. Your company is a startup, so the catalog schema may evolve. Which do you choose?

- [ ] Neo4j
- [ ] Redis
- [ ] MySQL
- [x] MongoDB

#### Q55. You need to select a NoSQL database for heavy aggregate query workloads. Which type do you choose?

- [ ] graph
- [ ] key-value
- [ ] document
- [x] columnstore
