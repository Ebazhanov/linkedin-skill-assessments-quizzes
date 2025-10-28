## C (Programming Language)

#### Q1. Which Code sample will eventually cause the computer to run out of memory?

- [x] :

```c
while(1)
{
    char *smallString = (char *) malloc(10);
}
```

- [ ] :

```c
long long number = 1;
    while(1)
    number *= 2;
```

- [ ] :

```c
while(1)
{
    char hugeString[1000000L];
    memset(hugeString, 0, 1000000L);
}
```

- [ ] :

```c
while(1)
{
    long *bigArray = (long *) malloc(sizeof(long) * 1000);
    memset(bigArray, 1000000, 1000);

    (bigArray);
}
```

#### Q2. What will be the output of the code below?

```c
int f1 (int a, int b)
{
    if (a > b)
    {
        printf("A is greater than B\n");
        return 1;
    }
    else
    {
        printf("B is greater than A");
        return 0;
    }
}

main()
{
    if (f1(20,10) || f1(10,20))
        printf("C is fun!\n");
}
```

- [x] :

```
A is greater than B
C is fun!
```

- [ ] :

```
A is greater than B
B is greater than A
C is fun!
```

- [ ] :

```
A is greater than B
B is greater than A
```

- [ ] Nothing is printed on Screen

#### Q3. What is the name for calling a function inside the same function?

- [x] recursion
- [ ] subfunction
- [ ] inner call
- [ ] infinite loop

