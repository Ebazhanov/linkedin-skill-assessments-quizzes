## MongoDB

#### Q1. Which command adds members to the replica set from MongoDB shell?

- [x] `rs.add("<hostname>")`
- [ ] `replicaSetAdd("<hostname>")`
- [ ] `rs.insert("<hostname>")`
- [ ] `replica.add("<hostname>")`

#### Q2. Which MongoDB shell command should you use to back up a database?

- [ ] restore
- [ ] backup
- [ ] mongobackup
- [x] mongodump

#### Q3. Which shell query displays all citizens with an age greater than or equal to 21?

- [ ] `db.citizens.select('WHERE age >= 21')`
- [ ] `db.citizens.where('age >= 21')`
- [ ] `db.citizens.find('WHERE age >= 21')`
- [x] `db.citizens.find({age: {$gte: 21}})`

#### Q4. What does a MongoDB collection consist of?

- [ ] data
- [x] documents
- [ ] fields
- [ ] rows

#### Q5. Given an ObjectId in `_id`, how do you get the time it was created?

- [ ] `getDateTime(_id)`
- [ ] `_id.createDate()`
- [x] `_id.getTimestamp()`
- [ ] `_id.getDateTime()`

#### Q6. Given a cursor named myCursor, which command returns a boolean value?

- [x] myCursor.hasNext()
- [ ] myCursor.sort()
- [ ] myCursor.next()
- [ ] myCursor.find()

#### Q7. Which command returns a specific document in the user's collection?

- [x] `db.users.find({_id: 1})`
- [ ] `db.users.seek({_id: 1})`
- [ ] `db.users.query({_id: 1})`
- [ ] `db.query.users({_id: 1})`

#### Q8. To import a JSON array into Mongo, what flags are needed with MongoDBimport?

- [ ] `--type jsonArray`
- [ ] `--json`
- [ ] `--type json`
- [x] `--jsonArray`

#### Q9. Choose the shell command that connects to a MongoDB database.

- [x] mongo
- [ ] mongod
- [ ] mongoconnect
- [ ] dbconnect

#### Q10. In the MongoDB shell, how can you tell if an index was used with a query?

- [x] db.customers.find({lastName: 'smith'}).explain()
- [ ] db.customers.find({lastName: 'smith'}).perf()
- [ ] db.customers.find({lastName: 'smith'}).plan()
- [ ] db.customers.find({lastName: 'smith'}).usedIndex()

#### Q11. Suppose your aggregation pipeline terminated with an exception referring to exceeded memory limit. What is the best way to resolve the issue?

- [ ] Set useMemory to twice amount indicated in exception.
- [ ] Switch a 64 bit instance of MongoDB.
- [ ] Increase the memory of the MongoDB server.
- [x] Set allowDiskUse to true.

#### Q12. What is the recommended way to delete a user?

- [ ] db.deleteUser("user")
- [ ] db.removeUser("user") DEPRECATED
- [ ] db.remove("user")
- [x] db.dropUser("user")

#### Q13. What the primary database in a replica set fails, when does failover begin?

- [ ] once the primary has been down for 10 minutes
- [ ] once the primary reboots
- [x] immediately
- [ ] after the administrator reboots the primary

#### Q14. What is the correct option to set up Kerberos when starting MongoDBd?

- [x] `--setParameter authenticationMechanisms=GSSAPI`
- [ ] `--setAuthentication=GSSAPI`
- [ ] `--setParam auth=K`
- [ ] `--setAuth method=Kerberos`

#### Q15. What is the purpose of an arbiter in a replica set?

- [ ] It monitors replica set and sends email in case of failure
- [x] It casts the tie-breaking vote in an election.
- [ ] It holds a backup copy of the database.
- [ ] It reboots the failed server.

#### Q16. You want to know how many types of items you have in each category. Which query does this?

- [ ] `db.product.group({_id: "$category", count: {$sum:1}})`
- [ ] `db.product.aggregate($sum: {_id: "$category", count: {$group:1}})`
- [x] `db.product.aggregate($group: {_id: "$category", count: {$sum:1}})`
- [ ] `db.product.aggregate($count: {_id: "$category", count: {$group:1}})`

#### Q17. To restrict the number of records coming back from a query, which command should you use?

- [ ] take
- [x] limit
- [ ] max
- [ ] skip

#### Q18. You have a collection named restaurants with the geographical information stored in the location property, how do you create a geospatial index on it?

- [x] `db.restaurants.CreateIndex({location: "2dsphere"})`
- [ ] `db.restaurants.geospatial({location: "2dsphere"})`
- [ ] `db.restaurants.CreateIndex("2dsphere":"location")`
- [ ] `db.restaurants.CreateIndex({geospatial: "location"})`

