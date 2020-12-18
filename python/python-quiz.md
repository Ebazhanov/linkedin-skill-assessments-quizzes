## Python Assessment

---

#### Q1. What is an abstract class?

- [ ] An abstract class is the name for any class from which you can instantiate an object.
- [ ] Abstract classes must be redefined any time an object is instantiated from them.
- [ ] Abstract classes must inherit from concrete classes.
- [x] An abstract class exists only so that other "concrete" classes can inherit from the abstract class.

#### Q2. What happens when you use the build-in function `any()` on a list?

- [ ] The `any()` function will randomly return any item from the list.
- [x] The `any()` function returns True if any item in the list evaluates to True. Otherwise, it returns False.
- [ ] The `any()` function takes as arguments the list to check inside, and the item to check for. If "any" of the items in the list match the item to check for, the function returns True.
- [ ] The `any()` function returns a Boolean value that answers the question "Are there any items in this list?"

#### Q3. What data structure does a binary tree degenerate to if it isn't balanced properly?

- [x] `linked list`
- [ ] `queue`
- [ ] `set`
- [ ] `OrderedDict`

#### Q4. What is a static method?

- [ ] `Static methods are called static because they always return "None".`
- [ ] `Static methods can be bound to either a class or an instance of a class.`
- [x] `They serve mostly as utility methods or helper methods, since they can't access or modify a class's state.`
- [ ] `Static methods can access and modify the state of a class or an instance of a class.`

#### Q5. What are attributes?

- [ ] Attributes are long-form version of an `if/else` statement, used when testing for equality between objects.
- [x] Attributes are a way to hold data or describe a state for a class or an instance of a class.
- [ ] Attributes are strings that describe characteristics of a class.
- [ ] Function arguments are called "attributes" in the context of class methods and instance methods.

#### Q6. What is the term to describe this code?

```python
count, fruit, price = (2, 'apple', 3.5)
```

- [ ] `tuple assignment`
- [x] `tuple unpacking`
- [ ] `tuple matching`
- [ ] `tuple duplication`

#### Q7. What built-in list method would you use to remove items from a list?

- [ ] `".delete()" method`
- [ ] `pop(my_list)`
- [ ] `del(my_list)`
- [x] `".pop()" method`

#### Q8. What is one of the most common use of Python's sys library?

- [x] `to capture command-line arguments given at a file's runtime`
- [ ] `to connect varios systems, such as connecting a web front end, an API service, a database, and a mobile app`
- [ ] `to take a snapshot of all the packages and libraries in your virtual environment`
- [ ] `to scan the health of your Python ecosystem while inside a virtual environment`

#### Q9. What is the runtime of accessing a value in a dictionary by using its key?

- [ ] `"O(n)", also called linear time`
- [ ] `"O(log n)", also called logarithmic time`
- [ ] `"O(n^2)", also called quadratic time`
- [x] `"O(1)", also called constant time`

#### Q10. What is the correct syntax for defining a class called Game?

- [x] `class Game: pass`
- [ ] `def Game(): pass`
- [ ] `def Game: pass`
- [ ] `class Game(): pass`

#### Q11. What is the correct way to write a doctest?

- [ ] `-`

```
def sum(a, b):
    """
    sum(4, 3)
    7

    sum(-4, 5)
    1
    """
    return a + b
```

- [x] `-`

```
def sum(a, b):
    """
    >>> sum(4, 3)
    7

    >>> sum(-4, 5)
    1
    """
    return a + b
```

- [ ] `-`

```
def sum(a, b):
    """
    # >>> sum(4, 3)
    # 7

    # >>> sum(-4, 5)
    # 1
    """
    return a + b
```

- [ ] `-`

```
def sum(a, b):
    ###
    >>> sum(4, 3)
    7

    >>> sum(-4, 5)
    1
    ###
    return a + b
```

#### Q12. What buit-in Python data type is commonly used to represent a stack?

- [ ] `set`
- [x] `list`
- [ ] `None. You can only build a stack from scratch.`
- [ ] `dictionary`

#### Q13. What would this expression return?

```
college_years = ['Freshman', 'Sophomore', 'Junior', 'Senior']
return list(enumerate(college_years, 2019)
```

