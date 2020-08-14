Scala Assessment
-------------

#### Q1. Scala bytecode can run on top of Java VM. What is the fundamental difference between Java object.clone() and Scala object.copy()?

- [ ] One is a Java object, the other is a Scala object.
- [ ] clone() will copy class structures but not the data, while copy() will also copy data into new objects.
- [ ] There is no difference.
- [ ] copy() allows you to change values during the copying process; clone() does not.


#### Q2. What value does this code return? 

```scala
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

```scala
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

```scala
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

```scala
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


#### Q16. What is the data type of y after this code is executed?  

```scala
val y = (math floor 3.1415 * 2)
```
- [ ] short
- [ ] double
- [ ] int
- [ ] bigInt


#### Q17. When using pattern matching, which character matches on any object?
- [ ] %
- [ ] _
- [ ] ^
- [ ] *


#### Q18. You have created an array using val. Can you change the value of any element of the array—and why or why not?

- [ ] Yes, the reference to the array is immutable, so the location that the array points to is immutable. The values in the array are mutable.
- [ ] The 0th element is immutable and cannot be modified. All other elements can be modified.
- [ ] Yes, val does not make arrays immutable.
- [ ] No, val makes the array and values of the array immutable.


#### Q19. What is the output of this function? 

```scala
def main () {
     var a = 0
     for (a<-1 until 5){println(a)}
```
- [ ] 1,2,3,4,5
- [ ] 0,1,2,3,4
- [ ] 1,2,3,4
- [ ] 2,3,4,5


#### Q20. What do you call objects with immutable state?

- [ ] singletons
- [ ] stationary objects
- [ ] functional objects
- [ ] fixed objects





