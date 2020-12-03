## C++ LinkedIn Assesment Questions Answers

Q1. What is printed from this code?

    vector<int> v(22);
    bool b= (v[6]);
    printf("%d",!b);

    a) False
    b) 0
    c) 1 << Correct
    d) This code has an error

Q2. Which of the following is a reason why using this line is considerd a bad practice?
	<pre>
	Using namespce std;
	a) The compiled code is always bigger because of all of the imported symbols.
	b) If the code uses the function defined in two different libraries with the same prototype but possibly with different implementation , there will be a compilation error due to ambuiguity.
	c) It automatically includes all header files in the standard library (cstdint,cstdlib,cstdio,iostream etc). << Correct
	d) It causes the compiler to enforce the exclusion , inclusion of header file belonging to the standard library , generating compilation error when a different header file is included.
	</pre>

Q3. What is the smallest size a variable of the type child_t may occupy in memory?
<pre>typedef struct {
unsigned int age : 4;
unsigned char gender :1;
unsigned int size : 2;
} child_t;

a) 7 bits. << Correct
b) 25 bytes.
c) 1 bit.
d) 1 bytes.
</pre>

Q4. Which of the following shows the contents of vector v1 and v2 after running this code?
<pre>std:: vector <int> v1{1,2,3},v2;
v2=v1;
v1.push_back(4);
v2.push_back(5);

a) Error <<< Correct because std::vector v1{1,2,3}; doesn't compile, It should be std::vector v1{1,2,3};
b) v1:{1,2,3,4};
   v2:{5};
c) v1:{1,2,3,4,5};
   v2:{1,2,3,4,5};
d) v1:{1,2,3,4};
   v2:{1,2,3,5}; <<  Correct
</pre>
Q5. Which of the following is a true statement about the difference between pointers and iterators?
<pre>a) While pointers are variable that hold memory address, iterators are generic functions used to traverse containers. These function allows the programmer to implement read and write code as the container is traversed. << Correct
b) Incrementing an iterator always means access the next element in the container(if any) , no matter the container. Incrementing the pointer means pointing to the next element in memory, not always the next element.
c) Pointers are variables that hold memory address where as iterator are unsigned integers that refers to offsets in arrays.
d) All iterator are implemented with pointers so all iterators are pointers but not all pointers are iterators.
</pre>
Q6. What's a benefit of declaring the parameter as a const reference instead of declaring it as a regular object.
int median(const my_arrary &a);
<pre>a) The argument is passed as a reference so the function receives a copy that can be modified without affecting the original value.
b) The argument is passed as a reference,so all if the passed my_array object is large, the program will require less time and memory. << Correct
c) Actually object can't be passed as regular variable because they require a constructor call. Therefore a const reference is the only way to pass class instances to functions.
d) There are no benefits because a reference and an object are treated as the same thing.
</pre>
Q7. What's the storage occupied by u1?
<pre>union {
unit16_t a;
unit32_t b;
int8_t c;
} u1;
a) 4 bytes << Correct You can see example [here](https://en.cppreference.com/w/cpp/language/union)
b) 7 bytes
c) 8 bytes
d) 2 bytes
</pre>
Q8. Which of the following operators is overloadable?

    a) ?:
    b) new << Correct
    c) ::
    d) .

Q9. Which of the following shows the contents of vector pointed by v1 and v2 after running this code?
<pre>std:: vector<int> *v1 = new std:: vector<int> ({1,2,3});
std:: vector<int> *v2;
v2=v1;
v1->push_back(4);
v2->push_back(5);

a) *v1:{1,2,3,4};
   *v2:{5};
b) *v1:{1,2,3,4'5};
   *v2:{1,2,3,4,5};
c) Error << Correct
d) *v1:{1,2,3,4};
   *v2:{1,2,3,5};
</pre>

