# Kotlin

#### Q1. You would like to print each score on its own line with its cardinal position. Without using **var** or **val**, which method allows iteration with both the value and its position?

```
fun main(){
  val highScores = listOf(4000, 2000, 10200, 12000, 9030)
```

- [x] `.withIndex()`
[references](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.sequences/with-index.html)
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
- [x] Only abstract classes can store state
[reference](https://blog.kotlin-academy.com/abstract-class-vs-interface-in-kotlin-5ab8697c3a14)

#### Q4. Inside an extension function, what is the name of the variable that corresponds to the receiver object

- [ ] The variable is named **it**
- [x] The variable is named **this**
[reference](https://www.programiz.com/kotlin-programming/extension-functions#:~:text=The%20class%20name%20is%20the,function%20refers%20the%20receiver%20object)
- [ ] The variable is named **receiver**
- [ ] The variable is named **default**

#### Q5. Your application has an **add** function. How could you use its **invoke** methods and display the results?

```
fun add(a: Int, b: Int): Int {
  return a + b
}
```

- [ ] `println(add(5,10).invoke())`
- [x] `println(::add.invoke(5, 10))`
[reference](https://kotlinlang.org/docs/operator-overloading.html#invoke-operator)
- [ ] `println(::add.invoke{5, 10})`
- [ ] `println(add.invoke(5,10))`
#### Q6. What is the entry point for a Kotlin application?

- [ ] `fun static main(){}`
- [x] `fun main(){}`
- [ ] `fun Main(){}`
- [ ] `public static void main(){}`

#### Q7. You are writing a console app in Kotlin that processes test entered by the user. If the user enters an empty string, the program exits. Which kind of loop would work best for this app? Keep in mind that the loop is entered at least once

- [x] a do..while loop
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
- [x] The integer is autoboxed to a Kotlin Int class

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
- [x] There is no implicit conversion from Int to Long
[reference](https://kotlinlang.org/docs/basic-types.html#explicit-conversions)
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

- [x] `3,4,5,6`
- [x] `in 3..6`
  [reference](https://kotlinlang.org/docs/ranges.html)
- [ ] `3 : 6`
- [ ] `{3,4,5,6}`

#### Q12. The function **typeChecker** receiver a parameter **obj** of type **Any**. Based upon the type of **obj**, it prints different messages for Int, String, Double, and Float types; if not any of the mentioned types, it prints "unknown type". What operator allows you to determine the type of an object?

- [ ] instanceof
- [x] is
- [ ] typeof
- [ ] as

#### Q13. This code does not print any output to the console. What is wrong?

```
firstName?.let {
  println("Greeting $firstname!")
}
```

- [ ] A null pointer exception is thrown
- [x] firstName is equal to null
- [ ] firstName is equal to an empty string
- [ ] firstName is equal to Boolean false

#### Q14. You have a function simple() that is called frequently in your code. You place the inline prefix on the function. What effect does it have on the code?

```
inline fun simple(x: Int): Int{
  return x * x
}

fun main() {
  for(count in 1..1000) {
    simple(count)
  }
}
```

- [ ] The code will give a stack overflow error
- [x] The compiler warns of insignificant performance impact
- [ ] The compiler warns of significant memory usage
- [ ] The code is significantly faster

#### Q15.How do you fill in the blank below to display all of the even numbers from 1 to 10 with least amount of code?

```
for (_____) {
  println("There are $count butterflies.")
}
```

- [ ] `count in 1..10`
- [x] `count in 2..10 step 2`
- [ ] `count in 1..10 % 2`
- [ ] `var count=2; count <= 10; count+=2`

#### Q16. What value is printed by println()?

```
val set = setOf("apple", "pear", "orange", "apple")
println(set.count())
```

- [ ] 3
- [x] 4
[reference](https://zetcode.com/kotlin/sets/)
- [ ] 1
- [ ] 5

#### Q17. Which line of code shows how to display a nullable string's length and shows 0 instead of null?

- [ ] `println(b!!.length ?: 0)`
- [x] `println(b?.length ?: 0)`
- [ ] `println(b?.length ?? 0)`
- [ ] `println(b == null? 0: b.length)`

#### Q18. In the file main.kt, you ae filtering a list of integers and want to use an already existing function, removeBadValues. What is the proper way to invoke the function from filter in the line below?

```
val list2 = (80..100).toList().filter(_____)
```

- [x] `::removeBadValues`
[reference](https://kotlinlang.org/docs/reflection.html#callable-references)
- [ ] `GlobalScope.removeBadValues()`
- [ ] `Mainkt.removeBadValues`
- [ ] `removeBadValues`

#### Q19. Which code snippet correctly shows a for loop using a range to display "1 2 3 4 5 6"?

- [ ] `for(z in 1..7) println("$z ")`
- [x] `for(z in 1..6) print("$z ")`
- [ ] `for(z in 1 to 6) print("$z ")`
- [ ] `for(z in 1..7) print("$z ")`

#### Q20. You are upgrading a Java class to Kotlin. What should you use to replace the Java class's static fields?

- [ ] an anonymous object
- [ ] a static property
- [x] a companion object
- [ ] a backing field

#### Q21. Your code need to try casting an object. If the cast is not possible, you do not want an exception generated, instead you want null to be assigned. Which operator can safely cast a value?

- [x] as?
- [ ] ??
- [ ] is
- [ ] as

#### Q22. Kotlin will not compile this code snippet. What is wrong?

```
class Employee
class Manager : Employee()
```

- [x] In order to inherit from a class, it must be marked **open**
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
- [x] `super.display()`
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
- [x] To produce result, a sequence must have terminal operation. In this case, it needs a .toList()
- [ ] The .filter{ it < 11 } should be .filter{ it > 11 }
- [ ] The yieldAll(1..20) should be yieldAll(1..10)

#### Q27. What three methods does this class have?

```
class Person
```

- [x] `equals(), hashCode(), and toString()`
[reference](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/)
- [ ] `equals(), toHash(), and super()`
- [ ] `print(), println(), and toString()`
- [ ] `clone(), equals(), and super()`

#### Q28. Which is the proper way to declare a singleton named DatabaseManager?

- [x] `object DatabaseManager {}`
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
- [x] You must override the displayJob() method
[reference](https://kotlinlang.org/docs/inheritance.html)
- [ ] You must mark the subclass as final
- [ ] An abstract class cannot be extended, so you must change it to open

#### Q30. The code snippet below translates a database user to a model user. Because their names are both User, you must use their fully qualified names, which is cumbersome. You do not have access to either of the imported classes' source code. How can you shorten the type names?

```
import com.tekadept.app.model.User
import com.tekadept.app.database.User

class UserService{
  fun translateUser(user: com.tekadept.app.database.User): User =
    com.tekadept.app.model.User("${user.first} ${user.last}")
}
```

- [ ] Use import as to change the type name
- [ ] Create subtypes with shorter names
- [ ] Create interfaces with shorter names
- [ ] Create extension classes with shorter names

#### Q31. Your function is passed by a parameter obj of type Any. Which code snippet shows a way to retrieve the original type of obj, including package information?

- [ ] `obj.classInfo()`
- [ ] `obj.typeInfo()`
- [x] `obj::class.simpleName`
[reference](https://kotlinlang.org/docs/reflection.html#constructor-references)
- [ ] `obj::class`

#### Q32. Which is the correct declaration of an integer array with a size of 5?

- [ ] `val arrs[5]: Int`
- [x] `val arrs = IntArray[5]`
[reference](https://kotlinlang.org/docs/basic-types.html#primitive-type-arrays)
- [ ] `val arrs: Int[5]`
- [ ] `val arrs = Array<Int>(5)`

#### Q33. You have created a class that should be visible only to the other code in its module. Which modifier do you use?

- [x] `internal`
[reference](https://kotlinlang.org/docs/visibility-modifiers.html#classes-and-interfaces)
- [ ] `private`
- [ ] `public`
- [ ] `protected`

#### Q34. Kotlin has two equality operators, == and ===. What is the difference?

- [ ] == determines if two primitive types are identical. === determines if two objects are identical
- [ ] == determines if two references point to the same object. === determines if two objects have the same value
- [ ] == determines if two objects have the same value. === determines if two strings have the same value
- [x] == determines if two objects have the same value. === determines if two references point to the same object
[reference](https://kotlinlang.org/docs/equality.html#structural-equality)

#### Q35. Which snippet correctly shows setting the variable max to whichever variable holds the greatest value, a or b, using idiomatic Kotlin?

- [ ] `val max3 = a.max(b)`
- [ ] `val max = a > b ? a : b`
- [x] `val max = if (a > b) a else b`
- [ ] `if (a > b) max = a else max = b`

#### Q36. You have an enum class Signal that represents the state of a network connection. You want to print the position number of the SENDING enum. Which line of code does that?

```java
enum class Signal { OPEN, CLOSED, SENDING }
```

- [ ] `println(Signal.SENDING.position())`
- [ ] `println(Signal.SENDING.hashCode())`
- [ ] `println(Signal.SENDING)`
- [x] `println(Signal.SENDING.ordinal)`
[reference](https://kotlinlang.org/docs/enum-classes.html#working-with-enum-constants)

#### Q37. Both const and @JvmField create constants. What can const do that @JvmField cannot?

```java
class Detail {
  companion object {
    const val COLOR = "Blue"
    @JvmField val SIZE = "Really Big"
  }
}
```

- [ ] const is compatible with Java, but @JvmField is not
- [ ] The compiler will inline const so it is faster and more memory efficient
- [ ] Virtually any type can be used with const but not @JvmField
- [ ] const can also be used with mutable types

#### Q38. You have a when expression for all of the subclasses of the class Attribute. To satisfy the when, you must include an else clause. Unfortunately, whenever a new subclass is added, it returns unknown. You would prefer to remove the else clause so the compiler generates an error for unknown subtypes. What is one simple thing you can do to achieve this?

```java
open class Attribute
class Href: Attribute()
class Src: Attribute()
class Alt: Attribute()

fun getAttribute(attribute: Attribute) : String {
  return when (attribute) {
    is Href -> "href"
    is Alt -> "alt"
    is Src -> "src"
    else -> "unknown"
  }
}
```

- [ ] Replace `open` with `closed`
- [ ] Replace `open` with `sealed`
- [ ] Replace `open` with `private`
- [ ] Replace `open` with `public`

#### Q39. You would like to know each time a class property is updated. Which code snippet shows a built-in delegated property that can accomplish this?

- [ ] `Delegates.watcher()`
- [x] `Delegates.observable()`
[reference](https://kotlinlang.org/docs/delegated-properties.html#observable-properties)
- [ ] `Delegates.rx()`
- [ ] `Delegates.observer()`

#### Q40. Why doesn't this code compile?

```java
infix fun Int.add(addedL Int=1) = this + addend
fun main(){
  val msg = "Hello"
  println( msg shouldMatch "Hello")    
  println( 10 multiply 5 + 2)
  println( 10 add 5)
}
```

- [ ] infix function must be marked public
- [ ] In Kotlin, add is a keyword
- [ ] Extension functions use it, not this, as the default parameter name
- [ ] infix functions cannot have default values

#### Q41. What is the correct way to initialize a nullable variable?

- [ ] `val name = null`
- [ ] `var name: String`
- [ ] `val name: String`
- [x] `val name: String? = null`

#### Q42. Which line of code is a shorter, more idiomatic version of the displayed snippet?

```java
val len: Int = if (x != null) x.length else -1
```

- [ ] `val len = x?.let{x.len} else {-1}`
- [ ] `val len = x!!.length ?: -1`
- [ ] `val len:Int = (x != null)? x.length : -1`
- [x] `val len = x?.length ?: -1`

#### Q43. You are creating a Kotlin unit test library. What else should you add to make the following code compile without error?

```java
fun String.shouldEqual(value: String) = this == value
fun main(){
  val msg = "test message"
  println(msg shouldEqual "test message")
}
```

- [ ] The extension function should be marked public
- [ ] Add the prefix operator to the shouldMatch extension function
- [ ] The code is not legal in Kotlin
- [ ] Add the prefix infix to the shouldMatch extension function

#### Q44. What is the difference between the declarations of COLOR and SIZE?

```java
class Record{
  companion object {
    const val COLOR = "Red"
    val SIZE = "Large"
  }
}
```

- [ ] Since COLOR and SIZE are both immutable, they are identical internally
- [ ] Both are immutable, but the use of the keyword const makes COLOR slower and less space efficient than SIZE
- [ ] const makes COLOR faster, but not compatible with Java. Without const, SIZE is still compatible with Java
- [ ] Both are immutable, but the use of the keyword const makes COLOR faster and mroe space efficient than SIZE

