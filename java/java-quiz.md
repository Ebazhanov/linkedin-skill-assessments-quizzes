## Java Assessment

#### Q1. Given the string "strawberries" saved in a variable called fruit, what would "fruit.substring(2, 5)" return?

- [ ] rawb
- [X] raw 
- [ ] awb
- [ ] traw

Reasoning: The substring method is accepting two arugments. The first argument being the index to start(includes that char at 2) and the second the index of the string to end the substring(excludes the char at 5). Strings in Java are like arrays of chars. Therefore the method will return "raw" as those are the chars in indexs 2,3, and 4. You can also take the ending index and subtract the beginning index from it, to determine how many chars will be included in the substring (5-2=3).

#### Q2. How can you achieve runtime polymorphism in Java?

- [ ] method overloading
- [ ] method overrunning
- [X] method overriding
- [ ] method calling

#### Q3. Given the following definitions, which of these expression will NOT evaluate to true?

```
boolean b1 = true, b2 = false; int i1 = 1, i2 = 2;
```

- [ ] (i1 | i2) == 3
- [X] i2 && b1 
- [ ] b1 || !b2
- [ ] (i1 ^ i2) < 4

#### Q4. What can you use to create new instances in Java?

- [X] constructor
- [ ] another instance
- [ ] field
- [ ] private method

#### Q5. What is the output of this code?

```shell script
1: class Main {
2:   public static void main (String[] args) {
3:     int array[] = {1, 2, 3, 4};
4:     for (int i = 0; i < array.size(); i++) {
5:        System.out.print(array[i]);
       }
     }
   }
```

- [X] It will not compile because of line 4.
- [ ] It will not compile because of line 3.
- [ ] 123
- [ ] 1234

#### Q6. Which of the following can replace the CODE SNIPPET to make the code below print "Hello World"?

```
}
interface Interface2 {
    static void print() {
        System.out.print("World!");
    }
}
```

- [ ] super1.print(); super2.print();
- [ ] this.print();
- [ ] super.print();
- [ ] Interface1.print(); Interface2.print();

#### Q7. What does the following code print?

```
String str = ""abcde"";
str.trim();
str.toUpperCase();
str.substring(3, 4);
System.out.println(str);
```

- [ ] CD
- [ ] CDE
- [ ] D
- [X] "abcde"

#### Q8. What is the result of this code?

```
1: class Main {
2:   public static void main (String[] args){
3:     System.out.println(print(1));
4:   }
5:   static Exception print(int i){
6:       if (i>0) {
7:          return new Exception();
8:       } else {
9:          throw new RuntimeException();
10:      }
11:  }
12: }
```

- [ ] It will show a stack trace with a runtime exception.
- [X] "java.lang.Exception"
- [ ] It will run and throw an exception.
- [ ] It will not compile.

#### Q9. Which class can compile given these declarations?

```
1: interface One {
2:      default void method() {
3:          System.out.println(""One"");
4:      }   }
5: interface Two {
6:      default void method () {
7:          System.out.println(""One"");
8:      }   }
```

- [ ] 

```
  class Three implements One, Two {
    publc void method() {
        super.One.method();
  } }
```

- [ ] 

```
  class Three implements One, Two {
    publc void method() {
        One.method();
  } }
```

- [ ] 

```
class Three implements One, Two {
}
```

- [X] 

```
  class Three implements One, Two {
    publc void method() {
        One.super.method();
  } }
```

#### Q10. What is the output of this code?

```
1: class Main {
2:  public static void main (String[] args) {
3:      List list = new ArrayList();
4:      list.add("hello");
5:      list.add(2);
6:      System.out.print(list.get(0) instanceof Object);
7:      System.out.print(list.get(1) instanceof Integer);
8:  }
9: }
```

- [ ] The code does not compile.
- [ ] truefalse
- [X] truetrue
- [ ] falsetrue

#### Q11. Given the following two classes, what will be the output of the Main class?

