## JavaScript

#### Q1. Which operator returns true if the two compared values are not equal?

- [ ] `<>`
- [ ] `~`
- [ ] `==!`
- [x] `!==`

#### Q2. How is a forEach statement different from a for statement?

- [ ] Only a for statement uses a callback function.
- [x] A for statement is generic, but a forEach statement can be used only with an array.
- [ ] Only a forEach statement lets you specify your own iterator.
- [ ] A forEach statement is generic, but a for statement can be used only with an array.

#### Q3. Review the code below. Which statement calls the addTax function and passes 50 as an argument?

#### Q3. How would you use this function to find out how much tax should be paid on \$50?

```js
function addTax(total) {
  return total * 1.05;
}
```

- [ ] addTax = 50;
- [ ] return addTax 50;
- [x] addTax(50);
- [ ] addTax 50;

#### Q4. Which statement is the correct way to create a variable called rate and assign it the value 100?

- [x] let rate = 100;
- [ ] let 100 = rate;
- [ ] 100 = let rate;
- [ ] rate = 100;

#### Q5. Which statement creates a new object using the Person constructor?

#### Q5. Which statement creates a new Person object called "student"?

- [x] var student = new Person();
- [ ] var student = construct Person;
- [ ] var student = Person();
- [ ] var student = construct Person();

#### Q6. When would the final statement in the code shown be logged to the console?

```js
let modal = document.querySelector('#result');
setTimeout(function(){
    modal.classList.remove('hidden);
}, 10000);
console.log('Results shown');
```

- [ ] after 10 second
- [ ] after results are received from the HTTP request
- [ ] after 10000 seconds
- [x] immediately

#### Q7. When would 'results shown' be logged to the console?

```js
let modal = document.querySelector('#results');
setTimeout(function () {
  modal.classList.remove('hidden');
}, 10000);
```

- [x] immediately
- [ ] after results are received from the HTTP request
- [ ] after 10 second
- [ ] after 10,000 seconds

#### Q8. You've written the code shown to log a set of consecutive values, but it instead results in the value 5, 5, 5, and 5 being logged to the console. Which revised version of the code would result in the value 1, 2, 3 and 4 being logged?

```js
for (var i = 1; i <= 4; i++) {
  setTimeout(function () {
    console.log(i);
  }, i * 10000);
}
```

- [ ]

```javascript
for (var i = 1; i <= 4; i++) {
  (function (i) {
    setTimeout(function () {
      console.log(j);
    }, j * 1000);
  })(j);
}
```

- [ ]

```javascript
while (var i=1; i<=4; i++) {
  setTimeout(function() {
    console.log(i);
    }, i*1000);
}
```

- [x]

```javascript
for (var i = 1; i <= 4; i++) {
  (function (j) {
    setTimeout(function () {
      console.log(j);
    }, j * 1000);
  })(i);
}
```

- [ ]

```javascript
for (var j = 1; j <= 4; j++) {
  setTimeout(function () {
    console.log(j);
  }, j * 1000);
}
```

#### Q9. How does a function create a closure?

- [ ] It reloads the document whenever the value changes.
- [x] It returns a reference to a variable in its parent scope.
- [ ] It completes execution without returning.
- [ ] It copies a local variable to the global scope.

#### Q10. Which statement creates a new function called discountPrice?

- [x]

```js
let discountPrice = function (price) {
  return price * 0.85;
};
```

- [ ]

```js
let discountPrice(price) {
  return price * 0.85;
};
```

- [ ]

```js
let function = discountPrice(price) {
  return price * 0.85;
};
```

- [ ]

```js
discountPrice = function (price) {
  return price * 0.85;
};
```

#### Q11. What is the result in the console of running the code shown?

```js
var Storm = function () {};
Storm.prototype.precip = 'rain';
var WinterStorm = function () {};
WinterStorm.prototype = new Storm();
WinterStorm.prototype.precip = 'snow';
var bob = new WinterStorm();
console.log(bob.precip);
```

- [ ] Storm()
- [ ] undefined
- [ ] 'rain'
- [x] 'snow'

#### Q12. You need to match a time value such as 12:00:32. Which of the following regular expressions would work for your code?

- [ ] /[0-9]{2,}:[0-9]{2,}:[0-9]{2,}/
- [ ] /\d\d:\d\d:\d\d/
- [ ] /[0-9]+:[0-9]+:[0-9]+/
- [ ] / : : /

