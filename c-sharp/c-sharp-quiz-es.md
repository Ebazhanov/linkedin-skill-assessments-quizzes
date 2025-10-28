## C#

#### Q1. ¿En cuál de estas situaciones son las interfaces mejores que las clases abstractas?

- [ ] Cuando necesitas definir las características de un tipo de objeto, usa una interface. Cuando necesitas definir las capacidades de un tipo de objeto, usa una clase abstracta.
- [ ] Las interfaces son un legado de versiones anteriores de C#, y son intercambiables con la característica más nueva de clase abstracta.
- [x] Cuando necesitas una lista de capacidades y datos que son independientes de las clases, usa una interface. Cuando necesitas que un cierto tipo de objeto comparta características, usa una clase abstracta.
- [ ] Deberías usar tanto una interface como una clase abstracta al definir cualquier objeto complejo.

#### Q2. ¿Cuál afirmación es verdadera sobre los delegates?

- [ ] Los delegates no están soportados en la versión actual de C#
- [ ] No pueden ser usados como callbacks.
- [ ] Solo las variables pueden ser pasadas a los delegates como parámetros.
- [x] Pueden ser encadenados juntos.

[Documentación oficial: Delegates](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/delegates/#delegates-overview)

#### Q3. ¿Cuál opción define mejor el modelo de programación asíncrona de C#?

- [ ] reactivo
- [ ] callback heredado
- [x] basado en tareas
- [ ] basado en callbacks

[Documentación oficial: Modelo de programación asíncrona basado en tareas](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/async/task-asynchronous-programming-model) respuesta correta --> var contacts = new List<string>();

#### Q4. ¿Cómo determinarías si una clase tiene un atributo particular?

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

1. [Documentación oficial: Clase Attribute](https://docs.microsoft.com/en-us/dotnet/api/system.attribute?view=net-5.0)
2. [Documentación oficial: Método Attribute.GetCustomAttribute](https://docs.microsoft.com/en-us/dotnet/api/system.attribute.getcustomattribute?view=net-5.0)

#### Q5. ¿Cuál es la diferencia entre las palabras clave ref y out?

- [ ] Las variables pasadas a out especifican que el parámetro es un parámetro de salida, mientras que ref especifica que una variable puede ser pasada a una función sin ser inicializada.
- [ ] Las variables pasadas a ref pueden ser pasadas a una función sin ser inicializadas, mientras que out especifica que el valor es un valor de referencia que puede ser cambiado dentro del método que llama.
- [x] Las variables pasadas a out pueden ser pasadas a una función sin ser inicializadas, mientras que ref especifica que el valor es un valor de referencia que puede ser cambiado dentro del método que llama.
- [ ] Las variables pasadas a ref especifican que el parámetro es un parámetro de salida, mientras que out especifica que una variable puede ser pasada a una función sin ser inicializada.

1. [Documentación oficial: ref](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/ref)
2. [Documentación oficial: modificador de parámetro out](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/out-parameter-modifier)

#### Q6. ¿Cómo podrías recuperar información sobre una clase, así como crear una instancia en tiempo de ejecución?

- [x] reflexión
- [ ] serialización
- [ ] abstracción
- [ ] inyección de dependencias

[Documentación oficial: Reflexión](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/reflection)

#### Q7. ¿De qué es un ejemplo este código?

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

- [ ] una clase privada que usa multithreading
- [ ] codificación multithread
- [ ] mala gestión de hilos
- [x] un deadlock potencial

[Documentación oficial: Deadlocks y condiciones de carrera](https://docs.microsoft.com/en-us/dotnet/standard/threading/managed-threading-best-practices#deadlocks-and-race-conditions)

#### Q8. ¿Cuál es la diferencia entre un tipo anónimo y un tipo de datos regular?

- [x] Los tipos anónimos no tienen nombres de tipo
- [ ] Los tipos anónimos solo pueden ser estáticos
- [ ] Los tipos anónimos solo pueden ser usados en structs
- [ ] Los tipos anónimos no funcionan con LINQ.

[Documentación oficial: Tipos Anónimos](https://docs.microsoft.com/en-us/dotnet/csharp/fundamentals/types/anonymous-types)

#### Q9. ¿Cuándo usarías un Dictionary en lugar de un tipo Array en tu aplicación?

- [ ] Cuando necesitas una estructura de colección irregular
- [ ] Cuando necesitas almacenar valores del mismo tipo
- [x] Cuando necesitas almacenar pares clave-valor en lugar de valores únicos
- [ ] Cuando necesitas una lista ordenada y buscable

[Documentación oficial: Clase Dictionary<TKey,TValue>](https://docs.microsoft.com/en-us/dotnet/api/system.collections.generic.dictionary-2?view=net-5.0)

#### Q10. ¿Cuál es la diferencia entre a.Equals(b) y a == b?

- [ ] El método .Equals compara identidades de referencia mientras que `==` compara contenidos.
- [ ] El método .Equals compara valores primitivos mientras que `==` compara todos los valores.
- [x] El método .Equals compara contenidos mientras que `==` compara identidad de referencia.
- [ ] El método .Equals compara tipos de referencia mientras que `==` compara tipos de valor primitivos

1. [Documentación oficial: Object.Equals](https://docs.microsoft.com/en-us/dotnet/api/system.object.equals)
2. [c-sharpcorner: Operador de Igualdad(==) vs .Equals()](https://www.c-sharpcorner.com/UploadFile/3d39b4/difference-between-operator-and-equals-method-in-C-Sharp)

#### Q11. ¿Cuál opción describe mejor una situación de deadlock?

- [ ] cuando intentas instanciar dos objetos al mismo tiempo en la misma clase o struct
- [ ] cuando estás tratando de ejecutar una acción después de que se registra un evento de usuario
- [x] cuando instrucciones simultáneas están esperando unas a otras para terminar antes de ejecutarse
- [ ] cuando intentas ejecutar una serie de eventos simultáneamente en múltiples hilos

[Documentación oficial: Deadlocks y condiciones de carrera](https://docs.microsoft.com/en-us/dotnet/standard/threading/managed-threading-best-practices#deadlocks-and-race-conditions)

#### Q12. ¿Cómo funciona la palabra clave async?

- [ ] Permite acceso a métodos asíncronos en la API de C#
- [ ] Permite agrupación de hilos y procesos síncronos en clases estáticas.
- [x] Permite que la palabra clave await sea usada en un método
- [ ] Permite acceso a métodos síncronos en la API de C#

[Documentación oficial: async](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/async)

#### Q13. ¿Qué es un objeto en C#?

- [ ] una clase o struct, incluyendo sus variables y funciones
- [ ] un tipo de datos primitivo que solo puede ser creado en tiempo de compilación
- [ ] un tipo de valor que solo puede ser usado con una clase abstracta
- [x] una instancia de una clase o struct que incluye campos, propiedades y/o métodos

[Documentación oficial: Objetos](https://docs.microsoft.com/en-us/dotnet/csharp/fundamentals/object-oriented/objects)

#### Q14. ¿Qué fragmento de código declara un tipo anónimo llamado userData?

- [ ] `var<<!---->T> userData = new <<!---->T> { name = "John", age = 32 };`
- [x] `var userData = new { name = "John", age = 32 };`
- [ ] `AType userData = new AType { name = "John", age = 32 };`
- [ ] `Anonymous<T> userData = new Anonymous<T> { name = "John", age = 32 };`

[Documentación oficial: Tipos Anónimos](https://docs.microsoft.com/en-us/dotnet/csharp/fundamentals/types/anonymous-types)

#### Q15. ¿Qué será retornado cuando este método sea ejecutado?

`public void userInput(string charParameters) { }`

- [x] Nada
- [ ] un Boolean
- [ ] una variable string
- [ ] un entero

[Documentación oficial: void](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/void)

#### Q16. ¿En qué orden serían impresos los nombres de empleados en este ejemplo en la consola?

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

- [x] ascendente
- [ ] desordenado
- [ ] descendente
- [ ] primero en entrar, primero en salir

[dotnetpattern: Operador LINQ OrderBy](http://dotnetpattern.com/linq-orderby-operator)

#### Q17. Las expresiones lambda son frecuentemente usadas en conjunto con cuál de las siguientes?

- [ ] Namespaces
- [x] LINQ
- [ ] Alias de Tipos
- [ ] Assemblies

[Documentación oficial: Resumen de Language Integrated Query (LINQ)](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/linq/)

#### Q18. ¿Cuál es el formato correcto para comentarios de una línea y múltiples líneas?

- [ ] `/_/ - Una Línea`
      `/_ - Múltiples líneas`
- [ ] `// Múltiples líneas`
      `/_ Una Línea _/`
- [ ] `//\* Múltiples líneas`
      `/ Una Línea`
- [x] `// Una Línea`
      `/* Múltiples líneas */`

[w3schools: Comentarios C#](https://www.w3schools.com/cs/cs_comments.php)

#### Q19. ¿Cómo haces que un método en una clase abstracta sea sobrescribible?

- [ ] Hazlo público
- [ ] Hazlo estático
- [ ] Hazlo privado
- [x] Hazlo virtual

1. [Documentación oficial: virtual](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/virtual)
2. [Documentación oficial: abstract](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/abstract)

#### Q20. ¿Cómo escribirías código para una propiedad entera llamada Age con un getter y setter?

- [ ] public int Age { get - set }
- [ ] public int Age: get set;
- [ ] public int Age (get, set );
- [x] public int Age { get; set; }

[Documentación oficial: Usando Propiedades](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/using-properties)

#### Q21. ¿Qué es una clase abstracta?

- [ ] una clase que está denotada por la palabra clave class (puede ser vista y usada por cualquier otra clase en el sistema--por lo tanto es pública por defecto)
- [ ] algo denotado por la palabra clave abstract y usado en todo el sistema; si quieres que cualquier programa cree un objeto de una clase usas la clase abstracta
- [ ] una clase que está denotada por la palabra clave virtual
- [x] una clase que solo puede ser usada como una clase base

[Documentación oficial: Clases Abstractas y Selladas y Miembros de Clase](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/abstract-and-sealed-classes-and-class-members)

#### Q22. ¿Qué pasa con un hilo dado después de que termina su tarea cuando usas un thread pool?

- [ ] El hilo es destruido y la memoria es liberada.
- [ ] El hilo corre en un bucle hasta la siguiente asignación.
- [ ] El hilo se vuelve inactivo en el fondo y espera la recolección de basura.
- [x] El hilo regresa al pool para reutilización.

[Documentación oficial: Características del thread pool](https://docs.microsoft.com/en-us/dotnet/standard/threading/the-managed-thread-pool#thread-pool-characteristics)

#### Q23. ¿Cuál opción representa una clase que hereda comportamiento de una clase base?

- [ ] una segunda clase base
- [ ] una clase revisada
- [x] una clase derivada
- [ ] una clase padre

[Documentación oficial: Herencia](https://docs.microsoft.com/en-us/dotnet/csharp/fundamentals/object-oriented/inheritance)

#### Q24. ¿Qué te permite hacer la sobrecarga de operadores?

- [ ] ocultar operadores integrados cuando sea necesario
- [ ] agregar métodos para ser interpretados por el compilador en tiempo de ejecución
- [ ] definir cómo funcionan los enums y otros tipos de valor primitivos dentro del resto de la aplicación
- [x] definir funcionalidad personalizada para operadores comunes como suma e igualdad

[Documentación oficial: Sobrecarga de operadores](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/operators/operator-overloading)

#### Q25. ¿Cuál es el propósito principal de LINQ?

- [ ] para eliminar datos duplicados
- [ ] para vincular namespaces y assemblies
- [x] para consultar y transformar datos
- [ ] para conectar assemblies

[Documentación oficial: Resumen de Language Integrated Query (LINQ)](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/linq/#query-expression-overview)

#### Q26. ¿Cuál es la sintaxis correcta para una nueva lista genérica de strings llamada contacts?

- [ ] public List<string names> contacts = new List<string names>();
- [ ] public List(string names) contacts = new List(string names)();
- [x] var contacts = new List<string>();
- [ ] var contacts = new List(string);

[Documentación oficial: Clase List<T>](https://docs.microsoft.com/en-us/dotnet/api/system.collections.generic.list-1?view=net-5.0)

#### Q27. ¿Cuál es la diferencia entre throw exceptions y throw clauses?

- [ ] Las throw clauses se disparan solo en tiempo de ejecución, mientras que las throw exceptions pueden dispararse en cualquier momento.
- [x] Las throw exceptions sobrescriben el stack trace, mientras que las throw clauses retienen la información del stack.
- [ ] Las throw clauses sobrescriben el stack trace, mientras que las throw exceptions retienen la información del stack.
- [ ] Las throw exceptions se disparan solo en tiempo de ejecución, mientras que las throw clauses pueden dispararse durante el tiempo de compilación.

1. [Documentación oficial: throw](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/throw)
2. [c-sharpcorner: Diferencia Entre Throw Exception y Throw Clause](https://www.c-sharpcorner.com/UploadFile/akkiraju/difference-between-throw-exception-and-throw-clause/)

#### Q28. Cuando un método asíncrono es ejecutado, el código corre pero no pasa nada más que una advertencia del compilador. ¿Qué es lo más probable que esté causando que el método no retorne nada?

- [ ] Falta la declaración return yield al final del método.
- [x] El método está faltando una palabra clave await en su cuerpo.
- [ ] Falta la palabra clave wait al final del método.
- [ ] Falta la palabra clave yield en el método.

[Documentación oficial: Iniciando tareas concurrentemente](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/async/#start-tasks-concurrently)

#### Q29. ¿Qué son los eventos de C#?

- [ ] acciones del sistema que se comunican directamente con el compilador en tiempo de ejecución
- [ ] acciones que se ejecutan cuando el código compila, generando logs y salida de prueba
- [x] acciones que generan notificaciones, que son enviadas a sus listeners registrados
- [ ] métodos solo de usuario que envían datos al backend de la aplicación

[Documentación oficial: Introducción a eventos](https://docs.microsoft.com/en-us/dotnet/csharp/events-overview)

#### Q30. ¿Qué tipo de valores pueden almacenar los arrays?

- [ ] colecciones desordenadas de valores numéricos
- [ ] pares clave-valor de cualquier tipo soportado por C#
- [ ] instancias de clase y struct
- [x] múltiples variables, o colecciones, del mismo tipo

[Documentación oficial: Arrays](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/arrays/)

#### Q31. Dada esta enumeración, ¿cómo accederías al valor de tipo entero de 'AppState.Loading'?

`enum AppState { OffLine, Loading, Ready }`

- [ ] string currentState = (string)AppState.Loading;
- [ ] string currentState = AppState.Loading.integralVal;
- [ ] int currentState = AppState.Loading.rawValue;
- [x] int currentState = (int)AppState.Loading;

[Documentación oficial: Tipos de enumeración](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/enum#conversions)

#### Q32. ¿Qué carácter usarías para iniciar un patrón de expresión regular en un límite de palabra?

- [ ] d
- [ ] \a
- [x] \b
- [ ] \w

1. [regular-expressions: Límites de Palabra](https://www.regular-expressions.info/wordboundaries.html)
2. [Documentación oficial: Referencia Rápida del Lenguaje de Expresión Regular](https://docs.microsoft.com/en-us/dotnet/standard/base-types/regular-expression-language-quick-reference)

#### Q33. Para conformar a la siguiente interface, ¿cuáles de sus miembros necesitan ser implementados?

```cs
public interface INameable
{
    string FirstName { get; set; }
    string LastName { get; }
}
```

- [x] Ambas propiedades FirstName y LastName necesitan ser implementadas.
- [ ] Ninguna, ambas son opcionales.
- [ ] Solo la propiedad LastName necesita ser implementada.
- [ ] Solo la propiedad FirstName necesita ser implementada.

[Documentación oficial: interface](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/interface)

#### Q34. Estás tratando con múltiples assemblies en tu programa, pero estás preocupado por la asignación de memoria. ¿En qué punto del ciclo de vida del programa se cargan los assemblies en memoria?

- [ ] en tiempo de ejecución
- [ ] en tiempo de compilación
- [x] solo cuando se requieren
- [ ] solo cuando se cargan programáticamente

1. [Documentación oficial: Carga de Assemblies](https://docs.microsoft.com/en-us/dotnet/framework/deployment/best-practices-for-assembly-loading)
2. [Stackoverflow: ¿Cuándo exactamente se cargan los assemblies?](https://stackoverflow.com/questions/21914692/when-exactly-are-assemblies-loaded)

#### Q35. ¿Cuál es la descripción más precisa de una expresión regular?

- [ ] Una expresión regular es una herramienta de C# usada para parsear HTML
- [x] Una expresión regular es una cadena de texto especial para describir un patrón de búsqueda.
- [ ] Una expresión regular permite que una variable sea pasada por referencia.
- [ ] Una expresión regular permite que una clase se conforme al protocolo Equatable.

1. [Documentación oficial: Referencia Rápida del Lenguaje de Expresión Regular](https://docs.microsoft.com/en-us/dotnet/standard/base-types/regular-expression-language-quick-reference)
2. [Documentación oficial: Expresiones regulares .NET](https://docs.microsoft.com/en-us/dotnet/standard/base-types/regular-expressions)

#### Q36. ¿Por qué usarías un campo de clase en C#?

- [ ] Para definir los comportamientos de la clase
- [x] Para mantener información y datos contenidos en el objeto de clase
- [ ] Para comunicar entre clases y objetos
- [ ] Para almacenar el valor de definición de la clase

[Documentación oficial: Introducción a clases](https://docs.microsoft.com/en-us/dotnet/csharp/fundamentals/types/classes)

#### Q37. ¿Cuándo usarías genéricos en tu código?

- [ ] para aumentar el rendimiento del código
- [x] todas estas respuestas
- [ ] cuando la reutilización de código es una prioridad
- [ ] cuando la seguridad de tipos es importante

[Documentación oficial: Clases y métodos genéricos](https://docs.microsoft.com/en-us/dotnet/csharp/fundamentals/types/generics)

#### Q38. ¿Qué se imprime en la consola cuando este código es ejecutado?

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
- [x] un error, porque la firma del método Login no coincide con el delegate
- [ ] Login successful... Valid user!

1. [Documentación oficial: Introducción a Delegates](https://docs.microsoft.com/en-us/dotnet/csharp/delegates-overview)
2. [Documentación oficial: Introducción a Eventos](https://docs.microsoft.com/en-us/dotnet/csharp/events-overview)

#### Q39. ¿Cómo declararías una clase sellada llamada User?

- [ ] public class User {}
- [ ] abstract User {}
- [x] sealed class User {}
- [ ] private sealed class User {}

[Documentación oficial: Clases Abstractas y Selladas y Miembros de Clase](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/abstract-and-sealed-classes-and-class-members)

#### Q40. ¿Cuál es la diferencia entre clases no estáticas y estáticas?

- [x] las clases no estáticas necesitan ser inicializadas antes del uso, mientras que las clases estáticas no
- [ ] las clases no estáticas son accesibles solo desde una interface mientras que las clases estáticas son accesibles desde cualquier lugar
- [ ] las clases no estáticas necesitan inicializar todos los miembros de clase en tiempo de ejecución, mientras que las clases estáticas no
- [ ] las clases no estáticas no necesitan ser inicializadas mientras que las clases estáticas sí

1. [stackoverflow](https://stackoverflow.com/questions/20451554/whats-the-function-of-a-static-constructor-in-a-non-static-class)
2. [Documentación oficial: Constructores Estáticos](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/static-constructors)

#### Q41. ¿Qué característica previene que este código compile?

`public int age="28"`

- [x] seguridad de tipos
- [ ] herencia simple
- [ ] inyección de dependencias
- [ ] herencia múltiple

[c-sharpcorner: Seguridad de Tipos en .NET](https://www.c-sharpcorner.com/UploadFile/vikie4u/type-safety-in-net/)

#### Q42. ¿Cómo serializarías esta clase?

`public class User {}`

- [ ] Marca la clase User con el `DeserializableAttribute`.
- [ ] Declara la clase como `public serializable class User {}`.
- [x] Marca la clase User con el atributo `SerializableAttribute`.
- [ ] Declara la clase como `private serializable class User {}`.

[Documentación oficial: Clase SerializableAttribute](https://docs.microsoft.com/en-us/dotnet/api/system.serializableattribute?view=net-5.0)

#### Q43. ¿Cómo escribirías un delegate llamado ResultCallback con un parámetro int llamado responseCode?

- [ ] public delegate ResultCallback(int responseCode);
- [ ] public delegate void ResultCallback<(int) responseCode>;
- [ ] public void delegate ResultCallback\<int responseCode\>;
- [x] public delegate void ResultCallback(int responseCode);

[Documentación oficial: Delegates](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/delegates/)

#### Q44. ¿Cuál es la diferencia entre un método estático y no estático?

- [ ] los métodos no estáticos siempre necesitan tener un tipo de retorno void
- [ ] los métodos no estáticos no tienen acceso a variables miembro estáticas
- [x] los métodos estáticos no tienen que instanciar una instancia de la clase para llamar al método
- [ ] los métodos estáticos siempre tienen que ser públicos

[Documentación oficial: Miembros Estáticos](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/static-classes-and-static-class-members#static-members)

#### Q45. ¿Cuál es la forma correcta de escribir un evento llamado apiResult basado en un delegate llamado ResultCallback?

- [ ] public void event ResultCallback apiResult;
- [ ] public event ResultCallback(() -> apiResult);
- [ ] public event void ResultCallback
- [x] public event ResultCallback apiResult;

[Documentación oficial: Introducción a eventos](https://docs.microsoft.com/en-us/dotnet/csharp/events-overview)

#### Q46. ¿Cuándo se ejecutará el código dentro del bloque finally en una declaración try-catch?

- [ ] si hay un error, no se ejecutará en absoluto
- [ ] entre los bloques try y catch
- [x] después de los bloques try y catch
- [ ] cuando el bloque finally anula el bloque catch y se ejecuta en su lugar

[Documentación oficial: try-catch](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/try-catch)

#### Q47. ¿Qué método extiende correctamente la clase string?

- [x] public static string IsvalidName(this string i, string value) {}
- [ ] public static void IsvalidName(this string i, string value) {}
- [ ] public string IsvalidName(this string i, string value) {}
- [ ] public void IsvalidName(this string i, string value) {}

#### Q48. ¿Cómo están limitadas las clases de C#?

- [x] No soportan herencia múltiple.
- [ ] Soportan herencia múltiple.
- [ ] Solo pueden tener un número establecido de propiedades.
- [ ] Solo pueden tener un número establecido de métodos.

[Documentación oficial: Herencia de clases](https://docs.microsoft.com/en-us/dotnet/csharp/fundamentals/types/classes#class-inheritance)

#### Q49. ¿Qué función realizan los namespaces?

- [ ] Los namespaces calculan la cobertura de código en tiempo de ejecución.
- [ ] Los namespaces compilan el código de aplicación juntos en tiempo de compilación.
- [ ] Los namespaces agrupan código juntos en un solo repositorio.
- [x] Los namespaces separan código en agrupaciones, controlan el acceso y evitan colisiones de nombres.

[Documentación oficial: namespace](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/namespace)

#### Q50. ¿Cuál es la forma correcta de escribir una propiedad pública con un campo de respaldo privado?

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

[Documentación oficial: Usando Propiedades](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/using-properties)

#### Q51. ¿Qué es un thread pool?

- [ ] una colección de métodos síncronos creados durante la inicialización que no pueden ser reutilizados
- [x] una colección de hilos creados durante la inicialización que pueden ser reutilizados
- [ ] una colección de hilos solo reconocidos en tiempo de compilación que pueden ser reutilizados
- [ ] una colección de métodos asíncronos creados en tiempo de compilación que no pueden ser reutilizados

[Documentación oficial: Clase ThreadPool](https://docs.microsoft.com/en-us/dotnet/api/system.threading.threadpool?view=net-5.0)

#### Q52. Cuando un objeto en C# es serializado, ¿en qué se convierte?

- [ ] XML
- [ ] JSON
- [x] flujo de bytes
- [ ] flujo de valores

[Documentación oficial: Serialización](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/serialization/)

#### Q53. ¿Qué es un delegate?

- [ ] una variable que mantiene una referencia a un tipo de valor y su contenido
- [ ] un tipo de valor específico que solo puede ser usado en métodos callback
- [x] un tipo que mantiene una referencia a un método con una lista de parámetros particular y tipo de retorno
- [ ] un tipo de variable personalizado que puede ser usado en clases abstractas

[Documentación oficial: Delegates](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/delegates/)

#### Q54. ¿Cuáles son las cuatro palabras clave asociadas con el manejo de excepciones en C#?

- [ ] try, catch, valid, invalid
- [ ] try, valid, finally, throw
- [x] try, catch, finally, throw
- [ ] finally, throw, valid, invalid

[Tutorial Point](https://www.tutorialspoint.com/csharp/csharp_exception_handling.htm#:~:text=Exceptions%20provide%20a%20way%20to,catch%2C%20finally%2C%20and%20throw.)

#### Q55. ¿Cuál es la diferencia principal entre los operadores is y as?

- [ ] El operador is verifica tipos de instancia, mientras que el operador as verifica el tipo heredado.
- [ ] El operador is verifica tipos de datos primitivos, mientras que el operador as verifica el tipo de objeto.
- [ ] El operador as verifica el tipo de objeto, mientras que el operador is intenta hacer cast de un objeto a un tipo específico.
- [x] El operador is verifica el tipo de objeto, mientras que el operador as intenta hacer cast de un objeto a un tipo específico.

[Guía Pluralsight](https://www.pluralsight.com/guides/csharp-is-as-operators-is-expressions)

#### Q56. ¿Cuál es la diferencia entre los bloques finally y finalize?

- [ ] El bloque finally es llamado durante la ejecución de un bloque try y catch, mientras que el método finalize es llamado después de la recolección de basura.
- [x] El bloque finally es llamado después de la ejecución de un bloque try y catch, mientras que el método finalize es llamado justo antes de la recolección de basura.
- [ ] El bloque finalize es llamado antes de la ejecución de un bloque try y catch, mientras que el método finally es llamado justo antes de la recolección de basura.
- [ ] El bloque finalize es llamado durante la ejecución de un bloque try y catch, mientras que el método finally es llamado después de la recolección de basura.

[C-sharpcorner](https://www.c-sharpcorner.com/forums/final-finally-and-finalize)

#### Q57. Tu aplicación tiene un tipo de valor llamado username que necesita poder aceptar valores null, pero esto está generando errores de tiempo de compilación. ¿Cómo arreglarías esto en código?

- [ ] Null<string> username = null;
- [x] string? username = null;
- [ ] Type<string>? username = null;
- [ ] Optional<string> username = null;

#### Q58. ¿Qué fragmento de código declara correctamente una excepción personalizada llamada InvalidResponse?

- [ ] struct InvalidResponse: Exception {}
- [x] class InvalidResponse: Exception {}
- [ ] public Exception InvalidResponse = new Exception ();
- [ ] public Exception InvalidResponse () -> Exception;

[Documentación oficial: Excepciones](https://docs.microsoft.com/en-us/dotnet/standard/exceptions/how-to-create-user-defined-exceptions)

#### Q59. ¿Cómo escribirías una variable enum llamada AppState con valores para Offline, Loading, y Ready?

- [ ] enum AppState = [Offline, Loading, Ready]
- [ ] enum AppState {"Offline", "Loading", "Ready"}
- [ ] enum AppState = {Offline, Loading, Ready}
- [x] enum AppState {Offline, Loading, Ready}

[Documentación oficial: Enum](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/enum)

#### Q60. ¿Cuál es la diferencia principal entre un tipo de valor y un tipo de referencia?

- [ ] Un tipo de valor puede ser cualquier tipo primitivo, mientras que los tipos de referencia deben ser independientes del tipo.
- [ ] Un tipo de valor se refiere a otro valor, mientras que un tipo de referencia se refiere a un valor en memoria.
- [x] Un tipo de valor almacena un valor real, mientras que un tipo de referencia es un puntero a un valor.
- [ ] Un tipo de valor está disponible solo en tiempo de ejecución, mientras que un tipo de referencia está disponible solo en tiempo de compilación.

1. [Documentación oficial: Tipos de valor](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/value-types)
2. [Documentación oficial: Tipos de referencia](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/reference-types)

#### Q61. ¿Cuál es la diferencia entre las palabras clave `break` y `continue`?

- [ ] La palabra clave `break` se usa para salir de múltiples declaraciones de iteración, mientras que `continue` solo puede salir de bloques de código que tienen iteraciones únicas.
- [x] La palabra clave `break` literalmente sale de una declaración de flujo de control, mientras que `continue` ignora el resto de la declaración de control o iteración y comienza la siguiente.
- [ ] La palabra clave `break` literalmente sale del código de flujo de control actual y lo detiene completamente, mientras que `continue` sigue ejecutando el código después de que se lanza una excepción.
- [ ] La palabra clave `break` salta de una iteración y luego procede con el resto del código de flujo de control, mientras que `continue` detiene el código ejecutándose completamente.

[Documentación oficial: Declaraciones de salto](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/statements/jump-statements)

#### Q62. ¿Qué fragmento de código declara correctamente una variable llamada userId con un `get` público y `set` privado?

- [ ] `public int userID <get, set>;`
- [ ] `public int userID [get, private set];`
- [x] `public int userID { get; private set; }`
- [ ] `public int userID = { public get, private set };`

[Documentación oficial: Propiedades](https://docs.microsoft.com/en-us/dotnet/csharp/properties)

#### Q63. ¿Qué es verdadero sobre los métodos virtuales?

- [ ] `Sobrescribir métodos virtuales en una clase derivada es obligatorio.`
- [ ] `Sobrescribir métodos virtuales en una clase derivada no es posible.`
- [x] `Los métodos virtuales siempre necesitan una implementación por defecto.`
- [ ] `Los métodos virtuales no pueden tener una implementación por defecto.`

1. [Documentación oficial: virtual](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/virtual)
2. [c-sharpcorner: Método Virtual en C#](https://www.c-sharpcorner.com/UploadFile/3d39b4/virtual-method-in-C-Sharp/)

#### Q64. ¿Qué es probable que pase si tienes múltiples hilos accediendo al mismo recurso en tu programa?

- [ ] `sobrecarga de recursos`
- [ ] `salto de hilos`
- [x] `deadlock y condiciones de carrera`
- [ ] `nada, ya que esto es para lo que sirve el threading`

[Documentación oficial: condiciones de carrera](https://docs.microsoft.com/en-us/archive/msdn-magazine/2008/october/concurrency-hazards-solving-problems-in-your-multithreaded-code)

#### Q65. ¿Cómo indicas que una cadena puede ser null?

- [ ] `Una cadena no puede ser nullable.`
- [x] `string? myVariable`
- [ ] `string myVariable = null`
- [ ] `string(null) myVariable`

[Documentación oficial: tipos de valor nullable](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/nullable-value-types#declaration-and-assignment)

#### Q66. ¿Necesitas declarar una variable out antes de usarla?

- [x] `No, puedes declarar un out en la lista de parámetros.`
- [ ] `No, las variables Out ya no son parte de C#.`
- [ ] `Debes declararla si es un tipo primitivo.`
- [ ] `Sí.`

#### Q67. ¿Cómo accederías a las últimas dos personas en un array llamado People?

- [x] `People[..^2]`
- [ ] `No puedes hacer esto en C#.`
- [ ] `People[..^3]`
- [ ] `People[^2]`

Explicación: **Puedes** hacer esto en C#. Sin embargo, ninguna de las respuestas anteriores es correcta. Puedes acceder a los últimos dos elementos usando `People[^2..]`. Por favor, consulta [issue #3354](https://github.com/Ebazhanov/linkedin-skill-assessments-quizzes/issues/3354) para más información.
Ver también: [Documentación Oficial: Rangos](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/proposals/csharp-8.0/ranges)

#### Q68. ¿Cuándo se pueden crear tipos anónimos?

- [x] `en tiempo de compilación`
- [ ] `después del tiempo de ejecución`
- [ ] `en tiempo de ejecución`
- [ ] `después del tiempo de compilación`

[C-sharpcorner: Tipos Anónimos](https://www.c-sharpcorner.com/UploadFile/ff2f08/anonymous-types-in-C-Sharp/)

#### Q69. ¿Qué es verdadero sobre la multitarea de hilos?

- [x] `La multitarea de hilos permite que el código se ejecute concurrentemente`
- [ ] `La multitarea de hilos permite que el código se ejecute solo cuando se maneja un evento de usuario.`
- [ ] `La multitarea de hilos bloquea el código para que no se ejecute simultáneamente para proteger la memoria.`
- [ ] `La multitarea de hilos suma bloques de código de un solo hilo.`

[Documentación Oficial: Hilos](https://docs.microsoft.com/en-us/dotnet/standard/threading/threads-and-threading)

#### Q70. ¿Qué nivel de accesibilidad tiene este campo de clase?

`private string LastName;`

- [x] Puede ser usado por otro código solo en la misma clase o struct.
- [ ] Puede ser usado por otro código en un ensamblado referenciado.
- [ ] Puede ser usado solo por código contenido en una clase derivada.
- [ ] Puede ser usado por otro código en el mismo ensamblado.

[Documentación Oficial: Niveles de Accesibilidad](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/accessibility-levels)

#### Q71. ¿Cómo declararías correctamente un array dentado llamado 'partyInvites' con 10 elementos vacíos?

- [ ] `string[] partyInvites = new string[10];`
- [x] `string[][] partyInvites = new string[10][];`
- [ ] `string[][] partyInvites = new string[10]();`
- [ ] `string <[]> partyInvites = new string <[10]>;`

[Documentación Oficial: Arrays Dentados](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/arrays/jagged-arrays)

#### Q72. ¿Cómo podrías pausar un hilo por tres segundos?

- [ ] Thread.Pause(3000);
- [ ] Thread.Resume(-3000);
- [ ] Thread.Suspend(3000);
- [x] Thread.Sleep(3000);

[Referencia](https://docs.microsoft.com/en-us/dotnet/api/system.threading.thread.sleep?view=net-6.0)

#### Q73. ¿Qué está mal con este código?

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

- [ ] La variable c nunca se usa; mostrarla en la consola no cuenta como uso.
- [ ] Las variables a y b nunca se usan.
- [ ] No puedes colocar código dentro de corchetes dentro de otro bloque.
- [x] La variable c ya no existe fuera del bloque.

[Referencia](https://stackoverflow.com/a/6136865)

#### Q74. ¿Cuál declaración es verdadera?

- [ ] Todas son verdaderas.
- [ ] Ninguna es verdadera.
- [ ] string es un tipo de valor.
- [x] string es un alias para String

[Referencia](https://stackoverflow.com/q/7074)

#### Q75. ¿Cómo devolverías más de un valor desde un método?

- [x] Usa una tupla o una variable out.
- [ ] La única forma es usar una variable out.
- [ ] La única forma es usar una tupla.
- [ ] Esto no se puede hacer

#### Q76. ¿Cuál es un ejemplo válido de una clase derivada?

- [ ] `public class PremiumUser sub User {}`
- [x] `public class PremiumUser: User {}`
- [ ] `public class PremiumUser -> sub User {}`
- [ ] `public class User: PremiumUser {}`

#### Q77. ¿Cuál es la forma correcta de llamar a un método estático llamado DebugString desde una clase estática llamada InputManager?

- [ ] `static InputManager.DebugString();`
- [ ] `InputManager().DebugString;`
- [ ] `new InputManager().DebugString();`
- [x] `InputManager.DebugString();`

#### Q78. ¿Qué valores se pueden asignar a esta variable?

```cs
public string? nickname
```

- [ ] null
- [ ] Valores String
- [x] Valores String o null
- [ ] Valores String con más de un carácter

#### Q79. ¿Qué es un destructor?

- [ ] `un método especial llamado automáticamente cada vez que se crea o actualiza un objeto`
- [ ] `un método implícito llamado automáticamente cuando se procesan grupos de hilos concurrentemente`
- [ ] `un método explícito llamado automáticamente cuando el compilador comienza a ejecutarse`
- [x] `un método especial llamado automáticamente cada vez que se elimina o destruye un objeto`

[Referencia](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/destructors)

#### Q80. ¿Qué fragmento de código declara correctamente un alias de tipo CustomInt de tipo Int32?

- [ ] `typealias CustomInt = System.Int32;`
- [ ] `var<T> CustomInt = Int32;`
- [x] `using CustomInt = System.Int32;`
- [ ] `type CustomInt = System<Int32>;`

[Referencia](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/using-directive)

#### Q81. ¿Qué es un tipo de enumeración?

- [ ] `un objeto de tipo de paso por referencia`
- [ ] `un tipo de valor que no puede contener constantes`
- [x] `conjunto de constantes integrales con nombre`
- [ ] `un objeto de tipo de paso por valor`

#### Q82. ¿Para qué se usa la palabra clave readonly en las declaraciones de campo?

- [ ] `para declarar una variable miembro que no se puede calcular en tiempo de ejecución`
- [x] `para declarar un campo cuyo valor se puede asignar solo antes de que salga el constructor`
- [ ] `para declarar una variable estática que debe establecerse en tiempo de compilación`
- [ ] `para declarar una variable estática que debe establecerse en tiempo de ejecución`

#### Q83. ¿Cuál declaración es verdadera sobre los métodos de C#?

- [ ] `Los métodos almacenan variables.`
- [x] `Los métodos son acciones que un objeto puede realizar`
- [ ] `Un método se puede usar solo una vez por archivo C#.`
- [ ] `Un método determina el estado de una propiedad dada.`

[Documentación oficial: Métodos (Guía de Programación C#)](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/methods)

#### Q84 ¿Cuál es una clase de Excepción integrada válida de C#?

- [ ] `ArgumentNullValue`
- [ ] `InvalidFormatFoundException`
- [ ] `IndexOutOfPocket`
- [x] `ArgumentNullException`

[Documentación oficial: Clase ArgumentNullException](https://docs.microsoft.com/en-us/dotnet/api/system.argumentnullexception?view=net-5.0)

#### Q85. ¿Cuál es el propósito de una interfaz en C#?

- [ ] Las interfaces se usan para almacenar datos.
- [x] Las interfaces definen un contrato que las clases deben cumplir, especificando un conjunto de métodos y propiedades que las clases implementadoras deben proporcionar.
- [ ] Las interfaces se usan para crear instancias de clases.
- [ ] Las interfaces se usan para organización de código.

[Documentación Oficial: Interfaces (Guía de Programación C#)](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/interfaces/)

#### Q86. ¿Cuál es el propósito principal del bloque `finally` en una declaración try-catch-finally de C#?

- [ ] El bloque `finally` se usa para manejar excepciones.
- [ ] El bloque `finally` se usa para definir la lógica principal de la declaración try-catch.
- [ ] El bloque `finally` es opcional y no es requerido en las declaraciones try-catch.
- [x] El bloque `finally` se usa para asegurar que cierto código se ejecute independientemente de si ocurre una excepción.

[Documentación Oficial: try-catch (Referencia C#)](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/try-catch)

#### Q87. ¿Qué estructura de datos en C# te permite almacenar pares clave-valor y se usa frecuentemente para recuperación rápida de datos?

- [ ] ArrayList
- [ ] List
- [ ] Array
- [x] Dictionary

[Documentación Oficial: Clase Dictionary<TKey, TValue>](https://docs.microsoft.com/en-us/dotnet/api/system.collections.generic.dictionary-2)

#### Q88 ¿La ejecución del programa comienza con?

- [x] Main()
- [ ] Get()
- [ ] Class()
- [ ] Display()

[Referencia]: https://www.gkseries.com/c-sharp-programming/multiple-choice-questions-and-answers

#### Q89 En C# 'using' es un?

- [ ] Clase
- [x] Directiva
- [ ] Función
- [ ] Palabra clave

[Referencia]: https://www.gkseries.com/c-sharp-programming/multiple-choice-questions-and-answers
