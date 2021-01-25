## C++

#### Q1. What is printed from this code?
```
vector<int> v(22);
bool b= (v[6]);
printf("%d",!b);
```
 - [ ] False
 - [ ] 0
 - [x] 1
 - [ ] This code has an error

#### Q2. Which of the following is a reason why using this line is considerd a bad practice?
`Using namespce std;`
 - [ ] The compiled code is always bigger because of all of the imported symbols.
 - [ ] If the code uses the function defined in two different libraries with the same prototype but possibly with different implementation , there will be a compilation error due to ambuiguity.
 - [ ] It automatically includes all header files in the standard library (cstdint,cstdlib,cstdio,iostream et- []. << Correct
 - [ ] It causes the compiler to enforce the exclusion , inclusion of header file belonging to the standard library , generating compilation error when a different header file is included.

#### Q3. What is the smallest size a variable of the type child_t may occupy in memory?
```
typedef struct {
unsigned int age : 4;
unsigned char gender :1;
unsigned int size : 2;
} child_t;
```
 - [x] 7 bits. << Correct
 - [ ] 25 bytes.
 - [ ] 1 bit.
 - [ ] 1 bytes.

#### Q4. Which of the following shows the contents of vector v1 and v2 after running this code?
```
std:: vector <int> v1{1,2,3},v2;
v2=v1;
v1.push_back(4);
v2.push_back(5);
```
 - [x] Error <<< Correct because std::vector v1{1,2,3}; doesn't compile, It should be std::vector v1{1,2,3};
 - [ ] v1:{1,2,3,4};
v2:{5};
 - [ ] v1:{1,2,3,4,5};
v2:{1,2,3,4,5};
 - [x] v1:{1,2,3,4};
v2:{1,2,3,5}; <<  Correct

#### Q5. Which of the following is a true statement about the difference between pointers and iterators?
 - [x] While pointers are variable that hold memory address, iterators are generic functions used to traverse containers. These function allows the programmer to implement read and write code as the container is traversed.
 - [ ] Incrementing an iterator always means access the next element in the container(if any) , no matter the container. Incrementing the pointer means pointing to the next element in memory, not always the next element.
 - [ ] Pointers are variables that hold memory address where as iterator are unsigned integers that refers to offsets in arrays.
 - [ ] All iterator are implemented with pointers so all iterators are pointers but not all pointers are iterators.

#### Q6. What's a benefit of declaring the parameter as a const reference instead of declaring it as a regular object?
`int median(const my_arrary &a);`
 - [ ] The argument is passed as a reference so the function receives a copy that can be modified without affecting the original value.
 - [x] The argument is passed as a reference,so all if the passed my_array object is large, the program will require less time and memory.
 - [ ] Actually object can't be passed as regular variable because they require a constructor call. Therefore a const reference is the only way to pass class instances to functions.
 - [ ] There are no benefits because a reference and an object are treated as the same thing.

#### Q7. What's the storage occupied by u1?
```
union {
    unit16_t a;
    unit32_t b;
    int8_t c;
} u1;
```
 - [x] 4 bytes //You can see example [here](https://en.cppreference.com/w/cpp/language/union)
 - [ ] 7 bytes
 - [ ] 8 bytes
 - [ ] 2 bytes

#### Q8. Which of the following operators is overloadable?
 - [ ] ?:
 - [x] new
 - [ ] ::
 - [ ] .

#### Q9. Which of the following shows the contents of vector pointed by v1 and v2 after running this code?
```
std:: vector<int> *v1 = new std:: vector<int> ({1,2,3});
std:: vector<int> *v2;
v2=v1;
v1->push_back(4);
v2->push_back(5);
```
 - [ ] *v1:{1,2,3,4};
*v2:{5};
 - [ ] *v1:{1,2,3,4'5};
*v2:{1,2,3,4,5};
 - [x] Error
 - [ ] *v1:{1,2,3,4};
*v2:{1,2,3,5};
   
#### Q10. Which of the following is not a difference between a class and a struct?
 - [ ] Because structor are part of the c programming language there some complexity between c and c++ struct This is not the case with classes.
 - [ ] Classes may have member function;struct private.
 - [ ] The default acces specifier for members of struct is public, where as for member of class , it is private. << Correct -> You can see the answer [here](https://www.fluentcpp.com/2017/06/13/the-real-difference-between-struct-class/)
 - [ ] Template type parameters can be declared with , but not with the struct keyword.

#### Q11. Suppose you need to keep a data struct with permission to access some resource base on the days of week , but you can't be use a bool variable for each day.you need to use one bit per day of the week.
which of the following is a correct implementation of a structure with bit fields for this application?
- [x] 
```
typedef struct {
    int sunday:1;
    int monday:1;
    // more days
    int friday:1;
    int satarday:1;
} weekdays; << Correct  That syntax says that each variable size is 1 bit. 'bit' is not a type in C++.
```
- [ ] 
```
typedef char[7]: weekdays;
```
- [ ] 
```
typedef struct {
    bit sunday:1;
    bit monday:1;
    // more days
    bit fridyas:1;
    bit satarday:1;
} weekdays;
```
- [ ] 
```
typedef struct {
    bit sunday;
    bit monday;
    // more days
    bit friday;
    bit satarday;
} weekdays;
```

#### Q12. What is an lvalue?
 - [ ] It's a constant expression , meaning an expression composed of constants and operations.
 - [x] It's an expression that represents an object with an address.
 - [ ] It's an expression suitable for the left hand side operand in binary operation.
 - [ ] It's a location value , meaning a memory address suitable for assigning to pointer or reference.

#### Q13. What does auto type specifier do in this line of code (since c++ 11)?
 - [ ] It specifies that the type of x will be deducted from the initializer in this case,double.
 - [ ] It specifies that the type of x is automatic meaning that if can be assigned different type of data throughout the program.
 - [x] It specifies that x is a variable with automatic storage duration.
 - [ ] It soecifies that more memory will be allocated for x in case it needs more space, avoiding loss of data due to overflow.

#### Q14. What is a class template?
 - [x] It's a class written with the generic programming , specifying behavior in terms of type parameter rather than specific type.
 - [ ] It's a blank superclass intended for inheritence and polymorphism.
 - [ ] It's class that only consists of member variable , with no constructor , destructor nor member functions.
 - [ ] It's skelton source code for a class where the programming has to fill in specific parts to define the data types and algorithms used.

#### Q15. What is the ternary operator equivalent to this code snippet?
```
if(x)
y=a;
else
y=b;
```
 - [ ] y=a?b:x;
 - [ ] y=if(x?a:b);
 - [ ] y=(x&a)?a:(x&b)?b:0;
 - [x] y=x?a:b;

#### Q16.What is the output of this code?
```
#include <iostream>
int main()
{
    int x=10, y=20;
    std::cout << "x = " << x++ << " and y = " << --y << std::endl;
    std::cout << "x = " << x-- << " and y = " << ++y << std::endl;
    return(0);
}
```
 - [ ] x = 10 and y = 20 x = 11 and y = 19
 - [ ] x = 11 and y = 19 x = 10 and y = 20
 - [x] x = 10 and y = 19 x = 11 and y = 20
 - [ ] x = 11 and y = 20 x = 10 and y = 19

#### Q.17 What is the meaning of the two parts specified between parentheses in a range-based for loop, separated by a colon?What is the meaning of the two parts specified between parentheses in a range-based for loop, separated by a colon?
 - [ ] The first is a variable declaration that will hold an element in a sequence. The second is the sequence to traverse.
 - [ ] The first is an iterator, and the second is the increment value to be added to the iterator. The first is an iterator, and the second is the increment value to be added to the iterator.
 - [ ] The first is the iterating variable. The second is an `std::pair` that specifies the range (start and end) in which the variable will iterate.The first is the iterating variable. The second is an `std::pair` that specifies the range (start and end) in which the variable will iterate.
 - [ ] The first is a container object. The second is an `std::pair` that specifies the range (start and en in which the elements will be accessed within the loop.The first is a container object. The second is an `std::pair` that specifies the range (start and en in which the elements will be accessed within the loop.

#### Q.18 What is the output of this piece of code?
```
int8_t a=200;
uint8_t b=100;
- if(a>b) {
    std::cout<<"greater";
    else std::cout<<"less";
}
```
 - [x] There is no output because there is an exception when comparing an int8_t with a uint8t.There is no output because there is an exception when comparing an null with a null.
 - [ ] greaternull
 - [ ] lessnull
 - [ ] There is no output because there is a compiler error.There is no output because there is a compiler error.

#### Q.19 What results from executing this code snippet? What results from executing this code snippet?
```
int x=5, y=2;
if(x & y)
{ /_part A_/ } 
else{ /_part B_/ }
```
- [ ] Part A executes because x==5 (true) and y==2 (true), thus the AND operation evaluates as true. << wrong
- [ ] Part B executes because (x & y) results in 0, or false.Part B executes because null results in 0, or false. << correct
- [ ] ?
- [ ] ?

#### Q.20 What is a valid definition for the get_length function, which returns the length of a null-terminated string? What is a valid definition for the null function, which returns the length of a null-terminated string?
- [ ] int get_length(char *str){ int count=0; while(str[count++]); return count-1; }
- [x] int get_length(char *str){ int count=0; while(str!=NULL){ count++; str++; } return count; } <<Correct
- [ ] int get_length(char *str){ int count=0; while((*str)++) count++; return count; }
- [ ] int get_length(char *str){ int count=0; while(str++) count++; return count; }

#### Q.21 Which STL class is the best fit for implementing a collection of data that is always ordered so that the pop operation always gets the greatest of the elements? Suppose you are interested only in push and pop operations.
 - [ ] std::list
 - [ ] std::vector
 - [x] std::priority_queue
 - [ ] std::map

#### Q.22 What is the meaning of the three sections specified between parentheses in a for loop separated by semicolons?
 - [ ] The first is the iterating variable name, the second is the number of times to iterate, and the third is the desired increment or decrement (specified with a signed integer).
 - [x] The first is the initialization block, the second is the condition to iterate, and the third is the increment block. 
 - [ ] The first is the iterating variable, the second is the container in which it should operate, and the third is an exit condition to abort at any time.
 - [ ] The first is the iterating variable name, the second is the starting value for the iterating variable, and the third is the stop value (the last value plus one).

#### Q.23 What is printed from this code?
```
int i = 0;
printf("%d",i++);
printf("%d",i--);
printf("%d",++i);
printf("%d",--i);
```
 - [x] 0,1,1,0
 - [ ] 0,1,0,1
 - [ ] 0,0,1,0
 - [ ] 1,0,1,0

#### Q.24 What is true about the variable named ptr?
 - [ ] It is a pointer initialized at NULL
 - [ ] It is a pointer to a void function 
 - [ ] That declaration causes a compiler error, as pointers must specify a type. 
 - [ ] It is a pointer to a value with no specific type, so it may be cast to point to any type.

#### Q.25 What is the output of this code? 
```
int c=3; char d='A';
std::printf("c is %d and d is %c",c,d);
```
 - [ ] c is d and d is c 
 - [ ] c is A and d is 3 
 - [x] c is 3 and d is A
 - [ ] c is c and d is d 

#### Q.26 What is the output of this code?
`printf("1/2 = %f",(float)(1/2));`
 - [ ] /2 = 0.499999 
 - [ ] 1/2 = 0 
 - [x] 1/2 = 0.000000
 - [ ] 1/2 = 0.5 
	
### Q.27 What is the difference between a public and a private class member?
 - [ ] Public members are the same as global variables, so every part of the code has access to them. Private members are the same as  	automatic variables, so only their class has access to them.
 - [ ] Public members are made accessible to any running application. Private members are made accessible only to the application where   the object is instantiated.
 - [ ] Public members will be compiled as shared variables in a multithreaded environment. Private members will be compiled as Thread-local variables.
 - [ ] Public members can be accessed by any function. Private members can be accessed only by the same class's member functions and the friends of the class.

### Q.28 What is the value of x after running this code?
	```
	int x=10, a=-3;
	x=+a;
	```
 - [ ] 3
 - [ ] 7
 - [ ] -3
 - [ ] 13

### Q.29 Which statement is true?
 - [ ] Only classes can have member variables and methods.
 - [x] C++ supports multiple inheritance.
 - [ ] C++ supports only single inheritance.
 - [ ] Only structs can inherit.

### Q.30 Consider a pointer to void, named ptr, which has been set to point to a floating point variable g. Which choice is a valid way to dereference ptr to assign its pointed value to a float variable f later in the program?
```
	float g;
	void *ptr=&g;
```
 - [ ] float f=*(float)ptr;
 - [ ] float f=(float *)ptr;
 - [ ] float f=(float)*ptr;
 - [x] float f=*(float *)ptr;		

### Q.31 What is the .* operator and what does it do?
 - [ ] It is the same as the class member access operator, or arrow operator (->), which allows you to access a member of an object through a pointer to the object.
 - [ ] It is the pointer to member operator, and it allows you to access a member of an object through a pointer to that specific class member.
 - [ ] It is the member access with address of operator, which returns the address of a class or struct member.
 - [ ] It is a combination of the member access operator (.) and the dereference operator (*), so it allows you to access the object that a member pointer points to 

### Q.32 For these declarations, which choice shows four equivalent ways to assign the character "y" in the string to a char variable c?

	a)	c = buff[16];
	  	C = str[5];
	   	C = * (buff+16);
	   	c = * (str+5);
	b)	C = *(buff[15]);
		C = * (str[4]);
		c = buff+15;
		C-str+4;
	c)	c = buff[15];
		C = str[4];
		c = (buff+15);
		C = *(str+4);

#### Q.33 What is the output of this code? 
`printf("1/2 = %f",(float)(1/2));`
 - [ ] 1/2 = 0.499999 
 - [ ] 1/2 = 0 
 - [x] 1/2 = 0.000000
 - [ ] 1/2 = 0.5 
