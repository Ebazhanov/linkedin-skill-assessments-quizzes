## React.js

#### Q1. Si quisieras importar solamente un componente de la librería de React, ¿qué sintaxis usarías?

- [ ] `import React.Component from 'react'`
- [ ] `import [ Component ] from 'react'`
- [ ] `import Component from 'react'`
- [x] `import { Component } from 'react'`

#### Q2. Si una función componente quisiera rendearse de la misma manera dados los mismos parámetros, ¿cuál es una optimización simple disponible para el mismo?

- [x] Envolverlo en un componente `React.memo`.
- [ ] Implementar el hook `useReducer`.
- [ ] Implementar el hook `useMemo` Hook.
- [ ] Implementar el método de ciclo de vida `shouldComponentUpdate`.

#### Q3. ¿Cómo resuelves el error de sintáxis que resulta al ejecutar el siguiente código?

```javascript
const person =(firstName, lastName) =>
{
  first: firstName,
  last: lastName
}
console.log(person("Jill", "Wilson"))
```

- [x] Envolver el objeto devuelto entre paréntesis
- [ ] Llamar a la función desde otro archivo.
- [ ] Agregar un `return` ántes del último paréntesis.
- [ ] Reemplazar el objeto con un Array.

#### Q4. Si ves el siguiente import en un archivo, ¿qué dirías se está usando como administrador de estado en el componente?

`import React, {useState} from 'react';`

- [x] React Hooks
- [ ] componentes con estado
- [ ] matemática
- [ ] componentes de clase

#### Q5. Utilizando enriquecimiento literal de objetos, tu puedes ponerle valores de vuelta en los mismos. En este ejemplo, cuando leas el resultado del log en la consola, ¿qué leerás?

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

#### Q6. ¿Cuál es la librería de testeo más usualmente asociada con React?

- [ ] Mocha
- [ ] Chai
- [ ] Sinon
- [x] Jest

#### Q7. Utilizando deconstrucción de arrays, ¿Cómo obtendrías el primer item del array ("cooking")?

```javascript
const topics = ['cooking', 'art', 'history'];
```

- [ ] `const first = ["cooking", "art", "history"]`
- [ ] `const [] = ["cooking", "art", "history"]`
- [ ] `const [, first]["cooking", "art", "history"]`
- [x] `const [first] = ["cooking", "art", "history"]`

#### Q8. ¿Qué utilizas para pasar propiedades hacia abajo en un árbol de componentes sin tener que manualmente definir en cada uno de ellos parámetros para recibirlos?

- [ ] React Send
- [ ] React Pinpoint
- [ ] React Router
- [x] React Context

#### Q9. ¿Qué se imprimirá en la consola el ejecutar el siguiente código?

```javascript
const [, , animal] = ['Horse', 'Mouse', 'Cat'];
console.log(animal);
```

- [ ] Horse
- [x] Cat
- [ ] Mouse
- [ ] undefined

#### Q10. ¿Qué herramienta es la que se usa para convertir JSX en llamadas a createElement

- [ ] JSX Editor
- [ ] ReactDOM
- [ ] Browser Buddy
- [x] Babel

#### Q11. ¿Porqué utilizarías useReducer en lugar de useState en un React component?

- [ ] cuando quieres reemplazar a Redux
- [x] cuando quieres manejar un estado más complejo en una app
- [ ] cuando quieres mejorar la performance
- [ ] cuando quieres destruir tu aplicación en producción

#### Q12. Utilizando la siguiente sintáxis, ¿Qué propiedades están disponibles para el componente?

```javascript
<Message {...props} />
```

- [ ] cualquier propiedad que no haya cambiado
- [x] todas las propiedades de `props`
- [ ] propiedades hijas
- [ ] todas las que hayan cambiado en valor

#### Q13. Considerando el siguiente código de un React Router, ¿Cómo se le llama al ":id" en la ruta del parámetro path?

```javascript
<Route path="/:id" />
```

- [ ] Un modal de ruta
- [x] Un parámetro de ruta
- [ ] Un divisor de ruta
- [ ] Un link de ruta

