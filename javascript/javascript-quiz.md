JavaScript Assessment
---------------------

#### Q1. Which operator returns true if the two compared values are not equal?
- <>
- ~
- ==! 
- !== <<<---Correct

#### Q2. How is a forEach statement different from a for statement?
- Only a for statement uses a callback function
- A for statement is generic, but a forEach statement can be used only with an array <<<--Correct
- Only a forEach statement lets you specify your own iterator.
- A forEach statement is generic, but a for statement ca be used only with an array

#### Q3. Review the code below. Which statement calls the addTax function and passes 50 as an argument?
```js
function addTax(total){
    return total * 1.05;
}
```
- addTax = 50;
- return addTax 50;
- addTax(50); <<<---Correct
- addTax 50;

#### Q4. Which statement is the correct way to create a variable called rate and assign it the value 100?
- let rate = 100; <<<---Correct
- let 100 = rate;
- 100 = let rate;
- rate = 100;

#### Q5. Which statement creates a new object using the Person constructor?
- var student = new Person(); <<<---Correct
- var student = construct Person;
- var student = Person();
- var student = construct Person();

#### Q6. When would the final statement in the code shown be logged to the console?
```js
let modal = document.querySelector('#result');
setTimeout(function(){
    modal.classList.remove('hidden);
}, 10000);
console.log('Results shown');
```
- after 10 second 
- after results are received from the HTTP request
- after 10000 seconds
- immediately <<<<<----Correct

#### Q7. You've written the code shown to log a set of consecutive values, but it instead results in the value 5, 5, 5, and 5 being logged to the console. Which revised version of the code would result in the value 1, 2, 3 and 4 being logged?
- ```for (var i=1; i<=4; i++){
    setTimeout(function(){
        console.log(i);
    }, i*10000);
   }`
   
- `for (var i=1; i<=4; i++){
       (function(i){
          setTimeout(function(){
            console.log(j);
          }, j*1000);
       })(j)
   }`
   
- `while (var i=1; i<=4; i++) {
    setTimeout(function() {
        console.log(i);
    }, i*1000);
   }`
   
- `for (var i=1; i<=4; i++) {
      {function(j) {
         setTimeout(function(){
           console.log(j);
         }, j*1000);
      })(i)
    }` // Correct
    
- `for (var j=1; j<=4; j++) {
     setTimeout(function() {
       console.log(j);
     }, j*1000);
   }` 
   
#### Q8. How does a function create a closure?
- It reloads the document whenever the value changes.
- It returns a reference to a variable in its parent scope <<<<---Correct
- It completes execution without returning
- It copies a local variable to the global scope

#### Q9. Which statement creates a new function called discountPrice?
- `let discountPrice = function(price) {
     return price * 0.85;
    };` <<<<----Correct

- `let discountPrice(price) {
     return price * 0.85;
    };`
    
- `let function = discountPrice(price) {
     return price * 0.85;
    };`
    
- `discountPrice = function(price) {
        return price * 0.85;
       };`
       
#### 10. What is the result in the console of running the code shown?
```js
var Storm = function() {};
Storm.prototype.precip = 'rain';
var WinterStorm = function() {};
WinterStorm.prototype = new Storm();
WinterStorm.prototype.precip = 'snow'; 
var bob = new WinterStorm();
console.log(bob.precip);
```
- Storm()
- undefined
- 'rain'
- 'snow' <<<---Correct

#### Q11. You need to match a time value such as 12:00:32. Which of the following regular expressions would work for your code?
- /[0-9]{2,}:[0-9]{2,}:[0-9]{2,}/
- /\d\d:\d\d:\d\d/ <<<---Correct, https://regex101.com/r/6e81up/2
- /[0-9]+:[0-9]+:[0-9]+/ 
- /  : : /
   
#### Q12. What is the result in the console of running this code?
```js
"use strict";
function logThis() {
    this.desc = "logger";
    console.log(this);
}
new logThis();
```
- undefined
- window
- {desc: "logger"} <<<<---Correct
- function

#### Q13. How would you reference the text 'avenue' in the code shown?
```js
let roadTypes = ['street', 'road', 'avenue', 'circle'];
```
- roadTypes.2
- roadTypes[3]
- roadTypes.3
- roadTypes[2] <<<---Correct

