## Go (Programming Language)

#### Q1. What do you need for two functions to be the same type?

- [x] They should share the same signatures, including parameter types and return types.
- [ ] They should share the same parameter types but can return different types.
- [ ] All functions should be the same type.
- [ ] The functions should not be a first class type.

[User defined function types in Go (Golang)](https://golangbyexample.com/user-defined-function-type-go/)

#### Q2. What does the `len()` function return if passed a UTF-8 encoded string?

- [ ] the number of characters
- [x] the number of bytes
- [ ] It does not accept string types.
- [ ] the number of code points

[Length of string in Go (Golang)](https://golangbyexample.com/length-of-string-golang/).

#### Q3. Which is _not_ a valid loop construct in Go?

- [x] `do { ... } while i < 5`
- [ ] `for _,c := range "hello" { ... }`
- [ ] `for i := 1; i < 5; i++ { ... }`
- [ ] `for i < 5 { ... }`

**Explanation:** Go has only `for`-loops

#### Q4. How will you add the number 3 to the right side?

`values := []int{1, 1, 2}`

- [ ] `values.append(3)`
- [ ] `values.insert(3, 3)`
- [ ] `append(values, 3)`
- [x] `values = append(values, 3)`

**Explanation:** slices in GO are immutable, so calling `append` does not modify the slice

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

[IOTA in Go (Golang)](https://golangbyexample.com/iota-in-golang/)

#### Q6. Which is the _only_ valid import statement in Go?

- [ ] `import "github/gin-gonic/gin"`
- [ ] `import "https://github.com/gin-gonic/gin"`
- [ ] `import "../template"`
- [x] `import "github.com/gin-gonic/gin"`

[Import in GoLang](https://golangdocs.com/import-in-golang)

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

1. [variables](https://golangbyexample.com/variables-in-golang-complete-guide/) in Go have initial values. For string type, it's an empty string.
2. [Go Playground](https://play.golang.org/p/TaRIzuD-nxC)

#### Q8. From where is the variable `myVar` accessible if it is declared outside of any functions in a file in package `myPackage` located inside module `myModule`?

- [x] It can be accessed anywhere inside `myPackage`, not the rest of myModule.
- [ ] It can be accessed by any application that imports `myModule`.
- [ ] It can be accessed from anywhere in `myModule`.
- [ ] It can be accessed by other packages in `myModule` as long as they import `myPackage`

**Explanation**: to make the variable available outside of `myPackage` change the name to `MyVar`.
See also an example of [Exported names](https://tour.golang.org/basics/3) in the Tour of Go.

#### Q9. How do you tell `go test` to print out the tests it is running?

- [ ] `go test`
- [ ] `go test -x`
- [ ] `go test --verbose`
- [x] `go test -v`

[test package](https://pkg.go.dev/cmd/go/internal/test)

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

1. [How to Parse JSON in Golang?](https://www.geeksforgeeks.org/how-to-parse-json-in-golang/)
2. [Go Playground](https://play.golang.org/p/RdL6y3Zv8ke)

#### Q11. What does a `sync.Mutex` block while it is locked?

- [ ] all goroutines
- [ ] any other call to lock that `Mutex`
- [x] any reads or writes of the variable it is locking
- [ ] any writes to the variable it is locking

1. [Mutex in GoLang](https://golangdocs.com/mutex-in-golang), sync.Mutex locks so only one goroutine at a time can access the locked variable.
2. [sync.Mutex](https://go.dev/tour/concurrency/9)

#### Q12. What is an idiomatic way to pause execution of the current scope until an arbitrary number of goroutines have returned?

- [ ] Pass an `int` and `Mutex` to each and count when they return.
- [ ] Loop over a `select` statement.
- [ ] Sleep for a safe amount of time.
- [x] `sync.WaitGroup`

**Explanation:** this is exactly what `sync.WaitGroup` is designed for - [Use sync.WaitGroup in Golang](https://nanxiao.me/en/use-sync-waitgroup-in-golang/)

#### Q13. What is a side effect of using `time.After` in a `select` statement?

- [ ] It blocks the other channels.
- [ ] It is meant to be used in select statements without side effects.
- [ ] It blocks the `select` statement until the time has passed.
- [x] The goroutine does not end until the time passes.

> Note: it doesn't block `select` and does not block other channels.  
> 1. [time.After() Function in Golang With Examples](https://www.geeksforgeeks.org/time-after-function-in-golang-with-examples/)  
> 2. [How can I use 'time.After' and 'default' in Golang?](https://stackoverflow.com/questions/39212333/how-can-i-use-time-after-and-default-in-golang)  
> 3. [Go Playground example](https://go.dev/play/p/WojTrG1ywRK)

#### Q14. What is the select statement used for?

- [ ] executing a function concurrently
- [ ] executing a different case based on the type of a variable
- [ ] executing a different case based on the value of a variable
- [x] executing a different case based on which channel returns first

[Select statement in GoLang](https://golangdocs.com/select-statement-in-golang)

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

**Explanation:** documentation block should start with a function name

[Comments in Go](https://exercism.org/tracks/go/concepts/comments)

#### Q16. What restriction is there on the type of `var` to compile this `i := myVal.(int)?`

- [ ] `myVal` must be an integer type, such as `int`, `int64`, `int32`, etc.
- [ ] `myVal` must be able to be asserted as an `int`.
- [x] `myVal` must be an interface.
- [ ] `myVal` must be a numeric type, such as `float64` or `int64`.

**Explanation**: This kind of type casting (using `.(type)`) is used on interfaces only.

1. [this example](https://tutorialedge.net/golang/snippets/type-casting-interface-to-string-go/)
2. [Primitive types are type-casted differently](https://golangdocs.com/type-casting-in-golang)
3. [Go Playground](https://play.golang.org/p/TXF_JBvThp6)
4. [Type assertions](https://go.dev/tour/methods/15)

#### Q17. What is a channel?

- [ ] a global variable
- [x] a medium for sending values between goroutines
- [ ] a dynamic array of values
- [ ] a lightweight thread for concurrent programming

[Channels](https://tour.golang.org/concurrency/2)

#### Q18. How can you make a file build only on Windows?

- [ ] Check runtime.GOOS.
- [ ] Add a // +build windows comment anywhere in the file.
- [ ] Add a \_ prefix to the file name.
- [x] Add a // +build windows comment at the top of the file.

1. [How to use conditional compilation with the go build tool, Oct 2013](https://dave.cheney.net/2013/10/12/how-to-use-conditional-compilation-with-the-go-build-tool)
2. [go commands Build constraints](https://pkg.go.dev/cmd/go#hdr-Build_constraints)

> `//go:build windows`  
> "Go versions 1.16 and earlier used a different syntax for build constraints, with a "// +build" prefix. The gofmt command will add an equivalent //go:build constraint when encountering the older syntax."

#### Q19. What is the correct way to pass this as a body of an HTTP POST request?

```go
data := "A group of Owls is called a parliament"
```

- [ ] `resp, err := http.Post("https://httpbin.org/post", "text/plain", []byte(data))`
- [ ] `resp, err := http.Post("https://httpbin.org/post", "text/plain", data)`
- [x] `resp, err := http.Post("https://httpbin.org/post", "text/plain", strings.NewReader(data))`
- [ ] `resp, err := http.Post("https://httpbin.org/post", "text/plain", &data)`

1. [net/http#Client.Post](https://pkg.go.dev/net/http#Client.Post)
2. [http.Post Golang example](https://dev.to/ramu_mangalarapu/httppost-golang-example-5jp)

#### Q20. What should the idiomatic name be for an interface with a single method and the signature `Save() error`?

- [ ] Saveable
- [ ] SaveInterface
- [ ] ISave
- [x] Saver

[Effective Go, Interface names](https://golang.org/doc/effective_go#interface-names)

#### Q21. A `switch` statement **\_** its own lexical block. Each `case` statement **\_** an additional lexical block

- [ ] does not create; creates
- [ ] does not create; does not create
- [x] creates; creates
- [ ] creates; does not create

[Go Language Core technology (Volume one) 1.5-scope](https://topic.alibabacloud.com/a/go-language-core-technology-volume-one-15-font-colorredscopefont_1_38_30923325.html)

Relevant excerpt from the article:

> _The second if statement is nested inside the first, so a variable declared in the first if statement is visible to the second if statement. There are similar rules in switch: Each case has its own lexical block in addition to the conditional lexical block._

#### Q22. What is the default case sensitivity of the JSON `Unmarshal` function?

- [x] The default behavior is case insensitive, but it can be overridden.
- [ ] Fields are matched case sensitive.
- [ ] Fields are matched case insensitive.
- [ ] The default behavior is case sensitive, but it can be overridden.

[encoding/json#Unmarshal](https://pkg.go.dev/encoding/json#Unmarshal)

Relevant excerpt from the article:

> _To unmarshal JSON into a struct, Unmarshal matches incoming object keys to the keys used by Marshal (either the struct field name or its tag), preferring an exact match but also accepting a case-insensitive match. By default, object keys which don't have a corresponding struct field are ignored (see Decoder.DisallowUnknownFields for an alternative)._

#### Q23. What is the difference between the `time` package’s `Time.Sub()` and `Time.Add()` methods?

- [ ] Time.Add() is for performing addition while Time.Sub() is for nesting timestamps.
- [ ] Time.Add() always returns a later time while time.Sub always returns an earlier time.
- [ ] They are opposites. Time.Add(x) is the equivalent of Time.Sub(-x).
- [x] Time.Add() accepts a Duration parameter and returns a Time while Time.Sub() accepts a Time parameter and returns a Duration.

1. [time#Time.Add](https://pkg.go.dev/time#Time.Add)
2. [time#Time.Sub](https://pkg.go.dev/time#Time.Sub)

#### Q24. What is the risk of using multiple field tags in a single struct?

- [ ] Every field must have all tags to compile.
- [x] It tightly couples different layers of your application.
- [ ] Any tags after the first are ignored.
- [ ] Missing tags panic at runtime.

1. [Example Code / b29r0fUD1cp](https://play.golang.org/p/b29r0fUD1cp)
2. [How To Use Struct Tags in Go](https://www.digitalocean.com/community/tutorials/how-to-use-struct-tags-in-go)

#### Q25. Where is the built-in recover method useful?

- [ ] in the main function
- [ ] immediately after a line that might panic
- [x] inside a deferred function
- [ ] at the beginning of a function that might panic

[Example of Recover Function in Go (Golang)](https://golangbot.com/panic-and-recover/#recoveringfromapanic)

Relevant excerpt from the article:

> _Recover is useful only when called inside deferred functions. Executing a call to recover inside a deferred function stops the panicking sequence by restoring normal execution and retrieves the error message passed to the panic function call. If recover is called outside the deferred function, it will not stop a panicking sequence._

#### Q26. Which choice does _not_ send output to standard error?

- [ ] `println(message)`
- [ ] `log.New(os.Stderr, "", 0).Println(message)`
- [x] `fmt.Errorf("%s\n", message)`
- [ ] `fmt.Fprintln(os.Stderr, message)`

1. [func println](https://pkg.go.dev/builtin#println): writes the result to _standard error_.
2. [func New](https://pkg.go.dev/log#New): func New(out io.Writer, prefix string, flag int) \*Logger; the out variable _sets the destination_ to which log data will be written.
3. [func Errorf](https://pkg.go.dev/fmt#Errorf): Errorf formats according to a format specifier and _returns the string_ as a value.
4. [func Fprintln](https://pkg.go.dev/fmt#Fprintln): func Fprintln(w io.Writer, a ...any) (n int, err error); Fprintln formats using the default formats for its operands and _writes to w_.

#### Q27. How can you tell Go to import a package from a different location?

- [ ] Use a proxy.
- [ ] Change the import path.
- [x] Use a replace directive in go.mod.
- [ ] Use a replace directory.

1. [Call your code from another module](https://go.dev/doc/tutorial/call-module-code): chapter 5., `go mod edit -replace example.com/greetings=../greetings`.
2. [go.mod replace directive](https://go.dev/doc/modules/gomod-ref#replace)

#### Q28. If your current working directory is the top level of your project, which command will run all its test packages?

- [ ] `go test all`
- [ ] `go run --all`
- [ ] `go test .`
- [x] `go test ./...`

1. [Example of testing in Go (Golang)](https://pkg.go.dev/testing)
2. [Example of cmd in Go (Golang)](https://pkg.go.dev/cmd/go)

Relevant excerpt from the article:

> _Relative patterns are also allowed, like "go test ./..." to test all subdirectories._

#### Q29. Which encodings can you put in a string?

- [ ] any, it accepts arbitary bytes
- [ ] any Unicode format
- [ ] UTF-8 or ASCII
- [x] UTF-8

1. [Strings, bytes, runes and characters in Go](https://go.dev/blog/strings)

Relevant excerpt from the article:

> _In short, Go source code is UTF-8, so the source code for the string literal is UTF-8 text._

2. [Example of encoding in Go (Golang)](https://pkg.go.dev/golang.org/x/text/encoding)

Relevant excerpt from the article:

> _Package encoding defines an interface for character encodings, such as Shift JIS and Windows 1252, that can convert to and from UTF-8._

#### Q30. How is the behavior of `t.Fatal` different inside a `t.Run`?

- [ ] There is no difference.
- [ ] t.Fatal does not crash the test harness, preserving output messages.
- [x] t.Fatal stops execution of the subtest and continues with other test cases.
- [ ] t.Fatal stops all tests and contains extra information about the failed subtest.

1. [Reference:](https://go.dev/play/p/gtne3iRL9AX)
2. [testing package in Go](https://pkg.go.dev/testing), the relevant excerpt from the article:

> `Fatal` is equivalent to `Log` followed by `FailNow`.  
> `Log` formats its arguments using default formatting, analogous to `Println`, and records the text in the error log.  
> `FailNow` marks the function as having failed and **stops its execution by calling `runtime.Goexit` (which then runs all deferred calls in the current goroutine). Execution will continue at the next test or benchmark.** `FailNow` must be called from the goroutine running the test or benchmark function, not from other goroutines created during the test. Calling `FailNow` does not stop those other goroutines.  
> `Run` runs `f` as a subtest of `t` called name. It runs `f` in a separate goroutine and blocks until `f` returns or calls `t.Parallel` to become a parallel test. Run reports whether `f` succeeded (or at least did not fail before calling `t.Parallel`).  
> Run may be called simultaneously from multiple goroutines, but all such calls must return before the outer test function for t returns.

#### Q31. What does `log.Fatal` do?

- [ ] It raises a panic.
- [ ] It prints the log and then raises a panic.
- [x] It prints the log and then safely exits the program.
- [ ] It exits the program.

[Example of func Fatal in Go (Golang)](https://pkg.go.dev/log#Fatal)

Relevant excerpt from the article:

> _`Fatal` is equivalent to `Print()` followed by a call to `os.Exit(1)`._

#### Q32. Which is a valid Go time format literal?

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

#### Q33. How should you log an error (err)

- [ ] `log.Error(err)`
- [x] `log.Printf("error: %v", err)`
- [ ] `log.Printf(log.ERROR, err)`
- [ ] `log.Print("error: %v", err)`

**Explanation:** There is defined neither _log.ERROR_, nor _log.Error()_ in [log package in Go](https://pkg.go.dev/log); `log.Print()` arguments are handled in the manner of `fmt.Print()`; `log.Printf()` arguments are handled in the manner of `fmt.Printf()`.

#### Q34. Which file names will the `go test` command recognize as test files?

- [ ] any that starts with `test`
- [ ] any files that include the word `test`
- [ ] only files in the root directory that end in `_test.go`
- [x] any that ends in `_test.go`

1. [Test packages in go command in Go](https://pkg.go.dev/cmd/go#hdr-Test_packages): _'Go test' recompiles each package along with any files with names matching the file pattern "\*\_test.go"._
2. [Add a test in Go](https://go.dev/doc/tutorial/add-a-test)

#### Q35. What will be the output of this code?

```go
ch := make(chan int)
ch <- 7
val := <-ch
fmt.Println(val)
```

- [ ] 0
- [x] It will deadlock
- [ ] It will not compile
- [ ] 2.718

[Go Playground share](https://go.dev/play/p/SQlfg8YSEOz), output:

```text
fatal error: all goroutines are asleep - deadlock!

goroutine 1 [chan send]:
main.main()
 /tmp/sandbox2282523250/prog.go:7 +0x37

Program exited.
```

#### Q36. What will be the output of this program?

```go
ch := make(chan int)
close(ch)
val := <-ch
fmt.Println(val)
```

- [ ] It will deadlock
- [ ] It will panic
- [x] 0
- [ ] NaN

[Go Playground share](https://go.dev/play/p/DjXq9wzJm5M), output:

```text
0

Program exited.
```

#### Q37. What will be printed in this code?

```go
var stocks map[string]float64 // stock -> price
price := stocks["MSFT"]
fmt.Printf("%f\n", price)
```

- [ ] 0
- [x] 0.000000
- [ ] The code will panic
- [ ] NaN

[Go Playground share](https://go.dev/play/p/CjdHskV1xq1), output:

```text
0.000000

Program exited.
```

#### Q38. What is the common way to have several executables in your project?

- [x] Have a cmd directory and a directory per executable inside it.
- [ ] Comment out main.
- [ ] Use build tags.
- [ ] Have a pkg directory and a directory per executable inside it.

1. [stackoverflow](https://stackoverflow.com/questions/9985559/organizing-a-multiple-file-go-project/51942843#51942843)
2. [medium](https://medium.com/@benbjohnson/structuring-applications-in-go-3b04be4ff091)
3. [medium](https://medium.com/golang-learn/go-project-layout-e5213cdcfaa2)

#### Q39. How can you compile main.go to an executable that will run on OSX arm64 ?

- [ ] Set GOOS to **arm64** and GOARCH to **darwin**.
- [ ] Set GOOS to **osx** and GOARCH to **arm64**.
- [ ] Set GOOS to **arm64** and GOARCH to **osx**.
- [x] Set GOOS to **darwin** and GOARCH to **arm64**.

[documentation](https://pkg.go.dev/cmd/go#hdr-Build_constraints)

#### Q40. What is the correct syntax to start a goroutine that will `print Hello Gopher!`?

- [ ] `go(fmt.Println("Hello Gopher!"))`
- [ ] `go func() { fmt.Println("Hello Gopher!") }`
- [x] `go fmt.Println("Hello Gopher!")`
- [ ] `Go fmt.Println("Hello Gopher!")`

[Example of start a goroutine](https://go.dev/play/p/KGgnAWpZMrS)

#### Q41. If you iterate over a map in a for range loop, in which order will the key:value pairs be accessed?

- [x] in pseudo-random order that cannot be predicted
- [ ] in reverse order of how they were added, last in first out
- [ ] sorted by key in ascending order
- [ ] in the order they were added, first in first out

[Reference](https://go.dev/ref/spec#:~:text=The%20iteration%20order%20over%20maps%20is%20not%20specified)

#### Q42. What is an idiomatic way to customize the representation of a custom struct in a formatted string?

- [ ] There is no customizing the string representation of a type.
- [ ] Build it in pieces each time by calling individual fields.
- [x] Implement a method `String()` string
- [ ] Create a wrapper function that accepts your type and outputs a string.

[Reference](https://go.dev/doc/effective_go#printing)

#### Q43. How can you avoid a goroutine leak in this code?

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

- [ ] Use a sync.WaitGroup.
- [x] Make ch a buffered channel.
- [ ] Add a default case to the select.
- [ ] Use runtime.SetFinalizer.

[Reference](https://www.ardanlabs.com/blog/2018/11/goroutine-leaks-the-forgotten-sender.html)

Relevant excerpt from the article:

> _The simplest way to resolve this leak is to change the channel from an unbuffered channel to a buffered channel with a capacity of 1. Now in the timeout case, after the receiver has moved on, the Goroutine will complete its send by placing the \*User value in the channel then it will return._

#### 44. What will this code print?

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

#### 45. Given the definition of worker below, what is the right syntax to start a start a goroutine that will call worker and send the result to a channel named ch?

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

[Go Playground example](https://go.dev/play/p/96j7tuQKF50)

#### Q46. In this code, which names are exported?

```go
package os

type FilePermission int
type userID int
```

- [x] FilePermission
- [ ] none of these answers
- [ ] FilePermission and userID
- [ ] userID

[Reference 1](https://www.ardanlabs.com/blog/2018/11/goroutine-leaks-the-forgotten-sender.html)  
[Reference 2](https://go.dev/tour/basics/3)

#### Q47. Which of the following is correct about structures in Go?

- [ ] Structure is another user defined data type available in Go programming, which allows you to combine data items of different kinds.
- [ ] Structures are used to represent a record
- [ ] To define a structure, you must use type and struct statements.
- [x] All of the above

#### Q48. What does the built-in `generate` command of the Go compiler do?

- [ ] It provides subcommands `sql`, `json`, `yaml`, and switches `--schema` and `--objects` to generate relevant code.
- [ ] It looks for files with names that end with `_generate.go`, and then compiles and runs each of these files individually.
- [x] It scans the projects source code looking for `//go:generate` comments, and for each such comment runs the terminal command it specifies.
- [ ] It has subcommands `mocks` and `tests` to generate relevant `.go` source files.

[Generate Go files by processing source](https://pkg.go.dev/cmd/go#hdr-Generate_Go_files_by_processing_source)

#### Q49. Using the time package, how can you get the time 90 minutes from now?

- [ ] `time.Now().Add(90)`
- [ ] `time.Now() + (90 * time.Minute)`
- [ ] `time.Now() + 90`
- [x] `time.Now().Add(90 * time.Minute)`

[func (Time) Add example](https://pkg.go.dev/time#example-Time.Add)

#### Q50. A program uses a channel to print five integers inside a goroutine while feeding the channel with integers from the main routine, but it doesn't work as is. What do you need to change to make it work?

- [ ] Add a `close(ch)` immediately after `wg.Wait()`.
- [x] Add a second parameter to `make(chan, int)`, e.g. `make(chan int, 5)`.
- [ ] Remove the use of unnecessary `WaitGroup` calls, e.g. all lines that start with `wg`.
- [ ] Move the 7-line goroutine immediately after `wg.Add(1)` to a line immediately before `wg.Wait()`.

[Reference](https://www.ardanlabs.com/blog/2018/11/goroutine-leaks-the-forgotten-sender.html)

Relevant excerpt from the article:

> _The simplest way to resolve this leak is to change the channel from an unbuffered channel to a buffered channel with a capacity of 1. Now in the timeout case, after the receiver has moved on, the Goroutine will complete its send by placing the \*User value in the channel then it will return._

#### Q51. After importing `encoding/json`, how will you access the `Marshal` function?

- [ ] `encoding.json.Marshal`
- [ ] `encoding/json.Marshal`
- [ ] `Marshal`
- [x] `json.Marshal`

[encoding/json#Marshal example](https://pkg.go.dev/encoding/json#example-Marshal)

#### Q52. What are the two missing segments of code that would complete the use of `context.Context` to implement a three-second timeout for this HTTP client making a GET request?

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

- [ ] `#1: ctx.SetTimeout(3*time.Second) #2: req.AttachContext(ctx)`
- [x] `#1: ctx, cancel = context.WithTimeout(ctx, 3*time.Second); defer cancel() #2: req = req.WithContext(ctx)`
- [ ] `#1: ctx, cancel = context.WithTimeout(ctx, 3*time.Second); defer cancel() #2: req.AttachContext(ctx)`
- [ ] `#1: ctx.SetTimeout(3*time.Second) #2: req = req.WithContext(ctx)`

1. [context#WithTimeout](https://pkg.go.dev/context#WithTimeout)
2. [net/http#Request.WithContext](https://pkg.go.dev/net/http#Request.WithContext)