Q10. Which of the following is not a difference between a class and a struct?
<pre>a) Because structor are part of the c programming language there some complexity between c and c++ struct This is not the case with classes.
b) Classes may have member function;struct private.
c) The default acces specifier for members of struct is public, where as for member of class , it is private. << Correct -> You can see the answer [here](https://www.fluentcpp.com/2017/06/13/the-real-difference-between-struct-class/)
d) Template type parameters can be declared with , but not with the struct keyword.
</pre>
Q11. Suppose you need to keep a data struct with permission to access some resource base on the days of week , but you can't be use a bool variable for each day.you need to use one bit per day of the week.
which of the following is a correct implementation of a structure with bit fields for this application?

    a) typedef struct {
    		int sunday:1;
    		int monday:1;
    		// more days
    		int friday:1;
    		int satarday:1;
    		} weekdays; << Correct  That syntax says that each variable size is 1 bit. 'bit' is not a type in C++.
    b) typedef char[7]: weekdays;
    c) typedef struct {
    		bit sunday:1;
    		bit monday:1;
    		// more days
    		bit fridyas:1;
    		bit satarday:1;
    		} weekdays;
    d) typedef struct {
    		bit sunday;
    		bit monday;
    		// more days
    		bit friday;
    		bit satarday;
    		} weekdays;

Q12. What is an lvalue?
<pre>a) It's a constant expression , meaning an expression composed of constants and operations.
b) It's an expression that represents an object with an address. << Correct
c) It's an expression suitable for the left hand side operand in binary operation.
d) It's a location value , meaning a memory address suitable for assigning to pointer or reference.
</pre>
Q13. What does auto type specifier do in this line of code (since c++ 11)?

    a) It specifies that the type of x will be deducted from the initializer in this case,double.
    b) It specifies that the type of x is automatic meaning that if can be assigned different type of data throughout the program.
    c) It specifies that x is a variable with automatic storage duration. << Correct
    d) It soecifies that more memory will be allocated for x in case it needs more space, avoiding loss of data due to overflow.

Q14. What is a class template?

    a) It's a class written with the generic programming , specifying behavior in terms of type parameter rather than specific type. << Correct
    b) It's a blank superclass intended for inheritence and polymorphism.
    c) It's class that only consists of member variable , with no constructor , destructor nor member functions.
    d) It's skelton source code for a class where the programming has to fill in specific parts to define the data types and algorithms used.

Q15. What is the ternary operator equivalent to this code snippet?

    if(x)
    y=a;
    else
    y=b;

    a) y=a?b:x;
    b) y=if(x?a:b);
    c) y=(x&a)?a:(x&b)?b:0;
    d) y=x?a:b; << Correct

Q16. What is the output of this code? What is the output of this code?

    #include <iostream>
    int main()
    {
    	int x=10, y=20;
    	std::cout << "x = " << x++ << " and y = " << --y << std::endl;
    	std::cout << "x = " << x-- << " and y = " << ++y << std::endl;
    	return(0);
    }

    a) x = 10 and y = 20 x = 11 and y = 19
    b) x = 11 and y = 19 x = 10 and y = 20
    c) x = 10 and y = 19 x = 11 and y = 20 << Correct
    d) x = 11 and y = 20 x = 10 and y = 19

Q.17 What is the meaning of the two parts specified between parentheses in a range-based for loop, separated by a colon?What is the meaning of the two parts specified between parentheses in a range-based for loop, separated by a colon?

    a) The first is a variable declaration that will hold an element in a sequence. The second is the sequence to traverse.
	
    b) The first is an iterator, and the second is the increment value to be added to the iterator. The first is an iterator, and the second is the increment value to be added to the iterator.


    c) The first is the iterating variable. The second is an std::pair that specifies the range (start and end) in which the variable will iterate.The first is the iterating variable. The second is an std::pair that specifies the range (start and end) in which the variable will iterate.


    d)The first is a container object. The second is an std::pair that specifies the range (start and end) in which the elements will be accessed within the loop.The first is a container object. The second is an std::pair that specifies the range (start and end) in which the elements will be accessed within the loop.