#### Q19. How do you find documents with a matching item in an embedded array?

- [ ] `db.customers.findmatch ({"jobs":"secretary"})`
- [ ] `db.customers.find ({"jobs:secretary"})`
- [ ] `db.customers.find ({"jobs":["secretary"]})`
- [x] `db.customers.find ({"jobs":"secretary"})`

#### Q20. Which query bypasses the first 5 customers and returns the next 10?

- [ ] `db.customers.find({}, {skip: 5, limit: 10})`
- [ ] `db.customers.find({}.page(5).take(10))`
- [ ] `db.customers.find({}).skip(5).take(10)`
- [x] `db.customers.find({}).skip(5).limit(10)`

#### Q21. How do you create a text index?

- [ ] `db.customers.createIndex({firstName, lastName})`
- [ ] `db.customers.createTextIndex({firstName, lastName})`
- [x] `db.customers.createIndex({firstName: "text", lastName: "text"})`
- [ ] `db.customers.createText({firstName: 1, lastName: 1})`

#### Q22. Assuming you have customers collection with a firstName and lastName field, which is the correct MongoDB shell command to create an index on lastName, then firstName both ascending?

- [ ] `db.customers.createIndex("lastName, firstName, ASC")`
- [ ] `db.customers.addIndex({lastName:"ASC", firstName: "ASC"})`
- [ ] `db.customers.newIndex({lastName:1, firstName:1})`
- [x] `db.customers.createIndex({lastName:1, firstName: 1})`

#### Q23. One of the documents in your collection has an \_id based upon an older database design and you want to change it. You write an update command to find the document and replace the \_id but the \_id isn't changed. How should you fix the issue?

- [ ] Set the replace option to true.
- [ ] Use the replaceOne() command instead.
- [x] You can't. Once set, the \_id field cannot be changed.
- [ ] Use the updateOne() command instead.

#### Q24. A compound index allows you to \_ ?

- [ ] Calculate interest quickly.
- [ ] Accomplish nothing, since compound indexes aren't allowed in Mongo.
- [ ] Use more than one field per index.
- [x] Combine fields in different collations.

#### Q25. Why are ad-hoc queries useful?

- [ ] They do not have to use the same operators.
- [ ] You do not need to structure the database to support them.
- [ ] They autogenerate reports.
- [x] They run faster than indexed queries.

#### Q26. How often do the members of a replica set send heartbeats to each other?

- [ ] every 2 minutes
- [ ] every 5 seconds
- [x] every 2 seconds
- [ ] every 10 seconds

#### Q27. Which command returns all of the documents in the customers collection?

- [ ] `db.customers.all();`
- [ ] `db.find().customers();`
- [x] `db.customers.find();`
- [ ] `db.customers.show();`

#### Q28. Given a cursor named myCursor, pointing to the customers collection, how to you get basic info about it?

- [ ] `myCursor.stats()`
- [ ] `myCursor.dump()`
- [ ] `myCursor.info()`
- [x] `myCursor.explain()`

#### Q29. What is true about indexes?

- [x] They speed up read access while slowing down writes.
- [ ] They secure the database from intruders.
- [ ] They speed up reads and writes.
- [ ] They speed up write access while slowing down reads.

#### Q30. What is the preferred format to store geospatial data in MongoDB?

- [ ] Latitude, longitude
- [ ] XML
- [x] GeoJSON
- [ ] BSON

#### Q31. Which programming language is used to write MongoDB queries? (_Alternative_: In the MongoDB shell, what programming language is used to make queries?)

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

#### Q34. In an MongoDB mapReduce command, the reduce function should \_.

- [ ] access the database
- [ ] be called only when the key has a single value
- [ ] access the database only to perform read operations
- [x] not access the data

#### Q35. On a newly created collection, which field will have an index?

- [ ] the name field
- [ ] the ObjectId field
- [x] the `_id` field
- [ ] no field will have an index

#### Q36. You have a collection of thousands of students. You'd like to return the second set of 20 documents from the sorted collection. What is the proper order in which to apply the operations?

- [ ] limit, skip, sort
- [ ] sort, limit, skip
- [ ] limit, sort, skip
- [x] sort, skip, limit

#### Q37. You would like the stats() command to return kilobytes instead of bytes. Which command should you run?

- [x] `db.vehicle.stats(1024)`
- [ ] `db.vehicle.stats("kilobytes")`
- [ ] `db.vehicle.stats(true)`
- [ ] `db.vehicle.stats("kb")`

#### Q38. You want to modify an existing index. What is the best way to do this?

- [ ] Use the `reIndex()` command to modify the index.
- [x] Delete the original index and create a new index.
- [ ] Call the `createIndex()` command with the update option.
- [ ] Use the `updateIndex()` command.

