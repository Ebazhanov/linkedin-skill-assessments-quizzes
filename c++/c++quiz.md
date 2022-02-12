## C++

#### Q1. What is printed from this code?

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
Using namespace std;
```

- [ ] The compiled code is always bigger because of all of the imported symbols.
- [x] If the code uses a function defined in two different libraries with the same prototype but possibly with different implementations, there will be a compilation error due to ambiguity.
- [ ] It automatically includes all header files in the standard library (cstdint, cstdlib, cstdio, iostream, etc).
- [ ] It causes the compiler to enforce the exclusive inclusion of header files belonging to the standard library, generating compilation error when a different header file is included.

[Reference](https://www.geeksforgeeks.org/using-namespace-std-considered-bad-practice/)

#### Q3. What is the smallest size a variable of the type child_t may occupy in memory?

```cpp
typedef struct{
    unsigned int  age    : 4;
    unsigned char gender : 1;
    unsigned int  size   : 2;
}child_t;
```

- [x] 7 bits.
- [ ] 25 bytes.
- [ ] 1 bit.
- [ ] 1 byte.

[Reference](https://en.cppreference.com/w/cpp/language/bit_field)

#### Q4. Which of the following shows the contents of vector v1 and v2 after running this code?

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

- [ ] While pointers are variable that hold memory address, iterators are generic functions used to traverse containers. These function allows the programmer to implement read and write code as the container is traversed.
- [x] Incrementing an iterator always means access the next element in the container(if any), no matter the container. Incrementing the pointer means pointing to the next element in memory, not always the next element.
- [ ] Pointers are variables that hold memory address where as iterator are unsigned integers that refers to offsets in arrays.
- [ ] All iterator are implemented with pointers so all iterators are pointers but not all pointers are iterators.

[Reference](https://stackoverflow.com/a/31128162)

#### Q6. What's a benefit of declaring the parameter as a const reference instead of declaring it as a regular object?

```cpp
int median(const my_array& a);
```

- [ ] The argument is passed as a reference, so the function receives a copy that can be modified without affecting the original value.
- [x] The argument is passed as a reference, so if the passed my_array object is large, the program will require less time and memory.
- [ ] Actually objects can't be passed as regular variables because they require a constructor call. Therefore a const reference is the only way to pass class instances to functions.
- [ ] There are no benefits because a reference and an object are treated as the same thing.

[Reference](https://stackoverflow.com/a/2627179/10773894)

#### Q7. What's the storage occupied by u1?

```cpp
union {
    unit16_t a;
    unit32_t b;
    int8_t c;
} u1;
```

- [x] 4 bytes
- [ ] 7 bytes
- [ ] 8 bytes
- [ ] 2 bytes

[Reference](https://en.cppreference.com/w/cpp/language/union)

#### Q8. Which of the following operators is overloadable?

- [ ] `?:`
- [x] `new`
- [ ] `::`
- [ ] `.`

[Reference](https://www.tutorialspoint.com/operators-that-cannot-be-overloaded-in-cplusplus)

#### Q9. Which of the following shows the contents of vector pointed by v1 and v2 after running this code?

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

#### Q10. Which of the following is not a difference between a class and a struct?

- [ ] Because structs are part of the C programming language, there are some complexity between C and C++ structs. This is not the case with classes.
- [x] Classes may have member functions; structs are private.
- [ ] The default access specifier for members of struct is public, whereas for member of class, it is private.
- [ ] Template type parameters can be declared with classes, but not with the struct keyword.

[Reference](https://www.fluentcpp.com/2017/06/13/the-real-difference-between-struct-class/)

#### Q11. Suppose you need to keep a data struct with permission to access some resource based on the days of the week, but you can't use a bool variable for each day. You need to use one bit per day of the week. Which of the following is a correct implementation of a structure with bit fields for this application?

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

_NOTE_: Correct syntax is that each variable size is 1 bit. `bit` is not a type in C++. [Reference](https://en.cppreference.com/w/cpp/language/bit_field)

#### Q12. What is an lvalue?

- [ ] It's a constant expression, meaning an expression composed of constants and operations.
- [x] It's an expression that represents an object with an address.
- [ ] It's an expression suitable for the left-hand side operand in a binary operation.
- [ ] It's a location value, meaning a memory address suitable for assigning to a pointer or reference.

#### Q13. What does auto type specifier do in this line of code (since C++11)?

```cpp
auto x = 4000.22;
```

- [x] It specifies that the type of x will be deduced from the initializer - in this case, double.
- [ ] It specifies that the type of x is automatic meaning that if can be assigned different types of data throughout the program.
- [ ] It specifies that x is a variable with automatic storage duration.
- [ ] It specifies that more memory will be allocated for x in case it needs more space, avoiding loss of data due to overflow.

#### Q14. A class template is a **\_**?

- [x] class written with the generic programming paradigm, specifying behavior in terms of type parameter rather than specific type.
- [ ] blank superclass intended for inheritance and polymorphism.
- [ ] lass that only consists of member variable, with no constructor, destructor nor member functions.
- [ ] skeleton source code for a class where the programmer has to fill in specific parts to define the data types and algorithms used.

[Reference](https://www.mygreatlearning.com/blog/templates-in-cpp/)

#### Q15. What is the ternary operator equivalent to this code snippet?

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

#### Q16. What is the output of this code?

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

#### Q17. What is the meaning of the two parts specified between parentheses in a range-based for loop, separated by a colon?

- [x] The first is a variable declaration that will hold an element in a sequence. The second is the sequence to traverse.
- [ ] The first is an iterator, and the second is the increment value to be added to the iterator.
- [ ] The first is the iterating variable. The second is an `std::pair` that specifies the range (start and end) in which the variable will iterate.
- [ ] The first is a container object. The second is an `std::pair` that specifies the range (start and end) in which the elements will be accessed within the loop.

#### Q18. What is the output of this piece of code?

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

#### Q19. What results from executing this code snippet?

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

#### Q23. What is printed from this code?

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

#### Q24. What is true about the variable named `ptr`?

```cpp
void *ptr;
```

- [ ] It is a pointer initialized at NULL.
- [ ] It is a pointer to a void function.
- [ ] That declaration causes a compiler error, as pointers must specify a type.
- [x] It is a pointer to a value with no specific type, so it may be cast to point to any type.

[Reference](https://en.cppreference.com/w/cpp/language/pointer)

#### Q25. What is the output of this code?

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

#### Q28. What is the value of `x` after running this code?

```cpp
int x=10, a=-3;
x=+a;
```

- [ ] 3
- [ ] 7
- [x] -3
- [ ] 13

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
- [x] It is the pointer to member operator, and it allows you to access a member of an object through a pointer to that specific class member.
- [ ] It is the member access with address of operator, which returns the address of a class or struct member.
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

#### Q34. What is the output of this code?

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

#### Q35. How can C++ code call a C function?

- [ ] by simply calling the C code
- [ ] there is no way for C++ to call a C function
- [x] by using extern "C"
- [ ] by importing the source C code

#### Q36. Which choice is _not_ a valid type definition of a structure that contains x and y coordinates as integers, and that can be used exactly as shown for the variable named `center`?

```
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
- [ ] It cherry picks library.h for the declarations and definitions of all data and functions used in the remainder of the source file main.cpp, finally replacing the `#include` directive by those declarations and definitions.
- [ ] It informs the linker that some functions or data used in the source file main.cpp are contained in library.h, so that they can be called in run time. This is also known as dynamic linking.
- [x] It causes the replacement of the `#include` directive by the entire contents of the source file library.h. This is similar to a Copy-Paste operation of library.h into main.cpp.

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

