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

#### Q4. <DUPLICATE OF Q34>

#### Q5. What is the output of this code?

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

#### Q6. Which of the following can replace the CODE SNIPPET to make the code below print "Hello World"?

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

#### Q7. What does the following code print?

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

#### Q8. What is the result of this code?

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

#### Q9. Which class can compile given these declarations?

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

#### Q10. What is the output of this code?

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

#### Q11. Given the following two classes, what will be the output of the Main class?

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

**Explanation:** `The answer is "123". The `abs()` method evaluates to the one inside mypackage.Math class.`

#### Q12. What is the result of this code?

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

**Explanation:** Compilation error at line 10 because of final methods cannot be overridden, and here message() is a final method,
and also note that Non-static method message() cannot be referenced from a static context.

#### Q13. Given this code, which command will output "2"?

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

#### Q14. What is the output of this code?

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

**Reasoning:** The int type in Java can be used to represent any whole number from -2147483648 to 2147483647. Therefore this code will not compile as the number assigned to 'a' is larger than the int type can hold.

#### Q15. What is the output of this code?

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

#### Q16. How do you write a foreach loop that will iterate over ArrayList\<Pencil\>pencilCase?

- [x] `for (Pencil pencil : pencilCase) {}`
- [ ] `for (pencilCase.next()) {}`
- [ ] `for (Pencil pencil : pencilCase.iterator()) {}`
- [ ] `for (pencil in pencilCase) {}`

#### Q17. <DUPLICATE of Q30>

#### Q18. <DUPICATE OF Q31>

#### Q19. What does this code print?

```java
System.out.print("apple".compareTo("banana"));
```

- [ ] `0`
- [ ] positive number
- [x] negative number
- [ ] compilation error

#### Q20. You have an ArrayList of names that you want to sort alphabetically. Which approach would **NOT** work?

- [ ] `names.sort(Comparator.comparing(String::toString))`
- [ ] `Collections.sort(names)`
- [x] `names.sort(List.DESCENDING)`
- [ ] `names.stream().sorted((s1, s2) -> s1.compareTo(s2)).collect(Collectors.toList())`

#### Q21. By implementing encapsulation, you cannot directly access the class's \_ properties unless you are writing code inside the class itself.

- [x] private
- [ ] protected
- [ ] no-modifier
- [ ] public

#### Q22. Which is the most up-to-date way to instantiate the current date?

- [ ] `new SimpleDateFormat("yyyy-MM-dd").format(new Date())`
- [ ] `new Date(System.currentTimeMillis())`
- [x] `LocalDate.now()`
- [ ] `Calendar.getInstance().getTime()`

**Explanation**: LocalDate is newest class added in java 8

#### Q23. Fill in the blank to create a piece of code that will tell whether `int0` is divisible by `5`:

`boolean isDivisibleBy5 = _____`

- [ ] `int0 / 5 ? true: false`
- [x] `int0 % 5 == 0`
- [ ] `int0 % 5 != 5`
- [ ] `Math.isDivisible(int0, 5)`

#### Q24. How many times will this code print "Hello World!"?

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

**Explanation**: Observe the loop increment. It's not an increment, it's an assignment(post).

#### Q25. The runtime system starts your program by calling which function first?

- [ ] print
- [ ] iterative
- [ ] hello
- [x] main

#### 26. What code would you use in Constructor A to call Constructor B?

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

  **Note:** This code won't compile, possibly broken code sample.

#### Q27. Which statement is **NOT** true?

- [ ] An anonymous class may specify an abstract base class as its base type.
- [x] An anonymous class does not require a zero-argument constructor.
- [ ] An anonymous class may specify an interface as its base type.
- [ ] An anonymous class may specify both an abstract class and interface as base types.

#### Q28. What will this program print out to the console when executed?

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

#### Q29. What is the output of this code?

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

#### Q30. Object-oriented programming is a style of programming where you organize your program around \_ rather than \_ and data rather than logic.

- [ ] functions; actions
- [x] objects; actions
- [ ] actions; functions
- [ ] actions; objects

#### Q31. What statement returns true if "nifty" is of type String?

- [ ] `"nifty".getType().equals("String")`
- [ ] `"nifty".getType() == String`
- [ ] `"nifty".getClass().getSimpleName() == "String"`
- [x] `"nifty" instanceof String`

