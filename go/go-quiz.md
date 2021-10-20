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

Explanation: most [variables](https://golangbyexample.com/variables-in-golang-complete-guide/) in Go has initial values. For string type it's an empty string.

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
- [x] Make `X` and `Y` exported (upercase)
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
