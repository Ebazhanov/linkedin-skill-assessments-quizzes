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

**Explanation:** Go has only `for`-loops

#### Q4. How will you add the number 3 to the right side?

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
