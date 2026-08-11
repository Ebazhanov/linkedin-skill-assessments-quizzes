## React.js

#### Q1. React 라이브러리에서 컴포넌트 하나만 가져오고 싶을 때 올바른 import 문법은?

- [ ] `import React.Component from 'react'`
- [ ] `import [ Component ] from 'react'`
- [ ] `import Component from 'react'`
- [x] `import { Component } from 'react'`

#### Q2. 함수 컴포넌트가 같은 props를 받았을 때 항상 같은 결과로 렌더링된다면, 적용할 수 있는 간단한 최적화는?

- [x] React.memo로 컴포넌트를 감싼다
- [ ] useReducer 훅을 사용한다
- [ ] useMemo 훅을 사용한다
- [ ] shouldComponentUpdate 생명주기 메서드를 구현한다

#### Q3. 다음 코드를 실행하면 문법 오류가 발생한다. 어떻게 고쳐야 할까?

```javascript
const person = (firstName, lastName) =>
{
  first: firstName,
  last: lastName
}
console.log(person("Jill", "Wilson"))
```

- [x] 반환하는 객체 리터럴을 소괄호로 감싼다
- [ ] 함수를 다른 파일에서 호출한다
- [ ] 마지막 소괄호 앞에 return을 추가한다
- [ ] 객체를 배열로 바꾼다

#### Q4. 다음 import 문이 있는 파일에서, 컴포넌트의 상태 관리에 무엇을 사용하고 있다고 볼 수 있을까?

`import React, { useState } from 'react';`

- [x] React Hooks
- [ ] 상태를 가진 클래스 컴포넌트
- [ ] 수학 연산
- [ ] 클래스 컴포넌트

#### Q5. 다음 코드에서 객체 축약 표기법(property shorthand)을 사용해 값을 채웠다. console.log(person)의 결과는?

```javascript
const name = 'Rachel';
const age = 31;
const person = { name, age };
console.log(person);
```

- [ ] `{ {name: "Rachel", age: 31} }`
- [x] `{name: "Rachel", age: 31}`
- [ ] `{person: "Rachel", person: 31}`
- [ ] `{person: {name: "Rachel", age: 31}}`

#### Q6. React와 가장 흔히 함께 쓰이는 테스트 라이브러리는?

- [ ] Mocha
- [ ] Chai
- [ ] Sinon
- [x] Jest

#### Q7. 배열 구조 분해(destructuring)를 사용해 다음 배열의 첫 번째 항목("cooking")을 가져오려면?

```javascript
const topics = ['cooking', 'art', 'history'];
```

- [ ] `const first = ["cooking", "art", "history"]`
- [ ] `const [] = ["cooking", "art", "history"]`
- [ ] `const [, first]["cooking", "art", "history"]`
- [x] `const [first] = ["cooking", "art", "history"]`

#### Q8. 컴포넌트 트리 아래로 props를 일일이 수동으로 내려주지 않고 값을 전달하려면 무엇을 사용해야 할까?

- [ ] React Send
- [ ] React Pinpoint
- [ ] React Router
- [x] React Context

#### Q9. 다음 코드를 실행하면 콘솔에 무엇이 출력될까?

```javascript
const [, , animal] = ['Horse', 'Mouse', 'Cat'];
console.log(animal);
```

- [ ] Horse
- [x] Cat
- [ ] Mouse
- [ ] undefined

#### Q10. JSX를 createElement 호출로 변환하는 데 사용하는 도구는?

- [ ] JSX Editor
- [ ] ReactDOM
- [ ] Browser Buddy
- [x] Babel

#### Q11. React 컴포넌트에서 useState 대신 useReducer를 쓰는 이유로 알맞은 것은?

- [ ] Redux를 대체하고 싶을 때
- [x] 앱에서 더 복잡한 상태를 다뤄야 할 때
- [ ] 성능을 개선하고 싶을 때
- [ ] 프로덕션에서 앱을 망가뜨리고 싶을 때

#### Q12. 다음 문법을 사용하면 컴포넌트에서 어떤 속성을 사용할 수 있을까?

```javascript
<Message {...props} />
```

- [ ] 값이 바뀌지 않은 속성만
- [x] props의 모든 속성
- [ ] 자식 속성들만
- [ ] 값이 바뀐 속성들만

#### Q13. React Router에서 다음 코드의 ":id"는 무엇이라고 부를까?

```javascript
<Route path="/:id" />
```

- [ ] 라우트 모달
- [x] 라우트 파라미터
- [ ] 라우트 구분자
- [ ] 라우트 링크

#### Q14. Dish 컴포넌트를 렌더링하면 DOM에 어떤 엘리먼트가 추가될까?

```javascript
function Dish() {
  return <h1>Mac and Cheese</h1>;
}

ReactDOM.render(<Dish />, document.getElementById('root'));
```

- [ ] `div`
- [ ] section
- [ ] component
- [x] `h1`

#### Q15. 다음 호출의 결과로 DOM에 만들어지는 엘리먼트는?

