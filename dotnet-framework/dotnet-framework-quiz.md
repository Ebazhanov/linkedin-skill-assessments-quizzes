## .NET Framework Assessment

#### 1. What is the difference between a stack and queue?

- Queues process value types by a top-down hierarchy - first in, first out (FIFO). Stacks follow this principle and insert items from the lower end while deleting ones from the top - last in, first-out (LIFO).

- Queues process value types by a top-down hierarchy-last in, first-out (LIFO). Stacks follow this principle and insert items from the lower end while deleting ones from the top-first in, first-out (FIFO).

- **Stacks process value types by a top-down hierarchy - last in, first-out (LIFO). Queues follow this principle and insert items from the lower end while deleting ones from the top - first in, first-out (FIFO).** <= Correct

- Stacks process value types by a top-down hierarchy-first in, first out (FIFO). Queues follow this principle and insert items from the lower end while deleting ones from the top-last in, first-out (LIFO).

#### 2. Which group contains all official types of JIT compilations?

- Pre-JIT, Quick-JIT, Coll-JIT

- Before-JIT, Quick-JIT, Cool-JIT

- Pre-JIT, Quick-JIT, Normal-JIT

- **Pre-JIT, Econo-JIT, Normal-JIT** <= Correct

#### 3. What is Kestrel?

- an iOS web server initially that was later designed to work with .NET Core

- **a cross-platform web server ASP.NET Core that is included by default in ASP.NET Core project templates** <= Correct

- a cross-platform, open-source web server that starts up web APIs

- a free and open-source cross-platform web server software that can communicate with IIS

#### 4. When would you use asynchronous actions?

- to release the quest thread of a I/O operation

- to capture the request thread of a I/O operation

- **to avoid blocking the request thread while waits for an I/O operation** <= Correct

- to block the request thread if it waits for an I/O operation

#### 5. What is CoreCLR?

- CoreCLR is a component that allows the highest degree of control when coding; you can Abort(), Suspend() or Resume().

- CoreCLR is the .NET execution engine that runs the source code. Special programs called compilers must rewrite it into MSIL.

- CoreCLR is the .NET execution engine the runs the source code. Special programs called compilers must rewrite it into IL.

- **CoreCLR is the .NET execution engine in .NET Core that performs functions like garbage collection and compilation to machine code.** <= Correct

#### 6. When you define an abstract method, how do you use it in a derived class?

- Abstract methods cannot be used in derived classes.

- In your derived class, overload the method.

- **In your derived class, override the method.** <= Correct

- In your derived class, declare the method as virtual.

#### 7. Which code do you use if you want to trigger a garbage collection in .NET?

- Garbage.CleanUp();

- System.GC.Clear();

- **System.GC.Collect();** <= Correct

- Garbage.Collect();

#### 8.You want to include language elements in a program. Which design pattern best fits this objective?

- Interpreter

- Command

- Bridge

- **Decorator** <= Not sure

#### 9.What makes a strong-named assembly?

- an assembly with the version specified

- **a signed assembly** <= Correct

- an assembly with culture information

- an assembly with the name marked as important

#### 10.What happens when you concatenate two strings?

- You cannot concatenate strings in .NET.

- The second string object is modified so it contains the concatenated strings.

- **A third string object is created containing the concatenated strings.** <= Correct

- The first string object is modified so it contains the concatenated strings.

#### 11.What is a delegate?

- A delegate is an object or collection initializer that adds flexibility, readability and maintainability in C#.

- **A delegate in .NET is similar to a function pointer in C or C++. Using a delegate allows the programmer to encapsulate a reference to a method inside a delegate object.** <= Correct

- A delegate is a collection initializer that adds flexibility, readability and maintainability in .NET.

- A delegate is an extension method. Using a delegate allows the programmer to add flexibility, readability and maintainability in .NET.

#### 12.Which is a set of features that extends the query capabilities of the .NET language syntax by adding sets of new standard query operators that allow data manipulation, regardless of the data source?

- XML

- C#

- **LINQ** <= Correct

- XAML

#### 13.What is the single responsibility principle?

