## React.js

#### Q1. Якщо потрібно імпортувати лише компонент з бібліотеки React, який синтаксис використовується?

- [ ] `import React.Component from 'react'`
- [ ] `import [ Component ] from 'react'`
- [ ] `import Component from 'react'`
- [x] `import { Component } from 'react'`

#### Q2. Якщо функціональний компонент завжди повинен рендеритись однаково за однакових пропсів, яка проста оптимізація продуктивності доступна для нього?

- [x] Обгорнути його у вищий компонент `React.memo`.
- [ ] Реалізувати хук `useReducer`.
- [ ] Реалізувати хук `useMemo`.
- [ ] Реалізувати метод життєвого циклу `shouldComponentUpdate`.

#### Q3. Як виправити синтаксичну помилку, що виникає при виконанні цього коду?

```javascript
const person =(firstName, lastName) =>
{
  first: firstName,
  last: lastName
}
console.log(person("Jill", "Wilson"))
```

- [x] Обгорнути об'єкт у дужки.
- [ ] Викликати функцію з іншого файлу.
- [ ] Додати оператор return перед першою фігурною дужкою.
- [ ] Замінити об'єкт на масив.

#### Q4. Якщо в файлі є наступний імпорт, що використовується для керування станом у компоненті?

`import React, {useState} from 'react';`

- [x] React Hooks
- [ ] stateful компоненти
- [ ] математика
- [ ] класові компоненти

#### Q5. Використовуючи покращення об'єктних літералів, можна повернути значення назад в об'єкт. Який результат буде виведено в консоль при логуванні person?

```javascript
const name = 'Rachel';
const age = 31;
const person = { name, age };
console.log(person);
```

- [ ] `{{name: "Rachel", age: 31}}`
- [x] `{name: "Rachel", age: 31}`
- [ ] `{person: "Rachel", person: 31}}`
- [ ] `{person: {name: "Rachel", age: 31}}`

#### Q6. Яка бібліотека для тестування найчастіше асоціюється з React?

- [ ] Mocha
- [ ] Chai
- [ ] Sinon
- [x] Jest