#### Q14. Al renderizar el componente Dish, ¿Qué elemento html resultaría agregado al DOM?

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

#### Q15. Dada la siguiente llamada, ¿Qué elemento resultará creado en el DOM?

```javascript
React.createElement('h1', null, "What's happening?");
```

- [ ] `<h1 props={null}>What's happening?</h1>`
- [x] `<h1>What's happening?</h1>`
- [ ] `<h1 id="component">What's happening?</h1>`
- [ ] `<h1 id="element">What's happening?</h1>`

#### Q16. ¿Qué propiedad necesitas definirle al componente Suspense para que muestre un indicador de progreso?

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

#### Q17. ¿Cómo se le llama al mensaje entre llaves?

```javascript
const message = 'Hi there';
const element = <p>{message}</p>;
```

- [ ] una JS function
- [ ] un elemento JS
- [x] una JS expression
- [ ] un envoltorio JSX

#### Q18. ¿Qué se utiliza para realizar/ejecutar fraccionamiento de código?

- [ ] `React.memo`
- [ ] `React.split`
- [x] `React.lazy`
- [ ] `React.fallback`

#### Q19. ¿Cuándo se utiliza `useLayoutEffect`?

- [ ] cuando quieres optimizar para todos los dispositivos
- [ ] para completar el update
- [ ] para cambiar la pantalla actual
- [x] cuando necesitas que el navegador renderice el DOM antes de que se ejecute el effecto

#### Q20. ¿Cuál es la diferencia en el comporamiento de los receptores del evento onClick de estos dos botones? (asumiendo que this.handleClick está correctamente bindeado)

```javascript
A. <button onClick={this.handleClick}>Click Me</button>
B. <button onClick={event => this.handleClick(event)}>Click Me</button>
```

- [ ] El botón A no tendrá acceso al evento que inició el llamado
- [ ] El botón B no disparará el this.handleClick exitosamente
- [ ] El botón A no disparará el this.handleClick exitosamente
- [x] No habrá diferencia, ambos harán lo mismo.

#### Q21. ¿Cómo deconstruyes las propiedades que son enviadas al componente Dish?

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

#### Q22. ¿Cuándo usarías un `React.PureComponent`?

- [ ] cuando no quieres que tu componente tenga propiedades
- [ ] cuando tienes componentes anidados que necesitan ser comparados
- [x] cuando necesitas hacer uso de su implementación del método `shouldComponentUpdate()`
- [ ] cuando no quieres que tu componente tenga un estado

#### Q23. ¿Porqué es importante evitar copiar valores de las propiedades de un componente a su estado interno siempre que sea posible?

- [ ] porque nunca debes mutar su estado
- [ ] porque `getDerivedStateFromProps()` es un metodo inseguro de usar
- [x] porque queremos permitirle al componente actualizarse al detectar cambios en sus propiedades
- [ ] porque queremos permitir el flujo de datos de vuelta al componente superior

#### Q24. ¿Qué és la propiedad children?

- [ ] una propiedad que agrega un hijo al estado del componente
- [x] una propiedad especial que JSX crea en componentes que contienen una etiqueta de apertura y una etiqueta de cierre, referenciando su contenido.
- [ ] una propiedad que permite definir un array como propiedad
- [ ] una propiedad que permite pasar datos a componentes hijos