#### Q39. You need to delete the index you created on the description field. Which command will accomplish this?

- [x] `db.vehicle.dropIndex("description_text")`
- [ ] `db.vehicle.dropIndex({"description":"text"})`
- [ ] `db.vehicle.removeIndex({"description":"text"})`
- [ ] `db.vehicle.removeIndex("description_text")`

#### Q40. You would like to know how many different categories you have. Which query will best get the job done?

- [ ] `db.vehicle.distinct("category")`
- [ ] `db.vehicle.unique("category")`
- [ ] `db.vehicle.distinct("category").count()`
- [x] `db.vehicle.distinct("category").length`

Note: count() works with find(...) but length works with distinct

#### Q41. From the MongoDB shell, how do you create a new document in the customers collection?

- [ ] `db.customers.add({name: "Bob"})`
- [x] `db.customers.save({name: "Bob"})`
- [ ] `db.customers.create({name: "Bob"})`
- [ ] `db.customers.new({name: "Bob"})`

#### Q42. Which field is required of all MongoDB documents?

- [x] `_id`
- [ ] `_name`
- [ ] ObjectId
- [ ] mongoDB is schema-less so no field is required

#### Q43. A MongoDB instance has at least what three files?

- [x] data, namespace, and journal
- [ ] namespace, journal, and log
- [ ] journal, data, and database
- [ ] data, log, and journal

#### Q44. You'd like a set of documents to be returned in last name, ascending order. Which query will accomplish this?

- [ ] `db.persons.find().sort({lastName: -1}}`
- [x] `db.persons.find().sort({lastName: 1}}`
- [ ] `db.persons.find().sort({lastName: ascending}}`
- [ ] `db.persons.find().sort({lastName: $asc}}`

#### Q45. What is NOT a standard role in MongoDB?

- [ ] restore
- [ ] read/write
- [x] dbadmin
- [ ] delete collections

#### Q46. Which MongoDB shell command deletes a single document?

- [ ] `db.customers.delete({_id: 1});`
- [ ] `db.customers.drop({_id: 1});`
- [ ] `db.drop.customers({_id: 1});`
- [x] `db.customers.remove({_id: 1});`

#### Q47. Using the MongoDB shell, how do you remove the customer collection and its indexes?

- [ ] `db.customers.remove({}).indexes();`
- [ ] `db.customers.remove({});`
- [x] `db.customers.drop();`
- [ ] `db.customers.delete();`

#### Q48. By default, applications direct their read operations to which member of the replica set?

- [ ] primary
- [x] arbiter
- [ ] secondary
- [ ] backup

#### Q49. You need to get the names of all the indexes on your current collection. What is the best way to accomplish this?

- [ ] `db.people.getName();`
- [ ] `db.people.reIndex({names: 1});`
- [ ] `db.people.getIndexKeys();`
- [x] `db.people.getIndexes();`

#### Q50. You are going to do a series of updates to multiple records. You find setting the multi option of the update() command too tiresome. What should you do instead?

- [ ] Use the replaceMany() command instead
- [ ] Use the updateMulti() command instead
- [x] Use the updateMany() command instead
- [ ] Set the global multi option to True

#### Q51. To cleanly shut down MongoDB, what command should you use from the MongoDB shell?

- [ ] quit()
- [ ] exit()
- [x] db.shutdownServer()
- [ ] db.shutdown()

#### Q52. Given a customer collection which includes fields for gender and city, which aggregate pipeline shows the number of female customers in each city? (_Alternative_: How can you view the execution performance statistics for a query?)

- [x] `db.members.aggregate([ {$match: {gender: "Female"}}, {$group: {_id: {city: "$city"}, number: {$sum: 1}}}, {$sort :{number: -1}}])`
- [ ] `db.members.find({$match: {gender: "Female"}}, {$group: {_id: {city: "$city"}, number: {$sum: 1}}}.$sort ({number: -1})`
- [ ] `db.members.find([ {$match: {gender: "Female"}}, {$group: {_id: {city: "$city"}, number: {$sum: 1}}}, {$sort :{number: -1}}])`
- [ ] `db.members.aggregate([ {$match: {gender: "Female"}}, {$sort :{number: -1}}])`

#### Q53. When no parameters are passed to `explain()`, what mode does it run in?

- [ ] wireTiger mode
- [ ] executionStats mode
- [x] queryPlanner mode
- [ ] allPlansExecution mode

#### Q54. What is the correct query to find all of the people who have a home phone number defined?

- [ ] `db.person.find({exists: 'homePhone'});`
- [ ] `db.person.exists({homePhone: true});`
- [x] `db.person.find({homePhone: {$exists: true}});`
- [ ] `db.person.has('homePhone');`