#### Q14. What is the result of running this statement?
`console.log(typeof(42));`
- 'float'
- 'value'
- 'number' <<<---Correct
- 'integer'

#### Q15. Which property references the DOM object that dispatched an event?
- self
- object
- target <<<---Correct
- source

#### Q16. You're adding error handling to the code shown. Which code would you include within the if statement to specify an error message?
```js
function addNumbers(x, y){
    if (isNaN(x) || isNaN(y)) {
    }
}
```
- exception('One or both parameters are not numbers')
- catch('One or both parameters are not numbers')
- error('One or both parameters are not numbers')
- throw('One or both parameters are not numbers') <<<<---Correct

#### Q17. Which method converts JSON data to a JavaScript object?
- JSON.fromString();
- JSON.parse() <<<<---Correct
- JSON.toObject()
- JSON.stringify()

#### Q18. When would you use a conditional statement?
- When you want to reuse a set of statements multiple times.
- When you want your code to choose between multiple options <<<---Correct
- When you want to group data together
- When you want to loop through a group of statement.

#### Q19. What would be the result in the console of running this code?
```js
for (var i=0; i<5; i++){
    console.log(i);
}
```
- 12345
- 1234
- 01234 <<<<---Correct
- 012345

#### Q20. Which Object method returns an iterable that can be used to iterate over the properties of an object?
- Object.get()
- Object.loop()
- Object.each()
- Object.keys() <<<<----Correct 

#### Q21. After the following code, what is the value of a.length?
```js
var a = ['dog','cat','hen'];
a[100] = 'fox';
```
- 101 <<<<----Correct
- 3
- 4
- 100

#### Q22. What is one difference between collections created with Map and collections created with Object?
- You can iterate over values in a Map in their insertion order. (Correct. Map.prototype.forEach(callbackFn[, thisArg]))
- You can count the records in a Map with a single method call. (Correct. Map.prototype.size)
- Keys in Maps can be strings. (Correct)
- You can access values in a Map without iterating over the whole collection. (Correct. Map.prototype.get(key))

#### Q23. Which property references the DOM object that dispatched an event?
- source
- object
- target <<<<----Correct 
- self

#### Q24. What is the value of dessert.type after executing this code?
```js
const dessert = { type: 'pie' };
dessert.type = 'pudding';
```
- pie
- The code will throw an error.
- pudding <<<<------- Correct 
- undefined

#### Q25. 0 && hi
- ReferenceError
- True
- 0 <<<<------- Correct 
- false

#### Q26. Which of the following operators can be used to do a short-circuit evaluation?
- \++
- \--
- \==
- || <<<<-------Correct 

#### Q27. Which statement sets the Person constructor as the parent of the Student constructor in the prototype chain?
- Student.parent = Person;
- Student.prototype = new Person(); <<<<----Correct
- Student.prototype = Person;
- Student.prototype = Person();

#### Q28. Why would you include a "use strict" statement in a JavaScript file?
- to tell parsers to interpret your JavaScript syntax loosely
- to tell parsers to enforce all JavaScript syntax rules when processing your code <<<<----Correct
- to instruct the browser to authmatically fix any errors it finds in the code
- to enable ES6 features in your code

#### Q29. Which Variable-defining keyword allows its variable to be accessed (as undefined) before the line that defines it?
- all of them
- const
- var <<<<----Correct
- let

#### Q30. Which of the following values is not a Boolean false?
- Boolean(0)
- Boolean("")
- Boolean(NaN)
- Boolean("false") <<<<------Correct 

#### Q31. Which of the following is not a keyword in JavaScript?
- this
- catch 
- function
- array <<<<------Correct

#### Q32. When would you use conditional statement?
- When you want to loop through a group of statements.
- When you want your code to choose between multiple options. <<<<----Correct
- When you want to reuse a set of statements multiple times.
- When you want to group data together.

#### Q33. Which variable is an implicit parameter for every function in JavaScript?
- Arguments <<<<----Correct
- args
- argsArray
- argumentsList

