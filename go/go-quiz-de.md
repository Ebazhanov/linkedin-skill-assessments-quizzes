## Go (Programming Language)

#### Q1. Was benötigen Sie, damit zwei Funktionen vom gleichen Typ sind?

- [x] Sie sollten dieselben Signaturen teilen, einschließlich Parametertypen und Rückgabetypen.
- [ ] Sie sollten dieselben Parametertypen teilen, können aber unterschiedliche Typen zurückgeben.
- [ ] Alle Funktionen sollten vom gleichen Typ sein.
- [ ] Die Funktionen sollten kein First-Class-Typ sein.

[User defined function types in Go (Golang)](https://golangbyexample.com/user-defined-function-type-go/)

#### Q2. Was gibt die Funktion `len()` zurück, wenn ihr eine UTF-8-kodierte Zeichenkette übergeben wird?

- [ ] die Anzahl der Zeichen
- [x] die Anzahl der Bytes
- [ ] Sie akzeptiert keine String-Typen.
- [ ] die Anzahl der Code Points

[Length of string in Go (Golang)](https://golangbyexample.com/length-of-string-golang/).

#### Q3. Welches ist KEINE gültige Schleifenkonstruktion in Go?

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

**Erklärung:** Go hat nur `for`-Schleifen

#### Q4. Wie fügen Sie die Zahl 3 rechts hinzu?

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

**Erklärung:** Slices in GO sind unveränderlich, sodass der Aufruf von `append` den Slice nicht modifiziert

#### Q5. Was ist der Wert von `Read`?

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
- [ ] ein zufälliger Wert

[IOTA in Go (Golang)](https://golangbyexample.com/iota-in-golang/)

#### Q6. Welches ist die EINZIGE gültige Import-Anweisung in Go?

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

#### Q7. Was würde passieren, wenn Sie versuchen würden, dieses Go-Programm zu kompilieren und auszuführen?

```go
package main
var GlobalFlag string
func main() {
  print("["+GlobalFlag+"]")
}
```

- [ ] Es würde nicht kompilieren, weil `GlobalFlag` nie initialisiert wurde.
- [x] Es würde kompilieren und `[]` ausgeben.
- [ ] Es würde kompilieren und nichts ausgeben, weil `"[" +nil+"]"` auch `nil` ist.
- [ ] Es würde kompilieren, aber dann panic auslösen, weil `GlobalFlag` nie initialisiert wurde.

1. [variables](https://golangbyexample.com/variables-in-golang-complete-guide/) in Go haben Anfangswerte. Für String-Typ ist es eine leere Zeichenkette.
2. [Go Playground](https://play.golang.org/p/TaRIzuD-nxC)

#### Q8. Von wo ist die Variable `myVar` zugänglich, wenn sie außerhalb aller Funktionen in einer Datei im Paket `myPackage` innerhalb des Moduls `myModule` deklariert ist?

- [x] Sie kann überall innerhalb von `myPackage` aufgerufen werden, nicht im Rest von myModule.
- [ ] Sie kann von jeder Anwendung aufgerufen werden, die `myModule` importiert.
- [ ] Sie kann von überall in `myModule` aufgerufen werden.
- [ ] Sie kann von anderen Paketen in `myModule` aufgerufen werden, solange sie `myPackage` importieren

**Erklärung**: Um die Variable außerhalb von `myPackage` verfügbar zu machen, ändern Sie den Namen in `MyVar`.
Siehe auch ein Beispiel für [Exported names](https://tour.golang.org/basics/3) in der Tour of Go.

#### Q9. Wie sagen Sie `go test`, dass es die auszuführenden Tests ausgeben soll?

- [ ] `go test`
- [ ] `go test -x`
- [ ] `go test --verbose`
- [x] `go test -v`

[test package](https://pkg.go.dev/cmd/go/internal/test)

#### Q10. Dieser Code gab `{0, 0}` aus. Wie können Sie es reparieren?

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

- [ ] `json.Decoder` verwenden
- [ ] Einen Zeiger auf `data` übergeben
- [x] `X` und `Y` exportieren (großschreiben)
- [ ] Feld-Tags verwenden

1. [How to Parse JSON in Golang?](https://www.geeksforgeeks.org/how-to-parse-json-in-golang/)
2. [Go Playground](https://play.golang.org/p/RdL6y3Zv8ke)

#### Q11. Was blockiert ein `sync.Mutex` während er gesperrt ist?

- [ ] alle Goroutinen
- [ ] jeden anderen Aufruf zum Sperren dieses `Mutex`
- [x] alle Lese- oder Schreibvorgänge der Variablen, die er sperrt
- [ ] alle Schreibvorgänge auf die Variable, die er sperrt

1. [Mutex in GoLang](https://golangdocs.com/mutex-in-golang), sync.Mutex sperrt, sodass immer nur eine Goroutine gleichzeitig auf die gesperrte Variable zugreifen kann.
2. [sync.Mutex](https://go.dev/tour/concurrency/9)

#### Q12. Was ist eine idiomatische Möglichkeit, die Ausführung des aktuellen Gültigkeitsbereichs anzuhalten, bis eine beliebige Anzahl von Goroutinen zurückgekehrt ist?

- [ ] Jedem eine `int` und einen `Mutex` übergeben und zählen, wenn sie zurückkehren.
- [ ] Über eine `select`-Anweisung iterieren.
- [ ] Für eine sichere Zeit schlafen.
- [x] `sync.WaitGroup`

**Erklärung:** Genau dafür ist `sync.WaitGroup` konzipiert - [Use sync.WaitGroup in Golang](https://nanxiao.me/en/use-sync-waitgroup-in-golang/)

#### Q13. Was ist ein Nebeneffekt der Verwendung von `time.After` in einer `select`-Anweisung?

- [ ] Es blockiert die anderen Kanäle.
- [ ] Es ist für die Verwendung in select-Anweisungen ohne Nebeneffekte gedacht.
- [ ] Es blockiert die `select`-Anweisung, bis die Zeit verstrichen ist.
- [x] Die Goroutine endet nicht, bis die Zeit verstrichen ist.

> Hinweis: Es blockiert `select` nicht und blockiert auch nicht die anderen Kanäle.

1. [time.After() Function in Golang With Examples](https://www.geeksforgeeks.org/time-after-function-in-golang-with-examples/)
2. [How can I use 'time.After' and 'default' in Golang?](https://stackoverflow.com/questions/39212333/how-can-i-use-time-after-and-default-in-golang)
3. [Go Playground example](https://go.dev/play/p/WojTrG1ywRK)

#### Q14. Wofür wird die select-Anweisung verwendet?

- [ ] gleichzeitige Ausführung einer Funktion
- [ ] Ausführung eines anderen Falls basierend auf dem Typ einer Variablen
- [ ] Ausführung eines anderen Falls basierend auf dem Wert einer Variablen
- [x] Ausführung eines anderen Falls basierend darauf, welcher Kanal zuerst zurückkehrt

[Select statement in GoLang](https://golangdocs.com/select-statement-in-golang)

#### Q15. Wie sollten Sie diese Funktion gemäß dem Go-Dokumentationsstandard dokumentieren?

```go
func Add(a, b int) int {
        return a + b
}
```

- [ ] A

  ```go
  // Calculate a + b
  // - a: int
  // - b: int
  // - returns: int
  func Add(a, b int) int {
          return a + b
  }
  ```

- [ ] B

  ```go
  // Does a + b
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

**Erklärung:** Der Dokumentationsblock sollte mit einem Funktionsnamen beginnen

[Comments in Go](https://exercism.org/tracks/go/concepts/comments)

#### Q16. Welche Einschränkung gibt es für den Typ von `var`, um `i := myVal.(int)?` zu kompilieren?

- [ ] `myVal` muss ein Integer-Typ sein, wie `int`, `int64`, `int32`, etc.
- [ ] `myVal` muss als `int` assertiert werden können.
- [x] `myVal` muss ein Interface sein.
- [ ] `myVal` muss ein numerischer Typ sein, wie `float64` oder `int64`.

**Erklärung**: Diese Art der Typumwandlung (mit `.(type)`) wird nur auf Interfaces angewendet.

1. [this example](https://tutorialedge.net/golang/snippets/type-casting-interface-to-string-go/)
2. [Primitive types are type-casted differently](https://golangdocs.com/type-casting-in-golang)
3. [Go Playground](https://play.golang.org/p/TXF_JBvThp6)
4. [Type assertions](https://go.dev/tour/methods/15)

#### Q17. Was ist ein Channel?

- [ ] eine globale Variable
- [x] ein Medium zum Senden von Werten zwischen Goroutinen
- [ ] ein dynamisches Array von Werten
- [ ] ein leichtgewichtiger Thread für gleichzeitige Programmierung

[Channels](https://tour.golang.org/concurrency/2)

#### Q18. Wie können Sie eine Datei so erstellen, dass sie nur unter Windows kompiliert wird?

- [ ] Prüfen Sie runtime.GOOS.
- [ ] Fügen Sie einen Kommentar // +build windows irgendwo in der Datei hinzu.
- [ ] Fügen Sie das Präfix \_ zum Dateinamen hinzu.
- [x] Fügen Sie einen Kommentar // +build windows am Anfang der Datei hinzu.

1. [How to use conditional compilation with the go build tool, Oct 2013](https://dave.cheney.net/2013/10/12/how-to-use-conditional-compilation-with-the-go-build-tool)
2. [go commands Build constraints](https://pkg.go.dev/cmd/go#hdr-Build_constraints)

> `//go:build windows`
> "Go-Versionen 1.16 und früher verwendeten eine andere Syntax für Build-Einschränkungen mit einem "// +build" Präfix. Der gofmt-Befehl fügt eine äquivalente //go:build Einschränkung hinzu, wenn er auf die ältere Syntax stößt."

#### Q19. Wie übergeben Sie dies korrekt als Body einer HTTP-POST-Anfrage?

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

#### Q20. Wie sollte der idiomatische Name für ein Interface mit einer einzelnen Methode und der Signatur `Save() error` lauten?

- [ ] Saveable
- [ ] SaveInterface
- [ ] ISave
- [x] Saver

[Effective Go, Interface names](https://golang.org/doc/effective_go#interface-names)

#### Q21. Eine `switch`-Anweisung **\_** ihren eigenen lexikalischen Block. Jede `case`-Anweisung **\_** einen zusätzlichen lexikalischen Block

- [ ] erstellt nicht; erstellt
- [ ] erstellt nicht; erstellt nicht
- [x] erstellt; erstellt
- [ ] erstellt; erstellt nicht

[Go Language Core technology (Volume one) 1.5-scope](https://topic.alibabacloud.com/a/go-language-core-technology-volume-one-15-font-colorredscopefont_1_38_30923325.html)

Relevant excerpt from the article:

> _The second if statement is nested inside the first, so a variable declared in the first if statement is visible to the second if statement. There are similar rules in switch: Each case has its own lexical block in addition to the conditional lexical block._

#### Q22. Was ist die Standard-Groß-/Kleinschreibung der JSON `Unmarshal`-Funktion?

- [x] Das Standardverhalten ist Groß-/Kleinschreibung unabhängig, aber es kann überschrieben werden.
- [ ] Felder werden Groß-/Kleinschreibung berücksichtigt zugeordnet.
- [ ] Felder werden Groß-/Kleinschreibung unabhängig zugeordnet.
- [ ] Das Standardverhalten ist Groß-/Kleinschreibung berücksichtigt, aber es kann überschrieben werden.

[encoding/json#Unmarshal](https://pkg.go.dev/encoding/json#Unmarshal)

Relevant excerpt from the article:

> _To unmarshal JSON into a struct, Unmarshal matches incoming object keys to the keys used by Marshal (either the struct field name or its tag), preferring an exact match but also accepting a case-insensitive match. By default, object keys which don't have a corresponding struct field are ignored (see Decoder.DisallowUnknownFields for an alternative)._

#### Q23. Was ist der Unterschied zwischen den Methoden `Time.Sub()` und `Time.Add()` des `time`-Pakets?

- [ ] Time.Add() dient zur Addition, während Time.Sub() zur Verschachtelung von Zeitstempeln dient.
- [ ] Time.Add() gibt immer eine spätere Zeit zurück, während time.Sub immer eine frühere Zeit zurückgibt.
- [ ] Sie sind gegensätzlich. Time.Add(x) ist äquivalent zu Time.Sub(-x).
- [x] Time.Add() akzeptiert einen Duration-Parameter und gibt eine Time zurück, während Time.Sub() einen Time-Parameter akzeptiert und eine Duration zurückgibt.

1. [time#Time.Add](https://pkg.go.dev/time#Time.Add)
2. [time#Time.Sub](https://pkg.go.dev/time#Time.Sub)

#### Q24. Was ist das Risiko der Verwendung mehrerer Feld-Tags in einer einzelnen Struktur?

- [ ] Jedes Feld muss alle Tags haben, um kompilieren zu können.
- [x] Es koppelt verschiedene Schichten Ihrer Anwendung eng miteinander.
- [ ] Alle Tags nach dem ersten werden ignoriert.
- [ ] Fehlende Tags lösen zur Laufzeit eine Panik aus.

1. [Example Code / b29r0fUD1cp](https://play.golang.org/p/b29r0fUD1cp)
2. [How To Use Struct Tags in Go](https://www.digitalocean.com/community/tutorials/how-to-use-struct-tags-in-go)

#### Q25. Wo ist die eingebaute recover-Methode nützlich?

- [ ] in der main-Funktion
- [ ] direkt nach einer Zeile, die eine Panik auslösen könnte
- [x] innerhalb einer deferred-Funktion
- [ ] am Anfang einer Funktion, die eine Panik auslösen könnte

[Example of Recover Function in Go (Golang)](https://golangbot.com/panic-and-recover/#recoveringfromapanic)

Relevant excerpt from the article:

> _Recover is useful only when called inside deferred functions. Executing a call to recover inside a deferred function stops the panicking sequence by restoring normal execution and retrieves the error message passed to the panic function call. If recover is called outside the deferred function, it will not stop a panicking sequence._

#### Q26. Welche Option sendet keine Ausgabe nach Standardfehler?

- [ ] `println(message)`
- [ ] `log.New(os.Stderr, "", 0).Println(message)`
- [x] `fmt.Errorf("%s\n", message)`
- [ ] `fmt.Fprintln(os.Stderr, message)`

1. [func println](https://pkg.go.dev/builtin#println): writes the result to _standard error_.
2. [func New](https://pkg.go.dev/log#New): func New(out io.Writer, prefix string, flag int) \*Logger; the out variable _sets the destination_ to which log data will be written.
3. [func Errorf](https://pkg.go.dev/fmt#Errorf): Errorf formats according to a format specifier and _returns the string_ as a value.
4. [func Fprintln](https://pkg.go.dev/fmt#Fprintln): func Fprintln(w io.Writer, a ...any) (n int, err error); Fprintln formats using the default formats for its operands and _writes to w_.

#### Q27. Wie können Sie Go mitteilen, ein Paket von einem anderen Speicherort zu importieren?

- [ ] Verwenden Sie einen Proxy.
- [ ] Ändern Sie den Import-Pfad.
- [x] Verwenden Sie eine replace-Direktive in go.mod.
- [ ] Verwenden Sie ein replace-Verzeichnis.

1. [Call your code from another module](https://go.dev/doc/tutorial/call-module-code): chapter 5., `go mod edit -replace example.com/greetings=../greetings`.
2. [go.mod replace directive](https://go.dev/doc/modules/gomod-ref#replace)

#### Q28. Wenn sich Ihr aktuelles Arbeitsverzeichnis auf der obersten Ebene Ihres Projekts befindet, welcher Befehl führt alle Test-Pakete aus?

- [ ] `go test all`
- [ ] `go run --all`
- [ ] `go test .`
- [x] `go test ./...`

1. [Example of testing in Go (Golang)](https://pkg.go.dev/testing)
2. [Example of cmd in Go (Golang)](https://pkg.go.dev/cmd/go)

Relevant excerpt from the article:

> _Relative patterns are also allowed, like "go test ./..." to test all subdirectories._

#### Q29. Welche Kodierungen können Sie in einer Zeichenkette verwenden?

- [ ] beliebige, sie akzeptiert beliebige Bytes
- [ ] jede Unicode-Format
- [ ] UTF-8 oder ASCII
- [x] UTF-8

1. [Strings, bytes, runes and characters in Go](https://go.dev/blog/strings)

Relevant excerpt from the article:

> _In short, Go source code is UTF-8, so the source code for the string literal is UTF-8 text._

2. [Example of encoding in Go (Golang)](https://pkg.go.dev/golang.org/x/text/encoding)

Relevant excerpt from the article:

> _Package encoding defines an interface for character encodings, such as Shift JIS and Windows 1252, that can convert to and from UTF-8._

#### Q30. Wie unterscheidet sich das Verhalten von `t.Fatal` innerhalb eines `t.Run`?

- [ ] Es gibt keinen Unterschied.
- [ ] t.Fatal stürzt das Test-Harness nicht ab, wodurch Ausgabemeldungen erhalten bleiben.
- [x] t.Fatal stoppt die Ausführung des Subtests und fährt mit anderen Testfällen fort.
- [ ] t.Fatal stoppt alle Tests und enthält zusätzliche Informationen über den fehlgeschlagenen Subtest.

1. [Reference:](https://go.dev/play/p/gtne3iRL9AX)
2. [testing package in Go](https://pkg.go.dev/testing), the relevant excerpt from the article:

> `Fatal` is equivalent to `Log` followed by `FailNow`.
> `Log` formats its arguments using default formatting, analogous to `Println`, and records the text in the error log.
> `FailNow` marks the function as having failed and **stops its execution by calling `runtime.Goexit` (which then runs all deferred calls in the current goroutine). Execution will continue at the next test or benchmark.** `FailNow` must be called from the goroutine running the test or benchmark function, not from other goroutines created during the test. Calling `FailNow` does not stop those other goroutines.
> `Run` runs `f` as a subtest of `t` called name. It runs `f` in a separate goroutine and blocks until `f` returns or calls `t.Parallel` to become a parallel test. Run reports whether `f` succeeded (or at least did not fail before calling `t.Parallel`).
> Run may be called simultaneously from multiple goroutines, but all such calls must return before the outer test function for t returns.

#### Q31. Was macht `log.Fatal`?

- [ ] Es löst eine Panik aus.
- [ ] Es gibt das Protokoll aus und löst dann eine Panik aus.
- [x] Es gibt das Protokoll aus und beendet das Programm sicher.
- [ ] Es beendet das Programm.

[Example of func Fatal in Go (Golang)](https://pkg.go.dev/log#Fatal)

Relevant excerpt from the article:

> _`Fatal` is equivalent to `Print()` followed by a call to `os.Exit(1)`._

#### Q32. Welches ist ein gültiges Go-Zeitformatliteral?

- [x] "2006-01-02"
- [ ] "YYYY-mm-dd"
- [ ] "y-mo-d"
- [ ] "year-month-day"

[func Time in Go](https://pkg.go.dev/time#pkg-constants)

Relevant excerpt from the article:

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

#### Q33. Wie sollten Sie einen Fehler (err) protokollieren?

- [ ] `log.Error(err)`
- [x] `log.Printf("error: %v", err)`
- [ ] `log.Printf(log.ERROR, err)`
- [ ] `log.Print("error: %v", err)`

**Erklärung:** Es ist weder _log.ERROR_ noch _log.Error()_ in [log package in Go](https://pkg.go.dev/log) definiert; `log.Print()` Argumente werden wie bei `fmt.Print()` behandelt; `log.Printf()` Argumente werden wie bei `fmt.Printf()` behandelt.

#### Q34. Welche Dateinamen erkennt der `go test` Befehl als Testdateien?

- [ ] alle, die mit `test` beginnen
- [ ] alle Dateien, die das Wort `test` enthalten
- [ ] nur Dateien im Stammverzeichnis, die auf `_test.go` enden
- [x] alle, die auf `_test.go` enden

1. [Test packages in go command in Go](https://pkg.go.dev/cmd/go#hdr-Test_packages): _'Go test' recompiles each package along with any files with names matching the file pattern "\*\_test.go"._
2. [Add a test in Go](https://go.dev/doc/tutorial/add-a-test)

#### Q35. Was wird die Ausgabe dieses Codes sein?

```go
ch := make(chan int)
ch <- 7
val := <-ch
fmt.Println(val)
```

- [ ] 0
- [x] Es wird ein Deadlock auftreten
- [ ] Es wird nicht kompilieren
- [ ] 2.718

[Go Playground share](https://go.dev/play/p/SQlfg8YSEOz), output:

```text
fatal error: all goroutines are asleep - deadlock!

goroutine 1 [chan send]:
main.main()
 /tmp/sandbox2282523250/prog.go:7 +0x37

Program exited.
```

#### Q36. Was wird die Ausgabe dieses Programms sein?

```go
ch := make(chan int)
close(ch)
val := <-ch
fmt.Println(val)
```

- [ ] Es wird ein Deadlock auftreten
- [ ] Es wird eine Panik auslösen
- [x] 0
- [ ] NaN

1. [The Go Programming Language Specification "Receive operator"](https://go.dev/ref/spec#Receive_operator), Relevant excerpt from the article:

   > _A receive operation on a closed channel can always proceed immediately, yielding the element type's zero value after any previously sent values have been received._

2. [Go Playground share](https://go.dev/play/p/DjXq9wzJm5M), output:

```text
0

Program exited.
```

#### Q37. Was wird in diesem Code ausgegeben?

```go
var stocks map[string]float64 // stock -> price
price := stocks["MSFT"]
fmt.Printf("%f\n", price)
```

- [ ] 0
- [x] 0.000000
- [ ] Der Code wird eine Panik auslösen
- [ ] NaN

[Go Playground share](https://go.dev/play/p/CjdHskV1xq1), output:

```text
0.000000

Program exited.
```

#### Q38. Was ist die gängige Methode, mehrere ausführbare Dateien in Ihrem Projekt zu haben?

- [x] Ein cmd-Verzeichnis und ein Verzeichnis pro ausführbarer Datei darin zu haben.
- [ ] main auskommentieren.
- [ ] Build-Tags verwenden.
- [ ] Ein pkg-Verzeichnis und ein Verzeichnis pro ausführbarer Datei darin zu haben.

1. [stackoverflow](https://stackoverflow.com/questions/9985559/organizing-a-multiple-file-go-project/51942843#51942843)
2. [medium](https://medium.com/@benbjohnson/structuring-applications-in-go-3b04be4ff091)
3. [medium](https://medium.com/golang-learn/go-project-layout-e5213cdcfaa2)

#### Q39. Wie können Sie main.go in eine ausführbare Datei kompilieren, die auf OSX arm64 läuft?

- [ ] Setzen Sie GOOS auf **arm64** und GOARCH auf **darwin**.
- [ ] Setzen Sie GOOS auf **osx** und GOARCH auf **arm64**.
- [ ] Setzen Sie GOOS auf **arm64** und GOARCH auf **osx**.
- [x] Setzen Sie GOOS auf **darwin** und GOARCH auf **arm64**.

[documentation](https://pkg.go.dev/cmd/go#hdr-Build_constraints)

#### Q40. Was ist die korrekte Syntax, um eine Goroutine zu starten, die `Hello Gopher!` ausgeben wird?

- [ ] `go(fmt.Println("Hello Gopher!"))`
- [ ] `go func() { fmt.Println("Hello Gopher!") }`
- [x] `go fmt.Println("Hello Gopher!")`
- [ ] `Go fmt.Println("Hello Gopher!")`

[Example of start a goroutine](https://go.dev/play/p/KGgnAWpZMrS)

#### Q41. Wenn Sie über eine Map in einer for-range-Schleife iterieren, in welcher Reihenfolge werden die Schlüssel:Wert-Paare abgerufen?

- [x] in pseudo-zufälliger Reihenfolge, die nicht vorhergesagt werden kann
- [ ] in umgekehrter Reihenfolge, wie sie hinzugefügt wurden, last in first out
- [ ] sortiert nach Schlüssel in aufsteigender Reihenfolge
- [ ] in der Reihenfolge, wie sie hinzugefügt wurden, first in first out

[Reference](https://go.dev/ref/spec#:~:text=The%20iteration%20order%20over%20maps%20is%20not%20specified)

#### Q42. Was ist eine idiomatische Möglichkeit, die Darstellung einer benutzerdefinierten Struktur in einer formatierten Zeichenkette anzupassen?

- [ ] Es gibt keine Anpassung der Zeichenketten-Darstellung eines Typs.
- [ ] Stück für Stück aufbauen, indem Sie jedes Mal einzelne Felder aufrufen.
- [x] Eine Methode `String()` string implementieren
- [ ] Eine Wrapper-Funktion erstellen, die Ihren Typ akzeptiert und eine Zeichenkette ausgibt.

[Reference](https://go.dev/doc/effective_go#printing)

#### Q43. Wie können Sie ein Goroutine-Leck in diesem Code vermeiden?

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

- [ ] Verwenden Sie einen sync.WaitGroup.
- [x] Machen Sie ch zu einem gepufferten Channel.
- [ ] Fügen Sie einen default-Fall zum select hinzu.
- [ ] Verwenden Sie runtime.SetFinalizer.

[Reference](https://www.ardanlabs.com/blog/2018/11/goroutine-leaks-the-forgotten-sender.html)

Relevant excerpt from the article:

> _The simplest way to resolve this leak is to change the channel from an unbuffered channel to a buffered channel with a capacity of 1. Now in the timeout case, after the receiver has moved on, the Goroutine will complete its send by placing the \*User value in the channel then it will return._

#### 44. Was wird dieser Code ausgeben?

```go
var i int8 = 120
i += 10
fmt.Println(i)
```

- [x] -126
- [ ] 0
- [ ] NaN
- [ ] 130

[Go Playground example](https://go.dev/play/p/T31_JuFioaC), output:

```text
-126

Program exited.
```

#### 45. Angenommen, die Definition von worker lautet wie folgt, was ist die richtige Syntax, um eine Goroutine zu starten, die worker aufruft und das Ergebnis an einen Channel namens ch sendet?

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

#### Q46. Welche Namen sind in diesem Code exportiert?

```go
package os

type FilePermission int
type userID int
```

- [x] FilePermission
- [ ] keine dieser Antworten
- [ ] FilePermission und userID
- [ ] userID

[Reference 1](https://www.ardanlabs.com/blog/2018/11/goroutine-leaks-the-forgotten-sender.html)
[Reference 2](https://go.dev/tour/basics/3)

#### Q47. Welches der Folgenden ist korrekt über Strukturen in Go?

- [ ] Struktur ist ein weiterer benutzerdefinierter Datentyp, der in der Go-Programmierung verfügbar ist, der es ermöglicht, Datenelemente verschiedener Art zu kombinieren.
- [ ] Strukturen werden verwendet, um einen Datensatz darzustellen
- [ ] Um eine Struktur zu definieren, müssen Sie type- und struct-Anweisungen verwenden.
- [x] Alle oben genannten

#### Q48. Was macht der eingebaute `generate` Befehl des Go-Compilers?

- [ ] Er stellt Unterbefehle `sql`, `json`, `yaml` und Schalter `--schema` und `--objects` bereit, um relevanten Code zu generieren.
- [ ] Er sucht nach Dateien mit Namen, die auf `_generate.go` enden, und kompiliert und führt dann jede dieser Dateien einzeln aus.
- [x] Er scannt den Quellcode des Projekts nach `//go:generate` Kommentaren und führt für jeden solchen Kommentar den Terminal-Befehl aus, den er angibt.
- [ ] Er hat Unterbefehle `mocks` und `tests`, um relevante `.go` Quelldateien zu generieren.

[Generate Go files by processing source](https://pkg.go.dev/cmd/go#hdr-Generate_Go_files_by_processing_source)

#### Q49. Wie können Sie mit dem time-Paket die Zeit 90 Minuten ab jetzt erhalten?

- [ ] `time.Now().Add(90)`
- [ ] `time.Now() + (90 * time.Minute)`
- [ ] `time.Now() + 90`
- [x] `time.Now().Add(90 * time.Minute)`

[func (Time) Add example](https://pkg.go.dev/time#example-Time.Add)

#### Q50. Ein Programm verwendet einen Channel, um fünf Ganzzahlen in einer Goroutine auszugeben, während der Channel mit Ganzzahlen aus der Hauptroutine gefüttert wird, aber es funktioniert nicht wie es ist. Was müssen Sie ändern, damit es funktioniert?

- [ ] Fügen Sie `close(ch)` direkt nach `wg.Wait()` hinzu.
- [x] Fügen Sie einen zweiten Parameter zu `make(chan, int)` hinzu, z. B. `make(chan int, 5)`.
- [ ] Entfernen Sie die Verwendung unnötiger `WaitGroup` Aufrufe, z. B. alle Zeilen, die mit `wg` beginnen.
- [ ] Verschieben Sie die 7-Zeilen-Goroutine direkt nach `wg.Add(1)` zu einer Zeile direkt vor `wg.Wait()`.

[Reference](https://www.ardanlabs.com/blog/2018/11/goroutine-leaks-the-forgotten-sender.html)

Relevant excerpt from the article:

> _The simplest way to resolve this leak is to change the channel from an unbuffered channel to a buffered channel with a capacity of 1. Now in the timeout case, after the receiver has moved on, the Goroutine will complete its send by placing the \*User value in the channel then it will return._

#### Q51. Wie greifen Sie nach dem Import von `encoding/json` auf die `Marshal` Funktion zu?

- [ ] `encoding.json.Marshal`
- [ ] `encoding/json.Marshal`
- [ ] `Marshal`
- [x] `json.Marshal`

[encoding/json#Marshal example](https://pkg.go.dev/encoding/json#example-Marshal)

#### Q52. Was sind die beiden fehlenden Codeteile, die die Verwendung von `context.Context` vervollständigen würden, um ein drei-Sekunden-Timeout für diesen HTTP-Client bei einer GET-Anfrage zu implementieren?

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

#### Q53. Wenn Sie eine Struktur namens Client in derselben .go-Datei wie die Anweisung definiert haben, wie exportieren Sie eine Variable mit einem Standardwert, damit die Variable von anderen Paketen zugänglich ist?

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

#### Q54. Dieses Programm gibt `{Master Chief Spartan Protagonist Halo}` aus. Wie würden Sie es so ändern, dass es stattdessen `Master Chief - a Spartan - is the Protagonist of Halo` ausgibt?

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
  // Replace
  // fmt.Println(mc)
  // with this:

  fmt.Printf("(?P<Name>) - a (?P<Class>) - is the (?P<Role>) of (?P<Game>)", mc)
  ```

- [ ] B

  ```go
  // Replace
  // fmt.Println(mc)
  // with this:
  fmt.Println(mc, func(c Character) string {
        return c. Name + " - a " + c.Class + " - is the " + c.Role + " of " + c.Game
  })
  ```

- [x] C

  ```go
  // add this to the package `main`

  func (c Character) String() string {
        return fmt.Sprintf("%s - a %s - is the %s of %s", c.Name, c.Class, c.Role,c.Game)
  }
  ```

- [ ] D

  ```go
   // add this to the package `main`

  func (c Character) OnPrint() {
        fmt.Println("{{c.Name}} - a {{c.Class}} - is the {{c.Role}} of {{c.Game}}")
  }
  ```

1. [fmt#Stringer](https://pkg.go.dev/fmt#Stringer)

#### Q55. Wie würden Sie eine funktionierende `Append()` Methode für `Clients` implementieren?

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

#### Q55. Wie würden Sie eine funktionierende `Append()`-Methode für `Clients` implementieren?

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

#### Q56. Wie würden Sie sich von einem durch eine aufgerufene Funktion ausgelösten `panic()` erholen, ohne dass Ihr Programm fehlschlägt, wobei davon ausgegangen wird, dass Ihre Antwort im selben Scope ausgeführt wird, in dem Ihr Funktionsaufruf den Panic erfährt?

- [ ] Umhüllen Sie den Funktionsaufruf in eine anonyme Funktion mit einem Rückgabetyp von `panic` und denken Sie daran, die anonyme Funktion durch das Suffix `()` aufzurufen, und untersuchen Sie dann die zurückgegebene `panic`-Instanz, um den Fehler zu behandeln.

- [ ] Verwenden Sie `try{ ... }`, um den Code, der die Funktion aufruft, zu umschließen und behandeln Sie dann den Fehler innerhalb des `catch{ ... }`.

- [x] Verwenden Sie `defer func { ... }()` vor dem fehlerhaften Funktionsaufruf und behandeln Sie die Panic innerhalb der anonymen Funktion.

- [ ] Präfixieren Sie den Funktionsaufruf mit `@`, um die Panic als `error`-Wert zurückzugeben, und behandeln Sie den Fehler dann so, wie Sie einen von einer Funktion zurückgegebenen `error` behandeln würden.

#### Q57. Was wird dieser Code ausgeben?

```go
var n int
fmt.Println (n)
```

- [x] 0
- [ ] nil
- [ ] a random value
- [ ] 1

> In Go erhält eine deklarierte, aber nicht initialisierte Variable den [Zero Value](https://go.dev/tour/basics/12) ihres Typs. Für Ganzzahlen wie `n` ist der Zero Value 0.

#### Q58. Welchen Verb sollten Sie für einen formatierten String verwenden, um die Methode `String() string` eines benutzerdefinierten Typs aufzurufen?

- [x] %s
- [ ] %b
- [ ] %v
- [ ] %string

> In Go wird der Verb `%s` verwendet, um einen String zu formatieren. Bei einem benutzerdefinierten Typ mit definierter `String()`-Methode wird diese automatisch aufgerufen, und ihr Rückgabewert wird im formatierten String verwendet.

#### Q59. Welcher Wert ist kein gültiges Layout beim Aufruf von `time.Now().Format(layout)`?

- [ ] time.REC3339
- [x] "1970-01-01"
- [ ] "Jan 2nd 2006"
- [ ] time.Kitchen

[time#Time.Format](https://pkg.go.dev/time#Time.Format)

Laut Dokumentation repräsentieren die Werte 1 und 01 den aktuellen Monat.

```text
each layout string is a representation of the time stamp,
	Jan 2 15:04:05 2006 MST
An easy way to remember this value is that it holds, when presented in this order, the values (lined up with the elements above):
	  1 2  3  4  5    6  -7
```

#### Q60. Wie signalisieren Sie dem Go-Compiler, dass die Struktur `Namespace` das Interface `JSONConverter` implementieren muss? Es wird angenommen, dass die Antwort im selben Package enthalten ist, in dem `Namespace` deklariert ist.

- [ ] var \_ JSONConverter = nil. (\*Namespace)
- [x] var \_ JSONConverter = (\*Namespace) (nil)
- [ ] type Namespace struct {
      implements JSONConverter
      // The rest of the struct declaration goes here
      }
- [ ] type Namespace struct {
      JSONConverter
      // The rest of the struct declaration goes here
      }

> Diese Syntax erstellt eine Variable `_` vom Typ `JSONConverter` und weist ihr den Wert `(*Namespace)(nil)` zu. Dadurch wird sichergestellt, dass `Namespace` das Interface `JSONConverter` erfüllt, indem überprüft wird, dass es einer Variablen vom Typ `JSONConverter` zugewiesen werden kann.

#### Q61. Welche Aussage über Typisierung und Interfaces ist falsch?

- [ ] Eine Methodensignatur ist die Kombination aus Methodenname und den Typen der deklarierten Parameter und Rückgabewerte.
- [x] Eine Struktur muss explizit mit dem Schlüsselwort `implements` deklarieren, dass ihre Instanzen überall verwendet werden können, wo eine Variable, ein Parameter und/oder ein Rückgabewert für das deklarierte Interface typisiert ist.
- [ ] Ein Interface deklariert eine Liste von Methoden und deren Signaturen, die ein Typ implementieren muss, um mit Werten kompatibel zu sein, die für dieses Interface typisiert sind.
- [ ] Variablen, Parameter und Rückgabewerte müssen „typisiert“ sein als 1) ein Built-in-Typ, 2) ein Type Alias, 3) ein abgeleiteter Typ, 4) ein zusammengesetzter Typ oder

5. ein Interface.

> In Go erfüllt ein Typ automatisch ein Interface, wenn er alle Methoden dieses Interfaces implementiert. Es ist nicht erforderlich, explizit zu deklarieren, dass eine Struktur ein Interface mit einem speziellen Schlüsselwort implementiert.

#### Q62. Wie würden Sie dieses Programm vervollständigen, um die angegebene Ausgabe zu erzeugen, vorausgesetzt, die SQL-Tabelle ist gegeben?

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

#### Q63. Füllen Sie die Lücken aus

1.  Testdateien in Go müssen **\_**.
2.  Einzelne Tests werden identifiziert durch **\_**.
3.  Sie können Subtests ausführen, indem Sie **\_\_**.
4.  Sie protokollieren den Fehler und markieren den Test als fehlgeschlagen, indem Sie **\_**.

- [ ] im Unterverzeichnis `/test/` dieses Packages gespeichert sein
      <br/>Funktionen, die einen `testing.Tester`-Parameter akzeptieren
      <br/>Funktionen schreiben, deren Namen `^Subtest` entsprechen
      <br/>`testing.AssertionFailed` aufrufen

- [x] auf `_test.go` enden
      <br/>Funktionsnamen, die `^Test[A-Z]` entsprechen
      <br/>`t.Run()` aufrufen
      <br/>`t.Errorf()` aufrufen

- [ ] mit `test_` beginnen
      <br/>Funktionen, die `[a-z]Test$` entsprechen
      <br/>`testing.Subtest()` aufrufen
      <br/>`testing.Assert()` erlauben, seine Assertion fehlschlagen zu lassen

- [ ] im Wurzelunterverzeichnis `/test/` des Projekts gespeichert sein
      <br/>Funktionen akzeptieren einen `testing.Test`-Parameter
      <br/>Closures an `testing.AddSubtest()` übergeben
      <br/>einen `error` aus der Funktion zurückgeben

#### Q64. Für welchen Typ ist ein `rune` ein Alias?

- [ ] char
- [ ] byte
- [x] int32
- [ ] string

1. [Strings, Bytes, Runes und Zeichen in Go](https://go.dev/blog/strings)

Relevanter Auszug aus dem Artikel:

> Der Begriff `rune` ist in Go ein Alias für den Typ `int32`, damit Programme klar machen können, wenn ein ganzzahliger Wert einen Code Point darstellt.

#### Q65. Wann können Sie die Syntax `:=` verwenden, um mehreren Variablen zuzuweisen? Zum Beispiel:

```go
x, err := myFunc()
```

- [x] wenn mindestens eine davon in diesem lexikalischen Block noch nicht deklariert wurde
- [ ] jederzeit, da vorhandene Variablen überschrieben werden
- [ ] wenn keine Variablen mit diesen Namen zugänglich sind
- [ ] wenn keine der Variablen in diesem lexikalischen Block existiert

1. [Short variable declarations](https://go.dev/ref/spec#Short_variable_declarations)

#### Q66. Wie können Sie die Profiler-Ausgabe in `cpu.pprof` im Browser ansehen?

- [ ] go pprof -to SVG cpu.prof
- [x] go tool pprof -http=:8080 cpu.pprof (true)
- [ ] go tool pprof cpu.pprof
- [ ] go tool trace cpu.pprof

#### Q67. Wann ergibt eine Variable vom Typ `interface{}` den Wert `nil`?

- [x] Ihr wurde ein dynamischer Typ zugewiesen, dessen Wert `nil` ist. (true)
- [ ] Sie wurde explizit auf `nil` gesetzt.
- [ ] Ihr wurde kein dynamischer Typ zugewiesen.
- [ ] Sie kann nicht `nil` sein.

#### Q68. Welchen Wert hält eine String-Variable, wenn sie alloziert, aber nicht zugewiesen wurde?

- [ ] nil
- [ ] undefined
- [ ] null
- [x] ""

> Wenn eine String-Variable alloziert, aber nicht zugewiesen wurde, ist ihr Standardwert der leere String "". In Go erhalten nicht initialisierte String-Variablen den Zero Value ihres Typs, der für Strings der leere String ist.

#### Q69. Welche eingebaute Funktion wird verwendet, um ein Programm am Weiterlaufen zu hindern?

- [x] panic
- [ ] There is no such function.
- [ ] raiseException
- [ ] exit

> Die eingebaute Funktion zum Anhalten des Programms ist `panic()`. Ein Aufruf von `panic()` löst eine Panic aus und beendet den normalen Ausführungsfluss. Wenn sie nicht abgefangen wird, beendet das Programm.

#### Q70. Was wird die Ausgabe sein?

```go
a,b := 1, 2
b,c:= 3, 4
fmt.Println(a, b, c)
```

- [x] 1 3 4
- [ ] 1 2 3
- [ ] 1 2 4
- [ ] It will not compile.

[Go Playground Example](https://go.dev/play/p/qUI50GNGWTq)

### Q71. Was ist der Operator für eine logische UND-Bedingung?

- [ ] \+
- [ ] and
- [x] &&
- [ ] ||

### Q72. Was ist eine anonyme Funktion in Go?

- [ ] Eine Funktion ohne Rückgabetyp.
- [ ] Eine Funktion ohne Parameter.
- [x] Eine Funktion ohne Namen.
- [ ] Eine Funktion, die innerhalb einer anderen Funktion deklariert wird.

### Q73. Welches Schlüsselwort wird verwendet, um eine anonyme Funktion in Go zu deklarieren?

- [ ] `func`
- [ ] `lambda`
- [x] `func()`
- [ ] `anonymous`

#### Q74. Was ist der Hauptvorteil der Verwendung anonymer Funktionen in Go?

- [ ] Sie haben immer bessere Performance als benannte Funktionen.
- [ ] Sie können mehrere Rückgabewerte haben.
- [x] Sie können inline dort definiert werden, wo sie verwendet werden.
- [ ] Sie haben eine kürzere Syntax als benannte Funktionen.

Erläuterung: Sie können inline dort definiert werden, wo sie verwendet werden, was mehr Flexibilität in der Codeorganisation bietet.

#### Q75. Wie ist die Syntax, um eine anonyme Funktion unmittelbar nach ihrer Deklaration in Go aufzurufen?

- [ ] `functionName(){}`
- [ ] `call functionName()`
- [x] `func(){}()`
- [ ] `execute func(){}`

[reference](https://stackoverflow.com/questions/6719089/javascript-anonymous-function-immediate-invocation-execution-expression-vs-dec)

#### Q76. Für welche Typen können Go-Entwickler Methoden definieren?

- [x] `all named types not built-in to Go, such as type Example int but not int, type Example struct{...} but not struct, etc.`
- [ ] `only types named struct, map, and slice, such as type Example struct{…}`
- [ ] `only types named struct, such as type Example struct{...}`
- [ ] `all types`

> Methoden können für jeden benannten Typ definiert werden, der kein Built-in-Typ ist. Wenn Sie mit einer Typdeklaration einen neuen Typ erstellen, wird er zu einem benannten Typ, und Sie können spezifische Methoden dafür definieren. An Built-in-Typen wie `int`, `string` etc. können jedoch keine Methoden direkt angefügt werden. [reference](https://go.dev/ref/spec#Method_declarations)