```
package mypackage;
public class Math {
    public static int abs(int num){
        return num<0?-num:num;
    }
}
package mypackage.elementary;
public class Math {
    public static int abs (int num) {
        return -num;
    }
}
1: import mypackage.Math;
2: import mypackage.elementary.*;

3: class Main {
4:  public static void main (String args[]){
5:      System.out.println(Math.abs(123));
6:  }
7: }
```

- [ ] Lines 1 and 2 generate compiler erros due to class name conflicts.
- [ ] "-123"
- [ ] It will throw an exception on line 5.
- [X] "123"  
// The answer is "123". The abs() method evaluates to the one inside mypackage.Math class.

#### Q12. What is the result of this code?

```
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

- [X] It will not compile because of line 10.
- [ ] "Hello!"
- [ ] It will not compile because of line 2.
- [ ] "World!"

#### Q13. Given this code, which command will output "2"?

```
class Main {
    public static void main(String[] args) {
        System.out.println(args[2]);
    }
}
```

- [ ] java Main 1 2 "3 4" 5
- [X] java Main 1 "2" "2" 5
- [ ] java Main.class 1 "2" 2 5
- [ ] java Main 1 "2" "3 4" 5

#### Q14. What is the output of this code?

```
class Main {
    public static void main(String[] args){
        int a = 123451234512345;
        System.out.println(a);
    }
}
```

- [ ] "123451234512345"
- [X] Nothing - this will not compile.
- [ ] a negative integer value
- [ ] "12345100000"

Reasoning: The int type in Java can be used to represent any whole number from -2147483648 to 2147483647. Therefore this code will not compile as the number assigned to 'a' is larger than the int type can hold.

#### Q15. What is the output of this code?

```
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
- [X] A runtime exception is thrown 
- [ ] "world!!world"
- [ ] "world!world!"

```
String m = "Hello world!";
String n = m.substring(6,12) + m.substring(12,6);
System.out.println(n);
```

#### Q16. How do you write a foreach loop that will iterate over ArrayList\<Pencil\>pencilCase?

- [X] for (Pencil pencil : pencilCase) {} 
- [ ] for (pencilCase.next()) {}
- [ ] for (Pencil pencil : pencilCase.iterator()) {}
- [ ] for (pencil in pencilCase) {}

#### Q17. Fill in the blanks?

- Object-oriented programming (OOP) is a programming language model that organizes software design around (objects), rather than (actions).

#### Q18. What code would you use to tell if "schwifty" is of type String?

- [ ] "schwifty".getType() == String
- [ ] "schwifty".getClass().getsimpleName() == "String"
- [ ] "schwifty".getType().equals("String")
- [X] "schwifty" instanceof String

#### Q19. Correct output of `"apple".compareTo("banana")`

- [ ] 0
- [ ] positive number
- [X] negative number
- [ ] compilation error

#### Q20. You have an ArrayList of names that you want to sort alphabetically. Which approach would NOT work?

- [ ] names.sort(Comparator.comparing(String::toString))
- [ ] Collections.sort(names)
- [X] names.sort(List.DESCENDING) <<<--- Correct
- [ ] names.stream().sorted((s1, s2) -> s1.compareTo(s2)).collect(Collectors.toList())

#### Q21. By implementing encapsulation, you cannot directly access the class's **\_** properties unless you are writing code inside the class itself.

- [X] private
- [ ] protected
- [ ] no-modifier
- [ ] public

#### Q22. Which is the most up-to-date way to instantiate the current date?

- [ ] new SimpleDateFormat("yyyy-MM-dd").format(new Date())
- [ ] new Date(System.currentTimeMillis())
- [ ] LocalDate.now()
- [X] Calender.getInstance().getTime() 

#### Q23. Fill in the blank to create a piece of code that will tell wether int0 is divisible by 5:

```
boolean isDivisibleBy5 = _____
```

- [ ] int0 / 5 ? true: false
- [X] int0 % 5 == 0 
- [ ] int0 % 5 != 5
- [ ] Math.isDivisible(int0, 5)

#### Q24. How many time will this code print "Hello World!"?

```
Class Main {
    public static void main(String[] args){
        for (int i=0; i<10; i=i++){
            i+=1;
            System.out.println("Hello World!");
        }
    }
}
```