- [ ] `[('Freshman', 2019), ('Sophomore', 2020), ('Junior', 2021), ('Senior', 2022)]`
- [ ] `[(2019, 2020, 2021, 2022), ('Freshman', 'Sophomore', 'Junior', 'Senior')]`
- [ ] `[('Freshman', 'Sophomore', 'Junior', 'Senior'), (2019, 2020, 2021, 2022)]`
- [x] `[(2019, 'Freshman'), (2020, 'Sophomore'), (2021, 'Junior'), (2022, 'Senior')]`

#### Q14. How does `defaultdict` work?

- [ ] `defaultdict` will automatically create a dictionary for you that has keys which are the integers 0-10.
- [ ] `defaultdict` forces a dictionary to only accept keys that are of the types specified when you created the `defaultdict` (such as string or integers).
- [x] If you try to access a key in a dictionary that doesn't exist, `defaultdict` will create a new key for you instead of throwing a `KeyError`.
- [ ] `defaultdict` stores a copy of a dictionary in memory that you can default to if the original gets unintentionally modified.

#### Q15. What is the correct syntax for defining a class called "Game", if it inherits from a parent class called "LogicGame"?

- [ ] `class Game.LogicGame(): pass`
- [ ] `def Game(LogicGame): pass`
- [x] `class Game(LogicGame): pass`
- [ ] `def Game.LogicGame(): pass`

#### Q16. What is the purpose of the "self" keyword when defining or calling instance methods?

- [ ] `self means that no other arguments are required to be passed into the method`
- [ ] `There is no real purpose for the self method; it"s just historic computer science jargona that Python keeps to stay consistent with other programming languages`
- [x] `self refers to the instance whose method was called`
- [ ] `self refers to the class that was inherited from to create the object using self`

#### Q17. Which of these is NOT a characteristic of namedtuples?

- [ ] `You can assign a name to each of the namedtuple members and refer to them that way, similarly to how you would access keys in dictionary`
- [ ] `Each member of a namedtuple object can be indexed to directly, just like in a regular tuple`
- [ ] `namedtuples are just as memory efficient as regular tuples`
- [x] `No import is needed to use namedtuples because they are available in the standard library`

#### Q18. What is an instance method?

- [x] `Instance methods can modify the state of an instance or the state of its parent class`
- [ ] `Instance methods hold data related to the instance`
- [ ] `An instance method is any class method that doesn"t take any arguments`
- [ ] `An instance method is a regular function that belongs to a class, but it must return None`

#### Q19. Which choice is the most syntactically correct example of the conditional branching?

- [ ] `-`

```
num_people = 5

if num_people > 10;
    print("There is a lot of people in the pool.")
elif num_people > 4;
    print("There are some people in the pool.")
elif num_people > 0;
    print("There are a few people in the pool.")
else:
    print("There is no one in the pool.")
```

- [ ] `-`

```
num_people = 5

if num_people > 10;
    print("There is a lot of people in the pool.")
if num_people > 4;
    print("There are some people in the pool.")
if num_people > 0;
    print("There are a few people in the pool.")
else:
    print("There is no one in the pool.")
```

- [x] `-`

```
num_people = 5

if num_people > 10:
    print("There is a lot of people in the pool.")
elif num_people > 4:
    print("There are some people in the pool.")
elif num_people > 0:
    print("There are a few people in the pool.")
else:
    print("There is no one in the pool.")
```

- [ ] `-`

```
if num_people > 10;
    print("There is a lot of people in the pool.")
if num_people > 4;
    print("There are some people in the pool.")
if num_people > 0;
    print("There are a few people in the pool.")
else:
    print("There is no one in the pool.")
```

#### Q20. Which statement does NOT describe the object-oriented programming concenpt of encapsulation?

- [ ] `It protects the data from outside interference `
- [ ] `A parent class is encapuslated and no data from the parent class passes on to the child class`
- [ ] `It keeps data and the methods that can manipulate that data in one place`
- [x] `It only allows the data to be changed by methods`

#### Q21. What is the purpose of an if/else statement?

