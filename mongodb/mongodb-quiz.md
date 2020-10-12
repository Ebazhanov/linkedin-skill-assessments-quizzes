MongoDB Assessment
-----------------

#### Q1. Which command adds members to the replica set from MongoDB shell?
- rs.add("<hostname>") <<<<<--CORRECT
- replicaSetAdd("<hostname>")
- rs.insert("<hostname>")
- replica.add("<hostname>")

#### Q2. Which MongoDB shell command should you use to back up a database?
- restore
- backup
- mongobackup
- mongodump <<<<---CORRECT

#### Q3. Which shell query displays all citizens with an age greater than or equal to 21?
- db.citizens.select('WHERE age >= 21')
- db.citizens.select('age >= 21')
- db.citizens.select('WHERE age >= 21')
- db.citizens.select({age: {$qte: 21}}) <<<<<----CORRECT

#### Q4. What does a MongoDB collection consist of?
- data
- documents <<<<<----CORRECT
- fields
- rows

#### Q5. Given an ObjectId in _id, how do you get the time it was created?
- getDateTime(_id)
- _id.createDate()
- _id.getTimestamp() <<<<---CORRECT
- _id.getDateTime()

#### Q6. Given a cursor named myCursor, which command returns a boolean value?
[x] myCursor.hasNext()
[ ] myCursor.sort()
[ ] myCursor.next()
[ ] myCursor.find()

#### Q7. Which command returns a specific document in the user's collection?
- db.users.find({_id: 1}) <<<<---CORRECT
- db.users.seek({_id: 1})
- db.users.query({_id: 1})
- db.query.users({_id: 1})

#### Q8. To import a JSON array into Mongo, what flags are needed with MongoDBimport?
-  `--type jsonArray`
-  `--json`
-  `--type json`
-  `--jsonArray` <<<<---CORRECT

#### Q9. Choose the shell command that connects to a MongoDB database.
- mongo <<<<--CORRECT
- mongod
- mongoconnect
- dbconnect

#### Q10. In the MongoDB shell, how can you tell if an index was used with a query?
- db.customers.find({lastName: 'smith'}).explain() <<<<---CORRECT
- db.customers.find({lastName: 'smith'}).perf()
- db.customers.find({lastName: 'smith'}).plan()
- db.customers.find({lastName: 'smith'}).usedIndex()

#### Q11. Suppose your aggregation pipeline terminated with an exception referring to exceeded memory limit. What is the best way to resolve the issue?
- Set useMemory to twice amount indicated in exception.
- Switch a 64 bit instance of MongoDB.
- Increase the memory of the MongoDB server.
- Set allowDiskUse to true. <<<<---CORRECT

#### Q12. What is the recommended way to delete a user?
[ ] db.deleteUser("user")
[ ] db.removeUser("user") DEPRECATED
[ ] db.remove("user")
[x] db.dropUser("user")

#### Q13. What the primary database in a replica set fails, when does failover begin?
- once the primary has been down for 10 minutes
- once the primary reboots
- immediately <<<---CORRECT
- after the administrator reboots the primary

#### Q14. What is the correct option to set up Kerberos when starting MongoDBd?
- `--setParameter authenticationMechanisms=GSSAPI` <<<---CORRECT
- `--setAuthentication=GSSAPI`
- `--setParam auth=K`
- `--setAuth method=Kerberos`

#### Q15. What is the purpose of an arbiter in a replica set?
- It monitors replica set and sends email in case of failure
- It casts the tie-breaking vote in an election. <<<---CORRECT
- It holds a backup copy of the database.
- It reboots the failed server.

#### Q16. You would like to know how many types of items you have in each category. Which query does this?

	1. db.product.group({_id: "$category", count: {$sum:1}})
	2. db.product.aggregate($sum: {_id: "$category", count: {$group:1}}})
	3. db.product.aggregate($group: {_id: "$category", count: {$sum:1}}})    <<<<<--CORRECT
	4. db.product.aggregate($count: {_id: "$category", count: {$group:1}}})

#### Q17. To restrict the number of records coming back from a query, which command should you use? 
	
	1. take
	2. limit    <<<<<--CORRECT
	3. max
	4. skip
	
#### Q18. We have a collection named restaurants with the geographical information stored in the location property, how do you create a geospatial index on it?
	
	1. db.restaurants.CreateIndex({location: "2dsphere"}) <<<<<--CORRECT
	2. db.restaurants.geospatial({location: "2dsphere"})
	3. db.restaurants.CreateIndex("2dsphere":"location")
	4. db.restaurants.CreateIndex({geospatial: "location"})
	
