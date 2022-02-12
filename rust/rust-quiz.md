## Rust (Programming Language)

#### Q1. Which type cast preserves the mathematical value in all cases?

- [ ] i64 as i32
- [ ] usize as u64
- [x] i32 as i64
- [ ] f64 as f32

#### Q2. What do the vertical bars represent here?

```rust
str::thread::spawn(|| {
    println!("LinkedIn");
});
```

- [x] a closure
- [ ] a thread
- [ ] a future
- [ ] a block

[reference](https://doc.rust-lang.org/book/ch13-01-closures.html#refactoring-with-closures-to-store-code)

#### Q3. Which choice is not a scalar data type?

- [ ] integer
- [ ] float
- [ ] boolean
- [x] tuple

#### Q4. **\_** cannot be destructured.

- [x] Traits
- [ ] Tuples
- [ ] Enums
- [ ] Structs

[reference](https://rust-lang.github.io/rfcs/2909-destructuring-assignment.html)

#### Q5. Which `cargo` command checks a program for error without creating a binary executable?

- [ ] cargo --version
- [ ] cargo init
- [ ] cargo build
- [x] cargo check

#### Q6. The term _box_ and related phrases such as _boxing a value_ are often used when relating to memory layout. What does _box_ refer to?

- [ ] It's creating a pointer on the heap that points to a value on the stack.
- [x] It's creating a pointer on the stack that points to a value on the heap.
- [ ] It's creating a memory guard around values to prevent illegal access.
- [ ] It's an abstraction that refers to ownership. "Boxed" values are clearly labelled.

#### Q7. What is an alternative way of writing `slice` that produces the same result?

```rust
...
let s = String::form("hello");
let slice = &s[0..2];
```

- [ ] let slice = &s[len + 2];
- [ ] let slice = &s[len - 2];
- [ ] let slice = &s.copy(0..2);
- [x] let slice = &s[..2];

#### Q8. Using the `?` operator at the end of an expression is equivalent to **\_**.

- [ ] a match pattern that branches into True or False
- [ ] calling ok_error()
- [ ] calling panic!()
- [x] a match pattern that may result an early return

#### Q9. Which is valid syntax for defining an array of i32 values?

- [ ] Array<i32>::with_capacity(10)
- [ ] [i32]
- [ ] Array<i32>::new(10)
- [x] [i32; 10]

#### Q10. What syntax is required to take a mutable reference to T, when used within a function argument?

```rust
fn increment(i: T) {
    // body elided
}
```

- [ ] \*mut T
- [ ] mut ref T
- [ ] mut &T
- [x] &mut T

#### Q11. The smart pointers Rc and Arc provide reference counting. What is the API for incrementing a reference count?

- [ ] .add()
- [ ] .incr()
- [x] .clone()
- [ ] .increment()

[reference](https://doc.rust-lang.org/book/ch15-04-rc.html)

#### Q12. What happens when an error occurs that is being handled by the question mark (?) operator?

- [ ] The error is reported and execution continues.
- [ ] An exception is raised. The effect(s) of the exception are defined by the error! macro.
- [ ] The program panics immediately.
- [x] Rust attempts to convert the error to the local function's error type and return it as Result::Err. If that fails, the program panics.

#### Q13. Which comment syntax is not legal?

- [ ] `/*`
- [x] `#`
- [ ] `//!`
- [ ] `//`

#### Q14. In matching patterns, values are ignored with \_.

- [ ] `.ignore()`
- [ ] `an underscore (_)`
- [x] ..
- [ ] skip

#### Q15. Defining a \_ requires a lifetime parameter.

- [ ] function that ends the lifetime of one of its arguments
- [x] struct that contains a reference to a value
- [ ] function with a generic argument
- [ ] struct that contains a reference to a boxed value

[Rust book reference](https://doc.rust-lang.org/book/ch10-03-lifetime-syntax.html#lifetime-annotations-in-struct-definitions)

#### Q16. Which example correctly uses std::collections::HashMap's Entry API to populate counts?

```rust
use std::collections::HashMap;
fn main() {
    let mut counts = HashMap::new();
    let text = "LinkedIn Learning";
    for c in text.chars() {
        // Complete this block
    }
    println!("{:?}", counts);
}
```

- [ ]

```rust
for c in text.chars() {
    if let Some(count) = &mut counts.get(&c) {
        counts.insert(c, *count + 1);
    } else {
        counts.insert(c, 1);
    };
}
```

- [x]

```rust
for c in text.chars() {
    let count = counts.entry(c).or_insert(0);
    *count += 1;
}
```

- [ ]

```rust
for c in text.chars() {
    let count = counts.entry(c);
    *count += 1;
}
```

- [ ]

```rust
for c in text.chars() {
    counts.entry(c).or_insert(0).map(|x| x + 1);
}
```

[reference](https://doc.rust-lang.org/std/collections/hash_map/struct.HashMap.html#method.entry)

#### Q17. Which fragment does not incur memory allocations while writing to a "file" (represented by a Vec<u8>)?

```rust
use std::collections::HashMap;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let mut v = Vec::<u8>::new();

    let a = "LinkedIn";
    let b = 123;
    let c = '🧀';

    // replace this line

    println!("{:?}", v);

    Ok(())
}
```

- [x]

```rust
write!(&mut v, "{}{}{}", a, b, c)?;
```

- [ ]

```rust
v.write(a)?;
v.write(b)?;
v.write(c)?;
```

- [ ]

```rust
v.write(a, b, c)?;
```

- [ ]

```rust
v.write_all(a.as_bytes())?;
v.write_all(&b.to_string().as_bytes())?;
c.encode_utf8(&mut v);
```

1. [Answered in rust user forum](https://users.rust-lang.org/t/formatting-and-writing-to-a-file-without-malloc-or-locks/52295/9)
2. [reference](https://doc.rust-lang.org/std/macro.write.html)

#### Q18. Does the `main` function compile? If so, why? If not, what do you need to change?

```rust
fn main() {
    let Some(x) = some_option_value;
}
```

- [ ] The code does not compile. `let` statements require a refutable pattern. Add `if` before `let`.
- [ ] The code compiles. `let` statements sometimes require a refutable pattern.
- [x] The code does not compile. `let` statements requires an irrefutable pattern. Add `if` before `let`.
- [ ] The code compiles. `let` do not require a refutable pattern.

#### Q19. Which statement about lifetimes is false?

- [ ] Lifetimes were redundantly specified in previous version of Rust.
- [ ] Lifetimes are specified when a struct is holding a reference to a value.
- [ ] Lifetimes are specified when certain values must outlive others.
- [x] Lifetimes are always inferred by the compiler.

#### Q20. When used as a return type, which Rust type plays a similar role to Python's `None`, JavaScript's `null`, or the `void` type in C/C++?

- [ ] `!`
- [ ] `None`
- [ ] `Null`
- [x] `()`

#### Q21. To convert a `Result` to an `Option`, which method should you use?

- [ ] `.as_option()`
- [x] `.ok()`
- [ ] `.to_option()`
- [ ] `.into()`

#### Q22. Which statement about the `Clone` and `Copy` traits is false?

- [x] `Copy` is enabled for primitive, built-in types.
- [ ] Without `Copy`, Rust applies move semantics to a type's access.
- [ ] When using `Clone`, copying data is explicit.
- [ ] Until a type implements either `Copy` or `Clone`, its internal data cannot be copied.

[ref from stack overflow](https://stackoverflow.com/questions/41413336/do-all-primitive-types-implement-the-copy-trait)

#### Q23. Why does this code _not_ compile?

```rust
fn returns_closure() -> dyn Fn(i32) -> i32 {
    |x| x + 1
}
```

- [ ] The returned `fn` pointer and value need to be represented by another trait.
- [ ] Closures are types, so they cannot be returned directly from a function.
- [ ] Closures are types and can be returned only if the concrete trait is implemented.
- [x] Closures are represented by traits, so they cannot be a return type.

[Rust book reference](https://doc.rust-lang.org/book/ch19-05-advanced-functions-and-closures.html#returning-closures)

#### Q24. What smart pointer is used to allow multiple ownership of a value in various threads?

- [x] `Arc<T>`
- [ ] `Box<T>`
- [ ] Both `Arc<T>` and `Rc<T>` are multithread safe.
- [ ] `Rc<T>`

[Rust book reference](https://doc.rust-lang.org/book/ch16-03-shared-state.html?highlight=arc%3CT%3E#atomic-reference-counting-with-arct)

#### Q25. Which types are _not_ allowed within an enum variant's body?

- [ ] zero-sized types
- [ ] structs
- [x] trait objects
- [ ] floating-point numbers

[Reference](https://doc.rust-lang.org/reference/types/trait-object.html)

#### Q26. Which statement about this code is true?

```rust
fn main() {
    let c = 'z';
    let heart_eyed_cat = '😻';
}
```

- [x] Both are character literals.
- [ ] `heart_eyed_cat` is an invalid expression.
- [ ] `c` is a string literal and `heart_eyed_cat` is a character literal.
- [ ] Both are string literals.

[Reference](https://doc.rust-lang.org/std/primitive.char.html)

#### Q27. Your application requires a single copy of some data type T to be held in memory that can be accessed by multiple threads. What is the thread-safe wrapper type?

- [ ] `Mutex<Arc<T>>`
- [ ] `Rc<Mutex<T>>`
- [x] `Arc<Mutex<T>>`
- [ ] `Mutex<Rc<T>>`

[Rust book reference](https://doc.rust-lang.org/book/ch16-03-shared-state.html#atomic-reference-counting-with-arct)

#### Q28. Which idiom can be used to concatenate the strings `a`, `b`, `c`?

```rust
let a = "a".to_string();
let b = "b".to_string();
let c = "c".to_string();
```

- [ ] `String::from(a,b,c)`
- [x] `format!("{}{}{}", a, b, c)`
- [ ] `concat(a,b,c)`
- [ ] `a + b + c`

#### Q29. In this function. what level of access is provided to the variable `a`?

```rust
use std::fmt::Debug;

fn report<T:Debug>(a: &T) {
    eprintln!("info: {:?}", a);
}
```

- [ ] print
- [x] read-only
- [ ] read/write
- [ ] debug

#### Q30. Which choice is _not_ valid loop syntax?

- [ ] `loop`
- [ ] `for`
- [ ] `while`
- [x] `do`

#### Q31. How do you construct a value of `Status` that is initialized to `Waiting`?

```rust
enum Status {
    Waiting,
    Busy,
    Error(String),
}
```

- [ ] `let s = Enum::new(Status::Waiting);`
- [ ] `let s = new Status::Waiting;`
- [x] `let s = Status::Waiting;`
- [ ] `let s = Status::new(Waiting);`

#### Q32. Which statement about enums is false?

- [ ] Enums are useful in matching patterns.
- [ ] Option is an enum type.
- [ ] Enum variants can have different types with associated data.
- [x] the term _enum_ is short for _enummap_
