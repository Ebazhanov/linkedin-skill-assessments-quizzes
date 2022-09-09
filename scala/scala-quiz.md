## Scala

#### Q1. Scala bytecode can run on top of Java VM. What is the fundamental difference between Java object.clone() and Scala object.copy()?

- [ ] One is a Java object, the other is a Scala object.
- [ ] clone() will copy class structures but not the data, while copy() will also copy data into new objects.
- [ ] There is no difference.
- [x] copy() allows you to change values during the copying process; clone() does not.

#### Q2. What value does this code return?

```scala
val m1 = Map("a"->1,"b"->2,"c"->3)
m1("a")
```

- [ ] a
- [ ] 2
- [ ] b
- [x] 1

#### Q3. What is one way to avoid low-level parallelization details?

- [ ] monads
- [ ] literal functions
- [ ] partially applied functions
- [x] parallel collections

#### Q4. What do you use in ScalaTest to see a detailed diagram of error messages when a test fails?

- [ ] ArgumentExceptions
- [ ] AssertionException
- [x] DiagrammedAssertions
- [ ] JUnit

#### Q5. What data type would you use to store an immutable collection of objects that contain a fixed number of varying types?

- [ ] Array
- [ ] ImmutableCollection
- [ ] List
- [x] Tuple

#### Q6. After defining a function in the interpreter, Scala returns the following. What does the `()` indicate?

```
myfnc: ()Unit
```

- [ ] The function has no side effects.
- [ ] The function takes no parameters.
- [x] The function returns no value.
- [ ] Returning unit types to the function is a closures.

#### Q7. What type of number is 1234.e5?

- [ ] hexadecimal
- [ ] short
- [x] floating point
- [ ] long

#### Q8. When you convert a map to a list using the `toList` method of the map, the result will be of which type?

- [ ] `List[(String, String)]`
- [ ] `List[(Array, Array)]`
- [ ] `List[(Collection, Collection)]`
- [x] `List`

#### Q9. What type of object does this code create?

```
val x = (1234, "Active")
```

- [ ] List
- [ ] Map
- [x] Tuple
- [ ] Array

#### Q10. Which is a subclass of all classes?

- [ ] AnyVal
- [ ] AnyRef
- [ ] Method
- [x] Null