- [ ] `An if/else statement tells the computer which chunk of code to run if the instructions you coded are incorrect `
- [ ] `An if/else statement runs one chunk of code if all the imports were succesful, and another chunk of code if the imports were not succesful `
- [x] `An if/else statement executes one chunk of code if a condition it true, but a different chunk of code if the condition is false`
- [ ] `An if/else statement tells the computer which chunk of code to run if the is enough memory to handle it. and which chunk of code to run if there is not enough memory to handle it`

#### Q22. What buit-in Python data type is commonly used to represent a queue?

- [ ] `dictionary`
- [ ] `set`
- [ ] `None. You can only build a stack from scratch.`
- [x] `list`

#### Q23. What is the correct syntax for instantiating a new object of the type Game?

- [ ] `my_game = class.Game()`
- [ ] `my_game = class(Game)`
- [x] `my_game = Game()`
- [ ] `my_game = Game.create()`

#### Q24. What does the built-in map() function do?

- [ ] It creates a path from multiple values in an iterable to a single value.
- [x] It applies a function to each item in an iterable and returns the value of that function.
- [ ] It converts a complex value type into simpler value types.
- [ ] It creates a mapping between two different elements of different iterables.

#### Q25. If you don't explicitly return a value from a function, what happens?

- [ ] `The function will return a RuntimeError if you don't return a value.`
- [x] `If the return keyword is absent, the function will return None.`
- [ ] `If the return keyword is absent, the function will return True.`
- [ ] `The function will enter an infinite loop because it won't know when to stop executing its code.`

#### Q26. What is the purpose of the `pass` statement in Python?

- [ ] It is used to skip the `yield` statement of a generator and return a value of None.
- [x] It is a null operation used mainly as a placeholder in functions, classes, etc.
- [ ] It is used to pass control from one statement block to another.
- [ ] It is used to skip the rest of a `while` or `for loop` and return to the start of the loop.

#### Q27. What is the term used to describe items that may be passed into a function?

- [x] `arguments`
- [ ] `paradigms`
- [ ] `attributes`
- [ ] `decorators`

#### Q28. Which collection type is used to associate values with unique keys?

- [ ] `slot`
- [x] `dictionary`
- [ ] `queue`
- [ ] `sorted list`

#### Q29. When does a for loop stop iterating?

- [ ] `when it encounters an infinite loop`
- [ ] `when it encounters an if/else statement that contains a break keyword`
- [x] `when it has assessed each item in the iterable it is working on or a break keyword is encountered`
- [ ] `when the runtime for the loop exceeds O(n^2)`

#### Q30. Assuming the node is in a singly linked list, what is the runtime complexity of searching for a specific node within a singly linked list?

- [x] The runtime is O(n) because in the worst case, the node you are searching for is the last node, and every node in the linked list must be visited.
- [ ] The runtime is O(nk), with n representing the number of nodes and k representing the amount of time it takes to access each node in memory.
- [ ] The runtime cannot be determined unless you know how many nodes are in the singly linked list.
- [ ] The runtime is O(1) because you can index directly to a node in a singly linked list.

#### Q31. Given the following three list, how would you create a new list that matches the desired output printed below?

```
fruits = ['Apples', 'Oranges', 'Bananas']
quantities = [5, 3, 4]
prices = [1.50, 2.25, 0.89]

# Desired output
[('Apples', 5, 1.50),
('Oranges', 3, 2.25),
('Bananas', 4, 0.89)]
```

- [ ] `-`

```
output = []

fruit_tuple_0 = (first[0], quantities[0], price[0])
output.append(fruit_tuple)

fruit_tuple_1 = (first[1], quantities[1], price[1])
output.append(fruit_tuple)

fruit_tuple_2 = (first[2], quantities[2], price[2])
output.append(fruit_tuple)

return output
```

- [x] `-`

```
i = 0
output = []
for fruit in fruits:
    temp_qty = quantities[i]
    temp_price = prices[i]
    output.append((fruit, temp_qty, temp_price))
    i += 1
return output
```

- [ ] `-`

```
groceries = zip(fruits, quantities, prices)
return groceries

>>> [
('Apples', 5, 1.50),
('Oranges', 3, 2.25),
('Bananas', 4, 0.89)
]
```

- [ ] `-`