```javascript
React.createElement('h1', null, "What's happening?");
```

- [ ] `<h1 props={null}>What's happening?</h1>`
- [x] `<h1>What's happening?</h1>`
- [ ] `<h1 id="component">What's happening?</h1>`
- [ ] `<h1 id="element">What's happening?</h1>`

#### Q16. 다음 Suspense 컴포넌트가 로딩 표시를 보여주게 하려면 어떤 속성을 지정해야 할까?

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

- [ ] lazy
- [ ] loading
- [x] fallback
- [ ] spinner

#### Q17. 다음 코드에서 중괄호 안의 message는 무엇이라고 부를까?

```javascript
const message = 'Hi there';
const element = <p>{message}</p>;
```

- [ ] JS 함수
- [ ] JS 엘리먼트
- [x] JS 표현식
- [ ] JSX 래퍼

#### Q18. 코드 분할(code splitting)을 실행할 때 사용하는 것은?

- [ ] `React.memo`
- [ ] `React.split`
- [x] `React.lazy`
- [ ] `React.fallback`

#### Q19. useLayoutEffect는 언제 사용할까?

- [ ] 모든 기기에 맞춰 최적화하고 싶을 때
- [ ] 업데이트를 완료시키고 싶을 때
- [ ] 현재 화면을 바꾸고 싶을 때
- [x] effect가 실행되기 전에 브라우저가 먼저 화면을 그려야 할 때

#### Q20. 다음 두 버튼의 onClick 이벤트 처리 방식에는 어떤 차이가 있을까? (this.handleClick은 이미 올바르게 바인딩되어 있다고 가정)

```javascript
A. <button onClick={this.handleClick}>Click Me</button>
B. <button onClick={event => this.handleClick(event)}>Click Me</button>
```

- [ ] A 버튼은 클릭을 일으킨 이벤트 객체에 접근할 수 없다
- [ ] B 버튼은 this.handleClick을 제대로 실행하지 못한다
- [ ] A 버튼은 this.handleClick을 제대로 실행하지 못한다
- [x] 차이가 없다. 둘 다 동일하게 동작한다

#### Q21. Dish 컴포넌트로 전달되는 속성을 구조 분해하려면 어떻게 고쳐야 할까?

```javascript
function Dish(props) {
  return (
    <h1>
      {props.name} {props.cookingTime}
    </h1>
  );
}
```

- [ ] `function Dish([name, cookingTime]) { return <h1>{name} {cookingTime}</h1>; }`
- [x] `function Dish({name, cookingTime}) { return <h1>{name} {cookingTime}</h1>; }`
- [ ] `function Dish(props) { return <h1>{name} {cookingTime}</h1>; }`
- [ ] `function Dish(...props) { return <h1>{name} {cookingTime}</h1>; }`

#### Q22. React.PureComponent는 언제 사용할까?

- [ ] 컴포넌트가 속성을 갖지 않기를 원할 때
- [ ] 비교가 필요한 중첩 컴포넌트를 가지고 있을 때
- [x] shouldComponentUpdate()의 기본 구현을 활용하고 싶을 때
- [ ] 컴포넌트가 상태를 갖지 않기를 원할 때

#### Q23. 컴포넌트의 props 값을 내부 state로 그대로 복사하는 것을 되도록 피해야 하는 이유는?

- [ ] state는 절대 변경하면 안 되기 때문에
- [ ] getDerivedStateFromProps()는 안전하지 않은 메서드이기 때문에
- [x] props가 바뀌었을 때 컴포넌트가 그 변화를 반영해 갱신되도록 하고 싶기 때문에
- [ ] 데이터를 상위 컴포넌트로 다시 흘려보내고 싶기 때문에

#### Q24. children이라는 속성은 무엇일까?

- [ ] 컴포넌트의 상태에 자식을 추가하는 속성
- [x] 여는 태그와 닫는 태그를 가진 컴포넌트에 대해 JSX가 만들어주는, 그 사이 내용을 가리키는 특수한 속성
- [ ] 배열을 속성으로 정의할 수 있게 해주는 속성
- [ ] 자식 컴포넌트에 데이터를 전달할 수 있게 해주는 속성