[Довідка](https://jestjs.io/uk/)

#### Q7. Щоб отримати перший елемент масиву ("cooking") за допомогою деструктуризації масиву, як потрібно змінити цей рядок?

```javascript
const topics = ['cooking', 'art', 'history'];
```

- [ ] `const first = ["cooking", "art", "history"]`
- [ ] `const [] = ["cooking", "art", "history"]`
- [ ] `const [, first]["cooking", "art", "history"]`
- [x] `const [first] = ["cooking", "art", "history"]`

#### Q8. Як передавати дані через дерево компонентів, не передаючи пропси вручну на кожному рівні?

- [ ] React Send
- [ ] React Pinpoint
- [ ] React Router
- [x] React Context

[Довідка](https://uk.react.dev/reference/react/useContext)

#### Q9. Що буде виведено в консоль при виконанні наступного коду?

```javascript
const [, , animal] = ['Horse', 'Mouse', 'Cat'];
console.log(animal);
```

- [ ] Horse
- [x] Cat
- [ ] Mouse
- [ ] undefined

#### Q10. Як називається інструмент, який перетворює JSX у виклики createElement?

- [ ] JSX Editor
- [ ] ReactDOM
- [ ] Browser Buddy
- [x] Babel

#### Q11. Чому може бути корисно використовувати useReducer замість useState у React-компоненті?

- [ ] коли потрібно замінити Redux
- [x] коли потрібно керувати складнішим станом у застосунку
- [ ] коли потрібно покращити продуктивність
- [ ] коли потрібно зламати ваш застосунок у продакшені

#### Q12. Які пропси з об'єкта props доступні компоненту з наступним синтаксисом?

```javascript
<Message {...props} />
```

- [ ] будь-які, що не змінилися
- [x] усі
- [ ] дочірні пропси
- [ ] будь-які, що змінилися

#### Q13. Розгляньте наступний код з React Router. Як називається :id у властивості path?

```javascript
<Route path="/:id" />
```

- [ ] Це модаль маршруту
- [x] Це параметр маршруту
- [ ] Це розділювач маршруту
- [ ] Це посилання маршруту

#### Q14. Якщо створено компонент під назвою Dish і його рендерять у DOM, який тип елемента буде відрендерено?

```javascript
function Dish() {
  return <h1>Mac and Cheese</h1>;
}

ReactDOM.render(<Dish />, document.getElementById('root'));
```

- [ ] `div`
- [ ] section
- [ ] компонент
- [x] `h1`

#### Q15. Як виглядає цей React-елемент, враховуючи наступний код?

```javascript
React.createElement('h1', null, "What's happening?");
```

- [ ] `<h1 props={null}>What's happening?</h1>`
- [x] `<h1>What's happening?</h1>`
- [ ] `<h1 id="component">What's happening?</h1>`
- [ ] `<h1 id="element">What's happening?</h1>`

[Довідка](https://uk.react.dev/reference/react/createElement)

#### Q16. Яку властивість потрібно додати до компонента Suspense, щоб відобразити спінер або стан завантаження?

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

[Довідка](https://uk.react.dev/reference/react/Suspense)

#### Q17. Як би ви описали змінну message, обгорнуту в фігурні дужки нижче?

```javascript
const message = 'Hi there';
const element = <p>{message}</p>;
```

- [ ] JS-функція
- [ ] JS-елемент
- [x] JS-вираз
- [ ] JSX-обгортка

#### Q18. Що можна використовувати для обробки розбиття коду?

- [ ] `React.memo`
- [ ] `React.split`
- [x] `React.lazy`
- [ ] `React.fallback`

[Довідка](https://uk.react.dev/reference/react/lazy#reference)

#### Q19. Коли використовується `useLayoutEffect`?

- [ ] для оптимізації для всіх пристроїв
- [ ] для завершення оновлення
- [x] для зміни компонування екрана
- [ ] коли потрібно, щоб браузер відмалював перед запуском ефекту

[Джерело](https://uk.react.dev/reference/react/useLayoutEffect)
"useLayoutEffect — це версія useEffect, яка викликається перед тим, як браузер перемалює екран."

[Довідка] Правильна відповідь на запитання "Коли використовувати useLayoutEffect?" така:

Коли потрібно змінити верстку екрана.

useLayoutEffect використовується, коли потрібно виконати зміни в DOM, що залежать від оновленого компонування елементів. Він дозволяє вносити зміни в DOM синхронно перед тим, як браузер виконає етап малювання. Це може бути корисно, коли потрібно виміряти або маніпулювати версткою, наприклад, отримати розміри або позиції елементів, розрахувати зсуви прокрутки або виконати інші операції, що потребують актуальної інформації про верстку.

Інший варіант відповіді є неточним:

"Коли потрібно, щоб браузер перемалював перед запуском ефекту" — це неправильно. Мета useLayoutEffect полягає в тому, щоб виконати ефект синхронно після оновлення DOM, але перед тим, як браузер перемалює, дозволяючи вносити зміни, пов'язані з версткою, до того, як відбудеться візуалізація.

**Пояснення:**
`useLayoutEffect` виконується _перед_ хуком `useEffect`, не зважаючи на мутації DOM. Хоча хук React `useLayoutEffect` встановлюється після хука `useEffect`, він викликається першим!

#### Q20. У чому різниця між поведінкою при клацанні цих двох кнопок (за умови, що this.handleClick правильно прив'язаний)?

```javascript
A. <button onClick={this.handleClick}>Click Me</button>
B. <button onClick={event => this.handleClick(event)}>Click Me</button>
```

- [ ] Кнопка A не матиме доступу до об'єкта події при кліку на кнопку.
- [ ] Кнопка B не викличе обробник this.handleClick успішно.
- [ ] Кнопка A не викличе обробник this.handleClick успішно.
- [x] Немає різниці.

#### Q21. Як деструктурувати властивості, що передаються до компонента Dish?

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

#### Q22. Коли можна використовувати `React.PureComponent`?

- [ ] коли не хочеться, щоб компонент мав пропси
- [ ] коли є компоненти-сиблінги, які потрібно порівняти
- [x] коли потрібна типова реалізація `shouldComponentUpdate()`
- [ ] коли не хочеться, щоб компонент мав стан

[Довідка](https://uk.react.dev/reference/react/PureComponent)

#### Q23. Чому важливо уникати копіювання значень пропсів у стан компонента, де це можливо?

- [ ] тому що ніколи не слід мутувати стан
- [ ] тому що `getDerivedStateFromProps()` — це небезпечний метод для використання
- [x] тому що потрібно дозволити компоненту оновлюватися у відповідь на зміни пропсів
- [ ] тому що потрібно дозволити даним передаватися назад до батьківського компонента

#### Q24. Що таке проп children?

- [ ] властивість, яка додає дочірні компоненти до стану
- [x] спеціальна властивість, яку JSX створює для компонентів, що містять як відкривальний, так і закривальний тег, посилаючись на їхній вміст.
- [ ] властивість, яка дозволяє встановити масив як властивість
- [ ] властивість, яка дозволяє передавати дані дочірнім елементам

[Довідка](https://uk.react.dev/reference/react/Children)

#### Q25. Який атрибут є заміною innerHTML у React для використання в DOM браузера?

- [ ] injectHTML
- [x] dangerouslySetInnerHTML
- [ ] weirdSetInnerHTML
- [ ] strangeHTML

[Довідка](https://uk.react.dev/reference/react-dom/components/common#dangerously-setting-the-inner-html)

#### Q26. Які з цих термінів зазвичай описують React-застосунки?

- [x] декларативні
- [ ] інтегровані
- [ ] закриті
- [ ] імперативні

[Довідка](https://uk.react.dev/learn/reacting-to-input-with-state#how-declarative-ui-compares-to-imperative)

#### Q27. Чому при використанні webpack потрібно використовувати loader?

- [ ] щоб зібрати фізичні папки файлів
- [x] для попередньої обробки файлів
- [ ] для завантаження зовнішніх даних
- [ ] для завантаження вебсайту на телефони всіх користувачів

#### Q28. Як називається представлення інтерфейсу користувача, яке зберігається в пам'яті та синхронізується з "реальним" DOM?

- [x] віртуальний DOM
- [ ] DOM
- [ ] віртуальні елементи
- [ ] shadow DOM

#### Q29. Ви написали наступний код, але нічого не рендериться. Як виправити цю проблему?

```javascript
const Heading = () => {
  <h1>Hello!</h1>;
};
```

- [ ] Додати функцію render.
- [x] Змінити фігурні дужки на круглі або додати оператор return перед тегом `h1`.
- [ ] Перемістити `h1` в інший компонент.
- [ ] Обгорнути `h1` в `div`.

#### Q30. Яке ключове слово використовується для створення константи в JavaScript?

- [x] const
- [ ] let
- [ ] constant
- [ ] var

#### Q31. Як називається React-компонент, який перехоплює помилки JavaScript у будь-якому місці дерева дочірніх компонентів?

- [ ] error bosses
- [ ] error catchers
- [ ] error helpers
- [x] error boundaries

[Довідка](https://uk.react.dev/reference/react/useTransition#displaying-an-error-to-users-with-error-boundary)

#### Q32. У якому методі життєвого циклу робляться запити на дані в класовому компоненті?

- [ ] constructor
- [x] componentDidMount
- [ ] componentWillReceiveProps
- [ ] componentWillMount

[Довідка](https://uk.react.dev/reference/react/Component#componentdidmount)

#### Q33. React-компоненти складаються для створення інтерфейсу користувача. Як саме компоненти складаються?

- [ ] шляхом розміщення їх в одному файлі
- [x] шляхом вкладення компонентів
- [ ] за допомогою webpack
- [ ] за допомогою розбиття коду

#### Q34. Усі React-компоненти повинні діяти як **\_** щодо своїх пропсів.

- [ ] монади
- [x] чисті функції
- [ ] рекурсивні функції
- [ ] функції вищого порядку

#### Q35. Як називається `[e.target.id]` у цьому фрагменті коду?

```javascript
const handleChange = (e) => {
  setState((prevState) => ({ ...prevState, [e.target.id]: e.target.value }));
};
```

- [ ] обчислювана назва властивості
- [ ] встановлене значення
- [x] динамічний ключ
- [ ] рядок коду JSX

[Довідка](https://www.geeksforgeeks.org/how-to-set-state-with-a-dynamic-key-name-in-reactjs/)

#### Q36. Як називається цей компонент?

```javascript
class Clock extends React.Component {
  render() {
    return <h1>Look at the time: {time}</h1>;
  }
}
```

- [x] Clock
- [ ] Він не має властивості name.
- [ ] React.Component
- [ ] Component

#### Q37. Що передається у функцію `Array.map()`?

- [x] функція зворотного виклику, яка викликається один раз для кожного елемента масиву
- [ ] назва іншого масиву для ітерації
- [ ] кількість разів, яку потрібно викликати функцію
- [ ] рядок, що описує, що повинна робити функція

#### Q38. Чому краще передавати функцію в `setState`, а не об'єкт?

- [ ] Це забезпечує кращу інкапсуляцію.
- [ ] Це гарантує, що об'єкт не буде змінено.
- [ ] Це автоматично оновлює компонент.
- [x] `setState` є асинхронним і може призвести до несинхронних значень.

[Довідка](https://medium.com/@wisecobbler/using-a-function-in-setstate-instead-of-an-object-1f5cfd6e55d1)

**Пояснення:** Оскільки `this.props` і `this.state` можуть оновлюватися асинхронно, не слід покладатися на їхні значення для обчислення наступного стану.

#### Q39. Який пакет містить функцію render(), що рендерить дерево React-елементів у DOM?

- [ ] `React`
- [x] `ReactDOM`
- [ ] `Render`
- [ ] `DOM`

#### Q40. Як встановити усталені значенні для неконтрольованого поля форми?

- [ ] Скористатися `value`.
- [x] Скористатися `defaultValue`.
- [ ] Скористатися `default`.
- [ ] Воно призначається автоматично.

#### Q41. Що потрібно змінити в цьому коді, щоб він працював?

```js
const clock = (props) => {
  return <h1>Look at the time: {props.time}</h1>;
};
```

- [ ] Додати лапки навколо значення, що повертається
- [ ] Видалити `this`
- [ ] Видалити метод `render`
- [x] Зробити `clock` з великої літери

[Довідка](https://uk.legacy.reactjs.org/docs/jsx-in-depth.html#html-tags-vs-react-components)

**Пояснення:** У JSX теги з малої літери вважаються HTML-тегами.

#### Q42. Який хук можна використовувати для оновлення заголовка документа?

- [x] `useEffect(function updateTitle() { document.title = name + ' ' + lastname; });`
- [ ] `useEffect(() => { title = name + ' ' + lastname; });`
- [ ] `useEffect(function updateTitle() { name + ' ' + lastname; });`
- [ ] `useEffect(function updateTitle() { title = name + ' ' + lastname; });`

#### Q43. Яку функцію з React можна використовувати для обгортання імпортів компонентів для їх лінивого завантаження?

- [ ] `fallback`
- [ ] `split`
- [x] `lazy`
- [ ] `memo`

[Довідка](https://uk.react.dev/reference/react/lazy#lazy)

#### Q44. Як викликати setDone тільки при монтуванні компонента, використовуючи хуки?

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

#### Q45. Зараз handleClick викликається замість того, щоб передаватися як посилання. Як це виправити?

```javascript
<button onClick={this.handleClick()}>Click this</button>
```

- [ ] `<button onClick={this.handleClick.bind(handleClick)}>Click this</button>`
- [ ] `<button onClick={handleClick()}>Click this</button>`
- [x] `<button onClick={this.handleClick}>Click this</button>`
- [ ] `<button onclick={this.handleClick}>Click this</button>`

#### Q46. Яка відповідь найкраще описує функціональний компонент?

- [ ] Функціональний компонент такий самий, як класовий компонент.
- [x] Функціональний компонент приймає один об'єкт props і повертає React-елемент.
- [ ] Функціональний компонент — це єдиний спосіб створити компонент.
- [ ] Функціональний компонент обов'язковий для створення React-компонента.

#### Q47. З якої бібліотеки походить функція `fetch()`?

- [ ] FetchJS
- [ ] ReactDOM
- [x] Жодної бібліотеки. `fetch()` підтримується більшістю браузерів.
- [ ] React

#### Q48. Що станеться, коли цей хук useEffect буде виконано, за умови, що name ще не дорівнює John?

```javascript
useEffect(() => {
  setName('John');
}, [name]);
```

- [ ] Це негайно викличе помилку.
- [ ] Код всередині функції буде виконано, але тільки після очікування, щоб переконатися, що жоден інший компонент не звертається до змінної name.
- [x] Значення name буде оновлено один раз і більше не виконуватиметься, поки name не зміниться ззовні.
- [ ] Це викличе нескінченний цикл.

#### Q49. Що не викличе повторного рендерингу React-компонента?

- [ ] якщо компонент викликає `this.setState(...)`
- [ ] якщо значення одного з пропсів компонента змінюється
- [ ] якщо компонент викликає `this.forceUpdate()`
- [x] якщо один із сиблінгів компонента повторно рендериться

#### Q50. Ви створили новий метод у класовому компоненті під назвою handleClick, але він не працює. Який код відсутній?

```javascript
class Button extends React.Component{

  constructor(props) {
    super(props);
    // Відсутній рядок
  }

  handleClick() {...}
}
```

- [ ] `this.handleClick.bind(this);`
- [ ] `props.bind(handleClick);`
- [ ] `this.handleClick.bind();`
- [x] `this.handleClick = this.handleClick.bind(this);`

#### Q51. React не рендерить два сиблінг-елементи, якщо вони не обгорнуті у фрагмент. Нижче наведено один зі способів рендерингу фрагмента. Яка скорочена форма для цього?

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

#### Q52. Якщо потрібно відобразити значення стану `count` у компоненті, що потрібно додати в фігурні дужки в `h1`?

```javascript
class Ticker extends React.component {
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

#### Q53. Згідно з наступним кодом, коли компонент Hello призначається змінній `greeting`?

```javascript
const greeting = isLoggedIn ? <Hello /> : null;
```

- [ ] ніколи
- [x] коли `isLoggedIn` дорівнює true
- [ ] коли користувач входить в систему
- [ ] коли викликається функція Hello

#### Q54. У наступному блоці коду, якого типу змінна `orderNumber`?

```javascript
ReactDOM.render(<Message orderNumber="16" />, document.getElementById('root'));
```

- [x] рядок
- [ ] булеве значення
- [ ] об'єкт
- [ ] число

#### Q55. Ви додали властивість стилю до `h1`, але виникає помилка неочікуваного токена під час виконання. Як це виправити?

```javascript
const element = <h1 style={ backgroundColor: "blue" }>Hi</h1>;
```

- [ ] `const element = <h1 style="backgroundColor: "blue""}>Hi</h1>;`
- [x] `const element = <h1 style={{backgroundColor: "blue"}}>Hi</h1>;`
- [ ] `const element = <h1 style={blue}>Hi</h1>;`
- [ ] `const element = <h1 style="blue">Hi</h1>;`

#### Q56. Яка функція використовується для оновлення змінних стану в класовому компоненті React?

- [ ] `replaceState`
- [ ] `refreshState`
- [ ] `updateState`
- [x] `setState`

#### Q57. Розгляньте наступний компонент. Який колір зірки за замовчуванням?

```javascript
const Star = ({ selected = false }) => <Icon color={selected ? 'red' : 'grey'} />;
```

- [ ] чорний
- [ ] червоний
- [x] сірий
- [ ] білий

#### Q58. У чому різниця між поведінкою кліку цих двох кнопок (припускаючи, що `this.handleClick` не прив'язано правильно)?

```javascript
  A. <button onClick=this.handleClick>Click Me</button>
  B. <button onClick={event => this.handleClick(event)}>Click Me</button>
```

- [ ] `Кнопка A не матиме доступу до об'єкта події при натисканні`
- [x] `Кнопка A не викличе обробник this.handleClick успішно`
- [ ] `Немає різниці`
- [ ] `Кнопка B не викличе обробник this.handleClick успішно`

#### Q59. Як додати до цього коду з React Router, щоб відобразити компонент під назвою About?

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

[Довідка](https://reactrouter.com/en/main/components/route)

#### Q60. Який класовий компонент еквівалентний цьому функціональному компоненту?

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

#### Q61. Відповідно до наведеного коду, що описує другий аргумент, переданий у функцію `render`?

```javascript
ReactDOM.render(
  <h1>Hi<h1>,
    document.getElementById('root')
)
```

- [x] де React-елемент має бути доданий до DOM
- [ ] де викликати функцію
- [ ] де знаходиться кореневий компонент
- [ ] де створити новий файл JavaScript

#### Q62. Чому слід використовувати компонент Link з React Router замість звичайного тега `<a>` у React?

- [ ] Компонент Link дозволяє користувачеві використовувати кнопку `Назад` у браузері.
- [ ] Немає різниці — компонент `Link` це просто інша назва для тега `<a>`.
- [ ] Тег `<a>` викличе помилку при використанні в React.
- [x] Тег `<a>` викликає повне перезавантаження сторінки, тоді як компонент `Link` цього не робить.

#### Q63. Що є першим аргументом, `x`, який передається у функцію `createElement`?

```javascript
React.createElement(x, y, z);
```

- [x] елемент, який має бути створений
- [ ] порядок, у якому цей елемент має бути розміщений на сторінці
- [ ] властивості елемента
- [ ] дані, які мають бути відображені в елементі

#### Q64. Який метод життєвого циклу класового компонента буде викликаний одночасно з цим ефектом Hook?

```javascript
useEffect(() => {
  // щось робити
}, []);
```

- [ ] componentWillUnmount
- [x] componentDidMount
- [ ] render
- [ ] componentDidUpdate

[Довідка](https://uk.legacy.reactjs.org/docs/react-component.html#componentdidmount)

#### Q65. Яка назва базового компонента цього компонента?

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

#### Q66. Коли використовується портал, що є першим аргументом?

```javascript
ReactDOM.createPortal(x, y);
```

- [ ] поточний стан
- [x] елемент для рендеру
- [ ] компонент App
- [ ] сторінка

[Довідка](https://uk.react.dev/reference/react-dom/createPortal)

#### Q67. Що таке `setCount`?

```javascript
const [count, setCount] = useState(0);
```

- [ ] початкове значення стану
- [ ] змінна
- [ ] об'єкт стану
- [x] функція для оновлення стану

[Довідка](https://uk.legacy.reactjs.org/docs/hooks-state.html)

#### Q68. Для чого використовується функція map у наведеному коді?

```javascript
const database = [{ data: 1 }, { data: 2 }, { data: 3 }];
database.map((user) => <h1>{user.data}</h1>);
```

- [ ] повертає карту всіх записів у базі даних
- [x] повертає тег заголовка для кожного запису в базі даних, що містить його дані
- [ ] повертає один тег заголовка для всіх записів у базі даних
- [ ] перевіряє, який запис у базі даних підходить для тега заголовка

#### Q69. Опишіть, що відбувається в цьому коді?

```javascript
const { name: firstName } = props;
```

- [ ] Створюється новий об'єкт, який містить ту саму властивість `name`, що й об'єкт `props`.
- [ ] Значення властивості `firstName` об'єкта `props` присвоюється константі з назвою `name`.
- [ ] Отримується значення `props.name.firstName`.
- [x] Значення властивості `name` об'єкта `props` присвоюється константі з назвою `firstName`.

#### Q70. Що не так з цим кодом?

```javascript
const MyComponent = ({ names }) => (
  <h1>Hello</h1>
  <p>Hello again</p>
);
```

- [ ] React-компоненти не можуть бути визначені за допомогою функцій.
- [x] React не дозволяє компонентам повертати більше одного елемента.
- [ ] Компонент повинен використовувати ключове слово return.
- [ ] Рядкові літерали повинні бути оточені лапками.

#### Q71. Коли використовується портал, що є другим аргументом?

```javascript
ReactDOM.createPortal(x, y);
```

- [ ] компонент App
- [ ] сторінка
- [ ] поточний стан
- [x] DOM-елемент, який існує поза батьківським компонентом

#### Q72. Що буде виведено в тег `<div>`?

```javascript
const MyComponent = ({ children }) => (
  <div>{children.length}</div>
);
...
<MyComponent>
<p>
  Hello <span>World!</span>
</p>
<p>Goodbye</p>
</MyComponent>
```

- [ ] Виникне помилка "cannot read property "length" of undefined."
- [ ] 1
- [ ] undefined
- [x] 2

#### Q73. Як називається цей патерн?

```javascript
const [count, setCount] = useState(0);
```

- [ ] деструктурування об'єкта
- [x] деструктурування масиву
- [ ] оператор розширення
- [ ] пушинг коду

#### Q74. Який файл завантажується першим у браузері в базовому проекті React?

- [ ] src/App.js
- [ ] src/index.js
- [ ] public/manifest.json
- [x] public/index.html

#### Q75. Код нижче нічого не рендерить і генерує помилку: "ReactDOM is not defined." Як виправити цю проблему?

```javascript
import React from 'react';
import { createRoot } from 'reactjs-dom';

const element = <h1>Hi</h1>;
// Примітка: Помилка в рядку нижче
const root = ReactDOM.createRoot(document.getElementById('root'));

root.render(element);
```

- [x] `createRoot(document.getElementById("root"));`
- [ ] `ReactDOM(element, document.getElementById("root"));`
- [ ] `renderDOM(element, document.getElementById("root"));`
- [ ] `DOM(element, document.getElementById("root"));`

#### Q76. У цьому компоненті, як відобразити, чи користувач увійшов у систему?

```javascript
render() {
  const isLoggedIn = this.state.isLoggedIn;
  return (
    <div>
      Користувач:
    </div>
  );
}
```

- [ ] `Користувач увійшов у систему? увійшов : не увійшов.`
- [ ] Написати функцію для перевірки статусу входу.
- [ ] `Користувач {isLoggedIn = "ні"}.`
- [x] `Користувач {isLoggedIn ? "увійшов." : "не увійшов"}.`

#### Q77. Ви рендерите список у React, коли в консолі з'являється попередження: "Warning: Each child in a list should have a unique 'key' prop." Як виправити цю проблему?

- [ ] Додати однакове значення ключа до кожного елемента списку
- [ ] Очистити попередження в консолі
- [ ] Використати хук UseId для генерації унікального ключа для кожного елемента списку
- [x] Під час ітерації по елементах списку додати унікальну властивість до кожного елемента списку.

#### Q78. Як би ви згенерували шаблонний код для нового застосунку, який ви створюєте для збору спідньої білизни?

- [ ] npm create-react-app collect-underpants
- [ ] npx start-app collect-underpants
- [ ] react new collect-underpants
- [x] npx create-react-app collect-underpants

[Джерело: React Docs](https://uk.react.dev/learn/start-a-new-react-project#create-react-app)

#### Q79. Додайте код, який запустить фотонні торпеди при натисканні кнопки.

```javascript
class StarTrekkin extends React.Component {
  firePhotonTorpedoes(e) {
    console.log('піу піу');
  }
  render() {
    return; // Відсутній код
  }
}
```

- [ ] `<button onClick={firePhotonTorpedoes()}>Піу Піу</button>`
- [ ] `<button onClick={firePhotonTorpedoes}>Піу Піу</button>`
- [ ] `<button onClick={this.firePhotonTorpedoes()}>Піу Піу</button>`
- [x] `<button onClick={this.firePhotonTorpedoes}>Піу Піу</button>`

[Джерело: React Docs](https://uk.legacy.reactjs.org/docs/handling-events.html)

#### Q80. Як називається процес визначення, чи потрібне оновлення?

- [ ] shadow DOM
- [ ] fiber
- [x] reconciliation
- [ ] встановлення стану

#### Q81. React є проєктом з відкритим кодом, але якою компанією він підтримується?

- [ ] Intuit
- [ ] Twitter
- [x] Facebook
- [ ] Snapchat

#### Q82. Яку команду можна використовувати для створення проєкту React?

- [ ] react-starter
- [x] create-react-app
- [ ] react-gen
- [ ] react-start

[підказка](https://create-react-app.dev/)

#### Q83. Як називається розширення для браузера, яке використовують розробники React для зневадження застосунків?

- [x] React Developer Tools
- [ ] React Tooling Add-on
- [ ] React Codewatch
- [ ] React Debug

#### Q84. Який інструмент не є частиною Create React App?

- [ ] React
- [x] jQuery
- [ ] webpack
- [ ] ReactDOM

#### Q85. Яке розширення синтаксису JavaScript зазвичай використовується для створення елементів React?

- [ ] HTML
- [ ] JavaScriptX
- [x] JSX
- [ ] React JavaScript

#### Q86. Як можна перевірити типи властивостей без використання Flow або TypeScript?

- [ ] Перевірити вручну.
- [ ] Використати `prop-helper`.
- [x] Використати `prop-types`.
- [ ] Використати `checker-types`.

#### Q87. Як додати id "heading" до наступного елемента h1?

```javascript
let dish = <h1>Mac and Cheese</h1>;
```

- [ ] `let dish = <h1 id={heading}>Mac and Cheese</h1>;`
- [x] `let dish = <h1 id="heading">Mac and Cheese</h1>;`
- [ ] `let dish = <h1 id:"heading">Mac and Cheese</h1>;`
- [ ] `let dish = <h1 class="heading">Mac and Cheese</h1>;`

#### Q88. Яке значення кнопки дозволить передати ім'я людини, яку потрібно обійняти?

```javascript
class Huggable extends React.Component {
  hug(id) {
    console.log("hugging " + id);
  }
  render() {
    let name = "kitten";
    let button = // Відсутній код
    return button;
  }
}
```

- [ ] `<button onClick={(name) => this.hug(name)}>Hug Button</button>;`
- [ ] `<button onClick={this.hug(e, name)}>Hug Button</button>;`
- [ ] `<button onClick={(e) => hug(name, e)}>Hug Button</button>;`
- [x] `<button onClick={(e) => this.hug(name, e)}>Hug Button</button>;`

**Пояснення:**
Це питання перевіряє знання класових компонентів React. Потрібно використовувати `this`, щоб викликати методи, оголошені всередині класових компонентів.

#### Q89. Який синтаксис використовується для створення компонента в React?

- [ ] генератор
- [x] функція або клас
- [ ] service worker
- [ ] тег

[Довідка](https://uk.legacy.reactjs.org/docs/components-and-props.html)

**Пояснення:**
Компоненти React схожі на функції, які повертають HTML-елементи. Компоненти є незалежними та багаторазовими частинами коду. Вони служать тій самій меті, що й функції JavaScript, але працюють ізольовано та повертають HTML. Компоненти бувають двох типів: класові та функціональні.

#### Q90. Ви хочете вимкнути кнопку, щоб вона не генерувала жодних подій onClick. Яку властивість використовувати для цього?

- [ ] onBlur
- [ ] onPress
- [ ] defaultValue
- [x] disabled

#### Q91. У цій функції, як найкраще описати компонент Dish?

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

- [ ] дочірній компонент
- [x] батьківський компонент
- [ ] вкладений компонент
- [ ] компонент-сиблінг

#### Q92. Коли викликається функція componentDidMount?

- [x] одразу після додавання компонента до DOM
- [ ] перед додаванням компонента до DOM
- [ ] одразу після оновлення компонента
- [ ] одразу після виклику API

[Довідка](https://uk.react.dev/reference/react/Component#componentdidmount)

#### Q93. Для чого можна використовувати webpack у розробці React?

- [ ] для отримання віддалених залежностей, які використовуються застосунком
- [x] для розбиття застосунку на менші частини, які можуть бути легше завантажені браузером
- [ ] для форматування коду, щоб він був більш читабельним
- [ ] для забезпечення того, щоб застосунок не був вразливим до ін'єкції коду

#### Q94. Коли використовується розширення React Developer Tools для Chrome, що означає, якщо значок React червоний?

- [x] Ви використовуєте версію React для розробки.
- [ ] Ви використовуєте версію React для продакшну.
- [ ] Ви використовуєте webpack.
- [ ] Ви використовуєте Create React App.

[Довідка](https://teamtreehouse.com/community/hey-why-the-logo-of-react-developer-tools-appears-in-red)

#### Q95. Як би ви змінили конструктор, щоб виправити цю помилку: "ReferenceError: Must call super constructor in derived class before accessing 'this'..."?

```javascript
class TransIsBeautiful extends React.Component {
  constructor(props){
  // Відсутній рядок
  console.log(this) ;
  }
  ...
}
```

- [ ] render(props);
- [x] super(props);
- [ ] super(this);
- [ ] this.super();

#### Q96. Яку мову не можна використовувати з React?

- [x] Swift.
- [ ] JSX.
- [ ] JavaScript.
- [ ] TypeScript.

#### Q97. Цей код є частиною застосунку, який збирає покемонів. Як би ви вивели список зібраних покемонів?

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

[Довідка](https://www.digitalocean.com/community/tutorials/how-to-manage-state-on-react-class-components#step-3-setting-state-from-a-static-value)

#### Q98. Який результат виконання цього коду?

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

Пояснення: функція, викликана без параметра, використовуватиме типове значення для параметрів, тому x завжди буде дорівнювати 1, а y завжди буде дорівнювати 2.

#### Q99. Коли може бути використаний React.ref?

- [ ] для посилання на інший JS-файл
- [ ] для прив'язки функції
- [ ] для виклику функції
- [x] для прямого доступу до DOM-вузла

[Довідка](https://uk.react.dev/learn/referencing-values-with-refs)

#### Q100. Який патерн використовується в цьому блоці коду?

```javascript
const { tree, lake } = nature;
```

- [ ] функціональні значення за замовчуванням
- [ ] деструктурування масиву
- [ ] PRPL патерн
- [x] деструктурування присвоєння

[Довідка](https://uk.javascript.info/destructuring-assignment)

#### Q101. Як би ви виправили цей блок коду, щоб переконатися, що властивість `sent` встановлена в булеве значення false?

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

[Передача пропсів компоненту](https://uk.react.dev/learn/passing-props-to-a-component)

#### Q102. Цей код є частиною застосунку, який збирає покемонів. Хук useState є частиною стану, що зберігає імена зібраних покемонів. Як би ви отримали доступ до зібраних покемонів у стані?

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

Пояснення: useState завжди повертає масив із двома значеннями: сам стан (перше значення) і функцію set, яка дозволяє оновлювати стан (друге значення).
[Довідка по useState](https://uk.react.dev/reference/react/useState)

#### Q103. Що передати в проп onClick, щоб дозволити передати властивість initName у обробник greet?

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

Пояснення: Очевидно, що в питанні була помилка, де замість `greet` було написано `hug`. Відкинувши це, все одно можна винести уроки з цього питання.

- У функції глобальний об'єкт є усталеним прив'язуванням для `this`. У вікні браузера глобальний об'єкт — це [об'єкт Window].
  Це функціональний компонент, тому `this` з `this.hug` насправді відноситься до вікна браузера.
  Оскільки це функціональний компонент, можна безпосередньо звертатися до hug без використання `this`.
- Щоб передати обробник до onClick, завжди потрібно передавати функцію, а не виконувати її. Тому тут потрібно використовувати зворотний виклик.
  `initName` доступний у функціональній області Greeting, тому його можна безпосередньо передати як аргумент до hug().

#### Q104. Як називається компілятор, що використовується для перетворення JSX у JavaScript?

- [x] Babel
- [ ] JSX Editor
- [ ] Browser Buddy
- [ ] ReactDOM

[JSX Transform with Babel](https://uk.react.dev/learn/writing-markup-with-jsx)

#### Q105. Який хук використовується для запобігання повторному створенню функції під час кожного рендеру компонента?

- [x] useCallback
- [ ] useMemo
- [ ] useRef
- [ ] useTransition

[React Hooks useCallback документація](https://uk.react.dev/reference/react/useCallback)

#### Q106. Навіщо може використовуватися хук `useRef`?

- [ ] Для прив'язування функції
- [ ] Для виклику функції
- [x] Для безпосереднього доступу до DOM
- [ ] Для посилання на інший JS файл

[Довідка](https://uk.react.dev/reference/react/useRef)

#### Q107. Що з наведеного є обов'язковим для використання React?

- [x] JavaScript
- [ ] React Router
- [ ] Redux
- [ ] Prop-Types

[Довідка](https://uk.react.dev/learn/tutorial-tic-tac-toe)

#### Q108. Який правильний спосіб отримати значення з контексту?

- [ ] const value = useContext(MyContext.Consumer)
- [ ] const value = useContext(MyContext.Provider)
- [x] const value = useContext(MyContext)
- [ ] const value = useContext({value: "initial value"})

[Довідка](https://uk.react.dev/reference/react/useContext)

#### Q109. Навіщо використовується ref?

- [ ] для прив'язування функції
- [ ] для виклику функції
- [x] для безпосереднього доступу до DOM вузла
- [ ] для посилання на інший JS файл

[Довідка](https://uk.react.dev/reference/react/useRef)

#### Q110. Який метод слід перевизначити, щоб зупинити оновлення компонента?

- [ ] componentDidMount
- [ ] componentDidUpdate
- [ ] willComponentUpdate
- [x] shouldComponentUpdate

[Довідка](https://uk.legacy.reactjs.org/docs/react-component.html#shouldcomponentupdate)

#### Q111. Яка функціональність команди "webpack"?

- [ ] Запускає локальний сервер розробки react
- [ ] Переносить усі JS файли в один файл
- [ ] Модульний збирач
- [x] Усе вищезазначене

#### Q112. Який метод не є частиною ReactDOM?

- [ ] ReactDOM.createPortal()
- [ ] ReactDOM.hydrate()
- [x] ReactDOM.destroy()
- [ ] ReactDOM.findDOMnode()

#### Q113. У React ключ повинен бути?

- [x] Унікальним серед своїх братів і сестер
- [ ] Унікальним у DOM
- [ ] Не потребує бути унікальним
- [ ] Усе вищезазначене

[Довідка](https://uk.legacy.reactjs.org/docs/lists-and-keys.html#keys)

#### Q114. Яка компанія розробила ReactJS?

- [ ] Google
- [x] Meta (колишній Facebook)
- [ ] Apple
- [ ] Twitter

[Довідка](https://github.com/facebook/react)

#### Q115. Яка бібліотека найчастіше асоціюється з React?

- [ ] Chai
- [ ] Sinon
- [x] Jest
- [ ] Mocha

[Довідка](https://uk.legacy.reactjs.org/docs/testing-recipes.html)

#### Q116. Що з наведеного використовується в React.js для підвищення продуктивності?

- [ ] Оригінальний DOM
- [x] Віртуальний DOM
- [ ] Обидва варіанти
- [ ] Жоден з варіантів

[Довідка](https://uk.legacy.reactjs.org/docs/optimizing-performance.html)

#### Q117. Який з наведених варіантів допомагає React зберігати дані односпрямованими?

- [ ] DOM
- [x] flux
- [ ] JSX
- [ ] Props

[Довідка](https://uk.legacy.reactjs.org/blog/2014/05/06/flux.html)

#### Q118. Який варіант є правильним рефакторингом класового компонента Greeting у функціональний компонент?

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

#### Q119. Чому список очікування (waitlist) не оновлюється правильно?

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

- [x] `waitlist` змінюється безпосередньо. Використовуйте функцію `setWaitlist`, щоб оновити стан списку очікування.
- [ ] Форма перезавантажує сторінку кожного разу, коли натискається "Додати до списку очікування".
- [ ] Кнопка "Додати до списку очікування" не має обробника кліку.
- [ ] Ймовірно, у масиві `waitlist` є повторювані імена.

[Довідка](https://uk.legacy.reactjs.org/docs/react-component.html#setstate)

#### Q120. Який патерн використовується в Context.Consumer нижче?

<Context.Consumer>
{(isLoggedIn)=><b>{isLoggedIn ? "Online" : "Offline"}</b>}
</Context.Consumer>

- [ ] компонент вищого порядку
- [ ] wish компонент
- [x] Render Props
- [ ] setup компонент

#### Q121. У React.js який з наведених варіантів використовується для створення класу для наслідування?

- [ ] Create
- [x] Extends
- [ ] Inherits
- [ ] Delete

[Довідка](https://www.geeksforgeeks.org/react-js-quiz-set-1/)

#### Q122. Яка мета render() у React.js?

- [ ] Замінити наявну розмітку
- [ ] Оновити наявну розмітку
- [x] Обидва варіанти
- [ ] Жоден з варіантів

[Довідка](https://uk.react.dev/reference/react-dom/render)

#### Q123. Яка мета super(props) у React.js?

- [ ] Викликати конструктор батьківського класу
- [ ] Ініціалізувати this.props у конструкторі
- [x] Обидва варіанти
- [ ] Жоден з варіантів

[Довідка](https://uk.react.dev/reference/react/Component#constructor)

#### Q124. Що таке Redux у React.js?

- [x] Контейнер стану для JavaScript застосунків
- [ ] Інструмент для створення UI компонентів
- [ ] Обидва варіанти
- [ ] Жоден з варіантів

[Довідка](https://www.freecodecamp.org/news/what-is-redux-store-actions-reducers-explained/)

#### Q125. Яка мета віртуального DOM у React.js і як він покращує продуктивність вебзастосунків?

- [ ] Віртуальний DOM використовується для безпечного зберігання даних автентифікації користувачів.
- [ ] Віртуальний DOM — це резервна копія реального DOM, створена для налагодження.
- [x] Віртуальний DOM — це легке представлення реального DOM, і він допомагає покращити продуктивність, мінімізуючи безпосередню маніпуляцію реальним DOM.
- [ ] Віртуальний DOM — це база даних, яка використовується для зберігання станів компонентів.

[Довідка](https://medium.com/@vinaynkokate/demystifying-dynamic-web-applications-understanding-the-dom-and-web-browser-interactions-cc1b113adfa)

#### Q126. Ви запускаєте наступний код і отримуєте повідомлення про помилку: "invalid hook call." Що не так з кодом?

```javascript
import React from 'react';

const [poked, setPoked] = React.useState(false);

function PokeButton() {
  return <button onClick={() => setPoked(true)}>{poked ? 'You have left a poke.' : 'Poke'}</button>;
}
```

- [x] Виклик useState потрібно зробити всередині компонента PokeButton.
- [ ] Пакет react, ймовірно, не встановлено правильно.
- [ ] useState імпортовано неправильно. Імпортуйте useState безпосередньо замість імпорту react.
- [ ] PokeButton — це чиста функція, тому вона не може мати локального стану.

#### Q127. Колега звертається до вас за допомогою щодо компонента react. Він каже, що кнопка poke рендериться правильно, але коли натискається кнопка, з'являється помилка: "setPoked is not defined". Що не так з їхнім кодом?

```javascript
function PokeButton() {
  const { poked, setPoked } = useState(false);
  return <button onclick={() => setPoked(true)}>{poked ? 'You have left a poke.' : 'Poke'}</button>;
}
```

- [ ] Властивість onClick повинна бути onclick.
- [ ] Обробник кліку, переданий у властивість onClick, є вбудованим. Перемістіть цей обробник у змінну поза JSX.
- [x] Вони використовують деструктурування об'єкта замість деструктурування масиву. Обгорніть значення poked і setPoked у масив.
- [ ] poked і setPoked не деструктуровані в правильному порядку.

#### Q128. Цей компонент завантажується динамічно. Що слід замінити на XXXX, щоб завершити код?

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

#### Q129. Елементи у списках у React повинні мати \_**\_ які є \_\_\_** .

- [x] ключі ; унікальні
- [ ] ключі ; індекси
- [ ] стиль ; вбудований
- [ ] значення ; не-null
      [Джерело: React Docs](https://uk.legacy.reactjs.org/docs/lists-and-keys.html)

#### Q130. Ви хочете запам'ятати функцію зворотного виклику, щоб переконатися, що React не створює функцію під час кожного рендеру. Який хук ви б використали для цього?

- [ ] useRef
- [ ] useMemo
- [ ] memo
- [x] useCallback

[Джерело: CodeDamn](https://codedamn.com/news/reactjs/usememo-and-usecallback-hooks)

#### Q131. Ви хочете виконати мережеву операцію в результаті зміни стану компонента з назвою userInput. Що ви заміните на XXXX?

```javascript
useEffect(callNetworkFunc, XXXX);
```

- [x] [userInput]
- [ ] userInput
- [ ] undefined
- [ ] []

#### Q132. Коли відображається компонент Hello?

```javascript
<div>{isLoggedIn ? <Hello /> : null}</div>
```

- [ ] коли isLoggedIn є false
- [x] коли isLoggedIn є true
- [ ] коли isLoggedIn є false і викликається функція Hello
- [ ] ніколи

#### Q133. Коли використовується `useLayoutEffect`?

- [ ] для оптимізації для всіх пристроїв
- [ ] для завершення оновлення
- [x] для зміни компонування екрана
- [ ] коли потрібно, щоб браузер відобразив сторінку перед запуском ефекту

#### Q134. У чому різниця між state і props у React?

- [ ] Props задаються батьківським компонентом, state задається дочірнім компонентом
- [x] Props передаються компоненту, state керується всередині компонента
- [ ] Props можна оновлювати, state не можна оновлювати
- [ ] Немає різниці — props і state однакові

#### Q135. Яку мову не можна використовувати з React?

- [x] Swift.
- [ ] JSX.
- [ ] JavaScript.
- [ ] TypeScript.

#### Q136. Яка відповідь найкраще описує функціональний компонент?

- [ ] Функціональний компонент такий самий, як класовий компонент.
- [x] Функціональний компонент приймає один об'єкт props і повертає React елемент.
- [ ] Функціональний компонент — це єдиний спосіб створити компонент.
- [ ] Функціональний компонент обов'язковий для створення компонента React.

#### Q137. З якої бібліотеки походить функція `fetch()`?

- [ ] FetchJS
- [ ] ReactDOM
- [x] Жодної бібліотеки. `fetch()` підтримується більшістю браузерів.
- [ ] React

### Q138. У React, яка мета пропса `key` під час рендерингу списку компонентів?

- [ ] Пропс `key` використовується для надання унікального ідентифікатора компоненту.
- [ ] Пропс `key` використовується для визначення кольору компонента.
- [ ] Пропс `key` обов'язковий для рендерингу списку компонентів.
- [x] Пропс `key` використовується React для оптимізації оновлень і визначення, які елементи змінилися або були додані/видалені у списку.

#### Q139. Яка основна функція React Router?

- [ ] React Router використовується для отримання даних з API.
- [ ] React Router використовується для створення анімацій у React застосунках.
- [ ] React Router використовується для керування станом у компонентах React.
- [x] React Router використовується для додавання навігації та маршрутизації до React застосунків, дозволяючи користувачам переміщатися між різними видами або сторінками.

#### Q140. Коли слід використовувати Redux у React застосунку?

- [ ] Redux завжди потрібен у React застосунках.
- [ ] Redux слід використовувати, коли потрібно отримати дані з API.
- [ ] Redux використовується для створення інтерфейсів користувача, але не для керування станом.
- [x] Redux зазвичай використовується, коли є складні потреби в керуванні станом, наприклад, спільне використання стану між кількома компонентами або обробка глибоко вкладеного стану.

#### Q141. Яка мета React hooks?

- [ ] Для оптимізації React застосунків для мобільних пристроїв
- [ ] Для додавання візуальних ефектів до компонентів React.
- [x] Для дозволу використання стану та методів життєвого циклу у функціональних компонентах
- [ ] Для інтеграції з зовнішніми бібліотеками інтерфейсу користувача, як-от Bootstrap

#### Q142. Як можна передати дані через дерево компонентів React, не передаючи props вручну на кожному рівні?

- [x] Використовуючи контекст React
- [ ] Використовуючи redux
- [ ] Використовуючи react router
- [ ] Використовуючи методи життєвого циклу react
