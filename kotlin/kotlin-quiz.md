# Kotlin

#### Q1. You would like to print each score on its own line with its cardinal position. Without using **var** or **val**, which method allows iteration with both the value and its position?

```
fun main(){
  val highScores = listOf(4000, 2000, 10200, 12000, 9030)
```

- [ ] `.withIndex()`
- [ ] `.forEachIndexed()`
- [ ] `.forEach()`
- [ ] `.forIndexes()`

#### Q2. When the **Airplane** class is instantiated, it displays **Aircraft = null**, not **Aircraft = C130** why?

```
abstract class Aircraft {
  init { println("Aircraft = ${getName()}") }
  abstract fun getName(): String
}
class Airplane(private val name: String) : Aircraft() {
  override fun getName(): String = name
}
```

- [ ] Classes are initialized in the same order they are in the file, therefore, Aircraft should appear after Airplane
- [ ] The code needs to pass the parameter to the base class's primary constructor. Since it does not, it receives a null
- [ ] Abstract function always returns null
- [ ] A superclass is initialized before its subclass. Therefore, name has not been set before it is rendered

#### Q3. Kotlin interfaces ad abstract classes are very similar. What is one thing abstract class can do that interfaces cannot?

- [ ] Only abstract classes are inheritable by subclasses
- [ ] Only abstract classes can inherit from multiple superclasses
- [ ] Only abstract classes can have abstract methods
- [ ] Only abstract classes can store state

#### Q4. Inside an extension function, what is the name of the variable that corresponds to the receiver object

- [ ] The variable is named **it**
- [ ] The variable is named **this**
- [ ] The variable is named **receiver**
- [ ] The variable is named **default**

#### Q5. Your application has an **add** function. How could you use its **invoke** methods and display the results?

```
fun add(a: Int, b: Int): Int {
  return a + b
}
```

- [ ] `println(add(5,10).invoke())`
- [ ] `println(::add.invoke(5, 10))`
- [ ] `println(::add.invoke{5, 10})`
- [ ] `println(add.invoke(5,10))`

#### Q6. What is the entry point for a Kotlin application?

- [ ] `fun static main(){}`
- [x] `fun main(){}`
- [ ] `fun Main(){}`
- [ ] `public static void main(){}`

#### Q7. You are writing a console app in Kotlin that processes test entered by the user. If the user enters an empty string, the program exits. Which kind of loop would work best for this app? Keep in mind that the loop is entered at least once

- [ ] a do..while loop
- [ ] a for loop
- [ ] a while loop
- [ ] a forEach loop

#### Q8. You pass an integer to a function expecting type Any. It works without issue. Why is a primitive integer able to work with a function that expects an object?

```
fun showHashCode(obj: Any){
  println("${obj.hasCode()}")
}
fun main() {
  showHashCode(1)
}
```

- [ ] While the code runs, it does not produce correct results
- [ ] The integer is always a class
- [ ] The compiler runs an implicit .toClass() method on the integer
- [ ] The integer is autoboxed to a Kotlin Int class

#### Q9. You have started a long-running coroutine whose job you have assigned to a variable named **task**. If the need arose, how could you abort the coroutine?

```
val task = launch {
  // long running job
}
```

- [ ] `task.join()`
- [ ] `task.abort()`
- [ ] `job.stop()`
- [ ] `task.cancel()`

#### Q10. You are attempting to assign an integer variable to a long variable, but Kotlin compiler flags it as an error. Why?

- [ ] You must wrap all implicit conversion in a try/catch block
- [ ] You can only assign Long to an Int, not the other way around
- [ ] There is no implicit conversion from Int to Long
- [ ] All integers in Kotlin are of type Long

#### Q11. You have written a snippet of code to display the results of the roll of a six-sided die. When the die displays from 3 to 6 inclusive, you want to display a special message. Using a Kotlin range, what code should you add?

```
when (die) {
  1 -> println("die is 1")
  2 -> println("die is 2")
  ___ -> printlin("die is between 3 and 6")
  else -> printlin("dies is unknown")
}
```

- [ ] `3,4,5,6`
- [ ] `in 3..6`
- [ ] `3 : 6`
- [ ] `{3,4,5,6}`

#### Q12. The function **typeChecker** receiver a parameter **obj** of type **Any**. Based upon the type of **obj**, it prints different messages for Int, String, Double, and Float types; if not any of the mentioned types, it prints "unknown type". What operator allows you to determine the type of an object?

- [ ] instanceof
- [ ] is
- [ ] typeof
- [ ] as

#### Q13. This code does not print any output to the console. What is wrong?

```
firstName?.let {
  println("Greeting $firstname!")
}
```

- [ ] A null pointer exception is thrown
- [ ] firstName is equal to null
- [ ] firstName is equal to an empty string
- [ ] firstName is equal to Boolean false

#### Q14. You have a function simple() that is called frequently in your code. You place the inline prefix on the function. What effect does it have on the code?

```
inline fun simpe(x: Int): Int{
  return x * x
}

fun main() {
  for(count in 1..1000) {
    simple(count)
  }
}
```

- [ ] The code will give a stack overflow error
- [ ] The compiler warns of insignificant performance impact
- [ ] The compiler warns of significant memory usage
- [ ] The code is significantly faster

#### Q15.How do you fill in the blank below to display all of the even numbers from 1 to 10 with least amount of code?

