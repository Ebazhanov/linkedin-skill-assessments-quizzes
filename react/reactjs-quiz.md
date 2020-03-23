React.js Assessment
-----------------

#### Q1. If you want to import just the Component from the React library, what syntax do you use?
- `import React.Component from 'react'` 
- `import [ Component ] from 'react'`
- `import Component from 'react'`
- `import { Component } from 'react'` <<<<<--CORRECT

#### Q2. If a function component should always render the same way given the same props, what is a simple performance optimization available for it?
- Wrap it in the React.memo higher-order component. <<<<<--CORRECT
- Implement the useReducer Hook.
- Implement the useMemo Hook.
- Implement the shouldComponentUpdate lifecycle method.

#### Q3. How do you fix the syntax error that results from running this code?
```javascript
const person =(firstName, lastName) => 
       {
            first: firstName,
            last: lastName        
        }    
console.log(person("Jill", "Wolson"))
```
- Wrap the object in parentheses. <<<<<--CORRECT
- Call the function from another file.
- Add a return statement before the first curly brace.
- Replace the with an array

#### Q4. If you see the following import in a file, what is being used for state management in the component?
`import React, {useState} from 'react';`
- React Hooks <<<<<--CORRECT
- stateful components 
- math 
- class components

#### Q5. Using object literal enhancement, you can put values back into and object. When you log person to the console, what is the output?
```javascript
const name = "Rachel";
const age = 31;
const person = {name, age }
console.log(person)
```
- `{{name: "Rachel", age: 31}}`
- `{name: "Rachel", age: 31}` <<<<<--CORRECT
- `{person: "Rachel", person: 31}}`
- `{person: {name: "Rachel", age: 31}}`

#### Q6. What is the testing library most often associated with React?
- Mocha
- Chai
- Sinon
- Jest <<<<<--CORRECT

#### Q7. To get the first item from the array ("cooking") using array destructuring, how do you adjust this line?
```javascript
const topics = ["cooking", "art", "history"]
``` 
- `const first = ["cooking", "art", "history"]`
- `const [] = ["cooking", "art", "history"]`
- `const [, first]["cooking", "art", "history"]`
- `const [first] = ["cooking", "art", "history"]` <<<<<--CORRECT

#### Q8. How do you handle passing through the component tree without having to pass props down manually at every level?
- React Send
- React Pinpoint 
- React Router
- React Context <<<<<--CORRECT

#### Q9. What should the console read when the following code is run?
```javascript
const [, , animal] = ["Horse", "Mouse", "Cat"]
console.log(animal)
```
- Horse
- Cat <<<<<--CORRECT
- Mouse
- undefined

#### 10. What is the name of the tool used to take JSX and turn it into createElement calls?
- JSX Editor
- ReactDOM
- Browser Buddy
- Babel <<<<<--CORRECT

#### 11. Why might you use useReducer over useState in a React component?
- when you want to replace Redux
- when you need to manage more complex state in an app <<<<<--CORRECT
- when you want to improve performance 
- when you want to break your production app

#### 12. Which props from the props object is available to the component with the following syntax?
```javascript
<Message {...props}/>
```
- any that have not changed 
- all of them <<<<<--CORRECT
- child props
- any that have changed

#### 13. Consider the following code from React Router. What do you call :id in the path prop?
```javascript
<Route path="/:id" />
```
- This is a route modal
- This is a route parameter <<<<<--CORRECT
- This is a route splitter
- This is a route link

#### 14. If you created a component called Dish and rendered it to the DOM, what type of element would be rendered?
```javascript
function Dish() {
  return <h1> Mac and Cheese</h1>;
}

ReactDOM.render(
    <Dish />,
    document.getElementById('root')
)
```
- div
- section
- component
- h1 <<<<<--CORRECT

#### 15. What does this React element look like given the following function?
```javascript
React.createElement(
    "h1",
    null,
    "What's happening?"
);
```
- `<h1 props={null}>What's happenning?</h1>`
- `<h1>What's happening?</h1>` <<<<<--CORRECT
- `<h1 id="component">What's happening?</h1>`
- `<h1 id="element">What's happening?</h1>`

#### 16. What property do you need to add the Suspense component in order to display a spinner or loading state?
```javascript
function MyComponent() {
  return (
    <Suspense>
        <div>
            <Message />
        </div>
    </Suspense>
    );   
}
```
- lazy
- loading
- fallback <<<<<--CORRECT
- spinner

#### 17. What do you call the message wrapped in curly braces below?
```javascript
let message = "Hi there";
const element = <p>{message}</p>
```
- a JS function
- a JS element
- a JS expression <<<<<--CORRECT
- a JSX wrapper

#### 18. What can you use to handle code splitting?
- `React.memo`
- `React.split`
- `React.lazy` <<<<<--CORRECT
- `React.fallback`

#### 19. When do you use useLayoutEffect?
- to optimize for all devices
- to complete the update 
- to change the layout of the screen
- when you need the browser to paint before the effect runs <<<<<--CORRECT

#### 20. What is the difference between the click behaviors of these two buttons (assuming that this.handleClick is binded correctly)?
```javascript
A. <button onClick="{this.handleClick}>Click Me</button>"
B. <button onClick="{event => this.handleClick()event}}>Click Me</button>"
```
- Button A will not have access to the event object on click of the button.
- Button B will not fire the handler this.handleClick successfully. <<<<<--CORRECT
- Button A will not fire the handler this.handleClick successfully.
- There is no difference

#### 21. How do you destructure the properties that are sent to the Dish component?
```javascript
function Dish(props) {
   return <h1>{props.name} {props.cookingTime}</h1>
}
```
- `function Dish([name, cookingTime]) {
    return <h1>{name} {cookingTime}</h1>;
}`
- `function Dish({name, cookingTime}) {
    return <h1>{name} {cookingTime}</h1>; 
}` <<<<<--CORRECT

- `function Dish(props) {
    return <h1>{name} {cookingTime}</h1>;
}`
- `function Dish(...props) {
    return <h1>{name} {cookingTime}</h1>;
}`

#### 22. When might you use React.PureComponent?
- when you do not want your component to have props
- when you have sibling components that need to be compared
- when you want to implement shouldComponentUpdate() by default to not update unnecessarily <<<<<--CORRECT
- when you do not want your component to have state

#### 23. Why is it important to avoid copying the values of props into a component's state where possible?
- because you should never mutate state
- because getDerivedStateFromProps() is an unsafe method to use
- because you want to allow a component to update in response to changes in the props <<<<<--CORRECT
- because you want to allow data to flow back up to the parent

#### 24. What is the children prop?
- a property that adds child components to state
- a property that lets you pass components as data to other components <<<<<--CORRECT
- a property that lets you set an array as a property
- a property that lets you pass data to child elements