#### Q55. Which file in the MongoDB directly holds the MongoDB daemon?

- [ ] mongodb
- [x] mongo-daemon
- [ ] daemon
- [x] mongod

#### Q56. You have just secured your previously unsecured MongoDB server, but the server is still not requiring authentication. What is the best option?

- [x] Restart the `mongod` process.
- [ ] Issue the `secure()` command.
- [ ] Issue the `mongoimport` command.
- [ ] Issue the `authenticate()` command.

#### Q57. What is the most accurate statement regarding MongoDB and ad hoc queries?

- [x] MongoDB does not allow ad hoc queries; all queries require an index.
- [ ] Ad hoc queries are allowed only in the paid version.
- [ ] Ad hoc queries are allowed only through the ad hoc command.
- [x] MongoDB allows ad hoc queries.

#### Q58. In MongoDB, what does a projection do?

- [ ] allows you to do a calculation on the results
- [ ] allows you to run queries on the server
- [x] allows you to select which fields should be in the return data
- [ ] allows you to format the results for a display

#### Q59. To remove a database and all of its records from MongoDB, what operator should you use?

- [x] `dropDatabase()`
- [ ] `removeAll()`
- [ ] `clear()`
- [ ] `deleteDatabase()`

#### Q60. What option can be passed to start the MongoDB shell without connecting to a database?

- [ ] `-db=null`
- [ ] `--shell-only`
- [ ] `--free`
- [x] `-nodb`

#### Q61. How can you improve the appearance of the output JSON that contains the `_id`?

- [ ] `Use db.collection.set({$_id:pretty})`
- [ ] `Create a second index`
- [x] `Use db.collection.format(numeric)`
- [ ] `Use $_id = value`

#### Q62. What happens to a Replica set oplog if it runs out of memory?

- [x] `The oplog will be saved on one of the secondary servers.`
- [ ] `The oplog is capped collection and can't run out of memory`
- [ ] `The MongoDB instance will fail`
- [ ] `The oplog will stop recording logging information`

#### Q63. MongoDB ships with a variety of files. Which file runs the MongoDB shell?

- [x] mongo
- [ ] mongo-s
- [ ] shell
- [ ] mongo-shell

#### Q64. How can you view the execution performance statistics for a query?

- [ ] `db.performance.members.aggregate([ {$match: {gender: "Female"}}, {$group: {_id:{city:"$city"}, number: {$sum: 1}}}, {$sort : {number: -1}}])`
- [x] `db.members.aggregate([ {$match: {gender: "Female"}}, {$group: {_id: {city: "$city"}, number:{$sum:1}}}, {$sort: {number:-1}}]).explain("executionStats")`
- [ ] `db.members.aggregate([ {$match: {gender: "Female"}}, {$group:{_id: {city: "$city"}, number: {$sum: 1}}}, {$sort: {number: -1}}]).explain()`
- [ ] `db.members.aggregate([ {$match: {gender: """Female"""}}, {$group: {_id: {city: """$city"""}, number: {$sum:1}}}, {$sort: {number: -1}}]).number()`

#### Q65. From the MongoDB shell, how do you execute a JavaScript file named list.js?

- [ ] node 'list.js'
- [ ] exec('list.js)
- [ ] run('list.js)
- [x] load('list.js)

#### Q66. Which MongoDB shell query will sort the customer's collection by name descending?

- [ ] db.customers.sort({name: -1}.find({})
- [ ] db.customers.sort({name: -1})
- [x] db.customers.find({}).sort({name: -1})
- [ ] db.customers.find({}).sort({name: 1})

#### Q67. Suppose you are using the mongoimport command to import personnel data and there is a unique index on the email field. What happens when there are duplicate emails in the import?

- [ ] The import command aborts without importing any records.
- [ ] The import command imports records upto but not including the record, and then aborts.
- [ ] The import command doesn't import the bad document but does import the rest.
- [x] The import command prompts you to correct the bad record.

#### Q68. You have a collection with millions of documents. Each time you attempt to sort. MongoDB runs out of memory. What might help?

- [ ] Use the purge operator before the sort.
- [ ] Return the entire collection and sort on the client.
- [ ] Pass the --more-memory option.
- [x] Create an index on the field you are sorting.

#### Q69. You need to be able to quickly find a word in a text field. What should you do?

- [ ] Create a text index on the field and do a $text Query.
- [ ] Create an single field index in descending order, and do a query for the word.
- [x] Do a $text query.
- [ ] Create a $regex on the fields, and do a $regex query.

#### Q70. Which field is always included in a projection unless specifically excluded?

- [ ] index
- [ ] Name
- [x] `_id`
- [ ] row number

[Reference](https://docs.mongodb.com/manual/reference/operator/aggregation/project/#definition)
