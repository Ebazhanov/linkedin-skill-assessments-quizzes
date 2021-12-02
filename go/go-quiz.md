## Go (Programming Language)

#### Q1. What do you need for two functions to be the same type?

- [x] They should share the same signatures, including parameter types and return types.
- [ ] They should share the same parameter types but can return different types.
- [ ] All functions should be the same type.
- [ ] The functions should not be a first class type.

Explanation: [User defined function types in Go (Golang)](https://golangbyexample.com/user-defined-function-type-go/)

#### Q2. What does the `len()` function return if passed a UTF-8 encoded string?

- [ ] the number of characters
- [x] the number of bytes
- [ ] It does not accept string types.
- [ ] the number of code points

Explanation: [Length of string in Go (Golang)](https://golangbyexample.com/length-of-string-golang/).

#### Q3. Which is _not_ a valid loop construct in Go?

- [x] `do { ... } while i < 5`
- [ ] `for _,c := range "hello" { ... }`
- [ ] `for i := 1; i < 5; i++ { ... }`
- [ ] `for i < 5 { ... }`

Explanation: Go has only `for`-loops

#### Q4. How will you add the number 3 to the right side?

`values := []int{1, 1, 2}`

- [ ] `values.append(3)`
- [ ] `values.insert(3, 3)`
- [ ] `append(values, 3)`
- [x] `values = append(values, 3)`

Explanation: slices in GO are immutable, so calling `append` does not modify the slice

#### Q5. What is the value of `Read`?

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
- [ ] a random value

Reference: [IOTA in Go (Golang)](https://golangbyexample.com/iota-in-golang/)

#### Q6. Which is the _only_ valid import statement in Go?

- [ ] `import "github/gin-gonic/gin"`
- [ ] `import "https://github.com/gin-gonic/gin"`
- [ ] `import "../template"`
- [x] `import "github.com/gin-gonic/gin"`

Reference: [Import in GoLang](https://golangdocs.com/import-in-golang)

#### Q7. What would happen if you attempted to compile and run this Go program?

```go
package main
var GlobalFlag string
func main() {
  print("["+GlobalFlag+"]")
}
```

- [ ] It would not compile because `GlobalFlag` was never initialized.
- [x] It would compile and print `[]`.
- [ ] It would compile and print nothing because `"[" +nil+"]"` is also `nil`.
- [ ] It would compile but then panic because `GlobalFlag` was never initialized.

Explanation: most [variables](https://golangbyexample.com/variables-in-golang-complete-guide/) in Go have initial values. For string type, it's an empty string.

Here is this program on [Go Playground](https://play.golang.org/p/TaRIzuD-nxC)

#### Q8. From where is the variable `myVar` accessible if it is declared outside of any functions in a file in package `myPackage` located inside module `myModule`?

- [x] It can be accessed anywhere inside `myPackage`, not the rest of myModule.
- [ ] It can be accessed by any application that imports `myModule`.
- [ ] It can be accessed from anywhere in `myModule`.
- [ ] It can be accessed by other packages in `myModule` as long as they import `myPackage`

Explanation: to make the variable available outside of `myPackage` change the name to `MyVar`.
See also an example of [Exported names](https://tour.golang.org/basics/3) in the Tour of Go.

#### Q9. How do you tell `go test` to print out the tests it is running?

- [ ] `go test`
- [ ] `go test -x`
- [ ] `go test --verbose`
- [x] `go test -v`

Reference: [test package](https://pkg.go.dev/cmd/go/internal/test)

#### Q10. This code printed `{0, 0}`. How can you fix it?

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

- [ ] use `json.Decoder`
- [ ] Pass a pointer to `data`
- [x] Make `X` and `Y` exported (uppercase)
- [ ] Use field tags

Reference: [How to Parse JSON in Golang?](https://www.geeksforgeeks.org/how-to-parse-json-in-golang/)

Fixed version on [Go Playground](https://play.golang.org/p/RdL6y3Zv8ke)

#### Q11. What does a `sync.Mutex` block white it is locked?

- [ ] all goroutines
- [x] any other call to lock that `Mutex`
- [ ] any reads or writes of the variable it is locking
- [ ] any writes to the variable it is locking

Reference: [Mutex in GoLang](https://golangdocs.com/mutex-in-golang)

#### Q12. What is an idiomatic way to pause execution of the current scope until an arbitrary number of goroutines have returned?

- [ ] Pass an `int` and `Mutex` to each and count when they return.
- [ ] Loop over a `select` statement.
- [ ] Sleep for a safe amount of time.
- [x] `sync.WaitGroup`

Explanation: this is exactly what `sync.WaitGroup` is designed for - [Use sync.WaitGroup in Golang](https://nanxiao.me/en/use-sync-waitgroup-in-golang/)

#### Q13. What is a side effect of using `time.After` in a `select` statement?

- [ ] It blocks the other channels.
- [x] It is meant to be used in select statements without side effects.
- [ ] It blocks the `select` statement until the time has passed.
- [ ] The goroutine does not end until the time passes.

Note: it doesn't block `select` and does not block other channels.

#### Q14. What is the select statement used for?

- [ ] executing a function concurrently
- [ ] executing a different case based on the type of a variable
- [ ] executing a different case based on the value of a variable
- [x] executing a different case based on which channel returns first

#### Q15. According to the Go documentation standard, how should you document this function?

```go
func Add(a, b int) {
  return a + b
}
```

- [ ] A

```go
// Calculate a + b
// - a: int
// - b: int
// - returns: int
func Add(a, b int) {
  return a + b
}
```

- [ ] B

```go
// Does a + b
func Add(a, b int) {
  return a + b
}
```

- [x] C

```go
// Add returns the sum of a and b
func Add(a, b int) {
  return a + b
}
```

- [ ] D

```go
// returns the sum of a and b
func Add(a, b int) {
  return a + b
}
```

Explanation: documentation block should start with a function name

#### Q16. What restriction is there on the type of `var` to compile this `i := myVal.(int)?`

- [ ] `myVal` must be an integer type, such as `int`, `int64`, `int32`, etc.
- [ ] `myVal` must be able to be asserted as an `int`.
- [x] `myVal` must be an interface.
- [ ] `myVal` must be a numeric type, such as `float64` or `int64`.

Explanation: This kind of type casting (using `.(type)`) is used on interfaces only.
See [this example](https://tutorialedge.net/golang/snippets/type-casting-interface-to-string-go/) for instance.
Primitive types are type-casted differently - [Type-casting in GoLang](https://golangdocs.com/type-casting-in-golang)

Example on [Go Playground](https://play.golang.org/p/TXF_JBvThp6)

#### Q17. What is a channel?

- [ ] a global variable
- [x] a medium for sending values between goroutines
- [ ] a dynamic array of values
- [ ] a lightweight thread for concurrent programming

Reference: [Channels](https://tour.golang.org/concurrency/2)

#### Q18. How can you make a file build only on Windows?

- [ ] Check runtime.GOOS.
- [ ] Add a // +build windows comment anywhere in the file.
- [ ] Add a \_ prefix to the file name.
- [x] Add a // +build windows comment at the top of the file.

Reference: [How to use conditional compilation with the go build tool, Oct 2013](https://dave.cheney.net/2013/10/12/how-to-use-conditional-compilation-with-the-go-build-tool)

#### Q19. What is the correct way to pass this as a body of an HTTP POST request?

```go
data := "A group of Owls is called a parliament"
```

- [ ] resp, err := http.Post("https://httpbin.org/post", "text/plain", []byte(data))
- [ ] resp, err := http.Post("https://httpbin.org/post", "text/plain", data)
- [x] resp, err := http.Post("https://httpbin.org/post", "text/plain", strings.NewReader(data))
- [ ] resp, err := http.Post("https://httpbin.org/post", "text/plain", &data)

Reference: [net/http#Client.Post](https://pkg.go.dev/net/http#Client.Post)

#### Q20. What should the idiomatic name be for an interface with a single method and the signature `Save() error`?

- [ ] Saveable
- [ ] SaveInterface
- [ ] ISave
- [x] Saver

Reference: [Effective Go, Interface names](https://golang.org/doc/effective_go#interface-names)

#### Q21. A `switch` statement **\_** its own lexical block. Each `case` statement **\_** an additional lexical block.

- [ ] does not create; creates
- [ ] does not create; does not create
- [x] creates; creates
- [ ] creates; does not create

Reference: [Go Language Core technology (Volume one) 1.5-scope](https://topic.alibabacloud.com/a/go-language-core-technology-volume-one-15-font-colorredscopefont_1_38_30923325.html)

Relevant excerpt from the article:

> _The second if statement is nested inside the first, so a variable declared in the first if statement is visible to the second if statement. There are similar rules in switch: Each case has its own lexical block in addition to the conditional lexical block._

#### Q22. What is the default case sensitivity of the JSON `Unmarshal` function?

- [x] The default behavior is case insensitive, but it can be overridden.
- [ ] Fields are matched case sensitive.
- [ ] Fields are matched case insensitive.
- [ ] The default behavior is case sensitive, but it can be overridden.

Reference: [encoding/json#Unmarshal](https://pkg.go.dev/encoding/json#Unmarshal)

Relevant excerpt from the article:

> _To unmarshal JSON into a struct, Unmarshal matches incoming object keys to the keys used by Marshal (either the struct field name or its tag), preferring an exact match but also accepting a case-insensitive match. By default, object keys which don't have a corresponding struct field are ignored (see Decoder.DisallowUnknownFields for an alternative)._

#### Q23. What is the difference between the `time` package’s `Time.Sub()` and `Time.Add()` methods?

- [ ] Time.Add() is for performing addition while Time.Sub() is for nesting timestamps.
- [ ] Time.Add() always returns a later time while time.Sub always returns an earlier time.
- [x] They are opposites. Time.Add(x) is the equivalent of Time.Sub(-x).
- [ ] Time.Add() accepts a Duration parameter and returns a Time while Time.Sub() accepts a Time parameter and returns a Duration.

Reference: [time#Time.Add](https://pkg.go.dev/time#Time.Add)

Reference: [time#Time.Sub](https://pkg.go.dev/time#Time.Sub)

#### Q24. What is the risk of using multiple field tags in a single struct?

- [ ] Every field must have all tags to compile.
- [x] It tightly couples different layers of your application.
- [ ] Any tags after the first are ignored.
- [ ] Missing tags panic at runtime.

Reference: [Example Code / b29r0fUD1cp](https://play.golang.org/p/b29r0fUD1cp)

#### Q25. Where is the built-in recover method useful?

- [ ] in the main function
- [ ] immediately after a line that might panic
- [x] inside a deferred function
- [ ] at the beginning of a function that might panic

Reference: [Example of Recover Function in Go (Golang)](https://golangbot.com/panic-and-recover/#recoveringfromapanic)

Relevant excerpt from the article:

> _Recover is useful only when called inside deferred functions. Executing a call to recover inside a deferred function stops the panicking sequence by restoring normal execution and retrieves the error message passed to the panic function call. If recover is called outside the deferred function, it will not stop a panicking sequence._

#### Q26. Which choice does _not_ send output to standard error?

- [x] println(message)
- [ ] log.New(os.Stderr, "", 0).Println(message)
- [ ] fmt.Errorf("%s\n", message)
- [ ] fmt.Fprintln(os.Stderr, message)

#### Q27. How can you tell Go to import a package from a different location?

- [ ] Use a proxy.
- [ ] Change the import path.
- [x] Use a replace directive in go.mod.
- [ ] Use a replace directory.

#### Q28. If your current working directory is the top level of your project, which command will run all its test packages?

- [ ] go test all
- [ ] go run --all
- [ ] go test .
- [x] go test ./...

Reference: [Example of testing in Go (Golang)](https://pkg.go.dev/testing)

Reference: [Example of cmd in Go (Golang)](https://pkg.go.dev/cmd/go)

Relevant excerpt from the article:

> _Relative patterns are also allowed, like "go test ./..." to test all subdirectories._

#### Q29. Which encodings can you put in a string?

- [ ] any, it accepts arbitary bytes
- [ ] any Unicode format
- [ ] UTF-8 or ASCII
- [x] UTF-8

Reference: [Example of encoding in Go (Golang)](https://pkg.go.dev/golang.org/x/text/encoding)

Relevant excerpt from the article:

> _Package encoding defines an interface for character encodings, such as Shift JIS and Windows 1252, that can convert to and from UTF-8._

#### Q30. How is the behavior of `t.Fatal` different inside a `t.Run`?

- [ ] There is no difference.
- [ ] t.Fatal does not crash the test harness, preserving output messages.
- [ ] t.Fatal stops execution of the subtest and continues with other test cases.
- [ ] t.Fatal stops all tests and contains extra information about the failed subtest.

#### Q31. What does `log.Fatal` do?

- [ ] It raises a panic.
- [ ] It prints the log and then raises a panic.
- [x] It prints the log and then safely exits the program.
- [ ] It exits the program.

Reference: [Example of func Fatal in Go (Golang)](https://pkg.go.dev/log#Fatal)

Relevant excerpt from the article:

> _Fatal is equivalent to Print() followed by a call to os.Exit(1)._

#### Q32. Which is a valid Go time format literal?

- [x] "2006-01-02"
- [ ] "YYYY-mm-dd"
- [ ] "y-mo-d"
- [ ] "year-month-day"

Reference: [Example of func Time in Go (Golang)](https://pkg.go.dev/time)

Relevant excerpt from the article:

> _Most programs can use one of the defined constants as the layout passed to Format or Parse. The rest of this comment can be ignored unless you are creating a custom layout string._