- [X] 10 times 
- [ ] 9 times
- [ ] 5 times
- [ ] infinite number of times

Reason : Observe the loop increment. It's not an increment, it's an assignment(post).

#### Q25. The runtime system starts your program by calling which function first?

- [ ] print
- [ ] iterative
- [ ] hello
- [X] main 

#### Q26. What is the result of this code?

```
try{
    System.out.print("Hello World");
}catch(Exception e){
    System.out.println("e");
}catch(ArithmeticException e){
    System.out.println("e");
}finally{
    System.out.println("!")
}
```

- [ ] It will throw a runtime exception
- [X] It will not compile
- [ ] Hello World!
- [ ] Hello World

#### Q27. Which statement is NOT true?

- An anonymous class may specify an abstract base class as its base type.
- An anonymous class does not require a zero-argument constructor. <<<<---Correct
- An anonymous class may specify an interface as its base type.
- An anonymous class may specify both an abstract class and interface as base types

#### Q28. What will this program print out to the console when executed?

```
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

- [X] [5, 1, 10] 
- [ ] [10, 5, 1]
- [ ] [1, 5, 10]
- [ ] [10, 1, 5]

#### Q29. What is the output of this code?

```
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
- [X] A untime exception is thrown.
- [ ] The code does not compile.
- [ ] "ello"

#### Q30. Object-oriented programming is a style of programming where you organize your program around \_**\_ rather than \_\_** and data rather than logic.

- [ ] functions; actions
- [X] objects; actions
- [ ] actions; functions
- [ ] actions; objects

#### Q31. What statement returns true if "nifty" is of type String?

- [ ] "nifty".getType().equals("String")
- [ ] "nifty".getType() == String
- [ ] "nifty".getClass().getSimpleName() == "String"
- [X] "nifty" instanceof String

#### Q32. What is the output of this code?

```
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
- [X] 3true 

#### Q33. What is the result of this code?

```
1: class Main {
2: 		Object message(){
3: 			return "Hello!";
4: 		}
5: 		public static void main(String[] args) {
6: 			System.out.print(new Main().message());
7: 			System.out.print(new Main2().message());
8: 		}
9: }
10: class Main2 extends Main {
11: 	String message(){
12: 		return "World!";
13: 	}
14: }
```

- [ ] It will not compile because of line 7.
- [ ] Hello!Hello!
- [X] Hello!World!
- [ ] It will not compile because of line 11.

#### Q34. What method can be used to create a new instance of an object?

- [ ] another instance
- [ ] field
- [X] constructor 
- [ ] private method

#### Q35. Which is the most reliable expression for testing whether the values of two string variables are the same?

- [ ] string1 == string2
- [ ] string1 = string2
- [ ] string1.matches(string2)
- [X] string1.equals(string2)

#### Q36. Which letters will print when this code is run?

```
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
- [X] A and D

#### Q37. What is the output of this code?

```
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
- [X] It will print "Hello World!" three times.
- [ ] It will run forever.

#### Q38. What is the output of this code?

```
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
- [X] [0, 10, 2, abc] 

#### Q39. What is the output of this code?

```
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
- [X] HelloHelloWorld! 
- [ ] Hello Hello World!
- [ ] Hello HelloWorld!

#### Q40. What is displayed when this code is compiled and executed?

```
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
- [X] 10 
- [ ] 5

#### Q41. Which approach cannot be used to iterate over a List named _theList_?

- [ ]
 ```
  for (int i = 0; i < theList.size(); i++) {
      System.out.println(theList.get(i));
  }
  ```
  - [ ] 
```
  for (Object object : theList) {
      System.out.println(object);
  }
  ```
  - [ ]
 ```
  Iterator it = theList.iterator();
  for (it.hasNext()) {
      System.out.println(it.next());
  }
  ```
  - [X]
```
  theList.forEach(System.out::println);
  ```

#### Q42. What method signature will work with this code?

```
boolean healthyOrNot = isHealthy("avocado");
```