Q.18 What is the output of this piece of code? What is the output of this piece of code?
<pre>
int8_t a=200;
uint8_t b=100;
if(a>b) {
std::cout<<"greater";
else std::cout<<"less";
}

a)There is no output because there is an exception when comparing an int8_t with a uint8t.There is no output because there is an exception when comparing an null with a 	 null. << Correct
b)greaternull
c)lessnull
d)There is no output because there is a compiler error.There is no output because there is a compiler error.
</pre>
Q.19 What results from executing this code snippet? What results from executing this code snippet?<br/>
int x=5, y=2; <br/>
if(x & y)<br/>
{ /_part A_/ }<br/> 
else{ /_part B_/ }<br/><br/>
a) Part A executes because x==5 (true) and y==2 (true), thus the AND operation evaluates as true.Part A executes because null (true) and null (true), thus the null operation evaluates as true.<br/>
b) Part B executes because (x & y) results in 0, or false.Part B executes because null results in 0, or false. <<Correct<br/>
c) Part A executes because (x & y) results in a nonzero value, or true.Part A executes because null results in a nonzero value, or true.<br/>
d) Part B executes because the statement (x & y) is invalid, thus false.Part B executes because the statement null is invalid, thus false.<br/>
Q.20 What is a valid definition for the get_length function, which returns the length of a null-terminated string? What is a valid definition for the null function, which returns the length of a null-terminated string?<br>

int get_length(char \*str);<br/><br/>

a) int get_length(char *str){ int count=0; while(str[count++]); return count-1; }<br/>
b) int get_length(char *str){ int count=0; while(str!=NULL){ count++; str++; } return count; } <<Correct<br/>
c) int get_length(char *str){ int count=0; while((*str)++) count++; return count; }<br/>
d) int get_length(char *str){ int count=0; while(str++) count++; return count; }<br/>

Q.21 Which STL class is the best fit for implementing a collection of data that is always ordered so that the pop operation always gets the greatest of the elements? Suppose you are interested only in push and pop operations.

	a) std::list
	b) std::vector
	c) std::priority_queue
	d) std::map

Q.22 What is the meaning of the three sections specified between parentheses in a for loop separated by semicolons?

	a) The first is the iterating variable name, the second is the number of times to iterate, and the third is the desired increment or decrement (specified with a signed integer).
	b) The first is the initialization block, the second is the condition to iterate, and the third is the increment block. 
	c) The first is the iterating variable, the second is the container in which it should operate, and the third is an exit condition to abort at any time.
	d) The first is the iterating variable name, the second is the starting value for the iterating variable, and the third is the stop value (the last value plus one). 


Q.23 What is printed from this code?

	int i = 0;
	printf("%d",i++);
	printf("%d",i--);
	printf("%d",++i);
	printf("%d",--i);
	
	a) 0,1,1,0 << correct
	b) 0,1,0,1
	c) 0,0,1,0
	d) 1,0,1,0

Q.24 What is true about the variable named ptr?

	a) It is a pointer initialized at NULL
	b) It is a pointer to a void function 
	c) That declaration causes a compiler error, as pointers must specify a type. 
	d) It is a pointer to a value with no specific type, so it may be cast to point to any type. 

Q.25 What is the output of this code? 

	int c=3; char d='A';
	std::printf("c is %d and d is %c",c,d);
	
	a) c is d and d is c 
	b) c is A and d is 3 
	c) c is 3 and d is A << correct
	d) c is c and d is d 
Q.26 What is the output of this code? 

	printf("1/2 = %f",(float)(1/2)); 
	
	a) 1/2 = 0.499999 
	b) 1/2 = 0 
	c) 1/2 = 0.000000 << correct
	d) 1/2 = 0.5 