```
i = 0
output = []
for fruit in fruits:
    for qty in quantities:
        for price in prices:
            output.append((fruit, qty, price))
    i += 1
return output
```

#### Q32. What happens when you use the built-in function all() on a list?

- [ ] `The all() function returns a Boolean value that answers the question "Are all the items in this list the same?"`
- [ ] `The all() function returns True if all the items in the list can be converted to strings. Otherwise, it returns False.`
- [ ] `The all() function will return all the values in the list.`
- [x] `The all() function returns True if all items in the list evaluate to True. Otherwise, it returns False.`

#### Q33. What is the correct syntax for calling an instance method on a class named Game?

- [x] `-`

```
>>> dice = Game()
>>> dice.roll()
```

- [ ] `-`

```
>>> dice = Game(self)
>>> dice.roll(self)
```

- [ ] `-`

```
>>> dice = Game()
>>> dice.roll(self)
```

- [ ] `-`

```
>>> dice = Game(self)
>>> dice.roll()
```

#### Q34. What is the algorithmic paradigm of quick sort?

- [ ] `backtracking`
- [ ] `dynamic programming`
- [ ] `decrease and conquer`
- [x] `divide and conquer`

#### Q35. What is runtime complexity of the list's built-in .append() method?

- [x] `O(1), also called constant time`
- [ ] `O(log n), also called logarithmic time`
- [ ] `O(n^2), also called quardratic time`
- [ ] `O(n), also called linear time`

#### Q36. What is key difference between a set and a list?

- [ ] A set is an ordered collection unique items. A list is an unordered collection of non-unique items.
- [ ] Elements can be retrieved from a list but they cannot be retrieved from a set.
- [ ] A set is an ordered collection of non-unique items. A list is an unordered collection of unique items.
- [x] A set is an unordered collection unique items. A list is an ordered collection of non-unique items.

#### Q37. What is the definition of abstraction as applied to object-oriented Python?

- [ ] `Abstraction means that a different style of code can be used, since many details are already known to the program behind the scenes.`
- [x] `Abstraction means the implementation is hidden from the user, and only the relevant data or information is shown.`
- [ ] `Abstraction means that the data and the functionality of a class are combined into one entity.`
- [ ] `Abstraction means that a class can inherit from more than one parent class.`

#### Q38. What does this function print?

```
def print_alpha_nums(abc_list, num_list):
    for char in abc_list:
        for num in num_list:
            print(char, num)
    return

print_alpha_nums(['a', 'b', 'c'], [1, 2, 3])
```

- [x] `-`

```
a 1
a 2
a 3
b 1
b 2
b 3
c 1
c 2
c 3
```

- [ ] `-`

```
['a', 'b', 'c'], [1, 2, 3]
```

- [ ] `-`

```
aaa
bbb
ccc
111
222
333
```

- [ ] `-`

```
a 1 2 3
b 1 2 3
c 1 2 3
```

#### Q39. What is the correct syntax for calling an instance method on a class named `Game`?

- [x] `-`

```
my_game = Game()
my_game.roll_dice()
```

- [ ] `-`

```
my_game = Game()
self.my_game.roll_dice()
```

- [ ] `-`

```
my_game = Game(self)
self.my_game.roll_dice()
```

- [ ] `-`

```
my_game = Game(self)
my_game.roll_dice(self)
```

#### Q40. Correct representation of doctest for function in Python

- [ ] `-`

```
def sum(a, b):
    # a = 1
    # b = 2
    # sum(a, b) = 3

    return a + b
```

- [ ] `-`

```
def sum(a, b):
    """
    a = 1
    b = 2
    sum(a, b) = 3
    """

    return a + b
```

- [x] `-`

```
def sum(a, b):
    """
    >>> a = 1
    >>> b = 2
    >>> sum(a, b)
    3
    """

    return a + b
```

- [ ] `-`

```
def sum(a, b):
    '''
    a = 1
    b = 2
    sum(a, b) = 3
    '''
    return a + b
```

#### Q41. Suppose a Game class inherits from two parent classes: BoardGame and LogicGame. Which statement is true about the methods of an object instantiated from the Game class?