[Reference](https://www.cprogramming.com/tutorial/c/lesson16.html)

#### Q4. What does the declaration of variable c2 demonstrate?

```c
main(){
    char c1 ='a';
    char c2 = c1+10;
}
```

- [x] character arithmetic
- [ ] undefined assignment
- [ ] type conversion
- [ ] invalid declaration

[Reference](https://tutorialspoint.dev/language/c/character-arithmetic-c-c)

#### Q5. What is this declaration an example of?

```c
struct s {
    int i;
    struct s *s1;
    struct s *s2;
};
```

- [x] a node
- [ ] a linked list
- [ ] a stack
- [ ] a binary tree

#### Q6. Header files are listed using the preprocessing directive #include, and can have one of the following formats: #include &lt;fileA&gt; or #include "fileB". What is the difference between these two formats?

- [ ] The preprocessor will try to locate fileA in the same directory as the source file, and the fileB in a predetermined directory path.
- [ ] The preprocessor will try to locate fileA in the fixed system directory. It will try to locate fileB in the directory path designated by the -I option added to the command line while compiling the source code.
- [ ] The file using the fileA syntax must be system files, of unlimited number; fileB must be a user file at a maximum of one per source file.
- [x] The preprocessor will try to locate fileA in a predetermined directory path. It will try to locate fileB in the same directory as the source file along with a custom directory path.

[Reference](https://www.geeksforgeeks.org/difference-between-include-and-include-in-c-c-with-examples/#:~:text=The%20difference%20between%20the%20two,be%20included%20in%20the%20code.&text=%23include%20is%20for%20pre%2Ddefined%20header%20files.)

#### Q7. Using a for loop, how could you write a C code to count down from 10 to 1 and display each number on its own line?

- [ ] :

```c
for (int i = 0; i>=0, i--){
    printf("%d\n", i);
}//end of loop
```

- [ ] :

```c
int i;
for (i=1; i<=10; i++){
    printf("%d", i);
}
```

- [ ] :

```c
int i = 10;
while (i>0){
    printf("%d\n", i);
    i--;
}
```

- [x] :

```c
int i;
for (i= 10; i>0; i--){
    printf("%d\n", i);
}// end of loop
```

#### Q8. What is not one of the reserved words in standard C?

- [ ] volatile
- [x] typeof
- [ ] register
- [ ] typedef

[Reference](https://www.ibm.com/docs/en/adfz/developer-for-zos/14.2.0?topic=programs-c-reserved-keywords)

#### Q9. What does the program shown below return?

```c
int main(){
    int a=1, b=2, c=3, d=4;
    int x = a;
    if (a>b)
    if (b<c) x=b;
    else x=c;
    return(x);
}
```

- [x] 1
- [ ] 3
- [ ] 2
- [ ] 0

#### Q10. Using the Union declaration below, how many bytes of memory space will the data of this type occupy?

```c
union Cars {
    char make[20];
    char model[30];
    short year;
} car;
```

- [ ] 32
- [ ] 54
- [x] 30
- [ ] 52

#### Q11. In this code sample, what is not a problem for C compiler?

```c
main(){
    constant int PI = 3.14;
    printf("%f\n", pi);
}
```

- [x] The value of PI needs to be set to 3.141593, not 3.14
- [ ] The declaration of PI needs to say const, not constant.
- [ ] The data type of PI needs to be float, not int.
- [ ] The printf statement needs to use PI, not pi.

#### Q12. Which is the smallest program to compile and run without errors?

- [ ] main()
- [x] int main() {return 0;}
- [ ] main() { }
- [ ] main() { ; }

[Reference](https://www.beningo.com/150-the-wolrds-shortest-c-program/)

#### Q13. What is optional in a function declaration?

- [ ] data type of parameters
- [ ] return type of function
- [x] parameter names
- [ ] number of parameters

> **Explanation:**  
> In all modern C standards, parameter names in a function declaration are optional.  
> However, the meaning of an empty parameter list (`int f();`) differs by standard:
>
> - **Before C23:** Declares a function with an unspecified number of parameters (not a prototype).
> - **In C23:** Equivalent to `int f(void);` — declares a function that takes no parameters.
>
> [Reference](https://en.cppreference.com/w/c/language/function_declaration)

#### Q14. C treats all devices, such as the display and the keyboard, as files. Which file opens automatically when a program executes?

- [x] stdout
- [ ] stdio.h
- [ ] default.h
- [ ] string.h

#### Q15. In which segment does dynamic memory allocation take place?

- [ ] BSS Segment
- [ ] stack
- [x] heap
- [ ] data segment

[Reference](http://www.it.uc3m.es/pbasanta/asng/course_notes/dynamic_memory_heap_en.html#:~:text=The%20dynamic%20memory%20that%20is,reads%20a%20set%20of%20words.)

#### Q16. Which function do you use to deallocate memory?

- [ ] dalloc()
- [ ] dealloc()
- [ ] release()
- [x] free()

[Reference](https://devdocs.io/c/memory/free)

[Reference](https://www.tutorialspoint.com/c_standard_library/c_function_free.htm)

#### Q17. In C language what are the basic building blocks that are constructed together to write a program?

- [ ] keywords
- [ ] identifiers
- [x] tokens
- [ ] functions

[Reference](https://fresh2refresh.com/c-programming/c-tokens-identifiers-keywords/#:~:text=C%20tokens%20are%20the%20basic,are%20known%20as%20C%20tokens.)

#### Q18. When is memory for a variable allocated?

- [ ] during the assignment of the variable
- [ ] during the initialization of the variable
- [x] during the declaration of the variable
- [ ] during the definition of the variable

[Reference](https://www.codingame.com/playgrounds/14589/how-to-play-with-pointers-in-c/dynamic-memory-allocation#:~:text=When%20a%20variable%20is%20declared,allocation%20or%20dynamic%20memory%20allocation.)

#### Q19. C uses the call by value method to pass arguments to functions. How can you invoke the call by reference method?

- [x] by using pointers
- [ ] by declaring functions separately from defining them
- [ ] by using recursive functions
- [ ] by using global variables

[Reference](https://www.javatpoint.com/call-by-value-and-call-by-reference-in-c)

#### Q20. A union allows you to store different `___` in the same `___`.

- [ ] Objects; Structure
- [ ] Variables; Declaration
- [x] Data types; Memory space
- [ ] Arrays; Header file

#### Q21. What is the output of this program?

```c
main() {
    char c1='a' , c2='A';
    int i=c2-c1;
    printf("%d", i);
}
```

- [ ] 32
- [ ] Runtime error
- [x] -32
- [ ] 0

#### Q22. What is the difference between scanf() and sscanf() functions?

- [ ] The scanf() function reads data formatted as a string; The sscanf() function reads string input from the screen.
- [x] The scanf() function reads formatted data from the keyboard; The sscanf() function reads formatted input from a string.
- [ ] The scanf() function reads string data from the keyboard; The sscanf() function reads string data from a string.
- [ ] The scanf() function reads formatted data from a file; The sscanf() function reads input from a selected string

#### Q23. What is not a valid command with this declaration?

```c
char *string[20] = { "one", "two", "three"};
```

- [ ] `printf("%c", string[1][2]);`
- [x] `printf("%s", string[1][2]);`
- [ ] `printf("%s", string[1]);`
- [ ] `printf(string[1]);`

#### Q24. What is the expression player->name equivalent to?

- [ ] `player.name`
- [x] `(*player).name`
- [ ] `*player.name`
- [ ] `player.*name`

#### Q25. Which program will compile and run without errors?

- [ ] :

```c
main() {
    for(i=0; i<10; i++) ;
}
```

- [x] :

```c
main() {
int i=0;
    for(; i<10; i++) ;
}
```

- [ ] :

```c
main() {
    int i;
    for(i=0; i<j; i++) ;
}
```

- [ ] :

```c
main() {
int i;
    for (i= 10; i<10; i++)
}
```

#### Q26. What does this function call return?

```c
1 main() { float x = f1(10, 5); }
2 float f1(int a, int b) { return (a/b); }
```

- [ ] 2
- [ ] 2.000000
- [ ] a runtime error
- [x] a compiler error

#### Q27. What does this program create?

```c
#include <stdio.h>
int main() {
    int *p = NULL;
    return 0;
}
```

- [ ] a runtime error
- [x] a NULL pointer
- [ ] a compile error
- [ ] a void pointer

#### Q28. What is an alternative way to write the expression (\*x).y?

- [ ] There is no equivalent.
- [x] x->y
- [ ] \*x->y
- [ ] y->x

#### Q29. Compile time errors are static errors that can be found in the code.

- [x] in declarations and definitions
- [ ] in functions and expressions
- [ ] in syntax and semantics
- [ ] in objects and statements

#### Q30. File input and output (I/O) in C is heavily based on the way it is done `___`?

- [x] in Unix
- [ ] in C++
- [ ] in C#
- [ ] in DOS

#### Q31. What does the strcmp(str1, str2); function return?

- [x] 0 if str1 and str2 are the same, a negative number if str1 is less than str2, a positive number if str1 is greater than str2
- [ ] true (1) if str1 and str2 are the same, false (0) if str1 and str2 are not the same
- [ ] true (1) if str1 and str2 are the same, NULL if str1 and str2 are not the same
- [ ] 0 if str1 and str2 are the same, a negative number if str2 is less than str1, a positive number if str2 is greater than str1

#### Q32. What is the output of this program?

```c
int a=10, b=20;
int f1(a) { return(a*b); }
main() {
printf("%d", f1(5));
}
```

- [x] 100
- [ ] 200
- [ ] 5
- [ ] 50

#### Q33. Which is _not_ a correct way to declare a string variable?

- [ ] `char *string = "Hello World";`
- [x] `char string = "Hello World";`
- [ ] `char string[20] = {'H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd'};`
- [ ] `char string[] = "Hello World";`

#### Q34. Which choice is an include guard for the header file mylib.h?

- [ ] :

```c
#ifdef MYLIB_H
#undef MYLIB_H

// mylib.h content

#endif /* MYLIB_H */
```

- [x] :

```c
#ifndef MYLIB_H
#define MYLIB_H

// mylib.h content

#endif /* MYLIB_H */
```

- [ ] :

```c
#define MYLIB_H
#include "mylib.h"

#undef MYLIB_H
```

- [ ] :

```c
#ifdef MYLIB_H
#define MYLIB_H

// mylib.h content

#endif /* MYLIB_H */
```

#### Q35. How many times does the code inside the while loop get executed in this program?

```c
main(){
 int x=1;
 while(x++<100){
    x*=x;
    if(x<10) continue;
    if(x>50) break;
 }
}
```

- [ ] 100
- [x] 3
- [ ] 5
- [ ] 50

#### Q36. File input and output (I/O) in C is done through what?

- [ ] syntax-driven components
- [ ] native interfaces
- [ ] system objects
- [x] function calls

#### Q37. Directives are translated by the?

- [x] Pre-processor
- [ ] Compiler
- [ ] Linker
- [ ] Editor

#### Q38. The main loop structures in C programming are the for loop, the while loop, and which other loop?

- [x] do...while
- [ ] for...in
- [ ] repeat...until
- [ ] do...until

#### Q39. By default, C Functions are what type of functions?

- [x] global
- [ ] static
- [ ] library
- [ ] system

#### Q40. You have written a function that you want to include as a member of structure 'a'. How is such as structure member defined?

- [ ] A

```c
struct a {
    void *f1;
};
```

- [x] B

```c
struct a {
    void (*f1)();
};
```

- [ ] C

```c
struct a {
    *(void *f1)();
};
```

- [ ] D

```c
struct a {
    void *f1();
};
```

#### Q41. A Stack data structure allows all data operations at one end only, making it what kind of an implementation?

- [ ] FIFO
- [x] LIFO
- [ ] LILO
- [ ] LOLI

#### Q42. What does this program display?

```c
main(){
    char *p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    int i;
    for (i=0;i<5;i++) *p++; *p++;
    printf("%c",*p++);
}
```

- [ ] K
- [ ] M
- [ ] H
- [x] G

#### Q43. Describe the relationship between lvalue and rvalue.

- [ ] An lvalue may appear only on the left-hand side of an assignment; an rvalue may appear only on the right-hand side.
- [ ] An lvalue may appear only on the left-hand side of an assignment; an rvalue may appear on either the left-hand or right-hand side.
- [ ] An lvalue and an rvalue may appear on either the left-hand or right-hand side of an assignment.
- [x] An lvalue may appear on the left-hand or right-hand side of an assignment; an rvalue may appear only on the right-hand side.

#### Q44. Which operator is used to access the address of a variable?

- [ ] `%`
- [ ] `**`
- [ ] `*`
- [x] `&`

#### Q45. Which add function properly returns the updated value of the result?

- [x] A

```c
void add (int a, int b, int *result)
{
    *result = a+b;
}

main()
{
    int a = 10;
    int b = 20;
    int result = 0;

    add(a,b,&result);
}
```

- [ ] B

```c
void add (int a, int b, int result)
{
    result = a+b;
}

main()
{
    int a = 10;
    int b = 20;
    int result = 0;

    add(a,b,result);
}
```

- [ ] C

```c
void add (int a, int b, int *result)
{
    result = a+b;
}

main()
{
    int a = 10;
    int b = 20;
    int result = 0;

    add(a,b,result);
}
```

- [ ] D

```c
void add (int *a, int *b, int *result)
{
    result = a+b;
}

main()
{
    int a = 10;
    int b = 20;
    int result = 0;

    add(*a,*b,*result);
}
```

#### Q46. Consider the number of the Fibonacci series below 100: 0,1,1,2,3,5,8,13,21,34,55,89. Which piece of code outputs the sequence?

- [ ] A

```c
void fibonacci(int a, int b)
{
    int c = a+b;

    if(a>100)
       return;

    printf("%d", a);

    fibonacci(a,b);
}

int main()
{
    fibonacci(0,1);
}
```

- [ ] B

```c
void fibonacci(int a, int b)
{
    int c = a+b;

    if(a>100)
       return;

    printf("%d", b);

    fibonacci(a,c);
}

int main()
{
    fibonacci(0,1);
}
```

- [x] C

```c
void fibonacci(int a, int b)
{
    int c = a+b;

    if(a>100)
       return;

    printf("%d", a);

    fibonacci(b,c);
}

int main()
{
    fibonacci(0,1);
}
```

- [ ] D

```c
void fibonacci(int a, int b)
{
    int c = a+b;

    if(a>100)
       return;

    printf("%d", c);

    fibonacci(b,c);
}

int main()
{
    fibonacci(0,1);
}
```

#### Q47. Which is _not_ a storage class specifier?

- [x] `intern`
- [ ] `extern`
- [ ] `register`
- [ ] `static`

[Reference](https://en.cppreference.com/w/cpp/language/storage_duration)

#### Q48. Which line of code, after execution, results in `i` having the value of 1?

- [ ] `for(i=1; i<=1; i++);`
- [ ] `for(i=1; i=10; i++);`
- [x] `for(i=1; i==10; i++);`
- [ ] `for(i=10; i>=1; i--);`

#### Q49. What is the value of variable c at the end of this program?

```
1 main() {
2   int a, b, c;
3   a=10; b=50;
4   c=a * b % a;
5 }
```

- [ ] 50
- [ ] 5
- [x] 0
- [ ] 500

#### Q50. What is _not_ one of the basic data types in C

- [ ] long double
- [ ] unsigned char
- [x] array
- [ ] float

#### Q51. What is the member access operator for a structure?

- [ ] ,
- [ ] []
- [x] .
- [ ] :

#### Q52. What standard data type provides the smallest storage size and can be used in computations?

- [x] char
- [ ] float
- [ ] int
- [ ] short

#### Q53. what does the ctype tolower() function do?

- [ ] It returns TRUE for lowercase letters of the alphabet.
- [ ] It ensures that text output uses only ASCII values (0 through 127).
- [ ] It returns FALSE for lowercase letters of the alphabet.
- [x] It converts an uppercase letter of the alphabet to lowercase.

#### Q54. Void pointer _vptr_ is assigned the address of float variable _g_. What is a valid way to dereference _vptr_ to assign its pointed value to a float variable named _f_ later in the program?

```c
float g;
void *vptr=&g;
```

- [ ] `f=(float *)vptr;`
- [x] `f=*(float *)vptr;`
- [ ] `f=*(float)vptr;`
- [ ] `f=(float)*vptr;`

#### Q55. The dynamic memory allocation functions are defined in which system header file?

- [ ] stdio.h
- [x] stdlib.h
- [ ] limits.h
- [ ] stddef.h

#### Q56. A function is a set of **\_**.

- [ ] declarations
- [x] statements
- [ ] variables
- [ ] objects

#### Q57. How are static functions different from global functions?

- [ ] Static functions must be declared in advance of being defined.
- [ ] Static functions must be declared in a separate header file.
- [ ] Static functions always return the same value.
- [x] Static functions can be accessed only in the file where they are declared.

#### Q58. Which code example creates the string "Hello Mars" in storage buffer `hello`.

- [ ] :

```c
    char hello[25];
    strcpy(hello, "Hello ");
    strcpy(hello, "Mars");
```

- [x] :

```c
    char hello[25];
    char *p;
    strcpy(hello, "Hello World");
    p = hello;
    p +=6;
    strcpy(p, "Mars");
```

- [ ] :

```c
    char *hello;
    strcpy(hello, "Hello World");
    hello+=6;
    strcpy(hello, "Mars");
```

- [ ] :

```c
    char hello[25];
    strcpy(hello, "Hello World");
    strcpy(*hello[6], "Mars");
```

#### Q59. If you use the fopen() function with the "a" mode, what happens if the named file doesn't exist?

- [ ] The file is created and opened for reading.
- [x] The file is created and opened for writing.
- [ ] The fopen() function returns a NULL indicating that the operation has failed.
- [ ] The file is created and opened for both writing and reading

[Reference](https://www.tutorialspoint.com/c_standard_library/c_function_fopen.htm)

#### Q60. What does this function return?

```c
int fl(int a, int b) { return(a>b?a:b); }
```

- [ ] compiler error
- [ ] the smaller value of the two passed parameters
- [ ] runtime error
- [x] the greater value of the two passed parameters

#### Q61. Which option is a valid function name?

- [x] draw_star()
- [ ] 5times()
- [ ] upper-limit()
- [ ] auto()

#### Q62. What is not a valid type definition of a structure that contains x and y coordinates as integers, and that can be used as shown for the variable named point?

```c
coord point;
point.x = 9;
point.y = 3;
```

- [ ] :

```c
struct coord{
    int x;
    int y;
};
typedef struct coord coord;
```

- [x] :

```c
typedef struct coord{
    int x;
    int y;
};
```

- [ ] :

```c
typedef struct coord{
    int x;
    int y;
} coord;
```

- [ ] :

```c
typedef struct{
    int x;
    int y;
} coord;
```

#### Q63. What is the output of the below program?

```c
#include <stdio.h>
#if X == 3
    #define Y 3
#else
    #define Y 5
#endif

int main()
{
    printf("%d", Y);
    return 0;
}
```

- [ ] 3
- [x] 5
- [ ] 3 or 5 depending on input
- [ ] Compile time error

#### Q64. What do the functions malloc() and calloc() allocate?

- [ ] reallocated memory
- [ ] static memory
- [x] dynamic memory
- [ ] fragmented memory

[Calloc](https://devdocs.io/c/memory/calloc)
[Malloc](https://devdocs.io/c/memory/malloc)

#### Q65. You need to determine if a string variable is a substring of another string. Which standard C library function do you use?

- [ ] substr(str1, str2);
- [x] strstr(str1, str2);
- [ ] substring(str1, str2);
- [ ] strspn(str1, str2);

[Reference](https://devdocs.io/c/string/byte/strstr)

#### Q66. Find the output of the program.

```c
#include <stdio.h>

#define L 10
int main(){
    int a =10;
    switch (a,a<<2){
        case L:printf("a==L");     break;
        case L*2 : printf("a = L* 2\n");     break;
        case L*4 : printf("a = L* 4\n");    break;
        default: printf("Error\n");
    }
}
```

- [ ] `a=L*2`
- [ ] `a=L`
- [ ] `Error`
- [x] `a=L*4`

[Reference](https://www.geeksforgeeks.org/left-shift-right-shift-operators-c-cpp/)

#### Q67. Predict the output of the following code when the **integer** variables x is initialized to 10,y to 2, and z to 0.

```c
z = x + y * x + 10 / 2 * x;
printf("value is =%d",z);
```

- [x] 80
- [ ] 170
- [ ] 31.5
- [ ] 6

[Reference](https://www.informit.com/articles/article.aspx?p=2062174&seqNum=4)

#### Q68. What will be the output of the following code snippet?

```c
#include <stdio.h>
void solve() {
    int x = 2;
    printf("%d", (x << 1) + (x >> 1));
}
int main() {
    solve();
	return 0;
}
```

- [x] 5
- [ ] 4
- [ ] 2
- [ ] 1

#### Q69. What is the output of this program?

```c
int a=20, b=10;
int f1(a) {
    return(a*b);
}
main() {
    printf("%d", f1(5));
}
```

- [ ] 100
- [ ] 200
- [ ] 5
- [x] 50

#### Q70. What is /0 character?

- [ ] String
- [x] NULL Character
- [ ] ZERO
- [ ] Variable

[Reference](<https://www.youth4work.com/Talent/C-Language/Forum/117150-what-is-the-use-of-a-0-character-in-c-language#:~:text=by%20using%20of%20null%20character(%27%5C0%27)%20it%20terminates%20the%20string%20untill%20the%20null%20character%20hit...%20which%20means%20comes%20out%20of%20the%20loop...%20In%20strings%20by%20default%20takes%20the%20null%20charater>)

#### Q71. What is the correct output for the following code?

```c
#include&lt;stdio.h&gt;
#include&lt;conio.h&gt;
main()
{
     int a=10, b=20;
     clrscr();
     printf("Before swapping a=%d b=%d",a,b);
     a=a+b;
     b=a-b;
     a=a-b;
     printf("nAfter swapping a=%d b=%d",a,b);
     getch();
}
```

- [ ] Before a=10 b=20 , After a=10 b=10
- [ ] Before a=10 b=10 , After a=20 b=10
- [ ] Before a=10 b=20 , After a=20 b=20
- [x] Before a=10 b=20 , After a=20 b=10

#### Q72. What is the Incorrect option that explains # pragma directive ?

- [ ] #pragma exit allows us to specify functions called upon program exit.
- [ ] This is a preprocessor directive that can be used to turn on or off certain features.
- [x] #pragma startup doesn't allow us to specify functions called upon program startup.
- [ ] It is of two types #pragma startup, #pragma exit and pragma warn.

#### Q73. What will be the output of the following code snippet?

```c
#include <stdio.h>
union School {
    int age, rollNo;
    double marks;
};
void solve() {
    union School sc;
    sc.age = 19;
    sc.rollNo = 82;
    sc.marks = 19.04;
    printf("%d", (int)sizeof(sc));
}
int main() {
    solve();
	return 0;
}
```

- [ ] 2
- [ ] 4
- [x] 8
- [ ] 10

#### Q74. What will be the output of the following code snippet?

```c
#include <stdio.h>
struct School {
    int age, rollNo;
};
void solve() {
    struct School sc;
    sc.age = 19;
    sc.rollNo = 82;
    printf("%d %d", sc.age, sc.rollNo);
}
int main() {
    solve();
	return 0;
}
```

- [x] 19 82
- [ ] Compilation Error
- [ ] 82 19
- [ ] None of these

#### Q75. What is the output of the following code snippet?

```c
int main() {
	int sum = 2 + 4 / 2 + 6 * 2;
	printf("%d", sum);
	return 0;
}
```

- [ ] 2
- [ ] 15
- [x] 16
- [ ] 18

#### Q76. What does the following declaration mean?

```
int (*ptr)[10];
```

- [ ] ptr is an array of pointers to 10 integers
- [x] ptr is a pointer to an array of 10 integers
- [ ] ptr is an array of 10 integers
- [ ] ptr is a pointer to an array

#### Q77. What will be the output of the following code snippet?

```c
#include <stdio.h>
void change(int,int);
int main()
{
   int a=10,b=20;
   change(a,b); //calling a function by passing the values of variables.
   printf("Value of a is: %d",a);
   printf("\n");
   printf("Value of b is: %d",b);
   return 0;
}
void change(int x,int y)
{
   x=13;
   y=17;
}
```

- [x] 10,20
- [ ] 10,10
- [ ] 20,20
- [ ] 20,10

**Explanation:** The function "change" will change the value of x and y only within its own scope, so a and is unaffected.

#### Q78. Choose true or false. When a variable is created in C, a memory address is assigned to the variable.

- [x] True
- [ ] False

#### Q79. What does the following fragment of C-program print?

```c
#include <stdio.h>

int main()
{
    char c[] = "GATE2011";

    char *p = c;

    printf("%s", p + p[3] -p[1]);

    return 0;
}
```

- [ ] GATE 2011
- [ ] E2011
- [x] 2011
- [ ] 01

**Explanation:** char c[ ] = "GATE2011"; since char \*p =c it means p represents the base address of string “GATE2011” SO p[3] is 'E' and p[1] is 'A'. Value of Sub expression p[3] – p[1] = ASCII value of ‘E’ – ASCII value of ‘A’ = 4. So the expression p + p[3] – p[1] becomes ( p + 4) And (p+4) represent to base address of string “2011” printf(“%s”, p + p[3] – p[1]) ; So it will print 2011

#### Q80. What is the output of the following code snippet?

```c
int main() {
	int a = 5, b = 6, c;
	c = a++ + ++b;
	printf("%d %d %d", a, b, c);
	return 0;
}
```

- [ ] 5 6 11
- [x] 6 7 12
- [ ] 5 6 12
- [ ] 6 6 12

#### Q81. What will be the output of the following C program segment?

```c
char inchar = 'A';
switch (inchar)
{
case 'A' :
	printf ("choice A \n") ;
case 'B' :
	printf ("choice B ") ;
case 'C' :
case 'D' :
case 'E' :
default:
	printf ("No Choice") ;
}

```

- [ ] No choice
- [ ] Choice A
- [x] Choice A
      Choice B No choice
- [ ] Program gives no output as it is erroneous

#### Q82. String variable str1 has the value of "abc", and string variable str2 has the value "xyz". What are the values of str1 and str2 after this statement is executed?

```c
strcpy(str1, str2);
```

- [x] str1: "xyz" ; str2: "xyz"
- [ ] str1: "abc" ; str2: "xyz"
- [ ] str1: "xyz" ; str2: "abc"
- [ ] str1: "abc" ; str2: "abc"

#### Q88. What is not a valid command with this declaration?

```c
char *string[20] = { "one", "two", "three"};
```

- [ ] `printf("%c", string[1][2]);`
- [x] `printf("%s", string[1][2]);`
- [ ] `printf("%s", string[1]);`
- [ ] `printf(string[1]);`

#### Q89. What is the output of this code?

```c
int x = 5;
int y = ++x + x++;
printf("%d %d", x, y);
```

- [ ] 6 11
- [x] 7 12
- [ ] 7 11
- [ ] 6 12

**Explanation:**
First, ++x increments x to 6 and uses 6 in the expression. Then x++ uses 6 and increments x to 7 after. So y = 6 + 6 = 12, and x becomes 7.

[Reference](https://en.cppreference.com/w/c/language/operator_precedence)

#### Q90. What does the `volatile` keyword indicate in C?

- [ ] The variable cannot be modified
- [x] The variable may be changed by external factors
- [ ] The variable is stored in ROM
- [ ] The variable is a constant

**Explanation:**
The `volatile` keyword tells the compiler that a variable's value may be changed by external factors (hardware, interrupts, other threads), so the compiler should not optimize away reads/writes to it.

[Reference](https://en.cppreference.com/w/c/language/volatile)

#### Q91. What is the purpose of the `restrict` keyword in C99?

- [x] To indicate that a pointer is the only way to access an object
- [ ] To restrict the scope of a variable
- [ ] To prevent modification of a variable
- [ ] To restrict function access

**Explanation:**
The `restrict` keyword is a type qualifier that can be applied to pointers. It tells the compiler that for the lifetime of the pointer, only it or a value directly derived from it will be used to access the object it points to. This enables certain compiler optimizations.

[Reference](https://en.cppreference.com/w/c/language/restrict)

#### Q92. What is the difference between `malloc()` and `calloc()`?

- [ ] malloc is faster than calloc
- [x] calloc initializes allocated memory to zero, malloc does not
- [ ] malloc can allocate more memory than calloc
- [ ] There is no difference

**Explanation:**
`calloc()` allocates memory and initializes all bytes to zero, while `malloc()` allocates memory but leaves it uninitialized. `calloc()` also takes two arguments (number of elements and size of each element) while `malloc()` takes one (total size in bytes).

[Reference](https://en.cppreference.com/w/c/memory/calloc)

#### Q93. What is a dangling pointer?

- [ ] A pointer that points to NULL
- [x] A pointer that points to freed or deleted memory
- [ ] A pointer that has not been initialized
- [ ] A pointer that points to a constant

**Explanation:**
A dangling pointer is a pointer that points to memory that has been freed or deleted. Accessing such a pointer leads to undefined behavior.

[Reference](https://en.wikipedia.org/wiki/Dangling_pointer)

#### Q94. What is the output of this code?

```c
int arr[] = {1, 2, 3, 4, 5};
printf("%d", *(arr + 3));
```

- [ ] 1
- [ ] 2
- [ ] 3
- [x] 4

**Explanation:**
`arr` is a pointer to the first element. `arr + 3` points to the 4th element (index 3). The `*` operator dereferences it to get the value 4.

[Reference](https://en.cppreference.com/w/c/language/operator_member_access)

#### Q95. What does the `static` keyword do when applied to a function?

- [x] Limits the function's scope to the current file
- [ ] Makes the function run faster
- [ ] Prevents the function from being called
- [ ] Makes the function inline

**Explanation:**
When `static` is applied to a function, it limits the function's linkage to internal linkage, meaning it can only be called from within the same translation unit (source file).

[Reference](https://en.cppreference.com/w/c/language/storage_duration)

#### Q96. What is the size of a pointer in a 64-bit system?

- [ ] 4 bytes
- [x] 8 bytes
- [ ] 16 bytes
- [ ] Depends on what it points to

**Explanation:**
On a 64-bit system, pointers are typically 8 bytes (64 bits) regardless of what they point to. The size is determined by the system architecture, not the pointed-to type.

[Reference](https://en.cppreference.com/w/c/language/pointer)

#### Q97. What is the purpose of `typedef`?

- [ ] To define a new data type
- [x] To create an alias for an existing data type
- [ ] To declare a variable
- [ ] To define a macro

**Explanation:**
`typedef` creates an alias (alternative name) for an existing data type. It doesn't create a new type, just a new name for an existing one.

[Reference](https://en.cppreference.com/w/c/language/typedef)

#### Q98. What is a memory leak?

- [ ] When a pointer points to invalid memory
- [x] When allocated memory is not freed
- [ ] When a variable goes out of scope
- [ ] When stack overflow occurs

**Explanation:**
A memory leak occurs when dynamically allocated memory (via `malloc`, `calloc`, etc.) is not freed using `free()`, causing the program to consume more and more memory over time.

[Reference](https://en.wikipedia.org/wiki/Memory_leak)

#### Q99. What is the output of this code?

```c
int x = 10;
int *p = &x;
*p = 20;
printf("%d", x);
```

- [ ] 10
- [x] 20
- [ ] Address of x
- [ ] Undefined

**Explanation:**
`p` points to `x`. `*p = 20` modifies the value at the address p points to, which is `x`. So `x` becomes 20.

[Reference](https://en.cppreference.com/w/c/language/pointer)

#### Q100. What does `sizeof(char)` always return in C?

- [x] 1
- [ ] 2
- [ ] 4
- [ ] Depends on the system

**Explanation:**
By definition in the C standard, `sizeof(char)` is always 1. This is the fundamental unit of size in C, and all other sizes are multiples of it.

[Reference](https://en.cppreference.com/w/c/language/sizeof)

#### Q101. What is the difference between `++i` and `i++`?

- [x] ++i increments before use, i++ increments after use
- [ ] ++i is faster than i++
- [ ] i++ can only be used in loops
- [ ] There is no difference

**Explanation:**
`++i` (pre-increment) increments the variable and returns the new value. `i++` (post-increment) returns the current value and then increments the variable.

[Reference](https://en.cppreference.com/w/c/language/operator_incdec)

#### Q102. What is a segmentation fault?

- [ ] A syntax error
- [x] An error caused by accessing invalid memory
- [ ] A compilation error
- [ ] A warning

**Explanation:**
A segmentation fault (segfault) occurs when a program tries to access memory it's not allowed to access, such as dereferencing a NULL pointer or accessing freed memory.

[Reference](https://en.wikipedia.org/wiki/Segmentation_fault)

#### Q103. What is the purpose of the `const` keyword with pointers?

```c
const int *p;
```

- [x] The value pointed to cannot be modified through p
- [ ] The pointer p cannot be modified
- [ ] Both the pointer and value are constant
- [ ] It has no effect

**Explanation:**
`const int *p` means p points to a constant integer - you cannot modify the value through p, but you can change where p points to. For `int * const p`, the pointer itself is constant.

[Reference](https://en.cppreference.com/w/c/language/const)

#### Q104. What is the output of this code?

```c
int arr[5] = {1, 2, 3};
printf("%d", arr[4]);
```

- [x] 0
- [ ] 3
- [ ] Garbage value
- [ ] Compilation error

**Explanation:**
When an array is partially initialized, the remaining elements are automatically initialized to 0. So arr[3] and arr[4] are both 0.

[Reference](https://en.cppreference.com/w/c/language/array_initialization)

#### Q105. What does the `extern` keyword do?

- [ ] Makes a variable external to the program
- [x] Declares a variable that is defined elsewhere
- [ ] Exports a variable to other programs
- [ ] Creates a global variable

**Explanation:**
`extern` declares a variable or function that is defined in another source file or later in the same file. It tells the compiler that the definition exists elsewhere.

[Reference](https://en.cppreference.com/w/c/language/extern)

#### Q106. What is the difference between `struct` and `union`?

- [x] struct members have separate memory, union members share memory
- [ ] struct is faster than union
- [ ] union can have more members than struct
- [ ] There is no difference

**Explanation:**
In a `struct`, each member has its own memory location. In a `union`, all members share the same memory location, and only one member can hold a value at a time. The size of a union is the size of its largest member.

[Reference](https://en.cppreference.com/w/c/language/union)

#### Q107. What is the output of this code?

```c
int x = 5;
printf("%d", x << 2);
```

- [ ] 5
- [ ] 7
- [x] 20
- [ ] 10

**Explanation:**
The `<<` operator is a left bit shift. `x << 2` shifts the bits of x left by 2 positions, which is equivalent to multiplying by 2^2 = 4. So 5 \* 4 = 20.

[Reference](https://en.cppreference.com/w/c/language/operator_arithmetic)

#### Q108. What is a function pointer?

- [ ] A pointer to a function's return value
- [x] A pointer that stores the address of a function
- [ ] A function that returns a pointer
- [ ] A pointer inside a function

**Explanation:**
A function pointer is a variable that stores the address of a function. It can be used to call the function indirectly or pass functions as arguments to other functions.

[Reference](https://en.cppreference.com/w/c/language/pointer#Pointers_to_functions)

#### Q109. What does `NULL` represent in C?

- [ ] The number zero
- [x] A null pointer constant
- [ ] An empty string
- [ ] An undefined value

**Explanation:**
`NULL` is a macro that represents a null pointer constant. It's typically defined as `((void*)0)` or just `0`. It indicates that a pointer doesn't point to any valid memory location.

[Reference](https://en.cppreference.com/w/c/types/NULL)

#### Q110. What is the output of this code?

```c
int x = 10, y = 20;
int *p1 = &x, *p2 = &y;
*p1 = *p2;
printf("%d %d", x, y);
```

- [ ] 10 20
- [x] 20 20
- [ ] 10 10
- [ ] 20 10

**Explanation:**
`*p1 = *p2` copies the value pointed to by p2 (which is 20) to the location pointed to by p1 (which is x). So x becomes 20, y remains 20.

[Reference](https://en.cppreference.com/w/c/language/pointer)

#### Q111. What is the purpose of `#pragma` directive?

- [ ] To include header files
- [ ] To define macros
- [x] To provide compiler-specific instructions
- [ ] To declare variables

**Explanation:**
`#pragma` is a preprocessor directive that provides additional information to the compiler. It's implementation-defined and used for compiler-specific features.

[Reference](https://en.cppreference.com/w/c/preprocessor/impl)

#### Q112. What is the difference between `break` and `continue`?

- [x] break exits the loop, continue skips to next iteration
- [ ] break is faster than continue
- [ ] continue exits the loop, break skips iteration
- [ ] There is no difference

**Explanation:**
`break` terminates the loop entirely and continues execution after the loop. `continue` skips the rest of the current iteration and moves to the next iteration of the loop.

[Reference](https://en.cppreference.com/w/c/language/break)

#### Q113. What is the output of this code?

```c
int arr[] = {1, 2, 3, 4, 5};
printf("%d", sizeof(arr) / sizeof(arr[0]));
```

- [ ] 4
- [x] 5
- [ ] 20
- [ ] 1

**Explanation:**
`sizeof(arr)` gives the total size of the array in bytes. `sizeof(arr[0])` gives the size of one element. Dividing them gives the number of elements: 5.

[Reference](https://en.cppreference.com/w/c/language/sizeof)

#### Q114. What is a void pointer?

- [ ] A pointer that points to nothing
- [x] A generic pointer that can point to any data type
- [ ] A pointer to void functions
- [ ] An invalid pointer

**Explanation:**
A `void*` pointer is a generic pointer that can point to any data type. It must be cast to the appropriate type before dereferencing.

[Reference](https://en.cppreference.com/w/c/language/pointer)

#### Q115. What does the `register` keyword suggest to the compiler?

- [ ] To make a variable global
- [x] To store a variable in a CPU register for faster access
- [ ] To protect a variable from modification
- [ ] To allocate memory on the heap

**Explanation:**
The `register` keyword suggests (but doesn't guarantee) that the compiler should store the variable in a CPU register for faster access. Modern compilers often ignore this hint and make their own optimization decisions.

[Reference](https://en.cppreference.com/w/c/language/storage_duration)

#### Q116. What is the output of this code?

```c
int x = 5;
int y = (x > 3) ? 10 : 20;
printf("%d", y);
```

- [x] 10
- [ ] 20
- [ ] 5
- [ ] 3

**Explanation:**
This is the ternary operator. Since x > 3 is true, y is assigned 10.

[Reference](https://en.cppreference.com/w/c/language/operator_other)

#### Q117. What is the difference between `malloc()` and `realloc()`?

- [ ] malloc is faster than realloc
- [x] realloc resizes previously allocated memory
- [ ] malloc initializes memory, realloc doesn't
- [ ] There is no difference

**Explanation:**
`malloc()` allocates new memory. `realloc()` changes the size of previously allocated memory block, potentially moving it to a new location if needed.

[Reference](https://en.cppreference.com/w/c/memory/realloc)

#### Q118. What is an enumeration in C?

- [ ] A loop construct
- [x] A user-defined type consisting of named integer constants
- [ ] A function that counts elements
- [ ] An array of constants

**Explanation:**
An enumeration (`enum`) is a user-defined type that consists of a set of named integer constants. It makes code more readable by giving meaningful names to integer values.

[Reference](https://en.cppreference.com/w/c/language/enum)

#### Q119. What is the output of this code?

```c
int x = 10;
int y = x++ + ++x;
printf("%d %d", x, y);
```

- [ ] 11 21
- [x] 12 22
- [ ] 12 21
- [ ] 11 22

**Explanation:**
First, x++ uses 10 and increments x to 11. Then ++x increments x to 12 and uses 12. So y = 10 + 12 = 22, and x is 12.

[Reference](https://en.cppreference.com/w/c/language/operator_incdec)

#### Q120. What is the purpose of `assert()` macro?

- [ ] To assign values to variables
- [x] To check assumptions and terminate if false
- [ ] To assert dominance over other functions
- [ ] To create assertions in documentation

**Explanation:**
`assert()` is a macro used for debugging. It checks if a condition is true. If false, it prints an error message and terminates the program. It's typically disabled in release builds.

[Reference](https://en.cppreference.com/w/c/error/assert)

#### Q121. What is the difference between `fgets()` and `gets()`?

- [ ] fgets is faster than gets
- [x] fgets is safer as it limits input size
- [ ] gets can read from any file
- [ ] There is no difference

**Explanation:**
`gets()` is unsafe because it doesn't check buffer size, leading to buffer overflow vulnerabilities. `fgets()` allows you to specify the maximum number of characters to read, making it safer. `gets()` was removed from C11 standard.

[Reference](https://en.cppreference.com/w/c/io/fgets)

#### Q122. What is the output of this code?

```c
int x = 5;
int *p = &x;
printf("%p %p", (void*)&x, (void*)p);
```

- [x] Same address printed twice
- [ ] Two different addresses
- [ ] Compilation error
- [ ] 5 5

**Explanation:**
`&x` gives the address of x, and p stores the address of x. Both print the same address (in hexadecimal format due to %p).

[Reference](https://en.cppreference.com/w/c/io/fprintf)

#### Q123. What is a preprocessor directive?

- [ ] A function that processes data
- [x] An instruction to the preprocessor before compilation
- [ ] A directive from the processor
- [ ] A type of loop

**Explanation:**
Preprocessor directives (like #include, #define, #ifdef) are instructions processed before actual compilation. They start with # and are handled by the preprocessor.

[Reference](https://en.cppreference.com/w/c/preprocessor)

#### Q124. What is the output of this code?

{% raw %}
```c
int arr[3][3] = {{1,2,3},{4,5,6},{7,8,9}};
printf("%d", arr[1][2]);
```
{% endraw %}

- [ ] 5
- [x] 6
- [ ] 8
- [ ] 9

**Explanation:**
`arr[1][2]` accesses row 1 (second row: {4,5,6}), column 2 (third element: 6).

[Reference](https://en.cppreference.com/w/c/language/array)

#### Q125. What is the purpose of `memset()` function?

- [ ] To allocate memory
- [x] To fill a block of memory with a specific value
- [ ] To copy memory
- [ ] To free memory

**Explanation:**
`memset()` fills a block of memory with a specified byte value. It's commonly used to initialize arrays or structures to zero.

[Reference](https://en.cppreference.com/w/c/string/byte/memset)

#### Q126. What is the difference between `strcpy()` and `strncpy()`?

- [ ] strcpy is faster
- [x] strncpy limits the number of characters copied
- [ ] strcpy can copy any data type
- [ ] There is no difference

**Explanation:**
`strcpy()` copies the entire string including null terminator. `strncpy()` copies at most n characters, providing protection against buffer overflow.

[Reference](https://en.cppreference.com/w/c/string/byte/strncpy)

#### Q127. What is the output of this code?

```c
int x = 10;
int y = 3;
printf("%d", x % y);
```

- [x] 1
- [ ] 3
- [ ] 0
- [ ] 10

**Explanation:**
The `%` operator is the modulo operator. 10 % 3 gives the remainder of 10 divided by 3, which is 1.

[Reference](https://en.cppreference.com/w/c/language/operator_arithmetic)

#### Q128. What is a macro in C?

- [ ] A large function
- [x] A preprocessor directive that defines a code fragment
- [ ] A type of variable
- [ ] A loop construct

**Explanation:**
A macro is defined using #define and represents a code fragment that is replaced by the preprocessor before compilation. It can be a constant or a function-like construct.

[Reference](https://en.cppreference.com/w/c/preprocessor/replace)

#### Q129. What is the output of this code?

```c
int x = 5;
int y = 10;
int z = (x > y) ? x : y;
printf("%d", z);
```

- [ ] 5
- [x] 10
- [ ] 1
- [ ] 0

**Explanation:**
The ternary operator checks if x > y. Since it's false (5 is not greater than 10), z is assigned the value of y, which is 10.

[Reference](https://en.cppreference.com/w/c/language/operator_other)

#### Q130. What is the purpose of `free()` function?

- [ ] To free up CPU resources
- [x] To deallocate dynamically allocated memory
- [ ] To free variables from scope
- [ ] To clear the screen

**Explanation:**
`free()` deallocates memory that was previously allocated by `malloc()`, `calloc()`, or `realloc()`. It's essential to prevent memory leaks.

[Reference](https://en.cppreference.com/w/c/memory/free)

#### Q131. What is the output of this code?

```c
char str[] = "Hello";
printf("%d", strlen(str));
```

- [ ] 6
- [x] 5
- [ ] 4
- [ ] Undefined

**Explanation:**
`strlen()` returns the length of the string excluding the null terminator. "Hello" has 5 characters.

[Reference](https://en.cppreference.com/w/c/string/byte/strlen)

#### Q132. What is a static variable inside a function?

- [ ] A variable that cannot change
- [x] A variable that retains its value between function calls
- [ ] A variable stored in ROM
- [ ] A global variable

**Explanation:**
A static variable inside a function retains its value between function calls. It's initialized only once and exists for the lifetime of the program.

[Reference](https://en.cppreference.com/w/c/language/storage_duration)

#### Q133. What is the output of this code?

```c
int arr[] = {1, 2, 3, 4, 5};
int *p = arr + 2;
printf("%d", *p);
```

- [ ] 1
- [ ] 2
- [x] 3
- [ ] 4

**Explanation:**
`arr + 2` points to the third element (index 2). Dereferencing it with `*p` gives the value 3.

[Reference](https://en.cppreference.com/w/c/language/operator_member_access)

#### Q134. What is the difference between `printf()` and `sprintf()`?

- [ ] printf is faster
- [x] sprintf writes to a string, printf writes to stdout
- [ ] sprintf can only print strings
- [ ] There is no difference

**Explanation:**
`printf()` writes formatted output to stdout (console). `sprintf()` writes formatted output to a character string buffer.

[Reference](https://en.cppreference.com/w/c/io/fprintf)

#### Q135. What is the output of this code?

```c
int x = 5;
printf("%d", x & 3);
```

- [ ] 5
- [ ] 3
- [x] 1
- [ ] 8

**Explanation:**
The `&` operator is bitwise AND. 5 in binary is 101, 3 is 011. 101 & 011 = 001 = 1.

[Reference](https://en.cppreference.com/w/c/language/operator_arithmetic)

#### Q136. What is a header guard?

- [ ] A security feature
- [x] A preprocessor construct to prevent multiple inclusion
- [ ] A function that guards headers
- [ ] A type of comment

**Explanation:**
Header guards (using #ifndef, #define, #endif) prevent a header file from being included multiple times in the same compilation unit, which would cause redefinition errors.

[Reference](https://en.cppreference.com/w/c/preprocessor/conditional)

#### Q137. What is the output of this code?

```c
int x = 10;
int y = 20;
int *p = &x;
p = &y;
printf("%d", *p);
```

- [ ] 10
- [x] 20
- [ ] Address of x
- [ ] Address of y

**Explanation:**
Initially p points to x. Then `p = &y` makes p point to y. `*p` dereferences p to get the value of y, which is 20.

[Reference](https://en.cppreference.com/w/c/language/pointer)

#### Q138. What is the purpose of `memcpy()` function?

- [ ] To allocate memory
- [x] To copy a block of memory from source to destination
- [ ] To compare memory blocks
- [ ] To free memory

**Explanation:**
`memcpy()` copies n bytes from source memory to destination memory. It's faster than copying element by element but doesn't handle overlapping memory regions (use `memmove()` for that).

[Reference](https://en.cppreference.com/w/c/string/byte/memcpy)

#### Q139. What is the output of this code?

```c
int x = 5;
printf("%d", x | 3);
```

- [ ] 3
- [ ] 5
- [x] 7
- [ ] 8

**Explanation:**
The `|` operator is bitwise OR. 5 in binary is 101, 3 is 011. 101 | 011 = 111 = 7.

[Reference](https://en.cppreference.com/w/c/language/operator_arithmetic)

#### Q140. What is the difference between `strcmp()` and `strncmp()`?

- [ ] strcmp is case-sensitive, strncmp is not
- [x] strncmp compares only first n characters
- [ ] strcmp is faster
- [ ] There is no difference

**Explanation:**
`strcmp()` compares entire strings. `strncmp()` compares at most n characters, which is useful for comparing string prefixes or limiting comparison length.

[Reference](https://en.cppreference.com/w/c/string/byte/strncmp)