```
for (_____) {
  println("There are $count butterflies.")
}
```

- [ ] `count in 1..10`
- [ ] `count in 2..10 step 2`
- [ ] `count in 1..10 % 2`
- [ ] `var count=2; count <= 10; count+=2`

#### Q16. What value is printed by println()?

```
val set = setOf("apple", "pear", "orange", "apple")
println(set.count())
```

- [ ] 3
- [ ] 4
- [ ] 1
- [ ] 5

#### Q17. Which line of code shows how to display a nullable string's length and shows 0 instead of null?

- [ ] `println(b!!.length ?: 0)`
- [ ] `println(b?.length ?: 0)`
- [ ] `println(b?.length ?? 0)`
- [ ] `println(b == null? 0: b.length)`

#### Q18. In the file main.kt, you ae filtering a list of integers and want to use an already existing function, removeBadValues. What is the proper way to invoke the function from filter in the line below?

```
val list2 = (80..100).toList().filter(_____)
```

- [ ] `::removeBadValues`
- [ ] `GlobalScope.removeBadValues()`
- [ ] `Mainkt.removeBadValues`
- [ ] `removeBadValues`

#### Q19. Which code snippet correctly shows a for loop using a range to display "1 2 3 4 5 6"?

- [ ] `for(z in 1..7) println("$z ")`
- [ ] `for(z in 1..6) print("$z ")`
- [ ] `for(z in 1 to 6) print("$z ")`
- [ ] `for(z in 1..7) print("$z ")`

#### Q20. You are upgrading a Java class to Kotlin. What should you use to replace the Java class's static fields?

- [ ] an anonymous object
- [ ] a static property
- [ ] a companion object
- [ ] a backing field

#### Q21. Your code need to try casting an object. If the cast is not possible, you do not want an exception generated, instead you want null to be assigned. Which operator can safely cast a value?

- [ ] as?
- [ ] ??
- [ ] is
- [ ] as

#### Q22. Kotlin will not compile this code snippet. What is wrong?

```
class Employee
class Manager : Employee()
```

- [ ] In order to inherit from a class, it must be marked **open**
- [ ] In order to inherit from a class, it must be marked **public**
- [ ] In order to inherit from a class, it must be marked **sealed**
- [ ] In order to inherit from a class, it must be marked **override**

#### Q23. Which function changes the value of the element at the current iterator location?

- [ ] `change()`
- [ ] `modify()`
- [ ] `set()`
- [ ] `assign()`

#### Q24. From the Supervisor subclass, how do you call the Employee class's display() method?

```
open class Employee(){
  open fun display() = println("Employee display()")
}
class Supervisor : Employee() {
  override fun display() {
    println("Supervisor display()")
  }
}
```

- [ ] `Employee.display() `
- [ ] `::display()`
- [ ] `super.display()`
- [ ] `override.display()`

#### Q25. The code below compiled and executed without issue before the addition of the line declaring errorStatus. Why does this line break the code?

```
sealed class Status(){
  object Error : Status()
  class Success : Status()
}
fun main(){
  var successStatus = Status.Success()
  var errorStatus = Status.Error()
}
```

- [ ] StatusError is an object, not a class and cannot be instantiated
- [ ] Only one instance of the class Status can be instantiated at a time
- [ ] Status.Error must be declared as an immutable type
- [ ] Status.Error is pribate to class and cannot be declared externally

#### Q26. The code below is expected to display the numbers from 1 to 10, but it does not. Why?

```
val seq = sequence { yieldAll(1..20) }
  .filter { it < 11 }
  println(seq)
```

- [ ] You cannot assign a sequence to a variable
- [ ] To produce result, a sequence must have terminal operation. In this case, it needs a .toList()
- [ ] The .filter{ it < 11 } should be .filter{ it > 11 }
- [ ] The yieldAll(1..20) should be yieldAll(1..10)

#### Q27. What three methods does this class have?

```
class Person
```

- [ ] `equals(), hashCode(), and toString()`
- [ ] `equals(), toHash(), and super()`
- [ ] `print(), println(), and toString()`
- [ ] `clone(), equals(), and super()`

#### Q28. Which is the proper way to declare a singleton named DatabaseManager?

- [ ] `object DatabaseManager {}`
- [ ] `singleton DatabaseManager {}`
- [ ] `static class DatabaseManager {}`
- [ ] `data class DatabaseManager {}`

#### Q29. In order to subclass the Person class, what is one thing you must do?

```
abstract class Person(val name: String){
  abstract fun displayJob(description: String)
}
```

- [ ] The subclass must be marked sealed
- [ ] You must override the displayJob() method
- [ ] You must mark the subclass as final
- [ ] An abstract class cannot be extended, so you must change it to open

#### Q30. The code snippet below translates a database user to a model user. Because their names are both User, you must use their fully qualified names, which is cumbersome. You do not have access to either of the imported classes' source code. How can you shorten the type names?

```
import com.tekadept.app.model.User
import com.tekadept.app.database.User

class UserService{
  fun translateUser(user: com.tekadept.app.database,Yser): User =
    com.tekadept.app.model.User("${user.first} ${user.last}")
}
```

- [ ] Use import as to change the type name
- [ ] Create subtypes with shorter names
- [ ] Create interfaces with shorter names
- [ ] Create extension classes with shorter names
