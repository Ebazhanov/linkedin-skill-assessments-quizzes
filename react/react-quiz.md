## React

#### Q1. What is React?

- [ ] A server-side programming language
- [x] A JavaScript library for building user interfaces
- [ ] A database management system
- [ ] A CSS framework

[Reference React Overview](https://reactjs.org/docs/getting-started.html)

#### Q2. Which method is used to create a React component?

- [ ] `React.createComponent()`
- [x] `function Component()` or `class Component extends React.Component`
- [ ] `new React.Component()`
- [ ] `React.makeComponent()`

[Reference Components and Props](https://reactjs.org/docs/components-and-props.html)

#### Q3. What is JSX?

- [ ] A new programming language
- [x] A syntax extension for JavaScript that allows writing HTML-like code
- [ ] A CSS preprocessor
- [ ] A database query language

[Reference Introducing JSX](https://reactjs.org/docs/introducing-jsx.html)

#### Q4. Which hook is used to manage state in functional components?

- [ ] `useEffect`
- [x] `useState`
- [ ] `useContext`
- [ ] `useReducer`

```jsx
const [count, setCount] = useState(0);
```

[Reference Using the State Hook](https://reactjs.org/docs/hooks-state.html)

#### Q5. What is the purpose of the `useEffect` hook?

- [ ] To manage component state
- [x] To perform side effects in functional components
- [ ] To create context
- [ ] To optimize performance

[Reference Using the Effect Hook](https://reactjs.org/docs/hooks-effect.html)

#### Q6. Which prop is used to pass data from parent to child components?

- [ ] `state`
- [x] `props`
- [ ] `context`
- [ ] `ref`

```jsx
<ChildComponent name="John" age={25} />
```

[Reference Components and Props](https://reactjs.org/docs/components-and-props.html)

#### Q7. What is the correct way to handle events in React?

```jsx
function Button() {
  const handleClick = () => {
    console.log('Button clicked');
  };
  
  return <button onClick={handleClick}>Click me</button>;
}
```

- [x] The above code is correct
- [ ] Use `onclick` instead of `onClick`
- [ ] Events cannot be handled in functional components
- [ ] Use `addEventListener` method

[Reference Handling Events](https://reactjs.org/docs/handling-events.html)

#### Q8. What is the purpose of keys in React lists?

- [ ] To style list items
- [x] To help React identify which items have changed, added, or removed
- [ ] To sort list items
- [ ] To filter list items

[Reference Lists and Keys](https://reactjs.org/docs/lists-and-keys.html)

#### Q9. Which lifecycle method is called after a component is mounted?

- [ ] `componentWillMount`
- [x] `componentDidMount`
- [ ] `componentWillUpdate`
- [ ] `componentDidUpdate`

[Reference Component Lifecycle](https://reactjs.org/docs/react-component.html#componentdidmount)

#### Q10. What is the correct way to update state in a class component?

- [ ] `this.state.count = 1;`
- [x] `this.setState({ count: 1 });`
- [ ] `this.updateState({ count: 1 });`
- [ ] `this.state = { count: 1 };`

[Reference State and Lifecycle](https://reactjs.org/docs/state-and-lifecycle.html)

#### Q11. Which hook is used to access React context?

- [ ] `useState`
- [ ] `useEffect`
- [x] `useContext`
- [ ] `useReducer`

[Reference useContext Hook](https://reactjs.org/docs/hooks-reference.html#usecontext)

#### Q12. What is the purpose of React.Fragment?

- [ ] To create new components
- [x] To group multiple elements without adding extra DOM nodes
- [ ] To handle errors
- [ ] To manage state

```jsx
return (
  <React.Fragment>
    <h1>Title</h1>
    <p>Description</p>
  </React.Fragment>
);
```

[Reference Fragments](https://reactjs.org/docs/fragments.html)

#### Q13. Which method is used to prevent default behavior in React events?

- [ ] `event.stop()`
- [x] `event.preventDefault()`
- [ ] `event.cancel()`
- [ ] `event.halt()`

[Reference SyntheticEvent](https://reactjs.org/docs/events.html)

#### Q14. What is the correct way to conditionally render elements in React?

```jsx
function Greeting({ isLoggedIn }) {
  return (
    <div>
      {isLoggedIn ? <h1>Welcome back!</h1> : <h1>Please sign up.</h1>}
    </div>
  );
}
```

- [x] The above code is correct
- [ ] Use `if-else` statements inside JSX
- [ ] Use `switch` statements inside JSX
- [ ] Conditional rendering is not possible in React

[Reference Conditional Rendering](https://reactjs.org/docs/conditional-rendering.html)

#### Q15. Which hook is used for performance optimization by memoizing expensive calculations?

- [ ] `useCallback`
- [x] `useMemo`
- [ ] `useEffect`
- [ ] `useState`

[Reference useMemo Hook](https://reactjs.org/docs/hooks-reference.html#usememo)

#### Q16. What is the purpose of the `useCallback` hook?

- [ ] To manage state
- [x] To memoize callback functions
- [ ] To perform side effects
- [ ] To access context

[Reference useCallback Hook](https://reactjs.org/docs/hooks-reference.html#usecallback)

#### Q17. Which method is used to create refs in functional components?

- [ ] `createRef()`
- [x] `useRef()`
- [ ] `makeRef()`
- [ ] `newRef()`

[Reference useRef Hook](https://reactjs.org/docs/hooks-reference.html#useref)

#### Q18. What is the correct way to pass a function as a prop?

```jsx
function Parent() {
  const handleClick = () => console.log('Clicked');
  return <Child onClick={handleClick} />;
}
```

- [x] The above code is correct
- [ ] Functions cannot be passed as props
- [ ] Use `onClick="handleClick"`
- [ ] Use `onClick={handleClick()}`

[Reference Passing Functions to Components](https://reactjs.org/docs/faq-functions.html)

#### Q19. Which statement about React components is correct?

- [ ] Component names must start with lowercase letters
- [x] Component names must start with uppercase letters
- [ ] Component names can start with numbers
- [ ] Component names are case-insensitive

[Reference Components and Props](https://reactjs.org/docs/components-and-props.html)

#### Q20. What is the purpose of the `key` prop in React?

- [ ] To encrypt component data
- [x] To provide a stable identity for list items
- [ ] To set component priority
- [ ] To define component styles

[Reference Reconciliation](https://reactjs.org/docs/reconciliation.html#keys)

#### Q21. Which hook is used to reduce state management complexity?

- [ ] `useState`
- [x] `useReducer`
- [ ] `useEffect`
- [ ] `useContext`

[Reference useReducer Hook](https://reactjs.org/docs/hooks-reference.html#usereducer)

#### Q22. What is the correct way to handle forms in React?

```jsx
function Form() {
  const [value, setValue] = useState('');
  
  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(value);
  };
  
  return (
    <form onSubmit={handleSubmit}>
      <input 
        value={value} 
        onChange={(e) => setValue(e.target.value)} 
      />
      <button type="submit">Submit</button>
    </form>
  );
}
```

- [x] The above code demonstrates controlled components
- [ ] Use uncontrolled components only
- [ ] Forms cannot be handled in React
- [ ] Use jQuery for form handling

[Reference Forms](https://reactjs.org/docs/forms.html)

#### Q23. Which method is used to update state based on previous state?

```jsx
setCount(prevCount => prevCount + 1);
```

- [x] Pass a function to the state setter
- [ ] Use `this.setState` with previous state
- [ ] Access state directly
- [ ] Use global variables

[Reference Functional Updates](https://reactjs.org/docs/hooks-reference.html#functional-updates)

#### Q24. What is the purpose of React.memo?

- [ ] To manage component state
- [x] To prevent unnecessary re-renders of functional components
- [ ] To create memoized values
- [ ] To handle side effects

[Reference React.memo](https://reactjs.org/docs/react-api.html#reactmemo)

#### Q25. Which hook is used to imperatively access DOM elements?

- [ ] `useState`
- [x] `useRef`
- [ ] `useEffect`
- [ ] `useContext`

[Reference Refs and the DOM](https://reactjs.org/docs/refs-and-the-dom.html)

#### Q26. What is the correct way to handle asynchronous operations in useEffect?

```jsx
useEffect(() => {
  const fetchData = async () => {
    const response = await fetch('/api/data');
    const data = await response.json();
    setData(data);
  };
  
  fetchData();
}, []);
```

- [x] Create an async function inside useEffect
- [ ] Make useEffect async directly
- [ ] Use promises only
- [ ] Async operations are not allowed in useEffect

[Reference Effect Hook with Async](https://reactjs.org/docs/hooks-faq.html#how-can-i-do-data-fetching-with-hooks)

#### Q27. Which statement about React Hooks is correct?

- [ ] Hooks can be called conditionally
- [x] Hooks must be called at the top level of React functions
- [ ] Hooks can be called in loops
- [ ] Hooks can be called in nested functions

[Reference Rules of Hooks](https://reactjs.org/docs/hooks-rules.html)

#### Q28. What is the purpose of the dependency array in useEffect?

- [ ] To pass data to the effect
- [x] To control when the effect runs
- [ ] To define effect priority
- [ ] To handle errors

[Reference Effect Dependencies](https://reactjs.org/docs/hooks-effect.html#tip-optimizing-performance-by-skipping-effects)

#### Q29. Which method is used to create a custom hook?

```jsx
function useCounter(initialValue = 0) {
  const [count, setCount] = useState(initialValue);
  
  const increment = () => setCount(count + 1);
  const decrement = () => setCount(count - 1);
  
  return { count, increment, decrement };
}
```

- [x] Create a function that starts with "use" and uses other hooks
- [ ] Use the `createHook` method
- [ ] Extend the Hook class
- [ ] Custom hooks are not possible

[Reference Building Your Own Hooks](https://reactjs.org/docs/hooks-custom.html)

#### Q30. What is the correct way to handle errors in React components?

- [ ] Use try-catch blocks in render methods
- [x] Use Error Boundaries with componentDidCatch
- [ ] Use global error handlers
- [ ] Errors cannot be handled in React

[Reference Error Boundaries](https://reactjs.org/docs/error-boundaries.html)

#### Q31. Which statement about React Context is correct?

- [ ] Context should be used for all state management
- [x] Context is designed to share data across the component tree
- [ ] Context cannot be used with hooks
- [ ] Context is only for class components

[Reference Context](https://reactjs.org/docs/context.html)

#### Q32. What is the purpose of the `useLayoutEffect` hook?

- [ ] To manage component layout
- [x] To perform DOM mutations synchronously after all DOM mutations
- [ ] To create responsive layouts
- [ ] To handle CSS animations

[Reference useLayoutEffect Hook](https://reactjs.org/docs/hooks-reference.html#uselayouteffect)

#### Q33. Which method is used to optimize performance by preventing unnecessary renders?

- [ ] `shouldComponentUpdate` only
- [x] `React.memo`, `useMemo`, `useCallback`, and `shouldComponentUpdate`
- [ ] `componentDidUpdate` only
- [ ] Performance optimization is automatic

[Reference Optimizing Performance](https://reactjs.org/docs/optimizing-performance.html)

#### Q34. What is the correct way to pass multiple props to a component?

```jsx
const props = { name: 'John', age: 25, city: 'New York' };
return <UserCard {...props} />;
```

- [x] Use the spread operator
- [ ] Pass props individually only
- [ ] Use arrays for multiple props
- [ ] Multiple props are not allowed

[Reference JSX Spread Attributes](https://reactjs.org/docs/jsx-in-depth.html#spread-attributes)

#### Q35. Which hook is used to debug custom hooks?

- [ ] `useEffect`
- [x] `useDebugValue`
- [ ] `useState`
- [ ] `useRef`

[Reference useDebugValue Hook](https://reactjs.org/docs/hooks-reference.html#usedebugvalue)

#### Q36. What is the purpose of React.StrictMode?

- [ ] To enforce strict typing
- [x] To highlight potential problems in an application during development
- [ ] To improve performance
- [ ] To enable strict mode in JavaScript

[Reference Strict Mode](https://reactjs.org/docs/strict-mode.html)

#### Q37. Which statement about React portals is correct?

- [ ] Portals are used for routing
- [x] Portals provide a way to render children into a DOM node outside the parent component
- [ ] Portals are used for state management
- [ ] Portals are deprecated

[Reference Portals](https://reactjs.org/docs/portals.html)

#### Q38. What is the correct way to handle component cleanup?

```jsx
useEffect(() => {
  const timer = setInterval(() => {
    console.log('Timer tick');
  }, 1000);
  
  return () => {
    clearInterval(timer);
  };
}, []);
```

- [x] Return a cleanup function from useEffect
- [ ] Use componentWillUnmount only
- [ ] Cleanup is automatic
- [ ] Use try-finally blocks

[Reference Effect Cleanup](https://reactjs.org/docs/hooks-effect.html#effects-with-cleanup)

#### Q39. Which method is used to forward refs in React?

- [ ] `React.createRef`
- [x] `React.forwardRef`
- [ ] `React.passRef`
- [ ] `React.sendRef`

[Reference Forwarding Refs](https://reactjs.org/docs/forwarding-refs.html)

#### Q40. What is the purpose of the `useImperativeHandle` hook?

- [ ] To manage component state
- [x] To customize the instance value exposed to parent components when using ref
- [ ] To handle imperative animations
- [ ] To create imperative APIs

[Reference useImperativeHandle Hook](https://reactjs.org/docs/hooks-reference.html#useimperativehandle)
