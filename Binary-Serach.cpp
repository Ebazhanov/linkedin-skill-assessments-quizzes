This content help to understand how to use concept of Binary search and this is also use for interviews perpuse ..
C++ Algorithm binary_search() function is used check whether the element in the range [first, last) is equivalent to val (or a binary predicate) and false otherwise.

The range [first, last) must satisfy all of the following conditions:
Partitioned with respect to element < val or comp (element, val).
Partitioned with respect to !(val < element) or !comp(value, element)
For all elements, if element < val or comp (element, val) is true then !(val < element) or !comp(val, element) is also true.
The first version uses operator< to compare the elements and the second version uses the given comparison function i.e. comp.
           Syntax
default (1)       template <class ForwardIterator, class T>  
                        bool binary_search (ForwardIterator first, ForwardIterator last,  
                             const T& val);  
  
custom (2)      template <class ForwardIterator, class T, class Compare>  
                       bool binary_search (ForwardIterator first, ForwardIterator last,  
                             const T& val, Compare comp);  
Parameter
first: A forward iterator pointing to the first element in the range to be searched.

last: A forward iterator pointing to the past last element in the range to be searched.

comp: A user-defined binary predicate function that accepts two arguments and returns true if the two arguments are in order and false otherwise. It follows the strict weak ordering to order the elements.
           #include <iostream>  
#include <vector>  
#include <algorithm>  
   
using namespace std;  
   
int main()  
{  
  int a[] = {1, 2, 3, 4, 5, 6, 7, 9, 10};  
  vector<int> v(a, a+9);  
  cout <<"\nHere are the values in the vector:\n";  
  for (vector<int>::size_type i=0; i<v.size(); i++)  
    cout <<v.at(i)<<" ";  
   
  if (binary_search(v.begin(), v.end(), 3))  
    cout <<"\nThe value 3 was found.";  
  else  
    cout <<"\nThe value 3 was not found.";  
   
  if (binary_search(v.begin(), v.end(), 8))  
    cout <<"\nThe value 8 was found.";  
  else  
    cout <<"\nThe value 8 was not found.";  
   
  return 0;  
}  
           OUTPUTS:-
           Here are the values in the vector:
           1 2 3 4 5 6 7 9 10 
           The value 3 was found.
           The value 8 was not found.
