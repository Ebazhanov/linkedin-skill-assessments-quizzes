## Java

#### Q1. Given the string "strawberries" saved in a variable called fruit, what would `fruit.substring(2, 5)` return?

- [ ] rawb
- [x] raw
- [ ] awb
- [ ] traw

**Reasoning:** The substring method is accepting two arguments.

- The first argument being the index to start(includes that char at 2)
- and the second the index of the string to end the substring(excludes the char at 5).
- Strings in Java are like arrays of chars.
- Therefore, the method will return "raw" as those are the chars in indexes 2,3, and 4.
- You can also take the ending index and subtract the beginning index from it, to determine how many chars will be included in the substring (5-2=3).

#### Q2. How can you achieve runtime polymorphism in Java?

- [ ] method overloading
- [ ] method overrunning
- [x] method overriding
- [ ] method calling

#### Q3. Given the following definitions, which of these expression will **NOT** evaluate to true?

`boolean b1 = true, b2 = false; int i1 = 1, i2 = 2;`

- [ ] `(i1 | i2) == 3`
- [x] `i2 && b1`
- [ ] `b1 || !b2`
- [ ] `(i1 ^ i2) < 4`

#### Q4. What is the output of this code?

```java
1: class Main {
2:   public static void main (String[] args) {
3:     int array[] = {1, 2, 3, 4};
4:     for (int i = 0; i < array.size(); i++) {
5:        System.out.print(array[i]);
6:     }
7:   }
8: }
```

- [x] It will not compile because of line 4.
- [ ] It will not compile because of line 3.
- [ ] 123
- [ ] 1234

#### Q5. Which of the following can replace the CODE SNIPPET to make the code below print "Hello World"?

```java
interface Interface1 {
    static void print() {
        System.out.print("Hello");
    }
}

interface Interface2 {
    static void print() {
        System.out.print("World!");
    }
}
```

- [ ] `super1.print(); super2.print();`
- [ ] `this.print();`
- [ ] `super.print();`
- [x] `Interface1.print(); Interface2.print();`

#### Q6. What does the following code print?

```java
String str = "abcde";
str.trim();
str.toUpperCase();
str.substring(3, 4);
System.out.println(str);
```

- [ ] CD
- [ ] CDE
- [ ] D
- [x] "abcde"

#### Q7. What is the result of this code?

```java
class Main {
    public static void main (String[] args){
        System.out.println(print(1));
    }
    static Exception print(int i){
        if (i>0) {
            return new Exception();
        } else {
            throw new RuntimeException();
        }
    }
}
```

- [ ] It will show a stack trace with a runtime exception.
- [x] "java.lang.Exception"
- [ ] It will run and throw an exception.
- [ ] It will not compile.

#### Q8. Which class can compile given these declarations?

```java
interface One {
    default void method() {
        System.out.println("One");
    }
}

interface Two {
    default void method () {
        System.out.println("One");
    }
}
```

- [ ] A

```java
class Three implements One, Two {
    public void method() {
        super.One.method();
    }
}
```

- [ ] B

```java
class Three implements One, Two {
    public void method() {
        One.method();
    }
}
```

- [ ] C

```java
class Three implements One, Two {
}
```

- [x] D

```java
class Three implements One, Two {
    public void method() {
        One.super.method();
    }
}
```

#### Q9. What is the output of this code?

```java
class Main {
    public static void main (String[] args) {
        List list = new ArrayList();
        list.add("hello");
        list.add(2);
        System.out.print(list.get(0) instanceof Object);
        System.out.print(list.get(1) instanceof Integer);
    }
}
```

- [ ] The code does not compile.
- [ ] truefalse
- [x] truetrue
- [ ] falsetrue

#### Q10. Given the following two classes, what will be the output of the Main class?

```java
package mypackage;
public class Math {
    public static int abs(int num){
        return num < 0 ? -num : num;
    }
}
package mypackage.elementary;
public class Math {
    public static int abs (int num) {
        return -num;
    }
}
```

```java
import mypackage.Math;
import mypackage.elementary.*;

class Main {
    public static void main (String args[]){
        System.out.println(Math.abs(123));
    }
}
```

- [ ] Lines 1 and 2 generate compiler errors due to class name conflicts.
- [ ] "-123"
- [ ] It will throw an exception on line 5.
- [x] "123"

**Explanation:** `The answer is "123". The `abs()` method evaluates to the one inside mypackage.Math class, because The import statements of the form:`

`import packageName.subPackage.*`