- Software entities should be open for extension, but closed for modification.

- Entities must depend on abstractions, not on concrete implementations.

- Objects in a program should be repleaceble with instances of their subtypes without altering the correctness of that programm.

- **A class should have only a single responsibility - that is, only changes to one part of the software's specification should be able to affect the specification of the class.** <= Correct

#### 14.When should a developer use the .NET Standard class library project type?

- when you want to increase the .NET API surface area your library can access, and allow only .NET Core apps to be compatible with your library

- **when you want to increase the number of apps that are compatible with your library, and decrease the .NET API surface area your library can access** <= Correct

- when you want to decrease speed but have more features

- when you want to increase compilation speed and have fewer features

#### 15.What is the difference between a SDK (software development kit) and runtime in .NET Core?

- The SDK is the "virtual machine" that hosts and runs the application and abstracts all the interaction with the operating system; the runtime usually includes documentation and other help files.

- The runtime is the virtual machine that hosts and runs the application and abstracts all the interaction with the operating system; the SDK usually includes documentation and other help files.

- The runtime compiles code along with the CLR; the SDK usually includes documentation and other help files.

- The SDK compiles code along with the CLR; the runtime usually includes documentation and other help files.

### 16. What is the Common Type System (CTS)?

- the component of CLR in which .NET Framework provides support for several languages since it contains a type system that is common with all the languages

- the component of CLI in which .NET Framework provides support for several languages since it contains a type system that is common with all the languages

- the component of CLR that allows you to map the content of a file to the logical address of an application

- the component of CLR that enables you to run multiple versions of an application or component and CLR on the same computer at the same time

### 17.Assuming y is a value type, which is an example of boxing?

- y = (int)thisObject;
- int y = 3;
- y = (int)thisObject=;3;

- **object thisObject = y; ** <= Correct

### 18.What is an abstract class in .NET?

- An abstract class provides a partial implementation for functionality and some abstract or virtual members that must be implemented by the inheriting entities. It can declare fields too.

- An abstract class allows developers to create new classes that reuse, extend, and modify the behavior defined in other classes.

- An abstract class is responsible for keeping track of what is actually executing and where each executing thread is.

- **An abstract class declares a contract or behavior that implementing classes require. It may declare only properties, methods, and events with no access modifiers. All the declared members must be implemented. ** <= Correct

### 19.What is the namespace for caching information in .NET?

- System.Data.Caching;

- All.System.Caching;

- **System.Runtime.Caching;** <-----CORRECT

- System.Compiler.Caching;

### 20.What is an interface in .NET?

- An interface provides a partial implementation for functionality and some abstract or virtual members that must be implemented by the inheriting entities. It can declare fields too.

- An interface is responsible for keeping track of what is actually executing and where each executing thread is.

- An interface allows developers to create new classes that reuse, extend, and modify the behavior defined in other classes.

- **An interface declares a contract or behavior that implementing classes require. It may declare only properties, methods, and events with no access modifiers. All the declared members must be implemented. ** <= Correct

### 21. What does CAS stand for and what does it do?

- CAS stands for Code Application Secrets and it enables users to restrict, on a very granular level, what hidden code can do according to a level of trust for an application.
- CAS stands for Code Access Secrets and it enables users to restrict, on a very granular level, what hidden code can do according to a level of trust.
- CAS stands for Cognitive Access Security and it enables users to restrict security logic manipulation.
- CAS stands for Code Access Security and it enables users to restrict, on a very granular level, what managed code can do according to a level of trust.

### 22. Which is NOT true about lambda statements?

- A statement lambda cannot return a value. <= Correct
- If a statement lambda has a return value, it has to use a return statement.
- A statement lambda requires using curly braces.
- A statement lambda can have more than one statement.

### 23. Which is NOT true about a read-only variable?

- At runtime, its value is evaluated.
- It can be either static or an instance member.
- It can be initialized at declaration only. <= Correct
- It can be initialized in either the constructor or the declaration.

### 24. What is the difference between System.String and string?

- string is used for fied-size strings in C#, while System.String is used for all the strings.
- There is no such class as System.String.
- **There is none—string is an alias for System. String. ** <---CORRECT
- System.String is a VB.NET data type, while string is a C# type.

