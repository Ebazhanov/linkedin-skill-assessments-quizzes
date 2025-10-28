## C#

#### Q1. Dans laquelle de ces situations les interfaces sont-elles meilleures que les classes abstraites ?

- [ ] Quand vous devez définir les caractéristiques d'un type d'objet, utilisez une interface. Quand vous devez définir les capacités d'un type d'objet, utilisez une classe abstraite.
- [ ] Les interfaces sont un héritage des versions antérieures de C#, et sont interchangeables avec la fonctionnalité plus récente de classe abstraite.
- [x] Quand vous avez besoin d'une liste de capacités et de données qui sont agnostiques aux classes, utilisez une interface. Quand vous avez besoin qu'un certain type d'objet partage des caractéristiques, utilisez une classe abstraite.
- [ ] Vous devriez utiliser à la fois une interface et une classe abstraite lors de la définition de tout objet complexe.

#### Q2. Quelle affirmation est vraie concernant les délégués ?

- [ ] Les délégués ne sont pas supportés dans la version actuelle de C#
- [ ] Ils ne peuvent pas être utilisés comme callbacks.
- [ ] Seules les variables peuvent être passées aux délégués comme paramètres.
- [x] Ils peuvent être chaînés ensemble.

[Documentation officielle : Délégués](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/delegates/#delegates-overview)

#### Q3. Quel choix définit le mieux le modèle de programmation asynchrone de C# ?

- [ ] réactif
- [ ] callback hérité
- [x] basé sur les tâches
- [ ] basé sur les callbacks

[Documentation officielle : Modèle de programmation asynchrone basé sur les tâches](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/async/task-asynchronous-programming-model) réponse correcte --> var contacts = new List<string>();

#### Q4. Comment détermineriez-vous si une classe a un attribut particulier ?

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

1. [Documentation officielle : Classe Attribute](https://docs.microsoft.com/en-us/dotnet/api/system.attribute?view=net-5.0)
2. [Documentation officielle : Méthode Attribute.GetCustomAttribute](https://docs.microsoft.com/en-us/dotnet/api/system.attribute.getcustomattribute?view=net-5.0)

#### Q5. Quelle est la différence entre les mots-clés ref et out ?

- [ ] Les variables passées à out spécifient que le paramètre est un paramètre de sortie, tandis que ref spécifie qu'une variable peut être passée à une fonction sans être initialisée.
- [ ] Les variables passées à ref peuvent être passées à une fonction sans être initialisées, tandis que out spécifie que la valeur est une valeur de référence qui peut être modifiée à l'intérieur de la méthode appelante.
- [x] Les variables passées à out peuvent être passées à une fonction sans être initialisées, tandis que ref spécifie que la valeur est une valeur de référence qui peut être modifiée à l'intérieur de la méthode appelante.
- [ ] Les variables passées à ref spécifient que le paramètre est un paramètre de sortie, tandis que out spécifie qu'une variable peut être passée à une fonction sans être initialisée.

1. [Documentation officielle : ref](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/ref)
2. [Documentation officielle : modificateur de paramètre out](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/out-parameter-modifier)

#### Q6. Comment pourriez-vous récupérer des informations sur une classe, ainsi que créer une instance à l'exécution ?

- [x] réflexion
- [ ] sérialisation
- [ ] abstraction
- [ ] injection de dépendance

[Documentation officielle : Réflexion](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/reflection)

#### Q7. De quoi ce code est-il un exemple ?

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

- [ ] une classe privée qui utilise le multithreading
- [ ] codage multithread
- [ ] mauvaise gestion des threads
- [x] un interblocage potentiel

[Documentation officielle : Interblocages et conditions de course](https://docs.microsoft.com/en-us/dotnet/standard/threading/managed-threading-best-practices#deadlocks-and-race-conditions)

#### Q8. Quelle est la différence entre un type anonyme et un type de données régulier ?

- [x] Les types anonymes n'ont pas de noms de type
- [ ] Les types anonymes ne peuvent être que statiques
- [ ] Les types anonymes ne peuvent être utilisés que dans les structs
- [ ] Les types anonymes ne fonctionnent pas avec LINQ.

[Documentation officielle : Types anonymes](https://docs.microsoft.com/en-us/dotnet/csharp/fundamentals/types/anonymous-types)

#### Q9. Quand utiliseriez-vous un Dictionary plutôt qu'un type Array dans votre application ?

- [ ] Quand vous avez besoin d'une structure de collection en escalier
- [ ] Quand vous devez stocker des valeurs du même type
- [x] Quand vous devez stocker des paires clé-valeur plutôt que des valeurs uniques
- [ ] Quand vous avez besoin d'une liste ordonnée et consultable

[Documentation officielle : Classe Dictionary<TKey,TValue>](https://docs.microsoft.com/en-us/dotnet/api/system.collections.generic.dictionary-2?view=net-5.0)

#### Q10. Quelle est la différence entre a.Equals(b) et a == b ?

- [ ] La méthode .Equals compare les identités de référence tandis que `==` compare le contenu.
- [ ] La méthode .Equals compare les valeurs primitives tandis que `==` compare toutes les valeurs.
- [x] La méthode .Equals compare le contenu tandis que `==` compare l'identité de référence.
- [ ] La méthode .Equals compare les types de référence tandis que `==` compare les types de valeur primitifs

1. [Documentation officielle : Object.Equals](https://docs.microsoft.com/en-us/dotnet/api/system.object.equals)
2. [c-sharpcorner : Opérateur d'égalité(==) vs .Equals()](https://www.c-sharpcorner.com/UploadFile/3d39b4/difference-between-operator-and-equals-method-in-C-Sharp)

#### Q11. Quel choix décrit le mieux une situation d'interblocage ?

- [ ] quand vous essayez d'instancier deux objets en même temps dans la même classe ou struct
- [ ] quand vous essayez d'exécuter une action après qu'un événement utilisateur soit enregistré
- [x] quand des instructions simultanées attendent que l'autre se termine avant d'exécuter
- [ ] quand vous essayez d'exécuter une série d'événements simultanément sur plusieurs threads

[Documentation officielle : Interblocages et conditions de course](https://docs.microsoft.com/en-us/dotnet/standard/threading/managed-threading-best-practices#deadlocks-and-race-conditions)

#### Q12. Comment fonctionne le mot-clé async ?

- [ ] Il permet l'accès aux méthodes asynchrones dans l'API C#
- [ ] Il permet le pooling de threads et les processus synchrones dans les classes statiques.
- [x] Il permet au mot-clé await d'être utilisé dans une méthode
- [ ] Il permet l'accès aux méthodes synchrones dans l'API C#

[Documentation officielle : async](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/async)

#### Q13. Qu'est-ce qu'un objet en C# ?

- [ ] une classe ou struct, y compris ses variables et fonctions
- [ ] un type de données primitif qui ne peut être créé qu'au moment de la compilation
- [ ] un type de valeur qui ne peut être utilisé qu'avec une classe abstraite
- [x] une instance d'une classe ou struct qui inclut des champs, des propriétés et/ou des méthodes

[Documentation officielle : Objets](https://docs.microsoft.com/en-us/dotnet/csharp/fundamentals/object-oriented/objects)

#### Q14. Quel extrait de code déclare un type anonyme nommé userData ?

- [ ] `var<<!---->T> userData = new <<!---->T> { name = "John", age = 32 };`
- [x] `var userData = new { name = "John", age = 32 };`
- [ ] `AType userData = new AType { name = "John", age = 32 };`
- [ ] `Anonymous<T> userData = new Anonymous<T> { name = "John", age = 32 };`

[Documentation officielle : Types anonymes](https://docs.microsoft.com/en-us/dotnet/csharp/fundamentals/types/anonymous-types)

#### Q15. Que sera retourné quand cette méthode est exécutée ?

`public void userInput(string charParameters) { }`

- [x] Rien
- [ ] un Boolean
- [ ] une variable string
- [ ] un entier

[Documentation officielle : void](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/void)

#### Q16. Dans quel ordre les noms d'employés dans cet exemple seraient-ils imprimés dans la console ?

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

- [x] croissant
- [ ] non ordonné
- [ ] décroissant
- [ ] premier entré, premier sorti

[dotnetpattern : Opérateur LINQ OrderBy](http://dotnetpattern.com/linq-orderby-operator)

#### Q17. Les expressions lambda sont souvent utilisées en tandem avec lequel des éléments suivants ?

- [ ] Espaces de noms
- [x] LINQ
- [ ] Alias de type
- [ ] Assemblies

[Documentation officielle : Vue d'ensemble de Language Integrated Query (LINQ)](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/linq/)

#### Q18. Quel est le formatage correct pour les commentaires sur une ligne et sur plusieurs lignes ?

- [ ] `/_/ - Une ligne`
      `/_ - Multiligne`
- [ ] `// Multiligne`
      `/_ Une ligne _/`
- [ ] `//\* Multiligne`
      `/ Une ligne`
- [x] `// Une ligne`
      `/* Multiligne */`

[w3schools : Commentaires C#](https://www.w3schools.com/cs/cs_comments.php)

#### Q19. Comment rendez-vous une méthode dans une classe abstraite surchargeable ?

- [ ] Rendez-la publique
- [ ] Rendez-la statique
- [ ] Rendez-la privée
- [x] Rendez-la virtuelle

1. [Documentation officielle : virtual](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/virtual)
2. [Documentation officielle : abstract](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/abstract)

#### Q20. Comment écririez-vous le code pour une propriété entière appelée Age avec un getter et un setter ?

- [ ] public int Age { get - set }
- [ ] public int Age: get set;
- [ ] public int Age (get, set );
- [x] public int Age { get; set; }

[Documentation officielle : Utilisation des propriétés](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/using-properties)

#### Q21. Qu'est-ce qu'une classe abstraite ?

- [ ] une classe qui est désignée par le mot-clé class (peut être vue et utilisée par toute autre classe du système--ainsi elle est par défaut publique)
- [ ] quelque chose désigné par le mot-clé abstract et utilisé à l'échelle du système ; si vous voulez qu'un programme crée un objet d'une classe, vous utilisez la classe abstraite
- [ ] une classe qui est désignée par le mot-clé virtual
- [x] une classe qui ne peut être utilisée que comme classe de base

[Documentation officielle : Classes et membres de classe abstraits et sealed](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/abstract-and-sealed-classes-and-class-members)

#### Q22. Quand on utilise un pool de threads, que se passe-t-il avec un thread donné après qu'il ait terminé sa tâche ?

- [ ] Le thread est détruit et la mémoire est libérée.
- [ ] Le thread s'exécute en boucle jusqu'à la prochaine assignation.
- [ ] Le thread devient inactif en arrière-plan et attend la collecte des ordures.
- [x] Le thread retourne au pool pour réutilisation.

[Documentation officielle : Caractéristiques du pool de threads](https://docs.microsoft.com/en-us/dotnet/standard/threading/the-managed-thread-pool#thread-pool-characteristics)

#### Q23. Quel choix représente une classe qui hérite du comportement d'une classe de base ?

- [ ] une deuxième classe de base
- [ ] une classe révisée
- [x] une classe dérivée
- [ ] une classe parent

[Documentation officielle : Héritage](https://docs.microsoft.com/en-us/dotnet/csharp/fundamentals/object-oriented/inheritance)

#### Q24. Que permet de faire la surcharge d'opérateur ?

- [ ] masquer les opérateurs intégrés quand nécessaire
- [ ] ajouter des méthodes à interpréter par le compilateur à l'exécution
- [ ] définir comment les enums et autres types de valeur primitifs fonctionnent dans le reste de l'application
- [x] définir une fonctionnalité personnalisée pour les opérateurs communs comme l'addition et l'égalité

[Documentation officielle : Surcharge d'opérateur](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/operators/operator-overloading)

#### Q25. Quel est le but principal de LINQ ?

- [ ] supprimer les données dupliquées
- [ ] lier les espaces de noms et les assemblies
- [x] interroger et transformer les données
- [ ] connecter les assemblies

[Documentation officielle : Vue d'ensemble de Language Integrated Query (LINQ)](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/linq/#query-expression-overview)

#### Q26. Quelle est la syntaxe correcte pour une nouvelle liste générique de strings nommée contacts ?

- [ ] public List<string names> contacts = new List<string names>();
- [ ] public List(string names) contacts = new List(string names)();
- [x] var contacts = new List<string>();
- [ ] var contacts = new List(string);

[Documentation officielle : Classe List<T>](https://docs.microsoft.com/en-us/dotnet/api/system.collections.generic.list-1?view=net-5.0)

#### Q27. Quelle est la différence entre throw exceptions et throw clauses ?

- [ ] Les throw clauses ne se déclenchent qu'à l'exécution, tandis que les throw exceptions peuvent se déclencher à tout moment.
- [x] Les throw exceptions écrasent la trace de pile, tandis que les throw clauses conservent les informations de pile.
- [ ] Les throw clauses écrasent la trace de pile, tandis que les throw exceptions conservent les informations de pile.
- [ ] Les throw exceptions ne se déclenchent qu'à l'exécution, tandis que les throw clauses peuvent se déclencher pendant la compilation.

1. [Documentation officielle : throw](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/throw)
2. [c-sharpcorner : Différence entre Throw Exception et Throw Clause](https://www.c-sharpcorner.com/UploadFile/akkiraju/difference-between-throw-exception-and-throw-clause/)

#### Q28. Quand une méthode asynchrone est exécutée, le code s'exécute mais rien ne se passe à part un avertissement du compilateur. Qu'est-ce qui cause le plus probablement que la méthode ne retourne rien ?

- [ ] L'instruction return yield manque à la fin de la méthode.
- [x] La méthode manque d'un mot-clé await dans son corps.
- [ ] Le mot-clé wait manque à la fin de la méthode.
- [ ] Le mot-clé yield manque dans la méthode.

[Documentation officielle : Démarrer les tâches de manière concurrente](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/async/#start-tasks-concurrently)

#### Q29. Que sont les événements C# ?

- [ ] des actions système qui communiquent directement avec le compilateur à l'exécution
- [ ] des actions qui s'exécutent quand le code compile, générant des logs et des sorties de test
- [x] des actions qui génèrent des notifications, qui sont envoyées à leurs auditeurs enregistrés
- [ ] des méthodes utilisateur uniquement qui envoient des données au backend de l'application

[Documentation officielle : Introduction aux événements](https://docs.microsoft.com/en-us/dotnet/csharp/events-overview)

#### Q30. Quel type de valeurs les tableaux peuvent-ils stocker ?

- [ ] collections non ordonnées de valeurs numériques
- [ ] paires clé-valeur de tout type supporté par C#
- [ ] instances de classe et struct
- [x] variables multiples, ou collections, du même type

[Documentation officielle : Tableaux](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/arrays/)

#### Q31. Étant donné cette énumération, comment accéderiez-vous à la valeur de type entier de 'AppState.Loading' ?

`enum AppState { OffLine, Loading, Ready }`

- [ ] string currentState = (string)AppState.Loading;
- [ ] string currentState = AppState.Loading.integralVal;
- [ ] int currentState = AppState.Loading.rawValue;
- [x] int currentState = (int)AppState.Loading;

[Documentation officielle : Types d'énumération](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/enum#conversions)

#### Q32. Quel caractère utiliseriez-vous pour commencer un motif d'expression régulière à une limite de mot ?

- [ ] d
- [ ] \a
- [x] \b
- [ ] \w

1. [regular-expressions : Limites de mots](https://www.regular-expressions.info/wordboundaries.html)
2. [Documentation officielle : Référence rapide du langage d'expression régulière](https://docs.microsoft.com/en-us/dotnet/standard/base-types/regular-expression-language-quick-reference)

#### Q33. Pour se conformer à l'interface suivante, lesquels de ses membres doivent être implémentés ?

```cs
public interface INameable
{
    string FirstName { get; set; }
    string LastName { get; }
}
```

- [x] Les propriétés FirstName et LastName doivent toutes les deux être implémentées.
- [ ] Aucune, elles sont toutes les deux optionnelles.
- [ ] Seule la propriété LastName doit être implémentée.
- [ ] Seule la propriété FirstName doit être implémentée.

[Documentation officielle : interface](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/interface)

#### Q34. Vous traitez avec plusieurs assemblies dans votre programme, mais vous vous inquiétez de l'allocation mémoire. À quel moment du cycle de vie du programme les assemblies sont-elles chargées en mémoire ?

- [ ] à l'exécution
- [ ] au moment de la compilation
- [x] seulement quand requis
- [ ] seulement quand chargées par programmation

1. [Documentation officielle : Chargement d'assemblies](https://docs.microsoft.com/en-us/dotnet/framework/deployment/best-practices-for-assembly-loading)
2. [Stackoverflow : Quand exactement les assemblies sont-elles chargées ?](https://stackoverflow.com/questions/21914692/when-exactly-are-assemblies-loaded)

#### Q35. Quelle est la description la plus précise d'une expression régulière ?

- [ ] Une expression régulière est un outil C# utilisé pour analyser HTML
- [x] Une expression régulière est une chaîne de texte spéciale pour décrire un motif de recherche.
- [ ] Une expression régulière permet à une variable d'être passée par référence.
- [ ] Une expression régulière permet à une classe de se conformer au protocole Equatable.

1. [Documentation officielle : Référence rapide du langage d'expression régulière](https://docs.microsoft.com/en-us/dotnet/standard/base-types/regular-expression-language-quick-reference)
2. [Documentation officielle : Expressions régulières .NET](https://docs.microsoft.com/en-us/dotnet/standard/base-types/regular-expressions)

#### Q36. Pourquoi utiliseriez-vous un champ de classe en C# ?

- [ ] Pour définir les comportements de la classe
- [x] Pour contenir les informations et données contenues dans l'objet de classe
- [ ] Pour communiquer entre les classes et objets
- [ ] Pour stocker la valeur de définition de classe

[Documentation officielle : Introduction aux classes](https://docs.microsoft.com/en-us/dotnet/csharp/fundamentals/types/classes)

#### Q37. Quand utiliseriez-vous les génériques dans votre code ?

- [ ] pour augmenter les performances du code
- [x] toutes ces réponses
- [ ] quand la réutilisation du code est une priorité
- [ ] quand la sécurité des types est importante

[Documentation officielle : Classes et méthodes génériques](https://docs.microsoft.com/en-us/dotnet/csharp/fundamentals/types/generics)

#### Q38. Qu'est-ce qui s'imprime dans la console quand ce code est exécuté ?

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
- [x] une erreur, car la signature de méthode de Login ne correspond pas au délégué
- [ ] Login successful... Valid user!

1. [Documentation officielle : Introduction aux délégués](https://docs.microsoft.com/en-us/dotnet/csharp/delegates-overview)
2. [Documentation officielle : Introduction aux événements](https://docs.microsoft.com/en-us/dotnet/csharp/events-overview)

#### Q39. Comment déclareriez-vous une classe sealed nommée User ?

- [ ] public class User {}
- [ ] abstract User {}
- [x] sealed class User {}
- [ ] private sealed class User {}

[Documentation officielle : Classes et membres de classe abstraits et sealed](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/abstract-and-sealed-classes-and-class-members)

#### Q40. Quelle est la différence entre les classes non-statiques et statiques ?

- [x] les classes non-statiques doivent être initialisées avant utilisation, tandis que les classes statiques ne le font pas
- [ ] les classes non-statiques sont accessibles seulement depuis une interface tandis que les classes statiques sont accessibles depuis n'importe où
- [ ] les classes non-statiques doivent initialiser tous les membres de classe à l'exécution, tandis que les classes statiques ne le font pas
- [ ] les classes non-statiques n'ont pas besoin d'être initialisées tandis que les classes statiques le font

1. [stackoverflow](https://stackoverflow.com/questions/20451554/whats-the-function-of-a-static-constructor-in-a-non-static-class)
2. [Documentation officielle : Constructeurs statiques](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/static-constructors)

#### Q41. Quelle caractéristique empêche ce code de compiler ?

`public int age="28"`

- [x] sécurité des types
- [ ] héritage simple
- [ ] injection de dépendance
- [ ] héritage multiple

[c-sharpcorner : Sécurité des types dans .NET](https://www.c-sharpcorner.com/UploadFile/vikie4u/type-safety-in-net/)

#### Q42. Comment sérialiseriez-vous cette classe ?

`public class User {}`

- [ ] Marquez la classe User avec l'attribut `DeserializableAttribute`.
- [ ] Déclarez la classe comme `public serializable class User {}`.
- [x] Marquez la classe User avec l'attribut `SerializableAttribute`.
- [ ] Déclarez la classe comme `private serializable class User {}`.

[Documentation officielle : Classe SerializableAttribute](https://docs.microsoft.com/en-us/dotnet/api/system.serializableattribute?view=net-5.0)

#### Q43. Comment écririez-vous un délégué nommé ResultCallback avec un paramètre int nommé responseCode ?

- [ ] public delegate ResultCallback(int responseCode);
- [ ] public delegate void ResultCallback<(int) responseCode>;
- [ ] public void delegate ResultCallback\<int responseCode\>;
- [x] public delegate void ResultCallback(int responseCode);

[Documentation officielle : Délégués](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/delegates/)

#### Q44. Quelle est la différence entre une méthode statique et non-statique ?

- [ ] les méthodes non-statiques ont toujours besoin d'avoir un type de retour void
- [ ] les méthodes non-statiques n'ont pas accès aux variables membres statiques
- [x] les méthodes statiques n'ont pas besoin d'instancier une instance de la classe pour appeler la méthode
- [ ] les méthodes statiques doivent toujours être publiques

[Documentation officielle : Membres statiques](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/static-classes-and-static-class-members#static-members)

#### Q45. Quelle est la bonne façon d'écrire un événement nommé apiResult basé sur un délégué nommé ResultCallback ?

- [ ] public void event ResultCallback apiResult;
- [ ] public event ResultCallback(() -> apiResult);
- [ ] public event void ResultCallback
- [x] public event ResultCallback apiResult;

[Documentation officielle : Introduction aux événements](https://docs.microsoft.com/en-us/dotnet/csharp/events-overview)

#### Q46. Quand le code à l'intérieur du bloc finally sera-t-il exécuté dans une instruction try-catch ?

- [ ] s'il y a une erreur, il ne s'exécutera pas du tout
- [ ] entre les blocs try et catch
- [x] après les blocs try et catch
- [ ] quand le bloc finally remplace le bloc catch et s'exécute à sa place

[Documentation officielle : try-catch](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/try-catch)

#### Q47. Quelle méthode étend correctement la classe string ?

- [x] public static string IsvalidName(this string i, string value) {}
- [ ] public static void IsvalidName(this string i, string value) {}
- [ ] public string IsvalidName(this string i, string value) {}
- [ ] public void IsvalidName(this string i, string value) {}

#### Q48. Comment les classes C# sont-elles limitées ?

- [x] Elles ne supportent pas l'héritage multiple.
- [ ] Elles supportent l'héritage multiple.
- [ ] Elles ne peuvent avoir qu'un nombre défini de propriétés.
- [ ] Elles ne peuvent avoir qu'un nombre défini de méthodes.

[Documentation officielle : Héritage de classe](https://docs.microsoft.com/en-us/dotnet/csharp/fundamentals/types/classes#class-inheritance)

#### Q49. Quelle fonction les espaces de noms remplissent-ils ?

- [ ] Les espaces de noms calculent la couverture de code à l'exécution.
- [ ] Les espaces de noms compilent le code d'application ensemble au moment de la compilation.
- [ ] Les espaces de noms groupent le code ensemble dans un seul dépôt.
- [x] Les espaces de noms séparent le code en groupements, contrôlent l'accès et évitent les collisions de noms.

[Documentation officielle : namespace](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/namespace)

#### Q50. Quelle est la bonne façon d'écrire une propriété publique avec un champ de support privé ?

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

[Documentation officielle : Utilisation des propriétés](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/using-properties)

#### Q51. Qu'est-ce qu'un pool de threads ?

- [ ] une collection de méthodes synchrones créées pendant l'initialisation qui ne peuvent pas être réutilisées
- [x] une collection de threads créés pendant l'initialisation qui peuvent être réutilisés
- [ ] une collection de threads reconnus seulement au moment de la compilation qui peuvent être réutilisés
- [ ] une collection de méthodes asynchrones créées au moment de la compilation qui ne peuvent pas être réutilisées

[Documentation officielle : Classe ThreadPool](https://docs.microsoft.com/en-us/dotnet/api/system.threading.threadpool?view=net-5.0)

#### Q52. Quand un objet en C# est sérialisé, en quoi est-il converti ?

- [ ] XML
- [ ] JSON
- [x] flux d'octets
- [ ] flux de valeurs

[Documentation officielle : Sérialisation](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/serialization/)

#### Q53. Qu'est-ce qu'un délégué ?

- [ ] une variable qui contient une référence à un type de valeur et son contenu
- [ ] un type de valeur spécifique qui ne peut être utilisé que dans les méthodes de callback
- [x] un type qui contient une référence à une méthode avec une liste de paramètres et un type de retour particuliers
- [ ] un type de variable personnalisé qui peut être utilisé dans les classes abstraites

[Documentation officielle : Délégués](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/delegates/)

#### Q54. Quels sont les quatre mots-clés associés à la gestion d'exceptions en C# ?

- [ ] try, catch, valid, invalid
- [ ] try, valid, finally, throw
- [x] try, catch, finally, throw
- [ ] finally, throw, valid, invalid

[Tutorial Point](https://www.tutorialspoint.com/csharp/csharp_exception_handling.htm#:~:text=Exceptions%20provide%20a%20way%20to,catch%2C%20finally%2C%20and%20throw.)

#### Q55. Quelle est la principale différence entre les opérateurs is et as ?

- [ ] L'opérateur is vérifie les types d'instance, tandis que l'opérateur as vérifie le type hérité.
- [ ] L'opérateur is vérifie les types de données primitifs, tandis que l'opérateur as vérifie le type d'objet.
- [ ] L'opérateur as vérifie le type d'objet, tandis que l'opérateur is tente de caster un objet vers un type spécifique.
- [x] L'opérateur is vérifie le type d'objet, tandis que l'opérateur as tente de caster un objet vers un type spécifique.

[Guide Pluralsight](https://www.pluralsight.com/guides/csharp-is-as-operators-is-expressions)

#### Q56. Quelle est la différence entre les blocs finally et finalize ?

- [ ] Le bloc finally est appelé pendant l'exécution d'un bloc try et catch, tandis que la méthode finalize est appelée après le garbage collection.
- [x] Le bloc finally est appelé après l'exécution d'un bloc try et catch, tandis que la méthode finalize est appelée juste avant le garbage collection.
- [ ] Le bloc finalize est appelé avant l'exécution d'un bloc try et catch, tandis que la méthode finally est appelée juste avant le garbage collection.
- [ ] Le bloc finalize est appelé pendant l'exécution d'un bloc try et catch, tandis que la méthode finally est appelée après le garbage collection.

[C-sharpcorner](https://www.c-sharpcorner.com/forums/final-finally-and-finalize)

#### Q57. Votre application a un type de valeur appelé username qui doit pouvoir accepter des valeurs null, mais cela génère des erreurs de compilation. Comment corrigeriez-vous cela dans le code ?

- [ ] Null<string> username = null;
- [x] string? username = null;
- [ ] Type<string>? username = null;
- [ ] Optional<string> username = null;

#### Q58. Quel extrait de code déclare correctement une exception personnalisée nommée InvalidResponse ?

- [ ] struct InvalidResponse: Exception {}
- [x] class InvalidResponse: Exception {}
- [ ] public Exception InvalidResponse = new Exception ();
- [ ] public Exception InvalidResponse () -> Exception;

[Documentation officielle : Exceptions](https://docs.microsoft.com/en-us/dotnet/standard/exceptions/how-to-create-user-defined-exceptions)

#### Q59. Comment écririez-vous une variable enum appelée AppState avec des valeurs pour Offline, Loading, et Ready ?

- [ ] enum AppState = [Offline, Loading, Ready]
- [ ] enum AppState {"Offline", "Loading", "Ready"}
- [ ] enum AppState = {Offline, Loading, Ready}
- [x] enum AppState {Offline, Loading, Ready}

[Documentation officielle : Enum](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/enum)

#### Q60. Quelle est la principale différence entre un type de valeur et un type de référence ?

- [ ] Un type de valeur peut être n'importe quel type primitif, tandis que les types de référence doivent être agnostiques au type.
- [ ] Un type de valeur fait référence à une autre valeur, tandis qu'un type de référence fait référence à une valeur en mémoire.
- [x] Un type de valeur stocke une valeur réelle, tandis qu'un type de référence est un pointeur vers une valeur.
- [ ] Un type de valeur n'est disponible qu'au moment de l'exécution, tandis qu'un type de référence n'est disponible qu'au moment de la compilation.

1. [Documentation officielle : Types de valeur](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/value-types)
2. [Documentation officielle : Types de référence](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/reference-types)

#### Q61. Quelle est la différence entre les mots-clés `break` et `continue` ?

- [ ] Le mot-clé `break` est utilisé pour sortir de plusieurs instructions d'itération, tandis que `continue` ne peut sortir que des blocs de code qui ont des itérations simples.
- [x] Le mot-clé `break` sort littéralement d'une instruction de flux de contrôle, tandis que `continue` ignore le reste de l'instruction de contrôle ou de l'itération et commence la suivante.
- [ ] Le mot-clé `break` sort littéralement du code de flux de contrôle actuel et l'arrête complètement, tandis que `continue` continue d'exécuter le code après qu'une exception soit levée.
- [ ] Le mot-clé `break` sort d'une itération puis procède avec le reste du code de flux de contrôle, tandis que `continue` arrête le code en cours d'exécution complètement.

[Documentation officielle : Instructions de saut](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/statements/jump-statements)

#### Q62. Quel extrait de code déclare correctement une variable nommée userId avec un `get` public et un `set` privé ?

- [ ] `public int userID <get, set>;`
- [ ] `public int userID [get, private set];`
- [x] `public int userID { get; private set; }`
- [ ] `public int userID = { public get, private set };`

[Documentation officielle : Propriétés](https://docs.microsoft.com/en-us/dotnet/csharp/properties)

#### Q63. Qu'est-ce qui est vrai à propos des méthodes virtuelles ?

- [ ] `Overriding virtual methods in a derived class is mandatory.`
- [ ] `Overriding virtual methods in a derived class is not possible.`
- [x] `Virtual methods always need a default implementation.`
- [ ] `Virtual methods cannot have a default implementation.`

1. [Documentation officielle : virtual](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/virtual)
2. [c-sharpcorner: Virtual Method in C#](https://www.c-sharpcorner.com/UploadFile/3d39b4/virtual-method-in-C-Sharp/)

#### Q64. Que risque-t-il de se passer si vous avez plusieurs threads accédant à la même ressource dans votre programme ?

- [ ] `resource overload`
- [ ] `thread jumping`
- [x] `deadlock and race conditions`
- [ ] `nothing, since this is what threading is for`

[Documentation officielle : race conditions](https://docs.microsoft.com/en-us/archive/msdn-magazine/2008/october/concurrency-hazards-solving-problems-in-your-multithreaded-code)

#### Q65. Comment indiquez-vous qu'une chaîne peut être null ?

- [ ] `A string cannot be nullable.`
- [x] `string? myVariable`
- [ ] `string myVariable = null`
- [ ] `string(null) myVariable`

[Documentation officielle : types de valeur nullable](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/nullable-value-types#declaration-and-assignment)

#### Q66. Devez-vous déclarer une variable out avant de l'utiliser ?

- [x] `No, you can declare an out in the parameter list.`
- [ ] `No, Out variables are no longer part of C#.`
- [ ] `You must declare it if it is a primitive type.`
- [ ] `Yes.`

#### Q67. Comment accéderiez-vous aux deux dernières personnes dans un tableau nommé People ?

- [x] `People[..^2]`
- [ ] `You cannot do this in C#.`
- [ ] `People[..^3]`
- [ ] `People[^2]`

Explication : Vous **pouvez** faire cela en C#. Cependant, aucune des réponses ci-dessus n'est correcte. Vous pouvez accéder aux deux derniers éléments en utilisant `People[^2..]`. Veuillez consulter [issue #3354](https://github.com/Ebazhanov/linkedin-skill-assessments-quizzes/issues/3354) pour plus d'informations.
Voir aussi : [Documentation officielle : Ranges](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/proposals/csharp-8.0/ranges)

#### Q68. Quand les types anonymes peuvent-ils être créés ?

- [x] `at compile time`
- [ ] `after runtime`
- [ ] `at runtime`
- [ ] `after compile time`

[C-sharpcorner: Anonymous Types](https://www.c-sharpcorner.com/UploadFile/ff2f08/anonymous-types-in-C-Sharp/)

#### Q69. Qu'est-ce qui est vrai à propos du multitâche de threads ?

- [x] `Thread multitasking allows code to be executed concurrently`
- [ ] `Thread multitasking allows code to be executed only when handling a user event.`
- [ ] `Thread multitasking blocks code from being executed simultaneously to guard memory.`
- [ ] `Thread multitasking adds single-threaded code blocks together.`

[Documentation officielle : Threads](https://docs.microsoft.com/en-us/dotnet/standard/threading/threads-and-threading)

#### Q70. Quel niveau d'accessibilité ce champ de classe a-t-il ?

`private string LastName;`

- [x] Il peut être utilisé par d'autres codes uniquement dans la même classe ou structure.
- [ ] Il peut être utilisé par d'autres codes dans un assembly référencé.
- [ ] Il peut être utilisé uniquement par le code contenu dans une classe dérivée.
- [ ] Il peut être utilisé par d'autres codes dans le même assembly.

[Documentation officielle : Niveaux d'accessibilité](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/accessibility-levels)

#### Q71. Comment déclareriez-vous correctement un tableau en escalier appelé 'partyInvites' avec 10 éléments vides ?

- [ ] `string[] partyInvites = new string[10];`
- [x] `string[][] partyInvites = new string[10][];`
- [ ] `string[][] partyInvites = new string[10]();`
- [ ] `string <[]> partyInvites = new string <[10]>;`

[Documentation officielle : Tableaux en escalier](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/arrays/jagged-arrays)

#### Q72. Comment pourriez-vous mettre en pause un thread pendant trois secondes ?

- [ ] Thread.Pause(3000);
- [ ] Thread.Resume(-3000);
- [ ] Thread.Suspend(3000);
- [x] Thread.Sleep(3000);

[Référence](https://docs.microsoft.com/en-us/dotnet/api/system.threading.thread.sleep?view=net-6.0)

#### Q73. Qu'est-ce qui ne va pas avec ce code ?

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

- [ ] La variable c n'est jamais utilisée ; l'afficher sur la console ne compte pas comme utilisation.
- [ ] Les variables a et b ne sont jamais utilisées.
- [ ] Vous ne pouvez pas placer de code entre crochets à l'intérieur d'un autre bloc.
- [x] La variable c n'existe plus en dehors du bloc.

[Référence](https://stackoverflow.com/a/6136865)

#### Q74. Quelle affirmation est vraie ?

- [ ] Toutes sont vraies.
- [ ] Aucune n'est vraie.
- [ ] string est un type de valeur.
- [x] string est un alias pour String

[Référence](https://stackoverflow.com/q/7074)

#### Q75. Comment retourneriez-vous plus d'une valeur depuis une méthode ?

- [x] Utilisez soit un tuple soit une variable out.
- [ ] La seule façon est d'utiliser une variable out.
- [ ] La seule façon est d'utiliser un tuple.
- [ ] Cela ne peut pas être fait

#### Q76. Lequel est un exemple valide de classe dérivée ?

- [ ] `public class PremiumUser sub User {}`
- [x] `public class PremiumUser: User {}`
- [ ] `public class PremiumUser -> sub User {}`
- [ ] `public class User: PremiumUser {}`

#### Q77. Quelle est la bonne façon d'appeler une méthode statique nommée DebugString depuis une classe statique appelée InputManager ?

- [ ] `static InputManager.DebugString();`
- [ ] `InputManager().DebugString;`
- [ ] `new InputManager().DebugString();`
- [x] `InputManager.DebugString();`

#### Q78. Quelles valeurs peuvent être assignées à cette variable ?

```cs
public string? nickname
```

- [ ] null
- [ ] String values
- [x] String values or null
- [ ] String values with more than one character

#### Q79. Qu'est-ce qu'un destructeur ?

- [ ] `a special called automatically whenever an object is created or updated`
- [ ] `an implicit method called automatically when thread pools are processed concurrently`
- [ ] `an explicit method called automatically when the compiler starts running`
- [x] `a special method called automatically whenever an object is deleted or destroyed`

[Référence](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/destructors)

#### Q80. Quel extrait de code déclare correctement un alias de type CustomInt de type Int32 ?

- [ ] `typealias CustomInt = System.Int32;`
- [ ] `var<T> CustomInt = Int32;`
- [x] `using CustomInt = System.Int32;`
- [ ] `type CustomInt = System<Int32>;`

[Référence](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/using-directive)

#### Q81. Qu'est-ce qu'un type d'énumération ?

- [ ] `an object of pass by reference type`
- [ ] `a value type that cannot hold constants`
- [x] `set of named integral constants`
- [ ] `an object of pass-by-value type`

#### Q82. À quoi sert le mot-clé readonly dans les déclarations de champ ?

- [ ] `to declare a member variable that cannot be calculated at runtime`
- [x] `to declare a field whose value can be assigned only before the constructor exits`
- [ ] `to declare a static variable that must be set at compile time`
- [ ] `to declare a static variable that must be set at runtime`

#### Q83. Quelle affirmation est vraie concernant les méthodes C# ?

- [ ] `Methods store variables.`
- [x] `Methods are actions that an object can take`
- [ ] `A method can be used only once per C# file.`
- [ ] `A method determines the state of a given property.`

[Documentation officielle : Méthodes (Guide de programmation C#)](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/methods)

#### Q84 Lequel est une classe d'exception C# intégrée valide ?

- [ ] `ArgumentNullValue`
- [ ] `InvalidFormatFoundException`
- [ ] `IndexOutOfPocket`
- [x] `ArgumentNullException`

[Documentation officielle : Classe ArgumentNullException](https://docs.microsoft.com/en-us/dotnet/api/system.argumentnullexception?view=net-5.0)

#### Q85. Quel est le but d'une interface en C# ?

- [ ] Les interfaces sont utilisées pour stocker des données.
- [x] Les interfaces définissent un contrat que les classes doivent respecter, spécifiant un ensemble de méthodes et de propriétés que les classes implémentantes doivent fournir.
- [ ] Les interfaces sont utilisées pour créer des instances de classes.
- [ ] Les interfaces sont utilisées pour l'organisation du code.

[Documentation officielle : Interfaces (Guide de programmation C#)](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/interfaces/)

#### Q86. Quel est le but principal du bloc `finally` dans une instruction try-catch-finally C# ?

- [ ] Le bloc `finally` est utilisé pour gérer les exceptions.
- [ ] Le bloc `finally` est utilisé pour définir la logique principale de l'instruction try-catch.
- [ ] Le bloc `finally` est optionnel et n'est pas requis dans les instructions try-catch.
- [x] Le bloc `finally` est utilisé pour s'assurer qu'un certain code est exécuté indépendamment de savoir si une exception se produit.

[Documentation officielle : try-catch (Référence C#)](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/try-catch)

#### Q87. Quelle structure de données en C# vous permet de stocker des paires clé-valeur et est souvent utilisée pour la récupération rapide de données ?

- [ ] ArrayList
- [ ] List
- [ ] Array
- [x] Dictionary

[Documentation officielle : Classe Dictionary<TKey, TValue>](https://docs.microsoft.com/en-us/dotnet/api/system.collections.generic.dictionary-2)

#### Q88 L'exécution du programme commence par ?

- [x] Main()
- [ ] Get()
- [ ] Class()
- [ ] Display()

[Référence] : https://www.gkseries.com/c-sharp-programming/multiple-choice-questions-and-answers

#### Q89 En C#, 'using' est un ?

- [ ] Class
- [x] Directive
- [ ] Function
- [ ] Keyword

[Référence] : https://www.gkseries.com/c-sharp-programming/multiple-choice-questions-and-answers
