- [ ] render(props);
- [x] super(props);
- [ ] super(this);
- [ ] this.super();

#### Q96. Which language can you not use with React?

- [x] Swift.
- [ ] JSX.
- [ ] Javascipt.
- [ ] TypeScript.

#### Q97. This code is part of an app that collects Pokemon. How would you print the list of the ones collected so far?

```javascript
constructor(props) {
    super(props);
    this.state = {
        pokeDex: []
    };
}
```

- [ ] console.log(props.pokeDex);
- [ ] console.log(this.props.pokeDex);
- [ ] console.log(pokeDex);
- [x] console.log(this.state.pokeDex);

[Reference](https://www.digitalocean.com/community/tutorials/how-to-manage-state-on-react-class-components#step-3-setting-state-from-a-static-value)

#### Q98. What would be the result of running this code?

```javascript
function add(x = 1, y = 2) {
  return x + y;
}

add();
```

- [ ] null
- [x] 3
- [ ] 0
- [ ] undefined

![image](https://user-images.githubusercontent.com/62549240/160531605-bf8790d5-5eb9-4291-a9bd-4232f2fd7b6e.png?raw=png)

Explanation: function that called without parameter will use its param default value, thus x will always be default to 1 and y will always be default to 2.

#### Q99. Why might you use a React.ref?

- [ ] to refer to another JS file
- [ ] to bind the function
- [ ] to call a function
- [x] to directly access the DOM node

[Reference](https://reactjs.org/docs/refs-and-the-dom.html)

#### Q100. What pattern is being used in this code block?

```javascript
const { tree, lake } = nature;
```

- [ ] function defaults
- [ ] array destructuring
- [ ] PRPL pattern
- [x] destructuring assignment

[Reference](https://javascript.info/destructuring-assignment)

#### Q101. How would you correct this code block to make sure that the sent property is set to the Boolean value false?

```javascript
ReactDom.render(
  <Message sent=false />,
  document.getElementById("root")
);
```

- [x] A

```javascript
<Message sent={false} />,
```

- [ ] B

```javascript
ReactDom.render(<Message sent="false" />, document.getElementById('root'));
```

- [ ] C

```javascript
<Message sent="false" />,
```

- [ ] D

```javascript
ReactDom.render(<Message sent="false" />, document.getElementById('root'));
```

[Passing Props to a Component](https://react.dev/learn/passing-props-to-a-component)

#### Q102. This code is part of an app that collects Pokemon. The useState hook below is a piece of state holding onto the names of the Pokemon collected so far. How would you access the collected Pokemon in state?

```javascript
const PokeDex = (props) => {
  const [pokeDex, setPokeDex] = useState([]);
  /// ...
};
```

- [ ] props.pokeDex
- [ ] this.props.pokeDex
- [ ] setPokeDex()
- [x] pokeDex

Explanation: useState always return an array with two values, the state itself (on first value) and the set function that lets you update the state (on second value)
[useState Reference](https://legacy.reactjs.org/blog/2020/09/22/introducing-the-new-jsx-transform.html)

#### Q103. What would you pass to the onClick prop that will allow you to pass the initName prop into the greet handler?

```javascript
const Greeting = ({ initName }) => {
  const greet = (name) => console.log("Hello, " + name + "!");
  return <button onClick={ ... }>Greeting Button </button>
}
```

- [ ] hug
- [ ] this.hug(initName)
- [ ] (name) => this.hug(name)
- [x] () => hug(initName)

Explanation: Apparently the question misstyped `greet` as `hug`. Putting this aside, we can still learn from this question.

- In a function, the global object is the default binding for `this`. In a browser window the global object is [object Window].
  This is a functional Component, so `this` from `this.hug` actually refers to browser window.
  Since it is a functional component, we can directly refer to hug without using `this`.
- To pass a handler to onClick, we should always pass a function rather than execute a function. So we need to use callback here.
  `initName` is available in Greeting's function scope, so we can directly supply as an argument to hug().

#### Q104. What is the name of the compiler used to transform JSX into JavaScript?

- [x] Babel
- [ ] JSX Editor
- [ ] Browser Buddy
- [ ] ReactDOM

[JSX Transform with Babel](https://legacy.reactjs.org/blog/2020/09/22/introducing-the-new-jsx-transform.html)

#### Q105. Which hook is used to prevent a function from being recreated on every component render?

- [x] useCallback
- [ ] useMemo
- [ ] useRef
- [ ] useTransition

[React Hooks useCallback docuementation](https://react.dev/reference/react/useCallback)

#### Q106. Why might you use the `useRef` hook?

- [ ] To bind the function
- [ ] To call a function
- [x] To directly access a DOM
- [ ] To refer to another JS file

[Reference](https://www.smashingmagazine.com/2020/11/react-useref-hook/)

#### Q107. Which of the following is required to use React?

- [x] JavaScript
- [ ] React Router
- [ ] Redux
- [ ] Prop-Types

[Reference](https://reactjs.org/tutorial/tutorial.html#:~:text=What%20Is%20React%3F,of%20code%20called%20%E2%80%9Ccomponents%E2%80%9D.&text=We'll%20get%20to%20the%20funny%20XML%2Dlike%20tags%20soon.)

#### Q108. What is the correct way to get a value from context?

- [ ] const value = useContext(MyContext.Consumer)
- [ ] const value = useContext(MyContext.Provider)
- [x] const value = useContext(MyContext)
- [ ] const value = useContext({value: "intiial value"})

[Reference](https://reactjs.org/docs/hooks-reference.html#usecontext)

#### Q109. Why is ref used?

- [ ] to bind function
- [ ] to call function
- [x] to directly access DOM node
- [ ] to refer to another JS file

[Reference](https://reactjs.org/docs/refs-and-the-dom.html#when-to-use-refs)

#### Q110. Choose the method which should be overridden to stop the component from updating?

- [ ] componentDidMount
- [ ] componentDidUpdate
- [ ] willComponentUpdate
- [x] shouldComponentUpdate

[Reference](https://reactjs.org/docs/react-component.html#shouldcomponentupdate)

#### Q111. What is the functionality of a “webpack” command?

- [ ] Runs react local development server
- [ ] Transfers all JS files to down into one file
- [ ] A module builder
- [x] All of the above

#### Q112. Choose the method which is not a part of ReactDOM?

- [ ] ReactDOM.createPortal()
- [ ] ReactDOM.hydrate()
- [x] ReactDOM.destroy()
- [ ] ReactDOM.findDOMnode()

#### Q113. In react, the key should be?

- [x] Unique among his siblings
- [ ] Unique in DOM
- [ ] Does not requires to be unique
- [ ] all of the above

[Reference](https://reactjs.org/docs/lists-and-keys.html#keys)

#### Q114. Which company developed ReactJS?

- [ ] Google
- [x] Meta (ex Facebook)
- [ ] Apple
- [ ] Twitter

[Reference](https://github.com/facebook/react)

#### Q115. Choose the library which is most often associated with react?

- [ ] Chai
- [ ] Sinon
- [x] Jest
- [ ] Mocha

[Reference](https://reactjs.org/docs/testing-recipes.html)

#### Q116. What of the following is used in React.js to increase performance?

- [ ] Original DOM
- [x] Virtual DOM
- [ ] Both of the above
- [ ] None of the above

[Reference](https://reactjs.org/docs/optimizing-performance.html)

#### Q117. Among The following options, choose the one which helps react for keeping their data uni-directional?

- [ ] DOM
- [x] flux
- [ ] JSX
- [ ] Props

[Reference](https://reactjs.org/blog/2014/05/06/flux.html)

#### Q118. Which choice is a correct refactor of the Greeting class component into a function component?

```javascript
class Greeting extends React.Component {
  render() {
    return <h1>Hello {this.props.name}!<h1>;
  }
}
```

- [ ] `const Greeting = (name) => <h1>{name}</h1>`
- [ ] `function Greeting(name){return <h1>{name}</h1>;}`
- [ ] `const Greeting = props => { <h1>{props.name}</h1> }`
- [x] `const Greeting = ({ name }) => <h1>Hello {name}</h1>;`

#### Q119. Why is the `waitlist` not updating correctly?

```javascript
const Waitlist = () => {
  const [name, setName] = useState('');
  const [waitlist, setWaitlist] = useState([]);
  const onSubmit = (e) => {
    e.preventDefault();
    waitlist.push(name);
  };
  return (
    <div>
      <form onSubmit={onSubmit}>
        <label>
          Name: <input type="text" value={name} onChange={(e) => setName(e.target.value)} />
        </label>
        <button type="submit">Add to waitlist</button>
      </form>

      <ol>
        {waitlist.map((name) => (
          <li key={name}>{name}</li>
        ))}
      </ol>
    </div>
  );
};
```

- [x] `waitlist` is being mutated directly. Use the `setWaitlist` function instead to update the waitlist state.
- [ ] The form is reloading the page each time `Add to waitlist` is clicked.
- [ ] The `Add to waitlist` button is missing a click handler.
- [ ] There are likely repeated names inside of the `waitlist` array.

[Reference](https://reactjs.org/docs/react-component.html#setstate)

#### Q120. What is the pattern that is used in the Context.Consumer below?

<Context.Consumer>
{(isLoggedIn)=><b>{isLoggedIn ? "Online" : "Offline"}</b>}
</Context.Consumer>

- [ ] higher-order component
- [ ] wish component
- [x] Render Props
- [ ] setup Componet

#### Q121. In React.js which one of the following is used to create a class for Inheritance ?

- [ ] Create
- [x] Extends
- [ ] Inherits
- [ ] Delete

[Reference](https://www.geeksforgeeks.org/react-js-quiz-set-1/)

#### Q122. What is the purpose of render() in React.js?

- [ ] To replace the existing markup
- [ ] To update the existing markup
- [x] Both of the above
- [ ] None of the above

[Reference](https://www.geeksforgeeks.org/explain-the-purpose-of-render-in-reactjs/)

#### Q123. What is the use of super(props) in React.js?

- [ ] To call the constructor of the parent class
- [ ] To initialize this.props in the constructor
- [x] Both of the above
- [ ] None of the above

[Reference](https://www.geeksforgeeks.org/what-is-the-use-of-superprops/)

#### Q124. What is Redux in React.js?

- [x] A state container for JavaScript apps
- [ ] A tool for building UI components
- [ ] Both of the above
- [ ] None of the above

[Reference](https://www.freecodecamp.org/news/what-is-redux-store-actions-reducers-explained/)

#### Q125. What is the purpose of the virtual DOM in React.js, and how does it improve performance in web applications??

- [ ] The virtual DOM is used to store user authentication data securely.
- [ ] The virtual DOM is a backup copy of the actual DOM, created for debugging purposes.
- [x] The virtual DOM is a lightweight representation of the actual DOM, and it helps improve performance by minimizing direct manipulation of the real DOM.
- [ ] The virtual DOM is a database used to store component states.

[Reference](https://medium.com/@vinaynkokate/demystifying-dynamic-web-applications-understanding-the-dom-and-web-browser-interactions-cc1b113adfa)

#### Q126. You run the following code and get this error message: "invalid hook call." what is wrong with the code?

```javascript
import React from 'react';

const [poked, setPoked] = React.useState(false);

function PokeButton() {
  return <button onClick={() => setPoked(true)}>{poked ? 'You have left a poke.' : 'Poke'}</button>;
}
```

- [x] The useState call needs to be called inside of the PokeButton component.
- [ ] The react package is likely not installed correctly.
- [ ] useState is not imported correctly. Import useState directly instead of importing react.
- [ ] PokeButton is a pure function and therefore cannot have any local state.

#### Q127. A colleague comes to you for help on a react component. They say that the poke button renders correctly, however when the button is clicked, this error is shown: "setPoked is not defined". What is wrong with their code?

```javascript
function PokeButton() {
  const { poked, setPoked } = useState(false);
  return <button onclick={() => setPoked(true)}>{poked ? 'You have left a poke.' : 'Poke'}</button>;
}
```

- [ ] onClick prop should be onclick.
- [ ] The click handler passed to the onClick prop is inlined. Move this handler into a variable outside of JSX.
- [x] They use object destructructing instead of array destructructing. Wrap the poked and setPoked values in an array.
- [ ] poked and setPoked are not destructured in the correct order.

#### Q128. This component is loaded dynamically. What should you replace XXXX with to complete the code?

```javascript
const OtherComponent = React.lazy(() => import('./OtherComponent.js'));

function MyComponent() {
  return (
    <XXXX fallback={<spinner />}>
      <OtherComponent />
    </XXXX>
  );
}
```

- [ ] Component
- [ ] Fragment
- [x] Suspense
- [ ] Lazy

#### Q129. Elements in lists in React should have \_**\_ that are \_\_\_** .

- [x] keys ; unique
- [ ] keys ; indexes
- [ ] style ; inline
- [ ] values ; not-null
      [Source: React Docs](https://legacy.reactjs.org/docs/lists-and-keys.html)

#### Q130. You want to memorize a callback function so you ensure that React does not recreate the function at each render. Which hook would you use to accomplish this?

- [ ] useRef
- [ ] useMemo
- [ ] memo
- [x] useCallback

[Source: CodeDamn](https://codedamn.com/news/reactjs/usememo-and-usecallback-hooks)

#### Q131. You want to perform a network operation as the result of a change to a component's state named userInput. what would you replace XXXX with?

```javascript
useEffect(callNetworkFunc, XXXX);
```

- [x] [userInput]
- [ ] userInput
- [ ] undefined
- [ ] []

#### Q132. When is the Hello component displayed?

```javascript
<div>{isLoggedIn ? <Hello /> : null}</div>
```

- [ ] when isLoggedIn is false
- [x] when isLoggedIn is true
- [ ] when isLoggedIn is false and the Hello function is invoked
- [ ] never

#### Q133. When do you use `useLayoutEffect`?

- [ ] to optimize for all devices
- [ ] to complete the update
- [x] to change the layout of the screen
- [ ] when you need the browser to paint before the effect runs

#### Q134. What is the difference between state and props in React?

- [ ] Props are set by the parent component, state is set by the child component
- [x] Props are passed to a component, state is managed within the component
- [ ] Props can be updated, state cannot be updated
- [ ] There is no difference - props and state are the same

#### Q135. Which language can you not use with React?

- [x] Swift.
- [ ] JSX.
- [ ] Javascipt.
- [ ] TypeScript.

#### Q136. Which answer best describes a function component?

- [ ] A function component is the same as a class component.
- [x] A function component accepts a single props object and returns a React element.
- [ ] A function component is the only way to create a component.
- [ ] A function component is required to create a React component.

#### Q137. Which library does the `fetch()` function come from?

- [ ] FetchJS
- [ ] ReactDOM
- [x] No library. `fetch()` is supported by most browsers.
- [ ] React

### Q138. In React, what is the purpose of the `key` prop when rendering a list of components

- [ ] The `key` prop is used to provide a unique identifier for the component.
- [ ] The `key` prop is used to define the color of the component.
- [ ] The `key` prop is required to render a list of components.
- [x] The `key` prop is used by React to optimize updates and identify which items have changed or been added/removed in the list.

#### Q139. What is the primary function of React Router?

- [ ] React Router is used for fetching data from APIs.
- [ ] React Router is used to create animations in React applications.
- [ ] React Router is used for managing state in React components.
- [x] React Router is used for adding navigation and routing to React applications, allowing users to navigate between different views or pages.

#### Q140. When should you use Redux in a React application?

- [ ] Redux is always required in React applications.
- [ ] Redux should be used when you need to fetch data from APIs.
- [ ] Redux is used for creating user interfaces but not for state management.
- [x] Redux is typically used when you have complex state management needs, such as sharing state between multiple components or handling deeply nested state.

#### Q141. What is the use of React hooks?

- [ ] To optimize React apps for mobile devices
- [ ] To add visual effects to React components.
- [x] To allow using state and lifecycle methods in function components
- [ ] To integrate with external UI libraries like Bootstrap

#### Q142. How can you pass data through a React component tree without having to pass props down manually at every level?

- [x] By using React context
- [ ] By using redux
- [ ] By using react router
- [ ] By using react lifecycle methods