NOTE: the first three expressions will all match. Question seem to be incorrect.

#### Q13. What is the result in the console of running this code?

```js
'use strict';
function logThis() {
  this.desc = 'logger';
  console.log(this);
}
new logThis();
```

- [ ] undefined
- [ ] window
- [x] {desc: "logger"}
- [ ] function

#### Q14. How would you reference the text 'avenue' in the code shown?

```js
let roadTypes = ['street', 'road', 'avenue', 'circle'];
```

- [ ] roadTypes.2
- [ ] roadTypes\[3\]
- [ ] roadTypes.3
- [x] roadTypes\[2\]

#### Q15. What is the result of running this statement?

```javascript
console.log(typeof 42);
```

- [ ] 'float'
- [ ] 'value'
- [x] 'number'
- [ ] 'integer'

#### Q16. Which property references the DOM object that dispatched an event?

- [ ] self
- [ ] object
- [x] target
- [ ] source

#### Q17. You're adding error handling to the code shown. Which code would you include within the if statement to specify an error message?

```js
function addNumbers(x, y) {
  if (isNaN(x) || isNaN(y)) {
  }
}
```

- [ ] exception('One or both parameters are not numbers')
- [ ] catch('One or both parameters are not numbers')
- [ ] error('One or both parameters are not numbers')
- [x] throw('One or both parameters are not numbers')

#### Q18. Which method converts JSON data to a JavaScript object?

- [ ] JSON.fromString();
- [x] JSON.parse()
- [ ] JSON.toObject()
- [ ] JSON.stringify()

#### Q19. When would you use a conditional statement?

- [ ] When you want to reuse a set of statements multiple times.
- [x] When you want your code to choose between multiple options.
- [ ] When you want to group data together.
- [ ] When you want to loop through a group of statement.

#### Q20. What would be the result in the console of running this code?

```js
for (var i = 0; i < 5; i++) {
  console.log(i);
}
```

- [ ] 12345
- [ ] 1234
- [x] 01234
- [ ] 012345

#### Q21. Which Object method returns an iterable that can be used to iterate over the properties of an object?

- [ ] Object.get()
- [ ] Object.loop()
- [ ] Object.each()
- [x] Object.keys()

#### Q22. What will be logged to the console?

```js
var a = ['dog', 'cat', 'hen'];
a[100] = 'fox';
console.log(a.length);
```

- [x] 101
- [ ] 3
- [ ] 4
- [ ] 100

#### Q23. What is one difference between collections created with Map and collections created with Object?

- [ ] You can iterate over values in a Map in their insertion order.
- [x] You can count the records in a Map with a single method call.
- [ ] Keys in Maps can be strings.
- [ ] You can access values in a Map without iterating over the whole collection.

**Explanation:** `Map.prototype.size returns the number of elements in a Map, whereas Object does not have a built-in method to return its size.`

#### Q24. What is the value of dessert.type after executing this code?

```js
const dessert = { type: 'pie' };
dessert.type = 'pudding';
```

- [ ] pie
- [ ] The code will throw an error.
- [x] pudding
- [ ] undefined

#### Q25. 0 && hi

- [ ] ReferenceError
- [ ] True
- [x] 0
- [ ] false

#### Q26. Which of the following operators can be used to do a short-circuit evaluation?

- [ ] \++
- [ ] \--
- [ ] \==
- [x] \|\|

#### Q27. Which statement sets the Person constructor as the parent of the Student constructor in the prototype chain?

- [ ] Student.parent = Person;
- [x] Student.prototype = new Person();
- [ ] Student.prototype = Person;
- [ ] Student.prototype = Person();

#### Q28. Why would you include a "use strict" statement in a JavaScript file?

- [ ] to tell parsers to interpret your JavaScript syntax loosely
- [x] to tell parsers to enforce all JavaScript syntax rules when processing your code
- [ ] to instruct the browser to automatically fix any errors it finds in the code
- [ ] to enable ES6 features in your code

#### Q29. Which Variable-defining keyword allows its variable to be accessed (as undefined) before the line that defines it?

- [ ] all of them
- [ ] const
- [x] var
- [ ] let

#### Q30. Which of the following values is not a Boolean false?

