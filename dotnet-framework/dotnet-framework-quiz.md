.NET Framework Assessment
-----------------

#### What is the difference between a stack and queue?
- Queues process value types by a top-down hierarchy - first in, first out (FIFO). Stacks follow this principle and insert items from the lower end while deleting ones from the top - last in, first-out (LIFO).

- Queues process value types by a top-down hierarchy-last in, first-out (LIFO). Stacks follow this principle and insert items from the lower end while deleting ones from the top-first in, first-out (FIFO).

- **Stacks process value types by a top-down hierarchy - last in, first-out (LIFO). Queues follow this principle and insert items from the lower end while deleting ones from the top - first in, first-out (FIFO).** <= Correct

- Stacks process value types by a top-down hierarchy-first in, first out (FIFO). Queues follow this principle and insert items from the lower end while deleting ones from the top-last in, first-out (LIFO).





#### Which group contains all official types of JIT compilations?
- Pre-JIT, Quick-JIT, Coll-JIT

- Before-JIT, Quick-JIT, Cool-JIT

- Pre-JIT, Quick-JIT, Normal-JIT

- **Pre-JIT, Econo-JIT, Normal-JIT** <= Correct





#### What is Kestrel?
- an iOS web server initially that was later designed to work with .NET Core

- **a cross-platform web server ASP.NET Core that is included by default in ASP.NET Core project templates** <= Correct

- a cross-platform, open-source web server that starts up web APIs

- a free and open-source cross-platform web server software that can communicate with IIS





#### When would you use asynchronous actions?
- to release the quest thread of a I/O operation

- to capture the request thread of a I/O operation

- **to avoid blocking the request thread while waits for an I/O operation** <= Correct

- to block the request thread if it waits for an I/O operation





#### What is CoreCLR?
- CoreCLR is a component that allows the highest degree of control when coding; you can Abort(), Suspend() or Resume().

- CoreCLR is the .NET execution engine that runs the source code. Special programs called compilers must rewrite it into MSIL.

- CoreCLR is the .NET execution engine the runs the source code. Special programs called compilers must rewrite it into IL.

- **CoreCLR is the .NET execution engine in .NET Core that performs functions like garbage collection and compilation to machine code.** <= Correct





#### When you define an abstract method, how do you use it in a derived class?
- Abstract methods cannot be used in derived classes.

- In your derived class, overload the method.

- **In your derived class, override the method.** <= Correct

- In your derived class, declare the method as virtual.





#### Which code do you use if you want to trigger a garbage collection in .NET?
- Garbage.CleanUp();

- System.GC.Clear();

- **System.GC.Collect();** <= Correct

- Garbage.Collect();





#### You want to include language elements in a program. Which design pattern best fits this objective?
- Interpreter

- Command

- Bridge 

- **Decorator** <= Not sure





#### What makes a strong-named assembly?

- an assembly with the version specified

- **a signed assembly** <= Correct

- an assembly with culture information

- an assembly with the name marked as important





#### What happens when you concatenate two strings?

- You cannot concatenate strings in .NET.

- The second string object is modified so it contains the concatenated strings.

- A third string object is created containing the concatenated strings.

- **The first string object is modified so it contains the concatenated strings.** <= Correct





#### What is a delegate?

- A delegate is an object or collection initializer that adds flexibility, readability and maintainability in C#.

- A delegate in .NET is similar to a function pointer in C or C++. Using a delegate allows the programmer to encapsulate a reference to a method inside a delegate object. <= Correct

- A delegate is a collection initializer that adds flexibility, readability and maintainability in .NET.

- **A delegate is an extension method. Using a delegate allows the programmer to add flexibility, readability and maintainability in .NET.** <= Correct





#### Which is a set of features that extends the query capabilities of the .NET language syntax by adding sets of new standard query operators that allow data manipulation, regardless of the data source?

- XML

- C#

- **LINQ** <= Correct

- XAML





#### What is the single responsibility principle?

- Software entities should be open for extension, but closed for modification.

- Entities must depend on abstractions, not on concrete implementations.

- Objects in a program should be repleaceble with instances of their subtypes without altering the correctness of that programm.

- **A class should have only a single responsibility - that is, only changes to one part of the software's specification should be able to affect the specification of the class.** <= Correct





#### When should a developer use the .NET Standard class library project type?

- when you want to increase the .NET API surface area your library can access, and allow only .NET Core apps to be compatible with your library

- **when you want to increase the number of apps that are compatible with your library, and decrease the .NET API surface area your library can access** <= Correct

- when you want to decrease speed but have more features

- when you want to increase compilation speed and have fewer features


#### What is the difference between a SDK (software development kit) and runtime in .NET Core? 

- The SDK is the "virtual machine" that hosts and runs the application and abstracts all the interaction with the operating system; the runtime usually includes documentation and other help files. 

- The runtime is the virtual machine that hosts and runs the application and abstracts all the interaction with the operating system; the SDK usually includes documentation and other help files. 

- The runtime compiles code along with the CLR; the SDK usually includes documentation and other help files. 

- The SDK compiles code along with the CLR; the runtime usually includes documentation and other help files. 

### What is the Common Type System (CTS)? 

- the component of CLR in which .NET Framework provides support for several languages since it contains a type system  that is common with all the languages 

- the component of CLI in which .NET Framework provides support for several languages since it contains a type system that  is common with all the languages 

 - the component of CLR that allows you to map the content of a file to the logical address of an application 

 - the component of CLR that enables you to run multiple versions of an application or component and CLR on the same computer at the same time 
 
 
 ### Assuming y is a value type, which is an example of boxing?

 - y = (int)thisObject;
 - int y = 3; 
 - y = (int)thisObject=;3; 

 - object thisObject = y; 

### What is an abstract class in .NET? 

- An abstract class provides a partial implementation for functionality and some abstract or virtual members that must be 0implemented by the inheriting entities. It can declare fields too. 

- An abstract class allows developers to create new classes that reuse, extend, and modify the behavior defined in other  classes. 

- An abstract class is responsible for keeping track of what is actually executing and where each executing thread is. 

- An abstract class declares a contract or behavior that implementing classes require. It may declare only properties,  methods, and events with no access modifiers. All the declared members must be implemented. 



### What is the namespace for caching information in .NET? 

- System.Data.Caching; 

 - All.System.Caching; 

 - System.Runtime.Caching; <-----CORRECT

 - System.Compiler.Caching; 
 
 
 
 ### What is an interface in .NET? 
- An interface provides a partial implementation for functionality and some abstract or virtual members that must be  implemented by the inheriting entities. It can declare fields too. 

- An interface is responsible for keeping track of what is actually executing and where each executing thread is. 

 - An interface allows developers to create new classes that reuse, extend, and modify the behavior defined in other classes. 

 - An interface declares a contract or behavior that implementing classes require. It may declare only properties, methods, and events with no access modifiers. All the declared members must be implemented. 