### 25. When break is used inside two nested for loops, does control come out of the inner for loop or the outer for loop?

- It breaks from only the outer loop.
- It breaks from all loops.
- **It breaks from only the inner loop.** <= Correct
- It breaks from the outer loop after the second iteration.

### 26. You want to separate object construction from its representation. Which design pattern best fits this objective?

- Adapter
- Bridge
- Singleton
- **Builder ** <= Correct

### 27. You want to encapsulate a command request as an object. Which design pattern best fits this objective?

- Command <= Correct
- Iterator
- Facade
- Observer

### 28. Why would Pre-JIT be used by the .NET Framework?

- to compile only the methods that are called at runtime and store those methods in cache after execution
- to compile complete source code into native code in a single compilation cycle during deployment of the application <= Correct
- to compile only the methods that are called at runtime and then store them in cache for one minute
- to compile only the methods that are called at runtime and remove them from memory after execution

### 29. What do code contracts do?

- Code contracts are data structures that can operate on demand per requirements.
- Code contracts provide a way to specify preconditions, postconditions, and object invariants in your code. <= Correct
- Code contracts contain definitions for a group of related functionalities that a class or a struct can implement.
- Code contracts contain data structures for a group of related functionalities that a class or a struct can implement.

### 30. You must connect an app to an online identity provider using OAuth. For authentication, the app uses WebAuthenticationBroker object. You need to make sure the app registers with the provider. Which actions do you take?

- Construct an HTTP request URI and an HTTPS request URI.
- Invoke the GetCurrentApplicationCallbackUri method and construct an HTTPS request URI.
- Invoke the AuthenticateAsync and GetCurrentApplicationCallbackUri methods.
- Invoke the AuthenticateAsync method and construct an HTTPS request URI.

### 31.You want to create a class of which only a single instance can exist. Which design pattern best fits this objective?

- Adapter
- Singleton <= Correct
- Bridge
- Decorator

### 32.What is the dependency inversion principle?

- Objects in a program should be replaceable with instances of their subtypes without altering the correctness of that program.
- A class should have only a single responsibility—that is, only changes to one part of the software's specification should be able to affect the specification of the class.
- Software entities should be open for extension, but closed for modification.
- Entities must depend on abstractions, not on concrete implementations. <= Correct

### 33.What is a namespace?

- a group of generic collections—in a logical hierarchy by function—that enable you to access the core functionality you need in your applications
- a group of methods—in a logical hierarchy by class—that enable you to access the core functionality you need in .NET
- a group of assemblies—in a logical hierarchy by function—that enable you to access the core functionality you need in your applications
- a group of classes, structures, interfaces, enumerations, and delegates—organized in a logical hierarchy by function that enable you to access the core functionality you need in your applications <= Correct

### 34.Which of the following selects an anonymous type?

- **select new { a.Country, a.Region }** <-----CORRECT
- select a
- select a.Country, a.Region
- select { a.Country, a.Region }

### 35.Which is NOT true about a constant variable?

- At compile time, the value is evaluated.
- Only at declaration can it be initialized.
- At runtime, its value is evaluated.
- It cannot be static.

### 36.What is the purpose of CLR?

- CLR performs various operations such as security checks, spell checks, assembly loading, and thread management. It provides a secure execution environment for the internet.
- CLR sets the rules developers must use for the components that are interlanguage compatible. CLR is reusable across all the .NET-compliant languages.
- CLR is a compiler that converts Intermediate Language to a native code.
- CLR performs various operations such as memory management, security checks, assembly loading, and thread management. It also provides a secure execution environment for applications.

### 37.What is CIL?

- Formerly known as MSIL, CIL is a programming language that NET developers use. It represents the lowest possible level for a language that humans can still read.
- CIL is an object-oriented programming language that is a partially compiled code that .NET developers will then compile to native machine code.
- CIL is used to convert a value type to an object type.
- CIL is a compiled code library that Microsoft developed as an open specification. Developers use it for security, versioning, and deployment purposes.
