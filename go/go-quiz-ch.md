## Go（编程语言）

#### Q1. 让两个函数属于相同类型需要满足什么条件？

- [x] 它们应当具有相同的签名，包括参数类型和返回类型。
- [ ] 它们应当具有相同的参数类型，但可以返回不同类型。
- [ ] 所有函数都应当是相同的类型。
- [ ] 函数不应当是 first-class 类型。

[Go（Golang）中的用户自定义函数类型](https://golangbyexample.com/user-defined-function-type-go/)

#### Q2. 将一个 UTF-8 编码的字符串传给 `len()` 函数会返回什么？

- [ ] 字符数
- [x] 字节数
- [ ] 它不接受字符串类型。
- [ ] 码点（code points）数量

[Go（Golang）中字符串长度](https://golangbyexample.com/length-of-string-golang/).

#### Q3. 下列哪一个不是 Go 中有效的循环结构？

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

**Explanation:** Go 只有 `for` 循环。

#### Q4. 你如何把数字 3 添加到右侧？

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

**Explanation:** 在 Go 中切片是不可变的，因此调用 `append` 不会修改原切片。

#### Q5. `Read` 的值是多少？

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
- [ ] 一个随机值

[Go（Golang）中的 IOTA](https://golangbyexample.com/iota-in-golang/)

#### Q6. 下列哪个是 Go 中唯一有效的 import 语句？

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

[GoLang 中的 Import](https://golangdocs.com/import-in-golang)

#### Q7. 如果你尝试编译并运行下面这个 Go 程序，会发生什么？

```go
package main
var GlobalFlag string
func main() {
  print("["+GlobalFlag+"]")
}
```

- [ ] 不会编译通过，因为 `GlobalFlag` 从未被初始化。
- [x] 会编译并打印 `[]`。
- [ ] 会编译并什么也不打印，因为 `"[" +nil+"]"` 也是 `nil`。
- [ ] 会编译但随后 panic，因为 `GlobalFlag` 从未被初始化。

1. Go 中[变量](https://golangbyexample.com/variables-in-golang-complete-guide/)有初始值。对字符串类型来说，其初始值是空字符串。
2. [Go Playground](https://play.golang.org/p/TaRIzuD-nxC)

#### Q8. 如果变量 `myVar` 在模块 `myModule` 中的包 `myPackage` 的某个文件里、所有函数之外声明，那么它可以从哪里被访问？

- [x] 在 `myPackage` 内的任何地方都可以访问，`myModule` 的其它部分不行。
- [ ] 任何导入了 `myModule` 的应用都可以访问。
- [ ] 可以从 `myModule` 的任意位置访问。
- [ ] `myModule` 中其他包只要导入了 `myPackage` 就可以访问。

**Explanation**: 若要让该变量在 `myPackage` 之外可用，请将名称改为 `MyVar`。
另请参阅 Go 之旅中的[导出名称](https://tour.golang.org/basics/3)示例。

#### Q9. 你如何让 `go test` 打印它正在运行的测试？

- [ ] `go test`
- [ ] `go test -x`
- [ ] `go test --verbose`
- [x] `go test -v`

[test 包](https://pkg.go.dev/cmd/go/internal/test)

#### Q10. 这段代码打印了 `{0, 0}`。你如何修复它？

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

- [ ] 使用 `json.Decoder`
- [ ] 传入 `data` 的指针
- [x] 让 `X` 和 `Y` 导出（大写）
- [ ] 使用字段标签（field tags）

1. [如何在 Golang 中解析 JSON？](https://www.geeksforgeeks.org/how-to-parse-json-in-golang/)
2. [Go Playground](https://play.golang.org/p/RdL6y3Zv8ke)

#### Q11. 当 `sync.Mutex` 处于加锁状态时，它会阻塞什么？

- [ ] 所有 goroutine
- [ ] 对该 `Mutex` 的任何其它加锁调用
- [x] 对其所保护变量的任何读或写
- [ ] 对其所保护变量的任何写操作

1. [GoLang 中的 Mutex](https://golangdocs.com/mutex-in-golang)，`sync.Mutex` 会加锁，使得同一时间只有一个 goroutine 可以访问被保护的变量。
2. [sync.Mutex](https://go.dev/tour/concurrency/9)

#### Q12. 以惯用方式暂停当前作用域的执行，直到任意数量的 goroutine 返回，应当使用什么？

- [ ] 传给每个 goroutine 一个 `int` 和 `Mutex`，并在它们返回时计数。
- [ ] 在 `select` 语句上循环。
- [ ] 休眠一个足够安全的时间。
- [x] `sync.WaitGroup`

**Explanation:** 这正是 `sync.WaitGroup` 的用途——[在 Golang 中使用 sync.WaitGroup](https://nanxiao.me/en/use-sync-waitgroup-in-golang/)

#### Q13. 在 `select` 语句中使用 `time.After` 的副作用是什么？

- [ ] 它会阻塞其他通道。
- [ ] 它被设计为在 `select` 语句中使用且没有副作用。
- [ ] 它会阻塞 `select` 语句直到时间过去。
- [x] 该 goroutine 在时间到达之前不会结束。

> 注意：它不会阻塞 `select`，也不会阻塞其他通道。

1. [Golang 中的 time.After() 函数及示例](https://www.geeksforgeeks.org/time-after-function-in-golang-with-examples/)
2. [如何在 Golang 中使用 'time.After' 和 'default'？](https://stackoverflow.com/questions/39212333/how-can-i-use-time-after-and-default-in-golang)
3. [Go Playground 示例](https://go.dev/play/p/WojTrG1ywRK)

#### Q14. `select` 语句用于什么？

- [ ] 并发执行一个函数
- [ ] 基于变量的类型执行不同的分支
- [ ] 基于变量的值执行不同的分支
- [x] 基于哪个通道先返回来执行不同的分支

[GoLang 中的 Select 语句](https://golangdocs.com/select-statement-in-golang)

#### Q15. 按照 Go 文档标准，你应该如何为下面的函数编写文档？

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

**Explanation:** 文档注释应当以函数名开头。

[Go 中的注释](https://exercism.org/tracks/go/concepts/comments)

#### Q16. 为了能编译 `i := myVal.(int)`，`myVal` 的类型限制是什么？

- [ ] `myVal` 必须是整数类型，例如 `int`、`int64`、`int32` 等。
- [ ] `myVal` 必须能够被断言为 `int`。
- [x] `myVal` 必须是一个接口（interface）。
- [ ] `myVal` 必须是数值类型，例如 `float64` 或 `int64`。

**Explanation**: 这种使用 `.(type)` 的类型断言只用于接口。

1. [示例](https://tutorialedge.net/golang/snippets/type-casting-interface-to-string-go/)
2. [原始类型的类型转换方式不同](https://golangdocs.com/type-casting-in-golang)
3. [Go Playground](https://play.golang.org/p/TXF_JBvThp6)
4. [类型断言](https://go.dev/tour/methods/15)

#### Q17. 什么是通道（channel）？

- [ ] 一个全局变量
- [x] 在 goroutine 之间传递值的媒介
- [ ] 一个动态数组
- [ ] 用于并发编程的轻量级线程

[Channels](https://tour.golang.org/concurrency/2)

#### Q18. 如何让某个文件仅在 Windows 上编译？

- [ ] 检查 runtime.GOOS。
- [ ] 在文件的任意位置添加 `// +build windows` 注释。
- [ ] 给文件名加上 `_` 前缀。
- [x] 在文件顶部添加 `// +build windows` 注释。

1. [如何使用 go build 工具进行条件编译（2013 年 10 月）](https://dave.cheney.net/2013/10/12/how-to-use-conditional-compilation-with-the-go-build-tool)
2. [go 命令的构建约束](https://pkg.go.dev/cmd/go#hdr-Build_constraints)

> `//go:build windows`
> “Go 1.16 及更早版本使用不同的构建约束语法，前缀为 `// +build`。当遇到旧语法时，gofmt 会添加等效的 `//go:build` 约束。”

#### Q19. 将如下内容作为 HTTP POST 请求的 body 传递时，正确的方式是什么？

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
2. [http.Post Golang 示例](https://dev.to/ramu_mangalarapu/httppost-golang-example-5jp)

#### Q20. 对于只有一个方法且签名为 `Save() error` 的接口，惯用的命名是什么？

- [ ] Saveable
- [ ] SaveInterface
- [ ] ISave
- [x] Saver

[Effective Go，接口命名](https://golang.org/doc/effective_go#interface-names)

#### Q21. 一个 `switch` 语句**\_**它自己的词法块（lexical block）。每个 `case` 语句**\_**一个额外的词法块

- [ ] 不创建；创建
- [ ] 不创建；不创建
- [x] 创建；创建
- [ ] 创建；不创建

[Go 语言核心技术（上卷）1.5—作用域](https://topic.alibabacloud.com/a/go-language-core-technology-volume-one-15-font-colorredscopefont_1_38_30923325.html)

相关文章摘录：

> 第二个 if 语句嵌套在第一个 if 语句内部，因此在第一个 if 中声明的变量对第二个 if 可见。`switch` 中也有类似规则：除了条件的词法块外，每个 `case` 还拥有自己的词法块。

#### Q22. JSON 的 `Unmarshal` 函数在大小写敏感性上的默认行为是什么？

- [x] 默认不区分大小写，但可以被覆盖。
- [ ] 字段匹配时区分大小写。
- [ ] 字段匹配时不区分大小写。
- [ ] 默认区分大小写，但可以被覆盖。

[encoding/json#Unmarshal](https://pkg.go.dev/encoding/json#Unmarshal)

相关文章摘录：

> 将 JSON 解组到结构体时，`Unmarshal` 会将传入对象的键与 `Marshal` 使用的键（结构体字段名或其标签）进行匹配，更倾向于精确匹配，但也接受大小写不敏感的匹配。默认情况下，没有对应结构体字段的对象键将被忽略（另见 `Decoder.DisallowUnknownFields`）。

#### Q23. `time` 包中 `Time.Sub()` 与 `Time.Add()` 的区别是什么？

- [ ] `Time.Add()` 用于做加法，而 `Time.Sub()` 用于嵌套时间戳。
- [ ] `Time.Add()` 总是返回更晚的时间，而 `time.Sub` 总是返回更早的时间。
- [ ] 它们是相反操作。`Time.Add(x)` 等价于 `Time.Sub(-x)`。
- [x] `Time.Add()` 接受 `Duration` 参数并返回 `Time`，而 `Time.Sub()` 接受 `Time` 参数并返回 `Duration`。

1. [time#Time.Add](https://pkg.go.dev/time#Time.Add)
2. [time#Time.Sub](https://pkg.go.dev/time#Time.Sub)

#### Q24. 在一个结构体里使用多个字段标签（field tags）有什么风险？

- [ ] 每个字段都必须拥有所有标签才能编译。
- [x] 它会让你应用的不同层强耦合。
- [ ] 第一个之后的任何标签都会被忽略。
- [ ] 缺失的标签会在运行时触发 panic。

1. [示例代码 / b29r0fUD1cp](https://play.golang.org/p/b29r0fUD1cp)
2. [如何在 Go 中使用 Struct Tags](https://www.digitalocean.com/community/tutorials/how-to-use-struct-tags-in-go)

#### Q25. 内置的 `recover` 方法在什么地方有用？

- [ ] 在 `main` 函数里
- [ ] 在可能 panic 的代码行之后立即调用
- [x] 在延迟执行的函数（deferred function）内部
- [ ] 在可能 panic 的函数开头

[Go（Golang）中 Recover 函数示例](https://golangbot.com/panic-and-recover/#recoveringfromapanic)

相关文章摘录：

> 只有在延迟执行的函数内部调用 `recover` 才有用。在延迟函数内部执行 `recover` 会通过恢复正常执行来停止正在进行的 panic 序列，并获取传给 `panic` 的错误信息。如果在延迟函数之外调用 `recover`，它不会停止 panic 序列。

#### Q26. 下列哪个选项不会把输出发送到标准错误（stderr）？

- [ ] `println(message)`
- [ ] `log.New(os.Stderr, "", 0).Println(message)`
- [x] `fmt.Errorf("%s\n", message)`
- [ ] `fmt.Fprintln(os.Stderr, message)`

1. [func println](https://pkg.go.dev/builtin#println)：将结果写入标准错误。
2. [func New](https://pkg.go.dev/log#New)：`func New(out io.Writer, prefix string, flag int) *Logger`；参数 `out` 用于设置日志数据的输出目标。
3. [func Errorf](https://pkg.go.dev/fmt#Errorf)：`Errorf` 根据格式化说明符进行格式化，并将字符串作为值返回。
4. [func Fprintln](https://pkg.go.dev/fmt#Fprintln)：`func Fprintln(w io.Writer, a ...any) (n int, err error)`；`Fprintln` 使用操作数的默认格式并写入到 `w`。

#### Q27. 如何让 Go 从不同的位置导入某个包？

- [ ] 使用代理（proxy）。
- [ ] 改变 import 路径。
- [x] 在 `go.mod` 中使用 `replace` 指令。
- [ ] 使用替换目录。

1. [从另一个模块调用你的代码](https://go.dev/doc/tutorial/call-module-code)：第 5 章，`go mod edit -replace example.com/greetings=../greetings`。
2. [`go.mod` 的 replace 指令](https://go.dev/doc/modules/gomod-ref#replace)

#### Q28. 如果你的当前工作目录位于项目顶层，哪条命令会运行其所有测试包？

- [ ] `go test all`
- [ ] `go run --all`
- [ ] `go test .`
- [x] `go test ./...`

1. [Go（Golang）中的 testing 包](https://pkg.go.dev/testing)
2. [Go（Golang）中的 cmd 包](https://pkg.go.dev/cmd/go)

相关文章摘录：

> 也允许使用相对模式，例如 `go test ./...` 来测试所有子目录。

#### Q29. 你可以在字符串中放入哪些编码？

- [ ] 任意编码，它接受任意字节
- [ ] 任意 Unicode 格式
- [ ] UTF-8 或 ASCII
- [x] UTF-8

1. [Go 中的字符串、字节、rune 和字符](https://go.dev/blog/strings)

相关文章摘录：

> 简而言之，Go 源码是 UTF-8，因此字符串字面量的源码是 UTF-8 文本。

2. [Go（Golang）中的编码示例](https://pkg.go.dev/golang.org/x/text/encoding)

相关文章摘录：

> `encoding` 包定义了字符编码（如 Shift JIS 和 Windows 1252）的接口，可与 UTF-8 相互转换。

#### Q30. 在 `t.Run` 内部，`t.Fatal` 的行为有什么不同？

- [ ] 没有区别。
- [ ] `t.Fatal` 不会导致测试工具崩溃，从而保留输出信息。
- [x] `t.Fatal` 会停止该子测试的执行，并继续运行其他测试用例。
- [ ] `t.Fatal` 会停止所有测试，并包含关于失败子测试的额外信息。

1. [参考](https://go.dev/play/p/gtne3iRL9AX)
2. [Go 中的 testing 包](https://pkg.go.dev/testing)，相关文章摘录：

> `Fatal` 等价于先 `Log` 再 `FailNow`。
> `Log` 使用默认格式化参数记录文本到错误日志。
> `FailNow` 将函数标记为失败，并通过调用 `runtime.Goexit` 停止其执行（随后会运行当前 goroutine 中所有延迟调用）。执行将继续到下一个测试或基准。`FailNow` 必须在运行测试或基准函数的 goroutine 中调用，而不是在测试期间创建的其它 goroutine 中调用。调用 `FailNow` 不会停止那些其它 goroutine。
> `Run` 将 `f` 作为 `t` 的一个名为 `name` 的子测试运行。它在单独的 goroutine 中运行 `f` 并阻塞直到 `f` 返回或调用 `t.Parallel` 成为并行测试。`Run` 会报告 `f` 是否成功（或至少在调用 `t.Parallel` 之前没有失败）。
> 可以从多个 goroutine 同时调用 `Run`，但所有这些调用必须在外层测试函数返回之前返回。

#### Q31. `log.Fatal` 做了什么？

- [ ] 它会触发 `panic`。
- [ ] 它会打印日志然后触发 `panic`。
- [x] 它会打印日志然后安全地退出程序。
- [ ] 它会退出程序。

[Go（Golang）中 func Fatal 示例](https://pkg.go.dev/log#Fatal)

相关文章摘录：

> `Fatal` 等价于先 `Print()`，然后调用 `os.Exit(1)`。

#### Q32. 哪一个是有效的 Go 时间格式字面量？

- [x] "2006-01-02"
- [ ] "YYYY-mm-dd"
- [ ] "y-mo-d"
- [ ] "year-month-day"

[Go 中的时间常量](https://pkg.go.dev/time#pkg-constants)

相关文章摘录：

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

#### Q33. 你应该如何记录一个错误（`err`）？

- [ ] `log.Error(err)`
- [x] `log.Printf("error: %v", err)`
- [ ] `log.Printf(log.ERROR, err)`
- [ ] `log.Print("error: %v", err)`

**Explanation:** 在 [Go 的 log 包](https://pkg.go.dev/log) 中既没有 `log.ERROR` 也没有 `log.Error()`；`log.Print()` 的参数处理方式类似 `fmt.Print()`；`log.Printf()` 的参数处理方式类似 `fmt.Printf()`。

#### Q34. `go test` 命令会把哪些文件名识别为测试文件？

- [ ] 任何以 `test` 开头的文件
- [ ] 任何包含 `test` 这个词的文件
- [ ] 只有根目录下以 `_test.go` 结尾的文件
- [x] 任何以 `_test.go` 结尾的文件

1. [go 命令中的测试包](https://pkg.go.dev/cmd/go#hdr-Test_packages)：'Go test' 会重新编译每个包以及任何名称匹配“\*\_test.go”模式的文件。
2. [在 Go 中添加测试](https://go.dev/doc/tutorial/add-a-test)

#### Q35. 这段代码的输出是什么？

```go
ch := make(chan int)
ch <- 7
val := <-ch
fmt.Println(val)
```

- [ ] 0
- [x] 它会死锁（deadlock）
- [ ] 它不会编译
- [ ] 2.718

[Go Playground 分享](https://go.dev/play/p/SQlfg8YSEOz)，输出：

```text
fatal error: all goroutines are asleep - deadlock!

goroutine 1 [chan send]:
main.main()
 /tmp/sandbox2282523250/prog.go:7 +0x37

Program exited.
```

#### Q36. 这个程序的输出是什么？

```go
ch := make(chan int)
close(ch)
val := <-ch
fmt.Println(val)
```

- [ ] 它会死锁
- [ ] 它会 panic
- [x] 0
- [ ] NaN

1. [Go 语言规范 “接收操作符”](https://go.dev/ref/spec#Receive_operator)，相关文章摘录：

   > 从已关闭的通道进行接收的操作总能立即继续执行，在接收了所有已发送的值之后，会得到该元素类型的零值。

2. [Go Playground 分享](https://go.dev/play/p/DjXq9wzJm5M)，输出：

```text
0

Program exited.
```

#### Q37. 这段代码会打印什么？

```go
var stocks map[string]float64 // stock -> price
price := stocks["MSFT"]
fmt.Printf("%f\n", price)
```

- [ ] 0
- [x] 0.000000
- [ ] 代码会 panic
- [ ] NaN

[Go Playground 分享](https://go.dev/play/p/CjdHskV1xq1)，输出：

```text
0.000000

Program exited.
```

#### Q38. 在项目中拥有多个可执行文件的常见方式是什么？

- [x] 使用 `cmd` 目录，并在其中为每个可执行文件创建一个子目录。
- [ ] 注释掉 `main`。
- [ ] 使用构建标签（build tags）。
- [ ] 使用 `pkg` 目录，并在其中为每个可执行文件创建一个子目录。

1. [Stack Overflow](https://stackoverflow.com/questions/9985559/organizing-a-multiple-file-go-project/51942843#51942843)
2. [Medium](https://medium.com/@benbjohnson/structuring-applications-in-go-3b04be4ff091)
3. [Medium](https://medium.com/golang-learn/go-project-layout-e5213cdcfaa2)

#### Q39. 如何将 `main.go` 编译为可在 OSX arm64 上运行的可执行文件？

- [ ] 将 GOOS 设为 arm64，将 GOARCH 设为 darwin。
- [ ] 将 GOOS 设为 osx，将 GOARCH 设为 arm64。
- [ ] 将 GOOS 设为 arm64，将 GOARCH 设为 osx。
- [x] 将 GOOS 设为 darwin，将 GOARCH 设为 arm64。

[文档](https://pkg.go.dev/cmd/go#hdr-Build_constraints)

#### Q40. 启动一个 goroutine 来 `print Hello Gopher!` 的正确语法是？

- [ ] `go(fmt.Println("Hello Gopher!"))`
- [ ] `go func() { fmt.Println("Hello Gopher!") }`
- [x] `go fmt.Println("Hello Gopher!")`
- [ ] `Go fmt.Println("Hello Gopher!")`

[启动 goroutine 的示例](https://go.dev/play/p/KGgnAWpZMrS)

#### Q41. 如果你在 `for range` 循环中迭代一个 map，键值对会以什么顺序访问？

- [x] 伪随机的、不可预测的顺序
- [ ] 按添加的逆序，后进先出
- [ ] 按键的升序排序
- [ ] 按添加顺序，先进先出

[参考](https://go.dev/ref/spec#:~:text=The%20iteration%20order%20over%20maps%20is%20not%20specified)

#### Q42. 以惯用的方式，自定义一个自定义结构体在格式化字符串中的表示应如何做？

- [ ] 无法自定义类型的字符串表示。
- [ ] 每次通过逐个字段拼接来构造。
- [x] 实现一个方法 `String() string`
- [ ] 创建一个包装函数，接受你的类型并输出字符串。

[参考](https://go.dev/doc/effective_go#printing)

#### Q43. 你如何避免这段代码中的 goroutine 泄漏？

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

- [ ] 使用 `sync.WaitGroup`。
- [x] 将 `ch` 设为带缓冲通道。
- [ ] 给 `select` 添加一个 `default` 分支。
- [ ] 使用 `runtime.SetFinalizer`。

[参考](https://www.ardanlabs.com/blog/2018/11/goroutine-leaks-the-forgotten-sender.html)

相关文章摘录：

> 解决该泄漏的最简单方式是把通道从无缓冲改为容量为 1 的带缓冲通道。这样在超时场景下，接收方离开后，goroutine 仍能把 `*User` 值放入通道，然后返回。

#### 44. 这段代码会打印什么？

```go
var i int8 = 120
i += 10
fmt.Println(i)
```

- [x] -126
- [ ] 0
- [ ] NaN
- [ ] 130

[Go Playground 示例](https://go.dev/play/p/T31_JuFioaC)，输出：

```text
-126

Program exited.
```

#### 45. 给定下面 `worker` 的定义，启动一个 goroutine 调用 `worker` 并将结果发送到名为 `ch` 的通道，正确的语法是？

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

[Go Playground 示例](https://go.dev/play/p/96j7tuQKF50)

#### Q46. 在这段代码中，哪些名称是导出的？

```go
package os

type FilePermission int
type userID int
```

- [x] FilePermission
- [ ] 这些选项都不是
- [ ] FilePermission 和 userID
- [ ] userID

[参考 1](https://www.ardanlabs.com/blog/2018/11/goroutine-leaks-the-forgotten-sender.html)
[参考 2](https://go.dev/tour/basics/3)

#### Q47. 关于 Go 中的结构体，下列哪项是正确的？

- [ ] 结构体是 Go 中另一种用户自定义数据类型，允许你组合不同类型的数据项。
- [ ] 结构体用于表示一条记录。
- [ ] 定义结构体必须使用 `type` 和 `struct` 语句。
- [x] 以上全部正确

#### Q48. Go 编译器内置的 `generate` 命令做什么？

- [ ] 提供 `sql`、`json`、`yaml` 子命令以及 `--schema`、`--objects` 开关来生成相关代码。
- [ ] 查找以 `_generate.go` 结尾的文件，然后分别编译并运行这些文件。
- [x] 扫描项目源码，查找 `//go:generate` 注释，并为每个注释运行其指定的终端命令。
- [ ] 提供 `mocks` 和 `tests` 子命令来生成相应的 `.go` 源文件。

[通过处理源码生成 Go 文件](https://pkg.go.dev/cmd/go#hdr-Generate_Go_files_by_processing_source)

#### Q49. 使用 `time` 包，如何获得从现在起 90 分钟后的时间？

- [ ] `time.Now().Add(90)`
- [ ] `time.Now() + (90 * time.Minute)`
- [ ] `time.Now() + 90`
- [x] `time.Now().Add(90 * time.Minute)`

[func (Time) Add 示例](https://pkg.go.dev/time#example-Time.Add)

#### Q50. 一个程序使用通道在 goroutine 中打印五个整数，同时在主协程中向通道喂入整数，但按现状它不能正常工作。你需要修改什么才能让它工作？

- [ ] 在 `wg.Wait()` 之后立刻添加 `close(ch)`。
- [x] 给 `make(chan, int)` 添加第二个参数，例如 `make(chan int, 5)`。
- [ ] 移除不必要的 `WaitGroup` 调用，例如所有以 `wg` 开头的行。
- [ ] 将那段 7 行的 goroutine 从 `wg.Add(1)` 之后移动到 `wg.Wait()` 之前。

[参考](https://www.ardanlabs.com/blog/2018/11/goroutine-leaks-the-forgotten-sender.html)

相关文章摘录：

> 解决该泄漏的最简单方式是把通道从无缓冲改为容量为 1 的带缓冲通道。这样在超时场景下，接收方离开后，goroutine 仍能把 `*User` 值放入通道，然后返回。

#### Q51. 在导入了 `encoding/json` 之后，你将如何访问 `Marshal` 函数？

- [ ] `encoding.json.Marshal`
- [ ] `encoding/json.Marshal`
- [ ] `Marshal`
- [x] `json.Marshal`

[encoding/json#Marshal 示例](https://pkg.go.dev/encoding/json#example-Marshal)

#### Q52. 为了用 `context.Context` 为这个发起 GET 请求的 HTTP 客户端实现 3 秒超时，缺失的两段代码是什么？

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

        // #1: <=== 这里应当写什么？

        req, _ := http.NewRequest(http.MethodGet,
                "https://linkedin.com",
                nil)

        // #2: <=== 这里应当写什么？

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

#### Q53. 如果你在同一个 .go 文件中定义了名为 `Client` 的结构体，如何导出一个带有默认值的变量，使其可以被其他包访问？

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

#### Q54. 该程序输出 `{Master Chief Spartan Protagonist Halo}`。怎样让它输出 `Master Chief - a Spartan - is the Protagonist of Halo`？

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
  // 替换
  // fmt.Println(mc)
  // 为：

  fmt.Printf("(?P<Name>) - a (?P<Class>) - is the (?P<Role>) of (?P<Game>)", mc)
  ```

- [ ] B

  ```go
  // 替换
  // fmt.Println(mc)
  // 为：
  fmt.Println(mc, func(c Character) string {
        return c. Name + " - a " + c.Class + " - is the " + c.Role + " of " + c.Game
  })
  ```

- [x] C

  ```go
  // 在包 `main` 中添加：

  func (c Character) String() string {
        return fmt.Sprintf("%s - a %s - is the %s of %s", c.Name, c.Class, c.Role,c.Game)
  }
  ```

- [ ] D

  ```go
   // 在包 `main` 中添加：

  func (c Character) OnPrint() {
        fmt.Println("{{c.Name}} - a {{c.Class}} - is the {{c.Role}} of {{c.Game}}")
  }
  ```

1. [fmt#Stringer](https://pkg.go.dev/fmt#Stringer)

#### Q55. 你会如何为 `Clients` 实现一个可用的 `Append()` 方法？

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

#### Q56. 你如何从被调用函数抛出的 `panic()` 中恢复，同时不让程序失败？假设你的答案将在发生 `panic` 的同一作用域内运行。

- [ ] 用返回类型为 `panic` 的匿名函数包裹该函数调用，并在其后加 `()` 调用它，然后内省返回的 `panic` 实例来处理错误。

- [ ] 使用 `try{ ... }` 包裹调用语句，并在 `catch{ ... }` 中处理错误。

- [x] 在发生错误的函数调用之前使用 `defer func { ... }()`，并在匿名函数内部处理该 `panic`。

- [ ] 在函数调用前加前缀 `@`，强制把 `panic` 作为 `error` 返回，然后像处理普通 `error` 一样处理。

#### Q57. 这段代码会打印什么？

```go
var n int
fmt.Println (n)
```

- [x] 0
- [ ] nil
- [ ] 一个随机值
- [ ] 1

> 因为在 Go 中，当变量被声明但未显式初始化时，会被赋予基于其类型的默认[零值](https://go.dev/tour/basics/12)。对于整数 `n` 来说，零值是 0。

#### Q58. 在创建格式化字符串时，如果希望调用自定义类型的 `String() string` 方法，应使用哪个动词？

- [x] %s
- [ ] %b
- [ ] %v
- [ ] %string

> 在 Go 中，`%s` 用于格式化字符串。当用于定义了 `String()` 方法的自定义类型时，会自动调用 `String()`，其返回值将用于该格式化字符串。

#### Q59. 调用 `time.Now().Format(layout)` 时，下面哪个不是合法的 `layout` 值？

- [ ] time.REC3339
- [x] "1970-01-01"
- [ ] "Jan 2nd 2006"
- [ ] time.Kitchen

[time#Time.Format](https://pkg.go.dev/time#Time.Format)

根据文档，值 1 和 01 代表当前月份。

```text
each layout string is a representation of the time stamp,
	Jan 2 15:04:05 2006 MST
An easy way to remember this value is that it holds, when presented in this order, the values (lined up with the elements above):
	  1 2  3  4  5    6  -7
```

#### Q60. 你如何向 Go 编译器表明结构体 `Namespace` 必须实现接口 `JSONConverter`？假设答案写在声明 `Namespace` 的同一个包中。

- [ ] var \_ JSONConverter = nil. (\*Namespace)
- [x] var \_ JSONConverter = (\*Namespace) (nil)
- [ ] type Namespace struct {
      implements JSONConverter
      // 其余结构体声明在此
      }
- [ ] type Namespace struct {
      JSONConverter
      // 其余结构体声明在此
      }

> 该语法创建一个类型为 `JSONConverter` 的变量 `_`，并将 `(*Namespace)(nil)` 赋给它。这实质上检查了 `Namespace` 是否满足 `JSONConverter` 接口。

#### Q61. 关于类型与接口，下列哪一项是错误的？

- [ ] 方法签名由方法名以及其声明的参数类型与返回值类型构成。
- [x] 结构体必须显式使用 `implements` 关键字声明其实例可以用于任何被该接口类型化的变量、参数或返回值位置。
- [ ] 接口声明了若干方法及其签名，某个类型必须实现这些方法才能兼容该接口类型的值。
- [ ] 变量、参数和返回值必须被“类型化”为以下之一：1）内置类型，2）类型别名，3）派生类型，4）复合类型，或 5）接口。

> 在 Go 中，只要一个类型实现了接口的所有方法，它就自动满足该接口；无需显式声明“实现了某接口”。

#### Q62. 补全该程序以生成指定的输出，假设 SQL 表如下所示。

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

#### Q63. 填空题

1. Go 中的测试文件必须**\_**。
2. 单个测试由**\_**标识。
3. 你可以通过**\_\_**来运行子测试。
4. 通过**\_**可以记录错误并标记测试失败。

- [ ] 存放在该包的 `/test/` 子目录中
      <br/>接受 `testing.Tester` 参数的函数
      <br/>编写名称匹配 `^Subtest` 的函数
      <br/>调用 `testing.AssertionFailed`

- [x] 以 `_test.go` 结尾
      <br/>函数名匹配 `^Test[A-Z]`
      <br/>调用 `t.Run()`
      <br/>调用 `t.Errorf()`

- [ ] 以 `test_` 开头
      <br/>函数匹配 `[a-z]Test$`
      <br/>调用 `testing.Subtest()`
      <br/>允许 `testing.Assert()` 断言失败

- [ ] 存放在项目根目录的 `/test/` 子目录
      <br/>接受 `testing.Test` 参数的函数
      <br/>传递闭包给 `testing.AddSubtest()`
      <br/>从函数返回一个 `error`

#### Q64. `rune` 是哪种类型的别名？

- [ ] char
- [ ] byte
- [x] int32
- [ ] string

1. [Go 中的字符串、字节、rune 和字符](https://go.dev/blog/strings)

相关文章摘录：

> Go 语言将 `rune` 定义为 `int32` 类型的别名，这样当整数值表示一个码点时，程序可以更清晰。

#### Q65. 何时可以使用 `:=` 语法给多个变量赋值？例如：

```go
x, err := myFunc()
```

- [x] 只要至少有一个变量尚未在该词法块中声明
- [ ] 任何时候都可以，它会覆盖已有变量
- [ ] 如果没有同名变量可访问
- [ ] 如果这些变量在该词法块中都不存在

1. [简短变量声明](https://go.dev/ref/spec#Short_variable_declarations)

#### Q66. 你如何在浏览器中查看 `cpu.pprof` 的 profiler 输出？

- [ ] `go pprof -to SVG cpu.prof`
- [x] `go tool pprof -http=:8080 cpu.pprof`
- [ ] `go tool pprof cpu.pprof`
- [ ] `go tool trace cpu.pprof`

#### Q67. 何时 `interface{}` 类型的变量会被判断为 `nil`？

- [x] 当它被赋予的动态类型的值为 `nil` 时。
- [ ] 当它被显式设为 `nil` 时。
- [ ] 当它尚未被赋予动态类型时。
- [ ] 它不可能为 `nil`。

#### Q68. 如果一个字符串变量已分配但未赋值，它持有什么值？

- [ ] nil
- [ ] undefined
- [ ] null
- [x] ""

> 若字符串变量已分配但未赋值，其默认值是空字符串 `""`。在 Go 中，未初始化的字符串变量会被自动赋予其类型的零值。

#### Q69. 用于停止程序继续执行的内置函数是哪个？

- [x] `panic`
- [ ] 没有这样的函数。
- [ ] `raiseException`
- [ ] `exit`

> 内置函数 `panic()` 会触发 panic，停止正常执行流程并开始“恐慌”过程；若不被恢复，程序将终止。

#### Q70. 输出将是什么？

```go
a,b := 1, 2
b,c:= 3, 4
fmt.Println(a, b, c)
```

- [x] 1 3 4
- [ ] 1 2 3
- [ ] 1 2 4
- [ ] 它不会编译。

[Go Playground 示例](https://go.dev/play/p/qUI50GNGWTq)

### Q71. 逻辑与条件的运算符是？

- [ ] -
- [ ] and
- [x] &&
- [ ] ||

### Q72. 在 Go 中，什么是匿名函数？

- [ ] 没有返回类型的函数。
- [ ] 没有参数的函数。
- [x] 没有名称的函数。
- [ ] 在另一个函数内声明的函数。

### Q73. 在 Go 中，用于声明匿名函数的关键字是？

- [ ] `func`
- [ ] `lambda`
- [x] `func()`
- [ ] `anonymous`

#### Q74. 使用匿名函数的主要优势是什么？

- [ ] 它们总是比具名函数性能更好。
- [ ] 它们可以有多个返回值。
- [x] 它们可以在使用处内联定义。
- [ ] 它们的语法比具名函数更简短。

Explanation: 它们可以在使用处内联定义，提供了更灵活的代码组织方式。

#### Q75. 在 Go 中，如何在声明匿名函数后立即调用它？

- [ ] `functionName(){}`
- [ ] `call functionName(){}`
- [x] `func(){}()`
- [ ] `execute func(){}`

[参考](https://stackoverflow.com/questions/6719089/javascript-anonymous-function-immediate-invocation-execution-expression-vs-dec)

#### Q76. Go 开发者可以为哪些类型定义方法？

- [x] 所有非内置的具名类型，例如 `type Example int`（但不是 `int`）、`type Example struct{...}`（但不是 `struct`）等。
- [ ] 仅限名为 `struct`、`map`、`slice` 的类型，例如 `type Example struct{…}`
- [ ] 仅限名为 `struct` 的类型，例如 `type Example struct{...}`
- [ ] 所有类型

> 方法可以为任何非内置的具名类型定义。通过 `type` 声明创建的新类型是具名类型，可以为其定义方法；但不能直接为内置类型（如 `int`、`string` 等）附加方法。[参考](https://go.dev/ref/spec#Method_declarations)