[Null in Scala Standard library](https://www.scala-lang.org/api/current/scala/Null.html). The question is a bit incorrect - Null is a subtype of every type _except those of value classes_

#### Q11. For the for-yield construct, is the scope separate between for-body and yield-body?

- [ ] Yes and no. It is different depending on the for construct and what it does.
- [ ] Yes, because the for section does not expose its scope.
- [x] No, because for-yield shares the same scope, even though they are within separate curly braces.
- [ ] Yes, because they are within different curly braces.

**Example**: yield-body has access to the `e` variable from the for-body

```scala
val a = Array(1, 2, 3, 4, 5)
for {
     e <- a if e > 2
} yield e
```

#### Q12. What is one way to implement pattern matching on methods?

- [ ] using regex
- [ ] using monads
- [ ] using string matching
- [ ] using case classes

Note: ambiguous question, it's not clear what kind of [pattern matching](https://docs.scala-lang.org/tour/pattern-matching.html) is meant here.

#### Q13. What is the value of z after executing this code?

```
val y = List('a','b')
val z = y::List('c')
```

- [ ] List(a,b,c)
- [x] List(List(a, b), c)
- [ ] List(c,a,b)
- [ ] List(c,List(a,b))

#### Q14. What term is used to specify a precondition?

- [x] assert
- [ ] require
- [ ] precondition
- [ ] mustHave

#### Q15. Which Scala type may throw an exception or a successfully computed value, and is commonly used to trap and propagate errors?

- [ ] `scala.util.ExceptionHandling`
- [ ] `scala.Catch.Throw`
- [ ] `scala.exception.TryFinally`
- [x] `scala.util.Try`

[scala.util.Try](https://www.scala-lang.org/api/current/scala/util/Try.html)

#### Q16. What is the data type of y after this code is executed?

```
val y = (math floor 3.1415 * 2)
```

- [ ] short
- [x] double
- [ ] int
- [ ] bigInt

#### Q17. When using pattern matching, which character matches on any object?

- [ ] `%`
- [x] `_`
- [ ] `^`
- [ ] `-`

[Pattern Matching](https://docs.scala-lang.org/tour/pattern-matching.html)

#### Q18. You have created an array using val. Can you change the value of any element of the array—and why or why not?

- [x] Yes, the reference to the array is immutable, so the location that the array points to is immutable. The values in the array are mutable.
- [ ] The 0th element is immutable and cannot be modified. All other elements can be modified.
- [ ] Yes, val does not make arrays immutable.
- [ ] No, val makes the array and values of the array immutable.

**Explanation**:

```scala
val a1 = Array(1, 2, 3)
a1{1} = 3 // OK
a1 = Array(1, 3, 3) // error: reassignment to val
```

#### Q19. What is the output of this function?

```scala
def main () {
     var a = 0
     for (a<-1 until 5){println(a)}
```

- [ ] 1,2,3,4,5
- [ ] 0,1,2,3,4
- [x] 1,2,3,4
- [ ] 2,3,4,5

#### Q20. What do you call objects with immutable state?

- [ ] singletons
- [ ] stationary objects
- [x] functional objects
- [ ] fixed objects

**Note:** singletons may have mutable state

#### Q21. You have written a Scala script. How would you access command-line arguments in the script?

- [x] use array named args
- [ ] use tuple named args
- [ ] use numbered variables with a _ prefix for example _ 1, _ 2, _ 3
- [ ] use numbered variables with a $ prefix - for example $1, $2, $3

#### Q22. What does this code return? `val x = 3; if (x > 2) x = 4 else x = x*2`

- [ ] 4
- [x] an error
- [ ] 6
- [ ] 3

#### Q23. Which statement returns a success or a failure indicator when you execute this code?

`val MyFuture = Future {runBackgroundFunction() }`

- [x] myFuture.onComplete
- [ ] myFuture(status)
- [ ] myFuture.Finished
- [ ] complete(myFuture)

#### Q24. To denote a parameter that may be repeated, what should you place after type?

- [ ] `%`
- [ ] `&`
- [ ] `_`
- [x] `-`

#### Q25. What is called when a superclass has more than one subclass in Scala?

- [ ] polyinheritance
- [ ] multilevel inheritance
- [ ] multimode inheritance
- [x] hierarchical inheritance

#### Q26. One way to improve code reliability is to use `__` , which will evaluate a condition and return an error if the condition is violated.

- [ ] packages
- [ ] polymorphisms
- [x] assertions
- [ ] traits

#### Q27. Which statement about if-else-if-else statements is true?

- [ ] If the first else-if does not succeed, then no other else-ifs are tested.
- [ ] If an else-if does not succeed, then none of the remaining else-if statements or elses will be tested.
- [ ] All else-if statements are tested in all cases.
- [x] If an else-if succeeds, then none of the remaining else-if statements or elses will tested.

#### Q28. What do you call the process of changing the definition of an inherited method?

- [ ] recursive methods
- [ ] currying methods
- [ ] redefining methods
- [x] overriding methods

#### Q29. To denote a parameter that may be repeated, what should you place after the type?

- [ ] `_`
- [x] `*`
- [ ] `%`
- [ ] `&`

[Repeated Parameters in Scala](https://www.baeldung.com/scala/repeated-parameters)

#### Q30. What is the code below equivalent to?

```scala
myClass.foreach(println _)
```

- [ ] `myClass.foreach(println ())`
- [ ] `myClass.foreach(print NIL)`
- [ ] `myClass.loop(println ())`
- [x] `myClass.foreach(x => println(x))`

#### Q31. What is an advantage of an immutable object?

- [ ] Immutable objects use less memory than their mutable counterparts.
- [ ] Immutable objects do not require error handling.
- [ ] Immutable objects can be used in classes, mutable objects cannot.
- [x] Immutable objects are threadsafe.

#### Q32. You want to create an iteration loop that tests the condition at the end of the loop body. Which iteration would you use?

- [x] do-while loop
- [ ] while loop
- [ ] for loop
- [ ] do-until loop

#### Q33. What can you use to make querying a database more efficient, by avoiding the need to parse the SQL string every time a query is executed from Scala?

- [ ] database driver
- [ ] connection
- [x] prepared statement
- [ ] SQL view

[PreparedStatement from Java](https://docs.oracle.com/javase/8/docs/api/java/sql/PreparedStatement.html) which is also used in Scala

#### Q34. Which is _not_ a member of the collections hierarchy?

- [ ] Set
- [ ] Seq
- [x] Hash
- [ ] Map

#### Q35. Which term makes the contents of packages available without prefixing?

- [ ] use
- [ ] include
- [x] import
- [ ] assertion

#### Q36. If you wanted to find the remainder after division, what operator would you use?

- [x] %
- [ ] DIV
- [ ] //
- [ ] /

#### Q37. What are defined inside a class definition?

- [ ] method
- [x] fields and methods
- [ ] fields, methods, and packages
- [ ] fields

#### Q38. What defines methods and fields that can then be reused by mixing into classes?

- [ ] singleton
- [ ] assertion
- [x] trait
- [ ] monad

#### Q39. When do you need to explicitly state the return type in a function definition?

- [ ] when the function has no side effects
- [ ] when the function returns a Unit type
- [x] when the function is recursive
- [ ] when the function has side effects

#### Q40. Why would you make a field private?

- [ ] so only methods in the same file can access the field
- [ ] so only methods in the same package can access the field
- [x] so only methods in the same class could access the field
- [ ] so only methods defined in a Java class can access the field

#### Q41. What's the difference between `.equals` and `==`?

- [ ] They do the exact same thing
- [ ] `==` won't work on objects
- [ ] `==` cannot be applied to `String`
- [x] `==` is a wrapper of `.equals()` and checks for nulls

[Source:](https://www.programmersought.com/article/3717957705/)

#### Q42. What is denotes the intersection between two sets?

- [ ] ||
- [ ] &&
- [x] &
- [ ] %

[Source:](https://docs.scala-lang.org/overviews/collections/sets.html)

#### Q43. What do you call a function defined in a block?

- [ ] private function
- [ ] block function
- [ ] local function
- [ ] method

#### Q44. What do you call a Scala method that is parametrized by type as well as by value?

- [ ] multimode method
- [ ] polymorphic method
- [ ] closure
- [ ] collection method

#### Q45. What type of exception is thrown when a precondition is violated?

- [x] IllegalArgumentException
- [ ] NumberFormatException
- [ ] NullPointerExcepetion
- [ ] MalformedParameterException

#### Q46. In scala what is precondition?

- [ ] a constraint on where a method may be called from
- [ ] a constraint on values passed to a methode constructor
- [x] a class of predifined error messages
- [ ] a class of Boolean operators

#### Q47. What would you change in this code to make it execute in parallel?

```
 val myNums = (1 to 500).toList
 list.map(_ + 1)
```

- [x] Change **list.map** to **list.par.map.**
- [ ] Change **toList** to **toListPar**
- [ ] Change **val** to **val.par**
- [ ] Change **toList** to **toParallelList**

#### Q48. What is a free variable?

- [x] a variable defined outside a function
- [ ] a variable referenced in a function that is not assigned a value by that function
- [ ] a variable that has a global scope
- [ ] a variable defined in a class and available to all methods in that class

#### Q49. What's the best way to execute code in the background in a separate thread?

- [ ] AltThread
- [ ] AltFuture
- [ ] AltProcess
- [x] Future

#### Q50. What value does this code return?

```scala
x= List(1,2,4); x(1)?
```

- [ ] (1,2,4)
- [ ] 1
- [ ] Nil
- [x] 2