#### Q19. How do you find documents with a matching item in an embedded array?
	
	1. db.customers.findmatch ({"jobs":"secretary"}) 
	2. db.customers.find ({"jobs:secretary"})
	3. db.customers.find ({"jobs":["secretary"]})
	4. db.customers.find ({"jobs":"secretary"}) <<<<<--CORRECT
	
	
#### Q20. Which query bypasses the first 5 customers and returns the next 10?
	
	1. db.customers.find({}, {skip: 5, limit: 10})
	2. db.customers.find({}.page(5).take(10)
	3. db.customers.find({}).skip(5).take(10)
	4. db.customers.find({}).skip(5).limit(10) <<<<<--CORRECT
	
#### Q21. How do you create a text index?
	
	1. db.customers.createIndex({firstName, lastName})
	2. db.customers.createTextIndex({firstName, lastName})
	3. db.customers.createIndex({firstName: "text", lastName: "text"})  <<<<<--CORRECT
	4. db.customers.createText({firstName: 1, lastName: 1}) 
	
	
#### Q22. Assuming you have customers collection with a firstName and lastName field, which is the correct MongoDB shell command to create an index on lastName, then firstName both ascending?
	
	1. db.customers.createIndex("lastName, firstName, ASC")
	2. db.customers.addIndex({lastName:"ASC", firstName: "ASC"})
	3. db.customers.newIndex({lastName:1, firstName:1})
	4. db.customers.createIndex({lastName:1, firstName: 1})     <<<<<--CORRECT 
	
#### Q23. One of the documents in your collection has an _ id based upon an older database design and you want to change it. You write an update command to find the document and replace the _ id but the _ id isnt changed. How should you fix the issue?
	
	1. Set the replace option to true.
	2. Use the replaceOne() command instead.
	3. You cant. Once set the _ id field cannot be changed.  <<<<<--CORRECT
	4. Use the updateOne() command instead.
	
#### Q24. A compound index allows you to ___ ?
	
	1. Calculate interest quickly.
	2. Accomplish nothing, since compound indexes arent allowed in Mongo.
	3. Use more than one field per index.
	4. Combine fields in different collations.    <<<<<--CORRECT
	
#### Q25. Why are ad-hoc queries useful?
	
	1. They do not have to use the same operators.
	2. You do not need to structure the database to support them.
	3. They autogenerate reports.
	4. They run faster than indexed queries.    <<<<<--CORRECT

#### Q26. How often do the members of a replica set send heartbeats to each other?
	
[ ] every 2 minutes
[ ] every 5 seconds
[x] every 2 seconds
[ ] every 10 seconds

#### Q27. Which command returns all of the documents in the customers collection?

[ ] db.customers.all()
[ ] db.find().customers();
[x] db.customers.find();
[ ] db.customers.show()

#### Q28. Given a cursor named myCursor, pointing to the customers collection, how to you get basic info about it?

[ ] myCursor.stats()
[ ] myCursor.dump()
[ ] myCursor.info()
[x] myCursor.explain()
	
#### Q29. What is true about indexes?

	1. They speed up read access while slowing down writes.   <<<<<--CORRECT
	2. They secure the database from intruders.
	3. They speed up reads and writes.
	4. They speed up write access while slowing down reads.
	
#### Q30. What is the preferred format to store geospatial data in MongoDB?

	1. Latitude, longitude
	2. XML
	3. GeoJSON <<<<<--CORRECT
	4. BSON
	
#### Q31. Which programming language is used to write MongoDB queries?

- [ ] Python
- [x] JavaScript
- [ ] SQL
- [ ] TypeScript

#### Q32. You have two text fields in your document and you'd like both to be quickly searchable. What should you do?

- [x] Create a text index on each field.
- [ ] MongoDB is not able to do this.
- [ ] Create a compound text index using both fields.
- [ ] Create a text index on one field and a single field index on the other.
	
#### Q33. To import a CSV file into MongoDB, which command should you issue?

- [ ] mongorestore
- [ ] mongoi
- [ ] upload
- [x] mongoimport
	
#### Q34. In an MongoDB mapReduce command, the reduce function should ____. 

- [ ] access the database
- [ ] be called only when the key has a single value
- [ ] acces the database only to perform read operations
- [x] not access the data

