## C++

#### Q1. What is the output of this code?

```cpp
vector<int> v(22);
bool b = (v[6]);
printf("%d", !b);
```

- [ ] False
- [ ] 0
- [x] 1
- [ ] This code has an error.

#### Q2. Which of the following is a reason why using this line is considered a bad practice? (_Alternative_: Why is using this line considered a bad practice?)

```cpp
using namespace std;
```

- [ ] The compiled code is always bigger because of all of the imported symbols.
- [x] If the code uses a function defined in two different libraries with the same prototype but possibly with different implementations, there will be a compilation error due to ambiguity.
- [ ] It automatically includes all header files in the standard library (cstdint, cstdlib, cstdio, iostream, etc).
- [ ] It causes the compiler to enforce the exclusive inclusion of header files belonging to the standard library, generating a compilation error when a different header file is included.

[Reference](https://www.geeksforgeeks.org/using-namespace-std-considered-bad-practice/)

#### Q3. What is the smallest size a variable of the type child_t may occupy in memory?

```cpp
typedef struct{
    unsigned int  age    : 4;
    unsigned char gender : 1;
    unsigned int  size   : 2;
}child_t;
```

- [ ] 7 bits.
- [ ] 25 bytes.
- [ ] 1 bit.
- [x] 1 byte.

[Reference](https://en.cppreference.com/w/cpp/language/bit_field)

#### Q4. What are the vectors v1 and v2 after executing the code?

```cpp
std::vector<int> v1{1,2,3},v2;
v2=v1;
v1.push_back(4);
v2.push_back(5);
```

- [ ] Error
- [ ] v1:{1,2,3,4}; v2:{5};
- [ ] v1:{1,2,3,4,5}; v2:{1,2,3,4,5};
- [x] v1:{1,2,3,4}; v2:{1,2,3,5};

#### Q5. Which of the following is a true statement about the difference between pointers and iterators?

- [ ] While pointers are variables that hold memory addresses, iterators are generic functions used to traverse containers. This function allows the programmer to implement read and write code as the container is traversed.
- [x] Incrementing an iterator always means accessing the next element in the container(if any), no matter the container. Incrementing the pointer means pointing to the next element in memory, not always the next element.
- [ ] Pointers are variables that hold memory address whereas iterator is unsigned integers that refer to offsets in arrays.
- [ ] All iterators are implemented with pointers so all iterators are pointers but not all pointers are iterators.

[Reference](https://stackoverflow.com/a/31128162)

#### Q6. What's the storage occupied by u1?

```cpp
union {
    uint16_t a;
    uint32_t b;
    int8_t c;
} u1;
```

- [x] 4 bytes
- [ ] 7 bytes
- [ ] 8 bytes
- [ ] 2 bytes

[Reference](https://en.cppreference.com/w/cpp/language/union)

#### Q7. Which of the following operator can be overloaded?

- [ ] `?:`
- [x] `new`
- [ ] `::`
- [ ] `.`

[Reference](https://www.tutorialspoint.com/operators-that-cannot-be-overloaded-in-cplusplus)

#### Q8. Which of the following shows the contents of the vector pointed by v1 and v2 after running this code?

```cpp
std:: vector<int> *v1 = new std::vector<int>({1,2,3});
std:: vector<int> *v2;
v2=v1;
v1->push_back(4);
v2->push_back(5);
```

- [ ] `*v1:{1,2,3,4}; *v2:{5};`
- [x] `*v1:{1,2,3,4,5}; *v2:{1,2,3,4,5};`
- [ ] Error
- [ ] `*v1:{1,2,3,4}; *v2:{1,2,3,5};`

v1 and v2 point to the same vector.

#### Q9. Which of the following is not a difference between a class and a struct?

- [ ] Because structs are part of the C programming language, there is some complexity between C and C++ structs. This is not the case with classes.
- [ ] Classes may have member functions; structs are private.
- [ ] The default access specifier for members of a struct is public, whereas, for members of the class, it is private.
- [x] Template type parameters can be declared with classes, but not with the struct keyword.

Templates can be used with both classes and structs
[Refernce](https://docs.microsoft.com/en-us/cpp/cpp/struct-cpp?view=msvc-170)
[Reference](https://www.fluentcpp.com/2017/06/13/the-real-difference-between-struct-class/)

#### Q10. Suppose you need to keep a data struct with permission to access some resource based on the days of the week, but you can't use a bool variable for each day. You need to use one bit per day of the week. Which of the following is a correct implementation of a structure with bit fields for this application?

- [x] A

```cpp
typedef struct {
    int sunday:1;
    int monday:1;
    // more days
    int friday:1;
    int saturday:1;
} weekdays;
```

- [ ] B

```cpp
typedef char[7]: weekdays;
```

- [ ] C

```cpp
typedef struct {
    bit sunday:1;
    bit monday:1;
    // more days
    bit friday:1;
    bit saturday:1;
} weekdays;

```

- [ ] D

```cpp
typedef struct {
    bit sunday;
    bit monday;
    // more days
    bit friday;
    bit saturday;
} weekdays;
```

[Reference](https://en.cppreference.com/w/cpp/language/bit_field) _NOTE_: Correct syntax is that each variable size is 1 bit. `bit` is not a type in C++.

#### Q11. What is an lvalue?

- [ ] It's a constant expression, meaning an expression composed of constants and operations.
- [ ] It's an expression that represents an object with an address.
- [ ] It's an expression suitable for the left-hand side operand in a binary operation.
- [x] It's a location value, meaning a memory address suitable for assigning to a pointer or reference.

#### Q12. What does auto type specifier do in this line of code (since C++11)?

```cpp
auto x = 4000.22;
```

- [x] It specifies that the type of x will be deduced from the initializer - in this case, double.
- [ ] It specifies that the type of x is automatic meaning that it can be assigned different types of data throughout the program.
- [ ] It specifies that x is a variable with automatic storage duration.
- [ ] It specifies that more memory will be allocated for x in case it needs more space, avoiding loss of data due to overflow.

#### Q13. A class template is a \_?

- [x] class written with the generic programming paradigm, specifying behavior in terms of type parameter rather than specific type.
- [ ] blank superclass intended for inheritance and polymorphism.
- [ ] class that only consists of a member variable, with no constructor, destructor, or member functions.
- [ ] skeleton source code for a class where the programmer has to fill in specific parts to define the data types and algorithms used.

[Reference](https://www.mygreatlearning.com/blog/templates-in-cpp/)

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

#### Q15. What is the output of the code given below?

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

#### Q16. What is the meaning of the two parts specified between parentheses in a range-based for loop, separated by a colon?

- [x] The first is a variable declaration that will hold an element in a sequence. The second is the sequence to traverse.
- [ ] The first is an iterator, and the second is the increment value to be added to the iterator.
- [ ] The first is the iterating variable. The second is a `std::pair` that specifies the range (start and end) in which the variable will iterate.
- [ ] The first is a container object. The second is a `std::pair` that specifies the range (start and end) in which the elements will be accessed within the loop.

#### Q17. What is the output of the code given below?

```cpp
int8_t a=200;
uint8_t b=100;
if(a>b)
    std::cout<<"greater";
else
    std::cout<<"less";
```

- [ ] There is no output because there is an exception when comparing an int8_t with a uint8_t.
- [ ] greater
- [x] less
- [ ] There is no output because there is a compiler error.

Note: a variant of the question below.

#### Q18. What is the output of this block of code?

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

#### Q19. What is the output after executing this code snippet?

```cpp
int x=5, y=2;
if(x & y) {
    /*_part A_*/
}
else {
    /*_part B_*/
}
```

- [ ] Part A executes because x==5 (true) and y==2 (true), thus the AND operation evaluates as true.
- [x] Part B executes because (x & y) results in 0, or false.
- [ ] Part A executes because (x & y) results in a nonzero value, or true.
- [ ] Part B executes because the statement (x & y) is invalid, thus false.

[Reference](https://stackoverflow.com/questions/63867765/dont-understand-why-if-5-2-is-false)

#### Q20. What is a valid definition for the `get_length` function, which returns the length of a null-terminated string?

- [x] A

```cpp
int get_length(char *str) {
    int count=0;
    while(str[count++]);
    return count-1;
}
```

- [ ] B

```cpp
int get_length(char *str) {
    int count=0;
    while(str!=NULL){
        count++;
        str++;
    }
    return count;
}
```

- [ ] C

```cpp
int get_length(char *str) {
    int count=0;
    while((*str)++)
        count++;
    return count;
}
```

- [ ] D

```cpp
int get_length(char *str) {
    int count=0;
    while(str++)
        count++;
    return count;
}
```

#### Q21. Which STL class is the best fit for implementing a collection of data that is always ordered so that the pop operation always gets the greatest of the elements? Suppose you are interested only in push and pop operations.

- [ ] `std::list`
- [ ] `std::vector`
- [x] `std::priority_queue`
- [ ] `std::map`

#### Q22. What is the meaning of the three sections specified between parentheses in a for loop separated by semicolons?

- [ ] The first is the iterating variable name, the second is the number of times to iterate, and the third is the desired increment or decrement (specified with a signed integer).
- [x] The first is the initialization block, the second is the condition to iterate, and the third is the increment block.
- [ ] The first is the iterating variable, the second is the container in which it should operate, and the third is an exit condition to abort at any time.
- [ ] The first is the iterating variable name, the second is the starting value for the iterating variable, and the third is the stop value (the last value plus one).

#### Q23. What does this code print?

```cpp
int i = 0;
printf("%d", i++);
printf("%d", i--);
printf("%d", ++i);
printf("%d", --i);
```

- [x] 0,1,1,0
- [ ] 0,1,0,1
- [ ] 0,0,1,0
- [ ] 1,0,1,0

[Reference](https://www.geeksforgeeks.org/pre-increment-and-post-increment-in-c/)

#### Q24. What is true about the variable named `ptr`?

```cpp
void *ptr;
```

- [ ] It is a pointer initialized at NULL.
- [ ] It is a pointer to a void function.
- [ ] That declaration causes a compiler error, as pointers must specify a type.
- [x] It is a pointer to a value with no specific type, so it may be cast to point to any type.

[Reference](https://en.cppreference.com/w/cpp/language/pointer)

#### Q25. What is the output of the code given below?

```cpp
int c=3; char d='A';
std::printf("c is %d and d is %c",c,d);
```

- [ ] c is d and d is c
- [ ] c is A and d is 3
- [x] c is 3 and d is A
- [ ] c is c and d is d

#### Q26. What is the output of this code?

```cpp
printf("1/2 = %f",(float)(1/2));
```

- [ ] 1/2 = 0.499999
- [ ] 1/2 = 0
- [x] 1/2 = 0.000000
- [ ] 1/2 = 0.5

#### Q27. What is the difference between a public and a private class member?

- [ ] Public members are the same as global variables, so every part of the code has access to them. Private members are the same as automatic variables, so only their class has access to them.
- [ ] Public members are made accessible to any running application. Private members are made accessible only to the application where the object is instantiated.
- [ ] Public members will be compiled as shared variables in a multithreaded environment. Private members will be compiled as Thread-local variables.
- [x] Public members can be accessed by any function. Private members can be accessed only by the same class's member functions and the friends of the class.

#### Q28. What is the value of `x` after executing this code?

```cpp
int x=10, a=-3;
x=+a;
```

- [ ] 3
- [ ] 7
- [x] -3
- [ ] 13

So x **+=** a would simply mean (x = x + a), here that yields x = 10 + (-3) = 7.
But, here it is (x **=+** a): This is equivalent to x = +a. Here, the unary plus operator + is used. However, the unary plus operator doesn't change the sign of the value; it simply ensures that the value is positive. So, it effectively does nothing in this context
[Reference](https://stackoverflow.com/questions/6958401/the-difference-between-and)

#### Q29. Which statement is true?

- [ ] Only classes can have member variables and methods.
- [x] C++ supports multiple inheritance.
- [ ] C++ supports only single inheritance.
- [ ] Only structs can inherit.

#### Q30. Consider a pointer to void, named `ptr`, which has been set to point to a floating point variable `g`. Which choice is a valid way to dereference `ptr` to assign its pointed value to a float variable `f` later in the program?

```cpp
float g;
void *ptr=&g;
```

- [ ] `float f=*(float)ptr;`
- [ ] `float f=(float *)ptr;`
- [ ] `float f=(float)*ptr;`
- [x] `float f=*(float *)ptr;`

#### Q31. What is the `.*` operator and what does it do?

- [ ] It is the same as the class member access operator, or arrow operator `(->)`, which allows you to access a member of an object through a pointer to the object.
- [x] It is the pointer to the member operator, and it allows you to access a member of an object through a pointer to that specific class member.
- [ ] It is the member access with an address of the operator, which returns the address of a class or struct member.
- [ ] It is a combination of the member access operator `(.)` and the dereference operator `(*)`, so it allows you to access the object that a member pointer points to.

[Reference](https://en.cppreference.com/w/cpp/language/operator_member_access)

#### Q32. For these declarations, which choice shows four equivalent ways to assign the character "y" in the string to a char variable c?

```cpp
char buff[50] = "strings as arrays of characters are fun!"
char *str = buff+11;
char c;
```

- [ ] A

```cpp
c = buff[16];
c = str[5];
c = *(buff+16);
c = *(str+5);
```

- [ ] B

```cpp
c = *(buff[15]);
c = *(str[4]);
c = buff+15;
c = str+4;
```

- [x] C

```cpp
c = buff[15];
c = str[4];
c = *(buff+15);
c = *(str+4);
```

- [ ] D

```cpp
c = *(buff[16]);
c = *(str[5]);
c = buff+16;
c = str+5;
```

#### Q33. Which choice is the correct declaration for the class named Dog, derived from the Animal class?

```cpp
class Animal{
    //....
}
```

- [ ] A

```cpp
class Dog :: public Animal {
   //....
};
```

- [x] B

```cpp
class Dog : public Animal {
   //....
};
```

- [ ] C

```cpp
public class Animal :: Dog {
   //....
};
```

- [ ] D

```cpp
public class Dog extends Animal {
   //....
};
```

#### Q34. What is the output of this code given below?

```cpp
#include <cstdio>
using namespace std;

int main(){
    char c = 255;
    if(c>10)
        printf("c = %i, which is greater than 10", c);
    else
        printf("c = %i, which is less than 10", c);
    return 0;
}
```

- [x] c = -1, which is less than 10
- [ ] c = 255, which is greater than 10
- [ ] c = -1, which is greater than 10
- [ ] c = 255, which is less than 10

Technically, whether a `char` is `signed` or `unsigned` is implementation-defined;
in the latter case, the second answer would be correct.
[Reference](https://en.cppreference.com/w/cpp/language/types)

#### Q35. How can C++ code call a C function?

- [ ] by simply calling the C code
- [ ] There is no way for C++ to call a C function
- [x] by using extern "C"
- [ ] by importing the source C code

#### Q36. Which choice is _not_ a valid type definition of a structure that contains x and y coordinates as integers, and that can be used exactly as shown for the variable named `center`?

```cpp
coord center;
center.x = 5;
center.y = 3;
```

- [x] A

```cpp
typedef struct coord {
    int x;
    int y;
};
```

- [ ] B

```cpp
typedef struct coord {
    int x;
    int y;
} coord;
```

- [ ] C

```cpp
typedef struct {
    int x;
    int y;
} coord;
```

- [ ] D

```cpp
struct coord {
    int x;
    int y;
};

typedef struct coord coord;
```

#### Q37. Which choice does _not_ produce the same output as this code snippet? Assume the variable `i` will not be used anywhere else in the code.

```cpp
for (i=1;i<10;i++){
    cout<<i<<endl;
}
```

- [x] A

```cpp
i=1;
while(i<10){
    cout<<++i<<endl;
}
```

- [ ] B

```cpp
for (int i:{1,2,3,4,5,6,7,8,9}) {
    cout<<i<<endl;
}
```

- [ ] C

```cpp
i = 1;
do {
    cout<<i++<<endl;
} while(i<10);
```

- [ ] D

```cpp
i = 1;
loop:
    cout<<i++<<endl;
    if(i<10) goto loop;
```

#### Q38. What does this part of a main.cpp file do?

```cpp
#include "library.h"
```

- [ ] It causes the toolchain to compile all the contents of library.h so that its executable code is available when needed by the final application.
- [ ] It cherry-picks library.h for the declarations and definitions of all data and functions used in the remainder of the source file main.cpp, finally replacing the `#include` directive with those declarations and definitions.
- [ ] It informs the linker that some functions or data used in the source file main.cpp are contained in library.h, so that they can be called in run time. This is also known as dynamic linking.
- [x] It causes the replacement of the `#include` directive by the entire contents of the source file library.h. This is similar to the Copy-Paste operation of library.h into main.cpp.

#### Q39. Consider this function declaration of `is_even`, which takes in an integer and returns true if the argument is an even number and false otherwise. Which declarations are correct for overloaded versions of that function to support floating point numbers and string representations of numbers?

```cpp
bool is_even(int);
```

- [x] A

```cpp
bool is_even(float f);
bool is_even(char *str);
```

- [ ] B

```cpp
bool is_even(float f);
bool is_even(char str);
```

- [ ] C

```cpp
bool is_even_float(float f);
bool is_even_str(char *str);
```

- [ ] D

```cpp
float is_even(float f);
char *is_even(char *str);
```

#### Q40. Which choice is an include guard for the header file `my_library.h`?

- [ ] A

```cpp
#ifdef MY_LIBRARY_H
#define MY_LIBRARY_H

// my_library.h content

#endif /* MY_LIBRARY_H */
```

- [x] B

```cpp
#ifndef MY_LIBRARY_H
#define MY_LIBRARY_H

// my_library.h content

#endif /* MY_LIBRARY_H */
```

- [ ] C

```cpp
#ifdef MY_LIBRARY_H
#undef MY_LIBRARY_H

// my_library.h content

#endif /* MY_LIBRARY_H */
```

- [ ] D

```cpp
#define MY_LIBRARY_H
#include MY_LIBRARY_H

// my_library.h content

#undef MY_LIBRARY_H
```

#### Q41. What's wrong with this definition when using a pre-C++11 compiler?

```cpp
std::vector<std::vector<int>> thematrix;
```

- [x] There's nothing wrong with it.
- [ ] An `std::vector` cannot contain more `std::vector` containers as its elements.
- [ ] The correct syntax should be: `std::vector[std::vector[int]] thematrix;`
- [ ] `>>` is parsed as the shift-right operator, and thus results in a compile error.

#### Q42. What is the statement below equivalent to?

#### Q42.b. What is the statement equivalent to?

```cpp
sprite->x
```

- [ ] `sprite.x`
- [ ] `sprite.*x`
- [x] `(*sprite).x`
- [ ] `*sprite.x`

#### Q43. Consider a class named `complexNumber`. Which code will result in an equivalent object?

```cpp
complexNumber(float real, float im)
: real_part(real),
 im_part(im){}
```

- [ ] A

```cpp
complexNumber(float real, float im) {
    this->real = real_part;
    this->im = im_part;
}
```

- [ ] B

```cpp
complexNumber(float real, float im) {
    this->real_part(real);
    this->im_part(im);
}
```

- [x] C

```cpp
complexNumber(float real, float im) {
    this->real_part = real;
    this->im_part = im;
}
```

- [ ] D

```cpp
complexNumber(float real, float im) {
    this->real_part = &real;
    this->im_part = &im;
}
```

#### Q44. What is the result of executing this code snippet?

```cpp
bool x=true, y=false;

if (~x || y) {
    /*part A*/
} else {
    /*part B*/
}
```

- [ ] Part A executes because the expression `(~x || y)` always results in true if `y==false`.
- [ ] Part B executes because the statement `(~x || y)` is invalid, thus false.
- [x] Part A executes because `~x` is not zero, meaning true.
- [ ] Part B executes because `~x` is false and `y` is false, thus the `OR` operation evaluates as false.

#### Q45. What would be the output of this code?

```cpp
int32_t nums[3]={2,4,3};
std::cout << ( nums[0] << nums[1] << nums[2] );
```

- [ ] The output is the addresses of `nums[0]`, `nums[1]`, and `nums[2]`, in that order, with no spaces.
- [x] 256
- [ ] `0`
- [ ] `243`

#### Q46. What is the output of this code?

```cpp
float values[5]={0.54f, 2.71828f, 3.14159f, 5.499999f, 10.0f};
for(auto f:values)
    printf("%i ",(int)(f+0.5f));
```

- [ ] `0.54 2.71828 3.14159 5.499999 10.0`
- [ ] `1 3 4 6 11`
- [ ] `0 2 3 5 10`
- [x] `1 3 3 5 10`

#### Q47. Which of the following STL classes is the best fit for implementing a phonebook? Suppose each entry contains a name and a phone number, with no duplicates, and you want to have a lookup by name.

- [ ] `std::priority_queue`
- [ ] `std::list`
- [ ] `std::vector`
- [x] `std::map`

[Reference](https://en.cppreference.com/w/cpp/container/map)

#### Q48. What does this program do?

```cpp
#include <iostream>
#include <fstream>
using namespace std;

int main(){
    ifstream file1("text1.txt", ios::binary);
    ofstream file2("text2.txt", ios::binary);
    file2 << file1.rdbuf();
}
```

- [ ] It renames text1.txt to text2.txt.
- [ ] It makes a directory called text2.txt and moves text1.txt there.
- [x] It copies the contents of text1.txt into text2.txt - i.e., it makes a copy of text1.txt, named text2.txt.
- [ ] It appends the contents of text1.txt into text2.txt - i.e., replaces the contents of text2.txt by the concatenation of text2.txt and text1.txt.

[Reference](https://en.cppreference.com/w/cpp/header/fstream)

#### Q49. Which of the following is _not_ a consequence of declaring the member variable `count` of my_class as static? / Alt.: Which statement is true when declaring the member variable `count` as static?

```cpp
class my_class {
    public: static int count;
}
```

- [x] The variable cannot be modified by any part of the code in the same application or thread. However, other threads may modify it.
- [ ] The variable exists even when no objects of the class have been defined so it can be modified at any point in the source code.
- [ ] The variable is allocated only once, regardless of how many objects are instantiated because it is bound to the class itself, not its instances.
- [ ] All objects that try to access their count member variable actually refer to the only class-bound static count variable.

[Reference](https://en.cppreference.com/w/cpp/language/static)

#### Q50. What is the assumed type of a constant represented in the source code as `0.44`?

- [x] double
- [ ] long float
- [ ] long double
- [ ] float

#### Q51. What is an appropriate way of removing `my_object` as shown below?

```cpp
my_class *my_object = new my_class();
```

- [x] `delete(my_object);`
- [ ] `free(my_object);`
- [ ] The garbage collector will destroy the object eventually.
- [ ] Exiting the scope will destroy the object.

#### Q52. What is the correct way to call the `count` member function for the object pointer called `grades`?

```cpp
class my_array{
    public:
        int count();
};  // ... more members above

int main(){
    my_array *grades = new my_array();
};  // ... more code above
```

- [ ] `grades.count();`
- [ ] `my_array->count();`
- [x] `grades->count();`
- [ ] `my_array.count();`

[Reference](https://en.cppreference.com/w/c/language/operator_member_access)

#### Q53. What would be the output of this code?

```cpp
int i0=4, i1=6, i2=8;
int& nums[3]={i2,i0,i1};
std::cout<<nums[0]<<nums[1]<<nums[2];
```

- [x] There is no output. The code causes a compiler error because `nums` is an array of references, which is illegal.
- [ ] 846
- [ ] The output is the addresses of `i2`, `i0`, and `i1`, in that order, with no spaces.
- [ ] 468

[Reference](https://en.cppreference.com/w/cpp/language/array)

#### Q54. Does this code cause a compiler error? If so, why, and if not, what is `child_t`?

```cpp
typedef struct{
    unsigned int  age    : 4;
    unsigned char gender : 1;
    char                 : 0;
    unsigned int  size   : 2;
}child_t;
```

- [ ] Yes, it causes a compiler error because the colon character is not allowed in struct definitions.
- [x] No, and `child_t` is a type defined as a structure with bit fields. It has 4 bits for age and 1 bit for gender in the first byte, and 2 bits for size in the second byte.
- [ ] Yes, it causes a compiler error because there is an unnamed field.
- [ ] Yes, it causes a compiler error because one field is defined as having a size of 0.

[Reference](https://en.cppreference.com/w/cpp/language/bit_field)

#### Q55. What is this expression equivalent to?

```cpp
A->B
```

- [ ] `*(A.B)`
- [ ] `B=A`
- [x] `(*A).B`
- [ ] `&A.B`

Note: a simpler variant of the question below.

#### Q56. What is this expression equivalent to?

```cpp
A->B->C->D
```

- [ ] `A.B.C.D`
- [ ] `*A.*B.*C.*D`
- [ ] `&A.&B.&C.&D`
- [x] `*(*((*A).B).C).D`

**Note:** a more complex variant of the question above.

#### Q57. What does this function do?

```cpp
auto buff = new char[50];
std::memset(buff,20,50);
```

- [ ] It declares a memory buffer named buff that starts at address 20 and ends at address 70.
- [ ] It sets all bits in the array named buffer from its element at index 20 to its element at index 50.
- [x] It writes the value 20 in every memory address from buff to buff+49.
- [ ] It declares a memory buffer named buff that starts at address 20 and ends at address 50.

[Reference](https://en.cppreference.com/w/cpp/string/byte/memset)

#### Q58. Consider a class named `CustomData`. Which choice is a correct declaration syntax to overload the postfix `++` operator as a class member?

- [ ] `CustomData& operator++();`
- [ ] `void operator++(CustomData);`
- [ ] `CustomData operator++(CustomData);`
- [x] `CustomData operator++(int);`

[Reference](https://en.cppreference.com/w/cpp/language/operators)

#### Q59. You want to sort my_array, declared below. Which choice is the correct call to std::sort, using a lambda expression as the comparison function?

```cpp
std::array<uint32_t, 50> my_array;
```

- [x] A

```cpp
std::sort(my_array.begin(), my_array.end(),
    [](uint32_t a, uint32_t b) {
        return a < b;
    })
```

- [ ] B

```cpp
lambda(uint32_t a, uint32_t b){
    return a < b;
}
std::sort(my_array.begin(), my_array.end(), lambda);
```

- [ ] C

```cpp
std::sort(my_array.begin(), my_array.end(),
    lambda(uint32_t a, uint32_t b){
        return a < b;
    })
```

- [ ] D

```cpp
lambda(uint32_t a, uint32_t b){
    return a < b;
}
std::sort(my_array.begin(), my_array.end(), &lambda);
```

[Reference](https://docs.microsoft.com/en-us/cpp/cpp/lambda-expressions-in-cpp?view=msvc-160)

#### Q60. Which choice is the most reasonable implementation of the function std::mutex::lock() by using std::mutex::try_lock()?

- [x] A

```cpp
void std::mutex::lock(){
    while(!this->try_lock());
}
```

- [ ] B

```cpp
void std::mutex::lock(){
    return (this->try_lock());
}
```

- [ ] C

```cpp
void std::mutex::lock(){
    while(1)
        this->try_lock();
}
```

- [ ] D

```cpp
void std::mutex::lock(){
    while(this->try_lock());
}
```

Note: variant of the question below.

#### Q61. What is the main difference between these two Functions?

```cpp
std::mutex::lock()
std::mutex::try_lock()
```

- [ ] `lock()` has a higher privilege over `try_lock()`. This means that you have a better chance of acquiring a mutex `with lock()`.
- [x] Both attempt to acquire a lock, but `lock()` blocks if the mutex is not available, whereas `try_lock()` returns whether the mutex is available or not.
- [ ] `lock()` enforces preemption, whereas `try_lock()` suggests preemption.
- [ ] If the mutex is not available, `try_lock()` returns with a corresponding code, whereas `lock()` snatches the mutex from the thread that currently has it.

Note: variant of the question above.

[Reference](https://en.cppreference.com/w/cpp/thread/mutex/try_lock)

#### Q62. What is the purpose of a destructor?

- [x] It allows the programmer to write the necessary code to free the resources acquired by the object prior to deleting the object itself.
- [ ] It deletes an object. One example of a destructor is the `delete()` function.
- [ ] It terminates a program. This may be achieved as a regular function call or as an exception.
- [ ] There are no destructors in C++.

#### Q63. What is one benefit of declaring the parameter as a `const` reference instead of declaring it as a regular object?

```cpp
int calculateMedian(const my_array& a)
```

- [ ] Actually, objects cannot be passed as regular variables, because they require a constructor call. Therefore, a `const` reference is the only way to pass class instances to functions.
- [ ] There are no benefits because a reference and an object are treated as the same thing.
- [x] The `const` qualifier forbids the code to modify the argument, so the programmer can rest assured that the source object will remain unchanged. / Alt.: The argument is passed as a reference, so if the passed my_array object is large, the program will require less time and memory.
- [ ] The argument is passed as a reference, so the function receives a copy that can be modified without affecting the original variable.

[Reference](https://stackoverflow.com/a/2627179/10773894)

#### Q64. What is an include guard?

- [ ] a preprocessor directive that prevents inconsistent behaviors in lines that contain the #ifdef, #ifndef, or #elif directives
- [ ] a compiler option that prevents the user code from including additional libraries
- [x] a preprocessor statement that prevents a source file from being included more than once in a project
- [ ] a library that adds safety features such as mutexes, watchdog timers, and assertions to the project

#### Q65. What would be the correct declaration of a default constructor for a class named Sprite?

- [x] A
  ```cpp
  public: Sprite();
  ```
- [ ] B
  ```cpp
  private: void Sprite();
  ```
- [ ] C
  ```cpp
  public: void Sprite();
  ```
- [ ] D
  ```cpp
  private: Sprite();
  ```

#### Q66. What is the purpose of this line in a header file?

```cpp
#pragma once
```

- [ ] to restrict the use of its contents to only one source file
- [ ] to tell the compiler that only one variable can be instantiated from the classes or types contained in this header file
- [ ] to help the compiler finish faster by assuring that only one compiler pass is necessary for the code included in this header file
- [x] to make the compiler parse that header file only once, even if it is included multiple times in the source

[reference here](https://en.cppreference.com/w/cpp/preprocessor/impl)

#### Q67. What is a variable of type double?

- [ ] a 2-tuple
- [ ] an integer number
- [x] a floating point number
- [ ] a string with more than 255 characters

[Reference](https://www.educba.com/c-plus-plus-double/)

#### Q68. Other than shifting bits to the left, what is the << operator used for?

- [ ] shifting characters to the left in a string.
- [x] inserting characters into an output stream like std::cout.
- [ ] comparing floating point numbers as less-than.
- [ ] assigning a variable to a reference.

#### Q69. Which choice is a reason to specify the type of a pointer instead of using `void *`, which works as a pointer to any type?

- [ ] The compiler needs the data type to make sure that the pointer is not going to be used on illegal non-pointable types such as functions, labels, pointers, and references.
- [ ] `void *` does not work for any type. The language does not allow assigning anything other than `void` to a pointer to `void *`.
- [x] The compiler needs the data type to know how much memory to allocate for the pointer because different data types require different pointer lengths.
- [ ] Yes, it causes a compiler error because one field is defined as having a size of 0.

[Reference](https://stackoverflow.com/questions/9802585/why-is-the-data-type-needed-in-pointer-declarations)

#### Q70. What is wrong with this piece of code?

```cpp
#include <iostream>
char str[20];
int main(){
    std::cout << "What's your name? ";
    str << std::cin
    std::cout << "Hello, " << str;
    return 0;
}
```

- [ ] The main function is supposed to have a void return type.
- [ ] `std::cin` and `std::cout` are invalid. The correct names for the character input and output streams are `cin` and `cout`.
- [ ] The address of `str` is supposed to be used. That is `&str` instead of `str`.
- [x] The input operator flow is inverted. it should start from `std::cin` and then flow (>>) into `str`.

#### Q71. When placed in a valid execution context, which statement will dynamically allocate memory from the heap for an integer of value 11?

- [ ] `int anInt = new int(11);`
- [ ] `int* anInt = new int[11];`
- [ ] `int anInt = new int[11];`
- [x] `int* anInt = new int(11);`

#### Q72. Which choice best describes the type `long`?

- [x] an integer number of at least 32 bits
- [ ] a string with more than 255 characters
- [ ] a pointer
- [ ] a 64-bit floating point number

#### Q73. Which of the following types has the closest functionality to a class?

- [x] `struct`
- [ ] `union`
- [ ] `enum`
- [ ] `namespace`

[Reference](https://en.cppreference.com/w/c/language/struct)

#### Q74. Given these records in a map, how will you update the value for the key "Sinead" to 22?

![image](images/Q79.png?raw=png)

- [x] `marks["Sinead"] = 22`
- [ ] `marks["Sinead"].22`
- [ ] `marks["Sinead"] -> 22`
- [ ] `marks["Sinead"].value = 22`

#### Q75. Why can the std::sort receive a function object as one of its parameters?

- [x] `The std::sort function is a template. The programmer is free to enter the sorting algorithm in a function object as an argument.`
- [ ] `Actually, std::sort takes only one argument, which is the container to be sorted.`
- [ ] `std::sort operates on a template container. The compiler does not know how to relationally compare the values it contains, so a function must be provided to do the comparison.`
- [ ] `std::sort will use the parameter function as an error handler. The function will be called if an error occurs.`

#### Q76. What will happen when you execute this code snippet?

```
#include <iostream>

int main() {
float a = 5.51;
int b = static_cast<int>(a);
std::cout << b;
}
```

- [ ] `6 will be printed on standard output, with no compilation warnings generated.`
- [x] `5 will be printed on standard output, with no compilation warnings generated.`
- [ ] `6 will be printed on standard output, with compilation warnings generated.`
- [ ] `5 will be printed on standard output, with compilation warnings generated.`

#### Q77. Which access specifier does not allow class members to be accessed from outside the class, but allows them to be accessed by derived classes?

- [ ] guarded
- [x] protected
- [ ] public
- [ ] private

#### Q78. The default executable generation on UNIX for a C++ program is \_

- [ ] a.exe
- [ ] a
- [x] a.out
- [ ] out.a

#### Q79. What will be the output of the following program?

```cpp
#include <iostream>
using namespace std;
int main() {
  int a=1;
  cout<<(a++)*(++a)<<endl;
  return 0;
}
```

- [ ] 1
- [ ] 2
- [x] 3
- [ ] 6

#### Q80. What does "c" stand for in cout and cin?

- [ ] compiler
- [ ] console
- [x] character
- [ ] standard namespace

#### Q81. What is the use of tellp()?

- [ ] Current Input Pointer position
- [x] Current Output Pointer position
- [ ] Last Input Pointer position
- [ ] Last Output Pointer position

#### Q82. What is callback function?

- [ ] Pointer for a pointer
- [x] Pointer for a function
- [ ] function for a pointer
- [ ] function for a class

#### Q83. What is the correct syntax to output "Hello World" in C++?

- [x] cout << "Hello World";
- [ ] System.out.println("Hello World");
- [ ] print("Hello World");
- [ ] Console.WriteLine("Hello World");

#### Q84. How many categories of iterators are there in C++?

- [ ] 4
- [ ] 3
- [ ] 7
- [x] 5

#### Q85. What is the meaning of base class in C++ ?

- [ ] It inherits other class
- [ ] It has a pointer variable
- [ ] It is the first class declared
- [x] Another class got inherited from this class

#### Q86. The size of C++ objects is expressed in terms of multiples of the size of a ** and the size of a char is **.

- [ ] char, 4
- [ ] float, 8
- [ ] int, 1
- [x] char, 1

#### Q87. Implementation-dependent aspects about an implementation can be found in

- [ ] `<numeric>`
- [ ] `<limit>`
- [x] `<limits>`
- [ ] `<implementation>`

#### Q88. What is a default constructor?

- [x] a constructor that can be used with no arguments
- [ ] a constructor that does not have a return value
- [ ] a constructor that is used by multiple classes
- [ ] a constructor that initializes all members of a class

#### Q89. When protecting a header file, why would you use '#pragma once' instead of 'include' guard?

- [ ] There is no reason to choose because they serve different purposes
- [x] An include guard uses a macro to achieve single inclusion, but the compiler cannot prevent the programmer from defining that macro elsewhere, which would result in no inclusion at all
      defining that macro elsewhere, which would result in no inclusion at all
- [ ] '#pragma once' guarantees that the header code will never be changed because it is enforced by the compiler
- [ ] Include guards refer to the header file in the file system, not to the code, so they are not helpful if the header file exists
      more than once in a project. This is not a problem with '#pragma once'

#### Q90. Which of the following statements is valid?

- [ ] We can create a new C++ operator.
- [ ] We can change the precedence of the C++ operator.
- [x] We can not change the operator templates.
- [ ] We can change the associativity of the C++ operators.

#### Q91. Which of the following is/are automatically added to every class, if we do not write our own?

- [ ] Copy Constructor
- [ ] Assignment Operator
- [ ] A constructor without any parameter
- [x] All of the above

#### Q92. The if-else statement can be replaced by which operator?

- [ ] certain structure
- [ ] choosing structure
- [x] selective structure
- [ ] None of the Above

#### Q93. Which choice would be a recursive solution to the factorial n! problem?

- [ ] &shy;

```cpp
void fact(int n) {
    if (n <= 0)
        return 0;
    else
        return 1;
}
```

- [ ] &shy;

```cpp
int fact(int n) {
    if (n <= 0)
        return 1;
    else
        return (fact(n) * (n-1));
}
```

- [ ] &shy;

```cpp
int fact(int n) {
    if (n >= 0)
        return 1;
    else
        return (fact(n-1) * n);
}
```

- [x] &shy;

```cpp
int fact(int n) {
    if (n <= 0)
        return 1;
    else
        return (fact(n-1) * n);
}
```

#### Q94. A class destructor can be called when a variety of situations occur. Which choice is not one of those situations?

- [ ] The program is terminated. This calls the destructor of static duration objects.
- [ ] The delete () function is called for an object pointer assigned with the new operator.
- [x] The garbage collector detects that an object is no longer going to be used.
- [ ] An automatic storage duration object goes out of scope.

#### Q95. You are designing a foreign exchange payments system in C++, You need to model a transaction of a currency that has an integer as its quantity and a float as its price. You then want to declare an actual object of this type. How will you achieve this?

- [x] A

```cpp
struct currencyDeal {
    float price;
    int quantity;
};

currencyDeal firstDeal;
```

- [ ] B

```cpp
union currencyDeal {
    float price;
    int quantity;
};

currencyDeal firstDeal;
```

- [ ] C

```cpp
struct currencyDeal {
    float price;
    int quantity;
};
```

- [ ] D

```cpp
union currencyDeal {
    float price;
    int quantity;
};
```

#### Q96. What will happen if you attempt to call this function with checkConcatThreshold("a");?

```cpp
int checkConcatThreshold(string a, string b) {
    return (a + b).length () > 120;
}
```

- [ ] A compilation warning will occur and the second argument will be given a default value of b.
- [ ] A compilation warning will occur and the second argument will be given a default value of the empty string.
- [x] A compilation error will occur.
- [ ] No compilation errors will occur and no compilation warnings will occur.

#### Q97. You need to define a C++ lambda function. You want the function to have access to only the variables that are local to it. The function should receive a single parameter, and a name, and construct a simple greeting. How will you achieve this?

- [ ] A

```cpp
auto myVeryFirstLambda = [=] (string name) {
        return "Hello " + name + "!";
    };
```

- [ ] B

```cpp
myVeryFirstLambda = [&] (string name) {
        return "Hello " + name + "!";
    };
```

- [x] C

```cpp
auto myVeryFirstLambda = [] (string name) {
        return "Hello " + name + "!";
    };
```

- [ ] D

```cpp
myVeryFirstLambda = [] (string name) {
        return "Hello " + name + "!";
    };
```

[Reference](https://docs.microsoft.com/en-us/cpp/cpp/lambda-expressions-in-cpp?view=msvc-160)

#### Q98. What is the value of X after running this code?

```cpp
int x=10, a=-3;
X+=a;
```

- [ ] -3
- [x] 7
- [ ] 13
- [ ] 3

**Explanation :** `+=` means increasing value. So `x += a` is equivalent to `x = x + a`

#### Q99. Once you are done writing to a file, what method will you call on the `ofstream` to notify the operating system?

- [ ] printout()
- [x] close()
- [ ] destroy()
- [ ] flush()

#### Q100. Which choice is not a C++ keyword?

- [ ] static_assert
- [ ] reinterpret_cast
- [x] comPl
- [ ] alignas

#### Q101. The size_in_bits function seems to take any type of parameter. This can be done by overloading the function, or by letting the compiler take care of it by writing a template. Which choice is an implementation of that template?

```cpp
int main()
{
cout « size_in_bits(21) « endl;
cout « size_in_bits('f') « endl;
cout « size_in_bits(32.1f) « endl;
cout « size_in_bits(32.1) « endl;
return 0;
}
```

- [x] A

```cpp
template <typename T>
size_t size_in_bits(const T& a){
return sizeof(a)*8;
}
```

- [ ] B

```cpp
template size_t size_in_bits(const {int,float,double,char,long}& a){
return sizeof(a)*8;
}
```

- [x] C

```cpp
template <typename T {int,float,double,char,long>
size_t size_in_bits(const T& a){
return sizeof(a)*8;
}
```

- [ ] D

```cpp
size_t size_in_bits(void * a){
return sizeof(a)*8;
}
```

#### Q102. To use the keyboard as input the iostream library is included. To read input from files as input what library is needed?

- [x] fstream
- [ ] cstdlib
- [ ] filestream
- [ ] iostream

#### Q103. What will this object-oriented program print?

```cpp
#include <iostream>
#include <string>
using namespace std;

class Vehicle {
public:
	string fuel = "none";
};

class MotorizedVehicle : public Vehicle {
public:
	string fuel = "fossil";
};

class NextgenMotorizedVehicle : public MotorizedVehicle {
public:
	string fuel = "hydrogen";
};

int main() {
	MotorizedVehicle aCar;
	cout << aCar.fuel;
	return 0;
}
```

- [x] fossil
- [ ] fossil none
- [ ] hydrogen
- [ ] none

#### Q104. The program below is handling a stack container. What is the output of running the program?

```cpp
#include <iostream>
#include <stack>

int main()
{
	std::stack<int> stack;
	stack.push(1);
	stack.push(2);
	stack.push(3);

	stack.pop();

	stack.push(4);

	stack.top();
	stack.pop();

	std::cout << stack.top();
}
```

- [ ] 1
- [x] 2
- [ ] 3
- [ ] 4

#Detailed explanation:

Now here we are supposed to implement a stack data structure that follows the **FILO** or (First IN Last Out) principle,
_stack.push()_ -> pushes an element into the from the end array.
_stack.pop()_ -> removes an element from the end of the array.
_stack.top()_ -> Just gives us the topmost element of the array.
Now following the sequences of push and pop: **[1,2,3]** then pop function is used,
The newly formed array is: **[1,2,4]** then the top is used to retrieve the topmost element '4' then again the pop function is used which removes 4.
thus, the resulting array is: 1,2.
Then it prints the topmost element (ie: 2).

#### Q105. Which choice is a valid way to overload the ternary conditional operator?

- [ ] `void& operator ?:(const bool cond, const void& iftrue, const void& iffalse);`
- [x] `The ternary operator is not overloadable.`
- [ ] `void& operator conditional(const bool cond, const void& iftrue, const void& iffalse);`
- [ ] `void* operator ?:(const bool cond, const void* iftrue, const void* iffalse);`

[Reference](https://en.cppreference.com/w/cpp/language/operators)

#### Q106. Which class hierarchy represents an example of multilevel inheritance?

- [ ] In the same program, at different points, a given class derives individually from more than one different class.
- [ ] A first-class derives directly, at the same time, from a second and third class.
- [x] In the same program, at different points, a given class derives individually from more than two different classes.
- [ ] A first classderives from a second class, and that second class is already derived from a third class

#### Q107. Which of the following is the correct syntax to print the message in C++ language?

- [ ] Out <<"Hello world!
- [ ] Cout << Hello world! ;
- [x] cout <<"Hello world!";
- [ ] None of the above

[Reference](https://en.cppreference.com/w/cpp/io/cout)

#### Q108. Consider the following program. What will be the output/error?

```cpp
#include<iostream>
#include<algorithm>
#include<string.h>
using namespace std;
bool compare(char c1, char c2){
return tolower(c1) > tolower(c2);    //LINE-1
}
int main(){
char arr1[20] = "C++ Program", arr2[20] = "C Program";
cout << lexicographical_compare(arr1, arr1+strlen(arr1), arr2, arr2+strlen(arr2),
compare);
return 0;
}
```

- [x] 1
- [ ] 0
- [ ] -1
- [ ] Compilation Error: function is not defined

[Reference](https://www.geeksforgeeks.org/tolower-function-in-cpp/)

#### Q109. Consider the following code segment. Fill in the blank at LINE-1 so that the program will print "not found"?

```cpp
#include <iostream>
#include <algorithm>
using namespace std;
int main() {
int data[] = {1,2,3,4,5};
int key = 5;
if(binary_search(__________))    //LINE-1
cout << "found";
else
cout << "not found";
return 0;
}
```

- [ ] &data[0], &data[5], key
- [ ] data, data+5, key
- [x] &data[0], &data[4], key
- [x] data+1, data+4, key

[Reference](https://www.geeksforgeeks.org/binary-search-algorithms-the-c-standard-template-library-stl/)

#### Q110. Consider the following code segment. What will be the output?

```cpp
#include <iostream>
#include <algorithm>
using namespace std;
int main () {
int data[] = {50, 30, 40, 10, 20};
sort (&data[1], &data[4]);
for (int i = 0; i < 5; i++)
cout << data[i] << " ";
return 0;
}
```

- [ ] 10 20 30 40 50
- [ ] 10 30 40 50 20
- [x] 50 10 30 40 20
- [ ] 50 10 20 30 40

[Reference](https://cplusplus.com/reference/algorithm/sort/)

#### Q111. Consider the following code segment. What will be the output?

```cpp
#include <iostream>
#include <algorithm>
using namespace std;
int main() {
int element[5];
for(int i = 1; i <= 5; i++)
*(element + i - 1) = i * 5;
rotate(element, element + 4, element + 5);
rotate(element, element + 1, element + 4);
for (int i = 0; i < 5; ++i)
cout << element[i] << " ";
return 0;
}
```

- [ ] 5 10 15 20 25
- [x] 5 10 15 25 20
- [ ] 20 10 15 25 5
- [ ] 25 5 10 15 20

[Reference](https://en.cppreference.com/w/cpp/algorithm/rotate)

#### Q112. Consider the following code segment. What will be the output?

```cpp
#include <iostream>
#include <vector>
using namespace std;
int main() {
const int size = 3, c = 65;
vector<char> vc(size, ’A’);
for (int i = 1; i <= 2; i++)
vc.push_back(65 + i);
vc.resize(10, 90);
vc.resize(8);
for (int i = 0; i < vc.size(); i++)
cout << vc[i] << " ";
return 0;
}
```

- [x] A A A B C Z Z Z
- [ ] A A B B C Z Z Z
- [ ] A A A B C Z Z
- [ ] A A A B C Z Z Z Z

[Reference](https://en.cppreference.com/w/cpp/container/vector)

#### Q113. Consider the following code segment. Choose the appropriate option to fill in the blank at LINE-1, such that the output of the code would be: a C++ Program.

```cpp
#include <iostream>
#include <string>
using namespace std;
int main(void) {
string s1 = "C++ ";
string s2 = "Program";
__________________;    //LINE-1
cout << s1;
return 0;
}
```

- [x] s1 += s2
- [ ] strcat(s1, s2)
- [x] s1.append(s2)
- [ ] s1.insert(s2)

[Reference](https://www.geeksforgeeks.org/stdstringappend-in-c/)

#### Q114. Consider the following code segment. Fill in the blank at LINE-1 such that the output is 5 2 3 4 5

```cpp
#include <iostream>
#include <algorithm>
using namespace std;
int main() {
int data[] = { 1, 2, 3, 4, 5 };
for (int i = 0; i < 1; i++) {
int j = data[i];
replace(data, data + 5, j, *(_________________));    //LINE-1
}
for (int i = 0; i < 5; ++i)
cout << data[i] << " ";
return 0;
}
```

- [x] data + 4 - i
- [ ] data + 5 - i
- [ ] data + i - 4
- [ ] data + i - 5

[Reference](https://www.geeksforgeeks.org/stdstringreplace-stdstringreplace_if-c/)

#### Q115. Consider the following code segment. What will be the output?

```cpp
#include <iostream>
#include <cstring>
#include <stack>
using namespace std;
int main(){
char str[10] = "123456789";
stack<char> s1, s2;
int i;
for(i = 0; i < strlen(str)/2; i++)
s1.push(str[i]);
for(i=i-1; i < strlen(str); i++)
s2.push(str[i]);
while (!s1.empty()) {
s2.push(s1.top()); s1.pop();
}
while (!s2.empty()) {
cout << s2.top(); s2.pop();
}
return 0;
}
```

- [x] 1234987654
- [ ] 123498765
- [ ] 1234897654
- [ ] 123459876

[Reference](https://en.cppreference.com/w/cpp/container/stack)

#### Q116. Consider the following code segment. Which statement/statements is/are correct?

```cpp
int i = 5;
const int *p = &i;
int * const q = &i;
int const *r = &i;
int const * const s = &i;
*p = 10; //STMT-1
*q = 10; //STMT-2
*r = 10; //STMT-3
*s = 10; //STMT-4
```

- [ ] STMT-1
- [x] STMT-2
- [ ] STMT-3
- [ ] STMT-4

[Reference](https://www.geeksforgeeks.org/const-keyword-in-cpp/)

#### Q117. Consider the following program. What will be the output/error(s)?

```cpp
#include <iostream>
using namespace std;
char add(char c1 = ’a’) { return c1; }
char add(char c1 = ’a’, char c2 = ’b’) { return c1 + c2 - ’a’;}
char add(char c1 = ’a’, int d1 = 100){ return c1 + d1 - ’a’; }
char add(char c1 = ’a’, char c2 = ’b’, char c3) { return c1 + c2 + c3 - ’a’; }
int main() {
char c = add(’o’, ’k’);
cout << c << endl;
return 0;
}
```

- [ ] y
- [ ] z
- [x] Compilation Error: default argument missing for "char add(char, char, char)"
- [x] Compilation Error: call of overload "add(char, char)" is ambiguous

[Reference](https://learn.microsoft.com/en-us/cpp/cpp/function-overloading?view=msvc-170)

#### Q118. Consider the following code segment. What will be the output?

```cpp
#include <iostream>
using namespace std;
#define SQR(x) (x)*(x)
int main() {
int a=3;
cout << SQR(a++) << endl;
return 0;
}
```

- [x] 12
- [ ] 25
- [ ] 9
- [ ] 16

[Reference](https://www.geeksforgeeks.org/output-of-the-program-use-macros-carefully/)

#### Q119. Consider the following code segment. Which line/s will give you an error?

```cpp
#include<iostream>
#define X 1
using namespace std;
int main(){
int i;
const int i1 = 2;
const int i2 = i1; //LINE-1
i2 = X;
i = i1;
i1 = i;
return 0;
//LINE-2
//LINE-3
//LINE-4
}
```

- [ ] LINE-1
- [x] LINE-2
- [ ] LINE-3
- [x] LINE-4

#### Q120. Consider the following code segment. What will be the output/error?

```cpp
#include<iostream>
using namespace std;
int main(){
int a = 5;
int &b = a+1;
a = a*b;
cout << a << " " << b;
return 0;
}
```

- [ ] 36
- [ ] 30
- [ ] 25
- [x] Compilation Error: invalid initialization of non-const reference

#Detailed explanation:
The error is occurring because it is trying to create a reference to a temporary value. In the line int &b = a+1; we are attempting to create a reference b to the result of the expression a + 1, which is a temporary value. References must be bound to an actual object, not a temporary value or an expression that does not have a memory location.

#### Q121. Consider the following code segment. What will be the output?

```cpp
#include <iostream>
using namespace std;
int& func(int& i) {     //LINE-1
return i = i+5;
}
int main() {
int x = 1, y = 2;
int& z = func(x);
cout << x << " " << z << " ";
func(x) = y;
cout << x << " " << z;
return 0;
}
```

- [x] 6 6 2 2
- [ ] 6 6 7 7
- [ ] 1 1 2 2
- [ ] 1 1 7 7

[Reference](https://www.ibm.com/docs/en/zos/2.4.0?topic=calls-pass-by-reference-c-only)

#### Q122. Consider the following code segment. Choose the appropriate option to fill in the blanks at LINE-1, such that the output of the code would be: 300 20000.

```cpp
#include <iostream>
using namespace std;
void compute(int n1, int n2, ________, ________){ //LINE-1
n3 = n1 + n2;
*n4 = n1 * n2;
}
int main(){
int a = 100, b = 200, c = 0, d = 0;
compute(a, b, c, &d); //LINE-2
cout << c << ", ";
cout << d;
return 0;
}
```

- [ ] int n3, int\* n4
- [x] int& n3, int \*n4
- [ ] int* n3, int* n4
- [ ] int& n3, int& n4

#### Q123. Consider the following code segment. What will be the output/error?

```cpp
#include <iostream>
using namespace std;
int main() {
int a = 2, *b;
*b = 5;
int * const ptr;    // LINE-1
// LINE-2
ptr = b;
cout << *ptr;
return 0;
}
```

- [ ] <garbage value>
- [ ] 5
- [x] Compilation Error at LINE-1: uninitialized const ’ptr’
- [x] Compilation Error at LINE-2: assignment of read-only variable ’ptr’

#### Q124. Consider the following code segment. What will be the output/error?

```cpp
#include <iostream>
using namespace std;
void fun(int a = 5) { cout << a << endl; }
//LINE-1
int fun(int x = 10) { cout << x << endl; return 0; }    //LINE-2
int main() {
fun();
return 0;
}
```

- [ ] 5
- [ ] 10
- [ ] 5
- [x] Compilation error at LINE-2: ambiguating new declaration of ’int fun(int)’

#### Q125. Consider the following code segment. Fill in the blank at LINE-1 such that the program will print 5 + i3

```cpp
#include<iostream>
using namespace std;
struct complex{
int re, im;
void show(){ cout << re << " + i" << im; }
};
______________________________________{ //Line-1
c2.re = c1.re+c2.re;
c2.im = c1.im+c2.im;
return c2;
}
int main(){
struct complex c1={2,5},c2{3,-2};
struct complex t = c1 + c2;
t.show();
return 0;
}
```

- [x] complex operator+(complex &c1, complex &c2)
- [ ] complex operator+(const complex &c1, const complex &c2)
- [ ] operator+(complex &c1, complex &c2)
- [ ] complex +(complex &c1, complex &c2)

[Reference](https://www.w3schools.com/cpp/cpp_structs.asp)

#### Q126. Consider the following program. Which line/s will generate an error?

```cpp
#include<iostream>
using namespace std;
class myClass{
int pra = 5;
public:
int pub = 10;
void set_pr(int x){ pra = x; }
void set_pu(int x){ pub = x; }
};
int main(){
myClass m;
int a, b;
a = m.pra; //LINE-1
b = m.pub; //LINE-2
m.set_pr(100); //LINE-3
m.set_pu(200); //LINE-4
return 0;
}
```

- [x] LINE-1
- [ ] LINE-2
- [ ] LINE-3
- [ ] LINE-4

[Reference](https://stackoverflow.com/questions/4855422/c-classes-public-private-and-protected)

#### Q127. Consider the following class. Fill in the blanks with proper access specifiers so that member y can be accessed from outside of the class but member x cannot be accessed.

```cpp
class Test{
________:
int x;
________:
int y;
/* Some more code */
};
```

- [ ] public, public
- [ ] public, private
- [ ] private, public
- [x] private, private

#### Q128. Which C++ Standard did add in-class default member initializers?

- [ ] C++98
- [x] C++11
- [ ] C++14
- [ ] C++17.

#### Q129. Can you use auto type deduction for non-static data members?

- [ ] Yes, since C++11
- [x] No
- [ ] Yes, since C++20

#### Q130. Do you need to define a static inline data member in a cpp file?

- [x] No, the definition happens at the same place where a static inline member is declared.
- [ ] Yes, the compiler needs the definition in a cpp file.
- [ ] Yes, the compiler needs a definition in all translation units that use this variable.

[Reference](https://en.cppreference.com/w/cpp/language/bit_field)

#### Q131. What's the output of the following code:

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
- [x] Output is: 1, 42

#### Q132. Can a static inline variable be non-constant?

- [x] Yes, it's just a regular variable.
- [ ] No, inline variables must be constant.

#### Q133. Consider the following code:

```cpp
struct C {
    C(int x) : a(x) { }
    int a { 10 };
    int b { 42 };
};
C c(0);

```

- [ ] C::a is initialized twice. The first time, it's initialized with 10, and then the second time with 0 in the constructor.
- [x] C::a is initialized only once with 0 in the constructor.
- [ ] The code doesn't compile because the compiler cannot decide how to initialize the C::a member.
- [ ] 2 bytes

#### Q134. What happens when you throw an exception from a constructor?

- [ ] The object is considered "created" so it will follow the regular lifetime of an object.
- [x] The object is considered "partially created," and thus, the compiler won't call its destructor.
- [ ] he compiler calls std::terminate as you cannot throw exceptions from constructors.

#### Q135. What happens when you compile this code?

```cpp
struct Point { int x; int y; };
Point pt {.y = 10, .x = 11 };
std::cout << pt.x << ", " << pt.y;
```

- [x] The code doesn't compile. Designators have to be in the same order as the data members in the Point class.
- [ ] The code compiles and prints 11, 10.
- [ ] The code compiles and prints 10, 11.

#### Q136. Will this code work in C++11?

```cpp
struct User { std::string name = "unknown"; unsigned age { 0 }; };
User u { "John", 101 };
```

- [ ] Yes, the code compiles in C++11 mode.
- [x] The code compiles starting with C++14 mode.
- [ ] The code doesn't compile even in C++20.

#### Q137. Assume you have a std::map<string, int> m;. Select the single true statement about the following loop:

```cpp
for (const pair<string, int>& elem : m)
```

- [x] A The loop properly iterates over the map, creating no extra copies.

- [ ] B The loop will create a copy of each element in the map as the type of elem mismatches.

- [ ] C The code won't compile as a const pair cannot bind to a map.

#### Q138. Identify the correct extension of the user-defined header file in C++.

- [ ] .cpp
- [ ] .hg
- [x] .h
- [ ] .hf

#### Q139.Identify the incorrect constructor type.

```cpp
auto x = 4000.22;
```

- [x] Friend Constructor
- [ ] Default Constructor
- [ ] Parameterised Constructor
- [ ] CopyConstructor

#### Q140.Which of the following data types is supported in C++ but not in C?

- [x] bool
- [ ] int
- [ ] double
- [ ] float

[Reference]: https://stackoverflow.com/questions/1608318/is-bool-a-native-c-type

#### Q141. Identify the correct syntax for declaring arrays in C++.

- [x] int arr[10]
- [ ] array arr[10]
- [ ] array{10}
- [ ] int arr

[Reference]: (https://en.cppreference.com/w/cpp/language/array)

#### Q142.Size of wchat_t is.

- [ ] 2
- [ ] 4
- [ ] 2 or 4
- [x] Depends on the number of bits in the system

#### Q143.Which of the following loops is best when we know the number of iterations?

- [ ] while
- [x] for
- [ ] do
- [ ] All of the above

#### Q144.Which keyword is used to define the macros in C++?

- [ ] #macro
- [x] #define
- [ ] macro
- [ ] keyword

#### Q145.Which of the following operators should be preferred to overload as a global function rather than a member method?

- [ ] Postfix ++
- [x] Comparison Operator
- [ ] Insertion Operator <<
- [ ] Prefix++

#### Q146.How can we restrict the dynamic allocation of objects of a class using new?

- [ ] By overloading new operator
- [ ] By making an empty private new operator.
- [x] By making an empty private new and new[] operators
- [ ] By overloading new operators and new[] operators

#### Q147.What is the time complexity of the below code?

```cpp
for(int i=0;i<n;i++){
   for(int j=0;j<n;j++){
       cout<<"hello";
    }
}
```

- [ ] O(n^3)
- [x] O(n^2)
- [ ] O(n)
- [ ] O(1)

[Reference]: https://medium.com/enjoy-algorithm/analysis-of-loop-in-programming-cc9a644ef8cd#:~:text=At%20each%20step%20of%20the%20iteration%2C%20the%20nested%20loop%20is,%20%3D%20O(n%C2%B2).

#### Q148.What is the output of the code given below?

```cpp
int a=10;
int k=++a;
int m=a++;
cout<<k+m;
```

- [ ] 20
- [ ] 21
- [x] 22
- [ ] 23

Both **++a** and **a++** increase the value of a by 1 (ie: 11) and hence k+m becomes 22.

#### Q149. Which C++ construct is used for exception handling?

- [x] try-catch
- [ ] if-else
- [ ] for loop
- [ ] switch-case

#### Q150. What is the purpose of the `break` statement in a loop in C++?

- [ ] Exit the program
- [ ] Skip the current iteration and continue with the next one
- [x] Terminate the loop
- [ ] Return a value

[Reference]: (https://www.tutorialspoint.com/cprogramming/c_break_statement.htm)

#### Q151. In C++, what is the purpose of the `const` keyword when used with a variable?

- [x] It makes the variable immutable
- [ ] It changes the data type
- [ ] It defines a constant function
- [ ] It makes the variable a pointer

#### Q152. Which is more effective while calling the C++ functions??

- [x] Call by reference
- [ ] Call by value
- [ ] Call by pointer
- [ ] Call by object

[Reference]: (https://www.algbly.com/More/MCQs/Cpp-mcq/Cpp-functions.html)

#### Q153. What will be the output of the following C++ program?

```cpp
#include <iostream>
using namespace std;
class A{
public:
	A(){
		cout<<"Constructor called\n";
	   }
	~A(){
		cout<<"Destructor called\n";
	    }
};
int main(int argc, char const *argv[])
{
	A *a = new A[5];
	delete[] a;
	return 0;
}
```

- [ ] Segmentation fault
- [x] “Constructor called” five times and then “Destructor called” five times
- [ ] “Constructor called” five times and then “Destructor called” once
- [ ] Error

#### Q.153 What is the output of this code?

```c++
printf("1/2 = %f",(float)(1/2));
```

- [ ] 1/2 = 0.499999
- [ ] 1/2 = 0
- [x] 1/2 = 0.000000
- [ ] 1/2 = 0.5

#### Q.154 Which choice is _not_ related to declaring the member variable count as static in my_class?

```cpp
class my_class{
    public: static int count;
}
```

- [ ] All objects that try to access their count member variable actually refer to the only class-bound static count variable.
- [ ] The variable exists even when no objects of the class have been defined, so it can be modified at any point in the source code.
- [ ] The variable cannot be modified by any part of the code in the same application or thread. However, other threads may modify it.
- [ ] The variable is allocated only once, regardless of how many objects are instantiated, because it is bound to the class itself, not its instances.

#### Q11. What is the purpose of the `constexpr` keyword in C++?

- Ref(https://learn.microsoft.com/en-us/cpp/cpp/constexpr-cpp?view=msvc-170#:~:text=constexpr%20indicates%20that%20the%20value,template%20arguments%20and%20array%20declarations.)

- [ ] It is used to define constants in C++.
- [ ] `constexpr` is used to specify that a variable is a constant pointer.
- [x] `constexpr` is used to indicate that an expression can be evaluated at compile-time, making it suitable for use in constant expressions.
- [ ] It is a keyword used to create asynchronous functions.


#### Q16. What is a template metaprogram in C++?

- Ref(https://www.geeksforgeeks.org/template-metaprogramming-in-c/)

- [ ] A template metaprogram is a high-level programming language.
- [ ] It refers to metaprogramming that uses templates in C++.
- [ ] It's a type of user interface design pattern.
- [x] A template metaprogram is a compile-time computation, where templates and template specialization are used to perform computations at compile time.