- [ ] public void isHealthy(String avocado)
- [X] boolean isHealthy(String string)
- [ ] public isHealthy("avocado")
- [ ] private String isHealthy(String food)

#### Q43. Which are valid keywords in a Java module descriptor (module-infoJava)?

- [ ] provides, employs
- [ ] imports, exports
- [ ] consumes, supplies
- [X] requires, exports

#### Q44. Which type of variable keeps a constant value once it is assigned?

- [ ] non-static
- [ ] static
- [X] final
- [ ] private

#### Q45. How does the keyword _volatile_ affect how a variable is handled?

- [ ] It will be read by only one thread at a time.
- [ ] It will be stored on the hard drive.
- [X] It will never be cached by the CPU. 
- [ ] It will be preferentially garbage collected.

#### Q46. What is the result of this code?

```
char smooch = 'x';
System.out.println((int) smooch);
```

- [ ] an alphanumeric character
- [ ] a negative number
- [X] a positive number 
- [ ] a ClassCastException

#### Q47. You get a NullPointerException. What is the most likely cause?

- [ ] A file that needs to be opened cannot be found.
- [ ] A network connection has been lost in the middle of communications.
- [ ] Your code has used up all available memory.
- [X] The object you are using has not been instantiated.

#### Q48. How would you fix this code so that it compiles?

```
public class Nosey {
	int age;
	public static void main(String[] args) {
		System.out.println("Your age is: " + age);
	}
}
```

- [X] Make age static.
- [ ] Make age global.
- [ ] Make age public.
- [ ] Initialize age to a number.

#### Q49. Add a Duck called "Waddles" to the ArrayList _ducks_.

```
public class Duck {
	private String name;
	Duck(String name) {}
}
```

- [ ] Duck waddles = new Duck();
  ducks.add(waddles);
- [ ] Duck duck = new Duck("waddles");
  ducks.add(wadd1es);
- [X] ducks.add(new Duck("waddles")); 
- [ ] ducks.add(new Waddles());

#### Q50. If you encounter `UnsupportedClassVersionError` it means the code was **\_** on a newer version of Java than the JRE **\_** it.

- [ ] executed; interpreting
- [ ] executed; compiling
- [X] compiled; executing
- [ ] compiled, translating

#### Q51. Given this class, how would you make the code compile?

```java
public class TheClass {
	private final int x;
}
```
- [ ]
 ```java
  public TheClass() {
  	x += 77;
  }
  ```
- [ ]
 ```java
  public TheClass() {
  	x = null;
  }
  ```
- [ ]
 ```java
  public TheClass() {
  	x = 77;
  }
  ```
- [X]
```java
  private void setX(int x) {
  	this.x = x;
  }
  public TheClass() {
  	setX(77);
  }
  ```

#### Q52. How many times f will be printed?

```
public class Solution {
	public static void main(String[] args) {
		for (int i = 44; i > 40; i--) {
			System.out.println("f");
		}
	}
}
```

- [X] 4 
- [ ] 3
- [ ] 5
- [ ] A Runtime exception will be thrown

#### Q53. Which statements about `abstract` classes are true?

1. They can be instantiated.
2. They allow member variables and methods to be inherited by subclasses.
3. They can contain constructors.

- [ ] 1, 2, and 3
- [ ] only 3
- [X] 2 and 3
- [ ] only 2

#### Q54. Which keyword lets you call the constructor of a parent class?

- [ ] parent
- [X] super
- [ ] this
- [ ] new

#### Q55. What is the result of this code?

```java
  1: int a = 1;
  2: int b = 0;
  3: int c = a/b;
  4: System.out.println(c);
```

- [X] It will throw an ArithmeticException.
- [ ] It will run and output 0.
- [ ] It will not compile because of line 3.
- [ ] It will run and output infinity.

#### Q56. Normally, to access a static member of a class such as Math.PI, you would need to specify the class "Math". What would be the best way to allow you to use simply "PI" in your code?

- [X] Add a static import.
- [ ] Declare local copies of the constant in your code.
- [ ] This cannot be done. You must always qualify references to static members with the class form which they came from.
- [ ] Put the static members in an interface and inherit from that interface.