[**Explicación**](https://reactjs.org/docs/jsx-in-depth.html#children-in-jsx)

#### Q25. ¿Qué atributo se utiliza para reemplazar la propiedad innerHTML en el DOM del navegador?

- [ ] injectHTML
- [x] dangerouslySetInnerHTML
- [ ] weirdSetInnerHTML
- [ ] strangeHTML

#### Q26. ¿Cuál de estos términos comunmente describe una aplicación de React?

- [x] declarativo
- [ ] integrado
- [ ] cerrado
- [ ] imperativo

#### Q27. Cuando utilizas webpack, ¿Cuándo necesitarías utilizar un "cargador" (loader)?

- [ ] para armar carpetas en el sistema de archivos
- [x] para preprocesar archivos
- [ ] para cargar datos externos
- [ ] para cargar el sitio web en los teléfonos de los usuarios

#### Q28. Una representación de una interfaz de usuario que es mantenida en la memoria en sincronía con el DOM "real" ¿cómo se llama?

- [x] DOM virtual
- [ ] DOM
- [ ] elementos virtuales
- [ ] DOM sombrío/oscuro

#### Q29. Haz escrito el siguiente código, pero nada se renderiza. ¿Cómo solucionas este problema?

```javascript
const Heading = () => {
  <h1>Hello!</h1>;
};
```

- [ ] Agregar una función de rendeo.
- [x] Reemplazar las llaves por paréntesis o agregar un return keyword antes del primer h1 tag
- [ ] Mover el h1 a otro componente
- [ ] Envolver el h1 en un div

#### Q30. To create a constant in JavaScript, which keyword do you use?

#### Q30. Para definir una constánte en javascript, ¿Qué keyword se utiliza?

- [x] const
- [ ] let
- [ ] constant
- [ ] var

#### Q31. ¿Cómo se llama a un React component que capture errores de Javascript en cualquier lugar del arbol de componentes?

- [ ] error bosses
- [ ] error catchers
- [ ] error helpers
- [x] error boundaries

#### Q32. ¿En qué método de ciclo de vida de un componente de clase se deben hacer peticiones de datos?

- [ ] constructor
- [x] componentDidMount
- [ ] componentWillReceiveProps
- [ ] componentWillMount

#### Q33. Los componentes en React se componen para crear interfaces de usuario. ¿Cómo se componen los componentes en sí mismos?

- [ ] poniéndolos en un mismo archivo
- [x] anidando otros componentes
- [ ] con webpack
- [ ] con separación de código

#### Q34. Todos los componentes en React deben actuar como **\_** con respecto a sus propiedades.

- [ ] monads
- [x] funciones puras
- [ ] functions recursivas
- [ ] funciones de alto orden

#### Q35. ¿Cómo se le llama a este fragmento `[e.target.id]` utilizado en el código de abajo?

```javascript
handleChange(e) {
  this.setState({ [e.target.id]: e.target.value })
}
```

- [ ] una propiedad de nombre computada
- [ ] un valor pre-seteado
- [x] una llave dinámica
- [ ] un código de cadena JSX

#### Q36. ¿Cuál es el nombre de este componente?

```javascript
class Clock extends React.Component {
  render() {
    return <h1>Look at the time: {time}</h1>;
  }
}
```

- [x] Clock
- [ ] No tiene una propiedad de nombre.
- [ ] React.Component
- [ ] Component

#### Q37. ¿Qué se le envía a una función `Array.map()` ?

- [x] un callback a una función que es llamada una vez por cada elemento del array
- [ ] el nombre de otro array para iniciar una iteración
- [ ] el número de veces que se quiere llamar a la función
- [ ] un string describiendo qué debería hacer la función

#### Q38. ¿Porqué sería una buena idea pasarle una función a `setState` en lugar de un objeto?

- [ ] Porque permite una mejor encapsulación
- [ ] Se asegura de que el objeto no haya mutado
- [ ] Actualiza automaticamente un componente
- [x] `setState` es asíncrono y podría resultar en valores no actualizados correctamente a tiempo.

[**Explicación/Hint**](https://medium.com/@wisecobbler/using-a-function-in-setstate-instead-of-an-object-1f5cfd6e55d1)

#### Q39. ¿Qué paquete contiene la función render() que renderiza los elementos React en el DOM?

- [ ] `React`
- [x] `ReactDOM`
- [ ] `Render`
- [ ] `DOM`

#### Q40. ¿Cómo se define un valor por defecto en un campo de formulario no controlado?

- [ ] usando la propiedad `value`
- [x] usando la propiedad `defaultValue`
- [ ] usando la propiedad `default`
- [ ] Se asigna uno automaticamente

#### Q41. ¿Qué tienes que cambiar en el siguiente código para que el mismo pueda ejecutarse sin errores?

```js
class clock extends React.Component {
  render() {
    return <h1>Look at the time: {this.props.time}</h1>;
  }
}
```

- [ ] Poner el valor de retorno entre comillas
- [ ] remover el `this`
- [ ] remover el método render
- [x] Capitalizar `clock`

**Explicación:** En JSX, nombres en minúsculas son considerados elementos de HTML.
Lee [este artículo](https://reactjs.org/docs/jsx-in-depth.html#html-tags-vs.-react-components)

#### Q42. ¿Qué Hook puede ser usado para cambiar el título de la página?

- [x] `useEffect(function updateTitle() { document.title = name + ' ' + lastname; });`
- [ ] `useEffect(() => { title = name + ' ' + lastname; });`
- [ ] `useEffect(function updateTitle() { name + ' ' + lastname; });`
- [ ] `useEffect(function updateTitle() { title = name + ' ' + lastname; });`

#### Q43. ¿Qué se usa para cargar componentes de forma perezosa (lazy load)?

- [ ] `React.fallback`
- [ ] `React.split`
- [x] `React.lazy`
- [ ] `React.memo`

#### Q44. ¿Cómo puedes invocar el callback setDone solamente cuando el componente sea montado?

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

#### Q45. Actualmente, `handleClick` está siendo invocado en vez de estar siendo pasado como referencia. ¿Cómo arreglamos esto?

```javascript
<button onClick={this.handleClick()}>Click this</button>
```

- [ ] `<button onClick={this.handleClick.bind(handleClick)}>Click this</button>`
- [ ] `<button onClick={handleClick()}>Click this</button>`
- [x] `<button onClick={this.handleClick}>Click this</button>`
- [ ] `<button onclick={this.handleClick}>Click this</button>`

#### Q46. ¿Qué respuesta mejor describe a una función componente?

- [ ] Una función componente es igual que una función de clase.
- [x] Una función componente acepta un único parámetro con sus propiedades y devuelve un elemento React
- [ ] Una función componente es la única forma en la que se puede crear un componente
- [ ] Una función componente es requerido para poder crear un componente en React

#### Q47. ¿Qué librería define el método global `fetch()`?

- [ ] FetchJS
- [ ] ReactDOM
- [x] Ninguna. `fetch()` es provisto nativamente por la mayoría de los navegadores.
- [ ] React

#### Q48. ¿Qué ocurrirá cuando este hook useEffect se ejecute, asumiendo que name no sea igual a "john"?

```javascript
useEffect(() => {
  setName('John');
}, [name]);
```

- [ ] Causará un error inmediato
- [ ] Se ejecutará el código de la función, pero solo luego de esperar que ningún otro componente esté accediendo a esa variable (name)
- [x] Va a actualizar el valor de la variable name una vez y no hará nada hasta que el valor de la misma vuelva a cambiar.
- [ ] Causará un bucle infinito

#### Q49. ¿Qué opción no causara que un componente React se vuelva a renderizar?

- [ ] si el componente invoca el método `this.setState(...)`
- [ ] el valor de alguno de sus propiedades cambia
- [ ] se invoca el método `this.forceUpdate()`
- [x] alguno de sus componentes hijos se vuelve a renderizar

#### Q50. Creaste un nuevo método en un componente de clase llamado handleClick, pero no está funcionando. ¿Qué está faltando?

```javascript
class Button extends React.Component{

  constructor(props) {
    super(props);
    // ¿Qué falta pones aquí?
  }

  handleClick() {...}
}
```

- [ ] `this.handleClick.bind(this);`
- [ ] `props.bind(handleClick);`
- [ ] `this.handleClick.bind();`
- [x] `this.handleClick = this.handleClick.bind(this);`

#### Q51. React no renderiza dos componentes anexos a menos que estén envueltos en un fragmento. Debajo se muestra una forma de renderizar un fragmento. ¿Cuál es el otro método más corta para hacer lo mismo?

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

#### Q52. Si quisieras monstrar el valor de la variable del estado `count`, ¿Qué necesitas agregar dentro de las llaves en el elemento `h1`?

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

#### Q53. Según el código siguiente, ¿Cuándo será asignado el componente Hello a la variable greeting?

```javascript
const greeting = isLoggedIn ? <Hello /> : null;
```

- [ ] nunca
- [x] cuando `isLoggedIn` sea true
- [ ] cuando el usuario se loguee
- [ ] cuando la función Hello sea llamada

#### Q54. En el siguiente código, ¿Cuál será el tipo del valor que la propiedad orderNumber recibirá?

```javascript
ReactDOM.render(<Message orderNumber="16" />, document.getElementById('root'));
```

- [x] string
- [ ] boolean
- [ ] object
- [ ] number

#### Q55. Agregaste una propiedad de estilo en el elemento `h1` pero hay un error inesperado indicando un error de token al ejecutarlo. ¿Cómo lo solucionas?

```javascript
const element = <h1 style={ backgroundColor: "blue" }>Hi</h1>;
```

- [ ] `const element = <h1 style="backgroundColor: "blue""}>Hi</h1>;`
- [x] `const element = <h1 style={{backgroundColor: "blue"}}>Hi</h1>;`
- [ ] `const element = <h1 style={blue}>Hi</h1>;`
- [ ] `const element = <h1 style="blue">Hi</h1>;`

#### Q56. ¿Qué función es usada para actualizar variables de estado en un componente de clase React?

- [ ] `replaceState`
- [ ] `refreshState`
- [ ] `updateState`
- [x] `setState`

#### Q57. Considerando el siguiente componente. ¿Cuál es el color por defecto para el icono de Star?

```javascript
const Star = ({ selected = false }) => <Icon color={selected ? 'red' : 'grey'} />;
```

- [ ] black
- [ ] red
- [x] grey
- [ ] white

#### Q58. Cuál es la diferencia entre los comportamientos ante el evento onClick para estos dos botones? (asumiendo que this.handleClick no fue bindeado correctamente)

```javascript
  A. <button onClick=this.handleClick>Click Me</button>
  B. <button onClick={event => this.handleClick(event)}>Click Me</button>
```

- [ ] El botón A no tendrá acceso a la referencia del evento onClick
- [x] El botón A no se ejecutará correctamente
- [ ] No hay diferencia, ambos se ejecutarán con éxito
- [ ] El botón B no se ejecutará correctamente

#### Q59. Cómo agregarías en este código, de React Router, un componente llamado About cuando esta ruta se active?

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

#### Q60. Qué componente de clase es equivalente a este componente de función?

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

#### Q61. De acuerdo al siguiente código, ¿Qué proporciona el segundo parámetro que se le pasa a la función?

```javascript
ReactDOM.render(
  <h1>Hi<h1>,
    document.getElementById('root')
)
```

- [x] El elemento destino donde react debería agregar sus elementos al DOM
- [ ] donde llamar a la función
- [ ] la ubicación del root element
- [ ] la ubicación donde crear nuevos javascript

#### Q62. ¿Porqué deberías usar el componente Link de React Router en lugar de el anchor tag de html `a`?

- [ ] El elemento Link le permite al usuario usar el botón de `volver` en el navegador
- [ ] No hay diferencia, el elemento Link es sinónimo del tag `<a>`
- [ ] El tag `<a>` causará errores cuando se use con React.
- [x] El tag `<a>` causará un refrezco total de la página, mientras que el componente `Link` no lo hará.

#### Q63. ¿Qué és el primer parámetro `x`, que es enviado a la función `createElement`?

```javascript
React.createElement(x, y, z);
```

- [x] el elemento que debería ser creado
- [ ] El orden en que este elemento debe ser creado en la página
- [ ] las propiedades del elemento
- [ ] información que debería ser motrada en el elemento

#### Q64. ¿Qué método de ciclo de vida de un componente de clase sería llamado al mismo tiempo que este hook?

```javascript
useEffect(() => {
  // do things
}, []);
```

- [ ] componentWillUnmount
- [x] componentDidMount
- [ ] render
- [ ] componentDidUpdate

#### Q65. ¿Cuál es el nombre del componente base de este componente?

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

#### Q66. Cuando utilizas un Portal, ¿Qué va en el primer parámetro?

```javascript
ReactDOM.createPortal(x, y);
```

- [ ] el estado actual
- [x] el elemento a renderizar
- [ ] una referencia al App componet
- [ ] la página

**Explicación:**
[Portals](https://reactjs.org/docs/portals.html)

#### Q67. ¿Qué es `setCount`?

```javascript
const [count, setCount] = useState(0);
```

- [ ] el valor inicial del estado
- [ ] una variable
- [ ] el objeto estado
- [x] una función callback para cambiar el valor del estado

**Referencia**
[Hooks-State](https://reactjs.org/docs/hooks-state.html#:~:text=If%20we%20want%20to%20update%20the%20current)

#### Q68. ¿Cuál es el uso de la función map en el código de abajo?

```javascript
const database = [{ data: 1 }, { data: 2 }, { data: 3 }];
database.map((user) => <h1>{user.data}</h1>);
```

- [ ] devuelve un mapa de todas las entradas en la base de datos
- [x] devuelve un h1 element por cada elemento en la variable database con su data como texto
- [ ] devuelve un elemento h1 conteniendo todos los elementos de la variable database
- [ ] chequea qué elemento de la base de datos es apta para ser mostrada en un elemento h1

#### Q69. Describe ¿qué está ocurriendo en este código?

```javascript
const { name: firstName } = person;
```

- [ ] está creando un nuevo objeto que contiene la misma propiedad `name` que el objeto firstName
- [ ] Está asignando el valor de la propiedad firstName del objeto person a una constante llamada name
- [ ] esta obteniendo el valor de person.name.firstName
- [x] está asignando el valor de la propiedad name del objeto person a una constante llamada firstName

#### Q70. ¿Qué esta mal con este código?

```javascript
const MyComponent = ({ names }) => (
  <h1>Hello</h1>
  <p>Hello again</p>
);
```

- [ ] Los componentes en React no pueden ser definidos usando funciones
- [x] React no permite que los componentes funcion devuelvan más de un elemento.
- [ ] El componente debe usar el keyword return para devolver elementos.
- [ ] Las cadenas de caracteres deben ser envueltas en comillas

#### Q71. Cuando se usa un portal, ¿Qupe es el segundo argumento?

```javascript
ReactDOM.createPortal(x, y);
```

- [ ] el App Compontent
- [ ] la página
- [ ] el estado actual
- [x] el elemento DOM que existe fuera del elemento padre

#### Q72. Dado el siguiente código, ¿Qué será renderizado dentro del tag `<h1>`?

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

- [ ] Emitirá un error diciendo "cannot read property "length" of undefined."
- [ ] 1
- [ ] undefined
- [x] 2

#### Q73. ¿Cómo se llama a este patrón de asignación?

```javascript
const [count, setCount] = useState(0);
```

- [ ] deconstrucción de objeto
- [x] deconstrucción de array
- [ ] operador de separación
- [ ] empuje de código

#### Q74. ¿Cuál es el primer archivo cargado por el navegador en un proyecto básico de React?

- [ ] src/App.js
- [ ] src/index.js
- [ ] public/manifest.json
- [x] public/index.html

#### Q75. El código de abajo no esta renderizando nada, y hay un error que dice "ReactDOM is not defined." ¿Cómo lo resolvemos?

```javascript
import React from 'react';
import { render } from 'reactjs-dom';

const element = <h1>Hi</h1>;

ReactDOM.render(element, document.getElementById('root'));
```

- [x] `render(element, document.getElementById("root"));`
- [ ] `ReactDOM(element, document.getElementById("root"));`
- [ ] `renderDOM(element, document.getElementById("root"));`
- [ ] `DOM(element, document.getElementById("root"));`

#### Q76. En este componente, ¿cómo mostramos si el usuario esta logueado o no?

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

- [ ] `The user is loggedIn ? logged in : not logged in.`
- [ ] Hay que escribir una función para determinar si el usuario está logueado o no
- [ ] `The user is {isLoggedIn = "no"}.`
- [x] `The user is {isLoggedIn ? "logged in." : "not logged in"}.`

#### Q77. Estas renderizando una lista en React cuando la siguiente advertencia aparece en la consola: "Warning: Each child in a list should have a unique 'key' prop." ¿Cómo resolvés este asunto?

- [ ] Pasa el nombre de cada item como valo en su propiedad key
- [ ] Agregar una propiedad key con el mismo valor en todos los items de la lista
- [ ] Borrar las advertencias de la consola
- [x] Agregar una propiedad key a cada item de la lista con un valor único asosiado al mismo.

#### Q78. ¿Cómo crearías código de boilerplate para un nuevo app que quieres hacer para coleccionar pantalones?

- [ ] npm create-react-app collect-pantalones
- [ ] npx start-app collect-pantalones
- [ ] react new collect-pantalones
- [x] npx create-react-app collect-pantalones

[Create react app](https://reactjs.org/docs/create-a-new-react-app.html#create-react-app)

#### Q79. Agregá código que dispare torpedos de fotones cuando el botón sea cliqueado.

```javascript
class StarTrekkin extends React.Component {
  firePhotonTorpedoes(e) {
    console.log('pew pew');
  }
  render() {
    return; // El código hay que agregarlo aquí
  }
}
```

- [ ] `<button onClick={firePhotonTorpedoes()}>Pew Pew</button>`
- [ ] `<button onClick={firePhotonTorpedoes}>Pew Pew</button>`
- [ ] `<button onClick={this.firePhotonTorpedoes()}>Pew Pew</button>`
- [x] `<button onClick={this.firePhotonTorpedoes}>Pew Pew</button>`

[Handling Events](https://reactjs.org/docs/handling-events.html)

#### Q80. ¿Cómo se llama al proceso para decidir si una update es necesaria o no?

- [ ] DOM Sombrío
- [ ] fibra
- [x] reconciliación
- [ ] definición de estado

#### Q81. React es un proyecto open-source pero ¿qué compañía lo mantiene?

- [ ] Intuit
- [ ] Twitter
- [x] Facebook
- [ ] Snapchat

#### Q82. ¿Qué comando podés usar para crear un proyecto en React?

- [ ] react-starter
- [x] create-react-app
- [ ] react-gen
- [ ] react-start

[hint](https://create-react-app.dev/)

#### Q83. ¿Cuál es la extensión de navegador que los desarrolladores de React usan para debugear sus aplicaciones?

- [x] React Developer Tools
- [ ] React Tooling Add-on
- [ ] React Codewatch
- [ ] React Debug

#### Q84. ¿Qué herramienta no es parte de Create React App?

- [ ] React
- [x] jQuery
- [ ] webpack
- [ ] ReactDOM

#### Q85. ¿Cuál es la extensión de sintáxis en Javascript que se usa comunmente para crear elementos React?

- [ ] HTML
- [ ] JavaScriptX
- [x] JSX
- [ ] React JavaScript

#### Q86. ¿Cómo podrías chequear el tipo de dato de las propiedades sin utilizar Flow o Typescript?

- [ ] Manualmente.
- [ ] Usando `prop-helper`.
- [x] Usando `prop-types`.
- [ ] Usando `checker-types`.

#### Q87. ¿Cómo le agregarías el id heading al siguiente elemento h1?

```javascript
let dish = <h1>Mac and Cheese</h1>;
```

- [ ] `let dish = <h1 id={heading}>Mac and Cheese</h1>;`
- [x] `let dish = <h1 id="heading">Mac and Cheese</h1>;`
- [ ] `let dish = <h1 id:"heading">Mac and Cheese</h1>;`
- [ ] `let dish = <h1 class="heading">Mac and Cheese</h1>;`

#### Q88. ¿Qué valor para el componente button nos permitiría pasarle el nombre de la persona para abrazar?

```javascript
class Huggable extends React.Component {
  hug(id) {
    console.log("hugging " + id);
  }
  render() {
    let name = "kitten";
    let button = // Missing code
    return button;
  }
}
```

- [ ] `<button onClick={(name) => this.hug(name)}>Hug Button</button>;`
- [ ] `<button onClick={this.hug(e, name)}>Hug Button</button>;`
- [ ] `<button onClick={(e) => hug(name, e)}>Hug Button</button>;`
- [x] `<button onClick={(e) => this.hug(name, e)}>Hug Button</button>;`

**Explicación:**
Esta pregunta testea tu conocimiento de componente de clases en react. Tenés que usar `this` para llamar métodos definidos en componentes de clases.

#### Q89. ¿Qué sintaxis usas para crear componentes en React?

- [ ] un generador
- [x] una función o una clase
- [ ] un service worker
- [ ] un tag

[Componentes y propiedades](https://reactjs.org/docs/components-and-props.html)

#### Q90. You want to disable a button so that it does not emit any events onClick. Which prop do you use to acomplish this?

#### Q90. Querés deshabilitar un botón para que no emita eventos de onClick. ¿Que propiedad utilizas para lograr esto?

- [ ] onBlur
- [ ] onPress
- [ ] defaultValue
- [x] disabled

#### Q91. Dado este componente función, ¿Qué describe mejor al Dish component?

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

- [ ] es un componente hijo
- [x] es un componente padre
- [ ] es un componente anidado
- [ ] es un componente anexo

#### Q92. When does the componentDidMount function fire?

#### Q92. ¿Cuándo se ejectua el método componentDidMount en un componente de clase?

- [x] luego de haber sido agregado al DOM
- [ ] antes de ser agregado al DOM
- [ ] inmediatamente luego de ser actualizado
- [ ] luego de una API call

#### Q93. ¿Para qué utilizarías webpack?

- [ ] para buscar dependecias externas que utilice mi app
- [x] para dividir mi aplicación en bloques de códigos más pequeños y así podér ser cargados más facilmente por el navegador
- [ ] para formatear mi código para que sea mas legible
- [ ] para proteger mi app de injecciones de código malicioso

#### Q94. Cuando utilizas la extensión de chrome React Developer Tools, ¿Qué significa cuando el ícono está en rojo?

- [x] Que se está utilizando la versión development del app
- [ ] Que se está usando la versión de producción del app
- [ ] Que se está usando webpack
- [ ] Que se está usando Create React App

[Reference](https://teamtreehouse.com/community/hey-why-the-logo-of-react-developer-tools-appears-in-red)

#### Q95. ¿Cómo modificarías el constructor para evitar el siguiente error? "ReferenceError: Must call super constructor in derived class before accessing 'this'..."?

```javascript
class TransIsBeautiful extends React.Component {
  constructor(props){
  // Línea faltante....
  console.log(this) ;
  }
  ...
}
```

- [ ] render(props);
- [x] super(props);
- [ ] super(this);
- [ ] this.super();

#### Q96. ¿Qué lenguaje NO podés usar con React?

- [x] Swift.
- [ ] JSX.
- [ ] Javascipt.
- [ ] TypeScript.

#### Q97. Este código es parte de un app que colecciona Pokemons. ¿Cómo podrías imprimir una lista de los que actualmente estén coleccionados?

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

#### Q98. ¿Cuál sería el resultado de ejecutar este código?

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

#### Q99. ¿Porqué podrías necesitar utilizar React.createRef?

- [ ] para referirnos a otro archivo JS
- [ ] para bindear una función
- [ ] para llamar a una función
- [x] para acceder directamente a un nodo DOM

[Reference](https://reactjs.org/docs/refs-and-the-dom.html)

#### Q100. ¿Qué patrón de asignación se está utilizando en este código?

```javascript
const { tree, lake } = nature;
```

- [ ] function defaults
- [ ] deconstrucción de arrays
- [ ] PRPL pattern
- [x] deconstrucción de objeto

[Reference](https://javascript.info/destructuring-assignment)

#### Q101. ¿Cómo corregirías este código para asegurarte que la propiedad sent tenga el valor booleano false?

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
