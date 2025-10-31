## Go (langage de programmation)

#### Q1. De quoi avez-vous besoin pour que deux fonctions soient du même type ?

- [x] Elles doivent avoir les mêmes signatures, y compris les types de paramètres et les types de retour.
- [ ] Elles doivent avoir les mêmes types de paramètres mais peuvent retourner des types différents.
- [ ] Toutes les fonctions doivent être du même type.
- [ ] Les fonctions ne doivent pas être de premier ordre.

[User defined function types in Go (Golang)](https://golangbyexample.com/user-defined-function-type-go/)

#### Q2. Que retourne la fonction `len()` si on lui passe une chaîne encodée en UTF-8 ?

- [ ] le nombre de caractères
- [x] le nombre d’octets
- [ ] Elle n’accepte pas les types string.
- [ ] le nombre de points de code

[Length of string in Go (Golang)](https://golangbyexample.com/length-of-string-golang/).

#### Q3. Lequel n’est pas un construit de boucle valide en Go ?

- [x] &shy;

```go
      do { ... } while i < 5
```

- [ ] &shy;

```go
      for _,c := range "hello" { ... }
```

- [ ] &shy;

```go
      for i := 1; i < 5; i++ { ... }
```

- [ ] &shy;

```go
      for i < 5 { ... }
```

**Explication :** Go ne possède que des boucles `for`.

#### Q4. Comment ajouterez-vous le nombre 3 à la fin (à droite) ?

```go
values := []int{1, 1, 2}
```

- [ ] &shy;

```go
      values.append(3)
```

- [ ] &shy;

```go
      values.insert(3, 3)
```

- [ ] &shy;

```go
      append(values, 3)
```

- [x] &shy;

```go
      values = append(values, 3)
```

**Explication :** les slices en Go sont immuables, donc appeler `append` ne modifie pas la slice en place.

#### Q5. Quelle est la valeur de `Read` ?

```go
const (
  Write = iota
  Read
  Execute
)
```

- [ ] 0
- [x] 1
- [ ] 2
- [ ] une valeur aléatoire

[IOTA in Go (Golang)](https://golangbyexample.com/iota-in-golang/)

#### Q6. Quelle est la seule instruction `import` valide en Go ?

- [ ] &shy;

```go
      import "github/gin-gonic/gin"
```

- [ ] &shy;

```go
      import "https://github.com/gin-gonic/gin"
```

- [ ] &shy;

```go
      import "../template"
```

- [x] &shy;

```go
      import "github.com/gin-gonic/gin"
```

[Import in GoLang](https://golangdocs.com/import-in-golang)

#### Q7. Que se passerait-il si vous tentiez de compiler et d’exécuter ce programme Go ?

```go
package main
var GlobalFlag string
func main() {
  print("["+GlobalFlag+"]")
}
```

- [ ] Il ne compilerait pas car `GlobalFlag` n’a jamais été initialisé.
- [x] Il compilerait et afficherait `[]`.
- [ ] Il compilerait et n’afficherait rien car `"[" +nil+"]"` est aussi `nil`.
- [ ] Il compilerait mais panique ensuite car `GlobalFlag` n’a jamais été initialisé.

1. Les [variables](https://golangbyexample.com/variables-in-golang-complete-guide/) en Go ont des valeurs initiales. Pour `string`, c’est la chaîne vide.
2. [Go Playground](https://play.golang.org/p/TaRIzuD-nxC)

#### Q8. Où la variable `myVar` est-elle accessible si elle est déclarée en dehors de toute fonction dans un fichier du paquet `myPackage` situé dans le module `myModule` ?

- [x] Elle est accessible partout dans `myPackage`, pas dans le reste de `myModule`.
- [ ] Elle est accessible par toute application important `myModule`.
- [ ] Elle est accessible depuis n’importe où dans `myModule`.
- [ ] Elle est accessible par d’autres paquets de `myModule` tant qu’ils importent `myPackage`.

**Explication :** pour rendre la variable disponible en dehors de `myPackage`, changez son nom en `MyVar`.
Voir aussi un exemple de [noms exportés](https://tour.golang.org/basics/3) dans le Tour of Go.

#### Q9. Comment demander à `go test` d’afficher les tests qu’il exécute ?

- [ ] `go test`
- [ ] `go test -x`
- [ ] `go test --verbose`
- [x] `go test -v`

[test package](https://pkg.go.dev/cmd/go/internal/test)

#### Q10. Ce code a affiché `{0, 0}`. Comment le corriger ?

```go
type Point struct {
  x int
  y int
}

func main() {
  data := []byte(`{"x":1, "y": 2}`)
  var p Point
  if err := json.Unmarshal(data, &p); err != nil {
    fmt.Println("error: ", err)
  } else {
    fmt.Println(p)
  }
}
```

- [ ] utiliser `json.Decoder`
- [ ] Passer un pointeur vers `data`
- [x] Rendre `X` et `Y` exportés (majuscules)
- [ ] Utiliser des tags de champ

1. [How to Parse JSON in Golang?](https://www.geeksforgeeks.org/how-to-parse-json-in-golang/)
2. [Go Playground](https://play.golang.org/p/RdL6y3Zv8ke)

#### Q11. Qu’est-ce qu’un `sync.Mutex` bloque pendant qu’il est verrouillé ?

- [ ] toutes les goroutines
- [ ] tout autre appel pour verrouiller ce `Mutex`
- [x] toute lecture ou écriture de la variable qu’il verrouille
- [ ] toute écriture de la variable qu’il verrouille

1. [Mutex in GoLang](https://golangdocs.com/mutex-in-golang), `sync.Mutex` verrouille pour qu’une seule goroutine à la fois accède à la variable protégée.
2. [sync.Mutex](https://go.dev/tour/concurrency/9)

#### Q12. Quelle est la manière idiomatique de suspendre l’exécution de la portée courante jusqu’à ce qu’un nombre arbitraire de goroutines aient terminé ?

- [ ] Passer un `int` et un `Mutex` à chacune et compter à leur retour.
- [ ] Boucler via un `select`.
- [ ] Dormir une durée « sûre ».
- [x] `sync.WaitGroup`

**Explication :** c’est exactement l’usage de `sync.WaitGroup` - [Use sync.WaitGroup in Golang](https://nanxiao.me/en/use-sync-waitgroup-in-golang/)

#### Q13. Quel est l’effet secondaire d’utiliser `time.After` dans une instruction `select` ?

- [ ] Cela bloque les autres canaux.
- [ ] Il est conçu pour être utilisé dans `select` sans effets secondaires.
- [ ] Cela bloque le `select` jusqu’à ce que le temps soit écoulé.
- [x] La goroutine ne se termine pas avant que le temps ne soit écoulé.

> Remarque : cela ne bloque pas `select` et ne bloque pas les autres canaux.

1. [time.After() Function in Golang With Examples](https://www.geeksforgeeks.org/time-after-function-in-golang-with-examples/)
2. [How can I use 'time.After' and 'default' in Golang?](https://stackoverflow.com/questions/39212333/how-can-i-use-time-after-and-default-in-golang)
3. [Go Playground example](https://go.dev/play/p/WojTrG1ywRK)

#### Q14. À quoi sert l’instruction `select` ?

- [ ] exécuter une fonction en concurrence
- [ ] exécuter un cas différent selon le type d’une variable
- [ ] exécuter un cas différent selon la valeur d’une variable
- [x] exécuter un cas différent selon le canal qui répond en premier

[Select statement in GoLang](https://golangdocs.com/select-statement-in-golang)

#### Q15. Selon le standard de documentation Go, comment devriez-vous documenter cette fonction ?

```go
func Add(a, b int) int {
        return a + b
}
```

- [ ] A

  ```go
  // Calcule a + b
  // - a: int
  // - b: int
  // - retourne: int
  func Add(a, b int) int {
          return a + b
  }
  ```

- [ ] B

  ```go
  // Fait a + b
  func Add(a, b int)  int {
          return a + b
  }
  ```

- [x] C

  ```go
  // Add returns the sum of a and b
  func Add(a, b int) int {
          return a + b
  }
  ```

- [ ] D

  ```go
  // returns the sum of a and b
  func Add(a, b int) int {
          return a + b
  }
  ```

**Explication :** le bloc de documentation doit commencer par le nom de la fonction.

[Comments in Go](https://exercism.org/tracks/go/concepts/comments)

#### Q16. Quelle contrainte s’applique au type de `myVal` pour compiler `i := myVal.(int)` ?

- [ ] `myVal` doit être un type entier, tel que `int`, `int64`, `int32`, etc.
- [ ] `myVal` doit pouvoir être asserté comme un `int`.
- [x] `myVal` doit être une interface.
- [ ] `myVal` doit être un type numérique, tel que `float64` ou `int64`.

**Explication :** ce type d’assertion de type (via `.(type)`) s’utilise uniquement sur des interfaces.

1. [this example](https://tutorialedge.net/golang/snippets/type-casting-interface-to-string-go/)
2. [Primitive types are type-casted differently](https://golangdocs.com/type-casting-in-golang)
3. [Go Playground](https://play.golang.org/p/TXF_JBvThp6)
4. [Type assertions](https://go.dev/tour/methods/15)

#### Q17. Qu’est-ce qu’un canal (`channel`) ?

- [ ] une variable globale
- [x] un moyen d’envoyer des valeurs entre des goroutines
- [ ] un tableau dynamique de valeurs
- [ ] un thread léger pour la programmation concurrente

[Channels](https://tour.golang.org/concurrency/2)

#### Q18. Comment faire en sorte qu’un fichier ne se compile que sur Windows ?

- [ ] Vérifier `runtime.GOOS`.
- [ ] Ajouter un commentaire `// +build windows` n’importe où dans le fichier.
- [ ] Ajouter un préfixe `_` au nom du fichier.
- [x] Ajouter un commentaire `// +build windows` en haut du fichier.

1. [How to use conditional compilation with the go build tool, Oct 2013](https://dave.cheney.net/2013/10/12/how-to-use-conditional-compilation-with-the-go-build-tool)
2. [go commands Build constraints](https://pkg.go.dev/cmd/go#hdr-Build_constraints)

> `//go:build windows`
> « Les versions de Go 1.16 et antérieures utilisaient une syntaxe différente pour les contraintes de build, avec le préfixe `// +build`. La commande gofmt ajoutera une contrainte `//go:build` équivalente en rencontrant l’ancienne syntaxe. »

#### Q19. Quelle est la bonne manière de passer ceci comme corps d’une requête HTTP POST ?

```go
data := "A group of Owls is called a parliament"
```

- [ ] &shy;

```go
  resp, err := http.Post("https://httpbin.org/post", "text/plain", []byte(data))
```

- [ ] &shy;

```go
      resp, err := http.Post("https://httpbin.org/post", "text/plain", data)
```

- [x] &shy;

```go
      resp, err := http.Post("https://httpbin.org/post", "text/plain", strings.NewReader(data))
```

- [ ] &shy;

```go
      resp, err := http.Post("https://httpbin.org/post", "text/plain", &data)
```

1. [net/http#Client.Post](https://pkg.go.dev/net/http#Client.Post)
2. [http.Post Golang example](https://dev.to/ramu_mangalarapu/httppost-golang-example-5jp)

#### Q20. Quel devrait être le nom idiomatique d’une interface avec une seule méthode ayant la signature `Save() error` ?

- [ ] Saveable
- [ ] SaveInterface
- [ ] ISave
- [x] Saver

[Effective Go, Interface names](https://golang.org/doc/effective_go#interface-names)

#### Q21. Une instruction `switch` **\_** son propre bloc lexical. Chaque instruction `case` **\_** un bloc lexical supplémentaire

- [ ] ne crée pas ; crée
- [ ] ne crée pas ; ne crée pas
- [x] crée ; crée
- [ ] crée ; ne crée pas

[Go Language Core technology (Volume one) 1.5-scope](https://topic.alibabacloud.com/a/go-language-core-technology-volume-one-15-font-colorredscopefont_1_38_30923325.html)

Extrait pertinent de l’article :

> Le second `if` est imbriqué dans le premier, donc une variable déclarée dans le premier `if` est visible dans le second. Il y a des règles similaires dans `switch` : chaque `case` possède son propre bloc lexical en plus du bloc conditionnel.

#### Q22. Quelle est la sensibilité à la casse par défaut de la fonction JSON `Unmarshal` ?

- [x] Le comportement par défaut est insensible à la casse, mais il peut être redéfini.
- [ ] Les champs sont pris en compte en respectant la casse.
- [ ] Les champs sont pris en compte sans tenir compte de la casse.
- [ ] Le comportement par défaut est sensible à la casse, mais il peut être redéfini.

[encoding/json#Unmarshal](https://pkg.go.dev/encoding/json#Unmarshal)

Extrait pertinent :

> To unmarshal JSON into a struct, Unmarshal matches incoming object keys to the keys used by Marshal (either the struct field name or its tag), preferring an exact match but also accepting a case-insensitive match. By default, object keys which don't have a corresponding struct field are ignored (see Decoder.DisallowUnknownFields for an alternative).

#### Q23. Quelle est la différence entre les méthodes `Time.Sub()` et `Time.Add()` du paquet `time` ?

- [ ] `Time.Add()` sert à faire des additions tandis que `Time.Sub()` sert à imbriquer des timestamps.
- [ ] `Time.Add()` retourne toujours un temps plus tard tandis que `Time.Sub()` retourne toujours un temps plus tôt.
- [ ] Elles sont opposées. `Time.Add(x)` équivaut à `Time.Sub(-x)`.
- [x] `Time.Add()` accepte un paramètre `Duration` et retourne un `Time` tandis que `Time.Sub()` accepte un `Time` et retourne une `Duration`.

1. [time#Time.Add](https://pkg.go.dev/time#Time.Add)
2. [time#Time.Sub](https://pkg.go.dev/time#Time.Sub)

#### Q24. Quel est le risque d’utiliser plusieurs tags de champ dans une même struct ?

- [ ] Chaque champ doit avoir tous les tags pour compiler.
- [x] Cela couple fortement différentes couches de votre application.
- [ ] Tous les tags après le premier sont ignorés.
- [ ] Des tags manquants provoquent un panic à l’exécution.

1. [Example Code / b29r0fUD1cp](https://play.golang.org/p/b29r0fUD1cp)
2. [How To Use Struct Tags in Go](https://www.digitalocean.com/community/tutorials/how-to-use-struct-tags-in-go)

#### Q25. Où la méthode intégrée `recover` est-elle utile ?

- [ ] dans la fonction `main`
- [ ] immédiatement après une ligne susceptible de paniquer
- [x] à l’intérieur d’une fonction différée (`deferred`)
- [ ] au début d’une fonction susceptible de paniquer

[Example of Recover Function in Go (Golang)](https://golangbot.com/panic-and-recover/#recoveringfromapanic)

Extrait pertinent :

> Recover is useful only when called inside deferred functions. Executing a call to recover inside a deferred function stops the panicking sequence by restoring normal execution and retrieves the error message passed to the panic function call. If recover is called outside the deferred function, it will not stop a panicking sequence.

#### Q26. Lequel des choix ne renvoie pas de sortie sur la sortie d’erreur standard ?

- [ ] `println(message)`
- [ ] `log.New(os.Stderr, "", 0).Println(message)`
- [x] `fmt.Errorf("%s\n", message)`
- [ ] `fmt.Fprintln(os.Stderr, message)`

1. [func println](https://pkg.go.dev/builtin#println) : écrit le résultat sur l’erreur standard.
2. [func New](https://pkg.go.dev/log#New) : `func New(out io.Writer, prefix string, flag int) *Logger`; le paramètre `out` définit la destination d’écriture des logs.
3. [func Errorf](https://pkg.go.dev/fmt#Errorf) : `Errorf` formate selon un spécificateur et retourne la chaîne comme valeur.
4. [func Fprintln](https://pkg.go.dev/fmt#Fprintln) : écrit dans `w`.

#### Q27. Comment indiquer à Go d’importer un paquet depuis un autre emplacement ?

- [ ] Utiliser un proxy.
- [ ] Changer le chemin d’import.
- [x] Utiliser une directive `replace` dans `go.mod`.
- [ ] Utiliser un répertoire `replace`.

1. [Call your code from another module](https://go.dev/doc/tutorial/call-module-code) : chapitre 5., `go mod edit -replace example.com/greetings=../greetings`.
2. [go.mod replace directive](https://go.dev/doc/modules/gomod-ref#replace)

#### Q28. Si votre répertoire de travail actuel est la racine de votre projet, quelle commande exécutera tous ses paquets de test ?

- [ ] `go test all`
- [ ] `go run --all`
- [ ] `go test .`
- [x] `go test ./...`

1. [Example of testing in Go (Golang)](https://pkg.go.dev/testing)
2. [Example of cmd in Go (Golang)](https://pkg.go.dev/cmd/go)

Extrait pertinent :

> Relative patterns are also allowed, like "go test ./..." to test all subdirectories.

#### Q29. Quelles encodages pouvez-vous mettre dans une chaîne ?

- [ ] n’importe lequel, elle accepte des octets arbitraires
- [ ] n’importe quel format Unicode
- [ ] UTF-8 ou ASCII
- [x] UTF-8

1. [Strings, bytes, runes and characters in Go](https://go.dev/blog/strings)

Extrait pertinent :

> In short, Go source code is UTF-8, so the source code for the string literal is UTF-8 text.

2. [Example of encoding in Go (Golang)](https://pkg.go.dev/golang.org/x/text/encoding)

Extrait pertinent :

> Package encoding defines an interface for character encodings, such as Shift JIS and Windows 1252, that can convert to and from UTF-8.

#### Q30. En quoi le comportement de `t.Fatal` diffère-t-il à l’intérieur d’un `t.Run` ?

- [ ] Il n’y a aucune différence.
- [ ] `t.Fatal` ne fait pas planter le banc de test, préservant les messages.
- [x] `t.Fatal` arrête l’exécution du sous-test et continue avec les autres cas de test.
- [ ] `t.Fatal` arrête tous les tests et contient des informations supplémentaires sur le sous-test échoué.

1. [Reference:](https://go.dev/play/p/gtne3iRL9AX)
2. [testing package in Go](https://pkg.go.dev/testing), extrait pertinent :

> `Fatal` is equivalent to `Log` followed by `FailNow`.
> `Log` formats its arguments using default formatting, analogous to `Println`, and records the text in the error log.
> `FailNow` marks the function as having failed and stops its execution by calling `runtime.Goexit` (which then runs all deferred calls in the current goroutine). Execution will continue at the next test or benchmark. `FailNow` must be called from the goroutine running the test or benchmark function, not from other goroutines created during the test. Calling `FailNow` does not stop those other goroutines.
> `Run` runs `f` as a subtest of `t` called name. It runs `f` in a separate goroutine and blocks until `f` returns or calls `t.Parallel` to become a parallel test. Run reports whether `f` succeeded (or at least did not fail before calling `t.Parallel`).
> Run may be called simultaneously from multiple goroutines, but all such calls must return before the outer test function for t returns.

#### Q31. Que fait `log.Fatal` ?

- [ ] Il déclenche un panic.
- [ ] Il affiche le log puis déclenche un panic.
- [x] Il affiche le log puis quitte le programme en toute sécurité.
- [ ] Il quitte le programme.

[Example of func Fatal in Go (Golang)](https://pkg.go.dev/log#Fatal)

Extrait pertinent :

> `Fatal` is equivalent to `Print()` followed by a call to `os.Exit(1)`.

#### Q32. Lequel est un littéral de format d’heure valide en Go ?

- [x] "2006-01-02"
- [ ] "YYYY-mm-dd"
- [ ] "y-mo-d"
- [ ] "year-month-day"

[func Time in Go](https://pkg.go.dev/time#pkg-constants)

Extrait pertinent :

```text
Year: "2006" "06"
Month: "Jan" "January" "01" "1"
Day of the week: "Mon" "Monday"
Day of the month: "2" "_2" "02"
Day of the year: "__2" "002"
Hour: "15" "3" "03" (PM or AM)
Minute: "4" "04"
Second: "5" "05"
AM/PM mark: "PM"
```

#### Q33. Comment devriez-vous journaliser une erreur (`err`) ?

- [ ] `log.Error(err)`
- [x] `log.Printf("error: %v", err)`
- [ ] `log.Printf(log.ERROR, err)`
- [ ] `log.Print("error: %v", err)`

**Explication :** Il n’y a ni `log.ERROR`, ni `log.Error()` dans le [paquet log en Go](https://pkg.go.dev/log) ; les arguments de `log.Print()` sont gérés comme `fmt.Print()` ; ceux de `log.Printf()` comme `fmt.Printf()`.

#### Q34. Quels noms de fichiers la commande `go test` reconnaît-elle comme fichiers de test ?

- [ ] tout fichier commençant par `test`
- [ ] tout fichier contenant le mot `test`
- [ ] uniquement les fichiers à la racine se terminant par `_test.go`
- [x] tout fichier se terminant par `_test.go`

1. [Test packages in go command in Go](https://pkg.go.dev/cmd/go#hdr-Test_packages) : « 'Go test' recompile chaque paquet avec tous les fichiers dont le nom matche le motif `*_test.go`. »
2. [Add a test in Go](https://go.dev/doc/tutorial/add-a-test)

#### Q35. Quelle sera la sortie de ce code ?

```go
ch := make(chan int)
ch <- 7
val := <-ch
fmt.Println(val)
```

- [ ] 0
- [x] Il y aura un deadlock
- [ ] Cela ne compilera pas
- [ ] 2.718

[Go Playground share](https://go.dev/play/p/SQlfg8YSEOz), sortie :

```text
fatal error: all goroutines are asleep - deadlock!

goroutine 1 [chan send]:
main.main()
 /tmp/sandbox2282523250/prog.go:7 +0x37

Program exited.
```

#### Q36. Quelle sera la sortie de ce programme ?

```go
ch := make(chan int)
close(ch)
val := <-ch
fmt.Println(val)
```

- [ ] Deadlock
- [ ] Panic
- [x] 0
- [ ] NaN

1. [The Go Programming Language Specification "Receive operator"](https://go.dev/ref/spec#Receive_operator), extrait pertinent :

   > A receive operation on a closed channel can always proceed immediately, yielding the element type's zero value after any previously sent values have been received.

2. [Go Playground share](https://go.dev/play/p/DjXq9wzJm5M), sortie :

```text
0

Program exited.
```

#### Q37. Qu’est-ce qui sera affiché par ce code ?

```go
var stocks map[string]float64 // stock -> price
price := stocks["MSFT"]
fmt.Printf("%f\n", price)
```

- [ ] 0
- [x] 0.000000
- [ ] Le code va paniquer
- [ ] NaN

[Go Playground share](https://go.dev/play/p/CjdHskV1xq1), sortie :

```text
0.000000

Program exited.
```

#### Q38. Quelle est la manière courante d’avoir plusieurs exécutables dans votre projet ?

- [x] Avoir un répertoire `cmd` et un sous-répertoire par exécutable.
- [ ] Commenter `main`.
- [ ] Utiliser des build tags.
- [ ] Avoir un répertoire `pkg` et un sous-répertoire par exécutable.

1. [stackoverflow](https://stackoverflow.com/questions/9985559/organizing-a-multiple-file-go-project/51942843#51942843)
2. [medium](https://medium.com/@benbjohnson/structuring-applications-in-go-3b04be4ff091)
3. [medium](https://medium.com/golang-learn/go-project-layout-e5213cdcfaa2)

#### Q39. Comment compiler `main.go` en un exécutable qui fonctionnera sur OSX arm64 ?

- [ ] Définir GOOS sur **arm64** et GOARCH sur **darwin**.
- [ ] Définir GOOS sur **osx** et GOARCH sur **arm64**.
- [ ] Définir GOOS sur **arm64** et GOARCH sur **osx**.
- [x] Définir GOOS sur **darwin** et GOARCH sur **arm64**.

[documentation](https://pkg.go.dev/cmd/go#hdr-Build_constraints)

#### Q40. Quelle est la syntaxe correcte pour démarrer une goroutine qui va `print Hello Gopher!` ?

- [ ] `go(fmt.Println("Hello Gopher!"))`
- [ ] `go func() { fmt.Println("Hello Gopher!") }`
- [x] `go fmt.Println("Hello Gopher!")`
- [ ] `Go fmt.Println("Hello Gopher!")`

[Example of start a goroutine](https://go.dev/play/p/KGgnAWpZMrS)

#### Q41. Si vous itérez sur une map dans une boucle `for range`, dans quel ordre les paires clé:valeur seront-elles accédées ?

- [x] dans un ordre pseudo-aléatoire imprévisible
- [ ] dans l’ordre inverse d’insertion (dernier entré, premier sorti)
- [ ] triées par clé par ordre croissant
- [ ] dans l’ordre d’insertion (premier entré, premier sorti)

[Reference](https://go.dev/ref/spec#:~:text=The%20iteration%20order%20over%20maps%20is%20not%20specified)

#### Q42. Quelle est la manière idiomatique de personnaliser la représentation d’une struct personnalisée dans une chaîne formatée ?

- [ ] Il n’y a pas de personnalisation de la représentation string d’un type.
- [ ] La construire en morceaux à chaque fois via les champs individuels.
- [x] Implémenter une méthode `String() string`
- [ ] Créer une fonction wrapper qui accepte votre type et retourne une chaîne.

[Reference](https://go.dev/doc/effective_go#printing)

#### Q43. Comment éviter une fuite de goroutine dans ce code ?

```go
func findUser(ctx context.Context, login string) (*User, error) {
    ch := make(chan *User)
    go func() {
            ch <- findUserInDB(login)
    }()

    select {
    case user := <-ch:
            return user, nil
    case <-ctx.Done():
            return nil, fmt.Errorf("timeout")
    }
}
```

- [ ] Utiliser un `sync.WaitGroup`.
- [x] Rendre `ch` tamponné (buffered).
- [ ] Ajouter un `default` au `select`.
- [ ] Utiliser `runtime.SetFinalizer`.

[Reference](https://www.ardanlabs.com/blog/2018/11/goroutine-leaks-the-forgotten-sender.html)

Extrait pertinent :

> The simplest way to resolve this leak is to change the channel from an unbuffered channel to a buffered channel with a capacity of 1. Now in the timeout case, after the receiver has moved on, the Goroutine will complete its send by placing the \*User value in the channel then it will return.

#### 44. Qu’est-ce que ce code va afficher ?

```go
var i int8 = 120
i += 10
fmt.Println(i)
```

- [x] -126
- [ ] 0
- [ ] NaN
- [ ] 130

[Go Playground example](https://go.dev/play/p/T31_JuFioaC), sortie :

```text
-126

Program exited.
```

#### 45. Étant donné la définition de `worker` ci-dessous, quelle est la bonne syntaxe pour démarrer une goroutine qui appellera `worker` et enverra le résultat dans un canal nommé `ch` ?

```go
func worker(m Message) Result
```

- [ ] &shy;

```go
go func() {
    r := worker(m)
    ch <- r
}
```

- [ ] &shy;

```go
go func() {
    r := worker(m)
    r -> ch
} ()
```

- [x] &shy;

```go
go func() {
    r := worker(m)
    ch <- r
} ()
```

- [ ] &shy;

```go
go ch <- worker(m)
```

[Go Playground example](https://go.dev/play/p/96j7tuQKF50)

#### Q46. Dans ce code, quels noms sont exportés ?

```go
package os

type FilePermission int
type userID int
```

- [x] FilePermission
- [ ] aucune de ces réponses
- [ ] FilePermission et userID
- [ ] userID

[Reference 1](https://www.ardanlabs.com/blog/2018/11/goroutine-leaks-the-forgotten-sender.html)
[Reference 2](https://go.dev/tour/basics/3)

#### Q47. Laquelle des affirmations suivantes est correcte à propos des structures en Go ?

- [ ] Une structure est un autre type de données défini par l’utilisateur en Go, qui vous permet de combiner des éléments de données de différents types.
- [ ] Les structures sont utilisées pour représenter un enregistrement.
- [ ] Pour définir une structure, vous devez utiliser les instructions `type` et `struct`.
- [x] Toutes les réponses ci-dessus

#### Q48. Que fait la commande intégrée `generate` du compilateur Go ?

- [ ] Elle fournit les sous-commandes `sql`, `json`, `yaml`, et les options `--schema` et `--objects` pour générer le code approprié.
- [ ] Elle recherche les fichiers dont le nom se termine par `_generate.go`, puis compile et exécute chacun individuellement.
- [x] Elle scanne le code source du projet à la recherche de commentaires `//go:generate` et exécute pour chacun la commande terminal spécifiée.
- [ ] Elle dispose des sous-commandes `mocks` et `tests` pour générer les fichiers `.go` correspondants.

[Generate Go files by processing source](https://pkg.go.dev/cmd/go#hdr-Generate_Go_files_by_processing_source)

#### Q49. En utilisant le paquet `time`, comment obtenir l’heure dans 90 minutes ?

- [ ] `time.Now().Add(90)`
- [ ] `time.Now() + (90 * time.Minute)`
- [ ] `time.Now() + 90`
- [x] `time.Now().Add(90 * time.Minute)`

[func (Time) Add example](https://pkg.go.dev/time#example-Time.Add)

#### Q50. Un programme utilise un canal pour imprimer cinq entiers dans une goroutine tout en alimentant le canal depuis la routine principale, mais cela ne fonctionne pas tel quel. Que faut-il changer pour le faire fonctionner ?

- [ ] Ajouter un `close(ch)` immédiatement après `wg.Wait()`.
- [x] Ajouter un second paramètre à `make(chan, int)`, par ex. `make(chan int, 5)`.
- [ ] Supprimer l’utilisation inutile de `WaitGroup`, par ex. toutes les lignes commençant par `wg`.
- [ ] Déplacer la goroutine de 7 lignes immédiatement avant `wg.Wait()`.

[Reference](https://www.ardanlabs.com/blog/2018/11/goroutine-leaks-the-forgotten-sender.html)

Extrait pertinent :

> The simplest way to resolve this leak is to change the channel from an unbuffered channel to a buffered channel with a capacity of 1. Now in the timeout case, after the receiver has moved on, the Goroutine will complete its send by placing the \*User value in the channel then it will return.

#### Q51. Après avoir importé `encoding/json`, comment accéderiez-vous à la fonction `Marshal` ?

- [ ] `encoding.json.Marshal`
- [ ] `encoding/json.Marshal`
- [ ] `Marshal`
- [x] `json.Marshal`

[encoding/json#Marshal example](https://pkg.go.dev/encoding/json#example-Marshal)

#### Q52. Quels sont les deux segments de code manquants pour compléter l’utilisation de `context.Context` afin d’implémenter un timeout de trois secondes pour ce client HTTP effectuant une requête GET ?

```go
package main

import (
        "context"
        "fmt"
        "net/http"
)

func main() {
        var cancel context.CancelFunc
        ctx := context.Background()

        // #1: <=== What should go here?

        req, _ := http.NewRequest(http.MethodGet,
                "https://linkedin.com",
                nil)

        // #2: <=== What should go here?

        client := &http.Client{}
        res, err := client.Do(req)
        if err != nil {
                fmt.Println("Request failed:", err)
                return
        }
        fmt.Println("Response received, status code:",
                res.StatusCode)
}
```

- [ ] &shy;

```go
      ctx.SetTimeout(3*time.Second)
      req.AttachContext(ctx)
```

- [x] &shy;

```go
      ctx, cancel = context.WithTimeout(ctx, 3*time.Second); defer cancel()
      req = req.WithContext(ctx)
```

- [ ] &shy;

```go
      ctx, cancel = context.WithTimeout(ctx, 3*time.Second); defer cancel() #2: req.AttachContext(ctx)
```

- [ ] &shy;

```go
      ctx.SetTimeout(3*time.Second)
      req = req.WithContext(ctx)
```

1. [context#WithTimeout](https://pkg.go.dev/context#WithTimeout)
2. [net/http#Request.WithContext](https://pkg.go.dev/net/http#Request.WithContext)

#### Q53. Si vous avez une struct nommée `Client` définie dans le même fichier `.go` que l’instruction, comment exporter une variable avec une valeur par défaut pour qu’elle soit accessible par d’autres paquets ?

- [ ] &shy;

  ```go
  let Default := new Client()
  ```

- [ ] &shy;

  ```go
  public default = &Client()
  ```

- [x] &shy;

  ```go
  var Default = &Client{}
  ```

- [ ] &shy;

  ```go
  export default := new Client{}
  ```

#### Q54. Ce programme affiche `{Master Chief Spartan Protagonist Halo}`. Comment faire pour qu’il affiche `Master Chief - a Spartan - is the Protagonist of Halo` à la place ?

```go
package main

import "fmt"

type Character struct{
        Name  string
        Class string
        Role  string
        Game  string
}

func main() {
        mc := Character{
                Name: "Master Chief",
                Class: "Spartan",
                Role: "Protagonist",
                Game: "Halo",
        }
        fmt.Println(mc)
}
```

- [ ] A

  ```go
  // Remplacez
  // fmt.Println(mc)
  // par :

  fmt.Printf("(?P<Name>) - a (?P<Class>) - is the (?P<Role>) of (?P<Game>)", mc)
  ```

- [ ] B

  ```go
  // Remplacez
  // fmt.Println(mc)
  // par :
  fmt.Println(mc, func(c Character) string {
        return c. Name + " - a " + c.Class + " - is the " + c.Role + " of " + c.Game
  })
  ```

- [x] C

  ```go
  // ajoutez ceci au package `main`

  func (c Character) String() string {
        return fmt.Sprintf("%s - a %s - is the %s of %s", c.Name, c.Class, c.Role,c.Game)
  }
  ```

- [ ] D

  ```go
   // ajoutez ceci au package `main`

  func (c Character) OnPrint() {
        fmt.Println("{{c.Name}} - a {{c.Class}} - is the {{c.Role}} of {{c.Game}}")
  }
  ```

1. [fmt#Stringer](https://pkg.go.dev/fmt#Stringer)

#### Q55. Comment implémenter une méthode `Append()` fonctionnelle pour `Clients` ?

```go
package main

type Client struct {
  Name string
}
type Clients struct {
  clients []*Client
}
func main() {
  c:= &Clients{clients.make([]*Client,0)}
  c.Append(&Client{Name: "LinkedIn API})
}
```

- [x] A

  ```go
  func (cc *Clients) Append(c *Client) {
    cc.clients = append(cc.clients, c)
  }
  ```

- [ ] B

  ```go
  func (cc *Clients) Append(c *Client) {
    cc.append(c)
  }
  ```

- [ ] C

  ```go
  func (cc Clients) Append(c Client) {
    cc.clients = append(cc.clients, c)
  }
  ```

- [ ] D

  ```go
  func (cc *Clients) Append(c Client) {
    cc.clients.append(c)
  }
  ```

#### Q56. Comment récupérer d’un `panic()` déclenché par une fonction appelée sans laisser votre programme échouer, en supposant que votre réponse s’exécute dans la même portée où l’appel de fonction provoquera le panic ?

- [ ] Enveloppant l’appel dans une fonction anonyme avec un type de retour `panic`, en n’oubliant pas de l’invoquer avec `()` puis en introspectant l’instance retournée pour gérer l’erreur.

- [ ] Utiliser `try{ ... }` pour envelopper le code et gérer l’erreur dans `catch{ ... }`.

- [x] Utiliser `defer func { ... }()` avant l’appel problématique puis gérer le panic dans la fonction anonyme.

- [ ] Préfixer l’appel de fonction avec `@` pour forcer le retour d’un `error` puis le gérer comme d’habitude.

#### Q57. Qu’est-ce que ce code va afficher ?

```go
var n int
fmt.Println (n)
```

- [x] 0
- [ ] nil
- [ ] une valeur aléatoire
- [ ] 1

> En Go, lorsqu’une variable est déclarée sans initialisation explicite, elle reçoit sa [valeur zéro](https://go.dev/tour/basics/12) selon son type. Pour les entiers comme `n`, la valeur zéro est 0.

#### Q58. Lors de la création d’une chaîne formatée, quel verbe devez-vous utiliser pour appeler la méthode `String() string` d’un type personnalisé ?

- [x] %s
- [ ] %b
- [ ] %v
- [ ] %string

> En Go, le verbe %s est utilisé pour formater une chaîne. Lorsqu’il est utilisé avec un type personnalisé ayant une méthode `String()`, celle-ci est appelée automatiquement et sa valeur de retour est utilisée dans la chaîne formatée.

#### Q59. Lequel n’est pas une valeur valide pour `layout` lors de l’appel de `time.Now().Format(layout)` ?

- [ ] time.REC3339
- [x] "1970-01-01"
- [ ] "Jan 2nd 2006"
- [ ] time.Kitchen

[time#Time.Format](https://pkg.go.dev/time#Time.Format)

Selon la documentation, la valeur 1 et 01 représentent le mois courant.

```text
each layout string is a representation of the time stamp,
	Jan 2 15:04:05 2006 MST
An easy way to remember this value is that it holds, when presented in this order, the values (lined up with the elements above):
	  1 2  3  4  5    6  -7
```

#### Q60. Comment signaler au compilateur Go que la struct `Namespace` doit implémenter l’interface `JSONConverter` ? Cette question suppose que la réponse sera incluse dans le même package où `Namespace` est déclarée.

- [ ] `var _ JSONConverter = nil.(*Namespace)`
- [x] `var _ JSONConverter = (*Namespace)(nil)`
- [ ] ````````go
                          type Namespace struct {
                              implements JSONConverter
                          }
                          ```
                      ````
                  `````
              ``````
          ```````
      ````````
- [ ] ````````go
                          type Namespace struct {
                              JSONConverter
                          }
                          ```
                      ````
                  `````
              ``````
          ```````
      ````````

> Cette syntaxe crée une variable `_` de type `JSONConverter` et lui assigne la valeur `(*Namespace)(nil)`. Cela vérifie que `Namespace` satisfait l’interface `JSONConverter` en s’assurant qu’elle peut être affectée à une variable de type `JSONConverter`.

#### Q61. Quelle affirmation à propos du typage et des interfaces est fausse ?

- [ ] Une signature de méthode est la combinaison d’un nom de méthode et des types de ses paramètres et valeurs de retour déclarés.
- [x] Une struct doit déclarer explicitement via le mot-clé `implements` que ses instances peuvent être utilisées partout où une variable, un paramètre et/ou une valeur de retour est typée pour l’interface déclarée.
- [ ] Une interface déclare une liste de méthodes et leurs signatures qu’un type doit implémenter pour être compatible avec les valeurs typées pour cette interface.
- [ ] Les variables, paramètres et valeurs de retour doivent être « typés » comme l’un de 1) un type intégré, 2) un alias de type, 3) un type dérivé, 4) un type composite, ou 5) une interface.

> En Go, un type satisfait automatiquement une interface s’il implémente toutes ses méthodes. Il n’y a pas besoin de déclarer explicitement qu’une struct implémente une interface via un mot-clé spécifique.

#### Q62. Comment compléter ce programme pour générer la sortie indiquée, en supposant la table SQL ?

```go
===[Output]================
1: &{GameId:1 Title:Wolfenstein YearReleased:1992}
2: &{GameId:2 Title:Doom YearReleased:1993}
3: &{GameId:3 Title:Quake YearReleased:1996}

===[main.go]================
package main

import (
        "database/sql"
        "fmt"
        _ "github.com/go-sql-driver/mysql"
        "log"
)

type Game struct {
        GameId       int
        Title        string
        YearReleased int
}

func main() {

        conn, err := sql.Open("mysql",
                "john_carmack:agiftw!@tcp(localhost:3306)/idsoftware")

        if err != nil {
                panic(err)
        }
        defer func() { _ = conn.Close() }()

        results, err := conn.Query("SELECT game_id,title,year_released FROM games;")
        if err != nil {
                panic(err)
        }
        defer func() { _ = results.Close() }()

        // #1 <=== What goes here?

        for results.Next() {
                var g Game

                // #2 <=== What goes here?

                if err != nil {
                        panic(err)
                }

                // #3 <=== What goes here?

        }

        for i, g := range games {
                fmt.Printf("%d: %+v\n", i, g)
        }

}
```

- [ ] &shy;

```go
#1: games := make([]*Game, results.RowsAffected())
#2: g, err = results.Fetch()
#3: games[results.Index()] = &g
```

- [ ] &shy;

```go
#1: games := []Game{}
#2: g, err = results.Fetch()
#3: games = append(games,g)
```

- [ ] &shy;

```go
#1: games := map[int]Game{}
#2: err = results.Scan(&g)
#3: games[g.GameId] = g
```

- [x] &shy;

```go
#1: games := make(map[int]*Game, 0)
#2: err = results.Scan(&g.GameId, &g.Title, &g.YearReleased)
#3: games[g.GameId] = &g
```

#### Q63. Complétez les blancs

1.  Les fichiers de test en Go doivent **\_**.
2.  Les tests individuels sont identifiés par **\_**.
3.  Vous pouvez exécuter des sous-tests en **\_**.
4.  Vous journalisez l’erreur et marquez le test comme échoué en **\_**.

- [ ] être stockés dans un sous-répertoire `/test/` de ce paquet<br/>fonctions acceptant un paramètre `testing.Tester`<br/>écrire des fonctions dont le nom matche `^Subtest`<br/>appeler `testing.AssertionFailed`

- [x] se terminer par `_test.go`<br/>noms de fonctions correspondant à `^Test[A-Z]`<br/>appeler `t.Run()`<br/>appeler `t.Errorf()`

- [ ] commencer par `test_`<br/>fonctions correspondant à `[a-z]Test$`<br/>appeler `testing.Subtest()`<br/>laisser `testing.Assert()` échouer son assertion

- [ ] être stockés dans le sous-dossier `/test/` à la racine du projet<br/>fonctions acceptant un paramètre `testing.Test`<br/>passer des closures à `testing.AddSubtest()`<br/>retourner une `error` depuis la fonction

#### Q64. Pour quel type `rune` est-il un alias ?

- [ ] char
- [ ] byte
- [x] int32
- [ ] string

1. [Strings, bytes, runes and characters in Go](https://go.dev/blog/strings)

Extrait pertinent :

> The Go language defines the word rune as an alias for the type int32, so programs can be clear when an integer value represents a code point.

#### Q65. Quand pouvez-vous utiliser la syntaxe `:=` pour affecter à plusieurs variables ? Par exemple :

```go
x, err := myFunc()
```

- [x] si au moins l’une d’elles n’a pas été déclarée dans ce bloc lexical
- [ ] tout le temps, cela écrasera les variables existantes
- [ ] si aucune variable de ces noms n’est accessible
- [ ] si aucune de ces variables n’existe dans ce bloc lexical

1. [Short variable declarations](https://go.dev/ref/spec#Short_variable_declarations)

#### Q66. Comment afficher la sortie du profileur dans `cpu.pprof` dans le navigateur ?

- [ ] `go pprof -to SVG cpu.prof`
- [x] `go tool pprof -http=:8080 cpu.pprof`
- [ ] `go tool pprof cpu.pprof`
- [ ] `go tool trace cpu.pprof`

#### Q67. Quand une variable de type `interface{}` est-elle évaluée à `nil` ?

- [x] Lorsqu’on lui a assigné un type dynamique dont la valeur est `nil`.
- [ ] Lorsqu’elle a été explicitement définie à `nil`.
- [ ] Lorsqu’aucun type dynamique ne lui a été assigné.
- [ ] Elle ne peut pas être évaluée à `nil`.

#### Q68. Quelle valeur une variable `string` contient-elle si elle a été allouée mais non affectée ?

- [ ] nil
- [ ] undefined
- [ ] null
- [x] ""

> Si une variable string a été allouée mais non affectée, sa valeur par défaut est une chaîne vide "". En Go, les variables non initialisées reçoivent la valeur zéro de leur type, pour les chaînes c’est "".

#### Q69. Quelle fonction intégrée est utilisée pour arrêter la poursuite d’un programme ?

- [x] `panic`
- [ ] Il n’existe pas une telle fonction.
- [ ] `raiseException`
- [ ] `exit`

> La fonction intégrée utilisée pour arrêter un programme est `panic()`. Lorsqu’elle est appelée, elle déclenche une panique qui interrompt le flot normal du programme. Si elle n’est pas récupérée, le programme se termine.

#### Q70. Quelle sera la sortie ?

```go
a,b := 1, 2
b,c:= 3, 4
fmt.Println(a, b, c)
```

- [x] 1 3 4
- [ ] 1 2 3
- [ ] 1 2 4
- [ ] Cela ne compilera pas.

[Go Playground Example](https://go.dev/play/p/qUI50GNGWTq)

### Q71. Quel est l’opérateur pour une condition ET logique ?

- [ ] -
- [ ] and
- [x] &&
- [ ] ||

### Q72. Qu’est-ce qu’une fonction anonyme en Go ?

- [ ] Une fonction sans type de retour.
- [ ] Une fonction sans paramètres.
- [x] Une fonction sans nom.
- [ ] Une fonction déclarée à l’intérieur d’une autre fonction.

### Q73. Quel mot-clé est utilisé pour déclarer une fonction anonyme en Go ?

- [ ] `func`
- [ ] `lambda`
- [x] `func()`
- [ ] `anonymous`

#### Q74. Quel est l’avantage principal d’utiliser des fonctions anonymes en Go ?

- [ ] Elles ont toujours de meilleures performances que les fonctions nommées.
- [ ] Elles peuvent avoir plusieurs valeurs de retour.
- [x] Elles peuvent être définies en ligne là où elles sont utilisées.
- [ ] Elles ont une syntaxe plus courte que les fonctions nommées.

Explication : elles peuvent être définies en ligne là où elles sont utilisées, offrant plus de flexibilité d’organisation du code.

#### Q75. Quelle est la syntaxe pour appeler immédiatement une fonction anonyme après sa déclaration en Go ?

- [ ] `functionName(){}`
- [ ] `call functionName(){}`
- [x] `func(){}()`
- [ ] `execute func(){}`

[reference](https://stackoverflow.com/questions/6719089/javascript-anonymous-function-immediate-invocation-execution-expression-vs-dec)

#### Q76. Pour quels types les développeurs Go peuvent-ils définir des méthodes ?

- [x] tous les types nommés non intégrés à Go, tels que `type Example int` mais pas `int`, `type Example struct{...}` mais pas `struct`, etc.
- [ ] uniquement les types nommés `struct`, `map` et `slice`, tels que `type Example struct{…}`
- [ ] uniquement les types nommés `struct`, tels que `type Example struct{...}`
- [ ] tous les types

> Les méthodes peuvent être définies pour tout type nommé qui n’est pas un type intégré. Lorsqu’on crée un nouveau type via une déclaration `type`, il devient un type nommé, et on peut définir des méthodes spécifiques à ce type. Les méthodes ne peuvent pas être attachées directement aux types intégrés comme `int`, `string`, etc. [reference](https://go.dev/ref/spec#Method_declarations)
