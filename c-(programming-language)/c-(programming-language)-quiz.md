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
    free(bigArray);
}
```

#### Q2. What will this code print on the screen?

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
A is greater then B
C is fun!
```

- [ ] :

```
A is greater then B
B is greater then A
C is fun!
```

- [ ] :

```
A is greater then B
B is greater then A
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

- [ ] The preprocessor will try to locate fileA in same directory as the source file, and the fileB in a predetermined directory path.
- [ ] The preprocessor will try to locate fileA in the fixed system directory. It will try to locate fileB in the directory path designated by the -I option added to the command line while compiling the source code.
- [ ] The file using the fileA syntax must be system files, of unlimited number; fileB must be a user file at a maximun of one per source file.
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
- [ ] The data type of PI needs to be float not int.
- [ ] The printf statement needs to use PI, not pi.

#### Q12. Which is the smallest program to compile and run without errors?

- [ ] main()
- [ ] int main() {return 0;}
- [x] main() { }
- [ ] main() { ; }

[Reference](https://www.beningo.com/150-the-wolrds-shortest-c-program/)

#### Q13. What is optional in a function declaration?

- [ ] data type of parameters
- [ ] return type of function
- [x] parameter names
- [ ] number of parameters

[Reference](https://www.cprogramming.com/tutorial/c/lesson4.html)

#### Q14. C treats all devices, such as the display and the keyboard, as files. Which file opens automatically when a program executes?

- [x] stdout
- [ ] stdio.h
- [ ] default.h
- [ ] string.h

#### Q15. In which segment does dynamic memory allocation takes place?

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

- [ ] during the assigment of the variable
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

#### Q29. Compile time errors are static errors that can be found where in the code?

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

- [ ] global
- [ ] static
- [x] library
- [ ] system

#### Q40. You have written a function that you want to include as a member of structure a. How is such as structure member defiened?

- [x] :

```c
struct a {
    void *f1;
};
```

- [ ] :

```c
struct a {
    void (*f1)();
};
```

- [ ] :

```c
struct a {
    *(void *f1)();
};
```

- [ ] :

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
- [ ] An lvalue and an rvalue may appear on either left-hand or right-hand side of an assignment.
- [x] An lvalue may appear on the left-hand or right-hand side of an assignment; an rvalue may appear only on the right-hand side.

#### Q44. Which operator is used to access the address of a variable?

- [ ] `%`
- [ ] `**`
- [ ] `*`
- [x] `&`

#### Q45. Which add function properly returns the updated value of result?

- [x] :

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

- [ ] :

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

- [ ] :

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

- [ ] :

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

- [ ] :

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

- [ ] :

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

- [x] :

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

- [ ] :

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

#### Q55. The dynamic memory allocation functions are defined in which system header file ?

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
- [ ] Static functions must be declared is a separate header file.
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

#### Q61. Which function fo you use to deallocate memory?

- [x] free()
- [ ] dealloc()
- [ ] release()
- [ ] dealloc()

#### Q62. Which option is a valid function name?

- [x] draw_star()
- [ ] 5times()
- [ ] upper-limit()
- [ ] auto()

#### Q63. What is not a valid type definition of a structure that contains x and y coordinates as integers, and that can be used as shown for the variable named point?

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

#### Q64. What is the output of the below program?

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

#### Q65. What do the functions malloc() and calloc() allocate?

- [ ] reallocatged memory
- [ ] static memeory
- [x] dynamic memory
- [ ] fragmented memory

[Reference](https://devdocs.io/c/memory/calloc , https://devdocs.io/c/memory/malloc )

#### Q66. You need to determine if a string variable is a substring of another string. Which standard C library function do you use?

- [ ] substr(str1, str2);
- [x] strstr(str1, str2);
- [ ] substring(str1, str2);
- [ ] strspn(str1, str2);

[Reference](https://devdocs.io/c/string/byte/strstr)

#### Q67. Find the output of the program?

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

#### Q68. Predict the output of the following code when the **interger** variables x is initialized to 10,y to 2 and z to 0.

```c
z = x + y * x + 10 / 2 * x;
printf("value is =%d",z);
```

- [x] 80
- [ ] 170
- [ ] 31.5
- [ ] 6

[Reference](https://www.informit.com/articles/article.aspx?p=2062174&seqNum=4)

#### Q69. What will be the output of the following code snippet?

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

#### Q70. What is the output of this program?

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

#### Q71. What is /0 character ?

- [ ] String
- [x] NULL Character
- [ ] ZERO
- [ ] Variable

[Reference](<https://www.youth4work.com/Talent/C-Language/Forum/117150-what-is-the-use-of-a-0-character-in-c-language#:~:text=by%20using%20of%20null%20character(%27%5C0%27)%20it%20terminates%20the%20string%20untill%20the%20null%20character%20hit...%20which%20means%20comes%20out%20of%20the%20loop...%20In%20strings%20by%20default%20takes%20the%20null%20charater>)

#### Q72. What is correct output for follwing code ?

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

#### Q73. What is Incorrect option that explain # pragma directive ?

- [ ] #pragma exit allows us to specify functions called upon program exit.
- [ ] This is a preprocessor directive that can be used to turn on or off certain features.
- [x] #pragma startup don't allows us to specify functions called upon program startup.
- [ ] It is of two types #pragma startup, #pragma exit and pragma warn.

#### Q74. What will be the output of the following code snippet?

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

#### Q75. What will be the output of the following code snippet?

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

#### Q76. What is the output of the following code snippet?

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

#### Q77. What is not a valid command with this declaration?

```
chat *string[20] = {"one", "two", "three"};
```

- [x] printf("%s", string[1][2]);
- [ ] printf("%s", string[1]);
- [ ] printf(string[1]);
- [ ] printf("%c", string[1][2]);

**Explanation :** This matrix is not defined in 2D because which this command is not valid and there will no output.

#### Q78. What does the following declaration mean?

```
int (*ptr)[10];
```

- [ ] ptr is array of pointers to 10 integers
- [x] ptr is a pointer to an array of 10 integers
- [ ] ptr is an array of 10 integers
- [ ] ptr is an pointer to array

#### Q79. What will be the output of the following code snippet?

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

**Explanation :** The function "change" will change the value of x and y only within its own scope, so a and is unaffected.

#### Q85. Choose true or false.When variable is created in C, a memory address is assigned to the variable.

- [x] True
- [ ] False

#### Q86. What does the following fragment of C-program print?

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

**Explanation :** char c[ ] = "GATE2011";since char \*p =c it means p represents to the base address of string “GATE2011” SO p[3] is 'E' and p[1] is 'A'. Value of Sub expression p[3] – p[1] = ASCII value of ‘E’ – ASCII value of ‘A’ = 4. So the expression p + p[3] – p[1] becomes ( p + 4) And (p+4) represent to base address of string “2011” printf(“%s”, p + p[3] – p[1]) ; So it will print 2011

#### Q87. What is the output of the following code snippet?

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

#### Q88. What will be the output of the following C program segment?

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