설명: [children in JSX](https://reactjs.org/docs/jsx-in-depth.html#children-in-jsx)

#### Q25. 브라우저 DOM의 innerHTML 속성을 대신하기 위해 사용하는 속성은?

- [ ] injectHTML
- [x] dangerouslySetInnerHTML
- [ ] weirdSetInnerHTML
- [ ] strangeHTML

#### Q26. React 애플리케이션을 흔히 설명할 때 쓰이는 표현으로 알맞은 것은?

- [x] 선언적(declarative)
- [ ] 통합적(integrated)
- [ ] 폐쇄적(closed)
- [ ] 명령적(imperative)

#### Q27. webpack을 사용할 때 로더(loader)가 필요한 상황은?

- [ ] 파일 시스템에 폴더를 구성할 때
- [x] 파일을 전처리(preprocess)할 때
- [ ] 외부 데이터를 불러올 때
- [ ] 사용자의 휴대폰에 웹사이트를 로드할 때

#### Q28. 실제 DOM과 동기화된 상태로 메모리에 유지되는 UI 표현을 무엇이라고 부를까?

- [x] 가상 DOM(Virtual DOM)
- [ ] DOM
- [ ] 가상 엘리먼트
- [ ] 그림자 DOM

#### Q29. 다음 코드를 작성했는데 아무것도 렌더링되지 않는다. 어떻게 고쳐야 할까?

```javascript
const Heading = () => {
  <h1>Hello!</h1>;
};
```

- [ ] 렌더링 함수를 추가한다
- [x] 중괄호를 소괄호로 바꾸거나, 첫 h1 태그 앞에 return 키워드를 추가한다
- [ ] h1을 다른 컴포넌트로 옮긴다
- [ ] h1을 div로 감싼다

#### Q30. 자바스크립트에서 상수를 만들 때 사용하는 키워드는?

- [x] const
- [ ] let
- [ ] constant
- [ ] var

#### Q31. 컴포넌트 트리 어디에서 발생하든 자바스크립트 에러를 잡아내는 React 컴포넌트를 무엇이라고 부를까?

- [ ] error boss
- [ ] error catcher
- [ ] error helper
- [x] error boundary

#### Q32. 클래스 컴포넌트의 어떤 생명주기 메서드에서 데이터 요청을 해야 할까?

- [ ] constructor
- [x] componentDidMount
- [ ] componentWillReceiveProps
- [ ] componentWillMount

#### Q33. React 컴포넌트는 조합돼 UI를 만든다. 컴포넌트 자체는 어떻게 조합될까?

- [ ] 같은 파일에 몰아넣어서
- [x] 다른 컴포넌트를 중첩시켜서
- [ ] webpack으로
- [ ] 코드 분할로

#### Q34. React의 모든 컴포넌트는 자신의 props에 대해 어떻게 동작해야 할까?

- [ ] 모나드(monad)처럼
- [x] 순수 함수(pure function)처럼
- [ ] 재귀 함수처럼
- [ ] 고차 함수처럼

#### Q35. 아래 코드에서 `[e.target.id]` 부분을 무엇이라고 부를까?

```javascript
handleChange(e) {
  this.setState({ [e.target.id]: e.target.value })
}
```

- [x] 계산된 프로퍼티 이름(computed property name)
- [ ] 미리 설정된 값
- [ ] 동적 키(dynamic key)
- [ ] JSX 문자열 코드

#### Q36. 이 컴포넌트의 이름은 무엇일까?

```javascript
class Clock extends React.Component {
  render() {
    return <h1>Look at the time: {time}</h1>;
  }
}
```

- [x] Clock
- [ ] 이름 속성을 가지고 있지 않다
- [ ] React.Component
- [ ] Component

#### Q37. Array.map() 함수에는 무엇을 넘길까?

- [x] 배열의 각 요소마다 한 번씩 호출되는 콜백 함수
- [ ] 새 순회를 시작할 다른 배열의 이름
- [ ] 함수를 호출하고 싶은 횟수
- [ ] 함수가 해야 할 일을 설명하는 문자열

#### Q38. setState에 객체 대신 함수를 넘기는 것이 좋은 이유는?

- [ ] 캡슐화가 더 잘 되기 때문에
- [ ] 객체가 변경되지 않았음을 보장하기 때문에
- [ ] 컴포넌트를 자동으로 업데이트하기 때문에
- [x] setState는 비동기라서 시점에 따라 값이 최신이 아닐 수 있기 때문에

설명: [setState에 함수 전달하기](https://medium.com/@wisecobbler/using-a-function-in-setstate-instead-of-an-object-1f5cfd6e55d1)

#### Q39. React 엘리먼트를 DOM에 렌더링하는 render() 함수는 어느 패키지에 들어있을까?

- [ ] `React`
- [x] `ReactDOM`
- [ ] `Render`
- [ ] `DOM`

#### Q40. 비제어(uncontrolled) 폼 필드에 기본값을 지정하려면 어떻게 해야 할까?

- [ ] value 속성을 사용한다
- [x] defaultValue 속성을 사용한다
- [ ] default 속성을 사용한다
- [ ] 자동으로 하나가 할당된다

#### Q41. 다음 코드가 에러 없이 실행되려면 무엇을 바꿔야 할까?

```javascript
class clock extends React.Component {
  render() {
    return <h1>Look at the time: {this.props.time}</h1>;
  }
}
```

- [ ] 반환값을 따옴표로 감싼다
- [ ] this를 제거한다
- [ ] render 메서드를 제거한다
- [x] clock의 첫 글자를 대문자로 바꾼다

**설명:** JSX에서는 소문자로 시작하는 이름을 HTML 태그로 인식한다.
자세한 내용은 [이 문서](https://reactjs.org/docs/jsx-in-depth.html#html-tags-vs.-react-components)에서 확인할 수 있다.

#### Q42. 페이지 제목을 바꿀 때 사용할 수 있는 훅 사용법으로 올바른 것은?

- [x] `useEffect(function updateTitle() { document.title = name + ' ' + lastname; });`
- [ ] `useEffect(() => { title = name + ' ' + lastname; });`
- [ ] `useEffect(function updateTitle() { name + ' ' + lastname; });`
- [ ] `useEffect(function updateTitle() { title = name + ' ' + lastname; });`

#### Q43. 컴포넌트를 지연 로드(lazy load)할 때 사용하는 것은?

- [ ] React.fallback
- [ ] React.split
- [x] React.lazy
- [ ] React.memo

#### Q44. 다음 컴포넌트가 마운트될 때만 setDone 콜백을 호출하려면?

```javascript
function MyComponent(props) {
  const [done, setDone] = useState(false);

  return <h1>Done: {done}</h1>;
}
```

- [ ] `useEffect(() => { setDone(true); });`
- [x] `useEffect(() => { setDone(true); }, []);`
- [ ] `useEffect(() => { setDone(true); }, [setDone]);`
- [ ] `useEffect(() => { setDone(true); }, [done, setDone]);`

#### Q45. 다음 코드는 handleClick을 참조로 넘기는 대신 즉시 호출해버리고 있다. 어떻게 고쳐야 할까?

```javascript
<button onClick={this.handleClick()}>Click this</button>
```

- [ ] `<button onClick={this.handleClick.bind(handleClick)}>Click this</button>`
- [ ] `<button onClick={handleClick()}>Click this</button>`
- [x] `<button onClick={this.handleClick}>Click this</button>`
- [ ] `<button onclick={this.handleClick}>Click this</button>`

#### Q46. 함수 컴포넌트를 가장 잘 설명하는 것은?

- [ ] 함수 컴포넌트는 클래스 컴포넌트와 동일하다
- [x] 함수 컴포넌트는 props 객체 하나를 받아 React 엘리먼트를 반환한다
- [ ] 함수 컴포넌트는 컴포넌트를 만드는 유일한 방법이다
- [ ] 함수 컴포넌트는 React 컴포넌트를 만들기 위해 반드시 필요하다

#### Q47. 전역 함수 fetch()는 어느 라이브러리에서 제공할까?

- [ ] FetchJS
- [ ] ReactDOM
- [x] 라이브러리 없이, 대부분의 브라우저가 기본 제공한다
- [ ] React

#### Q48. name이 처음에 "john"이 아니라고 가정할 때, 다음 useEffect가 실행되면 어떤 일이 벌어질까?

```javascript
useEffect(() => {
  setName('John');
}, [name]);
```

- [ ] 즉시 에러가 발생한다
- [ ] 다른 컴포넌트가 name 변수를 사용하지 않을 때까지 기다린 뒤 실행된다
- [x] name 값을 한 번 갱신하고, 그 값이 다시 바뀌기 전까지는 아무 일도 하지 않는다
- [ ] 무한 루프를 일으킨다

#### Q49. 다음 중 React 컴포넌트를 다시 렌더링시키지 않는 것은?

- [ ] 컴포넌트가 this.setState(...)를 호출한다
- [ ] props 중 하나의 값이 바뀐다
- [ ] this.forceUpdate()가 호출된다
- [x] 자식 컴포넌트 중 하나가 다시 렌더링된다

#### Q50. 클래스 컴포넌트에 handleClick이라는 메서드를 새로 만들었지만 동작하지 않는다. 무엇이 빠졌을까?

```javascript
class Button extends React.Component {

  constructor(props) {
    super(props);
    // 여기에 무엇이 빠졌을까?
  }

  handleClick() {...}
}
```

- [ ] this.handleClick.bind(this);
- [ ] props.bind(handleClick);
- [ ] this.handleClick.bind();
- [x] this.handleClick = this.handleClick.bind(this);

#### Q51. React는 인접한 두 엘리먼트를 Fragment로 감싸지 않으면 렌더링하지 않는다. 아래는 Fragment를 렌더링하는 한 방법이다. 같은 결과를 내는 더 짧은 문법은?

```javascript
<React.Fragment>
  <h1>Our Staff</h1>
  <p>Our staff is available 9-5 to answer your questions</p>
</React.Fragment>
```

- [ ] A

```javascript
<...>
  <h1>Our Staff</h1>
  <p>Our staff is available 9-5 to answer your questions</p>
</...>
```

- [ ] B

```javascript
<//>
  <h1>Our Staff</h1>
  <p>Our staff is available 9-5 to answer your questions</p>
<///>
```

- [x] C

```javascript
<>
  <h1>Our Staff</h1>
  <p>Our staff is available 9-5 to answer your questions</p>
</>
```

- [ ] D

```javascript
<Frag>
  <h1>Our Staff</h1>
  <p>Our staff is available 9-5 to answer your questions</p>
</Frag>
```


#### Q52. state 변수 count의 값을 보여주려면 h1 엘리먼트의 중괄호 안에 무엇을 넣어야 할까?

```javascript
class Ticker extends React.Component {
  constructor(props) {
    super(props);
    this.state = { count: 0 };
  }
  render() {
    return <h1>{}</h1>;
  }
}
```

- [x] this.state.count
- [ ] count
- [ ] state
- [ ] state.count

#### Q53. 다음 코드에서 greeting 변수에 Hello 컴포넌트가 할당되는 시점은?

```javascript
const greeting = isLoggedIn ? <Hello /> : null;
```

- [ ] 절대 할당되지 않는다
- [x] isLoggedIn이 true일 때
- [ ] 사용자가 로그인할 때
- [ ] Hello 함수가 호출될 때

#### Q54. 다음 코드에서 orderNumber 속성이 받는 값의 타입은?

```javascript
ReactDOM.render(<Message orderNumber="16" />, document.getElementById('root'));
```

- [x] string
- [ ] boolean
- [ ] object
- [ ] number

#### Q55. h1 엘리먼트에 style 속성을 추가했는데, 실행하면 예상치 못한 토큰 에러가 난다. 어떻게 고쳐야 할까?

```javascript
const element = <h1 style={ backgroundColor: "blue" }>Hi</h1>;
```

- [ ] `const element = <h1 style="backgroundColor: "blue"">Hi</h1>;`
- [x] `const element = <h1 style={{backgroundColor: "blue"}}>Hi</h1>;`
- [ ] `const element = <h1 style={blue}>Hi</h1>;`
- [ ] `const element = <h1 style="blue">Hi</h1>;`

#### Q56. React 클래스 컴포넌트에서 state 변수를 갱신할 때 사용하는 함수는?

- [ ] `replaceState`
- [ ] `refreshState`
- [ ] `updateState`
- [x] `setState`

#### Q57. 다음 컴포넌트에서 Star 아이콘의 기본 색상은?

```javascript
const Star = ({ selected = false }) => <Icon color={selected ? 'red' : 'grey'} />;
```

- [ ] black
- [ ] red
- [x] grey
- [ ] white

#### Q58. this.handleClick이 제대로 바인딩되지 않았다고 가정할 때, 다음 두 버튼의 onClick 동작에는 어떤 차이가 있을까?

```javascript
A. <button onClick=this.handleClick>Click Me</button>
B. <button onClick={event => this.handleClick(event)}>Click Me</button>
```

- [ ] A 버튼은 onClick 이벤트 참조에 접근할 수 없다
- [x] A 버튼은 제대로 실행되지 않는다
- [ ] 차이가 없다, 둘 다 성공적으로 실행된다
- [ ] B 버튼은 제대로 실행되지 않는다

#### Q59. 다음 React Router 코드에서, 이 라우트가 활성화됐을 때 About 컴포넌트를 렌더링하려면 어떻게 추가해야 할까?

```javascript
<Route path="/:id" />
```

- [x] A

```javascript
<Route path="/:id">
  {' '}
  <About />
</Route>
```

- [ ] B

```javascript
<Route path="/tid" about={Component} />
```

- [ ] C

```javascript
<Route path="/:id" route={About} />
```

- [ ] D

```javascript
<Route>
  <About path="/:id" />
</Route>
```


#### Q60. 다음 함수 컴포넌트와 동등한 클래스 컴포넌트는?

```javascript
const Greeting = ({ name }) => <h1>Hello {name}!</h1>;
```

- [ ] A

```javascript
class Greeting extends React.Component {
  constructor() {
    return <h1>Hello {this.props.name}!</h1>;
  }
}
```

- [ ] B

```javascript
class Greeting extends React.Component {
  <h1>Hello {this.props.name}!</h1>;
}
```

- [x] C

```javascript
class Greeting extends React.Component {
  render() {
    return <h1>Hello {this.props.name}!</h1>;
  }
}
```

- [ ] D

```javascript
class Greeting extends React.Component {
  render({ name }) {
    return <h1>Hello {name}!</h1>;
  }
}
```


#### Q61. 다음 코드에서 함수에 넘긴 두 번째 인자는 무엇을 의미할까?

```javascript
ReactDOM.render(
  <h1>Hi</h1>,
  document.getElementById('root')
)
```

- [x] React가 자신의 엘리먼트를 DOM에 추가해야 할 대상 엘리먼트
- [ ] 함수를 호출할 위치
- [ ] root 엘리먼트의 위치
- [ ] 새 자바스크립트를 만들 위치

#### Q62. HTML의 `<a>` 태그 대신 React Router의 Link 컴포넌트를 써야 하는 이유는?

- [ ] Link 엘리먼트를 쓰면 사용자가 브라우저의 '뒤로 가기' 버튼을 쓸 수 있게 되기 때문에
- [ ] 차이가 없다, Link 엘리먼트는 `<a>` 태그와 동의어다
- [ ] `<a>` 태그는 React와 함께 쓰면 에러를 일으키기 때문에
- [x] `<a>` 태그는 페이지 전체를 새로고침시키지만, Link 컴포넌트는 그렇지 않기 때문에

#### Q63. createElement 함수에 넘기는 첫 번째 인자 x는 무엇일까?

```javascript
React.createElement(x, y, z);
```

- [x] 생성될 엘리먼트(타입)
- [ ] 이 엘리먼트가 페이지에 생성돼야 할 순서
- [ ] 엘리먼트의 속성
- [ ] 엘리먼트 안에 표시돼야 할 정보

#### Q64. 다음 훅과 같은 시점에 호출되는 클래스 컴포넌트의 생명주기 메서드는?

```javascript
useEffect(() => {
  // do things
}, []);
```

- [ ] componentWillUnmount
- [x] componentDidMount
- [ ] render
- [ ] componentDidUpdate

#### Q65. 이 컴포넌트가 상속하는 기반 컴포넌트의 이름은?

```javascript
class Comp extends React.Component {
  render() {
    return <h1>Look at the time: {time}</h1>;
  }
}
```

- [ ] Comp
- [ ] h1
- [ ] React.Component
- [x] Component

#### Q66. Portal을 사용할 때 첫 번째 인자에는 무엇이 들어갈까?

```javascript
ReactDOM.createPortal(x, y);
```

- [ ] 현재 state
- [x] 렌더링할 엘리먼트
- [ ] App 컴포넌트에 대한 참조
- [ ] 페이지 전체

설명: [Portals](https://reactjs.org/docs/portals.html)

#### Q67. 다음 코드에서 setCount는 무엇일까?

```javascript
const [count, setCount] = useState(0);
```

- [ ] state의 초기값
- [ ] 그냥 변수
- [ ] state 객체 자체
- [x] state 값을 바꾸는 콜백 함수

설명: [Hooks-State](https://reactjs.org/docs/hooks-state.html#:~:text=If%20we%20want%20to%20update%20the%20current)

#### Q68. 아래 코드에서 map 함수는 어떤 역할을 할까?

```javascript
const database = [{ data: 1 }, { data: 2 }, { data: 3 }];
database.map((user) => <h1>{user.data}</h1>);
```

- [ ] database의 모든 항목을 담은 맵(map) 자료구조를 반환한다
- [x] database의 각 항목마다, 그 data를 텍스트로 담은 h1 엘리먼트를 하나씩 만들어 반환한다
- [ ] database의 모든 항목을 담은 h1 엘리먼트 하나를 반환한다
- [ ] database의 어떤 항목이 h1에 표시하기 적합한지 검사한다

#### Q69. 다음 코드에서 벌어지는 일을 가장 정확히 설명하면?

```javascript
const { name: firstName } = person;
```

- [ ] firstName 객체와 같은 name 프로퍼티를 가진 새 객체를 만든다
- [ ] person 객체의 firstName 프로퍼티 값을 name이라는 상수에 할당한다
- [ ] person.name.firstName의 값을 가져온다
- [x] person 객체의 name 프로퍼티 값을 firstName이라는 상수에 할당한다

#### Q70. 다음 코드의 문제는 무엇일까?

```javascript
const MyComponent = ({ names }) => (
  <h1>Hello</h1>
  <p>Hello again</p>
);
```

- [ ] React 컴포넌트는 함수로 정의할 수 없다
- [x] React는 함수 컴포넌트가 두 개 이상의 엘리먼트를 반환하는 것을 허용하지 않는다
- [ ] 컴포넌트는 엘리먼트를 반환하려면 return 키워드를 써야 한다
- [ ] 문자열은 따옴표로 감싸야 한다

#### Q71. Portal을 사용할 때 두 번째 인자는 무엇일까?

```javascript
ReactDOM.createPortal(x, y);
```

- [ ] App 컴포넌트
- [ ] 페이지 전체
- [ ] 현재 state
- [x] 부모 엘리먼트 바깥에 존재하는 DOM 엘리먼트

#### Q72. 다음 코드에서 `<h1>` 태그 안에는 무엇이 렌더링될까?

```javascript
const MyComponent = ({ children }) => (
  <h1>{children.length}</h1>
);
...
<MyComponent>
<p>Hello</p>
<p>Goodbye</p>
</MyComponent>
```

- [ ] "cannot read property 'length' of undefined" 에러
- [ ] 1
- [ ] undefined
- [x] 2

#### Q73. 다음과 같은 할당 패턴을 무엇이라고 부를까?

```javascript
const [count, setCount] = useState(0);
```

- [ ] 객체 구조 분해
- [x] 배열 구조 분해
- [ ] 스프레드 연산자
- [ ] 코드 푸시

#### Q74. 기본적인 React 프로젝트에서 브라우저가 가장 먼저 불러오는 파일은?

- [ ] src/App.js
- [ ] src/index.js
- [ ] public/manifest.json
- [x] public/index.html

#### Q75. 다음 코드는 아무것도 렌더링하지 않고 "ReactDOM is not defined."라는 에러가 난다. 어떻게 해결할까?

```javascript
import React from 'react';
import { render } from 'reactjs-dom';

const element = <h1>Hi</h1>;

ReactDOM.render(element, document.getElementById('root'));
```

- [x] render(element, document.getElementById("root"));
- [ ] ReactDOM(element, document.getElementById("root"));
- [ ] renderDOM(element, document.getElementById("root"));
- [ ] DOM(element, document.getElementById("root"));

#### Q76. 다음 컴포넌트에서 사용자의 로그인 여부를 표시하려면 어떻게 해야 할까?

```javascript
render() {
  const isLoggedIn = this.state.isLoggedIn;
  return (
    <div>
      The user is:
    </div>
  );
}
```

- [ ] The user is loggedIn ? logged in : not logged in.
- [ ] 사용자의 로그인 여부를 판단하는 함수를 따로 작성해야 한다
- [ ] `The user is {isLoggedIn = "no"}.`
- [x] `The user is {isLoggedIn ? "logged in." : "not logged in"}.`

#### Q77. React에서 리스트를 렌더링할 때 콘솔에 "Warning: Each child in a list should have a unique 'key' prop."라는 경고가 뜬다. 어떻게 해결할까?

- [ ] 각 항목의 이름을 key 값으로 넘긴다
- [ ] 리스트의 모든 항목에 같은 값의 key를 추가한다
- [ ] 콘솔의 경고 메시지를 지운다
- [x] 리스트의 각 항목에 그 항목과 연관된 고유한 값을 key로 추가한다

#### Q78. 바지를 모으는 새 앱을 위한 보일러플레이트 코드를 만들려면 어떤 명령을 쓸까?

- [ ] npm create-react-app collect-pantalones
- [ ] npx start-app collect-pantalones
- [ ] react new collect-pantalones
- [x] npx create-react-app collect-pantalones

설명: [Create React App](https://reactjs.org/docs/create-a-new-react-app.html#create-react-app)

#### Q79. 버튼을 클릭하면 광자 어뢰를 발사하도록 코드를 완성하면?

```javascript
class StarTrekkin extends React.Component {
  firePhotonTorpedoes(e) {
    console.log('pew pew');
  }
  render() {
    return; // 여기에 코드를 추가해야 한다
  }
}
```

- [ ] `<button onClick={firePhotonTorpedoes()}>Pew Pew</button>`
- [ ] `<button onClick={firePhotonTorpedoes}>Pew Pew</button>`
- [ ] `<button onClick={this.firePhotonTorpedoes()}>Pew Pew</button>`
- [x] `<button onClick={this.firePhotonTorpedoes}>Pew Pew</button>`

설명: [Handling Events](https://reactjs.org/docs/handling-events.html)

#### Q80. 업데이트가 필요한지 아닌지를 판단하는 과정을 무엇이라고 부를까?

- [ ] 섀도우 DOM
- [ ] 파이버(fiber)
- [x] 재조정(reconciliation)
- [ ] state 정의

#### Q81. React는 오픈소스 프로젝트지만, 어느 회사가 관리하고 있을까?

- [ ] Intuit
- [ ] Twitter
- [x] Facebook
- [ ] Snapchat

#### Q82. React 프로젝트를 만들 때 사용할 수 있는 명령은?

- [ ] react-starter
- [x] create-react-app
- [ ] react-gen
- [ ] react-start

#### Q83. React 개발자들이 앱을 디버깅할 때 사용하는 브라우저 확장 프로그램은?

- [x] React Developer Tools
- [ ] React Tooling Add-on
- [ ] React Codewatch
- [ ] React Debug

#### Q84. 다음 중 Create React App에 포함되지 않는 도구는?

- [ ] React
- [x] jQuery
- [ ] webpack
- [ ] ReactDOM

#### Q85. React 엘리먼트를 만들 때 흔히 쓰이는 자바스크립트 문법 확장은?

- [ ] HTML
- [ ] JavaScriptX
- [x] JSX
- [ ] React JavaScript

#### Q86. Flow나 TypeScript를 쓰지 않고 props의 타입을 검사하려면 어떻게 할까?

- [ ] 수동으로 직접 검사한다
- [ ] prop-helper를 사용한다
- [x] prop-types를 사용한다
- [ ] checker-types를 사용한다

#### Q87. 다음 h1 엘리먼트에 id "heading"을 추가하려면 어떻게 해야 할까?

```javascript
let dish = <h1>Mac and Cheese</h1>;
```

- [ ] `let dish = <h1 id={heading}>Mac and Cheese</h1>;`
- [x] `let dish = <h1 id="heading">Mac and Cheese</h1>;`
- [ ] `let dish = <h1 id:"heading">Mac and Cheese</h1>;`
- [ ] `let dish = <h1 class="heading">Mac and Cheese</h1>;`

#### Q88. 포옹할 사람의 이름을 버튼에 전달하려면 button 값에 무엇을 넣어야 할까?

```javascript
class Huggable extends React.Component {
  hug(id) {
    console.log("hugging " + id);
  }
  render() {
    let name = "kitten";
    let button = // 코드가 빠져 있다
    return button;
  }
}
```

- [ ] `<button onClick={(name) => this.hug(name)}>Hug Button</button>;`
- [ ] `<button onClick={this.hug(e, name)}>Hug Button</button>;`
- [ ] `<button onClick={(e) => hug(name, e)}>Hug Button</button>;`
- [x] `<button onClick={(e) => this.hug(name, e)}>Hug Button</button>;`

**설명:**
이 문제는 클래스 컴포넌트에 대한 지식을 테스트한다. 클래스 컴포넌트에 정의된 메서드를 호출하려면 this를 사용해야 한다.

#### Q89. React에서 컴포넌트를 만들 때 쓰는 문법은?

- [ ] generator
- [x] 함수 또는 클래스
- [ ] 서비스 워커
- [ ] 태그

설명: [컴포넌트와 props](https://reactjs.org/docs/components-and-props.html)

#### Q90. 버튼을 비활성화해서 onClick 이벤트가 발생하지 않게 하려면 어떤 속성을 사용할까?

- [ ] onBlur
- [ ] onPress
- [ ] defaultValue
- [x] disabled

#### Q91. 다음 함수 컴포넌트를 가장 잘 설명하는 것은?

```javascript
function Dish() {
  return (
    <>
      <Ingredient />
      <Ingredient />
    </>
  );
}
```

- [ ] 자식 컴포넌트다
- [x] 부모 컴포넌트다
- [ ] 중첩 컴포넌트다
- [ ] 인접 컴포넌트다

#### Q92. 클래스 컴포넌트에서 componentDidMount 메서드는 언제 실행될까?

- [x] DOM에 추가된 직후
- [ ] DOM에 추가되기 전
- [ ] 업데이트된 직후 즉시
- [ ] API 호출이 끝난 뒤

#### Q93. webpack은 어떤 용도로 사용할까?

- [ ] 앱이 사용하는 외부 의존성을 찾기 위해
- [x] 앱을 더 작은 코드 덩어리로 나눠서 브라우저가 더 쉽게 불러올 수 있게 하기 위해
- [ ] 코드를 읽기 좋게 포맷팅하기 위해
- [ ] 앱을 악성 코드 주입으로부터 보호하기 위해

#### Q94. 크롬 확장 프로그램 React Developer Tools를 사용할 때, 아이콘이 빨간색이면 무엇을 의미할까?

- [x] 앱이 개발(development) 버전으로 실행되고 있다
- [ ] 앱이 프로덕션 버전으로 실행되고 있다
- [ ] webpack이 사용되고 있다
- [ ] Create React App이 사용되고 있다

설명: [React Developer Tools 아이콘 색상](https://teamtreehouse.com/community/hey-why-the-logo-of-react-developer-tools-appears-in-red)

#### Q95. 다음 에러를 피하려면 생성자를 어떻게 고쳐야 할까? "ReferenceError: Must call super constructor in derived class before accessing 'this'..."

```javascript
class TransIsBeautiful extends React.Component {
  constructor(props){
  // 빠진 줄....
  console.log(this) ;
  }
  ...
}
```

- [ ] render(props);
- [x] super(props);
- [ ] super(this);
- [ ] this.super();

#### Q96. React와 함께 사용할 수 없는 언어는?

- [x] Swift
- [ ] JSX
- [ ] JavaScript
- [ ] TypeScript

#### Q97. 포켓몬을 모으는 앱의 일부인 다음 코드에서, 지금까지 모은 포켓몬 목록을 출력하려면 어떻게 해야 할까?

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

설명: [React 클래스 컴포넌트 state 관리](https://www.digitalocean.com/community/tutorials/how-to-manage-state-on-react-class-components#step-3-setting-state-from-a-static-value)

#### Q98. 다음 코드를 실행하면 결과는 무엇일까?

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

#### Q99. React.createRef를 사용해야 하는 이유는?

- [ ] 다른 JS 파일을 참조하기 위해
- [ ] 함수를 바인딩하기 위해
- [ ] 함수를 호출하기 위해
- [x] DOM 노드에 직접 접근하기 위해

설명: [Refs and the DOM](https://reactjs.org/docs/refs-and-the-dom.html)

#### Q100. 다음 코드에서 사용된 할당 패턴은?

```javascript
const { tree, lake } = nature;
```

- [ ] 함수 기본값(function defaults)
- [ ] 배열 구조 분해
- [ ] PRPL 패턴
- [x] 객체 구조 분해

설명: [Destructuring assignment](https://javascript.info/destructuring-assignment)

#### Q101. 다음 코드를 고쳐서 sent 속성이 불리언 값 false를 갖도록 하려면?

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

