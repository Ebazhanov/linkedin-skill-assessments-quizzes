
1. You would like to print each score on its own line with its cardinal position. Without using **var** or **val**, which method allows iteration with both the value and its position?
```
fun main(){
  val highScores = listOf(4000, 2000, 10200, 12000, 9030)
```
- [ ] .withIndex()
- [ ] .forEachIndexed()
- [ ] .forEach()
- [ ] .forIndexes()

2. When the **Airplane** class is instantiated, it displays **Aircraft = null**, not **Aircraft = C130** why?
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

3. Kotlin interfaces ad abstract classes are very similar. What is one thing abstract class can do that interfaces cannot?
- [ ] Only abstract classes are inheritable by subclasses
- [ ] Only abstract classes can inherit from multiple superclasses
- [ ] Only abstract classes can have abstract methods
- [ ] Only abstract classes can store state

4. Inside an extension function, what is the name of the variable that corresponds to the receiver object
- [ ] The variable is named **it**
- [ ] The variable is named **this**
- [ ] The variable is named **receiver**
- [ ] The variable is named **default**

5. Your application has an **add** function. How could you use its **invoke** methods and display the results?
```
fun add(a: Int, b: Int): Int {
  return a + b
}
```
- [ ] println(add(5,10).invoke())
- [ ] println(::add.invoke(5, 10))
- [ ] println(::add.invoke{5, 10})
- [ ] println(add.invoke(5,10))

6. What is the entry point for a Kotlin application?
- [ ] fun static main(){}
- [X] fun main(){}
- [ ] fun Main(){}
- [ ] public static void main()P{

7. You are writing a console app in Kotlin that processes test entered by the user. If the user enters an empty string, the program exits. Which kind of loop would work best for this app? Keep in mind that the loop is entered at least once
- [ ] a do..while loop
- [ ] a for loop
- [ ] a while loop
- [ ] a forEach loop

8. You pass an integer to a function expecting type Any. It works without issue. Why is a primitive integer able to work with a function that expects an object?
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

9. You have started a long-running coroutine whose job you have assigned to a variable named **task**. If the need arose, how could you abort the coroutine?
```
val task = launch {
  // long running job
}
```
- [ ] task.join()
- [ ] task.abort()
- [ ] job.stop()
- [ ] task.cancel()

10. You are attempting to assign an integer variable to a long variable, but Kotlin compiler flags it as an error. Why?
- [ ] You must wrap all implicit conversion in a try/catch block
- [ ] You can only assign Long to an Int, not the other way around
- [ ] There is no implicit conversion from Int to Long
- [ ] All integers in Kotlin are of type Long

11. You have written a snippet of code to display the results of the roll of a six-sided die. When the die displays from 3 to 6 inclusive, you want to display a special message. Using a Kotlin range, what code should you add?
```
when (die) {
  1 -> println("die is 1")
  2 -> println("die is 2")
  ___ -> printlin("die is between 3 and 6")
  else -> printlin("dies is unknown")
}
```
- [ ] 3,4,5,6
- [ ] in 3..6
- [ ] 3 : 6
- [ ] {3,4,5,6}

12. The function **typeChecker** receiver a parameter **obj** of type **Any**. Based upon the type of **obj**, it prints different messages for Int, String, Double, and Float types; if not any of the mentioned types, it prints "unknown type". What operator allows you to determine the type of an object?
- [ ] instanceof
- [ ] is
- [ ] typeof
- [ ] as

13. This code does not print any output to the console. What is wrong?
```
firstName?.let {
  println("Greeting $firstname!")
}
```
- [ ] A null pointer exception is thrown
- [ ] firstName is equal to null
- [ ] firstName is equal to an empty string
- [ ] firstName is equal to Boolean false

14. You have a function simple() that is called frequently in your code. You place the inline prefix on the function. What effect does it have on the code?
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
- [ ] The code will gave a stack overflow error
- [ ] The compiler warns of insignificant performance impact
- [ ] The compiler warns of significant memory usage
- [ ] The code is significantly faster

15.How do you fill in the blank below to display all of the even numbers from 1 to 10 with least amount of code?
```
for (_____) {
  println("There are $count butterflies.")
}
```
- [ ] count in 1..10
- [ ] count in 2..10 step 2
- [ ] count in 1..10 % 2
- [ ] var count=2; count <= 10; count+=2
