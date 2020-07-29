C# Assessment
-------------

#### In which of these situations are interfaces better than abstract classes?
- When you need  to define an object type's characteristics, use an interface. When you need to define an object type's capabilities, use an abstract class.
- Interfaces are a legacy of older versions of C#, and are interchangeable with the newer abstract class feature.
- **When you need a list of capabilities and data that are classes-agnostic, use an interface. When you need a certain object type to share characteristics, use an abstract class.** <= Not sure
- You should use both an interface and an abstract class when defining any complex object.

#### Which statement is true of delegates?
- Delegates are not supported in the current version of C#
- They cannot be used as callbacks.
- Only variables can be passed to delegates as parameters.
- **They can be chained together.** <= Correct

#### Which choice best defines C#'s asynchronous programming model?
- reactive
- inherited callback
- **task-based** <= Correct
- callback-based

#### How would you determine if a class has a particular attribute?
- 
```
var type = typeof(SomeType); 
var attribute = type.GetCustomAttribute<SomeAttribute>();
```
- 
```
var typeof(MyPresentationModel).Should().BeDecoratedWith<SomeAttribute>();
```
- 
```
Attribute.GetCustomAttribute, typeof(SubControllerActionToViewDataAttribute)
```
-
```
**Attribute.GetCustomAttribute(typeof(ExampleController), typeof(SubControllerActionToViewDataAttribute))** <= Correct
```
#### What is the difference between the ref and out keywords?
- Variables passed to out specify that the parameter is an output parameter, while ref specifies that a variable may be passed to a function without being initialized.
- Variables passed to ref can be passed to a function without being initialized, while out specifies that the value is a reference value that can be changed inside the calling method.
- **Variables passed to out can be passed to a function without being initialized, while ref specifies that the value is a reference value that can be changed inside the calling method.** <= Correct
- Variables passed to ref specify that the parameter is an output parameter, while out specifies that a variable may be passed to a function without being initialized.

#### How could you retrieve information about a class, as well as create an instance at runtime?
- **reflection** <= Correct
- serialization
- abstraction
- dependency injection

#### What is this code an example of?
```
private static object objA;
    private static object objB;

    private static void performTaskA()
    {
        lock (obj)
        {
            Thread.Sleep(1000);
            lock (objA) { }
        }
    }

    private static void PerformTaskB()
    {
        lock (objA)
        {
            lock (objB) { } 
        }
    }
```
- a private class that uses multithreading
- multithread coding
- thread mismanagement
- **a potential deadlock** <= Correct

#### What is the difference between an anonymous type and a regular data type?
- **Anonymous types don't have type names** <= Correct
- Anonymous types can only be static
- Anonymous types can be used only in struts
- Anonymous types don't work with LINQ.

#### When would you use a Dictionary rather that an Array type in your application?
- when you need a jagged collection structure
- when you need to store values of the same type
- **when you need to store key-value pairs rather than single values** <= Correct
- when you need an ordered, searchable list

#### What is the difference between a.Equals(b) and a == b?
- The .Equals method compares reference identities while the == compares contents.
- The .Equals method compares primitive values while == compares all values.
- **The .Equals method compares contents while == compares references reference identity.** <= Not sure
- The .Equals method compares reference type while == compares primitive value types.

#### Which choice best describes a deadlock situation?
- when you try to instantiate two objects at the same time in the same class or struct
- when you are trying to execute an action after a user event is registered
- **when simultaneous instructions are waiting on each other to finish before executing** <= Correct
- when you try to execute a series of events simultaneously on multiple threads

#### How does the async keyword work?
- It allows access to asynchronous methods in the C# API
- It allows thread pooling and synchronous processes in static classes.
- **It allows the await keyword to be used in a method** <= Correct
- It allows access to synchronous methods in the C# API

#### What is an object in C#?
- **a class or struct, including its variables and functions** <= Correct
- a primitive data type that can be created only at compile time 
- a value type that can be used only with an abstract class
- an instance of a class or struct that includes fields, properties, and/or methods

#### Which code snippet declares an anonymous type named usedData?
- var<T> userData = new <T> { name = "John", age = 32 };
- **var userData= new { name = "John", age = 32 };** <= Correct
- AType userData = new AType { name = "John", age = 32 };
- Anonymous<T> userData = new Anonymous<T> { name = "John", age = 32 };

#### What will be returned when this method is executed?
`public void userInput(string charParamters) { }`
- **nothing** <= Correct
- a Boolean
- a string variable
- an integer

#### What is the correct syntaxe for a new generic list of strings named contacts?
- public List<string names> contacts = new List<string names>();
- public List(string names) contacts = new List(string names)();
- **var contacts = new List<string>();** <= Correct
- var contacts = new List(string);

#### What is the difference between throw exceptions and throw clauses?
- Throw clauses fire only at rentime, while throw exceptions can fire at any time.
- **Throw exceptions overwrite the stack trace, while throw clauses retain the stack information.** <= Correct
- Throw clauses overwrite the stack trace, while throw exceptions retain the stack information.
- Throw exceptions fire only at runtime, while throw clauses can fire during compile time.

#### When an asynchronous method is executed, the code runs but nothing happens other than a compiler warning. What is most likely causing the method to not return anything?
- The return yield statement is missing at the end of the method.
- **The method is missing an await keyword in its body.** <= Not sure
- The wait keyword is missing from the end of the method.
- The yield keyword is missing from the method.

#### What are C# events?
- system actions that communicate directly with the compiler at runtime
- actions that execute when the code compiles, generating logs and test output
- **actions that generate notifications, which are sent to their registered listeners** <= Correct
- user-only methods that send data to the application's back end

#### What kind of values can arrays store?
- unordered collections of numerc values
- key-value pairs of any C# supported type
- class and struct instances
- **multiple variables, or collections, of the same type** <= Correct

#### Given this enumeration, how would you access the integer-type value of 'AppState.Loading'?
`enum AppState { OffLine, Loading, Ready }`
- string currentState = (string)AppState.Loading;
- string currentState = AppState.Loading.integralVal;
- int currentState = AppState.Loading.rawValue;
- **int currentState = (int)AppState.Loading;** <= Correct

#### What character would you use to start a regular expression pattern at a word boundary?
- d
- \a
- \b
- **\w** <= Correct

#### To conform to the following interface, which of its members need to be implemented?
```
public interface INameble
{
    string firstName { get; set; }
    string lastName { get; }
}
```
- **Both the firstName and lastName properties need to be implemented.** <= Correct
- Neither, they are both optional.
- Only the LastName property needs to be implemented.
- Only the FirstName property needs to be implemented.

#### You're dealing with multiple assemblies in your program, but are worried about memory allocation. At what point in the program life cycle are assemblies loaded into memory?
- **at runtime** <= Not sure
- at compile time
- only when required
- only when programmatically loaded

#### What is most accurate description of a regular expression?
- A regular expression is a C# tool used to parse HTML
- **A regular expression is a special text string for describint a search patters.** <= Not sure
- A regular expressions allows a variable to be passed by reference.
- A regular expression allows a class to conform to the Equatable protocol.