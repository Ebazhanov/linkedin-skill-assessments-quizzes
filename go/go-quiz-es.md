## Go (Lenguaje de Programación)

#### P1. ¿Qué necesitan dos funciones para ser del mismo tipo?

- [x] Deben compartir las mismas firmas, incluidos tipos de parámetros y tipos de retorno.
- [ ] Deben compartir los mismos tipos de parámetros pero pueden devolver tipos diferentes.
- [ ] Todas las funciones deben ser del mismo tipo.
- [ ] Las funciones no deben ser un tipo de primera clase.

[User defined function types in Go (Golang)](https://golangbyexample.com/user-defined-function-type-go/)

#### P2. ¿Qué devuelve la función `len()` si se le pasa una cadena codificada en UTF-8?

- [ ] el número de caracteres
- [x] el número de bytes
- [ ] No acepta tipos string.
- [ ] el número de code points

[Length of string in Go (Golang)](https://golangbyexample.com/length-of-string-golang/).

#### P3. ¿Cuál NO es una construcción de bucle válida en Go?

- [x]

```go
      do { ... } while i < 5
```

- [ ]

```go
      for _,c := range "hello" { ... }
```

- [ ]

```go
      for i := 1; i < 5; i++ { ... }
```

- [ ]

```go
      for i < 5 { ... }
```

**Explicación:** Go solo tiene bucles `for`.

#### P4. ¿Cómo agregarías el número 3 al final (lado derecho)?

```go
values := []int{1, 1, 2}
```

- [ ]

```go
      values.append(3)
```

- [ ]

```go
      values.insert(3, 3)
```

- [ ]

```go
      append(values, 3)
```

- [x]

```go
      values = append(values, 3)
```

**Explicación:** los slices en Go son inmutables en cuanto a tamaño; `append` devuelve un nuevo slice.

#### P5. ¿Cuál es el valor de `Read`?

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
- [ ] un valor aleatorio

[IOTA in Go (Golang)](https://golangbyexample.com/iota-in-golang/)

#### P6. ¿Cuál es la única sentencia `import` válida en Go?

- [ ]

```go
      import "github/gin-gonic/gin"
```

- [ ]

```go
      import "https://github.com/gin-gonic/gin"
```

- [ ]

```go
      import "../template"
```

- [x]

```go
      import "github.com/gin-gonic/gin"
```

[Import in GoLang](https://golangdocs.com/import-in-golang)

#### P7. ¿Qué pasaría si intentaras compilar y ejecutar este programa Go?

```go
package main
var GlobalFlag string
func main() {
  print("["+GlobalFlag+"]")
}
```

- [ ] No compilaría porque `GlobalFlag` nunca fue inicializada.
- [x] Compilaría e imprimiría `[]`.
- [ ] Compilaría y no imprimiría nada porque `"[" +nil+"]"` también es `nil`.
- [ ] Compilaría pero luego haría panic porque `GlobalFlag` nunca fue inicializada.

1. Las [variables](https://golangbyexample.com/variables-in-golang-complete-guide/) en Go tienen valores iniciales. Para `string` es la cadena vacía.
2. [Go Playground](https://play.golang.org/p/TaRIzuD-nxC)

#### P8. ¿Desde dónde es accesible la variable `myVar` si se declara fuera de cualquier función en un archivo del paquete `myPackage` ubicado dentro del módulo `myModule`?

- [x] Se puede acceder en cualquier lugar dentro de `myPackage`, no en el resto de `myModule`.
- [ ] Puede ser accedida por cualquier aplicación que importe `myModule`.
- [ ] Puede ser accedida desde cualquier lugar en `myModule`.
- [ ] Puede ser accedida por otros paquetes en `myModule` siempre que importen `myPackage`.

**Explicación**: para hacer disponible la variable fuera de `myPackage` cambia el nombre a `MyVar`.
Consulta también un ejemplo de [Exported names](https://tour.golang.org/basics/3) en el Tour of Go.

#### P9. ¿Cómo le indicas a `go test` que imprima las pruebas que está ejecutando?

- [ ] `go test`
- [ ] `go test -x`
- [ ] `go test --verbose`
- [x] `go test -v`

[test package](https://pkg.go.dev/cmd/go/internal/test)

#### P10. Este código imprimió `{0, 0}`. ¿Cómo lo corriges?

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

- [ ] usar `json.Decoder`
- [ ] Pasar un puntero a `data`
- [x] Hacer `X` y `Y` exportados (mayúsculas)
- [ ] Usar tags de campo

1. [How to Parse JSON in Golang?](https://www.geeksforgeeks.org/how-to-parse-json-in-golang/)
2. [Go Playground](https://play.golang.org/p/RdL6y3Zv8ke)

#### P11. ¿Qué bloquea un `sync.Mutex` mientras está bloqueado?

- [ ] todas las goroutines
- [ ] cualquier otra llamada a lock de ese `Mutex`
- [x] cualquier lectura o escritura de la variable que está protegiendo
- [ ] cualquier escritura de la variable que está protegiendo

1. [Mutex in GoLang](https://golangdocs.com/mutex-in-golang)
2. [sync.Mutex](https://go.dev/tour/concurrency/9)

#### P12. ¿Cuál es una forma idiomática de pausar la ejecución del ámbito actual hasta que un número arbitrario de goroutines hayan terminado?

- [ ] Pasar un `int` y `Mutex` a cada una y contar cuando regresen.
- [ ] Iterar sobre una sentencia `select`.
- [ ] Dormir por un tiempo seguro.
- [x] `sync.WaitGroup`

**Explicación:** esto es exactamente para lo que fue diseñado `sync.WaitGroup` - [Use sync.WaitGroup in Golang](https://nanxiao.me/en/use-sync-waitgroup-in-golang/)

#### P13. ¿Cuál es un efecto secundario de usar `time.After` en una sentencia `select`?

- [ ] Bloquea los otros canales.
- [ ] Está destinada a usarse en `select` sin efectos secundarios.
- [ ] Bloquea la sentencia `select` hasta que pase el tiempo.
- [x] La goroutine no termina hasta que pase el tiempo.

> Nota: no bloquea `select` ni otros canales.

1. [time.After() Function in Golang With Examples](https://www.geeksforgeeks.org/time-after-function-in-golang-with-examples/)
2. [How can I use 'time.After' and 'default' in Golang?](https://stackoverflow.com/questions/39212333/how-can-i-use-time-after-and-default-in-golang)
3. [Go Playground example](https://go.dev/play/p/WojTrG1ywRK)

#### P14. ¿Para qué se usa la sentencia `select`?

- [ ] ejecutar una función concurrentemente
- [ ] ejecutar un caso diferente según el tipo de una variable
- [ ] ejecutar un caso diferente según el valor de una variable
- [x] ejecutar un caso diferente según qué canal devuelva primero

[Select statement in GoLang](https://golangdocs.com/select-statement-in-golang)

#### P15. Según el estándar de documentación de Go, ¿cómo deberías documentar esta función?

```go
func Add(a, b int) int {
        return a + b
}
```

- [ ] A

  ```go
  // Calcula a + b
  // - a: int
  // - b: int
  // - retorna: int
  func Add(a, b int) int {
          return a + b
  }
  ```

- [ ] B

  ```go
  // Hace a + b
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

**Explicación:** el bloque de documentación debe comenzar con el nombre de la función.

[Comments in Go](https://exercism.org/tracks/go/concepts/comments)

#### P16. ¿Qué restricción existe sobre el tipo de `myVal` para compilar `i := myVal.(int)`?

- [ ] `myVal` debe ser un tipo entero, como `int`, `int64`, `int32`, etc.
- [ ] `myVal` debe poder ser afirmado como `int`.
- [x] `myVal` debe ser una interfaz.
- [ ] `myVal` debe ser un tipo numérico, como `float64` o `int64`.

**Explicación**: Este tipo de aserción de tipos (usando `.(type)`) solo se usa sobre interfaces.

1. [ejemplo](https://tutorialedge.net/golang/snippets/type-casting-interface-to-string-go/)
2. [Primitive types are type-casted differently](https://golangdocs.com/type-casting-in-golang)
3. [Go Playground](https://play.golang.org/p/TXF_JBvThp6)
4. [Type assertions](https://go.dev/tour/methods/15)

#### P17. ¿Qué es un canal?

- [ ] una variable global
- [x] un medio para enviar valores entre goroutines
- [ ] un arreglo dinámico de valores
- [ ] un hilo ligero para programación concurrente

[Channels](https://tour.golang.org/concurrency/2)

#### P18. ¿Cómo puedes hacer que un archivo compile solo en Windows?

- [ ] Comprobar `runtime.GOOS`.
- [ ] Agregar un comentario `// +build windows` en cualquier lugar del archivo.
- [ ] Agregar un prefijo `_` al nombre del archivo.
- [x] Agregar un comentario `// +build windows` en la parte superior del archivo.

1. [How to use conditional compilation with the go build tool, Oct 2013](https://dave.cheney.net/2013/10/12/how-to-use-conditional-compilation-with-the-go-build-tool)
2. [go commands Build constraints](https://pkg.go.dev/cmd/go#hdr-Build_constraints)

> `//go:build windows`
> "Go 1.16 y anteriores usan una sintaxis diferente con el prefijo `// +build`. `gofmt` añadirá una restricción equivalente `//go:build` al encontrar la sintaxis antigua."

#### P19. ¿Cuál es la forma correcta de pasar esto como cuerpo de una solicitud HTTP POST?

```go
data := "A group of Owls is called a parliament"
```

- [ ]

```go
  resp, err := http.Post("https://httpbin.org/post", "text/plain", []byte(data))
```

- [ ]

```go
      resp, err := http.Post("https://httpbin.org/post", "text/plain", data)
```

- [x]

```go
      resp, err := http.Post("https://httpbin.org/post", "text/plain", strings.NewReader(data))
```

- [ ]

```go
      resp, err := http.Post("https://httpbin.org/post", "text/plain", &data)
```

1. [net/http#Client.Post](https://pkg.go.dev/net/http#Client.Post)
2. [http.Post Golang example](https://dev.to/ramu_mangalarapu/httppost-golang-example-5jp)

#### P20. ¿Cuál debería ser el nombre idiomático para una interfaz con un único método y la firma `Save() error`?

- [ ] Saveable
- [ ] SaveInterface
- [ ] ISave
- [x] Saver

[Effective Go, Interface names](https://golang.org/doc/effective_go#interface-names)

#### P21. Una sentencia `switch` **\_** su propio bloque léxico. Cada `case` **\_** un bloque léxico adicional

- [ ] no crea; crea
- [ ] no crea; no crea
- [x] crea; crea
- [ ] crea; no crea

[Go Language Core technology (Volume one) 1.5-scope](https://topic.alibabacloud.com/a/go-language-core-technology-volume-one-15-font-colorredscopefont_1_38_30923325.html)

Extracto relevante del artículo:

> _El segundo `if` está anidado dentro del primero, por lo que una variable declarada en el primer `if` es visible para el segundo. Hay reglas similares en `switch`: cada `case` tiene su propio bloque léxico además del bloque condicional._

#### P22. ¿Cuál es la sensibilidad por defecto de `encoding/json` para `Unmarshal`?

- [x] El comportamiento por defecto es insensible a mayúsculas/minúsculas, pero se puede anular.
- [ ] Los campos coinciden distinguiendo mayúsculas/minúsculas.
- [ ] Los campos coinciden sin distinguir mayúsculas/minúsculas.
- [ ] El comportamiento por defecto distingue mayúsculas/minúsculas, pero se puede anular.

[encoding/json#Unmarshal](https://pkg.go.dev/encoding/json#Unmarshal)

Extracto relevante:

> _Para deserializar JSON en una struct, `Unmarshal` empareja las claves entrantes con el nombre del campo (o su tag), prefiriendo coincidencia exacta pero aceptando coincidencia insensible a mayúsculas._

#### P23. ¿Cuál es la diferencia entre los métodos `time.Time.Sub()` y `time.Time.Add()`?

- [ ] `Time.Add()` es para sumar y `Time.Sub()` para anidar timestamps.
- [ ] `Time.Add()` siempre devuelve un tiempo posterior mientras que `Time.Sub` siempre devuelve un tiempo anterior.
- [ ] Son opuestos. `Time.Add(x)` equivale a `Time.Sub(-x)`.
- [x] `Time.Add()` acepta un `Duration` y devuelve un `Time`, mientras que `Time.Sub()` acepta un `Time` y devuelve un `Duration`.

1. [time#Time.Add](https://pkg.go.dev/time#Time.Add)
2. [time#Time.Sub](https://pkg.go.dev/time#Time.Sub)

#### P24. ¿Cuál es el riesgo de usar múltiples tags de campo en una sola struct?

- [ ] Cada campo debe tener todas las tags para compilar.
- [x] Acopla fuertemente diferentes capas de tu aplicación.
- [ ] Cualquier tag después de la primera se ignora.
- [ ] Las tags faltantes provocan panic en runtime.

1. [Example Code / b29r0fUD1cp](https://play.golang.org/p/b29r0fUD1cp)
2. [How To Use Struct Tags in Go](https://www.digitalocean.com/community/tutorials/how-to-use-struct-tags-in-go)

#### P25. ¿Dónde es útil el método incorporado `recover`?

- [ ] en la función `main`
- [ ] inmediatamente después de una línea que podría hacer panic
- [x] dentro de una función `defer`
- [ ] al inicio de una función que podría hacer panic

[Example of Recover Function in Go (Golang)](https://golangbot.com/panic-and-recover/#recoveringfromapanic)

Extracto relevante:

> _`recover` es útil solo cuando se llama dentro de funciones diferidas. Ejecutar `recover` dentro de una función diferida detiene la secuencia de pánico y recupera el mensaje de error pasado a `panic`._

#### P26. ¿Cuál de las siguientes opciones NO envía salida a la salida de error estándar?

- [ ] `println(message)`
- [ ] `log.New(os.Stderr, "", 0).Println(message)`
- [x] `fmt.Errorf("%s\n", message)`
- [ ] `fmt.Fprintln(os.Stderr, message)`

1. [func println](https://pkg.go.dev/builtin#println)
2. [func New](https://pkg.go.dev/log#New)
3. [func Errorf](https://pkg.go.dev/fmt#Errorf)
4. [func Fprintln](https://pkg.go.dev/fmt#Fprintln)

#### P27. ¿Cómo le indicas a Go que importe un paquete desde una ubicación diferente?

- [ ] Usar un proxy.
- [ ] Cambiar la ruta de import.
- [x] Usar una directiva `replace` en `go.mod`.
- [ ] Usar un directorio replace.

1. [Call your code from another module](https://go.dev/doc/tutorial/call-module-code)
2. [go.mod replace directive](https://go.dev/doc/modules/gomod-ref#replace)

#### P28. Si tu directorio de trabajo actual es el nivel superior de tu proyecto, ¿qué comando ejecutará todas sus pruebas de paquetes?

- [ ] `go test all`
- [ ] `go run --all`
- [ ] `go test .`
- [x] `go test ./...`

1. [testing](https://pkg.go.dev/testing)
2. [cmd go](https://pkg.go.dev/cmd/go)

#### P29. ¿Qué codificaciones puedes poner en un `string`?

- [ ] cualquiera, acepta bytes arbitrarios
- [ ] cualquier formato Unicode
- [ ] UTF-8 o ASCII
- [x] UTF-8

1. [Strings, bytes, runes and characters in Go](https://go.dev/blog/strings)
2. [encoding](https://pkg.go.dev/golang.org/x/text/encoding)

#### P30. ¿Cómo se comporta `t.Fatal` dentro de un `t.Run`?

- [ ] No hay diferencia.
- [ ] `t.Fatal` no bloquea el arnés de pruebas, preservando mensajes.
- [x] `t.Fatal` detiene la subprueba y continúa con otros casos de prueba.
- [ ] `t.Fatal` detiene todas las pruebas e incluye información extra.

1. [Referencia](https://go.dev/play/p/gtne3iRL9AX)
2. [testing package](https://pkg.go.dev/testing)

#### P31. ¿Qué hace `log.Fatal`?

- [ ] Lanza un panic.
- [ ] Imprime el log y luego lanza un panic.
- [x] Imprime el log y luego sale del programa de forma segura.
- [ ] Sale del programa.

[func Fatal](https://pkg.go.dev/log#Fatal)

#### P32. ¿Cuál es un formato de tiempo literal válido en Go?

- [x] "2006-01-02"
- [ ] "YYYY-mm-dd"
- [ ] "y-mo-d"
- [ ] "year-month-day"

[func Time](https://pkg.go.dev/time#pkg-constants)

#### P33. ¿Cómo deberías registrar un error (`err`)?

- [ ] `log.Error(err)`
- [x] `log.Printf("error: %v", err)`
- [ ] `log.Printf(log.ERROR, err)`
- [ ] `log.Print("error: %v", err)`

**Explicación:** No existe `log.ERROR` ni `log.Error()`; `log.Printf()` formatea como `fmt.Printf()`.

#### P34. ¿Qué nombres de archivo reconocerá `go test` como archivos de prueba?

- [ ] cualquiera que comience con `test`
- [ ] cualquier archivo que incluya la palabra `test`
- [ ] solo archivos en el directorio raíz que terminen en `_test.go`
- [x] cualquiera que termine en `_test.go`

1. [cmd go - Test packages](https://pkg.go.dev/cmd/go#hdr-Test_packages)
2. [Add a test in Go](https://go.dev/doc/tutorial/add-a-test)

#### P35. ¿Cuál será la salida de este código?

```go
ch := make(chan int)
ch <- 7
val := <-ch
fmt.Println(val)
```

- [ ] 0
- [x] Se bloqueará (deadlock)
- [ ] No compilará
- [ ] 2.718

[Go Playground](https://go.dev/play/p/SQlfg8YSEOz)

#### P36. ¿Cuál será la salida de este programa?

```go
ch := make(chan int)
close(ch)
val := <-ch
fmt.Println(val)
```

- [ ] Se bloqueará (deadlock)
- [ ] Hará panic
- [x] 0
- [ ] NaN

1. [Receive operator](https://go.dev/ref/spec#Receive_operator)
2. [Go Playground](https://go.dev/play/p/DjXq9wzJm5M)

#### P37. ¿Qué se imprimirá en este código?

```go
var stocks map[string]float64 // stock -> price
price := stocks["MSFT"]
fmt.Printf("%f\n", price)
```

- [ ] 0
- [x] 0.000000
- [ ] El código hará panic
- [ ] NaN

[Go Playground](https://go.dev/play/p/CjdHskV1xq1)

#### P38. ¿Cuál es la forma común de tener varios ejecutables en tu proyecto?

- [x] Tener un directorio `cmd` y un directorio por ejecutable dentro de él.
- [ ] Comentar `main`.
- [ ] Usar build tags.
- [ ] Tener un directorio `pkg` y un directorio por ejecutable dentro de él.

1. [stackoverflow](https://stackoverflow.com/questions/9985559/organizing-a-multiple-file-go-project/51942843#51942843)
2. [medium](https://medium.com/@benbjohnson/structuring-applications-in-go-3b04be4ff091)
3. [medium](https://medium.com/golang-learn/go-project-layout-e5213cdcfaa2)

#### P39. ¿Cómo compilas `main.go` a un ejecutable que corra en macOS arm64?

- [ ] Establecer GOOS en **arm64** y GOARCH en **darwin**.
- [ ] Establecer GOOS en **osx** y GOARCH en **arm64**.
- [ ] Establecer GOOS en **arm64** y GOARCH en **osx**.
- [x] Establecer GOOS en **darwin** y GOARCH en **arm64**.

[documentation](https://pkg.go.dev/cmd/go#hdr-Build_constraints)

#### P40. ¿Cuál es la sintaxis correcta para iniciar una goroutine que imprima `Hello Gopher!`?

- [ ] `go(fmt.Println("Hello Gopher!"))`
- [ ] `go func() { fmt.Println("Hello Gopher!") }`
- [x] `go fmt.Println("Hello Gopher!")`
- [ ] `Go fmt.Println("Hello Gopher!")`

[Ejemplo](https://go.dev/play/p/KGgnAWpZMrS)

#### P41. Si iteras sobre un `map` en un `for range`, ¿en qué orden se accederán los pares clave:valor?

- [x] en un orden seudorandom que no puede predecirse
- [ ] en orden inverso a como fueron agregados (LIFO)
- [ ] ordenados por clave ascendente
- [ ] en el orden en que se agregaron (FIFO)

[Referencia](https://go.dev/ref/spec#:~:text=The%20iteration%20order%20over%20maps%20is%20not%20specified)

#### P42. ¿Una forma idiomática de personalizar la representación de una struct en una cadena formateada?

- [ ] No hay forma de personalizar la representación en cadena de un tipo.
- [ ] Construirla por partes llamando campos cada vez.
- [x] Implementar un método `String() string`
- [ ] Crear una función envoltorio que acepte tu tipo y devuelva un string.

[Referencia](https://go.dev/doc/effective_go#printing)

#### P43. ¿Cómo evitas una fuga de goroutine en este código?

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

- [ ] Usar un `sync.WaitGroup`.
- [x] Hacer que `ch` sea un canal con buffer.
- [ ] Agregar un `default` al `select`.
- [ ] Usar `runtime.SetFinalizer`.

[Referencia](https://www.ardanlabs.com/blog/2018/11/goroutine-leaks-the-forgotten-sender.html)

#### P44. ¿Qué imprimirá este código?

```go
var i int8 = 120
i += 10
fmt.Println(i)
```

- [x] -126
- [ ] 0
- [ ] NaN
- [ ] 130

[Go Playground](https://go.dev/play/p/T31_JuFioaC)

#### P45. Dada la definición de `worker` a continuación, ¿cuál es la sintaxis correcta para iniciar una goroutine que llame a `worker` y envíe el resultado a un canal llamado `ch`?

```go
func worker(m Message) Result
```

- [ ]

```go
go func() {
    r := worker(m)
    ch <- r
}
```

- [ ]

```go
go func() {
    r := worker(m)
    r -> ch
} ()
```

- [x]

```go
go func() {
    r := worker(m)
    ch <- r
} ()
```

- [ ]

```go
go ch <- worker(m)
```

[Go Playground](https://go.dev/play/p/96j7tuQKF50)

#### P46. En este código, ¿qué nombres están exportados?

```go
package os

type FilePermission int
type userID int
```

- [x] FilePermission
- [ ] ninguna de las respuestas
- [ ] FilePermission y userID
- [ ] userID

[Referencia](https://go.dev/tour/basics/3)

#### P47. ¿Cuál de las siguientes es correcta sobre las estructuras en Go?

- [ ] `struct` es otro tipo definido por el usuario que permite combinar datos de distintos tipos.
- [ ] Las estructuras se usan para representar un registro.
- [ ] Para definir una estructura, debes usar las sentencias `type` y `struct`.
- [x] Todas las anteriores.

#### P48. ¿Qué hace el comando incorporado `generate` del compilador de Go?

- [ ] Proporciona subcomandos `sql`, `json`, `yaml` y opciones `--schema` y `--objects` para generar código.
- [ ] Busca archivos con nombres que terminen en `_generate.go`, y luego compila y ejecuta cada uno individualmente.
- [x] Escanea el código fuente buscando comentarios `//go:generate` y ejecuta el comando de terminal especificado en cada uno.
- [ ] Tiene subcomandos `mocks` y `tests` para generar archivos `.go`.

[Generate Go files by processing source](https://pkg.go.dev/cmd/go#hdr-Generate_Go_files_by_processing_source)

#### P49. Usando el paquete `time`, ¿cómo obtienes el tiempo 90 minutos desde ahora?

- [ ] `time.Now().Add(90)`
- [ ] `time.Now() + (90 * time.Minute)`
- [ ] `time.Now() + 90`
- [x] `time.Now().Add(90 * time.Minute)`

[Ejemplo de (Time) Add](https://pkg.go.dev/time#example-Time.Add)

#### P50. Un programa usa un canal para imprimir cinco enteros dentro de una goroutine mientras alimenta el canal con enteros desde la rutina principal, pero no funciona tal como está. ¿Qué debes cambiar para que funcione?

- [ ] Agregar `close(ch)` inmediatamente después de `wg.Wait()`.
- [x] Agregar un segundo parámetro a `make(chan, int)`, p. ej. `make(chan int, 5)`.
- [ ] Quitar el uso innecesario de `WaitGroup`, p. ej. todas las líneas que comienzan con `wg`.
- [ ] Mover la goroutine de 7 líneas inmediatamente antes de `wg.Wait()`.

[Referencia](https://www.ardanlabs.com/blog/2018/11/goroutine-leaks-the-forgotten-sender.html)

#### P51. Después de importar `encoding/json`, ¿cómo accedes a la función `Marshal`?

- [ ] `encoding.json.Marshal`
- [ ] `encoding/json.Marshal`
- [ ] `Marshal`
- [x] `json.Marshal`

[encoding/json#Marshal example](https://pkg.go.dev/encoding/json#example-Marshal)

#### P52. ¿Cuáles son los dos segmentos de código faltantes para completar el uso de `context.Context` e implementar un timeout de tres segundos para este cliente HTTP que realiza un GET?

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

        // #1: <=== ¿Qué va aquí?

        req, _ := http.NewRequest(http.MethodGet,
                "https://linkedin.com",
                nil)

        // #2: <=== ¿Qué va aquí?

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

- [ ]

```go
      ctx.SetTimeout(3*time.Second)
      req.AttachContext(ctx)
```

- [x]

```go
      ctx, cancel = context.WithTimeout(ctx, 3*time.Second); defer cancel()
      req = req.WithContext(ctx)
```

- [ ]

```go
      ctx, cancel = context.WithTimeout(ctx, 3*time.Second); defer cancel() #2: req.AttachContext(ctx)
```

- [ ]

```go
      ctx.SetTimeout(3*time.Second)
      req = req.WithContext(ctx)
```

1. [context#WithTimeout](https://pkg.go.dev/context#WithTimeout)
2. [net/http#Request.WithContext](https://pkg.go.dev/net/http#Request.WithContext)

#### P53. Si tienes una struct llamada `Client` definida en el mismo archivo `.go`, ¿cómo exportas una variable con un valor por defecto para que sea accesible por otros paquetes?

- [ ] ``````go
                  let Default := new Client()
                  ```

              ````

          `````

      ``````

- [ ] ``````go
                  public default = &Client()
                  ```

              ````

          `````

      ``````

- [x] ``````go
                  var Default = &Client{}
                  ```

              ````

          `````

      ``````

- [ ] ``````go
                  export default := new Client{}
                  ```
              ````
          `````
      ``````

#### P54. Este programa imprime `{Master Chief Spartan Protagonist Halo}`. ¿Cómo harías para que imprima `Master Chief - a Spartan - is the Protagonist of Halo`?

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
  // Reemplaza
  // fmt.Println(mc)
  // con esto:

  fmt.Printf("(?P<Name>) - a (?P<Class>) - is the (?P<Role>) of (?P<Game>)", mc)
  ```

- [ ] B

  ```go
  // Reemplaza
  // fmt.Println(mc)
  // con esto:
  fmt.Println(mc, func(c Character) string {
        return c. Name + " - a " + c.Class + " - is the " + c.Role + " of " + c.Game
  })
  ```

- [x] C

  ```go
  // agrega esto al paquete `main`

  func (c Character) String() string {
        return fmt.Sprintf("%s - a %s - is the %s of %s", c.Name, c.Class, c.Role,c.Game)
  }
  ```

- [ ] D

  ```go
   // agrega esto al paquete `main`

  func (c Character) OnPrint() {
        fmt.Println("{{c.Name}} - a {{c.Class}} - is the {{c.Role}} of {{c.Game}}")
  }
  ```

1. [fmt#Stringer](https://pkg.go.dev/fmt#Stringer)

#### P55. ¿Cómo implementarías un método `Append()` funcional para `Clients`?

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

#### P56. ¿Cómo recuperarías de un `panic()` lanzado por una función llamada sin permitir que tu programa falle, asumiendo que tu respuesta se ejecute en el mismo ámbito donde ocurrirá el `panic`?

- [ ] Envolver la llamada en una función anónima con tipo de retorno `panic` y luego manejarla.
- [ ] Usar `try{ ... }` y `catch{ ... }`.
- [x] Usar `defer func { ... }()` antes de la llamada y manejar el `panic` dentro de la función.
- [ ] Prefijar la llamada con `@` para forzar retorno como `error`.

#### P57. ¿Qué imprimirá este código?

```go
var n int
fmt.Println (n)
```

- [x] 0
- [ ] nil
- [ ] un valor aleatorio
- [ ] 1

> En Go, una variable no inicializada toma su valor cero. Para `int`, es 0.

#### P58. Al crear una cadena formateada, ¿qué verbo debes usar para invocar `String() string` de un tipo personalizado?

- [x] %s
- [ ] %b
- [ ] %v
- [ ] %string

> `%s` formatea usando la representación de cadena; si existe `String()`, se invoca.

#### P59. ¿Cuál NO es un valor válido para `layout` al llamar `time.Now().Format(layout)`?

- [ ] time.REC3339
- [x] "1970-01-01"
- [ ] "Jan 2nd 2006"
- [ ] time.Kitchen

[time#Time.Format](https://pkg.go.dev/time#Time.Format)

#### P60. ¿Cómo señalas al compilador de Go que la struct `Namespace` debe implementar la interfaz `JSONConverter`? (Mismo paquete que `Namespace`.)

- [ ] var \_ JSONConverter = nil. (\*Namespace)
- [x] var \_ JSONConverter = (\*Namespace) (nil)
- [ ] ``````go
                  type Namespace struct {
                      implements JSONConverter
                  }
                  ```
              ````
          `````
      ``````
- [ ] ``````go
                  type Namespace struct {
                      JSONConverter
                  }
                  ```
              ````
          `````
      ``````

> Esta sintaxis verifica que `*Namespace` satisface `JSONConverter`.

#### P61. ¿Qué afirmación sobre tipado e interfaces es falsa?

- [ ] Una firma de método es el nombre más los tipos de parámetros y retornos.
- [x] Una struct debe declarar explícitamente con `implements` que implementa una interfaz.
- [ ] Una interfaz declara métodos y firmas que un tipo debe implementar.
- [ ] Variables, parámetros y retornos deben estar tipados como tipo incorporado, alias, derivado, compuesto o interfaz.

> En Go, un tipo satisface una interfaz automáticamente si implementa todos sus métodos.

#### P62. Completa este programa para generar la salida especificada, asumiendo la tabla SQL

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

        // #1 <=== ¿Qué va aquí?

        for results.Next() {
                var g Game

                // #2 <=== ¿Qué va aquí?

                if err != nil {
                        panic(err)
                }

                // #3 <=== ¿Qué va aquí?

        }

        for i, g := range games {
                fmt.Printf("%d: %+v\n", i, g)
        }

}
```

- [ ]

```go
#1: games := make([]*Game, results.RowsAffected())
#2: g, err = results.Fetch()
#3: games[results.Index()] = &g
```

- [ ]

```go
#1: games := []Game{}
#2: g, err = results.Fetch()
#3: games = append(games,g)
```

- [ ]

```go
#1: games := map[int]Game{}
#2: err = results.Scan(&g)
#3: games[g.GameId] = g
```

- [x]

```go
#1: games := make(map[int]*Game, 0)
#2: err = results.Scan(&g.GameId, &g.Title, &g.YearReleased)
#3: games[g.GameId] = &g
```

#### P63. Completa los espacios

1. Los archivos de prueba en Go deben **\_**.
2. Las pruebas individuales se identifican por **\_**.
3. Puedes ejecutar subpruebas **\_**.
4. Registras el error y marcas la prueba como fallida **\_**.

- [ ] almacenarse en un subdirectorio `/test/` de ese paquete
      <br/>funciones que aceptan un parámetro `testing.Tester`
      <br/>escribiendo funciones con nombres que coincidan con `^Subtest`
      <br/>llamando a `testing.AssertionFailed`

- [x] terminar en `_test.go`
      <br/>nombres de función que coincidan con `^Test[A-Z]`
      <br/>llamando a `t.Run()`
      <br/>llamando a `t.Errorf()`

- [ ] comenzar con `test_`
      <br/>funciones que coincidan con `[a-z]Test$`
      <br/>llamando a `testing.Subtest()`
      <br/>permitiendo que `testing.Assert()` falle su aserción

- [ ] almacenarse en el subdirectorio `/test/` de la raíz del proyecto
      <br/>funciones que acepten un parámetro `testing.Test`
      <br/>pasando closures a `testing.AddSubtest()`
      <br/>devolviendo un `error` desde la función

#### P64. ¿Para qué tipo es `rune` un alias?

- [ ] char
- [ ] byte
- [x] int32
- [ ] string

1. [Strings, bytes, runes and characters in Go](https://go.dev/blog/strings)

#### P65. ¿Cuándo puedes usar la sintaxis `:=` para asignar a múltiples variables? Por ejemplo:

```go
x, err := myFunc()
```

- [x] si al menos una no ha sido declarada en ese bloque léxico
- [ ] en todo momento, ya que sobrescribirá variables existentes
- [ ] si ninguna variable con esos nombres es accesible
- [ ] si ninguna de las variables existe en ese bloque léxico

1. [Short variable declarations](https://go.dev/ref/spec#Short_variable_declarations)

#### P66. ¿Cómo ves la salida del profiler en `cpu.pprof` en el navegador?

- [ ] `go pprof -to SVG cpu.prof`
- [x] `go tool pprof -http=:8080 cpu.pprof`
- [ ] `go tool pprof cpu.pprof`
- [ ] `go tool trace cpu.pprof`

#### P67. ¿Cuándo evalúa a `nil` una variable de tipo `interface{}`?

- [x] Se le ha asignado un tipo dinámico cuyo valor es `nil`.
- [ ] Se ha establecido explícitamente en `nil`.
- [ ] No se le ha asignado un tipo dinámico.
- [ ] No puede evaluar a `nil`.

#### P68. ¿Qué valor tiene una variable `string` si ha sido asignada pero no inicializada?

- [ ] nil
- [ ] undefined
- [ ] null
- [x] ""

#### P69. ¿Qué función incorporada se usa para detener la ejecución del programa?

- [x] panic
- [ ] No existe tal función.
- [ ] raiseException
- [ ] exit

#### P70. ¿Cuál será la salida?

```go
a,b := 1, 2
b,c:= 3, 4
fmt.Println(a, b, c)
```

- [x] 1 3 4
- [ ] 1 2 3
- [ ] 1 2 4
- [ ] No compilará.

[Go Playground](https://go.dev/play/p/qUI50GNGWTq)

### P71. ¿Cuál es el operador para una condición AND lógica?

- [ ] -
- [ ] and
- [x] &&
- [ ] ||

### P72. ¿Qué es una función anónima en Go?

- [ ] Una función sin tipo de retorno.
- [ ] Una función sin parámetros.
- [x] Una función sin nombre.
- [ ] Una función declarada dentro de otra función.

### P73. ¿Qué palabra clave se usa para declarar una función anónima en Go?

- [ ] `func`
- [ ] `lambda`
- [x] `func()`
- [ ] `anonymous`

#### P74. ¿Cuál es la principal ventaja de usar funciones anónimas en Go?

- [ ] Siempre tienen mejor rendimiento que las funciones con nombre.
- [ ] Pueden tener múltiples valores de retorno.
- [x] Pueden definirse inline donde se usan.
- [ ] Tienen una sintaxis más corta que las funciones con nombre.

#### P75. ¿Cuál es la sintaxis para llamar inmediatamente a una función anónima tras su declaración en Go?

- [ ] `functionName(){}`
- [ ] `call functionName(){}`
- [x] `func(){}()`
- [ ] `execute func(){}`

[referencia](https://stackoverflow.com/questions/6719089/javascript-anonymous-function-immediate-invocation-execution-expression-vs-dec)

#### P76. ¿Para qué tipos pueden los desarrolladores de Go definir métodos?

- [x] todos los tipos con nombre no incorporados a Go, p. ej. `type Example int` pero no `int`, `type Example struct{...}` pero no `struct`, etc.
- [ ] solo tipos `struct`, `map` y `slice`, p. ej. `type Example struct{…}`
- [ ] solo tipos `struct`, p. ej. `type Example struct{...}`
- [ ] todos los tipos

> Se pueden definir métodos para cualquier tipo con nombre que no sea incorporado. [reference](https://go.dev/ref/spec#Method_declarations)
