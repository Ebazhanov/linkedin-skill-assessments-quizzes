## Rust (Programming Language)

#### Q1. Which type cast preserves the mathematical value in all cases?

- [ ] i64 as i32
- [ ] usize as u64
- [ ] i32 as i64
- [ ] f64 as f32

#### Q2. What do the vertical bars represent here?

```rust
str::thread::spawn(|| {
  println!("LinkedIn");
});
```

- [ ] a closure
- [x] a thread
- [ ] a future
- [ ] a block

#### Q3. Which choice is not a scalar data type?

- [ ] integer
- [ ] float
- [ ] boolean
- [x] tuple

#### Q4. **\_** cannot be destructured.

- [ ] Traits
- [ ] Tuples
- [ ] Enums
- [ ] Structs

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
- [ ] .clone()
- [ ] .increment()

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
- [ ] struct that contains a reference to a value
- [ ] function with a generic argument
- [ ] struct that contains a reference to a boxed value
