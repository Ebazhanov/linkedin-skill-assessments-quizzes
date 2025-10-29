## C++

#### Q1. 这段代码的输出是什么？

```cpp
vector<int> v(22);
bool b = (v[6]);
printf("%d", !b);
```

- [ ] False
- [ ] 0
- [x] 1
- [ ] 此代码有错误。

#### Q2. 以下哪项是使用这一行被认为是不良实践的原因？（_备选_：为什么使用这一行被认为是不良实践？）

```cpp
using namespace std;
```

- [ ] 由于导入了所有符号，编译后的代码总是更大。
- [x] 如果代码使用了两个不同库中定义的具有相同原型但可能具有不同实现的函数，则会因歧义而发生编译错误。
- [ ] 它会自动包含标准库中的所有头文件（cstdint、cstdlib、cstdio、iostream等）。
- [ ] 它会导致编译器强制排他性地包含属于标准库的头文件，当包含不同的头文件时会产生编译错误。

[参考](https://www.geeksforgeeks.org/using-namespace-std-considered-bad-practice/)

#### Q3. child_t 类型的变量在内存中可能占用的最小大小是多少？

```cpp
typedef struct{
    unsigned int  age    : 4;
    unsigned char gender : 1;
    unsigned int  size   : 2;
}child_t;
```

- [ ] 7位。
- [ ] 25字节。
- [ ] 1位。
- [x] 1字节。

[参考](https://en.cppreference.com/w/cpp/language/bit_field)

#### Q4. 执行代码后，向量v1和v2是什么？

```cpp
std::vector<int> v1{1,2,3},v2;
v2=v1;
v1.push_back(4);
v2.push_back(5);
```

- [ ] 错误
- [ ] v1:{1,2,3,4}; v2:{5};
- [ ] v1:{1,2,3,4,5}; v2:{1,2,3,4,5};
- [x] v1:{1,2,3,4}; v2:{1,2,3,5};

#### Q5. 关于指针和迭代器之间的区别，以下哪项是正确的陈述？

- [ ] 虽然指针是保存内存地址的变量，但迭代器是用于遍历容器的通用函数。此函数允许程序员在遍历容器时实现读写代码。
- [x] 递增迭代器总是意味着访问容器中的下一个元素（如果有的话），无论容器是什么。递增指针意味着指向内存中的下一个元素，不一定是下一个元素。
- [ ] 指针是保存内存地址的变量，而迭代器是引用数组中偏移量的无符号整数。
- [ ] 所有迭代器都是用指针实现的，所以所有迭代器都是指针，但并非所有指针都是迭代器。

[参考](https://stackoverflow.com/a/31128162)

#### Q6. u1 占用的存储空间是多少？

```cpp
union {
    uint16_t a;
    uint32_t b;
    int8_t c;
} u1;
```

- [x] 4字节
- [ ] 7字节
- [ ] 8字节
- [ ] 2字节

[参考](https://en.cppreference.com/w/cpp/language/union)

#### Q7. 以下哪个运算符可以被重载？

- [ ] `?:`
- [x] `new`
- [ ] `::`
- [ ] `.`

[参考](https://www.tutorialspoint.com/operators-that-cannot-be-overloaded-in-cplusplus)

#### Q8. 运行此代码后，v1和v2指向的向量的内容是什么？

```cpp
std:: vector<int> *v1 = new std::vector<int>({1,2,3});
std:: vector<int> *v2;
v2=v1;
v1->push_back(4);
v2->push_back(5);
```

- [ ] `*v1:{1,2,3,4}; *v2:{5};`
- [x] `*v1:{1,2,3,4,5}; *v2:{1,2,3,4,5};`
- [ ] 错误
- [ ] `*v1:{1,2,3,4}; *v2:{1,2,3,5};`

v1和v2指向同一个向量。

#### Q9. 以下哪项不是类和结构体之间的区别？

- [ ] 因为结构体是C编程语言的一部分，所以C和C++结构体之间存在一些复杂性。类则没有这种情况。
- [ ] 类可以有成员函数；结构体是私有的。
- [ ] 结构体成员的默认访问说明符是公共的，而类成员的默认访问说明符是私有的。
- [x] 模板类型参数可以用类声明，但不能用struct关键字声明。

模板可以与类和结构体一起使用  
[参考](https://docs.microsoft.com/en-us/cpp/cpp/struct-cpp?view=msvc-170)  
[参考](https://www.fluentcpp.com/2017/06/13/the-real-difference-between-struct-class/)

#### Q10. 假设您需要保留一个数据结构，其中包含基于星期几访问某些资源的权限，但您不能为每天使用bool变量。您需要每周一天使用一位。以下哪项是此应用程序位字段结构的正确实现？

- [x] A

```cpp
typedef struct {
    int sunday:1;
    int monday:1;
    // 更多天数
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
    // 更多天数
    bit friday:1;
    bit saturday:1;
} weekdays;

```

- [ ] D

```cpp
typedef struct {
    bit sunday;
    bit monday;
    // 更多天数
    bit friday;
    bit saturday;
} weekdays;
```

[参考](https://en.cppreference.com/w/cpp/language/bit_field) _注意_：正确的语法是每个变量的大小为1位。`bit`不是C++中的类型。

#### Q11. 什么是左值？

- [ ] 它是一个常量表达式，意味着由常量和操作组成的表达式。
- [ ] 它是一个表示具有地址的对象的表达式。
- [ ] 它是一个适合在二元操作中作为左侧操作数的表达式。
- [x] 它是一个位置值，意味着适合赋值给指针或引用的内存地址。

#### Q12. 自动类型说明符在这行代码中做什么（自C++11起）？

```cpp
auto x = 4000.22;
```

- [x] 它指定x的类型将从初始化器推导出来 - 在这种情况下是double。
- [ ] 它指定x的类型是自动的，这意味着它可以在整个程序中分配不同类型的数据。
- [ ] 它指定x是一个具有自动存储期的变量。
- [ ] 它指定如果x需要更多空间，将为x分配更多内存，避免由于溢出而导致的数据丢失。

#### Q13. 类模板是什么？

- [x] 用泛型编程范式编写的类，用类型参数而不是特定类型指定行为。
- [ ] 用于继承和多态性的空白超类。
- [ ] 仅由成员变量组成的类，没有构造函数、析构函数或成员函数。
- [ ] 类的骨架源代码，程序员必须填写特定部分以定义使用的数据类型和算法。

[参考](https://www.mygreatlearning.com/blog/templates-in-cpp/)

#### Q14. 三元运算符等价于这段代码片段？

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

[参考](https://www.w3schools.com/cpp/cpp_conditions_shorthand.asp)

#### Q15. 下面给出的代码的输出是什么？

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

#### Q16. 范围for循环中括号之间由冒号分隔的两部分的含义是什么？

- [x] 第一个是一个变量声明，将保存序列中的元素。第二个是要遍历的序列。
- [ ] 第一个是迭代器，第二个是要添加到迭代器的增量值。
- [ ] 第一个是迭代变量。第二个是一个`std::pair`，指定变量将在其中迭代的范围（开始和结束）。
- [ ] 第一个是容器对象。第二个是一个`std::pair`，指定将在循环内访问元素的范围（开始和结束）。

#### Q17. 下面给出的代码的输出是什么？

```cpp
int8_t a=200;
uint8_t b=100;
if(a>b)
    std::cout<<"greater";
else
    std::cout<<"less";
```

- [ ] 没有输出，因为在比较int8_t和uint8_t时会发生异常。
- [ ] greater
- [x] less
- [ ] 没有输出，因为存在编译器错误。

注意：下面问题的变体。

#### Q18. 这段代码块的输出是什么？

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

注意：从'int'到'int8_t'（又名'signed char'）的隐式转换将值从200更改为-56

#### Q19. 执行此代码片段后的输出是什么？

```cpp
int x=5, y=2;
if(x & y) {
    /*_part A_*/
}
else {
    /*_part B_*/
}
```

- [ ] 部分A执行，因为x==5（真）且y==2（真），因此AND操作评估为真。
- [x] 部分B执行，因为(x & y)的结果为0，即假。
- [ ] 部分A执行，因为(x & y)的结果为非零值，即真。
- [ ] 部分B执行，因为语句(x & y)无效，因此为假。

[参考](https://stackoverflow.com/questions/63867765/dont-understand-why-if-5-2-is-false)

#### Q20. `get_length`函数的有效定义是什么，该函数返回以空字符结尾的字符串的长度？

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

#### Q21. 哪个STL类最适合实现始终排序的数据集合，以便pop操作始终获得元素中最大的元素？假设您只对push和pop操作感兴趣。

- [ ] `std::list`
- [ ] `std::vector`
- [x] `std::priority_queue`
- [ ] `std::map`

#### Q22. for循环中括号之间由分号分隔的三个部分的含义是什么？

- [ ] 第一个是迭代变量名称，第二个是迭代次数，第三个是所需的增量或减量（用带符号整数指定）。
- [x] 第一个是初始化块，第二个是迭代条件，第三个是增量块。
- [ ] 第一个是迭代变量，第二个是它应该操作的容器，第三个是随时中止的退出条件。
- [ ] 第一个是迭代变量名称，第二个是迭代变量的起始值，第三个是停止值（最后一个值加一）。

#### Q23. 这段代码打印什么？

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

[参考](https://www.geeksforgeeks.org/pre-increment-and-post-increment-in-c/)

#### Q24. 关于名为`ptr`的变量，以下哪项是正确的？

```cpp
void *ptr;
```

- [ ] 它是一个初始化为NULL的指针。
- [ ] 它是一个指向void函数的指针。
- [ ] 该声明会导致编译器错误，因为指针必须指定类型。
- [x] 它是一个指向没有特定类型的值的指针，因此可以转换为指向任何类型。

[参考](https://en.cppreference.com/w/cpp/language/pointer)

#### Q25. 下面给出的代码的输出是什么？

```cpp
int c=3; char d='A';
std::printf("c is %d and d is %c",c,d);
```

- [ ] c is d and d is c
- [ ] c is A and d is 3
- [x] c is 3 and d is A
- [ ] c is c and d is d

#### Q26. 这段代码的输出是什么？

```cpp
printf("1/2 = %f",(float)(1/2));
```

- [ ] 1/2 = 0.499999
- [ ] 1/2 = 0
- [x] 1/2 = 0.000000
- [ ] 1/2 = 0.5

#### Q27. 公共类成员和私有类成员之间的区别是什么？

- [ ] 公共成员与全局变量相同，因此代码的每个部分都可以访问它们。私有成员与自动变量相同，因此只有它们的类可以访问它们。
- [ ] 公共成员对任何运行的应用程序都是可访问的。私有成员仅对实例化对象的应用程序可访问。
- [ ] 公共成员将在多线程环境中编译为共享变量。私有成员将编译为线程局部变量。
- [x] 公共成员可以被任何函数访问。私有成员只能被同一类的成员函数和类的友元访问。

[参考](https://www.geeksforgeeks.org/difference-between-public-and-private-in-c-with-example/)

#### Q28. 执行此代码后`x`的值是多少？

```cpp
int x=10, a=-3;
x+=a;
```

- [ ] 3
- [x] 7
- [ ] -3
- [ ] 13

#### Q29. 以下哪项陈述是正确的？

- [ ] 只有类才能有成员变量和方法。
- [x] C++支持多重继承。
- [ ] C++只支持单继承。
- [ ] 只有结构体可以继承。

#### Q30. 考虑一个指向void的指针，名为`ptr`，它已设置为指向浮点变量`g`。以下哪个选择是解引用`ptr`以将其指向的值分配给程序后面的float变量`f`的有效方法？

```cpp
float g;
void *ptr=&g;
```

- [ ] `float f=*(float)ptr;`
- [ ] `float f=(float *)ptr;`
- [ ] `float f=(float)*ptr;`
- [x] `float f=*(float *)ptr;`

#### Q31. `.*`运算符是什么，它做什么？

- [ ] 它与类成员访问运算符或箭头运算符`(->)`相同，它允许您通过指向对象的指针访问对象的成员。
- [x] 它是指向成员运算符的指针，它允许您通过指向该特定类成员的指针访问对象的成员。
- [ ] 它是带有运算符地址的成员访问，它返回类或结构成员的地址。
- [ ] 它是成员访问运算符`(.)`和解引用运算符`(*)`的组合，因此它允许您访问成员指针指向的对象。

[参考](https://en.cppreference.com/w/cpp/language/operator_member_access)

#### Q32. 对于这些声明，哪个选择显示了四种等效的方法来将字符串中的字符"y"分配给char变量c？

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

#### Q33. 从Animal类派生的名为Dog的类的正确声明是哪个选择？

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

#### Q34. 下面给出的代码的输出是什么？

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

从技术上讲，`char`是`signed`还是`unsigned`是实现定义的；
在后一种情况下，第二个答案是正确的。
[参考](https://en.cppreference.com/w/cpp/language/types)

#### Q35. C++代码如何调用C函数？

- [ ] 直接调用C代码
- [ ] C++无法调用C函数
- [x] 使用extern "C"
- [ ] 导入C源代码

#### Q36. 以下哪个选择不是包含x和y坐标作为整数的结构的有效类型定义，并且可以完全按照为名为`center`的变量所示的方式使用？

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

#### Q37. 以下哪个选择不会产生与此代码片段相同的输出？假设变量`i`不会在代码的其他地方使用。

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

#### Q38. main.cpp文件的这一部分做什么？

```cpp
#include "library.h"
```

- [ ] 它导致工具链编译library.h的所有内容，以便在最终应用程序需要时其可执行代码可用。
- [ ] 它为源文件main.cpp中使用的所有数据和函数的声明和定义挑选library.h，最后用这些声明和定义替换`#include`指令。
- [ ] 它通知链接器，源文件main.cpp中使用的某些函数或数据包含在library.h中，以便它们可以在运行时调用。这也称为动态链接。
- [x] 它导致用源文件library.h的整个内容替换`#include`指令。这类似于将library.h复制粘贴到main.cpp中的操作。

#### Q39. 考虑`is_even`的这个函数声明，它接受一个整数，如果参数是偶数则返回true，否则返回false。以下哪些声明是该函数的重载版本的正确声明，以支持浮点数和数字的字符串表示？

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

#### Q40. 以下哪个选择是头文件`my_library.h`的包含保护？

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

#### Q41. 使用C++11之前的编译器时，这个定义有什么问题？

```cpp
std::vector<std::vector<int>> thematrix;
```

- [ ] 它没有任何问题。
- [ ] `std::vector`不能包含更多`std::vector`容器作为其元素。
- [ ] 正确的语法应该是：`std::vector[std::vector[int]] thematrix;`
- [x] `>>`被解析为右移运算符，因此导致编译错误。

#### Q42. 下面的语句等价于什么？

#### Q42.b. 该语句等价于什么？

```cpp
sprite->x
```

- [ ] `sprite.x`
- [ ] `sprite.*x`
- [x] `(*sprite).x`
- [ ] `*sprite.x`

#### Q43. 考虑一个名为`complexNumber`的类。以下哪段代码将产生等效的对象？

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

#### Q44. 执行此代码片段的结果是什么？

```cpp
bool x=true, y=false;

if (~x || y) {
    /*part A*/
} else {
    /*part B*/
}
```

- [ ] 部分A执行，因为如果`y==false`，表达式`(~x || y)`总是为真。
- [ ] 部分B执行，因为语句`(~x || y)`无效，因此为假。
- [x] 部分A执行，因为`~x`不为零，意味着真。
- [ ] 部分B执行，因为`~x`为假且`y`为假，因此OR操作评估为假。

#### Q45. 这段代码的输出是什么？

```cpp
int32_t nums[3]={2,4,3};
std::cout << ( nums[0] << nums[1] << nums[2] );
```

- [ ] 输出是`nums[0]`、`nums[1]`和`nums[2]`的地址，按顺序，没有空格。
- [x] 256
- [ ] `0`
- [ ] `243`

#### Q46. 这段代码的输出是什么？

```cpp
float values[5]={0.54f, 2.71828f, 3.14159f, 5.499999f, 10.0f};
for(auto f:values)
    printf("%i ",(int)(f+0.5f));
```

- [ ] `0.54 2.71828 3.14159 5.499999 10.0`
- [ ] `1 3 4 6 11`
- [ ] `0 2 3 5 10`
- [x] `1 3 3 5 10`

#### Q47. 以下哪个STL类最适合实现电话簿？假设每个条目包含一个姓名和一个电话号码，没有重复项，并且您希望按姓名查找。

- [ ] `std::priority_queue`
- [ ] `std::list`
- [ ] `std::vector`
- [x] `std::map`

[参考](https://en.cppreference.com/w/cpp/container/map)

#### Q48. 这个程序做什么？

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

- [ ] 它将text1.txt重命名为text2.txt。
- [ ] 它创建一个名为text2.txt的目录并将text1.txt移动到那里。
- [x] 它将text1.txt的内容复制到text2.txt中 - 即，它创建text1.txt的副本，命名为text2.txt。
- [ ] 它将text1.txt的内容追加到text2.txt中 - 即，用text2.txt和text1.txt的连接替换text2.txt的内容。

[参考](https://en.cppreference.com/w/cpp/header/fstream)

#### Q49. 以下哪项不是将my_class的成员变量`count`声明为static的结果？/ 备选：将成员变量`count`声明为static时，以下哪项陈述是正确的？

```cpp
class my_class {
    public: static int count;
}
```

- [x] 该变量不能被同一应用程序或线程中代码的任何部分修改。但是，其他线程可以修改它。
- [ ] 即使没有定义类的对象，该变量也存在，因此可以在源代码的任何位置修改。
- [ ] 该变量只分配一次，无论实例化多少个对象，因为它绑定到类本身，而不是其实例。
- [ ] 所有尝试访问其count成员变量的对象实际上都引用唯一的类绑定静态count变量。

[参考](https://en.cppreference.com/w/cpp/language/static)

#### Q50. 源代码中表示为`0.44`的常量的假定类型是什么？

- [x] double
- [ ] long float
- [ ] long double
- [ ] float

#### Q51. 如下所示，删除`my_object`的适当方法是什么？

```cpp
my_class *my_object = new my_class();
```

- [x] `delete(my_object);`
- [ ] `free(my_object);`
- [ ] 垃圾收集器最终会销毁该对象。
- [ ] 退出作用域将销毁该对象。

#### Q52. 对于名为`grades`的对象指针，调用`count`成员函数的正确方法是什么？

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

[参考](https://en.cppreference.com/w/c/language/operator_member_access)

#### Q53. 这段代码的输出是什么？

```cpp
int i0=4, i1=6, i2=8;
int& nums[3]={i2,i0,i1};
std::cout<<nums[0]<<nums[1]<<nums[2];
```

- [x] 没有输出。代码导致编译器错误，因为`nums`是引用数组，这是非法的。
- [ ] 846
- [ ] 输出是i2、i0和i1的地址，按顺序，没有空格。
- [ ] 468

[参考](https://en.cppreference.com/w/cpp/language/array)

#### Q54. 这段代码会导致编译器错误吗？如果是，为什么；如果不是，`child_t`是什么？

```cpp
typedef struct{
    unsigned int  age    : 4;
    unsigned char gender : 1;
    char                 : 0;
    unsigned int  size   : 2;
}child_t;
```

- [ ] 是的，它导致编译器错误，因为冒号字符不允许在结构定义中使用。
- [x] 否，`child_t`是一个定义为具有位字段的结构的类型。它在第一个字节中有4位用于年龄和1位用于性别，在第二个字节中有2位用于大小。
- [ ] 是的，它导致编译器错误，因为有一个未命名的字段。
- [ ] 是的，它导致编译器错误，因为一个字段的大小定义为0。

[参考](https://en.cppreference.com/w/cpp/language/bit_field)

#### Q55. 这个表达式等价于什么？

```cpp
A->B
```

- [ ] `*(A.B)`
- [ ] `B=A`
- [x] `(*A).B`
- [ ] `&A.B`

注意：下面问题的简化变体。

#### Q56. 这个表达式等价于什么？

```cpp
A->B->C->D
```

- [ ] `A.B.C.D`
- [ ] `*A.*B.*C.*D`
- [ ] `&A.&B.&C.&D`
- [x] `*(*((*A).B).C).D`

**注意：**上面问题的更复杂变体。

#### Q57. 这个函数做什么？

```cpp
auto buff = new char[50];
std::memset(buff,20,50);
```

- [ ] 它声明一个名为buff的内存缓冲区，从地址20开始到地址70结束。
- [ ] 它设置名为buffer的数组中从索引20到索引50的所有位。
- [x] 它将值20写入从buff到buff+49的每个内存地址。
- [ ] 它声明一个名为buff的内存缓冲区，从地址20开始到地址50结束。

[参考](https://en.cppreference.com/w/cpp/string/byte/memset)

#### Q58. 考虑一个名为`CustomData`的类。以下哪个选择是作为类成员重载后缀`++`运算符的正确声明语法？

- [ ] `CustomData& operator++();`
- [ ] `void operator++(CustomData);`
- [ ] `CustomData operator++(CustomData);`
- [x] `CustomData operator++(int);`

[参考](https://en.cppreference.com/w/cpp/language/operators)

#### Q59. 您想要对下面声明的my_array进行排序。使用lambda表达式作为比较函数调用std::sort的正确方法是哪个？

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

[参考](https://docs.microsoft.com/en-us/cpp/cpp/lambda-expressions-in-cpp?view=msvc-160)

#### Q60. 使用std::mutex::try_lock()实现函数std::mutex::lock()的最合理的实现是哪个选择？

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

注意：下面问题的变体。

#### Q61. 这两个函数之间的主要区别是什么？

```cpp
std::mutex::lock()
std::mutex::try_lock()
```

- [ ] `lock()`比`try_lock()`具有更高的特权。这意味着使用`lock()`获取互斥锁的机会更大。
- [x] 两者都尝试获取锁，但如果互斥锁不可用，`lock()`会阻塞，而`try_lock()`会返回互斥锁是否可用。
- [ ] `lock()`强制抢占，而`try_lock()`建议抢占。
- [ ] 如果互斥锁不可用，`try_lock()`会返回相应的代码，而`lock()`会从当前拥有它的线程中抢夺互斥锁。

注意：上面问题的变体。

[参考](https://en.cppreference.com/w/cpp/thread/mutex/try_lock)

#### Q62. 析构函数的目的是什么？

- [x] 它允许程序员编写必要的代码，在删除对象本身之前释放对象获取的资源。
- [ ] 它删除一个对象。析构函数的一个例子是`delete()`函数。
- [ ] 它终止程序。这可以作为常规函数调用或异常实现。
- [ ] C++中没有析构函数。

#### Q63. 将参数声明为`const`引用而不是将其声明为常规对象的一个好处是什么？

```cpp
int calculateMedian(const my_array& a)
```

- [ ] 实际上，对象不能作为常规变量传递，因为它们需要构造函数调用。因此，`const`引用是将类实例传递给函数的唯一方法。
- [ ] 没有好处，因为引用和对象被视为同一事物。
- [x] `const`限定符禁止代码修改参数，因此程序员可以确保源对象将保持不变。/ 备选：参数作为引用传递，因此如果传递的my_array对象很大，程序将需要更少的时间和内存。
- [ ] 参数作为引用传递，因此函数接收可以修改而不影响原始变量的副本。

[参考](https://stackoverflow.com/a/2627179/10773894)

#### Q64. 什么是包含保护？

- [ ] 一个预处理器指令，防止包含#ifdef、#ifndef或#elif指令的行中的不一致行为
- [ ] 一个编译器选项，防止用户代码包含其他库
- [x] 一个预处理器语句，防止源文件在项目中被多次包含
- [ ] 一个向项目添加安全功能（如互斥锁、看门狗定时器和断言）的库

#### Q65. 名为Sprite的类的默认构造函数的正确声明是什么？

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

#### Q66. 头文件中这一行的目的是什么？

```cpp
#pragma once
```

- [ ] 限制其内容仅用于一个源文件
- [ ] 告诉编译器此头文件中包含的类或类型只能实例化一个变量
- [ ] 通过确保此头文件中包含的代码只需要一次编译器传递来帮助编译器更快地完成
- [x] 使编译器只解析一次该头文件，即使它在源中被多次包含

[参考](https://en.cppreference.com/w/cpp/preprocessor/impl)

#### Q67. double类型的变量是什么？

- [ ] 2元组
- [ ] 整数
- [x] 浮点数
- [ ] 超过255个字符的字符串

[参考](https://www.educba.com/c-plus-plus-double/)

#### Q68. 除了将位向左移动之外，<<运算符还用于什么？

- [ ] 将字符串中的字符向左移动。
- [x] 将字符插入输出流，如std::cout。
- [ ] 将浮点数比较为小于。
- [ ] 将变量分配给引用。

#### Q69. 为什么要指定指针的类型而不是使用`void *`（它可以作为指向任何类型的指针）？

- [ ] 编译器需要数据类型以确保指针不会用于非法的不可指向类型，如函数、标签、指针和引用。
- [ ] `void *`不适用于任何类型。语言不允许将void以外的任何内容分配给指向`void *`的指针。
- [x] 编译器需要数据类型以知道为指针分配多少内存，因为不同的数据类型需要不同的指针长度。
- [ ] 是的，它导致编译器错误，因为一个字段的大小定义为0。

[参考](https://stackoverflow.com/questions/9802585/why-is-the-data-type-needed-in-pointer-declarations)

#### Q70. 这段代码有什么问题？

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

- [ ] main函数应该有void返回类型。
- [ ] `std::cin`和`std::cout`无效。字符输入和输出流的正确名称是`cin`和`cout`。
- [ ] 应该使用`str`的地址。即`&str`而不是`str`。
- [x] 输入运算符流被反转了。它应该从`std::cin`开始，然后流(>>)到`str`中。

#### Q71. 当放置在有效的执行上下文中时，哪个语句将从堆中动态分配内存以存储值为11的整数？

- [ ] `int anInt = new int(11);`
- [ ] `int* anInt = new int[11];`
- [ ] `int anInt = new int[11];`
- [x] `int* anInt = new int(11);`

#### Q72. 以下哪项最好地描述了`long`类型？

- [x] 至少32位的整数
- [ ] 超过255个字符的字符串
- [ ] 指针
- [ ] 64位浮点数

#### Q73. 以下哪种类型的功能最接近类？

- [x] `struct`
- [ ] `union`
- [ ] `enum`
- [ ] `namespace`

[参考](https://en.cppreference.com/w/c/language/struct)

#### Q74. 给定映射中的这些记录，您将如何将键"Sinead"的值更新为22？

![image](images/Q79.png?raw=png)

- [x] `marks["Sinead"] = 22`
- [ ] `marks["Sinead"].22`
- [ ] `marks["Sinead"] -> 22`
- [ ] `marks["Sinead"].value = 22`

#### Q75. 为什么std::sort可以接收函数对象作为其参数之一？

- [x] `std::sort函数是一个模板。程序员可以自由地在函数对象中输入排序算法作为参数。`
- [ ] `实际上，std::sort只接受一个参数，即要排序的容器。`
- [ ] `std::sort在模板容器上操作。编译器不知道如何关系比较它包含的值，因此必须提供一个函数来进行比较。`
- [ ] `std::sort将使用参数函数作为错误处理程序。如果发生错误，将调用该函数。`

#### Q76. 当您执行此代码片段时会发生什么？

```
#include <iostream>

int main() {
float a = 5.51;
int b = static_cast<int>(a);
std::cout << b;
}
```

- [ ] `6将在标准输出上打印，不会生成编译警告。`
- [x] `5将在标准输出上打印，不会生成编译警告。`
- [ ] `6将在标准输出上打印，会生成编译警告。`
- [ ] `5将在标准输出上打印，会生成编译警告。`

#### Q77. 哪个访问说明符不允许从类外部访问类成员，但允许派生类访问它们？

- [ ] guarded
- [x] protected
- [ ] public
- [ ] private

#### Q78. UNIX上C++程序的默认可执行文件生成是\_

- [ ] a.exe
- [ ] a
- [x] a.out
- [ ] out.a

#### Q79. 以下程序的输出是什么？

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

#### Q80. cout和cin中的"c"代表什么？

- [ ] compiler（编译器）
- [ ] console（控制台）
- [x] character（字符）
- [ ] standard namespace（标准命名空间）

#### Q81. tellp()的用途是什么？

- [ ] 当前输入指针位置
- [x] 当前输出指针位置
- [ ] 最后输入指针位置
- [ ] 最后输出指针位置

#### Q82. 什么是回调函数？

- [ ] 指向指针的指针
- [x] 指向函数的指针
- [ ] 用于指针的函数
- [ ] 用于类的函数

#### Q83. 在C++中输出"Hello World"的正确语法是什么？

- [x] `cout << "Hello World";`
- [ ] `System.out.println("Hello World");`
- [ ] `print("Hello World");`
- [ ] `Console.WriteLine("Hello World");`

#### Q84. C++中有多少类别的迭代器？

- [ ] 4
- [ ] 3
- [ ] 7
- [x] 5

#### Q85. C++中基类的含义是什么？

- [ ] 它继承其他类
- [ ] 它有一个指针变量
- [ ] 它是声明的第一个类
- [x] 另一个类从这个类继承

#### Q86. C++对象的大小以 ** 大小的倍数表示，char的大小是 **。

- [ ] char, 4
- [ ] float, 8
- [ ] int, 1
- [x] char, 1

#### Q87. 关于实现的实现相关方面可以在哪里找到

- [ ] `<numeric>`
- [ ] `<limit>`
- [x] `<limits>`
- [ ] `<implementation>`

#### Q88. 什么是默认构造函数？

- [x] 可以不带参数使用的构造函数
- [ ] 没有返回值的构造函数
- [ ] 由多个类使用的构造函数
- [ ] 初始化类的所有成员的构造函数

#### Q89. 在保护头文件时，为什么要使用'#pragma once'而不是'include'保护？

- [ ] 没有理由选择，因为它们的目的不同
- [x] 包含保护使用宏来实现单一包含，但编译器无法阻止程序员在其他地方定义该宏，这将导致根本没有包含
- [ ] '#pragma once'保证头代码永远不会被更改，因为它由编译器强制执行
- [ ] 包含保护引用文件系统中的头文件，而不是代码，因此如果头文件在项目中存在多次，它们没有帮助。'#pragma once'没有这个问题

#### Q90. 以下哪个陈述是有效的？

- [ ] 我们可以创建一个新的C++运算符。
- [ ] 我们可以改变C++运算符的优先级。
- [x] 我们不能改变运算符模板。
- [ ] 我们可以改变C++运算符的结合性。

#### Q91. 以下哪些会自动添加到每个类中，如果我们不编写自己的？

- [ ] 拷贝构造函数
- [ ] 赋值运算符
- [ ] 没有任何参数的构造函数
- [x] 以上所有

#### Q92. if-else语句可以被哪个运算符替换？

- [ ] 某种结构
- [ ] 选择结构
- [x] 选择结构
- [ ] 以上都不是

#### Q93. 以下哪个选择是阶乘n!问题的递归解决方案？

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

#### Q94. 当发生各种情况时，可以调用类析构函数。以下哪个选择不是这些情况之一？

- [ ] 程序终止。这会调用静态持续时间对象的析构函数。
- [ ] 为使用new运算符分配的对象指针调用delete()函数。
- [x] 垃圾收集器检测到不再使用对象。
- [ ] 自动存储期对象超出作用域。

#### Q95. 您正在用C++设计外汇支付系统，您需要对具有整数作为数量和浮点数作为价格的货币交易进行建模。然后您想声明此类型的实际对象。您将如何实现这一点？

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

#### Q96. 如果您尝试使用checkConcatThreshold("a");调用此函数，会发生什么？

```cpp
int checkConcatThreshold(string a, string b) {
    return (a + b).length () > 120;
}
```

- [ ] 将发生编译警告，第二个参数将被赋予默认值b。
- [ ] 将发生编译警告，第二个参数将被赋予空字符串的默认值。
- [x] 将发生编译错误。
- [ ] 不会发生编译错误，也不会发生编译警告。

#### Q97. 您需要定义一个C++ lambda函数。您希望该函数只能访问其本地的变量。该函数应接收单个参数和一个名称，并构建一个简单的问候语。您将如何实现这一点？

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

[参考](https://docs.microsoft.com/en-us/cpp/cpp/lambda-expressions-in-cpp?view=msvc-160)

#### Q98. 运行此代码后X的值是多少？

```cpp
int x=10, a=-3;
X+=a;
```

- [ ] -3
- [x] 7
- [ ] 13
- [ ] 3

**解释：**`+=`表示增加值。所以`x += a`等价于`x = x + a`

#### Q99. 完成写入文件后，您将在`ofstream`上调用什么方法来通知操作系统？

- [ ] printout()
- [x] close()
- [ ] destroy()
- [ ] flush()

#### Q100. 以下哪个选择不是C++关键字？

- [ ] static_assert
- [ ] reinterpret_cast
- [x] comPl
- [ ] alignas

#### Q101. size_in_bits函数似乎可以接受任何类型的参数。这可以通过重载函数或让编译器通过编写模板来处理它来实现。以下哪个选择是该模板的实现？

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

#### Q102. 要使用键盘作为输入，需要包含iostream库。要从文件读取输入作为输入，需要什么库？

- [x] fstream
- [ ] cstdlib
- [ ] filestream
- [ ] iostream

#### Q103. 这个面向对象的程序将打印什么？

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

#### Q104. 下面的程序正在处理一个栈容器。运行程序的输出是什么？

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

#详细解释：

现在我们应该实现一个遵循**FILO**或（先进后出）原则的栈数据结构，
_stack.push()_ -> 从数组末尾推入元素。
_stack.pop()_ -> 从数组末尾移除元素。
_stack.top()_ -> 只给我们数组的最顶层元素。
现在遵循push和pop的顺序：**[1,2,3]** 然后使用pop函数，
新形成的数组是：**[1,2,4]** 然后使用top检索最顶层的元素'4'，然后再次使用pop函数，该函数删除4。
因此，结果数组是：1,2。
然后它打印最顶层的元素（即：2）。

#### Q105. 以下哪个选择是重载三元条件运算符的有效方法？

- [ ] `void& operator ?:(const bool cond, const void& iftrue, const void& iffalse);`
- [x] `三元运算符不可重载。`
- [ ] `void& operator conditional(const bool cond, const void& iftrue, const void& iffalse);`
- [ ] `void* operator ?:(const bool cond, const void* iftrue, const void* iffalse);`

[参考](https://en.cppreference.com/w/cpp/language/operators)

#### Q106. 哪个类层次结构代表多级继承的示例？

- [ ] 在同一程序中，在不同的点，给定的类分别从多个不同的类派生。
- [ ] 第一类同时直接从第二和第三类派生。
- [x] 在同一程序中，在不同的点，给定的类分别从两个以上的不同类派生。
- [ ] 第一个类从第二个类派生，第二个类已经从第三个类派生

#### Q107. 以下哪个是在C++语言中打印消息的正确语法？

- [ ] Out <<"Hello world!
- [ ] Cout << Hello world! ;
- [x] cout <<"Hello world!";
- [ ] 以上都不是

[参考](https://en.cppreference.com/w/cpp/io/cout)

#### Q108. 考虑以下程序。输出/错误是什么？

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
- [ ] 编译错误：函数未定义

[参考](https://www.geeksforgeeks.org/tolower-function-in-cpp/)

#### Q109. 考虑以下代码段。在LINE-1处填空，使程序打印"not found"？

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

[参考](https://www.geeksforgeeks.org/binary-search-algorithms-the-c-standard-template-library-stl/)

#### Q110. 考虑以下代码段。输出是什么？

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

[参考](https://cplusplus.com/reference/algorithm/sort/)

#### Q111. 考虑以下代码段。输出是什么？

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

[参考](https://en.cppreference.com/w/cpp/algorithm/rotate)

#### Q112. 考虑以下代码段。输出是什么？

```cpp
#include <iostream>
#include <vector>
using namespace std;
int main() {
const int size = 3, c = 65;
vector<char> vc(size, 'A');
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

[参考](https://en.cppreference.com/w/cpp/container/vector)

#### Q113. 考虑以下代码段。选择适当的选项填写LINE-1处的空白，使代码的输出为：a C++ Program。

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

[参考](https://www.geeksforgeeks.org/stdstringappend-in-c/)

#### Q114. 考虑以下代码段。在LINE-1处填空，使输出为5 2 3 4 5

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

[参考](https://www.geeksforgeeks.org/stdstringreplace-stdstringreplace_if-c/)

#### Q115. 考虑以下代码段。输出是什么？

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

[参考](https://en.cppreference.com/w/cpp/container/stack)

#### Q116. 考虑以下代码段。以下哪个/哪些语句是正确的？

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

[参考](https://www.geeksforgeeks.org/const-keyword-in-cpp/)

#### Q117. 考虑以下程序。输出/错误是什么？

```cpp
#include <iostream>
using namespace std;
char add(char c1 = 'a') { return c1; }
char add(char c1 = 'a', char c2 = 'b') { return c1 + c2 - 'a';}
char add(char c1 = 'a', int d1 = 100){ return c1 + d1 - 'a'; }
char add(char c1 = 'a', char c2 = 'b', char c3) { return c1 + c2 + c3 - 'a'; }
int main() {
char c = add('o', 'k');
cout << c << endl;
return 0;
}
```

- [ ] y
- [ ] z
- [x] 编译错误："char add(char, char, char)"缺少默认参数
- [x] 编译错误：重载"add(char, char)"的调用不明确

[参考](https://learn.microsoft.com/en-us/cpp/cpp/function-overloading?view=msvc-170)

#### Q118. 考虑以下代码段。输出是什么？

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

[参考](https://www.geeksforgeeks.org/output-of-the-program-use-macros-carefully/)

#### Q119. 考虑以下代码段。哪一行/哪些行会给您一个错误？

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

#### Q120. 考虑以下代码段。输出/错误是什么？

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
- [x] 编译错误：非const引用的无效初始化

#详细解释：
发生错误是因为它试图创建对临时值的引用。在int &b = a+1;行中，我们试图创建对表达式a + 1结果的引用b，这是一个临时值。引用必须绑定到实际对象，而不是临时值或没有内存位置的表达式。

#### Q121. 考虑以下代码段。输出是什么？

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

[参考](https://www.ibm.com/docs/en/zos/2.4.0?topic=calls-pass-by-reference-c-only)

#### Q122. 考虑以下代码段。选择适当的选项填写LINE-1处的空白，使代码的输出为：300 20000。

```cpp
#include <iostream>
using namespace std;
void compute(int n1, int n2, ________, ________){  //LINE-1
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

#### Q123. 考虑以下代码段。输出/错误是什么？

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

- [ ] `<垃圾值>`
- [ ] 5
- [x] LINE-1的编译错误：未初始化的const 'ptr'
- [x] LINE-2的编译错误：对只读变量'ptr'的赋值

#### Q124. 考虑以下代码段。输出/错误是什么？

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
- [x] LINE-2的编译错误：'int fun(int)'的新声明产生歧义

#### Q125. 考虑以下代码段。在LINE-1处填空，使程序打印5 + i3

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

[参考](https://www.w3schools.com/cpp/cpp_structs.asp)

#### Q126. 考虑以下程序。哪一行/哪些行会产生错误？

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

[参考](https://stackoverflow.com/questions/4855422/c-classes-public-private-and-protected)

#### Q127. 考虑以下类。用适当的访问说明符填空，使成员y可以从类外部访问，但成员x不能被访问。

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

#### Q128. 哪个C++标准添加了类内默认成员初始化器？

- [ ] C++98
- [x] C++11
- [ ] C++14
- [ ] C++17.

#### Q129. 您可以对非静态数据成员使用auto类型推导吗？

- [ ] 是的，自C++11起
- [x] 否
- [ ] 是的，自C++20起

#### Q130. 您需要在cpp文件中定义静态内联数据成员吗？

- [x] 否，定义发生在声明静态内联成员的同一位置。
- [ ] 是的，编译器需要cpp文件中的定义。
- [ ] 是的，编译器需要在使用此变量的所有翻译单元中进行定义。

[参考](https://en.cppreference.com/w/cpp/language/bit_field)

#### Q131. 以下代码的输出是什么：

```cpp
struct S {
    int a { 10 };
    int b { 42 };
};
S s { 1 };
std::cout << s.a << ", " << s.b;
```

- [ ] 输出是：1, 0
- [ ] 输出是：10, 42
- [x] 输出是：1, 42

#### Q132. 静态内联变量可以是非常量的吗？

- [x] 是的，它只是一个普通变量。
- [ ] 否，内联变量必须是常量。

#### Q133. 考虑以下代码：

```cpp
struct C {
    C(int x) : a(x) { }
    int a { 10 };
    int b { 42 };
};
C c(0);

```

- [ ] C::a初始化两次。第一次用10初始化，然后在构造函数中用0第二次初始化。
- [x] C::a仅在构造函数中用0初始化一次。
- [ ] 代码无法编译，因为编译器无法决定如何初始化C::a成员。
- [ ] 2字节

#### Q134. 从构造函数抛出异常时会发生什么？

- [ ] 对象被视为"已创建"，因此它将遵循对象的常规生命周期。
- [x] 对象被视为"部分创建"，因此编译器不会调用其析构函数。
- [ ] 编译器调用std::terminate，因为您不能从构造函数抛出异常。

#### Q135. 编译此代码时会发生什么？

```cpp
struct Point { int x; int y; };
Point pt {.y = 10, .x = 11 };
std::cout << pt.x << ", " << pt.y;
```

- [x] 代码无法编译。指示符必须与Point类中的数据成员顺序相同。
- [ ] 代码编译并打印11, 10。
- [ ] 代码编译并打印10, 11。

#### Q136. 此代码在C++11中能工作吗？

```cpp
struct User { std::string name = "unknown"; unsigned age { 0 }; };
User u { "John", 101 };
```

- [ ] 是的，代码在C++11模式下编译。
- [x] 代码从C++14模式开始编译。
- [ ] 即使在C++20中，代码也无法编译。

#### Q137. 假设您有一个std::map<string, int> m;。选择关于以下循环的单个正确陈述：

```cpp
for (const pair<string, int>& elem : m)
```

- [x] A 循环正确地迭代映射，不创建额外的副本。

- [ ] B 循环将创建映射中每个元素的副本，因为elem的类型不匹配。

- [ ] C 代码无法编译，因为const pair无法绑定到映射。

#### Q138. 识别C++中用户定义头文件的正确扩展名。

- [ ] .cpp
- [ ] .hg
- [x] .h
- [ ] .hf

#### Q139. 识别不正确的构造函数类型。

```cpp
auto x = 4000.22;
```

- [x] 友元构造函数
- [ ] 默认构造函数
- [ ] 参数化构造函数
- [ ] 拷贝构造函数

#### Q140. 以下哪种数据类型在C++中支持但在C中不支持？

- [x] bool
- [ ] int
- [ ] double
- [ ] float

[参考]: https://stackoverflow.com/questions/1608318/is-bool-a-native-c-type

#### Q141. 识别在C++中声明数组的正确语法。

- [x] int arr[10]
- [ ] array arr[10]
- [ ] array{10}
- [ ] int arr

[参考]: (https://en.cppreference.com/w/cpp/language/array)

#### Q142. wchat_t的大小是。

- [ ] 2
- [ ] 4
- [ ] 2或4
- [x] 取决于系统中的位数

#### Q143. 当我们知道迭代次数时，以下哪个循环最好？

- [ ] while
- [x] for
- [ ] do
- [ ] 以上所有

#### Q144. 在C++中使用哪个关键字来定义宏？

- [ ] #macro
- [x] #define
- [ ] macro
- [ ] keyword

#### Q145. 以下哪个运算符应该优先作为全局函数而不是成员方法进行重载？

- [ ] 后缀++
- [x] 比较运算符
- [ ] 插入运算符<<
- [ ] 前缀++

#### Q146. 我们如何限制使用new动态分配类的对象？

- [ ] 通过重载new运算符
- [ ] 通过创建一个空的私有new运算符。
- [x] 通过创建空的私有new和new[]运算符
- [ ] 通过重载new运算符和new[]运算符

#### Q147. 下面代码的时间复杂度是多少？

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

[参考](<https://medium.com/enjoy-algorithm/analysis-of-loop-in-programming-cc9a644ef8cd#:~:text=At%20each%20step%20of%20the%20iteration%2C%20the%20nested%20loop%20is,%20%3D%20O(n%C2%B2)>)

#### Q148. 下面给出的代码的输出是什么？

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

**++a**和**a++**都将a的值增加1（即：11），因此k+m变为22。

#### Q149. 哪个C++构造用于异常处理？

- [x] try-catch
- [ ] if-else
- [ ] for循环
- [ ] switch-case

#### Q150. C++中循环中`break`语句的目的是什么？

- [ ] 退出程序
- [ ] 跳过当前迭代并继续下一次迭代
- [x] 终止循环
- [ ] 返回一个值

[参考]: (https://www.tutorialspoint.com/cprogramming/c_break_statement.htm)

#### Q151. 在C++中，当与变量一起使用时，`const`关键字的目的是什么？

- [x] 它使变量不可变
- [ ] 它改变数据类型
- [ ] 它定义一个常量函数
- [ ] 它使变量成为指针

#### Q152. 调用C++函数时哪个更有效？

- [x] 引用调用
- [ ] 值调用
- [ ] 指针调用
- [ ] 对象调用

[参考]: (https://www.algbly.com/More/MCQs/Cpp-mcq/Cpp-functions.html)

#### Q153. 以下C++程序的输出是什么？

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

- [ ] 段错误
- [x] "Constructor called"五次，然后"Destructor called"五次
- [ ] "Constructor called"五次，然后"Destructor called"一次
- [ ] 错误

#### Q154. 以下哪个选择与将my_class中的成员变量count声明为static无关？

```cpp
class my_class{
    public: static int count;
}
```

- [ ] 所有尝试访问其count成员变量的对象实际上都引用唯一的类绑定静态count变量。
- [ ] 即使没有定义类的对象，该变量也存在，因此可以在源代码的任何位置修改。
- [x] 该变量不能被同一应用程序或线程中代码的任何部分修改。但是，其他线程可以修改它。
- [ ] 该变量只分配一次，无论实例化多少个对象，因为它绑定到类本身，而不是其实例。

#### Q155. C++中`constexpr`关键字的目的是什么？

- [ ] 它用于在C++中定义常量。
- [ ] `constexpr`用于指定变量是常量指针。
- [x] `constexpr`用于指示表达式可以在编译时求值，使其适合在常量表达式中使用。
- [ ] 它是用于创建异步函数的关键字。

[参考](https://learn.microsoft.com/en-us/cpp/cpp/constexpr-cpp?view=msvc-170#:~:text=constexpr%20indicates%20that%20the%20value,template%20arguments%20and%20array%20declarations.)

#### Q156. C++中的模板元程序是什么？

- 参考(https://www.geeksforgeeks.org/template-metaprogramming-in-c/)

- [ ] 模板元程序是一种高级编程语言。
- [ ] 它指的是在C++中使用模板的元编程。
- [ ] 它是一种用户界面设计模式。
- [x] 模板元程序是编译时计算，其中模板和模板特化用于在编译时执行计算。

#### Q157. 识别前增量运算符的正确示例。

- [x] ++i
- [ ] i++
- [ ] --i
- [ ] +i

#### Q158. 以下代码的输出是什么？

```cpp
{% raw %}
int matrix[3][3] = {{1, 2, 3},{4, 5, 6},{7, 8, 9}};
for(int i=0;i<3;i++){
    for(int j=0;j<3;j++){
        int a = matrix[i][j];
        matrix[i][j] = matrix[j][i];
        matrix[j][i] = a;
    }
}
{% endraw %}
```

- [ ] 矩阵的转置
- [x] 相同的矩阵
- [ ] 矩阵的镜像
- [ ] 倒置矩阵

#### Q159. C++中的竞态条件是什么？

- [ ] 程序运行速度比预期快的条件
- [x] 多个线程并发访问共享数据，结果取决于它们执行的时间的条件
- [ ] 两个线程竞争CPU时间的条件
- [ ] 循环执行太快需要减速的条件

[参考](https://en.cppreference.com/w/cpp/language/memory_model)

#### Q160. 考虑以下具有竞态条件的代码。修复它的正确方法是什么？

```cpp
#include <thread>
#include <vector>

int counter = 0;

void incrementCounter() {
    for(int i = 0; i < 1000; i++) {
        counter++;
    }
}

int main() {
    std::vector<std::thread> threads;
    for(int i = 0; i < 10; i++) {
        threads.push_back(std::thread(incrementCounter));
    }
    for(auto& t : threads) {
        t.join();
    }
    return 0;
}
```

- [ ] 添加`volatile`关键字：`volatile int counter = 0;`
- [x] 使用`std::mutex`在关键部分的`counter++`周围锁定/解锁
- [ ] 使用`std::this_thread::sleep_for()`延迟每次增量
- [ ] 将`counter++`更改为`++counter`以实现原子操作

[参考](https://en.cppreference.com/w/cpp/thread/mutex)