- [ ] `When instantiating an object, the object doesn't inherit any of the parent class's methods.`
- [ ] `When instantiating an object, the object will inherit the methods of whichever parent class has more methods.`
- [ ] `When instantiating an object, the programmer must specify which parent class to inherit methods from.`
- [x] `An instance of the Game class will inherit whatever methods the BoardGame and LogicGame classes have.`

#### Q42. What does calling namedtuple on a collection type return?

- [ ] `a generic object class with iterable parameter fields`
- [ ] `a generic object class with non-iterable named fields`
- [ ] `a tuple subclass with non-iterable parameter fields`
- [x] `a tuple subclass with iterable named fields`

#### Q43. What symbol(s) do you use to assess equality between two elements?

- [ ] `&&`
- [ ] `=`
- [x] `==`
- [ ] `||`

#### Q44. Review the code below. What is the correct syntax for changing the price to 1.5?

fruit_info = {
'fruit': 'apple',
'count': 2,
'price': 3.5
}

- [x] `fruit_info ['price'] = 1.5`
- [ ] `my_list [3.5] = 1.5`
- [ ] `1.5 = fruit_info ['price]`
- [ ] `my_list['price'] == 1.5`

#### Q45. What value would be returned by this check for equality?

5!=6

- [ ] `yes`
- [ ] `False`
- [x] `True`
- [ ] `None`

#### Q46. What does a class's **init**() method do?

- [ ] `The __init_method makes classes aware of each other if more than one class is defined in a single code file.`
- [ ] `The _init_method is included to preserve backwards compatibility from Python 3 to Python 2, but no longer needs to be used in Python 3.`
- [x] `The __init__() method is a constructor method that is called automatically whenever a new object is created from a class. It sets the initial state of a new object.`
- [ ] `The __init__ method initializes any imports you may have included at the top of your file.`

#### Q47. What is meant by the phrase "space complexity"?

- [ ] `How many microprocessors it would take to run your code in less than one second`
- [ ] `How many lines of code are in your code file`
- [x] `The amount of space taken up in memory as a function of the input size`
- [ ] `How many copies of the code file could fit in 1 GB of memory`

#### Q48. What is the correct syntax for creating a variable that is bound to a dictionary?

- [x] `fruit_info = {'fruit': 'apple', 'count': 2, 'price': 3.5}`
- [ ] `fruit_info =('fruit': 'apple', 'count': 2,'price': 3.5 ).dict()`
- [ ] `fruit_info = ['fruit': 'apple', 'count': 2,'price': 3.5 ].dict()`
- [ ] `fruit_info = to_dict('fruit': 'apple', 'count': 2, 'price': 3.5)`

#### Q49. What is the proper way to write a list comprehension that represents all the keys in this dictionary?

fruits = {'Apples': 5, 'Oranges': 3, 'Bananas': 4}

- [ ] `fruit_names = [x in fruits.keys() for x]`
- [ ] `fruit_names = for x in fruits.keys() *`
- [x] `fruit_names = [x for x in fruits.keys()]`
- [ ] `fruit_names = x for x in fruits.keys()`

#### Q50. What is the algorithmic paradigm of quick sort?

- [ ] `backtracking`
- [x] `divide and conquer`
- [ ] `dynamic programming`
- [ ] `decrease and conquer`

#### Q51. What is the purpose of the `self` keyword when defining or calling methods on an instance of an object?

- [ ] `self` refers to the class that was inherited from to create the object using `self`.
- [ ] There is no real purpose for the `self` method. It's just legacy computer science jargon that Python keeps to stay consistent with other programming languages.
- [ ] `self` means that no other arguments are required to be passed into the method.
- [x] `self` refers to the instance whose method was called.

#### Q52. What is a class method?

- [ ] `A class method is a regular function that belongs to a class, but it must return None.`
- [x] `Class methods can modify the state of the class, but they can't directly modify the state of an instance that inherits from that class.`
- [ ] `A class method is similar to a regular function, but a class method doesn't take any arguments.`
- [ ] `Class methods hold all of the data for a particular class.`

#### Q53. What does it mean for a function to have linear runtime?

- [ ] You did not use very many advanced computer programming concepts in your code.
- [ ] The difficulty level your code is written at is not that high.
- [ ] It will take your program less than half a second to run.
- [x] The amount of time it takes the function to complete grows linearly as the input size increases.