- [ ] Boolean(0)
- [ ] Boolean("")
- [ ] Boolean(NaN)
- [x] Boolean("false")

#### Q31. Which of the following is not a keyword in JavaScript?

- [ ] this
- [ ] catch
- [ ] function
- [x] array

#### Q32. Which variable is an implicit parameter for every function in JavaScript?

- [x] Arguments
- [ ] args
- [ ] argsArray
- [ ] argumentsList

#### Q33. For the following class, how do you get the value of 42 from an instance of X?

```js
class X {
  get Y() {
    return 42;
  }
}
```

- [ ] x.get('Y')
- [x] x.Y
- [ ] x.Y()
- [ ] x.get().Y

#### Q34. What is the result of running this code?

```js
sum(10, 20);
diff(10, 20);
function sum(x, y) {
  return x + y;
}

let diff = function (x, y) {
  return x - y;
};
```

- [ ] 30, ReferenceError, 30, -10
- [x] 30, ReferenceError
- [ ] 30, -10
- [ ] ReferenceError, -10

#### Q35. Why is it usually better to work with Objects instead of Arrays to store a collection of records?

- [ ] Objects are more efficient in terms of storage.
- [ ] Adding a record to an object is significantly faster than pushing a record into an array.
- [x] Most operations involve looking up a record, and objects can do that better than arrays.
- [ ] Working with objects makes the code more readable.

**Explanation:** Records in an object can be retrieved using their key which can be any given value (e.g. an employee ID, a city name, etc), whereas to retrieve a record from an array we need to know its index.

#### Q36. Which statement is true about the "async" attribute for the HTML script tag?

- [ ] It can be used for both internal and external JavaScript code.
- [ ] It can be used only for internal JavaScript code.
- [ ] It can be used only for internal or external JavaScript code that exports a promise.
- [x] It can be used only for external JavaScript code.

#### Q37. How do you import the lodash library making it top-level Api available as the "\_" variable?

- [x] import \_ from 'lodash';
- [ ] import 'lodash' as \_;
- [ ] import '\_' from 'lodash;
- [ ] import lodash as \_ from 'lodash';

#### Q38. What does the following expression evaluate to?

```js
[] == [];
```

- [ ] True
- [ ] undefined
- [ ] []
- [x] False

#### Q39. What is the name of a function whose execution can be suspended and resumed at a later point?

- [x] Generator function
- [ ] Arrow function
- [ ] Async/ Await function
- [ ] Promise function

#### Q40. What will this code print?

```js
var v = 1;
var f1 = function () {
  console.log(v);
};

var f2 = function () {
  var v = 2;
  f1();
};

f2();
```

- [ ] 2
- [x] 1
- [ ] Nothing - this code will throw an error.
- [ ] undefined

#### Q41. Which statement is true about Functional Programming?

- [ ] Every object in the program has to be a function.
- [ ] Code is grouped with the state it modifies.
- [ ] Date fields and methods are kept in units.
- [x] Side effects are not allowed.

#### Q42. Your code is producing the error: TypeError: Cannot read property 'reduce' of undefined. What does that mean?

- [x] You are calling a method named reduce on an object that's declared but has no value.
- [ ] You are calling a method named reduce on an object that does not exist.
- [ ] You are calling a method named reduce on an empty array.
- [ ] You are calling a method named reduce on an object that's has a null value.

**Explanation**: `You cannot invoke reduce on undefined object... It will throw (yourObject is not Defined...)`

#### Q43. How many prototype objects are in the chain for the following array?

`let arr = [];`

- [ ] 3
- [x] 2
- [ ] 0
- [ ] 1

#### Q44. Which choice is _not_ a unary operator?

- [ ] typeof
- [ ] delete
- [x] instanceof
- [ ] void

#### Q45. What type of scope does the end variable have in the code shown?

```javascript
var start = 1;
if (start === 1) {
  let end = 2;
}
```

- [ ] conditional
- [x] block
- [ ] global
- [ ] function

#### Q46. What will the value of y be in this code:

```js
const x = 6 % 2;
const y = x ? 'One' : 'Two';
```

- [ ] One
- [ ] undefined
- [ ] TRUE
- [x] Two

#### Q47. Which keyword is used to create an error?

- [x] throw
- [ ] exception
- [ ] catch
- [ ] error

