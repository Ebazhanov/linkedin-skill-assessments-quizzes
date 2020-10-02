C++ LinkedIn Assesment Questions Answers
-

Q1. What is printed from this code?

	vector<int> v(22);
	bool b= (v[6]);
	printf("%d",!b);
	
	a) False  
	b) 0
	c) 1 << Correct
	d) This code has an error

Q2. Which of the following is a reason why using this line is considerd a bad practice?
	Using namespce std;
	
	a) The compiled code is always bigger because of all of the imported symbols.
	b) If the code uses the function defined in two different libraries with the same prototype but possibly with different implementation , there will be a compilation error due to ambuiguity.
	c) It automatically includes all header files in the standard library (cstdint,cstdlib,cstdio,iostream etc). << Correct
	d) It causes the compiler to enforce the exclusion , inclusion of header file belonging to the standard library , genrating compilation error when a different header file is included.

Q3. What is the smallest size a variable of the type child_t may occupy in memory?
	typedef struct {
		unsigned int age : 4;
		unsigned char gender :1;
		unsigned int size : 2;
		} child_t;

	a) 7 bits.
	b) 25 bytes.<< Correct
	c) 1 bit.
	d) 1 bytes. 

Q4. Which of the following shows the contents of vector v1 and v2 after running this code?
	std:: vector <int> v1{1,2,3},v2;
	v2=v1;
	v1.push_back(4);
	v2.push_back(5);

	a) Error
	b) v1:{1,2,3,4};
	   v2:{5};
	c) v1:{1,2,3,4,5};
	   v2:{1,2,3,4,5};
	d) v1:{1,2,3,4};
	   v2:{1,2,3,5}; <<  Correct

Q5. Which of the following is a true statement about the difference between pointers and iterators?
	
	a) While pointers are variable that hold memory address , iterators are genric functions used to traverse containers. These function allows the programmer to implement read and write code as 			the container is traversed. << Correct
	b) Incrementing an iterator always means acces the next element in the container(if any) , no matter the container. Incrementing the pointer means pointing to the next element in memory, not 			always the next element.
	c) Pointers are variables that hold memory address where as iterotor are unsigned integers that refers to offsets in arrays.
	d) All iterator are implemented with pointers so all iterators are pointers but not all pointers are iterators.

Q6. What's a benefit of declaring the parameter as a const reference instead of declaring it as a regular 	object.
	
	int median(const my_arrary &a);
	
	a) The argument is passed as a reference so the function receives a copy that can be modified without affecting the original value. 
	b) The argument is passed as a reference,so all if the passed my_array object is large, the program will require less time and memory. << Correct
	c) Actually object can't be passed as regular variable because they require a constructor call. Therefore a const reference is the only way to pass class instances to functions.
	d) There are no benefits because a reference and an object are treated as the same thing.

Q7. What's the storage occupied by u1?
	union {
		unit16_t a;
		unit32_t b;
		int8_t c;
	} u1;
	
	a) 4 bytes
	b) 7 bytes 
	c) 8 bytes << Correct
	d) 2 bytes

Q8. Which of the following operators is overloadable?

	a) ?:
	b) new << Correct
	c) ::
	d) .

Q9. Which of the following shows the contents of vector pointed by v1 and v2 after running this code?
	std:: vector<int> *v1 = new std:: vector<int> ({1,2,3});
	std:: vector<int> *v2;
	v2=v1;
	v1->push_back(4);
	v2->push_back(5);

	a) *v1:{1,2,3,4};
	   *v2:{5};
	b) *v1:{1,2,3,4'5};
	   *v2:{1,2,3,4,5};
	c) Error
	d) *v1:{1,2,3,4};
	   *v2:{1,2,3,5}; << Correct

Q10. Which of the following is not a difference between a class and a struct?
	
	a) Because structor are part of the c programming language there some complexity between c and c++ struct This is not the case with classes. << Correct
	b) Classes may have member function;struct private.
	c) The default acces specifier for members of struct is public, where as for member of class , it is private.
	d) Template type parameters can be declared with , but not with the struct keyword.

Q11. Suppose you need to keep a data struct with permission to access some resource base on the days of week , but you can't be use a bool variable for each day.you need to use one bit per day of the week. 	
	which of the following is a correct implementation of a structure with bit fields for this application?

	a) typedef struct {
			int sunday:1;
			int monday:1;
			// more days 
			int friday:1;
			int satarday:1;
			} weekdays;
	b) typedef char[7]: weekdays;
	c) typedef struct {
			bit sunday:1;
			bit monday:1;
			// more days
			bit fridyas:1;
			bit satarday:1;
			} weekdays; << Correct
	d) typedef struct { 
			bit sunday;
			bit monday;
			// more days
			bit friday;
			bit satarday;
			} weekdays;

Q12. What is an lvalue?
	
	a) It's a constant expression , meaning an expression composed of constants and operations. 
	b) It's an expression that represents an object with an address. << Correct
	c) It's an expression suitable for the left hand side operand in binary operation.
	d) It's a location value , meaning a memory address suitable for assigning to pointer or reference.

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







	