- [ ] There's nothing wrong with it.
- [ ] An `std::vector` cannot contain more `std::vector` containers as its elements.
- [ ] The correct syntax should be: `std::vector[std::vector[int]] thematrix;`
- [x] `>>` is parsed as the shift-right operator, and thus results in a compile error.

#### Q42. What is the statement below equivalent to?

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

#### Q44. What is the result from executing this code snippet?

```cpp
bool x=true, y=false;
if(~x || y){
    /*part A*/
}
else{
    /*part B*/
}
```

- [ ] Part A executes because the expression `(~x || y)` always results in true if `y==false`.
- [ ] Part B executes because the statement `(~x || y)` is invalid, thus false.
- [ ] Part A executes because `~x` is not zero, meaning true.
- [x] Part B executes because `~x` is false and `y` is false, thus the `OR` operation evaluates as false.

#### Q45. What would be the output of this code?

```cpp
int32_t nums[3]={2,4,3};
std::cout << ( nums[0] << nums[1] << nums[2] );
```

- [ ] The output is the addresses of `nums[0]`, `nums[1]`, and `nums[2]`, in that order, with no spaces.
- [x] `256`
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

#### Q47. Which of the following STL classes is the best fit for implementing a phonebook? Suppose each entry contains a name and a phone number, with no duplicates, and you want to have lookup by name.

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