#### Q48. What's one difference between the async and defer attributes of the HTML script tag?

- [ ] The defer attribute can work synchronously.
- [ ] The defer attribute works only with generators.
- [ ] The defer attribute works only with promises.
- [x] The defer attribute will asynchronously load the scripts in order.

#### Q49. The following program has a problem. What is it?

```js
var a;
var b = (a = 3) ? true : false;
```

- [x] The condition in the ternary is using the assignment operator.
- [ ] You can't define a variable without initializing it.
- [ ] You can't use a ternary in the right-hand side of an assignment operator.
- [ ] The code is using the deprecated var keyword.

#### Q50. Which statement references the DOM node created by the code shown?

```html
<p class="pull">lorem ipsum</p>
```

- [ ] `Document.querySelector('class.pull')`
- [x] `document.querySelector('.pull');`
- [ ] `Document.querySelector('pull')`
- [ ] `Document.querySelector('#pull')`

#### Q51. What value does this code return?

```js
let answer = true;
if (answer === false) {
  return 0;
} else {
  return 10;
}
```

- [x] 10
- [ ] true
- [ ] false
- [ ] 0

#### Q52. What is the result in the console of running the code shown?

```js
var start = 1;
function setEnd() {
  var end = 10;
}
setEnd();
console.log(end);
```

- [ ] 10
- [ ] 0
- [x] ReferenceError
- [ ] undefined

#### Q53. What will this code log in the console?

```js
function sayHello() {
  console.log('hello');
}

console.log(sayHello.prototype);
```

- [ ] undefined
- [ ] "hello"
- [x] an object with a constructor property
- [ ] an error message

#### Q54. Which collection object allows unique value to be inserted only once?

- [ ] Object
- [x] Set
- [ ] Array
- [ ] Map

#### Q55. What two values will this code print?

```js
function printA() {
  console.log(answer);
  var answer = 1;
}
printA();
printA();
```

- [ ] `1` then `1`
- [ ] `1` then `undefined`
- [x] `undefined` then `undefined`
- [ ] `undefined` then `1`

#### Q56. How does the `forEach()` method differ from a `for` statement?

- [ ] forEach allows you to specify your own iterator, whereas for does not.
- [ ] forEach can be used only with strings, whereas for can be used with additional data types.
- [x] forEach can be used only with an array, whereas for can be used with additional data types.
- [ ] for loops can be nested; whereas forEach loops cannot.

#### Q57. What will be logged to the console?

```javascript
'use strict';
function logThis() {
  this.desc = 'logger';
  console.log(this);
}
new logThis();
```

- [ ] undefined
- [ ] function
- [ ] windows
- [x] {desc: "logger"}

#### Q58. Which choice is an incorrect way to define an arrow function that returns an empty object?

- [ ] => ({})
- [x] => {}
- [ ] => { return {};}
- [ ] => (({}))

#### Q59. Why might you choose to make your code asynchronous?

- [x] to start tasks that might take some time without blocking subsequent tasks from executing immediately
- [ ] to ensure that tasks further down in your code are not initiated until earlier tasks have completed
- [ ] to make your code faster
- [ ] to ensure that the call stack maintains a LIFO (Last in, First Out) structure

**EXPLANATION:** "to ensure that tasks further down in your code are not initiated until earlier tasks have completed" you use the normal (synchronous) flow where each command is executed sequentially. Asynchronous code allows you to break this sequence: start a long running function (AJAX call to an external service) and continue running the rest of the code in parallel.

#### Q60. Which expression evaluates to true?

- [ ] `[3] == [3]`
- [x] `3 == '3'`
- [ ] `3 != '3'`
- [ ] `3 === '3'`

#### Q61. Which of these is a valid variable name?

- [ ] 5thItem
- [x] firstName
- [ ] grand total
- [ ] function

#### Q62. Which method cancels event default behavior?

- [ ] cancel()
- [ ] stop()
- [x] preventDefault()
- [ ] prevent()

#### Q63. Which method do you use to attach one DOM node to another?

- [ ] attachNode()
- [ ] getNode()
- [ ] querySelector()
- [x] appendChild()

#### Q64. Which statement is used to skip iteration of the loop?

- [ ] break
- [ ] pass
- [ ] skip
- [x] continue