#### Q32. What is the output of this code?

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

#### Q33. What is the result of this code?

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

#### Q34. What method can be used to create a new instance of an object?

- [ ] another instance
- [ ] field
- [x] constructor
- [ ] private method

#### Q35. Which is the most reliable expression for testing whether the values of two string variables are the same?

- [ ] string1 == string2
- [ ] string1 = string2
- [ ] string1.matches(string2)
- [x] string1.equals(string2)

#### Q36. Which letters will print when this code is run?

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

**Explanation**: `Error` is not inherited from `Exception`

#### Q37. What is the output of this code?

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

#### Q38. What is the output of this code?

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

- [ ] [abc, 0, 2, 10]
- [ ] The code does not compile.
- [ ] [abc, 2, 10, 0]
- [x] [0, 10, 2, abc]

**Explanation**: The `java.util.Arrays.asList(T... a)` returns a fixed-size list backed by the specified array. (Changes to the returned list "write through" to the array.)

#### Q39. What is the output of this code?

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

#### Q40. What is displayed when this code is compiled and executed?

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

#### Q41. Which approach cannot be used to iterate over a List named _theList_?

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

#### Q42. What method signature will work with this code?

`boolean healthyOrNot = isHealthy("avocado");`

- [ ] public void isHealthy(String avocado)
- [x] boolean isHealthy(String string)
- [ ] public isHealthy("avocado")
- [ ] private String isHealthy(String food)

#### Q43. Which are valid keywords in a Java module descriptor (module-info.java)?

- [ ] provides, employs
- [ ] imports, exports
- [ ] consumes, supplies
- [x] requires, exports

#### Q44. Which type of variable keeps a constant value once it is assigned?

- [ ] non-static
- [ ] static
- [x] final
- [ ] private

#### Q45. How does the keyword `volatile` affect how a variable is handled?

- [ ] It will be read by only one thread at a time.
- [ ] It will be stored on the hard drive.
- [x] It will never be cached by the CPU.
- [ ] It will be preferentially garbage collected.

#### Q46. What is the result of this code?

```java
char smooch = 'x';
System.out.println((int) smooch);
```

- [ ] an alphanumeric character
- [ ] a negative number
- [x] a positive number
- [ ] a ClassCastException

#### Q47. You get a NullPointerException. What is the most likely cause?

- [ ] A file that needs to be opened cannot be found.
- [ ] A network connection has been lost in the middle of communications.
- [ ] Your code has used up all available memory.
- [x] The object you are using has not been instantiated.

#### Q48. How would you fix this code so that it compiles?

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

#### Q49. Add a Duck called "Waddles" to the ArrayList **ducks**.

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

#### Q50. If you encounter `UnsupportedClassVersionError` it means the code was `___` on a newer version of Java than the JRE `___` it.

- [ ] executed; interpreting
- [ ] executed; compiling
- [x] compiled; executing
- [ ] compiled, translating

#### Q51. Given this class, how would you make the code compile?

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

#### Q52. How many times f will be printed?

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

#### Q53. Which statements about `abstract` classes are true?

```
1. They can be instantiated.
2. They allow member variables and methods to be inherited by subclasses.
3. They can contain constructors.
```

- [ ] 1, 2, and 3
- [ ] only 3
- [x] 2 and 3
- [ ] only 2

#### Q54. Which keyword lets you call the constructor of a parent class?

- [ ] parent
- [x] super
- [ ] this
- [ ] new

#### Q55. What is the result of this code?

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

#### Q56. Normally, to access a static member of a class such as Math.PI, you would need to specify the class "Math". What would be the best way to allow you to use simply "PI" in your code?

- [x] Add a static import.
- [ ] Declare local copies of the constant in your code.
- [ ] This cannot be done. You must always qualify references to static members with the class form which they came from.
- [ ] Put the static members in an interface and inherit from that interface.

#### Q57. Which keyword lets you use an interface?

- [ ] extends
- [x] implements
- [ ] inherits
- [ ] import

#### Q58. Why are ArrayLists better than arrays?

- [x] You don't have to decide the size of an ArrayList when you first make it.
- [ ] You can put more items into an ArrayList than into an array.
- [ ] ArrayLists can hold more kinds of objects than arrays.
- [ ] You don't have to decide the type of an ArrayList when you first make it.