#### Q49. Which of the following is _not_ a consequence of declaring the member variable count of my_class as static?

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

#### Q51. What is the output of this piece of code?

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

#### Q52. What is an appropriate way of removing `my_object` as shown below?

```cpp
my_class *my_object = new my_class();
```

- [x] `delete(my_object);`
- [ ] `free(my_object);`
- [ ] The garbage collector will destroy the object eventually.
- [ ] Exiting the scope will destroy the object.

#### Q53. What is the correct way to call the `count` member function for the object pointer called `grades`?

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

#### Q54. What would be the output of this code?

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

#### Q55. Does this code cause a compiler error? If so, why, and if not, what is `child_t`?

```cpp
typedef struct{
    unsigned int  age    : 4;
    unsigned char gender : 1;
    char                 : 0;
    unsigned int  size   : 2;
}child_t;
```

- [ ] Yes, it causes a compiler error because the colon character is not allowed in struct definitions.
- [x] and `child_t` is a type defined as a structure with bit fields. It has 4 bits for age and 1 bit for gender in the first byte, and 2 bits for size in the second byte.
- [ ] Yes, it causes a compiler error because there is an unnamed field.
- [ ] Yes, it causes a compiler error because one field is defined as having a size of 0.

[Reference](https://en.cppreference.com/w/cpp/language/bit_field)

#### Q56. What is this expression equivalent to?

```cpp
A->B->C->D
```

- [ ] `A.B.C.D`
- [ ] `*A.*B.*C.*D`
- [ ] `&A.&B.&C.&D`
- [x] `*(*((*A).B).C).D`

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

#### Q61. What is the purpose of a destructor?

- [x] It allows the programmer to write the necessary code to free the resources acquired by the object prior to deleting the object itself.
- [ ] It deletes an object. One example of a destructor is the `delete()` function.
- [ ] It terminates a program. This may be achieved as a regular function call or as an exception.
- [ ] There are no destructors in C++.

#### Q62. Which STL class is the best fit for implementing a phonebook? Suppose each entry contains a name and a phone number, with no duplicates, and you want to have lookup by name.

- [ ] `std::priority_queue`
- [x] `std::map`
- [ ] `std::vector`
- [ ] `std::list`

#### Q63. What is the main difference between these two Functions?

```cpp
std::mutex::lock()
std::mutex::try_lock()
```

- [ ] `lock()` has a higher privilege over `try_lock()`. This means that you have a better chance of acquiring a mutex `with lock()`.
- [x] Both attempt to acquire a lock, but `lock()` blocks if the mutex is not available, whereas `try_lock()` returns whether the mutex is available or not.
- [ ] `lock()` enforces preemption, whereas `try_lock()` suggests preemption.
- [ ] If the mutex is not available, `try_lock()` returns with a corresponding code, whereas `lock()` snatches the mutex from the thread that currently has it.

[Reference](https://en.cppreference.com/w/cpp/thread/mutex/try_lock)

#### Q64. What is one benefit of declaring the parameter as a `const` reference instead of declaring it as a regular object?

```cpp
int median(const my_array& a)
```

- [ ] Actually, objects cannot be passed as regular variables, because they require a constructor call. Therefore, a `const` reference is the only way to pass class instances to functions.
- [ ] There are no benefits because a reference and an object are treated as the same thing.
- [x] The `const` qualifier Forbids the code to modify the argument, so the programmer can rest assured that the source object will remain unchanged.
- [ ] The argument is passed as a reference, so the Function receives a copy that can be modified without affecting the original variable.

Note: This one is similar to Q6, but focuses on the `const` keyword.

#### Q65. What is an include guard?

- [ ] a preprocessor directive that prevents inconsistent behaviors in lines that contain the #ifdef, #ifndef, or #elif directives
- [ ] a compiler option that prevents the user code from including additional libraries
- [x] a preprocessor statement that prevents a source file from being included more than once in a project
- [ ] a library that adds safety features such as mutexes, watchdog timers, and assertions to the project

#### Q66. What would be the correct declaration of a default constructor for a class named Sprite?

- [x]
  ```cpp
  public:
    		Sprite();
  ```
- [ ]
  ```cpp
  private:
    		void Sprite();
  ```
- [ ]
  ```cpp
  public:
    		void Sprite();
  ```
- [ ]
  ```cpp
     private:
    		Sprite();
  ```

#### Q67. What is the purpose of this line in a header file?

```cpp
#pragma once
```

- [ ] to restrict the use of its contents to only one source file
- [ ] to tell the compiler that only one variable can be instantiated from the classes or types contained in this header file
- [ ] to help the compiler finish faster by assuring that only one compiler pass is neccessary for the code included in this header file
- [x] to make the compiler parse that header file only once, even if it is included multiple times in the source

[reference here](https://en.cppreference.com/w/cpp/preprocessor/impl)

#### Q68. What is a variable of type double?

- [ ] a 2-tuple
- [ ] an integer number
- [x] a floating point number
- [ ] a string with more than 255 characters

[Reference](https://www.educba.com/c-plus-plus-double/)

#### Q69. Consider this function declaration of is_even, which takes in an integer and returns true if the argument is an even number and false otherwise. Which declarations are correct for overloaded versions of that function to support floating point numbers and string representations of numbers?

```cpp
bool is_even(int);
```

- [x] bool is_even(float f); bool is_even(char \*str);
- [ ] bool is_even(float f); bool is_even(char str);
- [ ] bool is_even_float(float f); bool is_even_str(char \*str);
- [ ] float is_even(float f); char *is_even(char *str);

#### Q70. Other than shifting bits to the left, what is the << oprator used for ?

- [ ] shifting characters to the left in a string.
- [x] inserting characters into an output stream like std::cout.
- [ ] comparing floating point numbers as less-than.
- [ ] assigning a variable to a reference.

#### Q71. Does this code cause a compiler error? If so, why, and if not, what is `child_t`?

```cpp
typedef struct{
    unsigned int  age    : 4;
    unsigned char gender : 1;
    char                 : 0;
    unsigned int  size   : 2;
}child_t;
```

- [ ] Yes, it causes a compiler error because the colon character is not allowed in struct definitions.
- [x] and `child_t` is a type defined as a structure with bit fields. It has 4 bits for age and 1 bit for gender in the first byte, and 2 bits for size in the second byte.
- [ ] Yes, it causes a compiler error because there is an unnamed field.
- [ ] Yes, it causes a compiler error because one field is defined as having a size of 0.

[Reference](https://en.cppreference.com/w/cpp/language/bit_field)

#### Q72. Which choice is a reason to specify the type of a pointer instead of using `void *`, which works as a pointer ro any type?

- [ ] The compiler needs the dara type to make sure that the pointer is not going to be used on illegal non-pointable types such as functions, labels, pointers, and reference.
- [ ] `void *` does not work for any type. The language does not allow assigning anything other than `void` to a pointer to `void *`.
- [x] The compiler needs the data type to know how much memory to allocate for the pointer, because different data types require different pointer lengths.
- [ ] Yes, it causes a compiler error because one field is defined as having a size of 0.

[Reference](https://stackoverflow.com/questions/9802585/why-is-the-data-type-needed-in-pointer-declarations)

### Q73. What is wrong with this piece of code?

```cpp
#include <iostream>
char str[20]'
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
