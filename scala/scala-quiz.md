Scala Assessment
-------------

#### Q1. Scala bytecode can run on top of Java VM. What is the fundamental difference between Java object.clone() and Scala object.copy()?

- [ ] One is a Java object, the other is a Scala object.
- [ ] clone() will copy class structures but not the data, while copy() will also copy data into new objects.
- [ ] There is no difference.
- [ ] copy() allows you to change values during the copying process; clone() does not.


#### Q2. What value does this code return? 

```
val m1 = Map("a"->1,"b"->2,"c"->3)
m1("a")
```

- [ ] a
- [ ] 2
- [ ] b
- [ ] 1


#### Q3. What is one way to avoid low-level parallelization details?

- [ ] monads
- [ ] literal functions
- [ ] partially applied functions
- [ ] parallel collections


#### Q4. What do you use in ScalaTest to see a detailed diagram of error messages when a test fails?

- [ ] ArgumentExceptions
- [ ] AssertionException
- [ ] DiagrammedAssertions
- [ ] JUnit


#### Q5. What data type would you use to store an immutable collection of objects that contain a fixed number of varying types?

- [ ] Array
- [ ] ImmutableCollection
- [ ] List
- [ ] Tuple


#### Q6. After defining a function in the interpreter, Scala returns the following. What does the 

```
myfnc: ()Unit
```

- [ ] The function has no side effects.
- [ ] The function takes no parameters. 
- [ ] The function returns no value.
- [ ] Returning unit types to the function is a closures.


#### Q7. What type of number is 1234.e5?

- [ ] hexadecimal
- [ ] short
- [ ] floating point
- [ ] long


#### Q8. When you convert a map to a list using the toList method of the map, the result will be of which type?

- [ ] List[(String, String)]
- [ ] List[(Array, Array)]
- [ ] List[(Array, Array)]
- [ ] List


#### Q9. What type of object does this code create? 

```
val x = (1234, "Active")
```

- [ ] List
- [ ] Map 
- [ ] Tuple
- [ ] Array 


#### Q10. Which is a subclass of all classes?

- [ ] AnyVal
- [ ] AnyRef 
- [ ] Method
- [ ] Null


#### Q11. For the for-yield construct, is the scope separate between for-body and yield-body?

- [ ] Yes and no. It is different depending on the for construct and what it does.
- [ ] Yes, because the for section does not expose its scope.
- [ ] No, because for-yield shares the same scope, even though they are within separate curly braces.
- [ ] Yes, because they are within different curly braces.


#### Q12. What is one way to implement pattern matching on methods?

- [ ] using regex
- [ ] using monads
- [ ] using string matching
- [ ] using case classes


#### Q13. What is the value of z after executing this code? 

```
val y = List('a','b')
val z = y::List('c') 
```

- [ ] List(a,b,c)
- [ ] List(List(a, b), c)
- [ ] List(c,a,b)
- [ ] List(c,List(a,b))


#### Q14. What term is used to specify a precondition?

- [ ] assert
- [ ] require
- [ ] precondition
- [ ] mustHave


#### Q15. Which Scala type may throw an exception or a successfully computed value, and is commonly used to trap and propagate errors?

##### answers missing


