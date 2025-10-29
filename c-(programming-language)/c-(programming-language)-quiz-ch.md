## C语言编程题库

#### Q1. 哪个代码示例最终会导致计算机内存耗尽?

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

#### Q2. 下面的代码输出是什么?

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

- [ ] 屏幕上没有打印任何内容

#### Q3. 在同一个函数内部调用函数本身的名称是什么?

- [x] 递归
- [ ] 子函数
- [ ] 内部调用
- [ ] 无限循环

[参考](https://www.cprogramming.com/tutorial/c/lesson16.html)

#### Q4. 变量c2的声明演示了什么?

```c
main(){
    char c1 ='a';
    char c2 = c1+10;
}
```

- [x] 字符运算
- [ ] 未定义的赋值
- [ ] 类型转换
- [ ] 无效声明

[参考](https://tutorialspoint.dev/language/c/character-arithmetic-c-c)

#### Q5. 这个声明是什么的例子?

```c
struct s {
    int i;
    struct s *s1;
    struct s *s2;
};
```

- [x] 一个节点
- [ ] 一个链表
- [ ] 一个栈
- [ ] 一个二叉树

#### Q6. 头文件使用预处理指令#include列出,可以有以下两种格式:#include &lt;fileA&gt; 或 #include "fileB"。这两种格式有什么区别?

- [ ] 预处理器将尝试在与源文件相同的目录中定位fileA,在预定目录路径中定位fileB。
- [ ] 预处理器将尝试在固定的系统目录中定位fileA。它将尝试在编译源代码时添加到命令行的-I选项指定的目录路径中定位fileB。
- [ ] 使用fileA语法的文件必须是系统文件,数量不限;fileB必须是用户文件,每个源文件最多一个。
- [x] 预处理器将尝试在预定目录路径中定位fileA。它将尝试在与源文件相同的目录以及自定义目录路径中定位fileB。

[参考](https://www.geeksforgeeks.org/difference-between-include-and-include-in-c-c-with-examples/)

#### Q7. 使用for循环,如何编写C代码从10倒数到1并在单独的行上显示每个数字?

- [ ] :

```c
for (int i = 0; i>=0, i--){
    printf("%d\n", i);
}//循环结束
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
}// 循环结束
```

#### Q8. 以下哪个不是标准C中的保留字?

- [ ] volatile
- [x] typeof
- [ ] register
- [ ] typedef

[参考](https://www.ibm.com/docs/en/adfz/developer-for-zos/14.2.0?topic=programs-c-reserved-keywords)

#### Q9. 下面显示的程序返回什么?

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

#### Q10. 使用下面的联合声明,此类型的数据将占用多少字节的内存空间?

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

#### Q11. 在这个代码示例中,对于C编译器来说什么不是问题?

```c
main(){
    constant int PI = 3.14;
    printf("%f\n", pi);
}
```

- [x] PI的值需要设置为3.141593,而不是3.14
- [ ] PI的声明需要使用const,而不是constant。
- [ ] PI的数据类型需要是float,而不是int。
- [ ] printf语句需要使用PI,而不是pi。

#### Q12. 哪个是可以编译和运行而不出错的最小程序?

- [ ] main()
- [x] int main() {return 0;}
- [ ] main() { }
- [ ] main() { ; }

[参考](https://www.beningo.com/150-the-wolrds-shortest-c-program/)

#### Q13. 在函数声明中什么是可选的?

- [ ] 参数的数据类型
- [ ] 函数的返回类型
- [x] 参数名称
- [ ] 参数数量

> **解释:**  
> 在所有现代C标准中,函数声明中的参数名称是可选的。
> 但是,空参数列表(`int f();`)的含义因标准而异:
>
> - **C23之前:** 声明一个参数数量未指定的函数(不是原型)。
> - **在C23中:** 等同于`int f(void);` — 声明一个不接受参数的函数。
>
> [参考](https://en.cppreference.com/w/c/language/function_declaration)

#### Q14. C语言将所有设备(如显示器和键盘)视为文件。程序执行时哪个文件会自动打开?

- [x] stdout
- [ ] stdio.h
- [ ] default.h
- [ ] string.h

#### Q15. 动态内存分配在哪个段中进行?

- [ ] BSS段
- [ ] 栈
- [x] 堆
- [ ] 数据段

[参考](http://www.it.uc3m.es/pbasanta/asng/course_notes/dynamic_memory_heap_en.html)

#### Q16. 使用哪个函数来释放内存?

- [ ] dalloc()
- [ ] dealloc()
- [ ] release()
- [x] free()

[参考](https://devdocs.io/c/memory/free)

#### Q17. 在C语言中,构成程序的基本构建块是什么?

- [ ] 关键字
- [ ] 标识符
- [x] 标记(tokens)
- [ ] 函数

[参考](https://fresh2refresh.com/c-programming/c-tokens-identifiers-keywords/)

#### Q18. 什么时候为变量分配内存?

- [ ] 在变量赋值期间
- [ ] 在变量初始化期间
- [x] 在变量声明期间
- [ ] 在变量定义期间

[参考](https://www.codingame.com/playgrounds/14589/how-to-play-with-pointers-in-c/dynamic-memory-allocation)

#### Q19. C语言使用值传递方法向函数传递参数。如何调用引用传递方法?

- [x] 通过使用指针
- [ ] 通过将函数的声明和定义分开
- [ ] 通过使用递归函数
- [ ] 通过使用全局变量

[参考](https://www.javatpoint.com/call-by-value-and-call-by-reference-in-c)

#### Q20. 联合允许您在同一个`___`中存储不同的`___`。

- [ ] 对象;结构
- [ ] 变量;声明
- [x] 数据类型;内存空间
- [ ] 数组;头文件

#### Q21. 这个程序的输出是什么?

```c
main() {
    char c1='a' , c2='A';
    int i=c2-c1;
    printf("%d", i);
}
```

- [ ] 32
- [ ] 运行时错误
- [x] -32
- [ ] 0

#### Q22. scanf()和sscanf()函数有什么区别?

- [ ] scanf()函数读取格式化为字符串的数据;sscanf()函数从屏幕读取字符串输入。
- [x] scanf()函数从键盘读取格式化数据;sscanf()函数从字符串读取格式化输入。
- [ ] scanf()函数从键盘读取字符串数据;sscanf()函数从字符串读取字符串数据。
- [ ] scanf()函数从文件读取格式化数据;sscanf()函数从选定的字符串读取输入

#### Q23. 使用这个声明,哪个不是有效的命令?

```c
char *string[20] = { "one", "two", "three"};
```

- [ ] `printf("%c", string[1][2]);`
- [x] `printf("%s", string[1][2]);`
- [ ] `printf("%s", string[1]);`
- [ ] `printf(string[1]);`

#### Q24. 表达式player->name等价于什么?

- [ ] `player.name`
- [x] `(*player).name`
- [ ] `*player.name`
- [ ] `player.*name`

#### Q25. 哪个程序可以编译和运行而不出错?

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

#### Q26. 这个函数调用返回什么?

```c
1 main() { float x = f1(10, 5); }
2 float f1(int a, int b) { return (a/b); }
```

- [ ] 2
- [ ] 2.000000
- [ ] 运行时错误
- [x] 编译错误

#### Q27. 这个程序创建了什么?

```c
#include <stdio.h>
int main() {
    int *p = NULL;
    return 0;
}
```

- [ ] 运行时错误
- [x] 一个NULL指针
- [ ] 编译错误
- [ ] 一个void指针

#### Q28. 表达式(\*x).y的另一种写法是什么?

- [ ] 没有等价形式。
- [x] x->y
- [ ] \*x->y
- [ ] y->x

#### Q29. 编译时错误是可以在代码中找到的静态错误。

- [x] 在声明和定义中
- [ ] 在函数和表达式中
- [ ] 在语法和语义中
- [ ] 在对象和语句中

#### Q30. C语言中的文件输入和输出(I/O)在很大程度上基于它在`___`中的实现方式?

- [x] Unix中
- [ ] C++中
- [ ] C#中
- [ ] DOS中

#### Q31. strcmp(str1, str2);函数返回什么?

- [x] 如果str1和str2相同则返回0,如果str1小于str2则返回负数,如果str1大于str2则返回正数
- [ ] 如果str1和str2相同则返回true(1),如果str1和str2不同则返回false(0)
- [ ] 如果str1和str2相同则返回true(1),如果str1和str2不同则返回NULL
- [ ] 如果str1和str2相同则返回0,如果str2小于str1则返回负数,如果str2大于str1则返回正数

#### Q32. 这个程序的输出是什么?

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

#### Q33. 哪个不是声明字符串变量的正确方式?

- [ ] `char *string = "Hello World";`
- [x] `char string = "Hello World";`
- [ ] `char string[20] = {'H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd'};`
- [ ] `char string[] = "Hello World";`

#### Q34. 哪个选择是头文件mylib.h的包含保护?

- [ ] :

```c
#ifdef MYLIB_H
#undef MYLIB_H

// mylib.h内容

#endif /* MYLIB_H */
```

- [x] :

```c
#ifndef MYLIB_H
#define MYLIB_H

// mylib.h内容

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

// mylib.h内容

#endif /* MYLIB_H */
```

#### Q35. 在这个程序中,while循环内的代码执行了多少次?

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

#### Q36. C语言中的文件输入和输出(I/O)是通过什么完成的?

- [ ] 语法驱动组件
- [ ] 原生接口
- [ ] 系统对象
- [x] 函数调用

#### Q37. 指令由什么翻译?

- [x] 预处理器
- [ ] 编译器
- [ ] 链接器
- [ ] 编辑器

#### Q38. C编程中的主要循环结构是for循环、while循环和哪个其他循环?

- [x] do...while
- [ ] for...in
- [ ] repeat...until
- [ ] do...until

#### Q39. 默认情况下,C函数是什么类型的函数?

- [x] 全局
- [ ] 静态
- [ ] 库
- [ ] 系统

#### Q40. 您编写了一个要作为结构'a'成员包含的函数。如何定义这样的结构成员?

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

#### Q41. 栈数据结构只允许在一端进行所有数据操作,这使它成为什么样的实现?

- [ ] FIFO(先进先出)
- [x] LIFO(后进先出)
- [ ] LILO
- [ ] LOLI

#### Q42. 这个程序显示什么?

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

#### Q43. 描述左值和右值之间的关系。

- [ ] 左值只能出现在赋值的左侧;右值只能出现在右侧。
- [ ] 左值只能出现在赋值的左侧;右值可以出现在左侧或右侧。
- [ ] 左值和右值可以出现在赋值的左侧或右侧。
- [x] 左值可以出现在赋值的左侧或右侧;右值只能出现在右侧。

#### Q44. 哪个运算符用于访问变量的地址?

- [ ] `%`
- [ ] `**`
- [ ] `*`
- [x] `&`

#### Q45. 哪个add函数正确返回result的更新值?

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

#### Q46. 考虑100以下的斐波那契数列:0,1,1,2,3,5,8,13,21,34,55,89。哪段代码输出这个序列?

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

#### Q47. 哪个不是存储类说明符?

- [x] `intern`
- [ ] `extern`
- [ ] `register`
- [ ] `static`

[参考](https://en.cppreference.com/w/cpp/language/storage_duration)

#### Q48. 执行后哪行代码使i的值为1?

- [ ] `for(i=1; i<=1; i++);`
- [ ] `for(i=1; i=10; i++);`
- [x] `for(i=1; i==10; i++);`
- [ ] `for(i=10; i>=1; i--);`

#### Q49. 在这个程序结束时变量c的值是多少?

```c
main() {
  int a, b, c;
  a=10; b=50;
  c=a * b % a;
}
```

- [ ] 50
- [ ] 5
- [x] 0
- [ ] 500

#### Q50. 什么不是C语言的基本数据类型之一?

- [ ] long double
- [ ] unsigned char
- [x] array(数组)
- [ ] float

#### Q51. 结构的成员访问运算符是什么?

- [ ] ,
- [ ] []
- [x] .
- [ ] :

#### Q52. 哪种标准数据类型提供最小的存储大小并可用于计算?

- [x] char
- [ ] float
- [ ] int
- [ ] short

#### Q53. ctype tolower()函数做什么?

- [ ] 对于字母表的小写字母返回TRUE。
- [ ] 确保文本输出仅使用ASCII值(0到127)。
- [ ] 对于字母表的小写字母返回FALSE。
- [x] 将字母表的大写字母转换为小写。

#### Q54. void指针vptr被分配了float变量g的地址。稍后在程序中,什么是解引用vptr以将其指向的值分配给名为f的float变量的有效方法?

```c
float g;
void *vptr=&g;
```

- [ ] `f=(float *)vptr;`
- [x] `f=*(float *)vptr;`
- [ ] `f=*(float)vptr;`
- [ ] `f=(float)*vptr;`

#### Q55. 动态内存分配函数在哪个系统头文件中定义?

- [ ] stdio.h
- [x] stdlib.h
- [ ] limits.h
- [ ] stddef.h

#### Q56. 函数是一组**\_\_\_**。

- [ ] 声明
- [x] 语句
- [ ] 变量
- [ ] 对象

#### Q57. 静态函数与全局函数有何不同?

- [ ] 静态函数必须在定义之前声明。
- [ ] 静态函数必须在单独的头文件中声明。
- [ ] 静态函数总是返回相同的值。
- [x] 静态函数只能在声明它们的文件中访问。

#### Q58. 哪个代码示例在存储缓冲区hello中创建字符串"Hello Mars"?

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

#### Q59. 如果使用"a"模式的fopen()函数,如果命名的文件不存在会发生什么?

- [ ] 创建文件并打开以供读取。
- [x] 创建文件并打开以供写入。
- [ ] fopen()函数返回NULL,表示操作失败。
- [ ] 创建文件并打开以供写入和读取

[参考](https://www.tutorialspoint.com/c_standard_library/c_function_fopen.htm)

#### Q60. 这个函数返回什么?

```c
int fl(int a, int b) { return(a>b?a:b); }
```

- [ ] 编译错误
- [ ] 两个传递参数中的较小值
- [ ] 运行时错误
- [x] 两个传递参数中的较大值

#### Q61. 哪个选项是有效的函数名?

- [x] draw_star()
- [ ] 5times()
- [ ] upper-limit()
- [ ] auto()

#### Q62. 什么不是包含x和y坐标作为整数的结构的有效类型定义,并且可以如下所示用于名为point的变量?

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

#### Q63. 下面程序的输出是什么?

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
- [ ] 根据输入为3或5
- [ ] 编译时错误

#### Q64. malloc()和calloc()函数分配什么?

- [ ] 重新分配的内存
- [ ] 静态内存
- [x] 动态内存
- [ ] 碎片内存

[参考](https://devdocs.io/c/memory/calloc)
[参考](https://devdocs.io/c/memory/malloc)

#### Q65. 您需要确定一个字符串变量是否是另一个字符串的子串。您使用哪个标准C库函数?

- [ ] substr(str1, str2);
- [x] strstr(str1, str2);
- [ ] substring(str1, str2);
- [ ] strspn(str1, str2);

[参考](https://devdocs.io/c/string/byte/strstr)

#### Q66. 找出程序的输出。

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

[参考](https://www.geeksforgeeks.org/left-shift-right-shift-operators-c-cpp/)

#### Q67. 当整数变量x初始化为10,y为2,z为0时,预测以下代码的输出。

```c
z = x + y * x + 10 / 2 * x;
printf("value is =%d",z);
```

- [x] 80
- [ ] 170
- [ ] 31.5
- [ ] 6

[参考](https://www.informit.com/articles/article.aspx?p=2062174&seqNum=4)

#### Q68. 以下代码片段的输出是什么?

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

#### Q69. 这个程序的输出是什么?

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

#### Q70. /0字符是什么?

- [ ] 字符串
- [x] NULL字符
- [ ] 零
- [ ] 变量

[参考](https://www.youth4work.com/Talent/C-Language/Forum/117150-what-is-the-use-of-a-0-character-in-c-language)

#### Q71. 以下代码的正确输出是什么?

```c
#include<stdio.h>
#include<conio.h>
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

#### Q72. 哪个选项不正确地解释了#pragma指令?

- [ ] #pragma exit允许我们指定在程序退出时调用的函数。
- [ ] 这是一个预处理器指令,可用于打开或关闭某些功能。
- [x] #pragma startup不允许我们指定在程序启动时调用的函数。
- [ ] 它有两种类型:#pragma startup、#pragma exit和pragma warn。

#### Q73. 以下代码片段的输出是什么?

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

#### Q74. 以下代码片段的输出是什么?

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
- [ ] 编译错误
- [ ] 82 19
- [ ] 以上都不是

#### Q75. 以下代码片段的输出是什么?

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

#### Q76. 以下声明是什么意思?

```c
int (*ptr)[10];
```

- [ ] ptr是指向10个整数的指针数组
- [x] ptr是指向10个整数的数组的指针
- [ ] ptr是10个整数的数组
- [ ] ptr是指向数组的指针

#### Q77. 以下代码片段的输出是什么?

```c
#include <stdio.h>
void change(int,int);
int main()
{
   int a=10,b=20;
   change(a,b); //通过传递变量的值调用函数。
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

**解释:** 函数"change"只会在其自己的作用域内更改x和y的值,因此a和b不受影响。

#### Q78. 选择真或假。当在C中创建变量时,会为该变量分配一个内存地址。

- [x] 真
- [ ] 假

#### Q79. 以下C程序片段打印什么?

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

**解释:** char c[ ] = "GATE2011"; 由于char \*p =c,这意味着p表示字符串"GATE2011"的基地址,所以p[3]是'E',p[1]是'A'。子表达式p[3] – p[1]的值 = 'E'的ASCII值 – 'A'的ASCII值 = 4。因此表达式p + p[3] – p[1]变为(p + 4),而(p+4)表示字符串"2011"的基地址,printf("%s", p + p[3] – p[1]);所以它将打印2011

#### Q80. 以下代码片段的输出是什么?

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

#### Q81. 以下C程序段的输出是什么?

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
- [ ] 程序没有输出,因为它有错误

#### Q82. 字符串变量str1的值为"abc",字符串变量str2的值为"xyz"。执行此语句后str1和str2的值是什么?

```c
strcpy(str1, str2);
```

- [x] str1: "xyz" ; str2: "xyz"
- [ ] str1: "abc" ; str2: "xyz"
- [ ] str1: "xyz" ; str2: "abc"
- [ ] str1: "abc" ; str2: "abc"

#### Q88. 使用这个声明,哪个不是有效的命令?

```c
char *string[20] = { "one", "two", "three"};
```

- [ ] `printf("%c", string[1][2]);`
- [x] `printf("%s", string[1][2]);`
- [ ] `printf("%s", string[1]);`
- [ ] `printf(string[1]);`

#### Q89. 这段代码的输出是什么?

```c
int x = 5;
int y = ++x + x++;
printf("%d %d", x, y);
```

- [ ] 6 11
- [x] 7 12
- [ ] 7 11
- [ ] 6 12

**解释:**
首先,++x将x递增到6并在表达式中使用6。然后x++使用6并在之后将x递增到7。所以y = 6 + 6 = 12,x变为7。

[参考](https://en.cppreference.com/w/c/language/operator_precedence)

#### Q90. C语言中的`volatile`关键字表示什么?

- [ ] 变量不能被修改
- [x] 变量可能被外部因素改变
- [ ] 变量存储在ROM中
- [ ] 变量是常量

**解释:**
`volatile`关键字告诉编译器变量的值可能被外部因素(硬件、中断、其他线程)改变,因此编译器不应优化掉对它的读/写操作。

[参考](https://en.cppreference.com/w/c/language/volatile)

#### Q91. C99中`restrict`关键字的目的是什么?

- [x] 表示指针是访问对象的唯一方式
- [ ] 限制变量的作用域
- [ ] 防止修改变量
- [ ] 限制函数访问

**解释:**
`restrict`关键字是一个类型限定符,可应用于指针。它告诉编译器在指针的生命周期内,只有它或直接从它派生的值将用于访问它指向的对象。这使某些编译器优化成为可能。

[参考](https://en.cppreference.com/w/c/language/restrict)

#### Q92. `malloc()`和`calloc()`有什么区别?

- [ ] malloc比calloc快
- [x] calloc将分配的内存初始化为零,malloc不会
- [ ] malloc可以分配比calloc更多的内存
- [ ] 没有区别

**解释:**
`calloc()`分配内存并将所有字节初始化为零,而`malloc()`分配内存但不初始化。`calloc()`还接受两个参数(元素数量和每个元素的大小),而`malloc()`接受一个(以字节为单位的总大小)。

[参考](https://en.cppreference.com/w/c/memory/calloc)

#### Q93. 什么是悬空指针?

- [ ] 指向NULL的指针
- [x] 指向已释放或删除内存的指针
- [ ] 未初始化的指针
- [ ] 指向常量的指针

**解释:**
悬空指针是指向已释放或删除的内存的指针。访问这样的指针会导致未定义的行为。

[参考](https://en.wikipedia.org/wiki/Dangling_pointer)

#### Q94. 这段代码的输出是什么?

```c
int arr[] = {1, 2, 3, 4, 5};
printf("%d", *(arr + 3));
```

- [ ] 1
- [ ] 2
- [ ] 3
- [x] 4

**解释:**
`arr`是指向第一个元素的指针。`arr + 3`指向第4个元素(索引3)。`*`运算符解引用它以获取值4。

[参考](https://en.cppreference.com/w/c/language/operator_member_access)

#### Q95. 将`static`关键字应用于函数时会做什么?

- [x] 将函数的作用域限制到当前文件
- [ ] 使函数运行更快
- [ ] 阻止函数被调用
- [ ] 使函数内联

**解释:**
当`static`应用于函数时,它将函数的链接限制为内部链接,这意味着它只能从同一翻译单元(源文件)内调用。

[参考](https://en.cppreference.com/w/c/language/storage_duration)

#### Q96. 在64位系统中指针的大小是多少?

- [ ] 4字节
- [x] 8字节
- [ ] 16字节
- [ ] 取决于它指向的内容

**解释:**
在64位系统上,指针通常是8字节(64位),无论它们指向什么。大小由系统架构决定,而不是由指向的类型决定。

[参考](https://en.cppreference.com/w/c/language/pointer)

#### Q97. `typedef`的目的是什么?

- [ ] 定义新的数据类型
- [x] 为现有数据类型创建别名
- [ ] 声明变量
- [ ] 定义宏

**解释:**
`typedef`为现有数据类型创建别名(替代名称)。它不创建新类型,只是为现有类型创建新名称。

[参考](https://en.cppreference.com/w/c/language/typedef)

#### Q98. 什么是内存泄漏?

- [ ] 当指针指向无效内存时
- [x] 当分配的内存未被释放时
- [ ] 当变量超出作用域时
- [ ] 当发生栈溢出时

**解释:**
当动态分配的内存(通过`malloc`、`calloc`等)未使用`free()`释放时,就会发生内存泄漏,导致程序随时间消耗越来越多的内存。

[参考](https://en.wikipedia.org/wiki/Memory_leak)

#### Q99. 这段代码的输出是什么?

```c
int x = 10;
int *p = &x;
*p = 20;
printf("%d", x);
```

- [ ] 10
- [x] 20
- [ ] x的地址
- [ ] 未定义

**解释:**
`p`指向`x`。`*p = 20`修改p指向的地址处的值,即`x`。所以`x`变为20。

[参考](https://en.cppreference.com/w/c/language/pointer)

#### Q100. C语言中`sizeof(char)`总是返回什么?

- [x] 1
- [ ] 2
- [ ] 4
- [ ] 取决于系统

**解释:**
根据C标准的定义,`sizeof(char)`始终为1。这是C中大小的基本单位,所有其他大小都是它的倍数。

[参考](https://en.cppreference.com/w/c/language/sizeof)

#### Q101. `++i`和`i++`有什么区别?

- [x] ++i在使用前递增,i++在使用后递增
- [ ] ++i比i++快
- [ ] i++只能在循环中使用
- [ ] 没有区别

**解释:**
`++i`(前置递增)递增变量并返回新值。`i++`(后置递增)返回当前值,然后递增变量。

[参考](https://en.cppreference.com/w/c/language/operator_incdec)

#### Q102. 什么是段错误?

- [ ] 语法错误
- [x] 由访问无效内存引起的错误
- [ ] 编译错误
- [ ] 警告

**解释:**
段错误(segfault)发生在程序尝试访问不允许访问的内存时,例如解引用NULL指针或访问已释放的内存。

[参考](https://en.wikipedia.org/wiki/Segmentation_fault)

#### Q103. `const`关键字与指针的目的是什么?

```c
const int *p;
```

- [x] 通过p指向的值不能被修改
- [ ] 指针p不能被修改
- [ ] 指针和值都是常量
- [ ] 它没有效果

**解释:**
`const int *p`表示p指向一个常整数 - 您不能通过p修改值,但可以更改p指向的位置。对于`int * const p`,指针本身是常量。

[参考](https://en.cppreference.com/w/c/language/const)

#### Q104. 这段代码的输出是什么?

```c
int arr[5] = {1, 2, 3, 4, 5};
printf("%d", arr[4]);
```

- [ ] 1
- [ ] 2
- [ ] 3
- [x] 4

**解释:**
`arr`是指向第一个元素的指针。`arr + 3`指向第4个元素(索引3)。`*`运算符解引用它以获取值4。

[参考](https://en.cppreference.com/w/c/language/operator_member_access)

#### Q105. `extern`关键字做什么?

- [ ] 使变量在程序外部
- [x] 声明在其他地方定义的变量
- [ ] 将变量导出到其他程序
- [ ] 创建全局变量

**解释:**
`extern`声明在另一个源文件或同一文件的后面定义的变量或函数。它告诉编译器定义存在于其他地方。

[参考](https://en.cppreference.com/w/c/language/extern)

#### Q106. `struct`和`union`有什么区别?

- [x] struct成员有单独的内存,union成员共享内存
- [ ] struct比union快
- [ ] union可以有比struct更多的成员
- [ ] 没有区别

**解释:**
在`struct`中,每个成员都有自己的内存位置。在`union`中,所有成员共享同一内存位置,一次只能有一个成员保存值。联合的大小是其最大成员的大小。

[参考](https://en.cppreference.com/w/c/language/union)

#### Q107. 这段代码的输出是什么?

```c
int x = 5;
printf("%d", x << 2);
```

- [ ] 5
- [ ] 7
- [x] 20
- [ ] 10

**解释:**
`<<`运算符是左位移。`x << 2`将x的位左移2个位置,这相当于乘以2^2 = 4。所以5 \* 4 = 20。

[参考](https://en.cppreference.com/w/c/language/operator_arithmetic)

#### Q108. 什么是函数指针?

- [ ] 指向函数返回值的指针
- [x] 存储函数地址的指针
- [ ] 返回指针的函数
- [ ] 函数内部的指针

**解释:**
函数指针是存储函数地址的变量。它可用于间接调用函数或将函数作为参数传递给其他函数。

[参考](https://en.cppreference.com/w/c/language/pointer#Pointers_to_functions)

#### Q109. C语言中`NULL`代表什么?

- [ ] 数字零
- [x] 空指针常量
- [ ] 空字符串
- [ ] 未定义的值

**解释:**
`NULL`是表示空指针常量的宏。它通常定义为`((void*)0)`或只是`0`。它表示指针不指向任何有效的内存位置。

[参考](https://en.cppreference.com/w/c/types/NULL)

#### Q110. 这段代码的输出是什么?

```c
int x = 10;
int y = 20;
int *p1 = &x, *p2 = &y;
*p1 = *p2;
printf("%d %d", x, y);
```

- [ ] 10 20
- [x] 20 20
- [ ] 10 10
- [ ] 20 10

**解释:**
`*p1 = *p2`将p2指向的值(即20)复制到p1指向的位置(即x)。所以x变为20,y保持20。

[参考](https://en.cppreference.com/w/c/language/pointer)

#### Q111. `#pragma`指令的目的是什么?

- [ ] 包含头文件
- [ ] 定义宏
- [x] 提供编译器特定的指令
- [ ] 声明变量

**解释:**
`#pragma`是一个预处理器指令,向编译器提供额外信息。它是实现定义的,用于编译器特定的功能。

[参考](https://en.cppreference.com/w/c/preprocessor/impl)

#### Q112. `break`和`continue`有什么区别?

- [x] break退出循环,continue跳到下一次迭代
- [ ] break比continue快
- [ ] continue退出循环,break跳过迭代
- [ ] 没有区别

**解释:**
`break`完全终止循环并在循环后继续执行。`continue`跳过当前迭代的其余部分并移至循环的下一次迭代。

[参考](https://en.cppreference.com/w/c/language/break)

#### Q113. 这段代码的输出是什么?

```c
int arr[] = {1, 2, 3, 4, 5};
printf("%d", sizeof(arr) / sizeof(arr[0]));
```

- [ ] 4
- [x] 5
- [ ] 20
- [ ] 1

**解释:**
`sizeof(arr)`给出数组的总大小(以字节为单位)。`sizeof(arr[0])`给出一个元素的大小。将它们相除得到元素数量:5。

[参考](https://en.cppreference.com/w/c/language/sizeof)

#### Q114. 什么是void指针?

- [ ] 指向空的指针
- [x] 可以指向任何数据类型的通用指针
- [ ] 指向void函数的指针
- [ ] 无效指针

**解释:**
`void*`指针是可以指向任何数据类型的通用指针。在解引用之前必须强制转换为适当的类型。

[参考](https://en.cppreference.com/w/c/language/pointer)

#### Q115. `register`关键字向编译器建议什么?

- [ ] 使变量成为全局变量
- [x] 将变量存储在CPU寄存器中以便更快访问
- [ ] 保护变量不被修改
- [ ] 在堆上分配内存

**解释:**
`register`关键字建议(但不保证)编译器应将变量存储在CPU寄存器中以便更快访问。现代编译器通常忽略此提示并做出自己的优化决策。

[参考](https://en.cppreference.com/w/c/language/storage_duration)

#### Q116. 这段代码的输出是什么?

```c
int x = 5;
int y = (x > 3) ? 10 : 20;
printf("%d", y);
```

- [x] 10
- [ ] 20
- [ ] 5
- [ ] 3

**解释:**
这是三元运算符。由于x > 3为真,y被赋值为10。

[参考](https://en.cppreference.com/w/c/language/operator_other)

#### Q117. `malloc()`和`realloc()`有什么区别?

- [ ] malloc比realloc快
- [x] realloc调整先前分配的内存大小
- [ ] malloc初始化内存,realloc不会
- [ ] 没有区别

**解释:**
`malloc()`分配新内存。`realloc()`更改先前分配的内存块的大小,如果需要,可能将其移动到新位置。

[参考](https://en.cppreference.com/w/c/memory/realloc)

#### Q118. C语言中的枚举是什么?

- [ ] 循环结构
- [x] 由命名整数常量组成的用户定义类型
- [ ] 计数元素的函数
- [ ] 常量数组

**解释:**
枚举(`enum`)是由一组命名整数常量组成的用户定义类型。它通过为整数值提供有意义的名称使代码更具可读性。

[参考](https://en.cppreference.com/w/c/language/enum)

#### Q119. 这段代码的输出是什么?

```c
int x = 10;
int y = x++ + ++x;
printf("%d %d", x, y);
```

- [ ] 11 21
- [x] 12 22
- [ ] 12 21
- [ ] 11 22

**解释:**
首先,x++使用10并将x递增到11。然后++x将x递增到12并使用12。所以y = 10 + 12 = 22,x是12。

[参考](https://en.cppreference.com/w/c/language/operator_incdec)

#### Q120. `assert()`宏的目的是什么?

- [ ] 为变量赋值
- [x] 检查假设,如果为假则终止
- [ ] 对其他函数主张优势
- [ ] 在文档中创建断言

**解释:**
`assert()`是用于调试的宏。它检查条件是否为真。如果为假,它会打印错误消息并终止程序。它通常在发布版本中被禁用。

[参考](https://en.cppreference.com/w/c/error/assert)

#### Q121. `fgets()`和`gets()`有什么区别?

- [ ] fgets比gets快
- [x] fgets更安全,因为它限制输入大小
- [ ] gets可以从任何文件读取
- [ ] 没有区别

**解释:**
`gets()`不安全,因为它不检查缓冲区大小,导致缓冲区溢出漏洞。`fgets()`允许您指定要读取的最大字符数,使其更安全。`gets()`已从C11标准中删除。

[参考](https://en.cppreference.com/w/c/io/fgets)

#### Q122. 这段代码的输出是什么?

```c
int x = 5;
int *p = &x;
printf("%p %p", (void*)&x, (void*)p);
```

- [x] 打印两次相同的地址
- [ ] 两个不同的地址
- [ ] 编译错误
- [ ] 5 5

**解释:**
`&x`给出x的地址,p存储x的地址。两者都打印相同的地址(由于%p以十六进制格式)。

[参考](https://en.cppreference.com/w/c/io/fprintf)

#### Q123. 什么是预处理器指令?

- [ ] 处理数据的函数
- [x] 编译前给预处理器的指令
- [ ] 来自处理器的指令
- [ ] 一种循环类型

**解释:**
预处理器指令(如#include、#define、#ifdef)是在实际编译之前处理的指令。它们以#开头并由预处理器处理。

[参考](https://en.cppreference.com/w/c/preprocessor)

#### Q124. 这段代码的输出是什么?

```c
int arr[3][3] = { {1,2,3},{4,5,6},{7,8,9} };
printf("%d", arr[1][2]);
```

- [ ] 5
- [x] 6
- [ ] 8
- [ ] 9

**解释:**
`arr[1][2]`访问第1行(第二行:{4,5,6}),第2列(第三个元素:6)。

[参考](https://en.cppreference.com/w/c/language/array)

#### Q125. `memset()`函数的目的是什么?

- [ ] 分配内存
- [x] 用特定值填充内存块
- [ ] 复制内存
- [ ] 释放内存

**解释:**
`memset()`用指定的字节值填充内存块。它通常用于将数组或结构初始化为零。

[参考](https://en.cppreference.com/w/c/string/byte/memset)

#### Q126. `strcpy()`和`strncpy()`有什么区别?

- [ ] strcpy更快
- [x] strncpy限制复制的字符数
- [ ] strcpy可以复制任何数据类型
- [ ] 没有区别

**解释:**
`strcpy()`复制整个字符串,包括空终止符。`strncpy()`最多复制n个字符,提供防止缓冲区溢出的保护。

[参考](https://en.cppreference.com/w/c/string/byte/strncpy)

#### Q127. 这段代码的输出是什么?

```c
int x = 10;
int y = 3;
printf("%d", x % y);
```

- [x] 1
- [ ] 3
- [ ] 0
- [ ] 10

**解释:**
`%`运算符是模运算符。10 % 3给出10除以3的余数,即1。

[参考](https://en.cppreference.com/w/c/language/operator_arithmetic)

#### Q128. C语言中的宏是什么?

- [ ] 大型函数
- [x] 定义代码片段的预处理器指令
- [ ] 一种变量类型
- [ ] 循环结构

**解释:**
宏使用#define定义,表示在编译前由预处理器替换的代码片段。它可以是常量或类似函数的结构。

[参考](https://en.cppreference.com/w/c/preprocessor/replace)

#### Q129. 这段代码的输出是什么?

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

**解释:**
三元运算符检查x > y。由于它为假(5不大于10),z被赋值为y的值,即10。

[参考](https://en.cppreference.com/w/c/language/operator_other)

#### Q130. `free()`函数的目的是什么?

- [ ] 释放CPU资源
- [x] 释放动态分配的内存
- [ ] 从作用域释放变量
- [ ] 清除屏幕

**解释:**
`free()`释放先前由`malloc()`、`calloc()`或`realloc()`分配的内存。这对于防止内存泄漏至关重要。

[参考](https://en.cppreference.com/w/c/memory/free)

#### Q131. 这段代码的输出是什么?

```c
char str[] = "Hello";
printf("%d", strlen(str));
```

- [ ] 6
- [x] 5
- [ ] 4
- [ ] 未定义

**解释:**
`strlen()`返回字符串的长度,不包括空终止符。"Hello"有5个字符。

[参考](https://en.cppreference.com/w/c/string/byte/strlen)

#### Q132. 函数内部的静态变量是什么?

- [ ] 不能改变的变量
- [x] 在函数调用之间保留其值的变量
- [ ] 存储在ROM中的变量
- [ ] 全局变量

**解释:**
函数内部的静态变量在函数调用之间保留其值。它只初始化一次,在程序的生命周期内存在。

[参考](https://en.cppreference.com/w/c/language/storage_duration)

#### Q133. 这段代码的输出是什么?

```c
int arr[] = {1, 2, 3, 4, 5};
int *p = arr + 2;
printf("%d", *p);
```

- [ ] 1
- [ ] 2
- [x] 3
- [ ] 4

**解释:**
`arr + 2`指向第三个元素(索引2)。用`*p`解引用它得到值3。

[参考](https://en.cppreference.com/w/c/language/operator_member_access)

#### Q134. `printf()`和`sprintf()`有什么区别?

- [ ] printf更快
- [x] sprintf写入字符串,printf写入stdout
- [ ] sprintf只能打印字符串
- [ ] 没有区别

**解释:**
`printf()`将格式化输出写入stdout(控制台)。`sprintf()`将格式化输出写入字符串缓冲区。

[参考](https://en.cppreference.com/w/c/io/fprintf)

#### Q135. 这段代码的输出是什么?

```c
int x = 5;
printf("%d", x & 3);
```

- [ ] 5
- [ ] 3
- [x] 1
- [ ] 8

**解释:**
`&`运算符是按位与。5的二进制是101,3是011。101 & 011 = 001 = 1。

[参考](https://en.cppreference.com/w/c/language/operator_arithmetic)

#### Q136. 什么是头文件保护?

- [ ] 安全功能
- [x] 防止多次包含的预处理器结构
- [ ] 保护头文件的函数
- [ ] 一种注释类型

**解释:**
头文件保护(使用#ifndef、#define、#endif)防止头文件在同一编译单元中被多次包含,这会导致重定义错误。

[参考](https://en.cppreference.com/w/c/preprocessor/conditional)

#### Q137. 这段代码的输出是什么?

```c
int x = 10;
int y = 20;
int *p = &x;
p = &y;
printf("%d", *p);
```

- [ ] 10
- [x] 20
- [ ] x的地址
- [ ] y的地址

**解释:**
最初p指向x。然后`p = &y`使p指向y。`*p`解引用p以获取y的值,即20。

[参考](https://en.cppreference.com/w/c/language/pointer)

#### Q138. `memcpy()`函数的目的是什么?

- [ ] 分配内存
- [x] 从源复制内存块到目标
- [ ] 比较内存块
- [ ] 释放内存

**解释:**
`memcpy()`从源内存复制n个字节到目标内存。它比逐个元素复制更快,但不处理重叠的内存区域(为此使用`memmove()`)。

[参考](https://en.cppreference.com/w/c/string/byte/memcpy)

#### Q139. 这段代码的输出是什么?

```c
int x = 5;
printf("%d", x | 3);
```

- [ ] 3
- [ ] 5
- [x] 7
- [ ] 8

**解释:**
`|`运算符是按位或。5的二进制是101,3是011。101 | 011 = 111 = 7。

[参考](https://en.cppreference.com/w/c/language/operator_arithmetic)

#### Q140. `strcmp()`和`strncmp()`有什么区别?

- [ ] strcmp区分大小写,strncmp不区分
- [x] strncmp只比较前n个字符
- [ ] strcmp更快
- [ ] 没有区别

**解释:**
`strcmp()`比较整个字符串。`strncmp()`最多比较n个字符,这对于比较字符串前缀或限制比较长度很有用。

[参考](https://en.cppreference.com/w/c/string/byte/strncmp)
