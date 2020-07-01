C# Assessment
-------------

#### Q16.	Which choice best defines C#'s asynchronous programming model?
•	callback-based
•	inherited callback
•	task-based    CORRECT
•	Reactive
 
#### Q17.	Why would you use a class field in C#?
•	to store the class definition value
•	to hold information and data contained in the class object   CORRECT
•	to communicate between classes and object
•	to define behaviors inside a class
 
#### Q18.	How could you retrieve information about a class, as well as create an instance at runtime?
•	Serialization
•	Reflection   CORRECT
•	Abstraction
•	dependency injection
 
#### Q19.	What is the correct formatting for single line and multiline comments?
•	// Single Line /* Multiline */   CORRECT
•	// Multiline /* Single Line */
•	//* Multiline / Single Line
•	/*/ - Single Line /* - Multiline
 
#### Q20.	How could you pause a thread for three seconds?
•	Thread.Resume(-3000); 
•	Thread.Sleep(3000);   CORRECT
•	Thread.Suspend(3000); 
•	Thread.Pause(3000); 
 
#### Q21.	What is the correct way to write an event named apiResult based on a delegate named ResultCallback?
•	public event ResultCallback apiResult;   CORRECT
•	public event void ResultCallback;
•	public event ResultCallback(() -> apiResult);
•	public void event ResultCallback apiResult;
 
#### Q22.	What method correctly extends the string class?
•	public static void IsvalidName(this string i, string value) {}
•	public string IsvalidName(this string i, string value) {}
•	public static string IsvalidName(this string i, string value) {}   CORRECT
•	public void IsvalidName(this string i, string value) {}
 
#### Q23.	Which choice best describes a deadlock situation?
•	when you are trying to execute an action after a user event is registered 
•	when simultaneous instructions are waiting on each other to finish before executing   CORRECT
•	when you try to execute a series of events simultaneously on multiple threads 
•	when you try to instantiate two objects at the same time in the same class or struct 
 
 #### Q24.	What function do namespaces perform?
•	Namespaces compile application code together at compile time.
•	Namespaces group code together into a single repository.
•	Namespaces separate code into groupings, control access, and avoid naming collisions.   CORRECT
•	Namespaces calculate code coverage at runtime.
 
 #### Q25.	What is the main difference between a value type and a reference type?
•	A value type stores an actual value, while a reference type is a pointer to a value.  CORRECT
•	A value type can be any primitive type, while reference types must be type-agnostic.
•	A value type refers to another value, while a reference type refers to a value in memory. 
•	A value type is available only at runtime, while a reference type is available only at compile time. 
 
#### Q26.	What is an abstract class? 
•	something denoted by the abstract keyword and used system wide; if you want any program to create an object of a class, you use the abstract class  CORRECT
•	a class that is denoted by the class keyword (can be seen and used by any other class in the system—thus it is, by default, public)
•	a class that can be used only as a base class
•	a class that is denoted by the virtual keyword
 
#### Q27.	What is an object in C#?
•	a value type that can be used only with an abstract class.
•	an instance of a class or struct that includes fields, properties, and/or methods  CORRECT
•	a primitive data type that can be created only at compile time.
•	a class or struct, including its variables and functions
 
#### Q28.	What is a thread pool?
•	a collection of threads created during initialization that can be reused  CORRECT
•	a collection of synchronous methods created during initialization that cannot be reused
•	a collection of threads only recognized at compile time that can be reused
•	a collection of asynchronous methods created at compile time that cannot be reused
 
#### Q29.	What is the main function of an access modifier?
•	to control the accessibility level of types and members  CORRECT
•	to specify a derived classes type
•	to specify a base classes type
•	to modify a type or member value at runtime
 
#### Q30.	What is the difference between a.Equals(b) and a == b?
•	The. Equals method compares primitive values while == compares all values.
•	The. Equals method compares reference types while == compares primitive value types.
•	The. Equals method compares reference identities while the == compares contents.  CORRECT
•	The. Equals method compares contents while == compares reference identity.
 
#### Q31.	When would you use a Dictionary rather than an Array type in your application?
•	when you need to store key-value pairs rather than single values  CORRECT
•	when you need an ordered, searchable list
•	when you need to store values of the same type
•	when you need a jagged collection structure
 
#### Q32.	Which statement is true of delegates?
•	They can be chained together.   CORRECT
•	Only variables can be passed to delegates as parameters.
•	They cannot be used as callbacks.
•	Delegates are not supported in the current version of C#.
 
#### Q33.	What is the difference between the ref and out keywords?
•	Variables passed to out specify that the parameter is an output parameter, while ref specifies that a variable may be passed to a function without being initialized.
•	Variables passed to ref specify that the parameter is an output parameter, while out specifies that a variable may be passed to a function without being initialized.
•	Variables passed to out can be passed to a function without being initialized, while ref specifies that the value is a reference value that can be changed inside the calling method.  CORRECT
•	Variables passed to ref can be passed to a function without being initialized, while out specifies that the value is a reference value that can be changed inside the calling method.
 
#### Q34.	How would you determine if a class has a particular attribute?
•	Attribute.GetCustomAttribute(typeof(ExampleController), typeof(SubControllerActionToViewDataAttribute))  CORRECT
•	var type = typeof(SomeType); var attribute = type.GetCustomAttribute<SomeAttribute>();
•	typeof(MyPresentationModel).Should().BeDecoratedWith<SomeAttribute>();
•	Attribute.GetCustomAttribute, typeof(SubControllerActionToViewDataAttribute)
 
#### Q35.	In which of these situations are interfaces better than abstract classes?
•	When you need a list of capabilities and data that are classes-agnostic, use an interface. When you need a certain object type to share characteristics, use an abstract class.  CORRECT
•	Interfaces are a legacy of older versions of C# and are interchangeable with the newer abstract class feature.
•	You should use both an interface and an abstract class when defining any complex object.
•	When you need to define an object type's characteristics, use an interface. When you need to define an object type's capabilities, use an abstract class.
 
 #### Q36.	What is the most accurate description of a regular expression?
•	A regular expression is a C# tool used to parse HTML.
•	A regular expression is a special text string for describing a search pattern.  CORRECT
•	A regular expression allows a variable to be passed by reference.
•	A regular expression allows a class to conform to the Equatable protocol.
 
#### Q37.	What is the difference between throw exceptions and throw clauses?
•	Throw exceptions overwrite the stack trace, while throw clauses retain the stack information.  CORRECT
•	Throw clauses fire only at runtime, while throw exceptions can fire at any time.
•	Throw clauses overwrite the stack trace, while throw exceptions retain the stack information.
•	Throw exceptions fire only at runtime, while throw clauses can fire during compile time.
 
#### Q38.	Given this enumeration, how would you access the integer-typed value of `AppState.Loading`? 
•	int currentState = (int)AppState.Loading;
•	string currentState = AppState.Loading.integralVal;
•	string currentState = (string)AppState.Loading;
•	int currentState = AppState.Loading.rawValue;  CORRECT
 
#### Q39.	When will the code inside the finally block be executed in a try-catch statement?
•	If there is an error, it won't execute at all.
•	between the try and catch blocks
•	after the try and catch blocks   CORRECT
•	when the finally block overrides the catch block and executes in its place
 
#### Q40.	What is the correct syntax for a new generic list of strings named contacts?
•	public List(string names) contacts = new List(string names); 
•	var contacts = new List(string);
•	var contacts = new List<string>();   CORRECT
•	public List<string names> contacts = new List<string names>(); 
 
#### Q41.	Lambda expressions are often used in tandem with which of the following?
•	Type Aliasing
•	LINQ   CORRECT
•	Namespaces
•	Assemblies
 
#### Q42.	What are C# events?
•	system actions that communicate directly with the compiler at runtime
•	user-only methods that send data to the application's back end
•	actions that execute when the code compiles, generating logs and test output
•	actions that generate notifications, which are sent to their registered listeners  CORRECT
