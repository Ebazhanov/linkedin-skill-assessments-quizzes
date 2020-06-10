C# Assessment
-------------

#### Q1. In which of these situations are interfaces better than abstract classes?
- When you need  to define an object type's characteristics, use an interface. When you need to define an object type's capabilities, use an abstract class.
- Interfaces are a legacy of older versions of C#, and are interchangeable with the newer abstract class feature.
- When you need a list of capabilities and data that are classes-agnostic, use an interface. When you need a certain object type to share characteristics, use an abstract class.
- You should use both an interface and an abstract class when defining any complex object.

#### Q2. Which statement is true of delegates?
- Delegates are not supported in the current version of C#
- They cannot be used as callbacks.
- Only variables can be passed to delegates as parameters.
- They can be chained together.

#### Q3. Which choice best defines C#'s asynchronous programming model?
- reactive
- inherited callback
- task-based
- callback-based

#### Q4. How would you determine if a class has a particular attribute?
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
Attribute.GetCustomAttribute(typeof(ExampleController), typeof(SubControllerActionToViewDataAttribute))
```
#### Q5. What is the difference between the ref and out keywords?
- Variables passed to out specify that the parameter is an output parameter, while ref specifies that a variable may be passed to a function without being initialized.
- Variables passed to ref can be passed to a function without being initialized, while out specifies that the value is a reference value that can be changed inside the calling method.
- Variables passed to out can be passed to a function without being initialized, while ref specifies that the value is a reference value that can be changed inside the calling method.
- Variables passed to ref specify that the parameter is an output parameter, while out specifies that a variable may be passed to a function without being initialized.

#### Q6. How could you retrieve information about a class, as well as create an instance at runtime?
- reflection
- serialization
- abstraction
- dependency injection

#### Q7. What is this code an example of?
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
- a potential deadlock

#### Q8. What is the difference between an anonymous type and a regular data type?
- Anonymous types don't have type names
- Anonymous types can only be static
- Anonymous types can be used only in struts
- Anonymous types don't work with LINQ.

#### Q9. When would you use a Dictionary rather that an Array type in your application?
- when you need a jagged collection structure
- when you need to store values of the same type
- when you need to store key-value pairs rather than single values
- when you need an ordered, searchable list

#### Q10. What is the difference between a.Equals(b) and a == b?
- The .Equals method compares reference identities while the == compares contents.
- The .Equals method compares primitive values while == compares all values.
- The .Equals method compares contents while == compares references reference identity.
- The .Equals method compares reference type while == compares primitive value types.

#### Q11. Which choice best describes a deadlock situation?
- when you try to instantiate two objects at the same time in the same class or struct
- when you are trying to execute an action after a user event is registered
- when simultaneous instructions are waiting on each other to finish before executing
- when you try to execute a series of events simultaneously on multiple threads

#### Q12. How does the async keyword work?
- It allows access to asynchronous methods in the C# API
- It allows thread pooling and synchronous processes in static classes.
- It allows the await keyword to be used in a method
- It allows access to synchronous methods in the C# API

#### Q13. What is an object in C#?
- a class or struct, including its variables and functions
- a primitive data type that can be created only at compile time 
- a value type that can be used only with an abstract class
- an instance of a class or struct that includes fields, properties, and/or methods

#### Q14. Which code snippet declares an anonymous type named usedData?
- var<T> userData = new <T> { name = "John", age = 32 };
- var userData= new { name = "John", age = 32 };
- AType userData = new AType { name = "John", age = 32 };
- Anonymous<T> userData = new Anonymous<T> { name = "John", age = 32 };

#### Q15. What will be returned when this method is executed?
`public void userInput(string charParamters) { }`
- nothing 
- a Boolean
- a string variable
- an integer