#### Q59. Declare a variable that holds the first four digits of Π

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

#### Q60. Use the magic power to cast a spell

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

#### Q61. What language construct serves as a blueprint containing an object's properties and functionality?

- [ ] constructor
- [ ] instance
- [x] class
- [ ] method

#### Q62. What does this code print?

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

#### Q63. What is the result of this code?

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

#### Q64. What is not a java keyword

- [ ] finally
- [ ] native
- [ ] interface
- [x] unsigned

**Explanation:** `native` is a part of JNI interface

#### Q65. Which operator would you use to find the remainder after division?

- [x] `%`
- [ ] `//`
- [ ] `/`
- [ ] `DIV`

[Reference](http://www.cs.ukzn.ac.za/~hughm/java/intro/week2/21.html)

#### Q66. Which choice is a disadvantage of inheritance?

- [ ] Overridden methods of the parent class cannot be reused.
- [ ] Responsibilities are not evenly distributed between parent and child classes.
- [x] Classes related by inheritance are tightly coupled to each other.
- [ ] The internal state of the parent class is accessible to its children.

[Reference](http://erpbasic.blogspot.com/2012/01/inheritance-advantages-and.html#:~:text=Main%20disadvantage%20of%20using%20inheritance,used%20independent%20of%20each%20other.&text=4.,case%20of%20using%20that%20method.)

#### Q67. Declare and initialize an array of 10 ints.

- [ ] `Array<Integer> numbers = new Array<Integer>(10);`
- [ ] `Array[int] numbers = new Array[int](10);`
- [x] `int[] numbers = new int[10];`
- [ ] `int numbers[] = int[10];`

#### Q68. Refactor this event handler to a lambda expression:

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

#### Q69. Which functional interfaces does Java provide to serve as data types for lambda expressions?

- [ ] Observer, Observable
- [ ] Collector, Builder
- [ ] Filter, Map, Reduce
- [x] Consumer, Predicate, Supplier

[Reference](https://www.baeldung.com/java-8-functional-interfaces)

#### Q69. What is a valid use of the hashCode() method?

- [ ] encrypting user passwords
- [x] deciding if two instances of a class are equal
- [ ] enabling HashMap to find matches faster
- [ ] moving objects from a List to a HashMap

[Reference](https://www.baeldung.com/java-hashcode)

#### Q70. What kind of relationship does "extends" denote?

- [ ] uses-a
- [x] is-a
- [ ] has-a
- [ ] was-a

[Reference](https://www.c-sharpcorner.com/UploadFile/3614a6/is-a-and-has-a-relationship-in-java/)

#### Q71. How do you force an object to be garbage collected?

- [ ] Set object to null and call Runtime.gc()
- [x] Set object to null and call System.gc()
- [ ] Set object to null and call Runtime.getRuntime().runFinalization()
- [ ] There is no way to force an object to be garbage collected

[Reference](https://sematext.com/blog/java-garbage-collection/)

#### Q72. Java programmers commonly use design patterns. Some examples are the **\_**, which helps create instances of a class, the **\_**, which ensures that only one instance of a class can be created; and the **\_**, which allows for a group of algorithms to be interchangeable.

- [x] static factory method; singleton; strategy pattern
- [ ] strategy pattern; static factory method; singleton
- [ ] creation pattern; singleton; prototype pattern
- [ ] singleton; strategy pattern; static factory method

#### Q73. Using Java's Reflection API, you can use \_ to get the name of a class and \_ to retrieve an array of its methods.

- [x] this.getClass().getSimpleName(); this.getClass().getDeclaredMethods()
- [ ] this.getName(); this.getMethods()
- [ ] Reflection.getName(this); Reflection.getMethods(this)
- [ ] Reflection.getClass(this).getName(); Reflection.getClass(this).getMethods()

#### Q74. Which is not a valid lambda expression?

- [ ] `a -> false;`
- [ ] `(a) -> false;`
- [x] `String a -> false;`
- [ ] `(String a) -> false;`

#### Q75. Which access modifier makes variables and methods visible only in the class where they are declared?

- [ ] public
- [ ] protected
- [ ] nonmodifier
- [x] private

#### Q76. What type of variable can be assigned to only once?

- [ ] private
- [ ] non-static
- [x] final
- [ ] static

#### Q77. How would you convert a String to an Int?

- [ ] `"21".intValue()`
- [ ] `String.toInt("21")`
- [x] `Integer.parseInt("21")`
- [ ] `String.valueOf("21")`

#### Q78. What method should be added to the Duck class to print the name Moby?

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

#### Q79. Which operator is used to concatenate Strings in Java

- [x] `+`
- [ ] `&`
- [ ] `.`
- [ ] `-`

- [Reference](https://www.techiedelight.com/concatenate-two-strings-java/)

#### Q80. How many times does this loop print "exterminate"?

```java
for (int i = 44; i > 40; i--) {
    System.out.println("exterminate");
}
```

- [ ] two
- [x] four
- [ ] three
- [ ] five

#### Q81. What is the value of myCharacter after line 3 is run?

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

#### Q82. When should you use a static method?

- [ ] when your method is related to the object's characteristics
- [x] when you want your method to be available independently of class instances
- [ ] when your method uses an object's instance variable
- [ ] when your method is dependent on the specific instance that calls it

#### Q83. What phrase indicates that a function receives a copy of each argument passed to it rather than a reference to the objects themselves?

- [ ] pass by reference
- [ ] pass by occurrence
- [x] pass by value
- [ ] API call

#### Q84. In Java, what is the scope of a method's argument or parameter?

- [x] inside the method
- [ ] both inside and outside the method
- [ ] neither inside nor outside the method
- [ ] outside the method

#### Q85. What is the output of this code?

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

#### Q86. Which change will make this code compile successfully?

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

#### Q87. What is the output of this code?

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

#### Q88. Which code snippet is valid?

- [ ] `ArrayList<String> words = new ArrayList<String>(){"Hello", "World"};`
- [ ] `ArrayList words = Arrays.asList("Hello", "World");`
- [ ] `ArrayList<String> words = {"Hello", "World"};`
- [x] `ArrayList<String> words = new ArrayList<>(Arrays.asList("Hello", "World"));`

#### Q89. What is the output of this code?

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

#### Q90. How would you use the TaxCalculator to determine the amount of tax on $50?

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

- [Reference](https://www.geeksforgeeks.org/static-methods-vs-instance-methods-java/)
- [Code sample](https://replit.com/@mattheweller/EverlastingShadyBraces#TaxCalculator.java)

#### Q91. <DUPLICATE of Q81>

#### Q92. <DUPLICATE of Q37>

#### Q93. What is the output of this code?

```java
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

- [ ] 3
- [ ] 4
- [ ] 6
- [x] 7

#### Q94. Which characteristic does not apply to instances of java.util.HashSet=

- [ ] uses hashcode of objects when inserted
- [x] contains unordred elements
- [ ] contains unique elements
- [ ] contains sorted elements

#### Q95. What is the output?

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

#### Q96. What will this code print, assuming it is inside the main method of a class?

`System.out.println("hello my friends".split(" ")[0]);`

- [ ] my
- [ ] hellomyfriends
- [x] hello
- [ ] friends

#### Q97. You have an instance of type Map<String, Integer> named instruments containing the following key-value pairs: guitar=1200, cello=3000, and drum=2000. If you add the new key-value pair cello=4500 to the Map using the put method, how many elements do you have in the Map when you call instruments.size()?

`System.out.println("hello my friends".split(" ")[0]);`

- [ ] 2
- [ ] When calling the put method, Java will throw an exception
- [ ] 4
- [x] 3

#### Q98. Which class acts as root class for Java Exception hierarchy?

- [ ] Clonable
- [x] Throwable
- [ ] Object
- [ ] Serializable

#### Q99. <DUPLICATE of Q15>

#### Q100. Which class does not implement the java.util.Collection interface?

- [ ] java.util.Vector
- [ ] java.util.ArrayList
- [ ] java.util.HashSet
- [x] java.util.HashMap

**Explanation**: HashMap class implements Map interface.

#### Q101. You have a variable of named `employees` of type `List<Employee>` containing multiple entries. The `Employee` type has a method `getName()` that returns te employee name. Which statement properly extracts a list of employee names?

- [ ] `employees.collect(employee -> employee.getName());`
- [ ] `employees.filter(Employee::getName).collect(Collectors.toUnmodifiableList());`
- [x] `employees.stream().map(Employee::getName).collect(Collectors.toList());`
- [ ] `employees.stream().collect((e) -> e.getName());`
