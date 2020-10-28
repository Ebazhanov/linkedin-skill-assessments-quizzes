# Java

Q1 How can you test if a double value d is not a number?

- [] By evaluating Double.NaN.equals(d)
- [] By evaluating Double.NaN.compareTo(d)
- [] By evaluating d == Double.NaN

- [x] By evaluating Double. isNaN(d)

Q2 Which statement declares an integer field that is shared by all the instances of
the Holder class?

- [] public class Holder {
private int index;
}

- [x] public class Holder {
private static int index;
}

- [] public class Holder {
private final int index;
}
- [] public class Holder {
final int index;
}

Q3 You have an application developed by two teams. The first team uses Windows development machines and the second one MacOS development machines. They both deliver a module of your application, the source code and the compiled code in JARs. How can you run this application on your Linux server?

- [] Since MacOS is based on Linux, just recompile the source code compiled on Windows machines, then package it and deploy and run it on your Linux server.

- [] Recompile all the source code on a Linux machine, then package it and deploy and run it on your Linux server.

- [] Recompile all the source code on any machine, using cross-compilation, then package it and deploy and run it on your Linux server.

- [x] Package the JARs, deploy them and run them without having to recompile anything

Q4 What is the difference between an instance of the String class and array of
chars?

- [x] An instance of String is a reference on an object that wraps an array of chars or bytes, depending on the version of Java

- [] An instance of String is a just wrapper on an array of chars or bytes, depending on the version of Java.

- [] An instance of String is a just reference on a List of chars or bytes, depending on the version of Java.

- [] An instance of String is in fact just a reference on an array of chars or bytes, depending on the version of Java.

Q5 You need to mark that a method is obsolete and should not be used anymore.
What Javadoc tag are you going to use?

- [] @replacedBy

- [] @obsolete

- [] @toBeRemoved
- [] @deprecated

Q6 Which is a legal class declaration given that ClassA and ClassB are classes and
InterfaceA and InterfaceB are interfaces?

- [x] class A extends ClassA, ClassB implements InterfaceA, InterfaceB

- [] class A implements InterfaceA, InterfaceB extends ClassA

- [] class A extends ClassB8 implements InterfaceA, InterfaceB

- [] class A implements InterfaceA extends ClassA

Q7 What Java API is not supported in Android?

- [] Java Thread
- [] Java Swing
- [] Java I/O

- [] Java String

Q8 What happens when you try to add twice the same element to a Set?

- [] The element is not added, but the behavior of the add() method is implementation-dependant

- [] The element is not added and the set may be corrupted.

- [] AN IllegalStateException is thrown and the element is not added.
- [x] The add() returns false and the element is not added

Q9 You have the following class:

public class Holder {
    public Holder(int capacity) { }
}
You need to extend this class with the following class:

public class SmartHolder extends Holder {
    public SmartHolder(int capacity) {
    ..
    }
}

What code do you need to add to the SmartHolder constructor?

- [] super();
- [x] super(capacity);
- [] this(capacity);

- [] this();

Q10 You create a string of characters, trim it, put it in upper case, and extract the
first three characters using the substring method. How many instances of the
string would be created?

- [] 2
- [x] 4
- [] 1
- [] 3
Q11 Which of the following type is NOT valid within a switch statement's test
expression?

- [] int

- [] enum

- [] String

- [x] boolean

Q12 How can you add a method to an existing interface without having to modify
the classes that already implement it?

- [] You make this method an abstract method.

- [] You cannot add a method to an interface without implementing it in the existing implementing classes.

- [] You provide an implementation of this method in a separate static class.

- [x] You make this method a default method.

Q13 i is an int of value 2 and the result variable is declared. What does the following code print out?

switch(i) {

case 1: result = 1;
break;

case 2: result = 2;

case 3: result = 3;

case 4: result = 4;

}

system.out.printIn(“result ="+ result);

- [] result = 2
- [] result = 3
- [x] result = 4
- [] result = 1

Q14 You have a Person class with aname property of type string . You have a
stream of instances of this class and collect this stream with the following
collector: collectors.mapping(Person::getName, joining(", ")) .
What do you get as a result?

- [x] A string with the concatenation of the names of the people, separated by commas
- [] A list of the names of the people

- [] A string with the concatenation of the names of the people if they are not null, separated by commas

- [] A string with the concatenation of the names of the people if they are not empty, separated by commas

Q15 What Javadoc would you write to document the following method?

public static final Connection getConnection(String url) throws SQLTimeoutexception {
}

- [x] /**

-*Attempts to establish a connection to the database.
-*
-*@param url a database URL
-*@return a connection to the URL
-*@throws SQLTimeoutException when the connection is not available.*/

- [] /**

-*Attempts to establish a connection to the database.
-*
-*@param url a database URL*/

- [] /**

-* Attempts to establish a connection to the database.

-* @param url a database URL

-+ @returns a connection to the URL */

- [] /**

-*attempts to establish a connection to the database.

-*@param url a database URL

-*@returns a connection to the URL

-*@throw SQLTimeoutException when the connection is not available.*/

Q16 You need to create a method in a class to be used from within this class and
from all the extending classes. What visibility modifier are you going to use?

- [] default

- [] private
- [x] protected
- [] No visibility modifier

Q17 What implementation of List does the collectors.totist() create?

- [x] ArrayList
- [] LinkedList
- [] BagList

- [] CollectedList

Q18 What command must you use to execute a Main class that contains a main()
method?

- [] $ java Main.main()

- [] $ Main

- [] $ java Main.class
- [x] $ java Main