#### Q65. Which choice is valid example for an arrow function?

- [x] (a,b) => c
- [ ] a, b => {return c;}
- [ ] a, b => c
- [ ] { a, b } => c

#### Q66. Which concept is defined as a template that can be used to generate different objects that share some shape and/or behavior?

- [x] class
- [ ] generator function
- [ ] map
- [ ] proxy

#### Q67. How do you add a comment to JavaScript code?

- [ ] `! This is a comment`
- [ ] `# This is a comment`
- [ ] `\\ This is a comment`
- [x] `// This is a comment`

#### Q68. If you attempt to call a value as a function but the value is not a function, what kind of error would you get?

- [x] TypeError
- [ ] SystemError
- [ ] SyntaxError
- [ ] LogicError

#### Q69. Which method is called automatically when an object is initialized?

- [ ] create()
- [ ] new()
- [x] constructor()
- [ ] init()

#### Q70. What is the result of running the statement shown?

```javascript
let a = 5;
console.log(++a);
```

- [ ] 4
- [ ] 10
- [x] 6
- [ ] 5

#### Q71. You've written the event listener shown below for a form button, but each time you click the button, the page reloads. Which statement would stop this from happening?

```javascript
button.addEventListener(
  'click',
  function (e) {
    button.className = 'clicked';
  },
  false,
);
```

- [ ] e.blockReload();
- [ ] button.preventDefault();
- [ ] button.blockReload();
- [x] e.preventDefault();

#### Q72. Which statement represents the starting code converted to an IIFE?

- [ ] `function() { console.log('lorem ipsum'); }()();`
- [ ] `function() { console.log('lorem ipsum'); }();`
- [x] `(function() { console.log('lorem ipsum'); })();`

#### Q73. Which statement selects all img elements in the DOM tree?

- [ ] `Document.querySelector('img')`
- [ ] `Document.querySelectorAll('<img>')`
- [x] `Document.querySelectorAll('img')`
- [ ] `Document.querySelector('<img>')`

#### Q74. Why would you choose an asynchronous structure for your code?

- [ ] To use ES6 syntax
- [x] To start tasks that might take some time without blocking subsequent tasks from executing immediately
- [ ] To ensure that parsers enforce all JavaScript syntax rules when processing your code
- [ ] To ensure that tasks further down in your code aren't initiated until earlier tasks have completed

#### Q75. What is the HTTP verb to request the contents of an existing resource?

- [ ] DELETE
- [x] GET
- [ ] PATCH
- [ ] POST

#### Q76. Which event is fired on a text field within a form when a user tabs to it, or clicks or touches it?

- [x] focus
- [ ] blur
- [ ] hover
- [ ] enter

#### Q77. What is the result in the console of running this code?

```javascript
function logThis() {
  console.log(this);
}
logThis();
```

- [ ] function
- [ ] undefined
- [ ] Function.prototype
- [x] window

#### Q78. Which class-based component is equivalent to this function component?

```javascript
const Greeting = ({ name }) => <h1>Hello {name}!</h1>;
```

- [x] `class Greeting extends React.Component { render() { return <h1>Hello {this.props.name}!</h1>; } }`
- [ ] `class Greeting extends React.Component { constructor() { return <h1>Hello {this.props.name}!</h1>; } }`
- [ ] `class Greeting extends React.Component { <h>Hello {this.props.name}!</h>; } }`
- [ ] `class Greeting extends React.Component { render({ name }) { return <h1>Hello {name}!</h1>; } }`

#### Q79. Which class-based lifecycle method would be called at the same time as this effect Hook?

```javascript
useEffect(() => {
  // do things
}, []);
```

- [ ] componentWillUnmount
- [ ] componentDidUpdate
- [ ] render
- [x] componentDidMount

#### Q80. What is the output of this code?

```javascript
var obj;
console.log(obj);
```

- [ ] ReferenceError: obj is not defined
- [ ] {}
- [x] undefined
- [ ] null

#### Q81. How would you use the TaxCalculator to determine the amount of tax on \$50?

```javascript
class TaxCalculator {
  static calculate(total) {
    return total * 0.05;
  }
}
```

- [ ] calculate(50);
- [ ] new TaxCalculator().calculate(\$50);
- [x] TaxCalculator.calculate(50);
- [ ] new TaxCalculator().calculate(50);
