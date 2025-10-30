## Go (Programming Language)

#### Q1. Di cosa hanno bisogno due funzioni per essere dello stesso tipo?

- [x] Devono avere la stessa firma, inclusi tipi dei parametri e dei valori di ritorno.
- [ ] Devono avere gli stessi tipi di parametri ma possono restituire tipi diversi.
- [ ] Tutte le funzioni devono essere dello stesso tipo.
- [ ] Le funzioni non dovrebbero essere un tipo di prima classe.

[User defined function types in Go (Golang)](https://golangbyexample.com/user-defined-function-type-go/)

#### Q2. Cosa restituisce la funzione `len()` se le viene passata una stringa codificata in UTF-8?

- [ ] il numero di caratteri
- [x] il numero di byte
- [ ] Non accetta tipi string.
- [ ] il numero di code point

[Length of string in Go (Golang)](https://golangbyexample.com/length-of-string-golang/).

#### Q3. Quale NON è una costruzione di ciclo valida in Go?

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

**Spiegazione:** Go ha solo cicli `for`.

#### Q4. Come aggiungeresti il numero 3 a destra?

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

**Spiegazione:** le slice in Go sono immutabili, quindi chiamare `append` non modifica la slice.

#### Q5. Qual è il valore di `Read`?

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
- [ ] un valore casuale

[IOTA in Go (Golang)](https://golangbyexample.com/iota-in-golang/)

#### Q6. Qual è l’unica istruzione di import valida in Go?

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

#### Q7. Cosa succede se provi a compilare ed eseguire questo programma Go?

```go
package main
var GlobalFlag string
func main() {
  print("["+GlobalFlag+"]")
}
```

- [ ] Non compilerebbe perché `GlobalFlag` non è mai stata inizializzata.
- [x] Compilerebbe e stamperebbe `[]`.
- [ ] Compilerebbe e non stamperebbe nulla perché `"[" +nil+"]"` è anche `nil`.
- [ ] Compilerebbe ma andrebbe in panic perché `GlobalFlag` non è mai stata inizializzata.

1. Le [variabili](https://golangbyexample.com/variables-in-golang-complete-guide/) in Go hanno valori iniziali. Per il tipo string è la stringa vuota.
2. [Go Playground](https://play.golang.org/p/TaRIzuD-nxC)

#### Q8. Da dove è accessibile la variabile `myVar` se è dichiarata fuori da qualsiasi funzione in un file nel package `myPackage` dentro il modulo `myModule`?

- [x] È accessibile ovunque dentro `myPackage`, non nel resto di `myModule`.
- [ ] È accessibile da qualsiasi applicazione che importi `myModule`.
- [ ] È accessibile da ovunque in `myModule`.
- [ ] È accessibile da altri package in `myModule` se importano `myPackage`.

**Spiegazione**: per rendere la variabile disponibile fuori da `myPackage` cambia il nome in `MyVar`.
Vedi anche un esempio di [Exported names](https://tour.golang.org/basics/3) nel Tour of Go.

#### Q9. Come dici a `go test` di stampare i test che sta eseguendo?

- [ ] `go test`
- [ ] `go test -x`
- [ ] `go test --verbose`
- [x] `go test -v`

[test package](https://pkg.go.dev/cmd/go/internal/test)

#### Q10. Questo codice ha stampato `{0, 0}`. Come lo correggi?

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

- [ ] usa `json.Decoder`
- [ ] Passa un puntatore a `data`
- [x] Rendi `X` e `Y` esportate (maiuscole)
- [ ] Usa i tag di campo

1. [How to Parse JSON in Golang?](https://www.geeksforgeeks.org/how-to-parse-json-in-golang/)
2. [Go Playground](https://play.golang.org/p/RdL6y3Zv8ke)

#### Q11. Cosa blocca un `sync.Mutex` mentre è bloccato (locked)?

- [ ] tutte le goroutine
- [ ] qualsiasi altra chiamata a lock su quel `Mutex`
- [x] qualsiasi lettura o scrittura della variabile che sta proteggendo
- [ ] qualsiasi scrittura sulla variabile che sta proteggendo

1. [Mutex in GoLang](https://golangdocs.com/mutex-in-golang), `sync.Mutex` blocca in modo che solo una goroutine alla volta possa accedere alla variabile protetta.
2. [sync.Mutex](https://go.dev/tour/concurrency/9)

#### Q12. Qual è un modo idiomatico per sospendere l’esecuzione dell’ambito corrente finché un numero arbitrario di goroutine non è terminato?

- [ ] Passare un `int` e un `Mutex` a ciascuna e contare quando ritornano.
- [ ] Ciclo su uno `select`.
- [ ] Dormire per un tempo sicuro.
- [x] `sync.WaitGroup`

**Spiegazione:** è esattamente per questo che è progettato `sync.WaitGroup` - [Use sync.WaitGroup in Golang](https://nanxiao.me/en/use-sync-waitgroup-in-golang/)

#### Q13. Qual è un effetto collaterale dell’uso di `time.After` in uno statement `select`?

- [ ] Blocca gli altri canali.
- [ ] È pensato per essere usato in select senza effetti collaterali.
- [ ] Blocca lo statement `select` finché il tempo non è passato.
- [x] La goroutine non termina finché il tempo non è passato.

> Nota: non blocca `select` e non blocca altri canali.

1. [time.After() Function in Golang With Examples](https://www.geeksforgeeks.org/time-after-function-in-golang-with-examples/)
2. [How can I use 'time.After' and 'default' in Golang?](https://stackoverflow.com/questions/39212333/how-can-i-use-time-after-and-default-in-golang)
3. [Go Playground example](https://go.dev/play/p/WojTrG1ywRK)

#### Q14. A cosa serve l’istruzione `select`?

- [ ] eseguire una funzione in concorrenza
- [ ] eseguire un caso diverso in base al tipo di una variabile
- [ ] eseguire un caso diverso in base al valore di una variabile
- [x] eseguire un caso diverso in base a quale canale risponde per primo

[Select statement in GoLang](https://golangdocs.com/select-statement-in-golang)

#### Q15. Secondo lo standard di documentazione di Go, come dovresti documentare questa funzione?

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

**Spiegazione:** il blocco di documentazione dovrebbe iniziare con il nome della funzione.

[Comments in Go](https://exercism.org/tracks/go/concepts/comments)

#### Q16. Quale restrizione c’è sul tipo di `myVal` per compilare `i := myVal.(int)`?

- [ ] `myVal` deve essere un tipo intero, come `int`, `int64`, `int32`, ecc.
- [ ] `myVal` deve poter essere asserito come `int`.
- [x] `myVal` deve essere un’interfaccia.
- [ ] `myVal` deve essere un tipo numerico, come `float64` o `int64`.

**Spiegazione**: Questo tipo di casting (usando `.(type)`) si usa solo sulle interfacce.

1. [this example](https://tutorialedge.net/golang/snippets/type-casting-interface-to-string-go/)
2. [Primitive types are type-casted differently](https://golangdocs.com/type-casting-in-golang)
3. [Go Playground](https://play.golang.org/p/TXF_JBvThp6)
4. [Type assertions](https://go.dev/tour/methods/15)

#### Q17. Cos’è un canale?

- [ ] una variabile globale
- [x] un mezzo per inviare valori tra goroutine
- [ ] un array dinamico di valori
- [ ] un thread leggero per la programmazione concorrente

[Channels](https://tour.golang.org/concurrency/2)

#### Q18. Come puoi fare in modo che un file venga compilato solo su Windows?

- [ ] Controllare `runtime.GOOS`.
- [ ] Aggiungere un commento `// +build windows` in qualsiasi punto del file.
- [ ] Aggiungere un prefisso `_` al nome del file.
- [x] Aggiungere un commento `// +build windows` all’inizio del file.

1. [How to use conditional compilation with the go build tool, Oct 2013](https://dave.cheney.net/2013/10/12/how-to-use-conditional-compilation-with-the-go-build-tool)
2. [go commands Build constraints](https://pkg.go.dev/cmd/go#hdr-Build_constraints)

> `//go:build windows`
> "Go versions 1.16 and earlier used a different syntax for build constraints, with a "// +build" prefix. The gofmt command will add an equivalent //go:build constraint when encountering the older syntax."

#### Q19. Qual è il modo corretto per passare questo come body di una richiesta HTTP POST?

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

#### Q20. Quale dovrebbe essere il nome idiomatico per un’interfaccia con un singolo metodo con firma `Save() error`?

- [ ] Saveable
- [ ] SaveInterface
- [ ] ISave
- [x] Saver

[Effective Go, Interface names](https://golang.org/doc/effective_go#interface-names)

#### Q21. Un’istruzione `switch` **_** il proprio blocco lessicale. Ogni istruzione `case` **_** un blocco lessicale aggiuntivo

- [ ] non crea; crea
- [ ] non crea; non crea
- [x] crea; crea
- [ ] crea; non crea

[Go Language Core technology (Volume one) 1.5-scope](https://topic.alibabacloud.com/a/go-language-core-technology-volume-one-15-font-colorredscopefont_1_38_30923325.html)

Estratto rilevante dall’articolo:

> _La seconda istruzione if è annidata dentro la prima, quindi una variabile dichiarata nella prima è visibile alla seconda. Regole simili in switch: ogni case ha il proprio blocco lessicale oltre al blocco condizionale._

#### Q22. Qual è la sensibilità al maiuscolo/minuscolo predefinita della funzione JSON `Unmarshal`?

- [x] Il comportamento predefinito è case insensitive, ma può essere sovrascritto.
- [ ] I campi vengono confrontati con distinzione tra maiuscole e minuscole.
- [ ] I campi vengono confrontati senza distinzione.
- [ ] Il comportamento predefinito è case sensitive, ma può essere sovrascritto.

[encoding/json#Unmarshal](https://pkg.go.dev/encoding/json#Unmarshal)

Estratto rilevante dall’articolo:

> _Per deserializzare JSON in una struct, Unmarshal associa le chiavi dell’oggetto in ingresso alle chiavi usate da Marshal (il nome del campo struct o il suo tag), preferendo una corrispondenza esatta ma accettando anche una corrispondenza case-insensitive. Per impostazione predefinita, le chiavi senza campo corrispondente vengono ignorate (vedi Decoder.DisallowUnknownFields per un’alternativa)._ 

#### Q23. Qual è la differenza tra i metodi `Time.Sub()` e `Time.Add()` del package `time`?

- [ ] Time.Add() serve per eseguire addizioni mentre Time.Sub() per annidare timestamp.
- [ ] Time.Add() restituisce sempre un orario successivo mentre time.Sub sempre precedente.
- [ ] Sono opposti. Time.Add(x) equivale a Time.Sub(-x).
- [x] Time.Add() accetta un parametro `Duration` e restituisce un `Time` mentre Time.Sub() accetta un `Time` e restituisce una `Duration`.

1. [time#Time.Add](https://pkg.go.dev/time#Time.Add)
2. [time#Time.Sub](https://pkg.go.dev/time#Time.Sub)

#### Q24. Qual è il rischio di usare più tag di campo in un’unica struct?

- [ ] Ogni campo deve avere tutti i tag per compilare.
- [x] Collega strettamente i diversi livelli della tua applicazione.
- [ ] Qualsiasi tag dopo il primo viene ignorato.
- [ ] Tag mancanti generano panic a runtime.

1. [Example Code / b29r0fUD1cp](https://play.golang.org/p/b29r0fUD1cp)
2. [How To Use Struct Tags in Go](https://www.digitalocean.com/community/tutorials/how-to-use-struct-tags-in-go)

#### Q25. Dove è utile il metodo built-in `recover`?

- [ ] nella funzione `main`
- [ ] immediatamente dopo una riga che potrebbe fare panic
- [x] dentro una funzione differita (`deferred`)
- [ ] all’inizio di una funzione che potrebbe andare in panic

[Example of Recover Function in Go (Golang)](https://golangbot.com/panic-and-recover/#recoveringfromapanic)

Estratto rilevante dall’articolo:

> _`recover` è utile solo quando chiamato dentro funzioni differite. Eseguire `recover` dentro una funzione differita interrompe la sequenza di panic ripristinando l’esecuzione normale e recupera il messaggio di errore passato a `panic`. Se chiamato fuori da una funzione differita, non interrompe il panic._

#### Q26. Quale scelta NON invia output su standard error?

- [ ] `println(message)`
- [ ] `log.New(os.Stderr, "", 0).Println(message)`
- [x] `fmt.Errorf("%s\n", message)`
- [ ] `fmt.Fprintln(os.Stderr, message)`

1. [func println](https://pkg.go.dev/builtin#println): scrive il risultato su _standard error_.
2. [func New](https://pkg.go.dev/log#New): func New(out io.Writer, prefix string, flag int) \*Logger; la variabile out _imposta la destinazione_ per i log.
3. [func Errorf](https://pkg.go.dev/fmt#Errorf): formatta e _restituisce la stringa_ come valore.
4. [func Fprintln](https://pkg.go.dev/fmt#Fprintln): formatta e _scrive su w_.

#### Q27. Come puoi dire a Go di importare un package da una posizione diversa?

- [ ] Usare un proxy.
- [ ] Cambiare il path di import.
- [x] Usare una direttiva `replace` in `go.mod`.
- [ ] Usare una directory `replace`.

1. [Call your code from another module](https://go.dev/doc/tutorial/call-module-code): capitolo 5., `go mod edit -replace example.com/greetings=../greetings`.
2. [go.mod replace directive](https://go.dev/doc/modules/gomod-ref#replace)

#### Q28. Se la directory di lavoro corrente è il livello superiore del progetto, quale comando eseguirà tutti i package di test?

- [ ] `go test all`
- [ ] `go run --all`
- [ ] `go test .`
- [x] `go test ./...`

1. [Example of testing in Go (Golang)](https://pkg.go.dev/testing)
2. [Example of cmd in Go (Golang)](https://pkg.go.dev/cmd/go)

Estratto rilevante dall’articolo:

> _Sono consentiti anche pattern relativi, come "go test ./..." per testare tutte le sottodirectory._

#### Q29. Quali codifiche puoi mettere in una stringa?

- [ ] qualsiasi, accetta byte arbitrari
- [ ] qualsiasi formato Unicode
- [ ] UTF-8 o ASCII
- [x] UTF-8

1. [Strings, bytes, runes and characters in Go](https://go.dev/blog/strings)

Estratto rilevante dall’articolo:

> _In breve, il codice sorgente Go è UTF-8, quindi il letterale di stringa è testo UTF-8._

2. [Example of encoding in Go (Golang)](https://pkg.go.dev/golang.org/x/text/encoding)

Estratto rilevante dall’articolo:

> _Il package encoding definisce un’interfaccia per le codifiche di caratteri che possono convertire da e verso UTF-8._

#### Q30. In cosa differisce il comportamento di `t.Fatal` dentro un `t.Run`?

- [ ] Non c’è differenza.
- [ ] `t.Fatal` non blocca il test harness, preservando i messaggi di output.
- [x] `t.Fatal` ferma l’esecuzione del sotto-test e continua con gli altri test.
- [ ] `t.Fatal` ferma tutti i test e contiene info extra sul sotto-test fallito.

1. [Reference:](https://go.dev/play/p/gtne3iRL9AX)
2. [testing package in Go](https://pkg.go.dev/testing), estratto rilevante:

> `Fatal` è equivalente a `Log` seguito da `FailNow`... l’esecuzione continuerà al prossimo test o benchmark.

#### Q31. Cosa fa `log.Fatal`?

- [ ] Solleva un panic.
- [ ] Stampa il log e poi solleva un panic.
- [x] Stampa il log e poi esce in modo sicuro dal programma.
- [ ] Esce dal programma.

[Example of func Fatal in Go (Golang)](https://pkg.go.dev/log#Fatal)

Estratto rilevante:

> _`Fatal` è equivalente a `Print()` seguito da `os.Exit(1)`._

#### Q32. Quale è un formato letterale di tempo Go valido?

- [x] "2006-01-02"
- [ ] "YYYY-mm-dd"
- [ ] "y-mo-d"
- [ ] "year-month-day"

[func Time in Go](https://pkg.go.dev/time#pkg-constants)

Estratto rilevante:

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

#### Q33. Come dovresti loggare un errore (`err`)

- [ ] `log.Error(err)`
- [x] `log.Printf("error: %v", err)`
- [ ] `log.Printf(log.ERROR, err)`
- [ ] `log.Print("error: %v", err)`

**Spiegazione:** Non esistono né _log.ERROR_ né _log.Error()_ nel [package log di Go](https://pkg.go.dev/log); `log.Print()` gestisce gli argomenti come `fmt.Print()`; `log.Printf()` come `fmt.Printf()`.

#### Q34. Quali nomi di file il comando `go test` riconosce come file di test?

- [ ] qualsiasi che inizi con `test`
- [ ] qualsiasi file che includa la parola `test`
- [ ] solo file nella root che finiscono con `_test.go`
- [x] qualsiasi che finisca con `_test.go`

1. [Test packages in go command in Go](https://pkg.go.dev/cmd/go#hdr-Test_packages)
2. [Add a test in Go](https://go.dev/doc/tutorial/add-a-test)

#### Q35. Quale sarà l’output di questo codice?

```go
ch := make(chan int)
ch <- 7
val := <-ch
fmt.Println(val)
```

- [ ] 0
- [x] Andrà in deadlock
- [ ] Non compilerà
- [ ] 2.718

[Go Playground share](https://go.dev/play/p/SQLfg8YSEOz), output:

```text
fatal error: all goroutines are asleep - deadlock!

goroutine 1 [chan send]:
main.main()
 /tmp/sandbox2282523250/prog.go:7 +0x37

Program exited.
```

#### Q36. Quale sarà l’output di questo programma?

```go
ch := make(chan int)
close(ch)
val := <-ch
fmt.Println(val)
```

- [ ] Andrà in deadlock
- [ ] Andrà in panic
- [x] 0
- [ ] NaN

1. [The Go Programming Language Specification "Receive operator"](https://go.dev/ref/spec#Receive_operator)
2. [Go Playground share](https://go.dev/play/p/DjXq9wzJm5M)

```text
0

Program exited.
```

#### Q37. Cosa verrà stampato in questo codice?

```go
var stocks map[string]float64 // stock -> price
price := stocks["MSFT"]
fmt.Printf("%f\n", price)
```

- [ ] 0
- [x] 0.000000
- [ ] Il codice andrà in panic
- [ ] NaN

[Go Playground share](https://go.dev/play/p/CjdHskV1xq1), output:

```text
0.000000

Program exited.
```

#### Q38. Qual è il modo comune per avere più eseguibili nel tuo progetto?

- [x] Avere una directory `cmd` e una directory per eseguibile al suo interno.
- [ ] Commentare `main`.
- [ ] Usare build tag.
- [ ] Avere una directory `pkg` e una directory per eseguibile al suo interno.

1. [stackoverflow](https://stackoverflow.com/questions/9985559/organizing-a-multiple-file-go-project/51942843#51942843)
2. [medium](https://medium.com/@benbjohnson/structuring-applications-in-go-3b04be4ff091)
3. [medium](https://medium.com/golang-learn/go-project-layout-e5213cdcfaa2)

#### Q39. Come puoi compilare `main.go` in un eseguibile che girerà su macOS arm64?

- [ ] Imposta GOOS su **arm64** e GOARCH su **darwin**.
- [ ] Imposta GOOS su **osx** e GOARCH su **arm64**.
- [ ] Imposta GOOS su **arm64** e GOARCH su **osx**.
- [x] Imposta GOOS su **darwin** e GOARCH su **arm64**.

[documentation](https://pkg.go.dev/cmd/go#hdr-Build_constraints)

#### Q40. Qual è la sintassi corretta per avviare una goroutine che `print Hello Gopher!`?

- [ ] `go(fmt.Println("Hello Gopher!"))`
- [ ] `go func() { fmt.Println("Hello Gopher!") }`
- [x] `go fmt.Println("Hello Gopher!")`
- [ ] `Go fmt.Println("Hello Gopher!")`

[Example of start a goroutine](https://go.dev/play/p/KGgnAWpZMrS)

#### Q41. Se iteri su una mappa in un `for range`, in che ordine verranno accessi i pair chiave:valore?

- [x] in un ordine pseudo-casuale non prevedibile
- [ ] in ordine inverso rispetto a come sono stati aggiunti
- [ ] ordinati per chiave in ordine crescente
- [ ] nell’ordine in cui sono stati aggiunti, FIFO

[Reference](https://go.dev/ref/spec#:~:text=The%20iteration%20order%20over%20maps%20is%20not%20specified)

#### Q42. Qual è un modo idiomatico per personalizzare la rappresentazione di una struct personalizzata in una stringa formattata?

- [ ] Non c’è personalizzazione della rappresentazione string di un tipo.
- [ ] Costruirla a pezzi ogni volta chiamando i singoli campi.
- [x] Implementare un metodo `String()` string
- [ ] Creare una funzione wrapper che accetti il tuo tipo e restituisca una stringa.

[Reference](https://go.dev/doc/effective_go#printing)

#### Q43. Come puoi evitare una perdita di goroutine in questo codice?

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

- [ ] Usare un `sync.WaitGroup`.
- [x] Rendere `ch` un canale bufferizzato.
- [ ] Aggiungere un case `default` al `select`.
- [ ] Usare `runtime.SetFinalizer`.

[Reference](https://www.ardanlabs.com/blog/2018/11/goroutine-leaks-the-forgotten-sender.html)

Estratto rilevante:

> _Il modo più semplice per risolvere questa perdita è cambiare il canale da non bufferizzato a bufferizzato con capacità 1..._

#### 44. Cosa stamperà questo codice?

```go
var i int8 = 120
i += 10
fmt.Println(i)
```

- [x] -126
- [ ] 0
- [ ] NaN
- [ ] 130

[Go Playground example](https://go.dev/play/p/T31_JuFioaC)

```text
-126

Program exited.
```

#### 45. Data la definizione di `worker` sotto, qual è la sintassi corretta per avviare una goroutine che chiamerà `worker` e invierà il risultato su un canale `ch`?

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

#### Q46. In questo codice, quali nomi sono esportati?

```go
package os

type FilePermission int
type userID int
```

- [x] FilePermission
- [ ] nessuna di queste risposte
- [ ] FilePermission e userID
- [ ] userID

[Reference 1](https://www.ardanlabs.com/blog/2018/11/goroutine-leaks-the-forgotten-sender.html)
[Reference 2](https://go.dev/tour/basics/3)

#### Q47. Quale delle seguenti è corretta sulle struct in Go?

- [ ] La struct è un altro tipo definito dall’utente in Go che permette di combinare elementi di dati di diversi tipi.
- [ ] Le struct sono usate per rappresentare un record
- [ ] Per definire una struct devi usare le istruzioni `type` e `struct`.
- [x] Tutte le precedenti

#### Q48. Cosa fa il comando built-in `generate` del compilatore Go?

- [ ] Fornisce sottocomandi `sql`, `json`, `yaml`, e opzioni `--schema` e `--objects` per generare codice.
- [ ] Cerca file con nomi che terminano in `_generate.go`, poi compila ed esegue ciascuno di essi.
- [x] Scansiona il sorgente del progetto cercando commenti `//go:generate` e per ciascuno esegue il comando di terminale specificato.
- [ ] Ha sottocomandi `mocks` e `tests` per generare file `.go`.

[Generate Go files by processing source](https://pkg.go.dev/cmd/go#hdr-Generate_Go_files_by_processing_source)

#### Q49. Usando il package `time`, come puoi ottenere l’ora tra 90 minuti da adesso?

- [ ] `time.Now().Add(90)`
- [ ] `time.Now() + (90 * time.Minute)`
- [ ] `time.Now() + 90`
- [x] `time.Now().Add(90 * time.Minute)`

[func (Time) Add example](https://pkg.go.dev/time#example-Time.Add)

#### Q50. Un programma usa un canale per stampare cinque interi dentro una goroutine mentre il main alimenta il canale con interi, ma così non funziona. Cosa devi cambiare per farlo funzionare?

- [ ] Aggiungere un `close(ch)` immediatamente dopo `wg.Wait()`.
- [x] Aggiungere un secondo parametro a `make(chan, int)`, es. `make(chan int, 5)`.
- [ ] Rimuovere l’uso non necessario di `WaitGroup` (tutte le righe che iniziano con `wg`).
- [ ] Spostare la goroutine di 7 righe subito prima di `wg.Wait()`.

[Reference](https://www.ardanlabs.com/blog/2018/11/goroutine-leaks-the-forgotten-sender.html)

Estratto rilevante:

> _Il modo più semplice per risolvere questa perdita è cambiare il canale da non bufferizzato a bufferizzato con capacità 1..._

#### Q51. Dopo aver importato `encoding/json`, come accederai alla funzione `Marshal`?

- [ ] `encoding.json.Marshal`
- [ ] `encoding/json.Marshal`
- [ ] `Marshal`
- [x] `json.Marshal`

[encoding/json#Marshal example](https://pkg.go.dev/encoding/json#example-Marshal)

#### Q52. Quali sono i due segmenti mancanti per usare `context.Context` e implementare un timeout di 3 secondi per un client HTTP che fa una GET?

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

        // #1: <=== Cosa va qui?

        req, _ := http.NewRequest(http.MethodGet,
                "https://linkedin.com",
                nil)

        // #2: <=== Cosa va qui?

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

#### Q53. Se hai una struct chiamata `Client` definita nello stesso file `.go` dell’istruzione, come esporti una variabile con un valore di default in modo che sia accessibile dagli altri package?

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

#### Q54. Questo programma produce `{Master Chief Spartan Protagonist Halo}`. Come faresti ad ottenere `Master Chief - a Spartan - is the Protagonist of Halo` invece?

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

#### Q55. Come implementeresti un metodo `Append()` funzionante per `Clients`?

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

#### Q56. Come recupereresti da un `panic()` lanciato da una funzione chiamata senza permettere che il programma fallisca, assumendo che la risposta giri nello stesso scope in cui avviene il panic?

- [ ] Incapsula la chiamata in una funzione anonima con tipo di ritorno `panic`, ricordando di invocarla con `()` e gestendo l’errore.
- [ ] Usa `try{ ... }` e poi gestisci l’errore nel `catch{ ... }`.
- [x] Usa `defer func { ... }()` prima della chiamata e gestisci il panic dentro la funzione anonima.
- [ ] Prefissa la chiamata con `@` per forzare il ritorno del panic come `error`.

#### Q57. Cosa stamperà questo codice?

```go
var n int
fmt.Println (n)
```

- [x] 0
- [ ] nil
- [ ] un valore casuale
- [ ] 1

> Questo perché in Go, quando una variabile è dichiarata ma non inizializzata, riceve il [valore zero](https://go.dev/tour/basics/12) del suo tipo. Per gli interi come `n`, è 0.

#### Q58. Creando una stringa formattata, quale verb dovresti usare per chiamare il metodo `String() string` di un tipo custom?

- [x] %s
- [ ] %b
- [ ] %v
- [ ] %string

> In Go, il verb `%s` formatta una stringa. Con un tipo che ha `String()`, verrà chiamato automaticamente e usato il suo valore di ritorno.

#### Q59. Quale NON è un valore valido per `layout` chiamando `time.Now().Format(layout)`?

- [ ] time.REC3339
- [x] "1970-01-01"
- [ ] "Jan 2nd 2006"
- [ ] time.Kitchen

[time#Time.Format](https://pkg.go.dev/time#Time.Format)

Secondo la documentazione, i valori 1 e 01 rappresentano il mese corrente.

```text
each layout string is a representation of the time stamp,
	Jan 2 15:04:05 2006 MST
An easy way to remember this value is that it holds, when presented in this order, the values (lined up with the elements above):
	  1 2  3  4  5    6  -7
```

#### Q60. Come segnaleresti al compilatore Go che la struct `Namespace` deve implementare l’interfaccia `JSONConverter`? Si assume che la risposta sia nello stesso package di `Namespace`.

- [ ] var_JSONConverter = nil. (*Namespace)
- [x] var _ JSONConverter = (*Namespace) (nil)
- [ ] type Namespace struct {
      implements JSONConverter
      // The rest of the struct declaration goes here
      }
- [ ] type Namespace struct {
      JSONConverter
      // The rest of the struct declaration goes here
      }

> Questa sintassi crea una variabile `_` di tipo `JSONConverter` e le assegna `(*Namespace)(nil)`. In pratica verifica che `Namespace` soddisfi l’interfaccia.

#### Q61. Quale affermazione su typing e interfacce è falsa?

- [ ] La firma di un metodo è la combinazione del nome e dei tipi dei parametri/ritorno.
- [x] Una struct deve dichiarare esplicitamente con la keyword implements che le sue istanze possono essere usate dove un valore è tipizzato per l’interfaccia dichiarata.
- [ ] Un’interfaccia dichiara metodi e firme che un tipo deve implementare per essere compatibile.
- [ ] Variabili, parametri e ritorni devono essere tipizzati come: 1) built-in, 2) alias, 3) derivati, 4) compositi, o 5) un’interfaccia.

> In Go, un tipo soddisfa un’interfaccia automaticamente se implementa tutti i metodi. Non c’è keyword per dichiararlo.

#### Q62. Come completeresti questo programma per generare l’output specificato, assumendo la tabella SQL

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

        // #1 <=== Cosa va qui?

        for results.Next() {
                var g Game

                // #2 <=== Cosa va qui?

                if err != nil {
                        panic(err)
                }

                // #3 <=== Cosa va qui?

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

#- [x] &shy;

```go
#1: games := make(map[int]*Game, 0)
#2: err = results.Scan(&g.GameId, &g.Title, &g.YearReleased)
#3: games[g.GameId] = &g
```

#### Q63. Riempi gli spazi

1.  I file di test in Go devono **_**.
2.  I test individuali sono identificati da **_**.
3.  Puoi eseguire i subtest **__**.
4.  Logghi l’errore e marchi il test come fallito **_**.

- [ ] essere memorizzati in una sottodirectory `/test/` di quel package
      <br/>funzioni che accettano un parametro `testing.Tester`
      <br/>scrivendo funzioni con nomi che combaciano con `^Subtest`
      <br/>chiamando `testing.AssertionFailed`

- [x] finire in `_test.go`
      <br/>nomi funzione che combaciano con `^Test[A-Z]`
      <br/>chiamando `t.Run()`
      <br/>chiamando `t.Errorf()`

- [ ] iniziare con `test_`
      <br/>funzioni che combaciano con `[a-z]Test$`
      <br/>chiamando `testing.Subtest()`
      <br/>permettendo a `testing.Assert()` di fallire l’asserzione

- [ ] essere memorizzati nella root `/test/` del progetto
      <br/>funzioni che accettano un parametro `testing.Test`
      <br/>passando closure a `testing.AddSubtest()`
      <br/>restituendo un `error` dalla funzione

#### Q64. Di quale tipo è alias `rune`?

- [ ] char
- [ ] byte
- [x] int32
- [ ] string

1. [Strings, bytes, runes and characters in Go](https://go.dev/blog/strings)

Estratto rilevante:

> _Go definisce la parola rune come alias per `int32`, così i programmi possono essere chiari quando un intero rappresenta un code point._

#### Q65. Quando puoi usare la sintassi `:=` per assegnare a più variabili? Per esempio:

```go
x, err := myFunc()
```

- [x] se almeno una non è stata dichiarata in quel blocco lessicale
- [ ] sempre, sovrascriverà le variabili esistenti
- [ ] se nessuna variabile con quei nomi è accessibile
- [ ] se nessuna delle variabili esiste in quel blocco lessicale

1. [Short variable declarations](https://go.dev/ref/spec#Short_variable_declarations)

#### Q66. Come puoi visualizzare l’output del profiler in `cpu.pprof` nel browser?

- [ ] `go pprof -to SVG cpu.prof`
- [x] `go tool pprof -http=:8080 cpu.pprof`
- [ ] `go tool pprof cpu.pprof`
- [ ] `go tool trace cpu.pprof`

#### Q67. Quando una variabile di tipo `interface{}` valuta a `nil`?

- [x] Le è stato assegnato un tipo dinamico il cui valore è `nil`.
- [ ] È stata impostata esplicitamente a `nil`.
- [ ] Non le è stato assegnato un tipo dinamico.
- [ ] Non può valutare a `nil`.

#### Q68. Che valore contiene una variabile string se è stata allocata ma non assegnata?

- [ ] nil
- [ ] undefined
- [ ] null
- [x] ""

> Se una string è allocata ma non assegnata, il suo valore di default è la stringa vuota "". In Go, le variabili string non inizializzate ricevono il valore zero del tipo.

#### Q69. Quale funzione built-in si usa per fermare l’esecuzione di un programma?

- [x] `panic`
- [ ] Non esiste tale funzione.
- [ ] `raiseException`
- [ ] `exit`

> La funzione built-in per fermare l’esecuzione è `panic()`. Se non viene recuperata, il programma termina.

#### Q70. Quale sarà l’output?

```go
a,b := 1, 2
b,c:= 3, 4
fmt.Println(a, b, c)
```

- [x] 1 3 4
- [ ] 1 2 3
- [ ] 1 2 4
- [ ] Non compila.

[Go Playground Example](https://go.dev/play/p/qUI50GNGWTq)

### Q71. Qual è l’operatore per l’AND logico?

- [ ] +
- [ ] and
- [x] &&
- [ ] ||

### Q72. Cos’è una funzione anonima in Go?

- [ ] Una funzione senza tipo di ritorno.
- [ ] Una funzione senza parametri.
- [x] Una funzione senza nome.
- [ ] Una funzione dichiarata dentro un’altra funzione.

### Q73. Quale keyword si usa per dichiarare una funzione anonima in Go?

- [ ] `func`
- [ ] `lambda`
- [x] `func()`
- [ ] `anonymous`

#### Q74. Qual è il principale vantaggio nell’uso di funzioni anonime in Go?

- [ ] Hanno sempre migliori prestazioni delle funzioni con nome.
- [ ] Possono avere valori di ritorno multipli.
- [x] Possono essere definite inline dove sono usate.
- [ ] Hanno una sintassi più corta delle funzioni con nome.

Spiegazione: possono essere definite inline dove sono usate, offrendo maggiore flessibilità nell’organizzazione del codice.

#### Q75. Qual è la sintassi per chiamare immediatamente una funzione anonima dopo la sua dichiarazione in Go?

- [ ] `functionName(){}`
- [ ] `call functionName(){}`
- [x] `func(){}()`
- [ ] `execute func(){}`

[reference](https://stackoverflow.com/questions/6719089/javascript-anonymous-function-immediate-invocation-execution-expression-vs-dec)

#### Q76. Per quali tipi gli sviluppatori Go possono definire metodi?

- [x] tutti i tipi con nome non built-in in Go, ad esempio `type Example int` ma non `int`, `type Example struct{...}` ma non `struct`, ecc.
- [ ] solo i tipi chiamati struct, map e slice, ad esempio `type Example struct{…}`
- [ ] solo i tipi chiamati struct, ad esempio `type Example struct{...}`
- [ ] tutti i tipi

> I metodi possono essere definiti per qualsiasi tipo con nome che non sia built-in. Non possono essere attaccati direttamente a tipi built-in come `int`, `string`, ecc. [reference](https://go.dev/ref/spec#Method_declarations)