is [Type-Import-on-Demand Declarations](https://docs.oracle.com/javase/specs/jls/se7/html/jls-7.html#jls-7.5.2), which [never causes any other declaration to be shadowed](https://docs.oracle.com/javase/specs/jls/se7/html/jls-6.html#jls-6.4.1).

#### Q11. What is the result of this code?

```java
1: class MainClass {
2:  final String message(){
3:      return "Hello!";
4:  }
5: }

6: class Main extends MainClass {
7:  public static void main(String[] args) {
8:      System.out.println(message());
9:  }

10: String message(){
11:     return "World!";
12:  }
13: }
```

- [x] It will not compile because of line 10.
- [ ] "Hello!"
- [ ] It will not compile because of line 2.
- [ ] "World!"

**Explanation:** Compilation error at line 10 because of final methods cannot be overridden, and here message() is a final method, and also note that Non-static method message() cannot be referenced from a static context.

#### Q12. Given this code, which command will output "2"?

```java
class Main {
    public static void main(String[] args) {
        System.out.println(args[2]);
    }
}
```

- [ ] `java Main 1 2 "3 4" 5`
- [x] `java Main 1 "2" "2" 5`
- [ ] `java Main.class 1 "2" 2 5`
- [ ] `java Main 1 "2" "3 4" 5`

#### Q13. What is the output of this code?

```java
class Main {
    public static void main(String[] args){
        int a = 123451234512345;
        System.out.println(a);
    }
}
```

- [ ] "123451234512345"
- [x] Nothing - this will not compile.
- [ ] a negative integer value
- [ ] "12345100000"

**Reasoning:** `The int type in Java can be used to represent any whole number from -2147483648 to 2147483647. Therefore, this code will not compile as the number assigned to 'a' is larger than the int type can hold.`

#### Q14. What is the output of this code?

```java
class Main {
    public static void main (String[] args) {
        String message = "Hello world!";
        String newMessage = message.substring(6, 12)
            + message.substring(12, 6);
        System.out.println(newMessage);
    }
}
```

- [ ] The code does not compile.
- [x] A runtime exception is thrown.
- [ ] "world!!world"
- [ ] "world!world!"

#### Q15. How do you write a foreach loop that will iterate over ArrayList\<Pencil\>pencilCase?

- [x] `for (Pencil pencil : pencilCase) {}`
- [ ] `for (pencilCase.next()) {}`
- [ ] `for (Pencil pencil : pencilCase.iterator()) {}`
- [ ] `for (pencil in pencilCase) {}`

#### Q16. What does this code print?

```java
System.out.print("apple".compareTo("banana"));
```

- [ ] `0`
- [ ] positive number
- [x] negative number
- [ ] compilation error

#### Q17. You have an ArrayList of names that you want to sort alphabetically. Which approach would **NOT** work?

- [ ] `names.sort(Comparator.comparing(String::toString))`
- [ ] `Collections.sort(names)`
- [x] `names.sort(List.DESCENDING)`
- [ ] `names.stream().sorted((s1, s2) -> s1.compareTo(s2)).collect(Collectors.toList())`

#### Q18. By implementing encapsulation, you cannot directly access the class's \_ properties unless you are writing code inside the class itself.

- [x] private
- [ ] protected
- [ ] no-modifier
- [ ] public

#### Q19. Which is the most up-to-date way to instantiate the current date?

- [ ] `new SimpleDateFormat("yyyy-MM-dd").format(new Date())`
- [ ] `new Date(System.currentTimeMillis())`
- [x] `LocalDate.now()`
- [ ] `Calendar.getInstance().getTime()`

**Explanation**: LocalDate is the newest class added in java 8

#### Q20. Fill in the blank to create a piece of code that will tell whether `int0` is divisible by `5`:

`boolean isDivisibleBy5 = _____`

- [ ] `int0 / 5 ? true: false`
- [x] `int0 % 5 == 0`
- [ ] `int0 % 5 != 5`
- [ ] `Math.isDivisible(int0, 5)`

#### Q21. How many times will this code print "Hello World!"?

```java
class Main {
    public static void main(String[] args){
        for (int i=0; i<10; i=i++){
            i+=1;
            System.out.println("Hello World!");
        }
    }
}
```

- [x] 10 times
- [ ] 9 times
- [ ] 5 times
- [ ] infinite number of times

**Explanation**: `Observe the loop increment. It's not an increment, it's an assignment(post).`

#### Q22. The runtime system starts your program by calling which function first?

- [ ] print
- [ ] iterative
- [ ] hello
- [x] main

#### Q23. What code would you use in Constructor A to call Constructor B?

```java
public class Jedi {
  /* Constructor A */
  Jedi(String name, String species){}

  /* Constructor B */
  Jedi(String name, String species, boolean followsTheDarkSide){}
  }
```

- [ ] Jedi(name, species, false)
- [ ] new Jedi(name, species, false)
- [x] this(name, species, false)
- [ ] super(name, species, false)

**Note:** `This code won't compile, possibly broken code sample.`

#### Q24. Which statement is **NOT** true?

- [ ] An anonymous class may specify an abstract base class as its base type.
- [x] An anonymous class does not require a zero-argument constructor.
- [ ] An anonymous class may specify an interface as its base type.
- [ ] An anonymous class may specify both an abstract class and interface as base types.

#### Q25. What will this program print out to the console when executed?

```java
import java.util.LinkedList;

public class Main {
    public static void main(String[] args){
        LinkedList<Integer> list = new LinkedList<>();
        list.add(5);
        list.add(1);
        list.add(10);
        System.out.println(list);
    }
}
```

- [x] [5, 1, 10]
- [ ] [10, 5, 1]
- [ ] [1, 5, 10]
- [ ] [10, 1, 5]

#### Q26. What is the output of this code?

```java
class Main {
    public static void main(String[] args){
       String message = "Hello";
       for (int i = 0; i<message.length(); i++){
          System.out.print(message.charAt(i+1));
       }
    }
}
```

- [ ] "Hello"
- [x] A runtime exception is thrown.
- [ ] The code does not compile.
- [ ] "ello"

#### Q27. Object-oriented programming is a style of programming where you organize your program around \_ rather than \_ and data rather than logic.

- [ ] functions; actions
- [x] objects; actions
- [ ] actions; functions
- [ ] actions; objects

#### Q28. What statement returns true if "nifty" is of type String?

- [ ] `"nifty".getType().equals("String")`
- [ ] `"nifty".getType() == String`
- [ ] `"nifty".getClass().getSimpleName() == "String"`
- [x] `"nifty" instanceof String`

#### Q29. What is the output of this code?

```java
import java.util.*;
class Main {
	public static void main(String[] args) {
		List<Boolean> list = new ArrayList<>();
		list.add(true);
		list.add(Boolean.parseBoolean("FalSe"));
		list.add(Boolean.TRUE);
		System.out.print(list.size());
		System.out.print(list.get(1) instanceof Boolean);
	}
}
```

- [ ] A runtime exception is thrown.
- [ ] 3false
- [ ] 2true
- [x] 3true

#### Q30. What is the result of this code?

```java
1: class Main {
2: 	Object message(){
3: 		return "Hello!";
4: 	}
5: 	public static void main(String[] args) {
6: 		System.out.print(new Main().message());
7: 		System.out.print(new Main2().message());
8: 	}
9: }
10: class Main2 extends Main {
11: 	String message(){
12: 		return "World!";
13: 	}
14: }
```

- [ ] It will not compile because of line 7.
- [ ] Hello!Hello!
- [x] Hello!World!
- [ ] It will not compile because of line 11.

#### Q31. What method can be used to create a new instance of an object?

- [ ] another instance
- [ ] field
- [x] constructor
- [ ] private method

#### Q32. Which is the most reliable expression for testing whether the values of two string variables are the same?

- [ ] string1 == string2
- [ ] string1 = string2
- [ ] string1.matches(string2)
- [x] string1.equals(string2)

#### Q33. Which letters will print when this code is run?

```java
public static void main(String[] args) {
	try {
		System.out.println("A");
		badMethod();
		System.out.println("B");
	} catch (Exception ex) {
		System.out.println("C");
	} finally {
		System.out.println("D");
	}
}
public static void badMethod() {
	throw new Error();
}
```

- [ ] A, B, and D
- [ ] A, C, and D
- [ ] C and D
- [x] A and D

**Explanation**: ``Error` is not inherited from `Exception``

#### Q34. What is the output of this code?

```java
class Main {
	static int count = 0;
	public static void main(String[] args) {
		if (count < 3) {
			count++;
			main(null);
		} else {
			return;
		}
		System.out.println("Hello World!");
	}
}
```

- [ ] It will throw a runtime exception.
- [ ] It will not compile.
- [x] It will print "Hello World!" three times.
- [ ] It will run forever.

#### Q35. What is the output of this code?

```java
import java.util.*;
class Main {
	public static void main(String[] args) {
		String[] array = {"abc", "2", "10", "0"};
		List<String> list = Arrays.asList(array);
		Collections.sort(list);
		System.out.println(Arrays.toString(array));
	}
}
```

- [ ] `[abc, 0, 2, 10]`
- [ ] The code does not compile.
- [ ] `[abc, 2, 10, 0]`
- [x] `[0, 10, 2, abc]`

**Explanation**: The `java.util.Arrays.asList(T... a)` returns a fixed-size list backed by the specified array. (Changes to the returned list "write through" to the array.)

#### Q36. What is the output of this code?

```java
class Main {
	public static void main(String[] args) {
		String message = "Hello";
		print(message);
		message += "World!";
		print(message);
	}
	static void print(String message){
		System.out.print(message);
		message += " ";
	}
}
```

- [ ] Hello World!
- [x] HelloHelloWorld!
- [ ] Hello Hello World!
- [ ] Hello HelloWorld!

#### Q37. What is displayed when this code is compiled and executed?

```java
public class Main {
	public static void main(String[] args) {
		int x = 5;
		x = 10;
		System.out.println(x);
	}
}
```

- [ ] x
- [ ] null
- [x] 10
- [ ] 5

#### Q38. Which approach cannot be used to iterate over a List named _theList_?

- [ ] A

```java
for (int i = 0; i < theList.size(); i++) {
    System.out.println(theList.get(i));
}
```

- [ ] B

```java
for (Object object : theList) {
    System.out.println(object);
}
```

- [x] C

```java
Iterator it = theList.iterator();
for (it.hasNext()) {
    System.out.println(it.next());
}
```

- [ ] D

```java
theList.forEach(System.out::println);
```

**Explanation:** `for (it.hasNext())` should be `while (it.hasNext())`.

#### Q39. What method signature will work with this code?

`boolean healthyOrNot = isHealthy("avocado");`

- [ ] public void isHealthy(String avocado)
- [x] boolean isHealthy(String string)
- [ ] public isHealthy("avocado")
- [ ] private String isHealthy(String food)

#### Q40. Which are valid keywords in a Java module descriptor (module-info.java)?

- [ ] provides, employs
- [ ] imports, exports
- [ ] consumes, supplies
- [x] requires, exports

#### Q41. Which type of variable keeps a constant value once it is assigned?

- [ ] non-static
- [ ] static
- [x] final
- [ ] private

#### Q42. How does the keyword `volatile` affect how a variable is handled?

- [ ] It will be read by only one thread at a time.
- [ ] It will be stored on the hard drive.
- [x] It will never be cached by the CPU.
- [ ] It will be preferentially garbage collected.

#### Q43. What is the result of this code?

```java
char smooch = 'x';
System.out.println((int) smooch);
```

- [ ] an alphanumeric character
- [ ] a negative number
- [x] a positive number
- [ ] a ClassCastException

#### Q44. You get a NullPointerException. What is the most likely cause?

- [ ] A file that needs to be opened cannot be found.
- [ ] A network connection has been lost in the middle of communications.
- [ ] Your code has used up all available memory.
- [x] The object you are using has not been instantiated.

#### Q45. How would you fix this code so that it compiles?

```java
public class Nosey {
	int age;
	public static void main(String[] args) {
		System.out.println("Your age is: " + age);
	}
}
```

- [x] Make age static.
- [ ] Make age global.
- [ ] Make age public.
- [ ] Initialize age to a number.

#### Q46. Add a Duck called "Waddles" to the ArrayList **ducks**.

```java
public class Duck {
	private String name;
	Duck(String name) {}
}
```

- [ ] `Duck waddles = new Duck();`
      `ducks.add(waddles);`
- [ ] `Duck duck = new Duck("Waddles");`
      `ducks.add(waddles);`
- [x] `ducks.add(new Duck("Waddles"));`
- [ ] `ducks.add(new Waddles());`

#### Q47. If you encounter `UnsupportedClassVersionError` it means the code was `___` on a newer version of Java than the JRE `___` it.

- [ ] executed; interpreting
- [ ] executed; compiling
- [x] compiled; executing
- [ ] compiled, translating

#### Q48. Given this class, how would you make the code compile?

```java
public class TheClass {
    private final int x;
}
```

- [ ] A

```java
public TheClass() {
    x += 77;
}
```

- [ ] B

```java
public TheClass() {
    x = null;
}
```

- [x] C

```java
public TheClass() {
    x = 77;
}
```

- [ ] D

```java
private void setX(int x) {
    this.x = x;
}
public TheClass() {
    setX(77);
}
```

**Explanation:** `final` class members are allowed to be assigned only in three places: declaration, constructor or an instance-initializer block.

#### Q49. How many times f will be printed?

```java
public class Solution {
    public static void main(String[] args) {
        for (int i = 44; i > 40; i--) {
            System.out.println("f");
        }
    }
}
```

- [x] 4
- [ ] 3
- [ ] 5
- [ ] A Runtime exception will be thrown

#### Q50. Which statements about `abstract` classes are true?

```
1. They can be instantiated.
2. They allow member variables and methods to be inherited by subclasses.
3. They can contain constructors.
```

- [ ] 1, 2, and 3
- [ ] only 3
- [x] 2 and 3
- [ ] only 2

#### Q51. Which keyword lets you call the constructor of a parent class?

- [ ] parent
- [x] super
- [ ] this
- [ ] new

#### Q52. What is the result of this code?

```java
  1: int a = 1;
  2: int b = 0;
  3: int c = a/b;
  4: System.out.println(c);
```

- [x] It will throw an ArithmeticException.
- [ ] It will run and output 0.
- [ ] It will not compile because of line 3.
- [ ] It will run and output infinity.

#### Q53. Normally, to access a static member of a class such as Math.PI, you would need to specify the class "Math". What would be the best way to allow you to use simply "PI" in your code?

- [x] Add a static import.
- [ ] Declare local copies of the constant in your code.
- [ ] This cannot be done. You must always qualify references to static members with the class form which they came from.
- [ ] Put the static members in an interface and inherit from that interface.

#### Q54. Which keyword lets you use an interface?

- [ ] extends
- [x] implements
- [ ] inherits
- [ ] import

#### Q55. Why are ArrayLists better than arrays?

- [x] You don't have to decide the size of an ArrayList when you first make it.
- [ ] You can put more items into an ArrayList than into an array.
- [ ] ArrayLists can hold more kinds of objects than arrays.
- [ ] You don't have to decide the type of an ArrayList when you first make it.

#### Q56. Declare a variable that holds the first four digits of Π

- [ ] int pi = 3.141;
- [ ] decimal pi = 3.141;
- [x] double pi = 3.141;
- [ ] float pi = 3.141;

**Reasoning:**

```java
public class TestReal {
    public static void main (String[] argv)
    {
      double pi = 3.14159265;       //accuracy up to 15 digits
      float pi2 = 3.141F;           //accuracy up to 6-7 digits

      System.out.println ("Pi=" + pi);
      System.out.println ("Pi2=" + pi2);
    }
  }
```

```
The default Java type which Java will be using for a float variable will be double.
So, even if you declare any variable as float, what the compiler has to actually do is to assign a double value to a float variable,
which is not possible. So, to tell the compiler to treat this value as a float, that 'F' is used.
```

#### Q57. Use the magic power to cast a spell

```java
public class MagicPower {
    void castSpell(String spell) {}
}
```

- [x] `new MagicPower().castSpell("expecto patronum")`
- [ ] `MagicPower magicPower = new MagicPower();`
      `magicPower.castSpell();`
- [ ] `MagicPower.castSpell("expelliarmus");`
- [ ] `new MagicPower.castSpell();`

#### Q58. What language construct serves as a blueprint containing an object's properties and functionality?

- [ ] constructor
- [ ] instance
- [x] class
- [ ] method

#### Q59. What does this code print?

```java
public static void main(String[] args) {
    int x=5,y=10;
    swapsies(x,y);
    System.out.println(x+" "+y);
}

static void swapsies(int a, int b) {
    int temp=a;
    a=b;
    b=temp;
}
```

- [ ] 10 10
- [x] 5 10
- [ ] 10 5
- [ ] 5 5

#### Q60. What is the result of this code?

```java
try {
    System.out.println("Hello World");
} catch (Exception e) {
    System.out.println("e");
} catch (ArithmeticException e) {
    System.out.println("e");
} finally {
    System.out.println("!");
}
```

- [ ] Hello World
- [x] It will not compile because the second catch statement is unreachable
- [ ] Hello World!
- [ ] It will throw runtime exception

#### Q61. Which is not a java keyword

- [ ] finally
- [ ] native
- [ ] interface
- [x] unsigned

**Explanation:** `native` is a part of JNI interface

#### Q62. Which operator would you use to find the remainder after division?

- [x] `%`
- [ ] `//`
- [ ] `/`
- [ ] `DIV`

[Reference](http://www.cs.ukzn.ac.za/~hughm/java/intro/week2/21.html)

#### Q63. Which choice is a disadvantage of inheritance?

- [ ] Overridden methods of the parent class cannot be reused.
- [ ] Responsibilities are not evenly distributed between parent and child classes.
- [x] Classes related by inheritance are tightly coupled to each other.
- [ ] The internal state of the parent class is accessible to its children.

[Reference](http://erpbasic.blogspot.com/2012/01/inheritance-advantages-and.html#:~:text=Main%20disadvantage%20of%20using%20inheritance,used%20independent%20of%20each%20other.&text=4.,case%20of%20using%20that%20method.)

#### Q64. How would you declare and initialize an array of 10 ints?

- [ ] `Array<Integer> numbers = new Array<Integer>(10);`
- [ ] `Array[int] numbers = new Array[int](10);`
- [x] `int[] numbers = new int[10];`
- [ ] `int numbers[] = int[10];`

#### Q65. Refactor this event handler to a lambda expression:

```java
groucyButton.addActionListener(new ActionListener() {
    @Override
    public void actionPerformed(ActionEvent e) {
        System.out.println("Press me one more time..");
    }
});
```

- [ ] `groucyButton.addActionListener(ActionListener listener -> System.out.println("Press me one more time..."));`
- [x] `groucyButton.addActionListener((event) -> System.out.println("Press me one more time..."));`
- [ ] `groucyButton.addActionListener(new ActionListener(ActionEvent e) {() -> System.out.println("Press me one more time...");});`
- [ ] `groucyButton.addActionListener(() -> System.out.println("Press me one more time..."));`

[Reference](https://www.codejava.net/java-core/the-java-language/java-8-lambda-listener-example)

#### Q66. Which functional interfaces does Java provide to serve as data types for lambda expressions?

- [ ] Observer, Observable
- [ ] Collector, Builder
- [ ] Filter, Map, Reduce
- [x] Consumer, Predicate, Supplier

[Reference](https://www.baeldung.com/java-8-functional-interfaces)

#### Q67. What is a valid use of the hashCode() method?

- [ ] encrypting user passwords
- [x] deciding if two instances of a class are equal
- [ ] enabling HashMap to find matches faster
- [ ] moving objects from a List to a HashMap

[Reference](https://www.baeldung.com/java-hashcode)

#### Q68. What kind of relationship does "extends" denote?

- [ ] uses-a
- [x] is-a
- [ ] has-a
- [ ] was-a

[Reference](https://www.c-sharpcorner.com/UploadFile/3614a6/is-a-and-has-a-relationship-in-java/)

#### Q69. How do you force an object to be garbage collected?

- [ ] Set object to null and call Runtime.gc()
- [x] Set object to null and call System.gc()
- [ ] Set object to null and call Runtime.getRuntime().runFinalization()
- [ ] There is no way to force an object to be garbage collected

[Reference](https://sematext.com/blog/java-garbage-collection/)

#### Q70. Java programmers commonly use design patterns. Some examples are the **\_**, which helps create instances of a class, the **\_**, which ensures that only one instance of a class can be created; and the **\_**, which allows for a group of algorithms to be interchangeable.

- [x] static factory method; singleton; strategy pattern
- [ ] strategy pattern; static factory method; singleton
- [ ] creation pattern; singleton; prototype pattern
- [ ] singleton; strategy pattern; static factory method

#### Q71. Using Java's Reflection API, you can use \_ to get the name of a class and \_ to retrieve an array of its methods.

- [x] this.getClass().getSimpleName(); this.getClass().getDeclaredMethods()
- [ ] this.getName(); this.getMethods()
- [ ] Reflection.getName(this); Reflection.getMethods(this)
- [ ] Reflection.getClass(this).getName(); Reflection.getClass(this).getMethods()

#### Q72. Which is not a valid lambda expression?

- [ ] `a -> false;`
- [ ] `(a) -> false;`
- [x] `String a -> false;`
- [ ] `(String a) -> false;`

#### Q73. Which access modifier makes variables and methods visible only in the class where they are declared?

- [ ] public
- [ ] protected
- [ ] nonmodifier
- [x] private

#### Q74. What type of variable can be assigned to only once?

- [ ] private
- [ ] non-static
- [x] final
- [ ] static

#### Q75. How would you convert a String to an Int?

- [ ] `"21".intValue()`
- [ ] `String.toInt("21")`
- [x] `Integer.parseInt("21")`
- [ ] `String.valueOf("21")`

#### Q76. What method should be added to the Duck class to print the name Moby?

```java
public class Duck {
    private String name;

    Duck(String name) {
        this.name = name;
    }

    public static void main(String[] args) {
        System.out.println(new Duck("Moby"));
    }
}
```

- [x] `public String toString() { return name; } `
- [ ] `public void println() { System.out.println(name); } `
- [ ] `String toString() { return this.name; } `
- [ ] `public void toString() { System.out.println(this.name); } `

#### Q77. Which operator is used to concatenate Strings in Java

- [x] `+`
- [ ] `&`
- [ ] `.`
- [ ] `-`

[Reference](https://www.techiedelight.com/concatenate-two-strings-java/)

#### Q78. How many times does this loop print "exterminate"?

```java
for (int i = 44; i > 40; i--) {
    System.out.println("exterminate");
}
```

- [ ] two
- [x] four
- [ ] three
- [ ] five

#### Q79. What is the value of myCharacter after line 3 is run?

```java
1: public class Main {
2:   public static void main (String[] args) {
3:     char myCharacter = "piper".charAt(3);
4:   }
5: }
```

- [ ] p
- [ ] r
- [x] e
- [ ] i

#### Q80. When should you use a static method?

- [ ] when your method is related to the object's characteristics
- [x] when you want your method to be available independently of class instances
- [ ] when your method uses an object's instance variable
- [ ] when your method is dependent on the specific instance that calls it

#### Q81. What phrase indicates that a function receives a copy of each argument passed to it rather than a reference to the objects themselves?

- [ ] pass by reference
- [ ] pass by occurrence
- [x] pass by value
- [ ] API call

#### Q82. In Java, what is the scope of a method's argument or parameter?

- [x] inside the method
- [ ] both inside and outside the method
- [ ] neither inside nor outside the method
- [ ] outside the method

#### Q83. What is the output of this code?

```java
public class Main {
  public static void main (String[] args) {
    int[] sampleNumbers = {8, 5, 3, 1};
    System.out.println(sampleNumbers[2]);
  }
}
```

- [ ] 5
- [ ] 8
- [ ] 1
- [x] 3

#### Q84. Which change will make this code compile successfully?

```java
1: public class Main {
2:   String MESSAGE ="Hello!";
3:   static void print(){
4:     System.out.println(message);
5:   }
6:   void print2(){}
7: }
```

- [ ] Change line 2 to `public static final String message`
- [ ] Change line 6 to `public void print2(){}`
- [ ] Remove the body of the `print2` method and add a semicolon.
- [x] Remove the body of the `print` method.

**Explanation**: Changing line 2 to `public static final String message` raises the error `message not initialized in the default constructor`

#### Q85. What is the output of this code?

```java
import java.util.*;
class Main {
  public static void main(String[] args) {
    String[] array = new String[]{"A", "B", "C"};
    List<String> list1 = Arrays.asList(array);
    List<String> list2 = new ArrayList<>(Arrays.asList(array));
    List<String> list3 = new ArrayList<>(Arrays.asList("A", new String("B"), "C"));
    System.out.print(list1.equals(list2));
    System.out.print(list1.equals(list3));
  }
}
```

- [ ] falsefalse
- [x] truetrue
- [ ] falsetrue
- [ ] truefalse

#### Q86. Which code snippet is valid?

- [ ] `ArrayList<String> words = new ArrayList<String>(){"Hello", "World"};`
- [ ] `ArrayList words = Arrays.asList("Hello", "World");`
- [ ] `ArrayList<String> words = {"Hello", "World"};`
- [x] `ArrayList<String> words = new ArrayList<>(Arrays.asList("Hello", "World"));`

#### Q87. What is the output of this code?

```java
class Main {
  public static void main(String[] args) {
    StringBuilder sb = new StringBuilder("hello");
    sb.deleteCharAt(0).insert(0, "H")." World!";
    System.out.println(sb);
  }
}
```

- [x] A runtime exception is thrown.
- [ ] "HelloWorld!"
- [ ] "hello"
- [ ] ????

#### Q88. How would you use the TaxCalculator to determine the amount of tax on $50?

```java
class TaxCalculator {
  static calculate(total) {
    return total * .05;
  }
}
```

- [x] TaxCalculator.calculate(50);
- [ ] new TaxCalculator.calculate(50);
- [ ] calculate(50);
- [ ] new TaxCalculator.calculate($50);

**Note:** This code won't compile, broken code sample

1. [Reference](https://www.geeksforgeeks.org/static-methods-vs-instance-methods-java/)
2. [Code sample](https://replit.com/@mattheweller/EverlastingShadyBraces#TaxCalculator.java)

#### Q89. Which characteristic does not apply to instances of java.util.HashSet=

- [ ] uses hashcode of objects when inserted
- [ ] contains unordred elements
- [ ] contains unique elements
- [x] contains sorted elements

**Explanation**: HashSet makes no guarantees as to the iteration order of the set; in particular, it does not guarantee that the order will remain constant over time.

[Reference](https://docs.oracle.com/javase/7/docs/api/java/util/HashSet.html)

#### Q90. What is the output?

```java
import java.util.*;

public class Main {
	public static void main(String[] args)
	{
		PriorityQueue<Integer> queue = new PriorityQueue<>();
		queue.add(4);
		queue.add(3);
		queue.add(2);
		queue.add(1);

		while (queue.isEmpty() == false) {
			System.out.printf("%d", queue.remove());
		}
	}
}
```

- [ ] 1 3 2 4
- [ ] 4 2 3 1
- [x] 1 2 3 4
- [ ] 4 3 2 1

#### Q91. What will this code print, assuming it is inside the main method of a class?

`System.out.println("hello my friends".split(" ")[0]);`

- [ ] my
- [ ] hellomyfriends
- [x] hello
- [ ] friends

#### Q92. You have an instance of type Map<String, Integer> named instruments containing the following key-value pairs: guitar=1200, cello=3000, and drum=2000. If you add the new key-value pair cello=4500 to the Map using the put method, how many elements do you have in the Map when you call instruments.size()?

- [ ] 2
- [ ] When calling the put method, Java will throw an exception
- [ ] 4
- [x] 3

#### Q93. Which class acts as root class for Java Exception hierarchy?

- [ ] Clonable
- [x] Throwable
- [ ] Object
- [ ] Serializable

#### Q94. Which class does not implement the java.util.Collection interface?

- [ ] java.util.Vector
- [ ] java.util.ArrayList
- [ ] java.util.HashSet
- [x] java.util.HashMap

**Explanation**: HashMap class implements Map interface.

#### Q95. You have a variable of named `employees` of type `List<Employee>` containing multiple entries. The `Employee` type has a method `getName()` that returns the employee name. Which statement properly extracts a list of employee names?

- [ ] `employees.collect(employee -> employee.getName());`
- [ ] `employees.filter(Employee::getName).collect(Collectors.toUnmodifiableList());`
- [x] `employees.stream().map(Employee::getName).collect(Collectors.toList());`
- [ ] `employees.stream().collect((e) -> e.getName());`

#### Q96. This code does not compile. What needs to be changed so that it does?

```java
public enum Direction {
    EAST("E"),
    WEST("W"),
    NORTH("N"),
    SOUTH("S");

    private final String shortCode;

    public String getShortCode() {
        return shortCode;
    }
}
```

- [x] Add a constructor that accepts a `String` parameter and assigns it to the field `shortCode`.
- [ ] Remove the `final` keyword for the field `shortCode`.
- [ ] All enums need to be defined on a single line of code.
- [ ] Add a setter method for the field `shortCode`.

#### Q97. Which language feature ensures that objects implementing the `AutoCloseable` interface are closed when it completes?

- [ ] try-catch-finally
- [ ] try-finally-close
- [x] try-with-resources
- [ ] try-catch-close

#### Q98. What code should go in line 3?

```java
class Main {
    public static void main(String[] args) {

        array[0] = new int[]{1, 2, 3};
        array[1] = new int[]{4, 5, 6};
        array[2] = new int[]{7, 8, 9};
        for (int i = 0; i < 3; i++)
            System.out.print(array[i][1]); //prints 258
    }
}
```

- [ ] `int[][] array = new int[][];`
- [x] `int[][] array = new int[3][3];`
- [ ] `int[][] array = new int[2][2];`
- [ ] `int[][] array = [][];`

#### Q99. Is this an example of method overloading or overriding?

```java
class Car {
    public void accelerate() {}
}
class Lambo extends Car {
    public void accelerate(int speedLimit) {}
    public void accelerate() {}
}
```

- [ ] neither
- [x] both
- [ ] overloading
- [ ] overriding

#### Q100. Which choice is the best data type for working with money in Java?

- [ ] float
- [ ] String
- [ ] double
- [x] BigDecimal

[Reference](https://www.scaler.com/topics/java/primitive-data-types/#types-of-primitive-data-types-in-java)

#### Q101. Which statement about constructors is not ture?

- [ ] A class can have multiple constructors with a different parameter list.
- [ ] You can call another constructor with `this` or `super`.
- [ ] A constructor does not define a return value.
- [x] Every class must explicitly define a constructor without parameters.

#### Q102. What language feature allows types to be parameters on classes, interfaces, and methods in order to reuse the same code for different data types?

- [ ] Regular Expressions
- [ ] Reflection
- [x] Generics
- [ ] Concurrency

#### Q103. What will be printed?

```java
public class Berries{

    String berry = "blue";

    public static void main(String[] args) {
        new Berries().juicy("straw");
    }
    void juicy(String berry){
        this.berry = "rasp";
        System.out.println(berry + "berry");
    }
}
```

- [ ] raspberry
- [x] strawberry
- [ ] blueberry
- [ ] rasp

#### Q104. What is the value of `forestCount` after this code executes?

```java
Map<String, Integer> forestSpecies = new HashMap<>();

forestSpecies.put("Amazon", 30000);
forestSpecies.put("Congo", 10000);
forestSpecies.put("Daintree", 15000);
forestSpecies.put("Amazon", 40000);

int forestCount = forestSpecies.size();
```

- [x] 3
- [ ] 4
- [ ] 2
- [ ] When calling the put method, Java will throw an exception

#### Q105. What is a problem with this code?

```java
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;


class Main {

    public static void main(String[] args) {
        List<String> list = new ArrayList<String>(Arrays.asList("a", "b", "c"));
        for(String value :list) {
            if(value.equals("a")) {
                list.remove(value);
            }
        }
        System.out.println(list); // outputs [b,c]
    }
}
```

- [ ] String should be compared using == method instead of equals.
- [x] Modifying a collection while iterating through it can throw a ConcurrentModificationException.
- [ ] The List interface does not allow an argument of type String to be passed to the remove method.
- [ ] ArrayList does not implement the List interface.

#### Q106. How do you convert this method into a lambda expression?

```java
public int square(int x) {
    return x * x;
}
```

- [ ] `Function<Integer, Integer> squareLambda = (int x) -> { x * x };`
- [ ] `Function<Integer, Integer> squareLambda = () -> { return x * x };`
- [x] `Function<Integer, Integer> squareLambda = x -> x * x;`
- [ ] `Function<Integer, Integer> squareLambda = x -> return x * x;`

#### Q107. Which choice is a valid implementation of this interface?

```java
interface MyInterface {
    int foo(int x);
}
```

- [ ] A

```java
public class MyClass implements MyInterface {
    // ....
    public void foo(int x){
        System.out.println(x);
    }
}
```

- [ ] B

```java
public class MyClass implements MyInterface {
    // ....
    public double foo(int x){
        return x * 100;
    }
}
```

- [x] C

```java
public class MyClass implements MyInterface {
    // ....
    public int foo(int x){
        return x * 100;
    }
}
```

- [ ] D

```java
public class MyClass implements MyInterface {
    // ....
    public int foo(){
        return 100;
    }
}
```

#### Q108. What is the result of this program?

```java
interface Foo {
    int x = 10;
}

public class Main{

    public static void main(String[] args) {
        Foo.x = 20;
        System.out.println(Foo.x);
    }
}
```

- [ ] 10
- [ ] 20
- [ ] null
- [x] An error will occur when compiling.

#### Q109. Which statement must be inserted on line 1 to print the value true?

```java
1:
2: Optional<String> opt = Optional.of(val);
3: System.out.println(opt.isPresent());
```

- [ ] `Integer val = 15;`
- [x] `String val = "Sam";`
- [ ] `String val = null;`
- [ ] `Optional<String> val = Optional.empty();`

#### Q110. What will this code print, assuming it is inside the main method of a class?

```java
System.out.println(true && false || true);
System.out.println(false || false && true);
```

- [ ] false </br> true
- [ ] true </br> true
- [x] true </br> false
- [ ] false </br> false

#### Q111. What will this code print?

```java
List<String> list1 = new ArrayList<>();
list1.add("One");
list1.add("Two");
list1.add("Three");

List<String> list2 = new ArrayList<>();
list2.add("Two");

list1.remove(list2);
System.out.println(list1);
```

- [ ] `[Two]`
- [x] `[One, Two, Three]`
- [ ] `[One, Three]`
- [ ] `Two`

#### Q112. Which code checks whether the characters in two Strings,named `time` and `money`, are the same?

- [ ] `if(time <> money){}`
- [x] `if(time.equals(money)){}`
- [ ] `if(time == money){}`
- [ ] `if(time = money){}`

#### Q113. An **\_** is a serious issue thrown by the JVM that the JVM is unlikely to recover from. An **\_** is an unexpected event that an application may be able to deal with in order to continue execution.

- [ ] exception,assertion
- [ ] AbnormalException, AccidentalException
- [x] error, exception
- [ ] exception, error

#### Q114. Which keyword would not be allowed here?

```java
class Unicorn {
    _____ Unicorn(){}
}
```

- [x] static
- [ ] protected
- [ ] public
- [ ] void

#### Q115. Which OOP concept is this code an example of?

```java
List[] myLists = {
    new ArrayList<>(),
    new LinkedList<>(),
    new Stack<>(),
    new Vector<>(),
};

for (List list : myLists){
    list.clear();
}
```

- [ ] composition
- [ ] generics
- [x] polymorphism
- [ ] encapsulation

**Explanation:** switch between different implementations of the `List` interface

#### Q116. What does this code print?

```java
String a = "bikini";
String b = new String("bikini");
String c = new String("bikini");

System.out.println(a == b);
System.out.println(b == c);
```

- [ ] true; false
- [x] false; false
- [ ] false; true
- [ ] true; true

**Explanation:** `== operator` compares the object reference. `String a = "bikini"; String b = "bikini";` would result in True. Here new creates a new object, so false. Use `equals() method` to compare the content.

#### Q117. What keyword is added to a method declaration to ensure that two threads do not simultaneously execute it on the same object instance?

- [ ] native
- [ ] volatile
- [x] synchronized
- [ ] lock

[Java Documentation: Synchronized methods](https://docs.oracle.com/javase/tutorial/essential/concurrency/syncmeth.html)

#### Q118. Which is a valid type for this lambda function?

```java
_____ oddOrEven = x -> {
    return x % 2 == 0 ? "even" : "odd";
};
```

- [ ] `Function<Integer, Boolean>`
- [ ] `Function<String>`
- [x] `Function<Integer, String>`
- [ ] `Function<Integer>`

[Explaination](https://github.com/0nyr/java/tree/main/examples/lambda_function), [Reference](https://www.geeksforgeeks.org/function-interface-in-java-with-examples/)

#### Q119. What is displayed when this code is compiled and executed?

```java
import java.util.HashMap;

public class Main {
    public static void main(String[] args) {
        HashMap<String, Integer> pantry = new HashMap<>();

        pantry.put("Apples", 3);
        pantry.put("Oranges", 2);

        int currentApples = pantry.get("Apples");
        pantry.put("Apples", currentApples + 4);

        System.out.println(pantry.get("Apples"));
    }
}
```

- [ ] 6
- [ ] 3
- [ ] 4
- [x] 7

[Explanation](https://github.com/0nyr/java/tree/main/training/linkedin_assessment/what_is_displayed_0)

#### Q120. What variable type should be declared for capitalize?

```shell
List<String> songTitles = Arrays.asList("humble", "element", "dna");
_______ capitalize = (str) -> str.toUpperCase();
songTitles.stream().map(capitalize).forEach(System.out::println);
```

- [x] `Function<String, String>`
- [ ] `Stream<String>`
- [ ] `String<String, String>`
- [ ] `Map<String, String>`

[Explanation](https://github.com/0nyr/java/tree/main/training/linkedin_assessment/what_variable_type_0), [Reference](https://www.geeksforgeeks.org/function-interface-in-java-with-examples/)

#### Q121. Which is the correct return type for the processFunction method?

```java
_____ processFunction(Integer number, Function<Integer, String> lambda) {
        return lambda.apply(number);
    }
```

- [ ] `Integer`
- [x] `String`
- [ ] `Consumer`
- [ ] `Function<Integer, String>`

[Explanation](https://github.com/0nyr/java/tree/main/training/linkedin_assessment/which_return_type_0)

#### Q122. What function could you use to replace slashes for dashes in a list of dates?

```java
List<String> dates = new ArrayList<String>();
// missing code
dates.replaceAll(replaceSlashes);
```

- [x] `UnaryOperator<String> replaceSlashes = date -> date.replace("/", "-");`
- [ ] `Function<String, String> replaceSlashes = dates -> dates.replace("-", "/");`
- [ ] `Map<String, String> replaceSlashes = dates.replace("/", "-");`
- [ ] `Consumer<Date> replaceSlashes = date -> date.replace("/", "-");`

**Explanation:** `replaceAll` method for any List<T> only accepts UnaryOperator<T> to pass every single element into it then put the result into the List<T> again.

#### Q123. From which class do all other classes implicitly extend?

- [x] `Object`
- [ ] `Main`
- [ ] `Java`
- [ ] `Class`

[Explanation](https://stackoverflow.com/questions/17187218/default-class-that-is-extended-by-all-classes-in-java)

#### Q124. How do you create and run a Thread for this class?

```java
import java.util.date;

public class CurrentDateRunnable implements Runnable {
    @Override
    public void run () {
        while (true) {
            System.out.println("Current date: " + new Date());

            try {
                Thread.sleep(5000);
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
        }
    }
}
```

- [x] `Thread thread = new Thread(new CurrentDateRunnable()); thread.start();`
- [ ] `new Thread(new CurrentDateRunnable()).join();`
- [ ] `new CurrentDateRunnable().run();`
- [ ] `new CurrentDateRunnable().start();`

[Reference](https://www.w3schools.com/java/java_threads.asp)

#### Q125. Which expression is a functional equivalent?

```java
List<Integer> numbers = List.of(1,2,3,4);
int total = 0;

for (Integer x : numbers) {
    if (x % 2 == 0)
    total += x * x;
}
```

- [ ] A

```java
int total = numbers.stream()
                        .transform(x -> x * x)
                        .filter(x -> x % 2 == 0)
                        .sum ();
```

- [ ] B

```java
int total = numbers.stream()
                        .filter(x -> x % 2 == 0)
                        .collect(Collectors.toInt());
```

- [ ] C

```java
int total = numbers.stream()
                        .mapToInt (x -> {if (x % 2 == 0) return x * x;})
                        .sum();
```

- [x] D

```java
int total = numbers.stream()
                        .filter(x -> x % 2 == 0)
                        .mapToInt(x -> x * x)
                        .sum();
```

**Explanation:** The given code in the question will give you the output 20 as total

```java
numbers                         // Input `List<Integer>` > [1, 2, 3, 4] <br>
    .stream()                   // Converts input into `Stream<Integer>` <br>
    .filter(x -> x % 2 == 0)    // Filter even numbers and return `Stream<Integer>` > [2, 4] <br>
    .mapToInt(x -> x * x)       // Square the number, converts `Integer` to an `int`, and returns `IntStream` > [4, 16] <br>
    .sum()                      // Returns the sum as `int` > 20
```

#### Q126. Which is not one of the standard input/output streams provided by java.lang.System?

- [x] print
- [ ] out
- [ ] err
- [ ] in

#### Q127. The compiler is complaining about this assignment of the variable pickle to the variable jar. How woulld you fix this?

```java
double pickle = 2;
int jar = pickle;
```

- [ ] Use the method toInt() to convert pickle before assigning it to jar.
- [x] Cast pickle to an int before assigning it to jar.
- [ ] Make pickle into a double by adding + ".0"
- [ ] Use the new keyword to create a new Integer from pickle before assigning it to jar.

#### Q128. What value should x have to make this loop execute 10 times?

```java
for(int i=0; i<30; i+=x) {}
```

- [ ] 10
- [x] 3
- [ ] 1
- [ ] 0

#### Q129. The **\_** runs compiled Java code, while the **\_** compiles Java files.

- [ ] IDE; JRE
- [ ] JDK; IDE
- [x] JRE; JDK
- [ ] JDK; JRE

[Reference](https://stackoverflow.com/questions/1906445/what-is-the-difference-between-jdk-and-jre)

#### Q130. Which packages are part of Java Standard Edition

- [ ] java.net
- [ ] java.util
- [ ] java.lang
- [x] All above

[Reference](https://docs.oracle.com/en/java/javase/11/docs/api/allpackages-index.html)

#### Q131. What values for x and y will cause this code to print "btc"?

```java
String buy = "bitcoin";
System.out.println(buy.substring(x, x+1) + buy.substring(y, y+2))
```

- [x] int x = 0; int y = 2;
- [ ] int x = 1; int y = 3;
- [ ] int x = 0; int y = 3;
- [ ] int x = 1; int y = 3;

#### Q132. Which keyword would you add to make this method the entry point of the program?

- [ ] exception
- [ ] args
- [x] static
- [ ] String

[Reference](https://www.geeksforgeeks.org/java-main-method-public-static-void-main-string-args/)

#### Q133. You have a list of Bunny objects that you want to sort by weight using Collections.sort. What modification would you make to the Bunny class?

- [x] Implement the comparable interface by overriding the compareTo method.
- [ ] Add the keyword default to the weight variable.
- [ ] Override the equals method inside the Bunny class.
- [ ] Implement Sortable and override the sortBy method.

[Reference](https://www.geeksforgeeks.org/how-to-override-compareto-method-in-java/)

#### Q134. Identify the incorrect Java feature.

- [ ] Object oriented
- [x] Use of pointers
- [ ] Dynamic
- [ ] Architectural neural

[Reference](https://www.interviewbit.com/blog/features-of-java/)

#### Q135. What is the output of this code?

```java
int yearsMarried = 2;
switch (yearsMarried) {
   case 1:
      System.out.println("paper");
   case 2:
      System.out.println("cotton");
   case 3:
      System.out.println("leather");
   default:
      System.out.println("I don't gotta buy gifts for nobody!");
}
```

- [ ] cotton
- [ ] cotton <br> leather
- [x] cotton <br> leather <br> I don't gotta buy gifts for nobody!
- [ ] cotton <br> I don't gotta buy gifts for nobody!

#### Q136. What language feature do these expressions demonstrate?

```System.out::println
Doggie::fetch
```

- [ ] condensed invocation
- [ ] static references
- [x] method references
- [ ] bad code

#### Q137. What is the difference between the wait() and sleep methods?

- [ ] Only Threads can wait, but any Object can be put to sleep.
- [ ] A wait can be woken up by another Thread calling notify whereas a sleep cannot.
- [x] When things go wrong, sleep throws an IllegalMonitorStateException whereas wait throws an InterruptedException.
- [ ] Sleep allows for multi-threading whereas wait does not.

#### Q138. Which is the right way to declare an enumeration of cats?

- [ ] enum Cats (SPHYNX, SIAMESE, BENGAL);
- [ ] enum Cats ("sphynx", "siamese", "bengal");
- [x] enum Cats {SPHYNX, SIAMESE, BENGAL}
- [ ] enum Cats {"sphynx","siamese","bengal}

#### Q139. What happens when this code is run?

```java
List<String> horses = new ArrayList<String>();
horses.add (" Sea Biscuit ");
System.out.println(horses.get(1).trim());
```

- [ ] "Sea Biscuit" will be printed.
- [ ] " Sea Biscuit " will be printed.
- [x] An IndexOutOfBoundsException will be thrown.
- [ ] A NullPointerException will be thrown.

#### Q140. Which data structure would you choose to associate the amount of rainfall with each month?

- [ ] Vector
- [ ] LinkedList
- [x] Map
- [ ] Queue

> Explanation (from @yktsang01 in #3915 thread)

> Map because map is a key/value pair without creating new classes/objects. So can store the rainfall per month like
> `Map<java.time.Month, Double>`
> The other options will most likely need some new class to be meaningful

```java
public class Rainfall {
private java.time.Month month;
private double rainfall;
}
Vector<Rainfall>
LinkedList<Rainfall>
Queue<Rainfall>
```

#### Q141. Among the following which contains date information.

- [x] java.sql timestamp
- [ ] java.io time
- [ ] java.io.timestamp
- [ ] java.sql.time

#### Q142. What is the size of float and double in java?

- [x] 32 and 64
- [ ] 32 and 32
- [ ] 64 and 64
- [ ] 64 and 32

#### Q143. When you pass an object reference as an argument to a method call what gets passed?

- [ ] a reference to a copy
- [ ] a copy of the reference
- [ ] the object itself
- [x] the original reference

#### Q144. Which choice demonstrates a valid way to create a reference to a static function of another class?

- [x] Function<Integer, Integer> funcReference = MyClass::myFunction;
- [ ] Function<Integer, Integer> funcReference = MyClass.myFunction;
- [ ] Function<Integer, Integer> funcReference = MyClass().myFunction();
- [ ] Function<Integer, Integer> funcReference = MyClass::myFunction();

#### Q145. What is UNICODE?

- [ ] Unicode is used for external representation of words and strings
- [ ] Unicode is used for internal representation of characters and strings
- [x] Unicode is used for external representation of characters and strings
- [ ] Unicode is used for internal representation of words and strings

#### Q146. What kind of thread is the Garbage collector thread?

- [ ] User thread
- [x] Daemon thread
- [ ] Both
- [ ] None of these

#### Q147. What is HashMap and Map?

- [ ] HashMap is Interface and map is class that implements that
- [ ] HashMap is class and map is interface that implements that
- [ ] Map is class and Hashmap is interface that implements that
- [x] Map is Interface and Hashmap is class that implements that

#### Q148. What invokes a thread's run() method?

- [x] JVM invokes the thread's run() method when the thread is initially executed.
- [ ] Main application running the thread.
- [ ] start() method of the thread class.
- [ ] None of the above.

**Explanation:** After a thread is started, via its start() method of the Thread class, the JVM invokes the thread's run() method when the thread is initially executed.

#### Q149. What is true about a final class?

- [ ] class declared final is a final class.
- [ ] Final classes are created so the methods implemented by that class cannot be overriddden.
- [ ] It can't be inherited.
- [x] All of the above.

[Explanation](Final classes are created so the methods implemented by that class cannot be overridden. It can't be inherited. These classes are declared final.)

#### Q150. Which method can be used to find the highest value of x and y?

- [ ] Math.largest(x,y)
- [ ] Math.maxNum(x,y)
- [x] Math.max(x,y)
- [ ] Math.maximum(x,y)

#### Q151. What do these statments evaluate to?

- [ ] 1. false 2. true
- [ ] 1. false 2. false
- [ ] 1. true 2. true
- [x] 1. true 2. false

#### Q151. `void accept(T t)` is method of -?

- [x] Consumer
- [ ] Producer
- [ ] Both
- [ ] None

#### Q152. Which of these does `Stream filter()` operates on?

- [x] Predicate
- [ ] Interface
- [ ] Class
- [ ] Methods

#### Q153. Which of these does `Stream map()` operates on?

- [ ] Class
- [ ] Interface
- [ ] Predicate
- [x] Function

#### Q154. What code is needed at line 8?

```java
1: class Main {

2:      public static void main(String[] args) {

3:          Map<String, Integer> map = new HashMap<>();
4:          map.put("a", 1);
5:          map.put("b", 2);
6:          map.put("c", 3);

7:          int result = 0;

8:
9:              result += entry.getValue();
10:         }

11:         System.out.println(result); // outputs 6
12:     }
13: }
```

- [ ] for(MapEntry<String, Integer> entry: map.entrySet()) {
- [ ] for(String entry: map) {
- [ ] for(Integer entry: map.values()) {
- [x] for(Entry<String, Integer> entry: map.entrySet()) {

#### Q155. What will print when Lambo is instantiated?

```java
class Car {
    String color = "blue";
}

class Lambo extends Car {
    String color = "white";

    public Lambo() {
        System.out.println(super.color);
        System.out.println(this.color);
        System.out.println(color);
    }
}
```

- [x] blue
      white
      white
- [ ] blue
      white
      blue
- [ ] white
      white
      white
- [ ] white
      white
      blue

### Q156. Which command will run a FrogSounds app that someone emailed to you as a jar?

- [ ] jar FrogSounds.java
- [ ] javac FrogSounds.exe
- [ ] jar cf FrogSounds.jar
- [x] java -jar FrogSounds.jar

#### Q157. What is the default value of short variable?

- [x] 0
- [ ] 0.0
- [ ] null
- [ ] undefined

#### Q158. What will be the output of the following Java program?

```java
class variable_scope {
	public static void main(String args[])
        {
            int x;
            x = 5;
            {
	        int y = 6;
	        System.out.print(x + " " + y);
            }
            System.out.println(x + " " + y);
        }
}
```

- [x] Compilation Error
- [ ] Runtime Error
- [ ] 5 6 5 6
- [ ] 5 6 5

#### Q159. Subclasses of an abstract class are created using the keyword **\_**.

- [x] extends
- [ ] abstracts
- [ ] interfaces
- [ ] implements

[Reference See An Abstract Class Example ](https://docs.oracle.com/javase/tutorial/java/IandI/abstract.html)

#### Q160. Which keyword would not be allowed here?

```
class Unicorn {
_____ Unicorn(){}
}
```

- [ ] public
- [ ] static
- [ ] protected
- [x] void

Explaination : A constructor cannot have a return type (not even a void return type).

#### Q161. What language feature do these expressions demonstrate?

```
System.out::println
Doggie::fetch
```

- [x] method references
- [ ] bad code
- [ ] condensed invocation
- [ ] static references

[Reference](https://stackoverflow.com/questions/31020269/what-is-the-use-of-system-outprintln-in-java-8)

#### Q162. What will be the output of the following program?

```java
import java.util.Formatter;
public class Course {
    public static void main(String[] args) {
        Formatter data = new Formatter();
        data.format("course %s", "java ");
        System.out.println(data);
        data.format("tutorial %s", "Merit campus");
        System.out.println(data);
    }
}
```

- [ ] course java
      tutorial Merit campus
- [x] course java
      course java tutorial Merit campus
- [ ] Compilation Error
- [ ] Runtime Error
