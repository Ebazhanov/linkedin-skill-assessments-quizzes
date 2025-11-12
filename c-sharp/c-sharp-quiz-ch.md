## C#

#### Q1. 在以下哪种情况下，接口比抽象类更好？

- [ ] 当你需要定义对象类型的特征时，使用接口。当你需要定义对象类型的能力时，使用抽象类。
- [ ] 接口是C#旧版本的遗留物，与较新的抽象类功能可以互换。
- [x] 当你需要一个与类无关的能力和数据列表时，使用接口。当你需要某个对象类型共享特征时，使用抽象类。
- [ ] 在定义任何复杂对象时，你应该同时使用接口和抽象类。

#### Q2. 关于委托，哪个陈述是正确的？

- [ ] 委托在当前版本的C#中不受支持
- [ ] 它们不能用作回调。
- [ ] 只有变量可以作为参数传递给委托。
- [x] 它们可以链接在一起。

[官方文档：委托](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/delegates/#delegates-overview)

#### Q3. 哪个选择最好地定义了C#的异步编程模型？

- [ ] reactive
- [ ] inherited callback
- [x] task-based
- [ ] callback-based

[官方文档：基于任务的异步编程模型](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/async/task-asynchronous-programming-model) resposta correta --> var contacts = new List<string>();

#### Q4. 你如何确定一个类是否有特定的属性？

- [ ] .

```cs
var type = typeof(SomeType);
var attribute = type.GetCustomAttribute<SomeAttribute>();
```

- [ ] .

```cs
var typeof(MyPresentationModel).Should().BeDecoratedWith<SomeAttribute>();
```

- [ ] .

```cs
Attribute.GetCustomAttribute, typeof(SubControllerActionToViewDataAttribute)
```

- [x] .

```cs
Attribute.GetCustomAttribute(typeof(ExampleController), typeof(SubControllerActionToViewDataAttribute))
```

1. [官方文档：Attribute类](https://docs.microsoft.com/en-us/dotnet/api/system.attribute?view=net-5.0)
2. [官方文档：Attribute.GetCustomAttribute方法](https://docs.microsoft.com/en-us/dotnet/api/system.attribute.getcustomattribute?view=net-5.0)

#### Q5. ref和out关键字之间的区别是什么？

- [ ] 传递给out的变量指定参数是输出参数，而ref指定变量可以在不初始化的情况下传递给函数。
- [ ] 传递给ref的变量可以在不初始化的情况下传递给函数，而out指定值是一个引用值，可以在调用方法内部更改。
- [x] 传递给out的变量可以在不初始化的情况下传递给函数，而ref指定值是一个引用值，可以在调用方法内部更改。
- [ ] 传递给ref的变量指定参数是输出参数，而out指定变量可以在不初始化的情况下传递给函数。

1. [官方文档：ref](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/ref)
2. [官方文档：out参数修饰符](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/out-parameter-modifier)

#### Q6. 你如何检索关于类的信息，并在运行时创建实例？

- [x] reflection
- [ ] serialization
- [ ] abstraction
- [ ] dependency injection

[官方文档：反射](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/reflection)

#### Q7. 这段代码是什么例子？

```cs
    private static object objA;
    private static object objB;

    private static void performTaskA()
    {
        lock (objB)
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

- [ ] 使用多线程的私有类
- [ ] 多线程编码
- [ ] 线程管理不当
- [x] 潜在的死锁

[官方文档：死锁和竞争条件](https://docs.microsoft.com/en-us/dotnet/standard/threading/managed-threading-best-practices#deadlocks-and-race-conditions)

#### Q8. 匿名类型和常规数据类型之间的区别是什么？

- [x] 匿名类型没有类型名称
- [ ] 匿名类型只能是静态的
- [ ] 匿名类型只能在结构体中使用
- [ ] 匿名类型不能与LINQ一起使用。

[官方文档：匿名类型](https://docs.microsoft.com/en-us/dotnet/csharp/fundamentals/types/anonymous-types)

#### Q9. 在你的应用程序中，什么时候你会使用Dictionary而不是Array类型？

- [ ] 当你需要一个锯齿状集合结构时
- [ ] 当你需要存储相同类型的值时
- [x] 当你需要存储键值对而不是单个值时
- [ ] 当你需要一个有序的、可搜索的列表时

[官方文档：Dictionary<TKey,TValue>类](https://docs.microsoft.com/en-us/dotnet/api/system.collections.generic.dictionary-2?view=net-5.0)

#### Q10. a.Equals(b)和a == b之间的区别是什么？

- [ ] .Equals方法比较引用身份，而`==`比较内容。
- [ ] .Equals方法比较原始值，而`==`比较所有值。
- [x] .Equals方法比较内容，而`==`比较引用身份。
- [ ] .Equals方法比较引用类型，而`==`比较原始值类型

1. [官方文档：Object.Equals](https://docs.microsoft.com/en-us/dotnet/api/system.object.equals)
2. [c-sharpcorner：相等运算符(==)与.Equals()](https://www.c-sharpcorner.com/UploadFile/3d39b4/difference-between-operator-and-equals-method-in-C-Sharp)

#### Q11. 哪个选择最好地描述了死锁情况？

- [ ] 当你试图在同一类或结构体中同时实例化两个对象时
- [ ] 当你试图在用户事件注册后执行操作时
- [x] 当同时的指令在等待彼此完成执行时
- [ ] 当你试图在多个线程上同时执行一系列事件时

[官方文档：死锁和竞争条件](https://docs.microsoft.com/en-us/dotnet/standard/threading/managed-threading-best-practices#deadlocks-and-race-conditions)

#### Q12. async关键字如何工作？

- [ ] 它允许访问C# API中的异步方法
- [ ] 它允许在静态类中进行线程池和同步过程。
- [x] 它允许在方法中使用await关键字
- [ ] 它允许访问C# API中的同步方法

[官方文档：async](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/async)

#### Q13. C#中的对象是什么？

- [ ] 一个类或结构体，包括其变量和函数
- [ ] 只能在编译时创建的原始数据类型
- [ ] 只能与抽象类一起使用的值类型
- [x] 一个类或结构体的实例，包括字段、属性和/或方法

[官方文档：对象](https://docs.microsoft.com/en-us/dotnet/csharp/fundamentals/object-oriented/objects)

#### Q14. 哪个代码片段声明了一个名为userData的匿名类型？

- [ ] `var<<!---->T> userData = new <<!---->T> { name = "John", age = 32 };`
- [x] `var userData = new { name = "John", age = 32 };`
- [ ] `AType userData = new AType { name = "John", age = 32 };`
- [ ] `Anonymous<T> userData = new Anonymous<T> { name = "John", age = 32 };`

[官方文档：匿名类型](https://docs.microsoft.com/en-us/dotnet/csharp/fundamentals/types/anonymous-types)

#### Q15. 当这个方法被执行时会返回什么？

`public void userInput(string charParameters) { }`

- [x] Nothing
- [ ] a Boolean
- [ ] a string variable
- [ ] an integer

[官方文档：void](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/void)

#### Q16. 在这个例子中，员工姓名会以什么顺序打印到控制台？

```cs
string[] employees = { "Joe", "Bob", "Carol", "Alice", "Will" };

IEnumerable<string> employeeQuery = from person in employees
                                    orderby person
                                    select person;

foreach(string employee in employeeQuery)
{
    Console.WriteLine(employee);
}
```

- [x] ascending
- [ ] unordered
- [ ] descending
- [ ] first in, first out

[dotnetpattern：LINQ OrderBy运算符](http://dotnetpattern.com/linq-orderby-operator)

#### Q17. Lambda表达式经常与以下哪个一起使用？

- [ ] Namespaces
- [x] LINQ
- [ ] Type Aliasing
- [ ] Assemblies

[官方文档：语言集成查询(LINQ)概述](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/linq/)

#### Q18. 单行和多行注释的正确格式是什么？

- [ ] `/_/ - Single Line`
      `/_ - Multiline`
- [ ] `// Multiline`
      `/_ Single Line _/`
- [ ] `//\* Multiline`
      `/ Single Line`
- [x] `// Single Line`
      `/* Multiline */`

[w3schools：C#注释](https://www.w3schools.com/cs/cs_comments.php)

#### Q19. 你如何使抽象类中的方法可重写？

- [ ] 使其公开
- [ ] 使其静态
- [ ] 使其私有
- [x] 使其虚拟

1. [官方文档：virtual](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/virtual)
2. [官方文档：abstract](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/abstract)

#### Q20. 你如何为名为Age的整数属性编写带有getter和setter的代码？

- [ ] public int Age { get - set }
- [ ] public int Age: get set;
- [ ] public int Age (get, set );
- [x] public int Age { get; set; }

[官方文档：使用属性](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/using-properties)

#### Q21. 什么是抽象类？

- [ ] 由class关键字表示的类（可以被系统中的任何其他类看到和使用--因此默认情况下是公共的）
- [ ] 由abstract关键字表示并在系统范围内使用的东西；如果你想让任何程序创建类的对象，你使用抽象类
- [ ] 由virtual关键字表示的类
- [x] 只能用作基类的类

[官方文档：抽象和密封类及类成员](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/abstract-and-sealed-classes-and-class-members)

#### Q22. 使用线程池时，给定线程完成任务后会发生什么？

- [ ] 线程被销毁，内存被释放。
- [ ] 线程循环运行直到下一个任务。
- [ ] 线程在后台变为非活动状态并等待垃圾回收。
- [x] 线程返回到池中以供重用。

[官方文档：线程池特征](https://docs.microsoft.com/en-us/dotnet/standard/threading/the-managed-thread-pool#thread-pool-characteristics)

#### Q23. 哪个选择表示从基类继承行为的类？

- [ ] 第二个基类
- [ ] 修订类
- [x] 派生类
- [ ] 父类

[官方文档：继承](https://docs.microsoft.com/en-us/dotnet/csharp/fundamentals/object-oriented/inheritance)

#### Q24. 运算符重载允许你做什么？

- [ ] 在必要时隐藏内置运算符
- [ ] 添加在运行时由编译器解释的方法
- [ ] 定义枚举和其他原始值类型在应用程序其余部分中的工作方式
- [x] 为加法和相等性等常见运算符定义自定义功能

[官方文档：运算符重载](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/operators/operator-overloading)

#### Q25. LINQ的主要目的是什么？

- [ ] 删除重复数据
- [ ] 绑定命名空间和程序集
- [x] 查询和转换数据
- [ ] 连接程序集

[官方文档：语言集成查询(LINQ)概述](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/linq/#query-expression-overview)

#### Q26. 名为contacts的新字符串泛型列表的正确语法是什么？

- [ ] public List<string names> contacts = new List<string names>();
- [ ] public List(string names) contacts = new List(string names)();
- [x] var contacts = new List<string>();
- [ ] var contacts = new List(string);

[官方文档：List<T>类](https://docs.microsoft.com/en-us/dotnet/api/system.collections.generic.list-1?view=net-5.0)

#### Q27. throw exceptions和throw clauses之间的区别是什么？

- [ ] Throw clauses只在运行时触发，而throw exceptions可以在任何时候触发。
- [x] Throw exceptions覆盖堆栈跟踪，而throw clauses保留堆栈信息。
- [ ] Throw clauses覆盖堆栈跟踪，而throw exceptions保留堆栈信息。
- [ ] Throw exceptions只在运行时触发，而throw clauses可以在编译时触发。

1. [官方文档：throw](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/throw)
2. [c-sharpcorner：Throw Exception和Throw Clause之间的区别](https://www.c-sharpcorner.com/UploadFile/akkiraju/difference-between-throw-exception-and-throw-clause/)

#### Q28. 当异步方法被执行时，代码运行但除了编译器警告外什么都没有发生。最可能导致方法不返回任何内容的原因是什么？

- [ ] 方法末尾缺少return yield语句。
- [x] 方法体缺少await关键字。
- [ ] 方法末尾缺少wait关键字。
- [ ] 方法缺少yield关键字。

[官方文档：并发启动任务](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/async/#start-tasks-concurrently)

#### Q29. C#事件是什么？

- [ ] 在运行时直接与编译器通信的系统操作
- [ ] 在代码编译时执行的操作，生成日志和测试输出
- [x] 生成通知的操作，这些通知发送给它们的注册监听器
- [ ] 仅用户方法，将数据发送到应用程序的后端

[官方文档：事件介绍](https://docs.microsoft.com/en-us/dotnet/csharp/events-overview)

#### Q30. 数组可以存储什么类型的值？

- [ ] 数字值的无序集合
- [ ] 任何C#支持类型的键值对
- [ ] 类和结构体实例
- [x] 相同类型的多个变量或集合

[官方文档：数组](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/arrays/)

#### Q31. 给定这个枚举，你如何访问'AppState.Loading'的整型值？

`enum AppState { OffLine, Loading, Ready }`

- [ ] string currentState = (string)AppState.Loading;
- [ ] string currentState = AppState.Loading.integralVal;
- [ ] int currentState = AppState.Loading.rawValue;
- [x] int currentState = (int)AppState.Loading;

[官方文档：枚举类型](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/enum#conversions)

#### Q32. 你会使用什么字符在单词边界开始正则表达式模式？

- [ ] d
- [ ] \a
- [x] \b
- [ ] \w

1. [regular-expressions：单词边界](https://www.regular-expressions.info/wordboundaries.html)
2. [官方文档：正则表达式语言 - 快速参考](https://docs.microsoft.com/en-us/dotnet/standard/base-types/regular-expression-language-quick-reference)

#### Q33. 要符合以下接口，需要实现其哪些成员？

```cs
public interface INameable
{
    string FirstName { get; set; }
    string LastName { get; }
}
```

- [x] FirstName和LastName属性都需要实现。
- [ ] 都不需要，它们都是可选的。
- [ ] 只需要实现LastName属性。
- [ ] 只需要实现FirstName属性。

[官方文档：interface](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/interface)

#### Q34. 你在程序中处理多个程序集，但担心内存分配。程序集在程序生命周期的什么时候加载到内存中？

- [ ] 在运行时
- [ ] 在编译时
- [x] 仅在需要时
- [ ] 仅在程序化加载时

1. [官方文档：程序集加载](https://docs.microsoft.com/en-us/dotnet/framework/deployment/best-practices-for-assembly-loading)
2. [Stackoverflow：程序集何时被加载？](https://stackoverflow.com/questions/21914692/when-exactly-are-assemblies-loaded)

#### Q35. 正则表达式的最准确描述是什么？

- [ ] 正则表达式是C#中用于解析HTML的工具
- [x] 正则表达式是用于描述搜索模式的特殊文本字符串。
- [ ] 正则表达式允许变量通过引用传递。
- [ ] 正则表达式允许类符合Equatable协议。

1. [官方文档：正则表达式语言 - 快速参考](https://docs.microsoft.com/en-us/dotnet/standard/base-types/regular-expression-language-quick-reference)
2. [官方文档：.NET正则表达式](https://docs.microsoft.com/en-us/dotnet/standard/base-types/regular-expressions)

#### Q36. 为什么要在C#中使用类字段

- [ ] 定义类的行为
- [x] 保存类对象中包含的信息和数据
- [ ] 在类和对象之间通信
- [ ] 存储类定义值

[官方文档：类介绍](https://docs.microsoft.com/en-us/dotnet/csharp/fundamentals/types/classes)

#### Q37. 什么时候在代码中使用泛型？

- [ ] 提高代码性能
- [x] 所有这些答案
- [ ] 当代码重用是优先考虑时
- [ ] 当类型安全很重要时

[官方文档：泛型类和方法](https://docs.microsoft.com/en-us/dotnet/csharp/fundamentals/types/generics)

#### Q38. 当这段代码被执行时，什么会打印到控制台？

```cs
public delegate void AuthCallback(bool validUser);
public static AuthCallback loginCallback = Login;
public static void Login()
{
    Console.WriteLine("Valid user!");
}

public static void Main(string[] args)
{
    loginCallback(true);
}
```

- [ ] Login successful...
- [ ] Valid user!
- [x] an error, because the method signature of Login doesn't match the delegate
- [ ] Login successful... Valid user!

1. [官方文档：委托介绍](https://docs.microsoft.com/en-us/dotnet/csharp/delegates-overview)
2. [官方文档：事件介绍](https://docs.microsoft.com/en-us/dotnet/csharp/events-overview)

#### Q39. 你如何声明一个名为User的密封类？

- [ ] public class User {}
- [ ] abstract User {}
- [x] sealed class User {}
- [ ] private sealed class User {}

[官方文档：抽象和密封类及类成员](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/abstract-and-sealed-classes-and-class-members)

#### Q40. 非静态类和静态类之间的区别是什么？

- [x] 非静态类在使用前需要初始化，而静态类不需要
- [ ] 非静态类只能从接口访问，而静态类可以从任何地方访问
- [ ] 非静态类需要在运行时初始化所有类成员，而静态类不需要
- [ ] 非静态类不需要初始化，而静态类需要

1. [stackoverflow](https://stackoverflow.com/questions/20451554/whats-the-function-of-a-static-constructor-in-a-non-static-class)
2. [官方文档：静态构造函数](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/static-constructors)

#### Q41. 哪个特征阻止这段代码编译？

`public int age="28"`

- [x] type safety
- [ ] single inheritance
- [ ] dependency injection
- [ ] multiple inheritance

[c-sharpcorner：.NET中的类型安全](https://www.c-sharpcorner.com/UploadFile/vikie4u/type-safety-in-net/)

#### Q42. 你如何序列化这个类？

`public class User {}`

- [ ] 用`DeserializableAttribute`标记User类。
- [ ] 将类声明为`public serializable class User {}`。
- [x] 用`SerializableAttribute`属性标记User类。
- [ ] 将类声明为`private serializable class User {}`。

[官方文档：SerializableAttribute类](https://docs.microsoft.com/en-us/dotnet/api/system.serializableattribute?view=net-5.0)

#### Q43. 你如何编写一个名为ResultCallback的委托，带有一个名为responseCode的int参数？

- [ ] public delegate ResultCallback(int responseCode);
- [ ] public delegate void ResultCallback<(int) responseCode>;
- [ ] public void delegate ResultCallback\<int responseCode\>;
- [x] public delegate void ResultCallback(int responseCode);

[官方文档：委托](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/delegates/)

#### Q44. 静态方法和非静态方法之间的区别是什么？

- [ ] 非静态方法总是需要void返回类型
- [ ] 非静态方法无法访问静态成员变量
- [x] 静态方法不需要实例化类的实例来调用方法
- [ ] 静态方法总是必须是公共的

[官方文档：静态成员](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/static-classes-and-static-class-members#static-members)

#### Q45. 基于名为ResultCallback的委托，编写名为apiResult的事件的正确方法是什么？

- [ ] public void event ResultCallback apiResult;
- [ ] public event ResultCallback(() -> apiResult);
- [ ] public event void ResultCallback
- [x] public event ResultCallback apiResult;

[官方文档：事件介绍](https://docs.microsoft.com/en-us/dotnet/csharp/events-overview)

#### Q46. 在try-catch语句中，finally块中的代码什么时候执行？

- [ ] 如果有错误，它根本不会执行
- [ ] 在try和catch块之间
- [x] 在try和catch块之后
- [ ] 当finally块覆盖catch块并在其位置执行时

[官方文档：try-catch](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/try-catch)

#### Q47. 什么方法正确地扩展了string类？

- [x] public static string IsvalidName(this string i, string value) {}
- [ ] public static void IsvalidName(this string i, string value) {}
- [ ] public string IsvalidName(this string i, string value) {}
- [ ] public void IsvalidName(this string i, string value) {}

#### Q48. C#类如何受到限制？

- [x] 它们不支持多重继承。
- [ ] 它们支持多重继承。
- [ ] 它们只能有固定数量的属性。
- [ ] 它们只能有固定数量的方法。

[官方文档：类继承](https://docs.microsoft.com/en-us/dotnet/csharp/fundamentals/types/classes#class-inheritance)

#### Q49. 命名空间执行什么功能？

- [ ] 命名空间在运行时计算代码覆盖率。
- [ ] 命名空间在编译时将应用程序代码编译在一起。
- [ ] 命名空间将代码分组到单个存储库中。
- [x] 命名空间将代码分离到分组中，控制访问，并避免命名冲突。

[官方文档：namespace](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/namespace)

#### Q50. 编写带有私有支持字段的公共属性的正确方法是什么？

- [ ] A

```cs
private int _password;
pubic int Password = { get; set; }
```

- [ ] B

```cs
private int _password;
public int Password = _password;
```

- [ ] C

```cs
private int _password;
public int Password
{
  get -> _password;
  set-> _password = value;
}
```

- [x] D

```cs
private int _password;
public int Password
{
  get { return _password; }
  set { _password = value; }
}
```

[官方文档：使用属性](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/using-properties)

#### Q51. 什么是线程池？

- [ ] 在初始化期间创建的同步方法集合，无法重用
- [x] 在初始化期间创建的线程集合，可以重用
- [ ] 仅在编译时识别的线程集合，可以重用
- [ ] 在编译时创建的异步方法集合，无法重用

[官方文档：ThreadPool类](https://docs.microsoft.com/en-us/dotnet/api/system.threading.threadpool?view=net-5.0)

#### Q52. 当C#中的对象被序列化时，它被转换为什么？

- [ ] XML
- [ ] JSON
- [x] byte stream
- [ ] value stream

[官方文档：序列化](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/serialization/)

#### Q53. 什么是委托

- [ ] 保存对值类型及其内容的引用的变量
- [ ] 只能在回调方法中使用的特定值类型
- [x] 保存对具有特定参数列表和返回类型的方法的引用的类型
- [ ] 可以在抽象类中使用的自定义变量类型

[官方文档：委托](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/delegates/)

#### Q54. C#中与异常处理相关的四个关键字是什么？

- [ ] try, catch, valid, invalid
- [ ] try, valid, finally, throw
- [x] try, catch, finally, throw
- [ ] finally, throw, valid, invalid

[Tutorial Point](https://www.tutorialspoint.com/csharp/csharp_exception_handling.htm#:~:text=Exceptions%20provide%20a%20way%20to,catch%2C%20finally%2C%20and%20throw.)

#### Q55. is和as运算符之间的主要区别是什么？

- [ ] is运算符检查实例类型，而as运算符检查继承类型。
- [ ] is运算符检查原始数据类型，而as运算符检查对象类型。
- [ ] as运算符检查对象类型，而is运算符尝试将对象转换为特定类型。
- [x] is运算符检查对象类型，而as运算符尝试将对象转换为特定类型。

[Pluralsight指南](https://www.pluralsight.com/guides/csharp-is-as-operators-is-expressions)

#### Q56. finally和finalize块之间的区别是什么？

- [ ] finally块在try和catch块执行期间被调用，而finalize方法在垃圾回收后被调用。
- [x] finally块在try和catch块执行后被调用，而finalize方法在垃圾回收前被调用。
- [ ] finalize块在try和catch块执行前被调用，而finally方法在垃圾回收前被调用。
- [ ] finalize块在try和catch块执行期间被调用，而finally方法在垃圾回收后被调用。

[C-sharpcorner](https://www.c-sharpcorner.com/forums/final-finally-and-finalize)

#### Q57. 你的应用程序有一个名为username的值类型，需要能够接受null值，但这会产生编译时错误。你如何在代码中修复这个问题？

- [ ] Null<string> username = null;
- [x] string? username = null;
- [ ] Type<string>? username = null;
- [ ] Optional<string> username = null;

#### Q58. 哪个代码片段正确声明了一个名为InvalidResponse的自定义异常？

- [ ] struct InvalidResponse: Exception {}
- [x] class InvalidResponse: Exception {}
- [ ] public Exception InvalidResponse = new Exception ();
- [ ] public Exception InvalidResponse () -> Exception;

[官方文档：异常](https://docs.microsoft.com/en-us/dotnet/standard/exceptions/how-to-create-user-defined-exceptions)

#### Q59. 你如何编写一个名为AppState的枚举变量，值为Offline、Loading和Ready？

- [ ] enum AppState = [Offline, Loading, Ready]
- [ ] enum AppState {"Offline", "Loading", "Ready"}
- [ ] enum AppState = {Offline, Loading, Ready}
- [x] enum AppState {Offline, Loading, Ready}

[官方文档：Enum](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/enum)

#### Q60. 值类型和引用类型之间的主要区别是什么？

- [ ] 值类型可以是任何原始类型，而引用类型必须是类型无关的。
- [ ] 值类型引用另一个值，而引用类型引用内存中的值。
- [x] 值类型存储实际值，而引用类型是指向值的指针。
- [ ] 值类型仅在运行时可用，而引用类型仅在编译时可用。

1. [官方文档：值类型](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/value-types)
2. [官方文档：引用类型](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/reference-types)

#### Q61. `break`和`continue`关键字之间的区别是什么？

- [ ] `break`关键字用于跳出多个迭代语句，而`continue`只能跳出具有单个迭代的代码块。
- [x] `break`关键字字面上跳出控制流语句，而`continue`忽略控制语句或迭代的其余部分并开始下一个。
- [ ] `break`关键字字面上跳出当前控制流代码并停止它，而`continue`在抛出异常后继续执行代码。
- [ ] `break`关键字跳出迭代然后继续执行其余的控制流代码，而`continue`停止执行代码。

[官方文档：跳转语句](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/statements/jump-statements)

#### Q62. 哪个代码片段正确声明了一个名为userId的变量，带有公共`get`和私有`set`？

- [ ] `public int userID <get, set>;`
- [ ] `public int userID [get, private set];`
- [x] `public int userID { get; private set; }`
- [ ] `public int userID = { public get, private set };`

[官方文档：属性](https://docs.microsoft.com/en-us/dotnet/csharp/properties)

#### Q63. 关于虚拟方法，什么是正确的？

- [ ] `在派生类中重写虚拟方法是强制性的。`
- [ ] `在派生类中重写虚拟方法是不可能的。`
- [x] `虚拟方法总是需要默认实现。`
- [ ] `虚拟方法不能有默认实现。`

1. [官方文档：virtual](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/virtual)
2. [c-sharpcorner：C#中的虚拟方法](https://www.c-sharpcorner.com/UploadFile/3d39b4/virtual-method-in-C-Sharp/)

#### Q64. 如果你的程序中有多个线程访问同一资源，可能会发生什么？

- [ ] `资源过载`
- [ ] `线程跳跃`
- [x] `死锁和竞争条件`
- [ ] `什么都没有，因为这就是线程的用途`

[官方文档：竞争条件](https://docs.microsoft.com/en-us/archive/msdn-magazine/2008/october/concurrency-hazards-solving-problems-in-your-multithreaded-code)

#### Q65. 你如何表示字符串可能为null？

- [ ] `字符串不能为null。`
- [x] `string? myVariable`
- [ ] `string myVariable = null`
- [ ] `string(null) myVariable`

[官方文档：可空值类型](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/nullable-value-types#declaration-and-assignment)

#### Q66. 在使用out变量之前需要声明它吗？

- [x] `不需要，你可以在参数列表中声明out。`
- [ ] `不需要，Out变量不再是C#的一部分。`
- [ ] `如果是原始类型，你必须声明它。`
- [ ] `是的。`

#### Q67. 你如何访问名为People的数组中的最后两个人？

- [x] `People[..^2]`
- [ ] `在C#中你不能这样做。`
- [ ] `People[..^3]`
- [ ] `People[^2]`

解释：你**可以**在C#中这样做。但是，上述答案都不正确。你可以通过使用`People[^2..]`来访问最后两个项目。更多信息请参见[issue #3354](https://github.com/Ebazhanov/linkedin-skill-assessments-quizzes/issues/3354)。
另见：[官方文档：范围](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/proposals/csharp-8.0/ranges)

#### Q68. 什么时候可以创建匿名类型？

- [x] `在编译时`
- [ ] `在运行时之后`
- [ ] `在运行时`
- [ ] `在编译时之后`

[C-sharpcorner：匿名类型](https://www.c-sharpcorner.com/UploadFile/ff2f08/anonymous-types-in-C-Sharp/)

#### Q69. 关于线程多任务，什么是正确的？

- [x] `线程多任务允许代码并发执行`
- [ ] `线程多任务允许代码仅在处理用户事件时执行。`
- [ ] `线程多任务阻止代码同时执行以保护内存。`
- [ ] `线程多任务将单线程代码块加在一起。`

[官方文档：线程](https://docs.microsoft.com/en-us/dotnet/standard/threading/threads-and-threading)

#### Q70. 这个类字段有什么可访问性级别？

`private string LastName;`

- [x] 它只能被同一类或结构体中的其他代码使用。
- [ ] 它只能被引用程序集中的其他代码使用。
- [ ] 它只能被派生类中包含的代码使用。
- [ ] 它只能被同一程序集中的其他代码使用。

[官方文档：可访问性级别](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/accessibility-levels)

#### Q71. 你如何正确声明一个名为'partyInvites'的锯齿数组，包含10个空元素？

- [ ] `string[] partyInvites = new string[10];`
- [x] `string[][] partyInvites = new string[10][];`
- [ ] `string[][] partyInvites = new string[10]();`
- [ ] `string <[]> partyInvites = new string <[10]>;`

[官方文档：锯齿数组](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/arrays/jagged-arrays)

#### Q72. 你如何暂停线程三秒钟？

- [ ] Thread.Pause(3000);
- [ ] Thread.Resume(-3000);
- [ ] Thread.Suspend(3000);
- [x] Thread.Sleep(3000);

[参考](https://docs.microsoft.com/en-us/dotnet/api/system.threading.thread.sleep?view=net-6.0)

#### Q73. 这段代码有什么问题？

```cs
void MyFunction()
{
    {
        int a = 10;
        int b = 20;
        int c = a + b;
    }

    Console.WriteLine(c);
}
```

- [ ] 变量c从未被使用；在控制台上显示它不算作使用。
- [ ] 变量a和b从未被使用。
- [ ] 你不能在另一个块内的括号内放置代码。
- [x] 变量c在块外不再存在。

[参考](https://stackoverflow.com/a/6136865)

#### Q74. 以下哪个语句是正确的？

- [ ] 所有都是正确的。
- [ ] 没有一个是正确的。
- [ ] string 是值类型。
- [x] string 是 String 的别名

[参考](https://stackoverflow.com/q/7074)

#### Q75. 如何从方法中返回多个值？

- [x] 使用元组或 out 变量。
- [ ] 唯一的方法是使用 out 变量。
- [ ] 唯一的方法是使用元组。
- [ ] 这无法实现

#### Q76. 哪个是派生类的有效示例？

- [ ] `public class PremiumUser sub User {}`
- [x] `public class PremiumUser: User {}`
- [ ] `public class PremiumUser -> sub User {}`
- [ ] `public class User: PremiumUser {}`

#### Q77. 从名为 InputManager 的静态类调用名为 DebugString 的静态方法的正确方式是什么？

- [ ] `static InputManager.DebugString();`
- [ ] `InputManager().DebugString;`
- [ ] `new InputManager().DebugString();`
- [x] `InputManager.DebugString();`

#### Q78. 可以给这个变量赋什么值？

```cs
public string? nickname
```

- [ ] null
- [ ] 字符串值
- [x] 字符串值或 null
- [ ] 包含多个字符的字符串值

#### Q79. 什么是析构函数？

- [ ] `在对象创建或更新时自动调用的特殊方法`
- [ ] `在线程池并发处理时自动调用的隐式方法`
- [ ] `在编译器开始运行时自动调用的显式方法`
- [x] `在对象被删除或销毁时自动调用的特殊方法`

[参考](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/destructors)

#### Q80. 哪个代码片段正确声明了 Int32 类型的 CustomInt 类型别名？

- [ ] `typealias CustomInt = System.Int32;`
- [ ] `var<T> CustomInt = Int32;`
- [x] `using CustomInt = System.Int32;`
- [ ] `type CustomInt = System<Int32>;`

[参考](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/using-directive)

#### Q81. 什么是枚举类型？

- [ ] `按引用传递类型的对象`
- [ ] `不能保存常量的值类型`
- [x] `命名整数常量的集合`
- [ ] `按值传递类型的对象`

#### Q82. readonly 关键字在字段声明中用于什么？

- [ ] `声明一个在运行时无法计算的成员变量`
- [x] `声明一个只能在构造函数退出前赋值的字段`
- [ ] `声明一个必须在编译时设置的静态变量`
- [ ] `声明一个必须在运行时设置的静态变量`

#### Q83. 关于 C# 方法的哪个语句是正确的？

- [ ] `方法存储变量。`
- [x] `方法是对象可以执行的操作`
- [ ] `一个方法在每个 C# 文件中只能使用一次。`
- [ ] `方法确定给定属性的状态。`

[官方文档：方法（C# 编程指南）](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/methods)

#### Q84. 哪个是有效的内置 C# 异常类？

- [ ] `ArgumentNullValue`
- [ ] `InvalidFormatFoundException`
- [ ] `IndexOutOfPocket`
- [x] `ArgumentNullException`

[官方文档：ArgumentNullException 类](https://docs.microsoft.com/en-us/dotnet/api/system.argumentnullexception?view=net-5.0)

#### Q85. C# 中接口的目的是什么？

- [ ] 接口用于存储数据。
- [x] 接口定义类必须遵循的契约，指定实现类必须提供的一组方法和属性。
- [ ] 接口用于创建类的实例。
- [ ] 接口用于代码组织。

[官方文档：接口（C# 编程指南）](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/interfaces/)

#### Q86. C# try-catch-finally 语句中 `finally` 块的主要目的是什么？

- [ ] `finally` 块用于处理异常。
- [ ] `finally` 块用于定义 try-catch 语句的主要逻辑。
- [ ] `finally` 块是可选的，在 try-catch 语句中不是必需的。
- [x] `finally` 块用于确保无论是否发生异常，某些代码都会被执行。

[官方文档：try-catch（C# 参考）](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/try-catch)

#### Q87. C# 中哪个数据结构允许您存储键值对，通常用于快速数据检索？

- [ ] ArrayList
- [ ] List
- [ ] Array
- [x] Dictionary

[官方文档：Dictionary<TKey, TValue> 类](https://docs.microsoft.com/en-us/dotnet/api/system.collections.generic.dictionary-2)

#### Q88. 程序的执行从什么开始？

- [x] Main()
- [ ] Get()
- [ ] Class()
- [ ] Display()

[参考]：https://www.gkseries.com/c-sharp-programming/multiple-choice-questions-and-answers

#### Q89. 在 C# 中 'using' 是什么？

- [ ] 类
- [x] 指令
- [ ] 函数
- [ ] 关键字

[参考]：https://www.gkseries.com/c-sharp-programming/multiple-choice-questions-and-answers