#### Q54. What is the proper way to define a function?

- [ ] `def getMaxNum(list_of_nums): # body of function goes here`
- [ ] `func get_max_num(list_of_nums): # body of function goes here`
- [ ] `func getMaxNum(list_of_nums): # body of function goes here`
- [x] `def get_max_num(list_of_nums): # body of function goes here` [explanation](https://www.python.org/dev/peps/pep-0008/)

#### Q55. According to the PEP 8 coding style guidelines, how should constant values be named in Python?

- [ ] in camel case without using underscores to separate words -- e.g. `maxValue = 255`
- [ ] in lowercase with underscores to separate words -- e.g. `max_value = 255`
- [x] in all caps with underscores separating words -- e.g. `MAX_VALUE = 255`
- [ ] in mixed case without using underscores to separate words -- e.g. `MaxValue = 255`

#### Q56. Describe the functionality of a deque.

- [ ] A deque adds items to one side and remove items from the other side.
- [ ] A deque adds items to either or both sides, but only removes items from the top.
- [x] A deque adds items at either or both ends, and remove items at either or both ends.
- [ ] A deque adds items only to the top, but remove from either or both sides.

#### Q57. What is the correct syntax for creating a variable that is bound to a set?

- [x] `myset = {0, 'apple', 3.5}`
- [ ] `myset = to_set(0, 'apple', 3.5)`
- [ ] `myset = (0, 'apple', 3.5).to_set()`
- [ ] `myset = (0, 'apple', 3.5).set()`

#### Q58. What is the correct syntax for defining an `__init__()` method that takes no parameters?

- [ ] `-`

```
class __init__(self):
    pass
```

- [ ] `-`

```
def __init__():
    pass
```

- [ ] `-`

```
class __init__():
    pass
```

- [x] `-`

```
def __init__(self):
    pass
```

#### Q59. Which statement about the class methods is true?

- [ ] A class method holds all of the data for a particular class.
- [x] A class method can modify the state of the class, but it cannot directly modify the state of an instance that inherits from that class.
- [ ] A class method is a regular function that belongs to a class, but it must return `None`
- [ ] A class method is similar to a regular function, but a class method does not take any arguments.

#### Q60. Which of the following is TRUE About how numeric data would be organised in a banary Search tree?

- [x] `For any given Node in a binary Search Tree, the child node to the left is less than the value of the given node and the child node to its right is greater than the given node.` (Not Sure)
- [ ] `Binary Search Tree cannot be used to organize and search through numeric data, given the complication that arise with very deep trees`
- [ ] `The top node of the binary search tree would be an arbitray number. All the nodes to the left of the top node need to be less than the top node's number, but they don't need to ordered in any particular way`
- [ ] `The smallest numeric value would go in the top most node. The next highest number would go in its left child node, the the next highest number after that would go in its right child node. This pattern would continue until all numeric values were in their own node`

#### Q61. Why would you use a decorator?

- [ ] `A decorator is similar to a class and should be used if you are doing functional programming instead of object oriented programming.`
- [ ] `A decoratore is a visual indicator to someone reading your code that a portion of your code is critical and should not be changed`
- [x] `You use the decorator to alter the functionality of a function without the without having to modify the functions code`
- [ ] `An import statement is preceded by a decorator, pyhton knows to import the most recent version of whatever package or library is being imported`

#### Q62. When would you use a for loop ?

- [ ] `Only in some situations, as loops are used ony for certaing type of programming `
- [x] `When you need to check every element in an iterable of known length`
- [ ] `When you want to minimize the use of strings in your code `
- [ ] `When you want to run code in one file for a function in another file `

#### Q63. What is the most self-descriptive way to define a function that calculates sales tax on a purches?

- [ ] 
`def tax(my_float):
    '''Calculates the sales tax of a purchase. Takes in a float representing the subtotal ...???`
- [ ]
`def tx(amt):
    '''Gets the tax on an amount.'''`
- [ ]
`def sales_tax(amount):
    '''Calculates the sales tax of a purchase. Takes in a float representing the subtotal ...???`
-[x]
`def calculate_sales_tax(subtotal):
    pass`
