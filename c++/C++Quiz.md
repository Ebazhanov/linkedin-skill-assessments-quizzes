## C++

#### Q1.  Which C++ Standard did add in-class default member initializers?



- [ ] C++98
- [x] C++11
- []  C++14
- [ ] C++17.

#### Q2. Can you use auto type deduction for non-static data members?



- [ ] Yes, since C++11
- [x] No
- [ ] Yes, since C++20



#### Q3.  Do you need to define a static inline data member in a cpp file?



- [x] No, the definition happens at the same place where a static inline member is declared.
- [ ] Yes, the compiler needs the definition in a cpp file.
- [ ]  Yes, the compiler needs a definition in all translation units that use this variable.


[Reference](https://en.cppreference.com/w/cpp/language/bit_field)

#### Q4. What's the output of the following code:

```cpp
struct S {
    int a { 10 };
    int b { 42 };
};
S s { 1 };
std::cout << s.a << ", " << s.b;
```

- [ ] Output is: 1, 0
- [ ] Output is: 10, 42
- [X] Output is: 1, 42


#### Q5. Can a static inline variable be non-constant?

- [X] Yes, it's just a regular variable.
- []  No, inline variables must be constant.

#### Q6. Consider the following code:

```cpp
struct C {
    C(int x) : a(x) { }
    int a { 10 };
    int b { 42 };
};
C c(0);

```

- [] C::a is initialized twice. The first time, it's initialized with 10 and then the second time with 0 in the constructor.
- [X]  C::a is initialized only once with 0 in the constructor.
- [ ]The code doesn't compile because the compiler cannot decide how to initialize the C::a member.
- [ ] 2 bytes


#### Q7. What happens when you throw an exception from a constructor?

- [ ]The object is considered "created" so it will follow the regular lifetime of an object.
- [x] The object is considered "partially created," and thus, the compiler won't call its destructor.
- [ ] he compiler calls std::terminate as you cannot throw exceptions from constructors.




#### Q8. What happens when you compile this code?

```cpp
struct Point { int x; int y; };
Point pt {.y = 10, .x = 11 };
std::cout << pt.x << ", " << pt.y;
```

- [X] The code doesn't compile. Designators have to be in the same order as the data members in the Point class.
- [] The code compiles and prints 11, 10.
- [ ] The code compiles and prints 10, 11.


#### Q9. Will this code work in C++11?
```cpp
struct User { std::string name = "unknown"; unsigned age { 0 }; };
User u { "John", 101 };
```
- [ ] Yes, the code compiles in C++11 mode.
- [X] The code compiles starting with C++14 mode.
- [ ] The code doesn't compile even in C++20.



#### Q10. Assume you have a std::map<string, int> m;. Select the single true statement about the following loop:



```cpp
for (const pair<string, int>& elem : m)
```

- [ ] A The loop properly iterates over the map, creating no extra copies.

- [X] B The loop will create a copy of each element in the map as the type of elem mismatches.

- [ ] C The code won't compile as a const pair cannot bind to a map.

#### Q11. Identify the correct extension of the user-defined header file in C++.

- [ ] .cpp
- [] .hg
- [X] .h
- [ ] .hf

#### Q12.Identify the incorrect constructor type.

```cpp
auto x = 4000.22;
```

- [x] Friend Constructor
- [ ] Default Constructor
- [ ] Parameterised Constructor
- [ ] CopyConstructor

#### Q13.Which of the following data type is supported in C++ but not in C?







- [x] bool
- [ ] int
- [ ] double
- [ ] float

#### Q14. What is the ternary operator equivalent to this code snippet?

```cpp
if(x)
    y=a;
else
    y=b;
```

- [ ] `y=a?b:x;`
- [ ] `y=if(x?a:b);`
- [ ] `y=(x&a)?a:(x&b)?b:0;`
- [x] `y=x?a:b;`

[Reference](https://www.w3schools.com/cpp/cpp_conditions_shorthand.asp)

#### Q15. What is the output of this code?

```cpp
#include <iostream>

int main(){
    int x=10, y=20;
    std::cout << "x = " << x++ << " and y = " << --y << std::endl;
    std::cout << "x = " << x-- << " and y = " << ++y << std::endl;
    return(0);
}
```

- [ ] `x = 10 and y = 20`  
       `x = 11 and y = 19`
- [ ] `x = 11 and y = 19`  
       `x = 10 and y = 20`
- [x] `x = 10 and y = 19`  
       `x = 11 and y = 20`
- [ ] `x = 11 and y = 20`  
       `x = 10 and y = 19`

#### Q16. Identify the correct syntax for declaring arrays in C++.
- [x] int arr[10]
- [ ] array arr[10]
- [ ] array{10}
- [ ] int arr

#### Q17.Size of wchat_t is.



- [ ] 2
- [ ] 4
- [] 2 or 4
- [X] Depends on number of bits in system

Note: a variant of the question below.

#### Q18. What is the output of this piece of code?

```cpp
int8_t a=200;
uint8_t b=100;
std::cout<<"a="<<(int)a;
std::cout<<", b="<<(int)b;
```

- [x] a=-56, b=100
- [ ] a=-55, b=100
- [ ] a=200, b=-156
- [ ] a=200, b=100

Note: Implicit conversion from 'int' to 'int8_t' (aka 'signed char') changes value from 200 to -56

#### Q19.Which of the following loops is best when we know the number of iterations?



- [ ] While
- [x] For
- [ ] Do
- [ ] All of the above

#### Q20. goto can be classified into?

- [x] label
- [ ] variable 
- [ ] operator
- [ ] function
