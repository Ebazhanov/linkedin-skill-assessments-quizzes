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
- myCursor.hasNext()
- myCursor.sort()
- myCursor.next()
- myCursor.find() <<<<---CORRECT

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

#### Q11. Suppose your aggregation pipeline terminated with an exception referring to exceeded memory
#### limit. What is the best way to resolve the issue?
- Set useMemory to twice amount indicated in exception.
- Switch a 64 bit instance of MongoDB.
- Increase the memory of the MongoDB server.
- Set allowDiskUse to true. <<<<---CORRECT

#### Q12. What is the recommended way to delete a user?
- db.deleteUser("user")
- db.removeUser("user") <<<---CORRECT
- db.remove("user")
- db.dropUser("user")

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
