# pluralsight python core

## Q1 What function can find the list size?
- [] count()
- [] size()
- [] pos()
- [x] len() 

## Q2 What signal detection statement could stop an iterator from executing more than seven times?
- [x] if self.x <= 7:
- [] if self.x > 6:
- [] else self.x = 6:
- [] else self.x < 7:

## Q3 How can you create a global variable in Python?
- [x] You use the global keyword before its first assignment
- [] you cannot have global variables
- [] you can only do it in modules
- [] place it on top of the script

## Q4 What built-in function can operate on any iterable type and be used to filter what is passed to it?
- [] filt()
- [] f()
- [x] filter()
- [] filt()

## Q5 What shows the proper use of length?
- [] len[a]
- [] a._len_()
- [x] len(a)
- [] len().a

## Q6 When using contextmanager from contextlib module, what decorator do you use?
- [] !#contextmanager
- [x] contextlib.manager
- [] @contextmanager
- [] dec contextmanager

## Q7 Which method must you define for an iterable object?
- [] __iterator__
- [x] iterable
- [] next
- [] __iter__

## Q8 How to do a most efficient multiply function with two arguments as numbers?
- [] 
def multiply(x,y):
  z=x*y
  return z

- [x] 
def multiply(x,y):
  return x*y

- [] 
def multiply(ar1,ar2):
  z=x*y
  return z

- [] 
def multiply(kwargs):
  z=x*y
  return z

## Q9 What print function do you use to print out "Casey"?
employee={ 'firstname': 'Casey', 'lastname': 'Smith','age':43, 'hobbies': 'tennis'}
- [] print (employee('firstname'))
- [] print (employee[firstname])
- [x] print (employee['firstname'])
- [] print (employee.firstname)

## Q10 You use a custom context manager for the with statement to open a file. You run the code, but the file is still open. What can solve it?
class customContext:
    def __init__(myfile,name):
        myfile.name=name

    def __enter__(myfile):
        myfile.file=open(myfile.name, 'r')
        return myfile.file

    def __exit__(myfile):
        if myfile.file:

- [] myfile.file.close()
- [x] myfile.end
- [] myfile.name(close)
- [] del myfile

## Q11 What is an example of a relational operator?
- [] *
- [x] <
- [] &
- [] !

## Q12 Using a built-in Python function, what code option finds the distance from zero of the value of y?
- [] ero(y-0)
- [] sum(y-0)
- [] calc(y+0)
- [x] abs(y)

## Q13 What is the difference between a mutable and an immutable object?
- [] The immutable object type can only be string values while mutable object types can be any other valid data type
- [] The mutable object type can only be a List but the immutable object type cannot be a List.

- [] You cannot change the value of a mutable object after you create it while you can change an immutable object value after you create it.

- [x] You cannot change the value of an immutable object after you create it while you can change a mutable ok value after you create it.

## Q14 You're given the following directory tree:

dir
|
+-- my_script. py
|

+-- package
    |
    +-- _init_.py
    |
    +-- subpackage
        |
        +-- _init_.py
        |
        +-- module.py

What import statement would you use to import function1 located in module.py ?

- [] import function1 from module
- [x] from package.subpackage.module import function1
- [] from module1 import function1
- [] from ..package import function1

## Q15 What is the purpose of the continue statement inside a loop?

- [] It completely exits the program
- [] It leaves the loop and continues with the rest of the program
- [x] It leaves the current iteration and moves on to the next iteration 
- [] It leaves the loop after completing the current iteration

## Q16 You must review some code for a Python script designed to gather information from end users. What is the problem with the following code?

var = 1
while var == num = raw_input("Enter a number :")
    print “You entered: ", num

- [] The num variable will not function outside the while loop so the last print statement will fail
- [x] Var never in- or decreases so there is an infinite loop
- [] The library for the raw_input() function is not included in the script.
- [] The double equal sign in the while conditional will cause a syntax error.

## Q17 You are a data engineer working on a project that calculates oil pipeline revenues using Python for large data sets. In your code, you have a tuple that contains the current price for oil for different geographic areas. You wrote a function that will update this tuple when oil prices change for that area, however you are getting errors in Python when the function executes. What is the likely cause of this error?

- [] The function is taking in the tuple by reference not by value and therefore cannot update it
- [] You must use an anonymous function in Python if you want to update a tuple.
- [] The function that updates the tuple is using a different data type than it was inizialized with
- [x] Tuples are immutable and cannot be changed, therefore you should use an array instead. 

 
## Q18 You have a package that is developed on a different location from the default location. How can you make sure every time you open the shell, the package can be imported?

- [] Move the package to the known Python package paths.
- [] Add the path of the package with the sys module every time you rely on that specific package in your further scripts.
- [x] Either add the package's path to the default path so Python can find it, or install the package with pip install -e package So it will be installed by pip and known by the interpreter but remain editable
- [] Open the shell at the package's directory, so when the shell is opened it can find it.