#### Q34. For the following class, how do you get the value of 42 fro ma instance of X?
```js
class X {
    get Y() { return 42; }
}
```
- x.get('Y')
- x.Y <<<<-----Correct
- x.Y()
- x.get().Y

#### Q35. What is the result of running this code?
```js
sum(10,20);
diff(10,20);
function sum(x,y){
    return x+y;
}

let diff = function(x,y){
    return x-y
}
```
- 30, RefferanceError, 30, -10
- 30, ReferanceError  <<<<----Correct
- 30, -10
- ReferanceError, -10

#### Q36. Why is it usually better to work with Objects instead of Arrays to store a collection of records?
- Objects are more efficent in terms of storeage.
- Adding a record to an object is significantly faster than pushing a record into an array. <<<<----Correct
- Most operations involve looking up a record, and objects can do that better than arrays.
- Working with objects makes the code more readable.

#### Q37. Which statement is true about the "async" attribute for the HTML script tag?
- It can be used for both internal and external JavaScript code.
- It can be used only for internal JavaScript code. <<<<----Correct
- It can be used only for internal or external JavaScript code that exports a promise.
- It can be used only for external JavaScript code.

#### Q38. How do you import the lodash library making it top-level Api available as the "_" variable?
- import _ from 'lodash'; <<<<----Correct
- import 'lodash' as _;
- import '_' from 'lodash;
- import lodash as _ from 'lodash';

#### Q39. What does the following expression evaluate to?
```js
[] == []
```
- True
- undefined
- []
- False <<<<----Correct

#### Q40. What is the name of a function whose expecution can be suspended and resumed at a later point? 
- Generator function
- Arrow function 
- Async/ Await function <<<<----Correct
- Promise function

#### Q41. What will this code print?
```js
var v = 1
var f1 = function(){
    console.log(v)
}

var f2 = function(){
    var v = 2;
    f1()
}

f2()
```
- 2
- 1 <<<<----Correct
- Nothing--this code will throw an error.
- undefined 

#### Q42. Which statement is true about Functional Programming?
- Every object in the program has to be a function.
- Code is grouped with the state it modifies.
- Date fields and methods are kept in units.
- Side effecs are not allowed. <<<<<----- I believe it's this, FP shouldn't have side effects; i.e same output evry time, doesn't mutate 

#### Q43. Your code is producing the error: TypeError: Cannot read property 'reduce' of undefined. What does that mean?
- You are calling a method named reduce on an object that's declared but has no value.
- You are calling a method named reduce on an object that does not exist. <<<<----Correct
- You are calling a method named reduce on an empty array.
- You are calling a method named reduce on an object that's has a null value.

#### Q44. How many prototype objects are in the chain for the following array?
`let arr = [];`
- 3
- 2
- 0 <<<<----Correct
- 1

#### Q45. Which of the following is not a unary operator?
- typeof
- delete
- instanceof  <<<<----Correct
- void

#### Q46. What type of scope does the end variable have in the code shown? 
```
var start = 1;
if (start === 1) {
 let end = 2;
}
```
- conditional
- block
- global   <<<<----Correct
- function


#### Q47. What will the value of y be in this code: 
```
const x = 6 % 2;
const y = x ? 'One': 'Two';
```
- One
- undefined
- TRUE
- Two  <<<<----Correct


### Q48. Which keyword is used to create an error?
- throw   <<<<----Correct
- exception
- catch
- error


### Q49. What's one difference between the async and defer attributes of the HTML script tag?
- The defer attribute can work synchronously.
- The defer attribute works only with generators.
- The defer attribute works only with promises.
- The defer attribute will asynchronously load the scripts in order.   <<<<----Correct


### Q50. The following program has a problem. What is it?
```js
var a;
var b = (a = 3) ? true: false
```
- The condition in the ternary is using the assignment operator.   <<<<----Correct
- You can't define a variable without initializing it.
- You can't use a ternary in the right-hand side of an assignment operator.
- The code is using the deprecated var keyword


### Q51. Which statement references the DOM node created by the code shown?
```html
<p class="pull">lorem ipsum</p>
```
- `Document.querySelector('class.pull')`
- `document.querySelector('.pull');`   <<<<----Correct
- `Document.querySelector('pull')`
- `Document.querySelector('#pull')`
