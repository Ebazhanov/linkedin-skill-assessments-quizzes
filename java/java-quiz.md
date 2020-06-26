Java Assessment
---------------------

#### Q1. Given the string "strawberries" saved in a variable called fruit, what would "fruit.substring(2, 5)" return?
- rawb
- raw <<<<---Correct
- awb
- traw

#### Q2. How can you achieve runtime polymorphism in Java?
- method overloading 
- method overrunning 
- method overriding <<<<--- Correct
- method calling 

#### Q3. Given the following definitions, which of these expression will NOT evaluate to true?
`boolean b1 = true, b2 = false;
int i1 = 1, i2 = 2;`

- (i1 | i2) == 3
- i2 && b1 <<<<---Correct
- b1 || !b2
- (i1 ^ i2) < 4

#### Q4. What can you use to create new instances in Java?
- constructor <<<<---Correct
- another instance
- field
- private method

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
- It will not compile because of line 4. <<<<---Correct
- It will not compile because of line 3.
- 123
- 1234

#### Q6. Which of the following can replace the CODE SNIPPET to make the code below print "Hello World"?
```
}
interface Interface2 {
    static void print() {
        System.out.print("World!");
    }
}
```
- super1.print(); super2.print();
- this.print();
- super.print();
- Interface1.print(); Interface2.print();

#### Q7. What does the following code print?
```
String str = ""abcde"";
str.trim();
str.toUpperCase();
str.substring(3, 4);
System.out.println(str);
```
- CD
- CDE
- D
- "abcde" <<<<---Correct

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
- It will show a stack trace with a runtime exception.
- "java.lang.Exception" <<<<---Correct
- It will run and throw an exception.
- It will not compile. <--- Correct

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
- 
```
  class Three implements One, Two {
    publc void method() {
        super.One.method();
  } }
```
- 
```
  class Three implements One, Two {
    publc void method() {
        One.method();
  } }
```
- 
```
class Three implements One, Two {
}
```
- 
```
  class Three implements One, Two { <------ correct
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
- The code does not compile.
- truefalse
- truetrue <<<<---Correct
- falsetrue

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
- Lines 1 and 2 generate compiler erros due to class name conflicts.
- "-123" <--- Correct
- It will throw an exception on line 5.
- "123"

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
- It will not compile because of line 10. <--- Correct
- "Hello!"
- It will not compile because of line 2.
- "World!"

#### Q13. Given this code, which command will output "2"?
```
class Main {
    public static void main(String[] args) {
        System.out.println(args[2]);
    }
}
```
- java Main 1 2 "3 4" 5
- java Main 1 "2" "2" 5 <--- Correct
- java Main.class 1 "2" 2 5
- java Main 1 "2" "3 4" 5

#### Q14. What is the output of this code?
```
class Main {
    public static void main(String[] args){
        int a = 123451234512345;
        System.out.println(a);
    }
}
```
- "123451234512345"
- Nothing - this will not compile. <<<<---Correct
- a negative integer value
- "12345100000"

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
- The code does not compile.
- A runtime exception is thrown <<<<---Correct
- "world!!world"
- "world!world!"

```
String m = "Hello world!";
String n = m.substring(6,12) + m.substring(12,6);
System.out.println(n);
```

#### Q17. How do you write a foreach loop that will iterate over ArrayList\<Pencil\>pencilCase?
```
for(Pencil pencil = pencilCase){}
Iterator iterator = pencilCase.iterator();
for(){iterator.hasNext()}{}
```

#### Q18. Fill in the blanks?
- Object-oriented programming (OOP) is a programming language model that organizes software design around (objects), rather than (actions).

#### Q19. What code would you use to tell if "schwifty" is of type String?
- "schwifty".getType() == String
- "schwifty".getClass().getsimpleName() == "String"
- "schwifty".getType().equals("String")
- "schwifty" instanceof String <<<<---Correct

#### Q20. Correct output of `"apple".compareTo("banana")`
- 0
- positive number
- negitive number <<<<---Correct
- compilation error
