## C#

#### Q1. In quale di queste situazioni le interfacce sono migliori delle classi astratte?

- [ ] Quando devi definire le caratteristiche di un tipo di oggetto, usa un'interfaccia. Quando devi definire le capacità di un tipo di oggetto, usa una classe astratta.
- [ ] Le interfacce sono un retaggio delle versioni più vecchie di C# e sono intercambiabili con la più recente funzionalità di classe astratta.
- [x] Quando hai bisogno di un elenco di capacità e dati che sono indipendenti dalle classi, usa un'interfaccia. Quando hai bisogno che un certo tipo di oggetto condivida caratteristiche, usa una classe astratta.
- [ ] Dovresti usare sia un'interfaccia che una classe astratta quando definisci qualsiasi oggetto complesso.

#### Q2. Quale affermazione è vera per i delegate?

- [ ] I delegate non sono supportati nella versione corrente di C#
- [ ] Non possono essere usati come callback.
- [ ] Solo le variabili possono essere passate ai delegate come parametri.
- [x] Possono essere concatenati insieme.

[Documentazione ufficiale: Delegates](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/delegates/#delegates-overview)

#### Q3. Quale scelta definisce meglio il modello di programmazione asincrona di C#?

- [ ] reattivo
- [ ] callback ereditato
- [x] basato su task
- [ ] basato su callback

[Documentazione ufficiale: Task asynchronous programming model](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/async/task-asynchronous-programming-model) risposta corretta --> var contacts = new List<string>();

#### Q4. Come determineresti se una classe ha un attributo particolare?

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

1. [Documentazione ufficiale: Attribute Class](https://docs.microsoft.com/en-us/dotnet/api/system.attribute?view=net-5.0)
2. [Documentazione ufficiale: Attribute.GetCustomAttribute Method](https://docs.microsoft.com/en-us/dotnet/api/system.attribute.getcustomattribute?view=net-5.0)

#### Q5. Qual è la differenza tra le parole chiave ref e out?

- [ ] Le variabili passate a out specificano che il parametro è un parametro di output, mentre ref specifica che una variabile può essere passata a una funzione senza essere inizializzata.
- [ ] Le variabili passate a ref possono essere passate a una funzione senza essere inizializzate, mentre out specifica che il valore è un valore di riferimento che può essere modificato all'interno del metodo chiamante.
- [x] Le variabili passate a out possono essere passate a una funzione senza essere inizializzate, mentre ref specifica che il valore è un valore di riferimento che può essere modificato all'interno del metodo chiamante.
- [ ] Le variabili passate a ref specificano che il parametro è un parametro di output, mentre out specifica che una variabile può essere passata a una funzione senza essere inizializzata.

1. [Documentazione ufficiale: ref](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/ref)
2. [Documentazione ufficiale: out parameter modifier](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/out-parameter-modifier)

#### Q6. Come potresti recuperare informazioni su una classe e creare un'istanza a runtime?

- [x] reflection
- [ ] serialization
- [ ] abstraction
- [ ] dependency injection

[Documentazione ufficiale: Reflection ](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/reflection)

#### Q7. Di cosa è un esempio questo codice?

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

- [ ] una classe privata che usa multithreading
- [ ] codifica multithread
- [ ] gestione errata dei thread
- [x] un potenziale deadlock

[Documentazione ufficiale: Deadlocks and race conditions](https://docs.microsoft.com/en-us/dotnet/standard/threading/managed-threading-best-practices#deadlocks-and-race-conditions)

#### Q8. Qual è la differenza tra un tipo anonimo e un tipo di dati regolare?

- [x] I tipi anonimi non hanno nomi di tipo
- [ ] I tipi anonimi possono essere solo statici
- [ ] I tipi anonimi possono essere usati solo negli struct
- [ ] I tipi anonimi non funzionano con LINQ.

[Documentazione ufficiale: Anonymous Types](https://docs.microsoft.com/en-us/dotnet/csharp/fundamentals/types/anonymous-types)

#### Q9. Quando useresti un Dictionary piuttosto che un tipo Array nella tua applicazione?

- [ ] Quando hai bisogno di una struttura di collezione irregolare
- [ ] Quando hai bisogno di memorizzare valori dello stesso tipo
- [x] Quando hai bisogno di memorizzare coppie chiave-valore piuttosto che valori singoli
- [ ] Quando hai bisogno di un elenco ordinato e ricercabile

[Documentazione ufficiale: Dictionary<TKey,TValue> Class](https://docs.microsoft.com/en-us/dotnet/api/system.collections.generic.dictionary-2?view=net-5.0)

#### Q10. Qual è la differenza tra a.Equals(b) e a == b?

- [ ] Il metodo .Equals confronta le identità di riferimento mentre `==` confronta i contenuti.
- [ ] Il metodo .Equals confronta i valori primitivi mentre `==` confronta tutti i valori.
- [x] Il metodo .Equals confronta i contenuti mentre `==` confronta l'identità di riferimento.
- [ ] Il metodo .Equals confronta i tipi di riferimento mentre `==` confronta i tipi di valore primitivi

1. [Documentazione ufficiale: Object.Equals](https://docs.microsoft.com/en-us/dotnet/api/system.object.equals)
2. [c-sharpcorner: Equality Operator(==) vs .Equals()](https://www.c-sharpcorner.com/UploadFile/3d39b4/difference-between-operator-and-equals-method-in-C-Sharp)

#### Q11. Quale scelta descrive meglio una situazione di deadlock?

- [ ] quando provi a istanziare due oggetti contemporaneamente nella stessa classe o struct
- [ ] quando stai cercando di eseguire un'azione dopo che un evento utente è registrato
- [x] quando le istruzioni simultanee si aspettano l'una dall'altra di finire prima di eseguire
- [ ] quando provi a eseguire una serie di eventi simultaneamente su più thread

[Documentazione ufficiale: Deadlocks and race conditions](https://docs.microsoft.com/en-us/dotnet/standard/threading/managed-threading-best-practices#deadlocks-and-race-conditions)

#### Q12. Come funziona la parola chiave async?

- [ ] Consente l'accesso ai metodi asincroni nell'API di C#
- [ ] Consente il pooling dei thread e i processi sincroni nelle classi statiche.
- [x] Consente l'uso della parola chiave await in un metodo
- [ ] Consente l'accesso ai metodi sincroni nell'API di C#

[Documentazione ufficiale: async](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/async)

#### Q13. Cos'è un oggetto in C#?

- [ ] una classe o struct, incluse le sue variabili e funzioni
- [ ] un tipo di dati primitivo che può essere creato solo al momento della compilazione
- [ ] un tipo di valore che può essere usato solo con una classe astratta
- [x] un'istanza di una classe o struct che include campi, proprietà e/o metodi

[Documentazione ufficiale: Objects](https://docs.microsoft.com/en-us/dotnet/csharp/fundamentals/object-oriented/objects)

#### Q14. Quale frammento di codice dichiara un tipo anonimo chiamato userData?

- [ ] `var<<!---->T> userData = new <<!---->T> { name = "John", age = 32 };`
- [x] `var userData = new { name = "John", age = 32 };`
- [ ] `AType userData = new AType { name = "John", age = 32 };`
- [ ] `Anonymous<T> userData = new Anonymous<T> { name = "John", age = 32 };`

[Documentazione ufficiale: Anonymous Types](https://docs.microsoft.com/en-us/dotnet/csharp/fundamentals/types/anonymous-types)

#### Q15. Cosa verrà restituito quando questo metodo viene eseguito?

`public void userInput(string charParameters) { }`

- [x] Niente
- [ ] un Boolean
- [ ] una variabile stringa
- [ ] un intero

[Documentazione ufficiale: void](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/void)

#### Q16. In che ordine verrebbero stampati i nomi dei dipendenti in questo esempio nella console?

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
- [ ] non ordinato
- [ ] discendente
- [ ] first in, first out

[dotnetpattern: LINQ OrderBy Operator](http://dotnetpattern.com/linq-orderby-operator)

#### Q17. Le espressioni lambda sono spesso usate in tandem con quale delle seguenti?

- [ ] Namespaces
- [x] LINQ
- [ ] Type Aliasing
- [ ] Assemblies

[Documentazione ufficiale: Language Integrated Query (LINQ) Overview](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/linq/)

#### Q18. Qual è la formattazione corretta per i commenti su singola riga e multiriga?

- [ ] `/_/ - Single Line`
      `/_ - Multiline`
- [ ] `// Multiline`
      `/_ Single Line _/`
- [ ] `//\* Multiline`
      `/ Single Line`
- [x] `// Single Line`
      `/* Multiline */`

[w3schools: C# Comments](https://www.w3schools.com/cs/cs_comments.php)

#### Q19. Come rendi un metodo in una classe astratta sovrascrivibile?

- [ ] Rendilo pubblico
- [ ] Rendilo statico
- [ ] Rendilo privato
- [x] Rendilo virtuale

1. [Documentazione ufficiale: virtual](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/virtual)
2. [Documentazione ufficiale: abstract](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/abstract)

#### Q20. Come scriveresti il codice per una proprietà intera chiamata Age con getter e setter?

- [ ] public int Age { get - set }
- [ ] public int Age: get set;
- [ ] public int Age (get, set );
- [x] public int Age { get; set; }

[Documentazione ufficiale: Using Properties](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/using-properties)

#### Q21. Cos'è una classe astratta?

- [ ] una classe che è denotata dalla parola chiave class (può essere vista e usata da qualsiasi altra classe nel sistema--quindi è per default pubblica)
- [ ] qualcosa denotato dalla parola chiave abstract e usato a livello di sistema; se vuoi che qualsiasi programma crei un oggetto di una classe usi la classe astratta
- [ ] una classe che è denotata dalla parola chiave virtual
- [x] una classe che può essere usata solo come classe base

[Documentazione ufficiale: Abstract and Sealed Classes and Class Members](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/abstract-and-sealed-classes-and-class-members)

#### Q22. Quando si usa un thread pool cosa succede a un dato thread dopo che finisce il suo compito?

- [ ] Il thread viene distrutto e la memoria viene liberata.
- [ ] Il thread gira in un loop fino al prossimo incarico.
- [ ] Il thread diventa inattivo in background e aspetta la garbage collection.
- [x] Il thread ritorna al pool per il riutilizzo.

[Documentazione ufficiale: Thread pool characteristics](https://docs.microsoft.com/en-us/dotnet/standard/threading/the-managed-thread-pool#thread-pool-characteristics)

#### Q23. Quale scelta rappresenta una classe che eredita comportamento da una classe base?

- [ ] una seconda classe base
- [ ] una classe rivista
- [x] una classe derivata
- [ ] una classe padre

[Documentazione ufficiale: Inheritance](https://docs.microsoft.com/en-us/dotnet/csharp/fundamentals/object-oriented/inheritance)

#### Q24. Cosa ti permette di fare l'overloading degli operatori?

- [ ] nascondere gli operatori built-in quando necessario
- [ ] aggiungere metodi da interpretare dal compilatore a runtime
- [ ] definire come funzionano gli enum e altri tipi di valore primitivi all'interno del resto dell'applicazione
- [x] definire funzionalità personalizzate per operatori comuni come addizione e uguaglianza

[Documentazione ufficiale: Operator overloading](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/operators/operator-overloading)

#### Q25. Qual è lo scopo principale di LINQ?

- [ ] eliminare dati duplicati
- [ ] collegare namespace e assembly
- [x] interrogare e trasformare dati
- [ ] connettere assembly

[Documentazione ufficiale: Language Integrated Query (LINQ) Overview](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/linq/#query-expression-overview)

#### Q26. Qual è la sintassi corretta per una nuova lista generica di stringhe chiamata contacts?

- [ ] public List<string names> contacts = new List<string names>();
- [ ] public List(string names) contacts = new List(string names)();
- [x] var contacts = new List<string>();
- [ ] var contacts = new List(string);

[Documentazione ufficiale: List<T> Class](https://docs.microsoft.com/en-us/dotnet/api/system.collections.generic.list-1?view=net-5.0)

#### Q27. Qual è la differenza tra throw exceptions e throw clauses?

- [ ] Le throw clauses si attivano solo a runtime, mentre le throw exceptions possono attivarsi in qualsiasi momento.
- [x] Le throw exceptions sovrascrivono lo stack trace, mentre le throw clauses mantengono le informazioni dello stack.
- [ ] Le throw clauses sovrascrivono lo stack trace, mentre le throw exceptions mantengono le informazioni dello stack.
- [ ] Le throw exceptions si attivano solo a runtime, mentre le throw clauses possono attivarsi durante la compilazione.

1. [Documentazione ufficiale: throw](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/throw)
2. [c-sharpcorner: Difference Between Throw Exception and Throw Clause](https://www.c-sharpcorner.com/UploadFile/akkiraju/difference-between-throw-exception-and-throw-clause/)

#### Q28. Quando un metodo asincrono viene eseguito, il codice gira ma non succede niente tranne un avviso del compilatore. Qual è la causa più probabile per cui il metodo non restituisce niente?

- [ ] L'istruzione return yield manca alla fine del metodo.
- [x] Il metodo manca di una parola chiave await nel suo corpo.
- [ ] La parola chiave wait manca dalla fine del metodo.
- [ ] La parola chiave yield manca dal metodo.

[Documentazione ufficiale: Starting tasks concurrently](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/async/#start-tasks-concurrently)

#### Q29. Cosa sono gli eventi C#?

- [ ] azioni di sistema che comunicano direttamente con il compilatore a runtime
- [ ] azioni che si eseguono quando il codice compila, generando log e output di test
- [x] azioni che generano notifiche, che vengono inviate ai loro listener registrati
- [ ] metodi solo per utenti che inviano dati al backend dell'applicazione

[Documentazione ufficiale: Introduction to events](https://docs.microsoft.com/en-us/dotnet/csharp/events-overview)

#### Q30. Che tipo di valori possono memorizzare gli array?

- [ ] collezioni non ordinate di valori numerici
- [ ] coppie chiave-valore di qualsiasi tipo supportato da C#
- [ ] istanze di classi e struct
- [x] variabili multiple, o collezioni, dello stesso tipo

[Documentazione ufficiale: Arrays](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/arrays/)

#### Q31. Dato questo enumeration, come accederesti al valore di tipo intero di 'AppState.Loading'?

`enum AppState { OffLine, Loading, Ready }`

- [ ] string currentState = (string)AppState.Loading;
- [ ] string currentState = AppState.Loading.integralVal;
- [ ] int currentState = AppState.Loading.rawValue;
- [x] int currentState = (int)AppState.Loading;

[Documentazione ufficiale: Enumeration types](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/enum#conversions)

#### Q32. Quale carattere useresti per iniziare un pattern di espressione regolare a un confine di parola?

- [ ] d
- [ ] \a
- [x] \b
- [ ] \w

1. [regular-expressions: Word Boundaries](https://www.regular-expressions.info/wordboundaries.html)
2. [Documentazione ufficiale: Regular Expression Language - Quick Reference](https://docs.microsoft.com/en-us/dotnet/standard/base-types/regular-expression-language-quick-reference)

#### Q33. Per conformarsi alla seguente interfaccia, quali dei suoi membri devono essere implementati?

```cs
public interface INameable
{
    string FirstName { get; set; }
    string LastName { get; }
}
```

- [x] Entrambe le proprietà FirstName e LastName devono essere implementate.
- [ ] Nessuna, sono entrambe opzionali.
- [ ] Solo la proprietà LastName deve essere implementata.
- [ ] Solo la proprietà FirstName deve essere implementata.

[Documentazione ufficiale: interface](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/interface)

#### Q34. Stai gestendo più assembly nel tuo programma, ma sei preoccupato per l'allocazione della memoria. A che punto nel ciclo di vita del programma gli assembly vengono caricati in memoria?

- [ ] a runtime
- [ ] al momento della compilazione
- [x] solo quando richiesto
- [ ] solo quando caricati programmaticamente

1. [Documentazione ufficiale: Assembly Loading](https://docs.microsoft.com/en-us/dotnet/framework/deployment/best-practices-for-assembly-loading)
2. [Stackoverflow: When exactly are assemblies loaded?](https://stackoverflow.com/questions/21914692/when-exactly-are-assemblies-loaded)

#### Q35. Qual è la descrizione più accurata di un'espressione regolare?

- [ ] Un'espressione regolare è uno strumento C# usato per analizzare HTML
- [x] Un'espressione regolare è una stringa di testo speciale per descrivere un pattern di ricerca.
- [ ] Un'espressione regolare permette a una variabile di essere passata per riferimento.
- [ ] Un'espressione regolare permette a una classe di conformarsi al protocollo Equatable.

1. [Documentazione ufficiale: Regular Expression Language - Quick Reference](https://docs.microsoft.com/en-us/dotnet/standard/base-types/regular-expression-language-quick-reference)
2. [Documentazione ufficiale: .NET regular expressions](https://docs.microsoft.com/en-us/dotnet/standard/base-types/regular-expressions)

#### Q36. Perché useresti un campo di classe in C#?

- [ ] Per definire i comportamenti della classe
- [x] Per contenere informazioni e dati contenuti nell'oggetto classe
- [ ] Per comunicare tra classi e oggetti
- [ ] Per memorizzare il valore di definizione della classe

[Documentazione ufficiale: Introduction to classes](https://docs.microsoft.com/en-us/dotnet/csharp/fundamentals/types/classes)

#### Q37. Quando useresti i generics nel tuo codice?

- [ ] per aumentare le prestazioni del codice
- [x] tutte queste risposte
- [ ] quando il riutilizzo del codice è una priorità
- [ ] quando la type safety è importante

[Documentazione ufficiale: Generic classes and methods](https://docs.microsoft.com/en-us/dotnet/csharp/fundamentals/types/generics)

#### Q38. Cosa viene stampato nella console quando questo codice viene eseguito?

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
- [x] un errore, perché la firma del metodo Login non corrisponde al delegate
- [ ] Login successful... Valid user!

1. [Documentazione ufficiale: Introduction to Delegates](https://docs.microsoft.com/en-us/dotnet/csharp/delegates-overview)
2. [Documentazione ufficiale: Introduction to Events](https://docs.microsoft.com/en-us/dotnet/csharp/events-overview)

#### Q39. Come dichiareresti una classe sealed chiamata User?

- [ ] public class User {}
- [ ] abstract User {}
- [x] sealed class User {}
- [ ] private sealed class User {}

[Documentazione ufficiale: Abstract and Sealed Classes and Class Members](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/abstract-and-sealed-classes-and-class-members)

#### Q40. Qual è la differenza tra classi non-static e static?

- [x] le classi non-static devono essere inizializzate prima dell'uso, mentre le classi static non lo fanno
- [ ] le classi non-static sono accessibili solo da un'interfaccia mentre le classi static sono accessibili da ovunque
- [ ] le classi non-static devono inizializzare tutti i membri della classe a runtime, mentre le classi static non lo fanno
- [ ] le classi non-static non devono essere inizializzate mentre le classi static sì

1. [stackoverflow](https://stackoverflow.com/questions/20451554/whats-the-function-of-a-static-constructor-in-a-non-static-class)
2. [Documentazione ufficiale: Static Constructors](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/static-constructors)

#### Q41. Quale caratteristica impedisce a questo codice di compilare?

`public int age="28"`

- [x] type safety
- [ ] single inheritance
- [ ] dependency injection
- [ ] multiple inheritance

[c-sharpcorner: Type Safety in .NET](https://www.c-sharpcorner.com/UploadFile/vikie4u/type-safety-in-net/)

#### Q42. Come serializzeresti questa classe?

`public class User {}`

- [ ] Contrassegna la classe User con `DeserializableAttribute`.
- [ ] Dichiara la classe come `public serializable class User {}`.
- [x] Contrassegna la classe User con l'attributo `SerializableAttribute`.
- [ ] Dichiara la classe come `private serializable class User {}`.

[Documentazione ufficiale: SerializableAttribute Class](https://docs.microsoft.com/en-us/dotnet/api/system.serializableattribute?view=net-5.0)

#### Q43. Come scriveresti un delegate chiamato ResultCallback con un parametro int chiamato responseCode?

- [ ] public delegate ResultCallback(int responseCode);
- [ ] public delegate void ResultCallback<(int) responseCode>;
- [ ] public void delegate ResultCallback\<int responseCode\>;
- [x] public delegate void ResultCallback(int responseCode);

[Documentazione ufficiale: Delegates](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/delegates/)

#### Q44. Qual è la differenza tra un metodo static e non-static?

- [ ] i metodi non-static devono sempre avere un tipo di ritorno void
- [ ] i metodi non-static non hanno accesso alle variabili membro static
- [x] i metodi static non devono istanziare un'istanza della classe per chiamare il metodo
- [ ] i metodi static devono sempre essere pubblici

[Documentazione ufficiale: Static Members](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/static-classes-and-static-class-members#static-members)

#### Q45. Qual è il modo corretto di scrivere un evento chiamato apiResult basato su un delegate chiamato ResultCallback?

- [ ] public void event ResultCallback apiResult;
- [ ] public event ResultCallback(() -> apiResult);
- [ ] public event void ResultCallback
- [x] public event ResultCallback apiResult;

[Documentazione ufficiale: Introduction to events](https://docs.microsoft.com/en-us/dotnet/csharp/events-overview)

#### Q46. Quando verrà eseguito il codice all'interno del blocco finally in un'istruzione try-catch?

- [ ] se c'è un errore, non verrà eseguito affatto
- [ ] tra i blocchi try e catch
- [x] dopo i blocchi try e catch
- [ ] quando il blocco finally sovrascrive il blocco catch ed esegue al suo posto

[Documentazione ufficiale: try-catch](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/try-catch)

#### Q47. Quale metodo estende correttamente la classe string?

- [x] public static string IsvalidName(this string i, string value) {}
- [ ] public static void IsvalidName(this string i, string value) {}
- [ ] public string IsvalidName(this string i, string value) {}
- [ ] public void IsvalidName(this string i, string value) {}

#### Q48. Come sono limitate le classi C#?

- [x] Non supportano l'ereditarietà multipla.
- [ ] Supportano l'ereditarietà multipla.
- [ ] Possono avere solo un numero fisso di proprietà.
- [ ] Possono avere solo un numero fisso di metodi.

[Documentazione ufficiale: Class inheritance](https://docs.microsoft.com/en-us/dotnet/csharp/fundamentals/types/classes#class-inheritance)

#### Q49. Che funzione svolgono i namespace?

- [ ] I namespace calcolano la copertura del codice a runtime.
- [ ] I namespace compilano insieme il codice dell'applicazione al momento della compilazione.
- [ ] I namespace raggruppano il codice insieme in un singolo repository.
- [x] I namespace separano il codice in raggruppamenti, controllano l'accesso ed evitano collisioni di nomi.

[Documentazione ufficiale: namespace](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/namespace)

#### Q50. Qual è il modo corretto di scrivere una proprietà pubblica con un campo di supporto privato?

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

[Documentazione ufficiale: Using Properties](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/using-properties)

#### Q51. Cos'è un thread pool?

- [ ] una collezione di metodi sincroni creati durante l'inizializzazione che non possono essere riutilizzati
- [x] una collezione di thread creati durante l'inizializzazione che possono essere riutilizzati
- [ ] una collezione di thread riconosciuti solo al momento della compilazione che possono essere riutilizzati
- [ ] una collezione di metodi asincroni creati al momento della compilazione che non possono essere riutilizzati

[Documentazione ufficiale: ThreadPool Class](https://docs.microsoft.com/en-us/dotnet/api/system.threading.threadpool?view=net-5.0)

#### Q52. Quando un oggetto in C# viene serializzato, in cosa viene convertito?

- [ ] XML
- [ ] JSON
- [x] byte stream
- [ ] value stream

[Documentazione ufficiale: Serialization](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/serialization/)

#### Q53. Cos'è un delegate?

- [ ] una variabile che contiene un riferimento a un tipo di valore e al suo contenuto
- [ ] un tipo di valore specifico che può essere usato solo nei metodi callback
- [x] un tipo che contiene un riferimento a un metodo con una particolare lista di parametri e tipo di ritorno
- [ ] un tipo di variabile personalizzato che può essere usato nelle classi astratte

[Documentazione ufficiale: Delegates](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/delegates/)

#### Q54. Quali sono le quattro parole chiave associate alla gestione delle eccezioni in C#?

- [ ] try, catch, valid, invalid
- [ ] try, valid, finally, throw
- [x] try, catch, finally, throw
- [ ] finally, throw, valid, invalid

[Tutorial Point](https://www.tutorialspoint.com/csharp/csharp_exception_handling.htm#:~:text=Exceptions%20provide%20a%20way%20to,catch%2C%20finally%2C%20and%20throw.)

#### Q55. Qual è la differenza principale tra gli operatori is e as?

- [ ] L'operatore is controlla i tipi di istanza, mentre l'operatore as controlla il tipo ereditato.
- [ ] L'operatore is controlla i tipi di dati primitivi, mentre l'operatore as controlla il tipo di oggetto.
- [ ] L'operatore as controlla il tipo di oggetto, mentre l'operatore is tenta di fare il cast di un oggetto a un tipo specifico.
- [x] L'operatore is controlla il tipo di oggetto, mentre l'operatore as tenta di fare il cast di un oggetto a un tipo specifico.

[Pluralsight guide](https://www.pluralsight.com/guides/csharp-is-as-operators-is-expressions)

#### Q56. Qual è la differenza tra i blocchi finally e finalize?

- [ ] Il blocco finally viene chiamato durante l'esecuzione di un blocco try e catch, mentre il metodo finalize viene chiamato dopo la garbage collection.
- [x] Il blocco finally viene chiamato dopo l'esecuzione di un blocco try e catch, mentre il metodo finalize viene chiamato appena prima della garbage collection.
- [ ] Il blocco finalize viene chiamato prima dell'esecuzione di un blocco try e catch, mentre il metodo finally viene chiamato appena prima della garbage collection.
- [ ] Il blocco finalize viene chiamato durante l'esecuzione di un blocco try e catch, mentre il metodo finally viene chiamato dopo la garbage collection.

[C-sharpcorner](https://www.c-sharpcorner.com/forums/final-finally-and-finalize)

#### Q57. La tua applicazione ha un tipo di valore chiamato username che deve essere in grado di accettare valori null, ma questo sta generando errori di compilazione. Come risolveresti questo nel codice?

- [ ] Null<string> username = null;
- [x] string? username = null;
- [ ] Type<string>? username = null;
- [ ] Optional<string> username = null;

#### Q58. Quale frammento di codice dichiara correttamente un'eccezione personalizzata chiamata InvalidResponse?

- [ ] struct InvalidResponse: Exception {}
- [x] class InvalidResponse: Exception {}
- [ ] public Exception InvalidResponse = new Exception ();
- [ ] public Exception InvalidResponse () -> Exception;

[Documentazione ufficiale: Exceptions](https://docs.microsoft.com/en-us/dotnet/standard/exceptions/how-to-create-user-defined-exceptions)

#### Q59. Come scriveresti una variabile enum chiamata AppState con valori per Offline, Loading e Ready?

- [ ] enum AppState = [Offline, Loading, Ready]
- [ ] enum AppState {"Offline", "Loading", "Ready"}
- [ ] enum AppState = {Offline, Loading, Ready}
- [x] enum AppState {Offline, Loading, Ready}

[Documentazione ufficiale: Enum](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/enum)

#### Q60. Qual è la principale differenza tra un tipo valore e un tipo riferimento?

- [ ] Un tipo valore può essere qualsiasi tipo primitivo, mentre i tipi riferimento devono essere agnostici al tipo.
- [ ] Un tipo valore si riferisce a un altro valore, mentre un tipo riferimento si riferisce a un valore in memoria.
- [x] Un tipo valore memorizza un valore effettivo, mentre un tipo riferimento è un puntatore a un valore.
- [ ] Un tipo valore è disponibile solo a runtime, mentre un tipo riferimento è disponibile solo a tempo di compilazione.

1. [Documentazione ufficiale: Tipi valore](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/value-types)
2. [Documentazione ufficiale: Tipi riferimento](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/reference-types)

#### Q61. Qual è la differenza tra le parole chiave `break` e `continue`?

- [ ] La parola chiave `break` viene utilizzata per uscire da più istruzioni di iterazione, mentre `continue` può uscire solo da blocchi di codice che hanno iterazioni singole.
- [x] La parola chiave `break` esce letteralmente da un'istruzione di controllo del flusso, mentre `continue` ignora il resto dell'istruzione di controllo o iterazione e inizia la successiva.
- [ ] La parola chiave `break` esce letteralmente dal codice di controllo del flusso corrente e lo ferma completamente, mentre `continue` continua a eseguire il codice dopo che viene lanciata un'eccezione.
- [ ] La parola chiave `break` salta fuori da un'iterazione e poi procede con il resto del codice di controllo del flusso, mentre `continue` ferma completamente il codice in esecuzione.

[Documentazione ufficiale: Istruzioni di salto](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/statements/jump-statements)

#### Q62. Quale frammento di codice dichiara correttamente una variabile chiamata userId con un `get` pubblico e un `set` privato?

- [ ] `public int userID <get, set>;`
- [ ] `public int userID [get, private set];`
- [x] `public int userID { get; private set; }`
- [ ] `public int userID = { public get, private set };`

[Documentazione ufficiale: Proprietà](https://docs.microsoft.com/en-us/dotnet/csharp/properties)

#### Q63. Cosa è vero sui metodi virtuali?

- [ ] `L'override dei metodi virtuali in una classe derivata è obbligatorio.`
- [ ] `L'override dei metodi virtuali in una classe derivata non è possibile.`
- [x] `I metodi virtuali hanno sempre bisogno di un'implementazione predefinita.`
- [ ] `I metodi virtuali non possono avere un'implementazione predefinita.`

1. [Documentazione ufficiale: virtual](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/virtual)
2. [c-sharpcorner: Metodo Virtuale in C#](https://www.c-sharpcorner.com/UploadFile/3d39b4/virtual-method-in-C-Sharp/)

#### Q64. Cosa è probabile che accada se hai più thread che accedono alla stessa risorsa nel tuo programma?

- [ ] `sovraccarico della risorsa`
- [ ] `salto del thread`
- [x] `deadlock e condizioni di race`
- [ ] `niente, dato che questo è lo scopo del threading`

[Documentazione ufficiale: condizioni di race](https://docs.microsoft.com/en-us/archive/msdn-magazine/2008/october/concurrency-hazards-solving-problems-in-your-multithreaded-code)

#### Q65. Come indichi che una stringa potrebbe essere null?

- [ ] `Una stringa non può essere nullable.`
- [x] `string? myVariable`
- [ ] `string myVariable = null`
- [ ] `string(null) myVariable`

[Documentazione ufficiale: tipi valore nullable](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/nullable-value-types#declaration-and-assignment)

#### Q66. Devi dichiarare una variabile out prima di usarla?

- [x] `No, puoi dichiarare un out nella lista dei parametri.`
- [ ] `No, le variabili Out non fanno più parte di C#.`
- [ ] `Devi dichiararla se è un tipo primitivo.`
- [ ] `Sì.`

#### Q67. Come accederesti alle ultime due persone in un array chiamato People?

- [x] `People[..^2]`
- [ ] `Non puoi fare questo in C#.`
- [ ] `People[..^3]`
- [ ] `People[^2]`

Spiegazione: Puoi fare questo in C#. Tuttavia, nessuna delle risposte sopra è corretta. Puoi accedere agli ultimi due elementi usando `People[^2..]`. Vedi [issue #3354](https://github.com/Ebazhanov/linkedin-skill-assessments-quizzes/issues/3354) per maggiori informazioni.
Vedi anche: [Documentazione Ufficiale: Range](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/proposals/csharp-8.0/ranges)

#### Q68. Quando possono essere creati i tipi anonimi?

- [x] `a tempo di compilazione`
- [ ] `dopo il runtime`
- [ ] `a runtime`
- [ ] `dopo il tempo di compilazione`

[C-sharpcorner: Tipi Anonimi](https://www.c-sharpcorner.com/UploadFile/ff2f08/anonymous-types-in-C-Sharp/)

#### Q69. Cosa è vero sul multitasking dei thread?

- [x] `Il multitasking dei thread consente al codice di essere eseguito concorrentemente`
- [ ] `Il multitasking dei thread consente al codice di essere eseguito solo quando si gestisce un evento utente.`
- [ ] `Il multitasking dei thread blocca il codice dall'essere eseguito simultaneamente per proteggere la memoria.`
- [ ] `Il multitasking dei thread aggiunge insieme blocchi di codice single-threaded.`

[Documentazione Ufficiale: Thread](https://docs.microsoft.com/en-us/dotnet/standard/threading/threads-and-threading)

#### Q70. Che livello di accessibilità ha questo campo di classe?

`private string LastName;`

- [x] Può essere utilizzato da altro codice solo nella stessa classe o struct.
- [ ] Può essere utilizzato da altro codice in un assembly referenziato.
- [ ] Può essere utilizzato solo dal codice contenuto in una classe derivata.
- [ ] Può essere utilizzato da altro codice nello stesso assembly.

[Documentazione Ufficiale: Livelli di Accessibilità](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/accessibility-levels)

#### Q71. Come dichiareresti correttamente un array jagged chiamato 'partyInvites' con 10 elementi vuoti?

- [ ] `string[] partyInvites = new string[10];`
- [x] `string[][] partyInvites = new string[10][];`
- [ ] `string[][] partyInvites = new string[10]();`
- [ ] `string <[]> partyInvites = new string <[10]>;`

[Documentazione Ufficiale: Array Jagged](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/arrays/jagged-arrays)

#### Q72. Come potresti mettere in pausa un thread per tre secondi?

- [ ] Thread.Pause(3000);
- [ ] Thread.Resume(-3000);
- [ ] Thread.Suspend(3000);
- [x] Thread.Sleep(3000);

[Riferimento](https://docs.microsoft.com/en-us/dotnet/api/system.threading.thread.sleep?view=net-6.0)

#### Q73. Cosa c'è di sbagliato in questo codice?

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

- [ ] La variabile c non viene mai utilizzata; visualizzarla sulla console non conta come utilizzo.
- [ ] Le variabili a e b non vengono mai utilizzate.
- [ ] Non puoi posizionare codice tra parentesi graffe all'interno di un altro blocco.
- [x] La variabile c non esiste più fuori dal blocco.

[Riferimento](https://stackoverflow.com/a/6136865)

#### Q74. Quale affermazione è Vera?

- [ ] Tutte sono vere.
- [ ] Nessuna è vera.
- [ ] string è un tipo valore.
- [x] string è un alias per String

[Riferimento](https://stackoverflow.com/q/7074)

#### Q75. Come restituiresti più di un valore da un metodo?

- [x] Usa una tupla o una variabile out.
- [ ] L'unico modo è usare una variabile out.
- [ ] L'unico modo è usare una tupla.
- [ ] Questo non può essere fatto

#### Q76. Quale è un esempio valido di classe derivata?

- [ ] `public class PremiumUser sub User {}`
- [x] `public class PremiumUser: User {}`
- [ ] `public class PremiumUser -> sub User {}`
- [ ] `public class User: PremiumUser {}`

#### Q77. Qual è il modo corretto per chiamare un metodo statico chiamato DebugString da una classe statica chiamata InputManager?

- [ ] `static InputManager.DebugString();`
- [ ] `InputManager().DebugString;`
- [ ] `new InputManager().DebugString();`
- [x] `InputManager.DebugString();`

#### Q78. Quali valori possono essere assegnati a questa variabile?

```cs
public string? nickname
```

- [ ] null
- [ ] Valori String
- [x] Valori String o null
- [ ] Valori String con più di un carattere

#### Q79. Cos'è un distruttore?

- [ ] `un metodo speciale chiamato automaticamente ogni volta che un oggetto viene creato o aggiornato`
- [ ] `un metodo implicito chiamato automaticamente quando i thread pool vengono processati concorrentemente`
- [ ] `un metodo esplicito chiamato automaticamente quando il compilatore inizia a funzionare`
- [x] `un metodo speciale chiamato automaticamente ogni volta che un oggetto viene eliminato o distrutto`

[Riferimento](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/destructors)

#### Q80. Quale frammento di codice dichiara correttamente un alias di tipo CustomInt di tipo Int32?

- [ ] `typealias CustomInt = System.Int32;`
- [ ] `var<T> CustomInt = Int32;`
- [x] `using CustomInt = System.Int32;`
- [ ] `type CustomInt = System<Int32>;`

[Riferimento](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/using-directive)

#### Q81. Cos'è un tipo enumerazione?

- [ ] `un oggetto di tipo pass by reference`
- [ ] `un tipo valore che non può contenere costanti`
- [x] `insieme di costanti integrali nominate`
- [ ] `un oggetto di tipo pass-by-value`

#### Q82. A cosa serve la parola chiave readonly nelle dichiarazioni di campo?

- [ ] `per dichiarare una variabile membro che non può essere calcolata a runtime`
- [x] `per dichiarare un campo il cui valore può essere assegnato solo prima che il costruttore esca`
- [ ] `per dichiarare una variabile statica che deve essere impostata a tempo di compilazione`
- [ ] `per dichiarare una variabile statica che deve essere impostata a runtime`

#### Q83. Quale affermazione è vera sui metodi C#?

- [ ] `I metodi memorizzano variabili.`
- [x] `I metodi sono azioni che un oggetto può compiere`
- [ ] `Un metodo può essere utilizzato solo una volta per file C#.`
- [ ] `Un metodo determina lo stato di una data proprietà.`

[Documentazione ufficiale: Metodi (Guida alla programmazione C#)](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/methods)

#### Q84 Quale è una classe Exception built-in valida di C#?

- [ ] `ArgumentNullValue`
- [ ] `InvalidFormatFoundException`
- [ ] `IndexOutOfPocket`
- [x] `ArgumentNullException`

[Documentazione ufficiale: Classe ArgumentNullException](https://docs.microsoft.com/en-us/dotnet/api/system.argumentnullexception?view=net-5.0)

#### Q85. Qual è lo scopo di un'interfaccia in C#?

- [ ] Le interfacce vengono utilizzate per memorizzare dati.
- [x] Le interfacce definiscono un contratto che le classi devono rispettare, specificando un insieme di metodi e proprietà che le classi implementanti devono fornire.
- [ ] Le interfacce vengono utilizzate per creare istanze di classi.
- [ ] Le interfacce vengono utilizzate per l'organizzazione del codice.

[Documentazione Ufficiale: Interfacce (Guida alla programmazione C#)](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/interfaces/)

#### Q86. Qual è lo scopo principale del blocco `finally` in un'istruzione try-catch-finally di C#?

- [ ] Il blocco `finally` viene utilizzato per gestire le eccezioni.
- [ ] Il blocco `finally` viene utilizzato per definire la logica principale dell'istruzione try-catch.
- [ ] Il blocco `finally` è opzionale e non richiesto nelle istruzioni try-catch.
- [x] Il blocco `finally` viene utilizzato per garantire che un determinato codice venga eseguito indipendentemente dal fatto che si verifichi un'eccezione.

[Documentazione Ufficiale: try-catch (Riferimento C#)](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/try-catch)

#### Q87. Quale struttura dati in C# ti consente di memorizzare coppie chiave-valore ed è spesso utilizzata per il recupero rapido dei dati?

- [ ] ArrayList
- [ ] List
- [ ] Array
- [x] Dictionary

[Documentazione Ufficiale: Classe Dictionary<TKey, TValue>](https://docs.microsoft.com/en-us/dotnet/api/system.collections.generic.dictionary-2)

#### Q88 L'esecuzione del programma inizia con?

- [x] Main()
- [ ] Get()
- [ ] Class()
- [ ] Display()

[Riferimento]: https://www.gkseries.com/c-sharp-programming/multiple-choice-questions-and-answers

#### Q89 In C# 'using' è un?

- [ ] Classe
- [x] Direttiva
- [ ] Funzione
- [ ] Parola chiave

[Riferimento]: https://www.gkseries.com/c-sharp-programming/multiple-choice-questions-and-answers
