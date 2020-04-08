Java Assessment
---------------------

#### Q1. Given the string "strawberries" saved in a variable called fruit, what would "fruit.substring(2, 5)" return?
- rawb
- raw
- awb
- traw

#### Q2. How can you achieve runtime polymorphism in Java?
- method overloading 
- method overrunning 
- method overriding 
- method calling 

#### Q3. Given the following definitions, which of these expression will NOT evaluate to true?
`boolean b1 = true, b2 = false;
int i1 = 1, i2 = 2;`

- (i1 | i2) == 3
- i2 & b1
- b1 | !b2
- (i1 ^ i2) < 4

#### Q4. What can you use to create new instances in Java?
- constructor
- another instance
- field
- private method

#### Q5. What is the output of this code?
```shell script
1: class Main {
2:   public static void main (String[] args)
3:     int array[] = {1, 2, 3, 4};
4:     for (int i=0; i<array.size(); i++){
5:      System.out.print(array[i]);
    }
  }
}
```
- It will not compile because of line 4.
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
- "abcde"

#### Q8. What is the result of this code?
```
1: class Main {
2:   public static void main (String[] args){
3:     System.out.printlin(print(1));
4:   }
5:   static Exception print(int i){
6:       if (i>0) {
7:          return new Excepton();      
8:       } else {
9:          throw new RuntimeException();
10:      }
11:  }
12: }
```
- It will show a stack trace with a runtime exception.
- "java.lang.Exception"
- It will run and throw an exception.
- It will not compile.

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
  class Three implements One, Two {
    publc void method() {
        One.super.method();
  } }
```

#### Q10. What is the output of this code?
String m = "Hello world!";
String n = m.substring(6,12) + m.substring(12,6);
System.out.println(n);


#### Q11. What is the output of this code?
How do you write a foreeach loop that will iterate over ArrayList<Pencil>pencilCase?
for(Pencil pencil = pencilCase){}

Iterator iterator = pencilCase.iterator();
for(){iterator.hasNext()}{}

#### Q12. Fill in the blanks?
Object-oriented programming (OOP) is a programming language model that organizes software design around (objects), rather than (functions).
