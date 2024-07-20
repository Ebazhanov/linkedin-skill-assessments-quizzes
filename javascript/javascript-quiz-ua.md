## JavaScript

#### Q1. Який оператор поверне true якщо два порівнюваних значення не рівні?

- [ ] `<>`
- [ ] `~`
- [ ] `==!`
- [x] `!==`

[Посилання на оператори порівняння Javascript](https://www.w3schools.com/js/js_operators.asp)

#### Q2. Чим оператор forEach відрізняється від оператора for?

- [ ] Тільки оператор for використовує функцію зворотного виклику.
- [x] Оператор for є більш загальним і може використовуватися з різними ітерованими об’єктами, тоді як оператор forEach в основному розроблений для масивів, але також може використовуватися з іншими ітерованими об’єктами, такими як Sets.
- [ ] Тільки оператор forEach дозволяє вказати власний ітератор.
- [ ] Оператор forEach є загальним, а оператор for можна використовувати лише з масивом.

[Довідка. Відмінності між циклом forEach і for](https://www.geeksforgeeks.org/difference-between-foreach-and-for-loop-in-javascript/)

#### Q3. Перегляньте наведений нижче код. Який оператор викликає функцію addTax і передає 50 як аргумент?

```js
function addTax(total) {
  return total * 1.05;
}
```

- [ ] `addTax = 50;`
- [ ] `return addTax 50;`
- [x] `addTax(50);`
- [ ] `addTax 50;`

[Довідка. Функції в javascript](https://www.w3schools.com/js/js_functions.asp)

#### Q4. Який оператор є правильним способом створити змінну під назвою rate і присвоїти їй значення 100?

- [x] `let rate = 100;`
- [ ] `let 100 = rate;`
- [ ] `100 = let rate;`
- [ ] `rate = 100;`

[Довідка. Оператори призначення Javascript](https://www.w3schools.com/js/js_operators.asp)

#### Q5. Який оператор створює новий об’єкт за допомогою конструктора Person? Який оператор створює новий об’єкт Person під назвою «student»?

- [x] `var student = new Person();`
- [ ] `var student = construct Person;`
- [ ] `var student = Person();`
- [ ] `var student = construct Person();`

[Довідка](https://webdoky.org/uk/docs/Web/JavaScript/Reference/Classes/)

#### Q6. Коли останній вираз у показаному коді буде виведено в консоль? Коли «Results shown» буде виведено в консоль?

```js
let modal = document.querySelector('#result');
setTimeout(function () {
  modal.classList.remove('hidden');
}, 10000);
console.log('Results shown');
```

- [ ] через 10 секунд
- [ ] після отримання результатів із запиту HTTP
- [ ] через 10000 секунд
- [x] негайно

[Довідка. Javascript є синхронним і однопотоковим](https://stackoverflow.com/a/2035662/15067394)

#### Q7. Який фрагмент можна додати до цього коду, щоб надрукувати «food» в консолі?

```js
class Animal {
  static belly = [];
  eat() {
    Animal.belly.push('food');
  }
}
let a = new Animal();
a.eat();
console.log(/* Snippet Here */); //Друкує food
```

- [ ] `a.prototype.belly[0]`
- [ ] `Object.getPrototype0f (a).belly[0]`
- [x] `Animal.belly[0]`
- [ ] `a.belly[0]`

[Довідка Javascript Class static Keyword](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/static)

#### Q8. Ви написали код для виводу набору послідовних значень у консоль, але замість цього виводяться значення 5, 5, 5 і 5. Яка версія коду призведе до виводу значень 1, 2, 3 і 4?

- [ ] `A`

```js
for (var i = 1; i <= 4; i++) {
  setTimeout(function () {
    console.log(i);
  }, i * 10000);
}
```

- [ ] `B`

```js
for (var i = 1; i <= 4; i++) {
  (function (i) {
    setTimeout(function () {
      console.log(j);
    }, j * 1000);
  })(j);
}
```

- [ ] `C`

```js
for (var i = 1; i <= 4; i++) {
  setTimeout(function () {
    console.log(i);
  }, i * 1000);
}
```

- [x] `D`

```js
for (var i = 1; i <= 4; i++) {
  (function (j) {
    setTimeout(function () {
      console.log(j);
    }, j * 1000);
  })(i);
}
```

- [ ] `E`

```js
for (var j = 1; j <= 4; j++) {
  setTimeout(function () {
    console.log(j);
  }, j * 1000);
}
```

1. [Довідка setTimeout](https://developer.mozilla.org/en-US/docs/Web/API/setTimeout)
2. [Довідка анонімні функції, що викликаються негайно](https://www.javascripttutorial.net/javascript-anonymous-functions/)

#### Q9. Як функція створює замикання?

- [ ] Перезавантажує документ щоразу, коли змінюється значення.
- [x] Повертає посилання на змінну в її батьківській області.
- [ ] Завершує виконання без повернення.
- [ ] Копіює локальну змінну в глобальну область.

[Довідка](https://webdoky.org/uk/docs/Web/JavaScript/Closures/)

#### Q10. Який вираз створює нову функцію під назвою discountPrice?

- [x] `A`

```js
let discountPrice = function (price) {
  return price * 0.85;
};
```

- [ ] `B`

```js
let discountPrice(price) {
  return price * 0.85;
};
```

- [ ] `C`

```js
let function = discountPrice(price) {
  return price * 0.85;
};
```

- [x] `D`

```js
discountPrice = function (price) {
  return price * 0.85;
};
```

[Довідка. Визначення функцій у javascript](https://www.w3schools.com/js/js_functions.asp)

#### Q11. Який результат буде у консолі після виконання показаного коду?

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

[Довідка](https://webdoky.org/uk/docs/Web/JavaScript/Inheritance_and_the_prototype_chain/)

#### Q12. Потрібно знайти значення часу, наприклад 12:00:32. Який із наведених нижче регулярних виразів підійде для вашого коду?

- [ ] `/[0-9]{2,}:[0-9]{2,}:[0-9]{2,}/`
- [x] `/\d\d:\d\d:\d\d/`
- [ ] `/[0-9]+:[0-9]+:[0-9]+/`
- [ ] `/ : : /`

**ПРИМІТКА**: усі перші три частково правильні та відповідатимуть цифрам, але **другий варіант є найбільш правильним**, оскільки він **лише** відповідатиме **2-значним** значенням часу (12: 00:32). Перший варіант спрацював би, якби діапазон повторень виглядав як `[0-9]{2}`, однак через **кому** `[0-9]{2,}` буде вибрано 2 **або більше** цифр (120:000:321). Третій варіант відповідає будь-яким діапазонам цифр часу, одним _і_ кратним (це означає, що `1:2:3` також збігатиметься).

**Додаткові ресурси:**

1. [Символи, що повторюються](https://regexone.com/lesson/repeating_characters)
2. [Оператори Кліні](https://regexone.com/lesson/kleene_operators)

#### Q13. Який результат виконання цього коду в консолі?

```js
'use strict';
function logThis() {
  this.desc = 'logger';
  console.log(this);
}
new logThis();
```

- [ ] `undefined`
- [ ] `window`
- [x] `{desc: "logger"}`
- [ ] `function`

[Класи](https://webdoky.org/uk/docs/Web/JavaScript/Reference/Classes/)

#### Q14. Як би ви посилалися на текст 'avenue' у показаному коді?

```js
let roadTypes = ['street', 'road', 'avenue', 'circle'];
```

- [ ] roadTypes.2
- [ ] roadTypes\[3\]
- [ ] roadTypes.3
- [x] roadTypes\[2\]

[Доступ до масивів JavaScript](https://www.w3schools.com/js/js_arrays.asp)

#### Q15. Який результат виконання цього виразу?

```js
console.log(typeof 42);
```

- [ ] `'float'`
- [ ] `'value'`
- [x] `'number'`
- [ ] `'integer'`

[Типи та структури даних](https://webdoky.org/uk/docs/Web/JavaScript/Data_structures/)

#### Q16. Яка властивість посилається на об’єкт DOM, який відправив подію?

- [ ] `self`
- [ ] `object`
- [x] `target`
- [ ] `source`

[Події DOM](https://www.w3schools.com/jsref/dom_obj_event.asp)

#### Q17. Ви додаєте обробку помилок до показаного коду. Який код ви включите в вираз if, щоб вивести повідомлення про помилку?

```js
function addNumbers(x, y) {
  if (isNaN(x) || isNaN(y)) {
  }
}
```

- [ ] `exception('One or both parameters are not numbers')`
- [ ] `catch('One or both parameters are not numbers')`
- [ ] `error('One or both parameters are not numbers')`
- [x] `throw('One or both parameters are not numbers')`

[Javascript throw](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/throw)

#### Q18. Який метод перетворює дані JSON на об’єкт JavaScript?

- [ ] `JSON.fromString();`
- [x] `JSON.parse()`
- [ ] `JSON.toObject()`
- [ ] `JSON.stringify()`

[Перетворення json на об’єкт javascript](https://www.w3schools.com/js/js_json_parse.asp)

#### Q19. Коли б ви використовували умовний оператор?

- [ ] Коли ви хочете повторно використати набір операторів кілька разів.
- [x] Коли ви хочете, щоб ваш код вибирав між кількома варіантами.
- [ ] Коли потрібно згрупувати дані.
- [ ] Коли ви хочете прокрутити групу операторів.

[Умови в javascript](https://www.javascript.com/learn/conditionals)

#### Q20. Яким буде результат виконання цього коду в консолі?

```js
for (var i = 0; i < 5; i++) {
  console.log(i);
}
```

- [ ] 1 2 3 4 5
- [ ] 1 2 3 4
- [x] 0 1 2 3 4
- [ ] 0 1 2 3 4 5

[Цикли for в javascript](https://www.w3schools.com/js/js_loop_for.asp)

#### Q21. Який метод Object повертає ітерований елемент, який можна використовувати для перебору властивостей об’єкта?

- [ ] `Object.get()`
- [ ] `Object.loop()`
- [ ] `Object.each()`
- [x] `Object.keys()`

[Статичні методи об’єкта javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object#static_methods)

#### Q22. Що буде виведено в консолі?

```js
var a = ['dog', 'cat', 'hen'];
a[100] = 'fox';
console.log(a.length);
```

- [x] 101
- [ ] 3
- [ ] 4
- [ ] 100

#### Q23. Яка відмінність між колекціями, створеними за допомогою Map, і за допомогою Object?

- [ ] Ви можете перебирати значення в Map в порядку вставки.
- [x] Ви можете підрахувати записи в Map за допомогою одного виклику методу.
- [ ] Ключі в Map можуть бути рядками.
- [ ] Ви можете отримати доступ до значень в Map без ітерації по всій колекції.

**Пояснення:** `Map.prototype.size повертає кількість елементів у Map, тоді як Object не має вбудованого методу для повернення його розміру.`
[Методи Map](https://webdoky.org/uk/docs/Web/JavaScript/Reference/Global_Objects/Map/)

#### Q24. Яке значення dessert.type після виконання цього коду?

```js
const dessert = { type: 'pie' };
dessert.type = 'pudding';
```

- [ ] pie
- [ ] Код видасть помилку.
- [x] pudding
- [ ] undefined

[Робота з об'єктами](https://webdoky.org/uk/docs/Web/JavaScript/Guide/Working_with_objects/)

#### Q25. 0 && hi

- [ ] ReferenceError
- [ ] true
- [x] 0
- [ ] false

[Логіка boolean](https://ntgard.medium.com/https-medium-com-ntgard-boolean-logic-in-javascript-part-1-3371af974f19)

#### Q26. Який із наведених нижче операторів можна використовувати для скороченого обчислення?

- [ ] `++`
- [ ] `--`
- [ ] `==`
- [x] `||`

[Скорочене обчислення в javascript](https://codeburst.io/javascript-what-is-short-circuit-evaluation-ff22b2f5608c)

#### Q27. Який вираз встановлює конструктор Person як батьківський елемент конструктора Student у ланцюжку прототипів?

- [ ] `Student.parent = Person;`
- [x] `Student.prototype = new Person();`
- [ ] `Student.prototype = Person;`
- [ ] `Student.prototype = Person();`

[Прототип об'єкта js](https://webdoky.org/uk/docs/Web/JavaScript/Inheritance_and_the_prototype_chain/)

#### Q28. Навіщо включати оператор "use strict" у файл JavaScript?

- [ ] щоб наказати парсерам вільно інтерпретувати ваш синтаксис JavaScript
- [x] щоб повідомити парсерам застосовувати всі правила синтаксису JavaScript під час обробки вашого коду
- [ ] щоб наказати браузеру автоматично виправляти будь-які помилки, які він знаходить у коді
- [ ] щоб увімкнути функції ES6 у вашому коді

[Що таке use strict в js](https://www.w3schools.com/js/js_strict.asp)

#### Q29. Яке ключове слово, що визначає змінну, дозволяє отримати доступ до своєї змінної (як невизначеної) перед рядком, який її визначає?

- [ ] всі
- [ ] `const`
- [x] `var`
- [ ] `let`

[Var, let і const в js](https://www.freecodecamp.org/news/var-let-and-const-whats-the-difference/)

#### Q30. Яке з наведених нижче значень не є логічним значенням false?

- [ ] `Boolean(0)`
- [ ] `Boolean("")`
- [ ] `Boolean(NaN)`
- [x] `Boolean("false")`

[Вoolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean)

#### Q31. Що з наведеного не є ключовим словом у JavaScript?

- [ ] `this`
- [ ] `catch`
- [ ] `function`
- [x] `array`

[Зарезервовані слова JS](https://www.w3schools.com/js/js_reserved.asp)

#### Q32. Яка змінна є неявним параметром для кожної функції в JavaScript?

- [x] arguments
- [ ] args
- [ ] argsArray
- [ ] argumentsList

[Неявні параметри для функцій](https://www.codeproject.com/Tips/1221966/JavaScript-Functions-Implicit-Parameters)

#### Q33. Для наступного класу, як отримати значення 42 з екземпляра X?

```js
class X {
  get Y() {
    return 42;
  }
}
var x = new X();
```

- [ ] `x.get('Y')`
- [x] `x.Y`
- [ ] `x.Y()`
- [ ] `x.get().Y`

[Геттери](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/get)

#### Q34. Який результат виконання цього коду?

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

[Доступ раніше ініціалізації](https://stackoverflow.com/questions/56318460/cannot-access-variable-name-before-initialization)

#### Q35. Чому для зберігання колекції записів зазвичай краще працювати з об’єктами, а не з масивами?

- [ ] Об’єкти більш ефективні з точки зору зберігання.
- [ ] Додавання запису до об’єкта відбувається значно швидше, ніж розміщення запису в масиві.
- [x] Більшість операцій включають пошук запису, і об’єкти можуть робити це краще, ніж масиви.
- [ ] Робота з об'єктами робить код більш читабельним.

[Ефективність пошуку](https://stackoverflow.com/questions/17295056/array-vs-object-efficiency-in-javascript)
**Пояснення:** Записи в об’єкті можна отримати за допомогою їх ключа, який може бути будь-яким заданим значенням (наприклад, ідентифікатор працівника, назва міста тощо), тоді як для отримання запису з масиву нам потрібно знати його індекс.

#### Q36. Яке твердження вірне щодо атрибута "async" для тегу HTML-сценарію?

- [ ] Його можна використовувати як для внутрішнього, так і для зовнішнього коду JavaScript.
- [ ] Його можна використовувати лише для внутрішнього коду JavaScript.
- [ ] Його можна використовувати лише для внутрішнього або зовнішнього коду JavaScript, який експортує promise.
- [x] Його можна використовувати лише для зовнішнього коду JavaScript.

[Async атрибут для html](https://www.w3schools.com/tags/att_script_async.asp)

#### Q37. Як імпортувати бібліотеку lodash, щоб зробити її API верхнього рівня доступною як змінну "\_"?

- [x] `import _ from 'lodash';`
- [ ] `import 'lodash' as _;`
- [ ] `import '_' from 'lodash;`
- [ ] `import lodash as _ from 'lodash';`

[Як імпортувати бібліотеку](https://webdoky.org/uk/docs/Web/JavaScript/Reference/Statements/import/)

#### Q38. Що поверне наступний вираз?

```js
[] == [];
```

- [ ] true
- [ ] undefined
- [ ] []
- [x] false

[Масиви є об'єктами](https://stackoverflow.com/questions/30820611/why-doesnt-equality-check-work-with-arrays)

#### Q39. Виконання функції якого типу можна призупинити, а потім відновити пізніше?

- [x] Generator function
- [ ] Arrow function
- [ ] Async/ Await function
- [ ] Promise function

[Що таке генератори](https://www.guru99.com/node-js-generators-compare-callbacks.html#:~:text=Generators%20are%20function%20executions%20that,resumed%20at%20a%20later%20point.)

#### Q40. Що надрукує цей код?

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
- [ ] Нічого - цей код видасть помилку.
- [ ] undefined

[Замикання в js \/ вкладені функції](https://javascript.info/closure)

#### Q41.Яке твердження є правдивим щодо функціонального програмування?

- [ ] Кожен об'єкт програми повинен бути функцією.
- [ ] Код групується зі станом, який він модифікує.
- [ ] Поля дати та методи зберігаються в одиницях.
- [x] Побічні ефекти заборонені.

[Функціональне програмування](https://medium.com/javascript-scene/master-the-javascript-interview-what-is-functional-programming-7f218c68b3a0)

#### Q42.Ваш код видає помилку: TypeError: Cannot read property 'reduce' of undefined. Що це означає?

- [x] Ви визиваєте метод з назвою reduce у об'єкті, який оголошений, але не має значення.
- [ ] Ви визиваєте метод з назвою reduce на об'єкті, який не існує.
- [ ] Ви визиваєте метод з назвою reduce на порожньому масиві.
- [ ] Ви визиваєте метод з назвою reduce на об'єкті, який має значення null.

** Пояснення **: `Ви не можете викликати reduce на undefined об'єкті... Це видасть помилку (your object is not defined...)`

#### Q43.Скільки прототипних об'єктів знаходяться в ланцюзі для наступного масиву?

`let arr = [];`

- [ ] 3
- [x] 2
- [ ] 0
- [ ] 1

[Прототип масиву](https://www.w3schools.com/jsref/jsref_prototype_array.asp)

#### Q44. Який варіант _не є_ унарним оператором?

- [ ] `typeof`
- [ ] `delete`
- [x] `instanceof`
- [ ] `void`

[Унарні оператори](https://www.digitalocean.com/community/tutorials/javascript-unary-operators-simple-and-useful#:~:text=A%20unary%20operation%20is%20an,therefore%20their%20functionality%20is%20guaranteed.)

#### Q45.Яку область видимості має змінна end в показаному коді?

```js
var start = 1;
if (start === 1) {
  let end = 2;
}
```

- [ ] умовну
- [X] блочну
- [ ] глобальну
- [ ] функціональну

[Блочна проти функціональної видимості](https://josephcardillo.medium.com/the-difference-between-function-and-block-scope-in-javascript-4296b2322abe)

#### Q46.Яким буде значення y в цьому коді:

```js
const x = 6 % 2;
const y = x ? 'One' : 'Two';
```

- [ ] One
- [ ] undefined
- [ ] TRUE
- [x] Two

[Тернарний оператор](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_Operator)

#### Q47.Яке ключове слово використовується для створення помилки?

- [x] `throw`
- [ ] `exception`
- [ ] `catch`
- [ ] `error`

[Викидання помилок](<https://www.w3schools.com/jsref/jsref_throw.asp#:~:text=The%20throw%20statement%20throws%20(generates,to%20create%20a%20custom%20error.)>)

#### Q48. Яка різниця між async так defer атрибутами в HTML script тегу?

- [ ]  атрибут defer може працювати синхронно.
- [ ]  атрибут defer працює лише з генераторами.
- [ ]  атрибут defer працює лише з промісами.
- [x]  атрибут defer асинхронно завантажуватиме скрипти.

[Async проти defer](https://www.digitalocean.com/community/tutorials/html-defer-async#:~:text=%3E-,Async%20vs%20Defer,order%20as%20they%20are%20called.)

#### Q49.Наступна програма має проблему.Що це?

```js
var a;
var b = (a = 3) ? true : false;
```

- [x] Умова у тернарному виразі використовує оператор призначення
- [ ] Ви не можете визначити змінну, не ініціалізуючи її.
- [ ] Ви не можете використовувати тернарність у правій частині оператора призначення.
- [ ] Код використовує застаріле ключове слово var.

[Тернарний оператор](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_Operator)

#### Q50.Яке твердження є дійсним посиланням на вузол DOM, створений показаним кодом?

```html
<p class="pull">lorem ipsum</p>
```

- [ ] `Document.querySelector('class.pull')`
- [x] `document.querySelector('.pull');`
- [ ] `Document.querySelector('pull')`
- [ ] `Document.querySelector('#pull')`

[Query selector](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelector)

#### Q51.Яке значення повертає цей код?

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

[Умови](https://www.javascript.com/learn/conditionals)

#### Q52.Яким буде результат у консолі після запуску показаного коду?

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

[Довідка](https://webdoky.org/uk/docs/Web/JavaScript/Closures/)

#### Q53.Що цей код буде записувати в консолі?

```js
function sayHello() {
  console.log('hello');
}

console.log(sayHello.prototype);
```

- [ ] undefined
- [ ] "hello"
- [x] Об'єкт з властивістю конструктора
- [ ] Повідомлення про помилку

[Прототипи](https://webdoky.org/uk/docs/Web/JavaScript/Inheritance_and_the_prototype_chain/)

#### Q54.Який тип колекції дозволяє вставляти унікальне значення лише один раз?

- [ ] Object
- [x] Set
- [ ] Array
- [ ] Map

[Sets](https://webdoky.org/uk/docs/Web/JavaScript/Reference/Global_Objects/Set/)

#### Q55.Які два значення надрукує цей код?

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

[Довідка](https://webdoky.org/uk/docs/Web/JavaScript/Closures/)

#### Q56.Чим метод `forEach()` відрізняється від `for`?

- [ ] forEach дозволяє вказати власний ітератор, тоді як for - ні.
- [ ] forEach можна використовувати лише з рядками, for - з різними типами даних.
- [x] forEach можна використовувати лише з масивами, for - з різними типами даних.
- [ ] for цикли можуть бути вкладеними; тоді як forEach цикли - ні.

[Різниця між forEach та for циклами](https://www.geeksforgeeks.org/difference-between-foreach-and-for-loop-in-javascript/)

#### Q57. Який варіант є недійсним для визначення стрілкової функції яка повертає порожній об'єкт?

- [ ] => `({})`
- [x] => `{}`
- [ ] => `{ return {};}`
- [ ] => `(({}))`

[Стрілкові функції](https://webdoky.org/uk/docs/Web/JavaScript/Reference/Functions/Arrow_functions/)

#### Q58.Чому ви можете вирішити зробити код асинхронним?

- [x] запустити задачі, які можуть зайняти деякий час, не блокуючи подальші задачі для негайного виконання
- [ ] щоб переконатися, що задачі нижче у коді не запускаються, доки попередні не будуть завершені
- [ ] щоб зробити код швидше
- [ ] щоб забезпечити стек виклику LIFO (Last in, First Out)

**Пояснення:** `"щоб переконатися, що задачі нижче у коді не запускаються, доки попередні не будуть завершені" Ви використовуєте нормальний (синхронний) потік, де кожна команда виконується послідовно. Асинхронний код дозволяє порушити цю послідовність: запустити тривалу функцію (виклик AJAX до зовнішньої служби) і продовжуйте запускати решту коду паралельно.

#### Q59.Який вираз повертає true?

- [ ] `[3] == [3]`
- [x] `3 == '3'`
- [ ] `3 != '3'`
- [ ] `3 === '3'`

1. [Booleans](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean)
2. [Довідка 2 - booleans](https://www.scaler.com/topics/boolean-in-javascript/)

#### Q60. Що з цього є дійсною назвою змінної?

- [ ] 5thItem
- [x] firstName
- [ ] grand total
- [ ] function

[Конвенції кодування](https://www.w3schools.com/js/js_conventions.asp)

#### Q61.Який метод скасовує поведінку події за замовчуванням?

- [ ] `cancel()`
- [ ] `stop()`
- [x] `preventDefault()`
- [ ] `prevent()`

[Події](https://developer.mozilla.org/en-US/docs/Web/API/Event/preventDefault)

#### Q62.Яким методом скористатися, щоб приєднати один вузол DOM до іншого?

- [ ] `attachNode()`
- [ ] `getNode()`
- [ ] `querySelector()`
- [x] `appendChild()`

[Node interface](https://developer.mozilla.org/en-US/docs/Web/API/Node/appendChild)

#### Q63.Яке твердження можна використовувати для пропускання ітерації в циклі?

- [ ] `break`
- [ ] `pass`
- [ ] `skip`
- [x] `continue`

[Break проти continue](https://www.w3schools.com/js/js_break.asp)

#### Q64. Який варіант є дійсним прикладом для стрілкової функції?

- [x] `(a,b) => c`
- [ ] `a, b => {return c;}`
- [ ] `a, b => c`
- [ ] `{ a, b } => c`

[Стрілкові функції](https://webdoky.org/uk/docs/Web/JavaScript/Reference/Functions/Arrow_functions/)

#### Q65. Яка концепція визначається як шаблон, який можна використовувати для створення різних об'єктів, які поділяють певну форму та/або поведінку?

- [x] class
- [ ] generator function
- [ ] map
- [ ] proxy

[Класи](https://webdoky.org/uk/docs/Web/JavaScript/Reference/Classes/)

#### Q66. Як додати коментар до коду JavaScript?

- [ ] `! This is a comment`
- [ ] `# This is a comment`
- [ ] `\\ This is a comment`
- [x] `// This is a comment`

[Коментарі](https://www.w3schools.com/js/js_comments.asp)

#### Q67. Якщо ви намагаєтесь викликати значення як функцію, але значення не є функцією, яку помилку ви отримаєте?

- [x] TypeError
- [ ] SystemError
- [ ] SyntaxError
- [ ] LogicError

[Помилки](https://webdoky.org/uk/docs/Web/JavaScript/Reference/Global_Objects/Error/)

#### Q68. Який метод викликається автоматично, коли об'єкт ініціалізований?

- [ ] create()
- [ ] new()
- [x] constructor()
- [ ] init()

[Конструктори](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/constructor)

#### Q69.Який результат запуску показаного виразу?

```js
let a = 5;
console.log(++a);
```

- [ ] 4
- [ ] 10
- [x] 6
- [ ] 5

[++x проти x++](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Increment)

#### Q70. Ви написали слухача події, показаного нижче для кнопки форми, але кожного разу, коли ви натискаєте кнопку, сторінка перезавантажується. Яке твердження не дозволило б цьому відбутися?

```js
button.addEventListener(
  'click',
  function (e) {
    button.className = 'clicked';
  },
  false,
);
```

- [ ] `e.blockReload();`
- [ ] `button.preventDefault();`
- [ ] `button.blockReload();`
- [x] `e.preventDefault();`

[Події](https://developer.mozilla.org/en-US/docs/Web/API/Event/preventDefault)

#### Q71. Який вираз являє собою стартовий код IIFE?

- [ ] `function() { console.log('lorem ipsum'); }()();`
- [ ] `function() { console.log('lorem ipsum'); }();`
- [x] `(function() { console.log('lorem ipsum'); })();`

[Що таке Immediately Invoked Function Expression](https://javascript.plainenglish.io/https-medium-com-javascript-in-plain-english-stop-feeling-iffy-about-using-an-iife-7b0292aba174)

#### Q72. Яке твердження вибирає всі елементи IMG у дереві DOM?

- [ ] `Document.querySelector('img')`
- [ ] `Document.querySelectorAll('<img>')`
- [x] `Document.querySelectorAll('img')`
- [ ] `Document.querySelector('<img>')`

[Довідка query selector](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelector)

#### Q73. Чому б ви вибрали асинхронну структуру для свого коду?

- [ ] Використовувати синтаксис ES6
- [x] Щоб розпочати завдання, які можуть зайняти деякий час, не блокуючи подальші завдання від виконання негайно
- [ ] Щоб аналізатори виконували всі правила синтаксису JavaScript при обробці коду
- [ ] Щоб завдання подальші не ініціювались до тих пір, поки не виконані попередні

[Довідка async function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function)

#### Q74. Яке дієслово підходить для HTTP запиту вмісту існуючого ресурсу?

- [ ] DELETE
- [x] GET
- [ ] PATCH
- [ ] POST

[Довідка http методи](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)

#### Q75. Яка подія ініціюється на текстовому полі форми, коли користувач переходить на нього за допомогою tab чи клацає або тапає його?

- [x] focus
- [ ] blur
- [ ] hover
- [ ] enter

[Події](https://developer.mozilla.org/en-US/docs/Web/Events)

#### Q76.Який результат запуску цього коду у консолі?

```js
function logThis() {
  console.log(this);
}
logThis();
```

- [ ] function
- [ ] undefined
- [ ] Function.prototype
- [x] window

[Що таке window](https://www.w3schools.com/js/js_window.asp)

#### Q77. Який класовий компонент еквівалентний цьому функціональному компоненту?

```js
const Greeting = ({ name }) => <h1>Hello {name}!</h1>;
```

- [x] `class Greeting extends React.Component { render() { return <h1>Hello {this.props.name}!</h1>; } }`
- [ ] `class Greeting extends React.Component { constructor() { return <h1>Hello {this.props.name}!</h1>; } }`
- [ ] `class Greeting extends React.Component { <h>Hello {this.props.name}!</h>; } }`
- [ ] `class Greeting extends React.Component { render({ name }) { return <h1>Hello {name}!</h1>; } }`

#### Q79.Який вихід цього коду?

```js
var obj;
console.log(obj);
```

- [ ] `ReferenceError: obj is not defined`
- [ ] `{}`
- [x] `undefined`
- [ ] `null`

[Робота з об'єктами](https://webdoky.org/uk/docs/Web/JavaScript/Guide/Working_with_objects/)

#### Q80. Як би ви використовували TaxCalculator для визначення суми податку на \$50?

```js
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

[Функції](https://www.w3schools.com/js/js_functions.asp)

#### Q81. Що не так з цим кодом?

```js
const foo = {
  bar() {
    console.log('Hello, world!');
  },
  name: 'Albert',
  age: 26,
};
```

- [ ] Функцію bar потрібно визначити як пару ключ/значення.
- [ ] Коми в кінці не дозволено в JavaScript.
- [ ] Функції не може бути оголошено як властивості об'єктів.
- [x] Нічого, помилок немає.

1. [Функції](https://www.w3schools.com/js/js_functions.asp)
2. [Робота з об'єктами](https://webdoky.org/uk/docs/Web/JavaScript/Guide/Working_with_objects/)

#### Q82.Що буде показано в консолі?

```js
console.log('Я');
setTimeout(() => {
  console.log('люблю');
}, 0);
console.log('Javascript!');
```

- [x] .

```plaintext
Я
Javascript!
люблю
```

- [ ] .

```plaintext
люблю
Я
Javascript!
```

- [ ] Вихід може змінюватися з кожним виконанням коду і не може бути визначений.

- [ ] .

```plaintext
Я
люблю
Javascript!
```

**Довідка**
https://developer.mozilla.org/en-US/docs/Web/API/setTimeout#reasons_for_delays_longer_than_specified особливо подивіться розділ 'late timeouts' .

#### Q83.Що буде виведено в консолі?

```js
const foo = [1, 2, 3];
const [n] = foo;
console.log(n);
```

- [x] 1
- [ ] undefined
- [ ] NaN
- [ ] Ніщо--це не належний синтаксис JavaScript і кине помилку.

[Присвоєння з деструктуруванням](https://webdoky.org/uk/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment/)

#### Q84. Як видалити назву властивості з цього об'єкта?

```js
const foo = {
  name: 'Albert',
};
```

- [ ] delete name from foo;
- [x] delete foo.name;
- [ ] del foo.name;
- [ ] remove foo.name;

[Робота з об'єктами](https://webdoky.org/uk/docs/Web/JavaScript/Guide/Working_with_objects/)

#### Q85. Яка різниця між `map()` та `forEach()` методами у Array prototype?

- [ ] Різниці немає.
- [ ] метод `forEach()` повертає едине вихідне значення, тоді як метод `map()` виконує операцію на кожному значенні в масиві.
- [x] метод `map()` повертає новий масив з перетворенням, що застосовується на кожному елементі вихідного масиву, тоді як метод `forEach()` пробігає через масив без зворотного значення.
- [ ] метод `forEach()` повертає новий масив з перетворенням, що застосовується на кожному елементі вихідного масиву, тоді як метод `map()` пробігає через масив без зворотного значення.

1. [Map](https://webdoky.org/uk/docs/Web/JavaScript/Reference/Global_Objects/Map/)
2. [Довідка - різниця між forEach та for циклами](https://www.geeksforgeeks.org/difference-between-foreach-and-for-loop-in-javascript/)

#### Q86. Яку концепцію ілюструє цей код?

```js
function makeAdder(x) {
  return function (y) {
    return x + y;
  };
}

var addFive = makeAdder(5);
console.log(addFive(3));
```

- [ ] перегрузка
- [ ] замикання
- [x] каррінг
- [ ] перевизначення

[Каррінг](https://uk.javascript.info/currying-partials)

#### Q87. Яка пара тегів використовується в HTML для вбудовування JavaScript?

- [x] `<script></script>`
- [ ] `<js></js>`
- [ ] `<javascript></javascript>`
- [ ] `<code></code>`

[Тег “script”](https://uk.javascript.info/hello-world#teg-script)

#### Q88. If your app receives data from a third-party API, which HTTP response header must the server specify to allow exceptions to the same-origin policy?

- [ ] Security-Mode
- [x] Access-Control-Allow-Origin
- [ ] Different-Origin
- [ ] Same-Origin

[Reference Cross-Origin Resource Sharing](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)

#### Q89. What is the output of this code?

```js
let rainForests = ['Amazon', 'Borneo', 'Cerrado', 'Congo'];
rainForests.splice(0, 2);
console.log(rainForests);
```

- [ ] `["Amazon","Borneo","Cerrado","Congo"]`
- [x] `["Cerrado", "Congo"]`
- [ ] `["Congo"]`
- [ ] `["Amazon","Borneo"]`

[Reference array methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)

#### Q90. Which missing line would allow you to create five variables(one,two,three,four,five) that correspond to their numerical values (1,2,3,4,5)?

```js
const numbers = [1, 2, 3, 4, 5];
//MISSING LINE
```

- [x] `const [one,two,three,four,five]=numbers`
- [ ] `const {one,two,three,four,five}=numbers`
- [ ] `const [one,two,three,four,five]=[numbers]`
- [ ] `const {one,two,three,four,five}={numbers}`

[Reference array destructuring](https://webdoky.org/uk/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment/)

#### Q91. What will this code print?

```js
const obj = {
  a: 1,
  b: 2,
  c: 3,
};

const obj2 = {
  ...obj,
  a: 0,
};

console.log(obj2.a, obj2.b);
```

- [ ] Nothing, it will throw an error
- [x] 0 2
- [ ] undefined 2
- [ ] undefined 2

[Reference spread syntax es6](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax)

#### Q92. Which line could you add to this code to print "jaguar" to the console?

```js
let animals = ['jaguar', 'eagle'];
//Missing Line
console.log(animals.pop()); //Prints jaguar
```

- [ ] `animals.filter(e => e === "jaguar");`
- [ ] `animals.reverse();`
- [ ] `animals.shift();`
- [x] `animals.pop();`

[Reference Javascript Array pop()](https://www.w3schools.com/jsref/jsref_pop.asp)

shift() - removes the FIRST element of an array and returns the removed item.

pop() - removes the LAST element of an array and returns the removed item.

reverse() - reverses the order of the elements in an array.

filter() - get every element in the array that meets the condition.

#### Q93. What line is missing from this code?

```js
//Missing Line
for (var i = 0; i < vowels.length; i++) {
  console.log(vowels[i]);
  //Each letter printed on a separate line as follows;
  //a
  //e
  //i
  //o
  //u
}
```

- [ ] `let vowels = "aeiou".toArray();`
- [ ] `let vowels = Array.of("aeiou");`
- [ ] `let vowels = {"a", "e", "i", "o", "u"};`
- [x] `let vowels = "aeiou";`

[Reference working with arrays](https://www.w3schools.com/js/js_arrays.asp)

#### Q94. What will be logged to the console?

```js
const x = 6 % 2;
const y = x ? 'One' : 'Two';
console.log(y);
```

- [ ] undefined
- [ ] One
- [ ] true
- [x] Two

**Note:** `this question is same with Q46.`
[Reference ternary operator js](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_Operator)

#### Q95. How would you access the word It from this multidimensional array?

`let matrix = [["You","Can"],["Do","It"],["!","!","!"]];`

- [ ] `matrix[1[2]]`
- [x] `matrix[1][1]`
- [ ] `matrix[1,2]`
- [ ] `matrix[1][2]`

#### Q96. What does this code do?

```js
const animals = ['Rabbit', 'Dog', 'Cat'];
animals.unshift('Lizard');
```

- [x] It adds "Lizard" to the start of the animals array.
- [ ] It adds "Lizard" to the end of the animals array.
- [ ] It replaces "Rabbit" with "Lizard" in the animals array.
- [ ] It replaces "Cat" with "Lizard" in the animals array.

[Reference working with arrays](https://www.w3schools.com/js/js_arrays.asp)

#### Q97. What is the output of this code?

```js
let x = 6 + 3 + '3';
console.log(x);
```

- [x] 93
- [ ] 12
- [ ] 66
- [ ] 633

[Reference type coercion](https://www.freecodecamp.org/news/js-type-coercion-explained-27ba3d9a2839/)

#### Q98. Which statement can take a single expression as input and then look through a number of choices until one that matches that value is found?

- [ ] else
- [ ] when
- [ ] if
- [x] switch

[Reference switch](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/switch)

#### Q99. Which statement prints "roar" to the console?

```js
var sound = 'grunt';
var bear = { sound: 'roar' };
function roar() {
  console.log(this.sound);
}
```

- [ ] `bear.bind(roar);`
- [ ] `roar.bind(bear);`
- [x] `roar.apply(bear);`
- [ ] `bear[roar]();`

1. [Reference Apply](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/apply)
2. [Reference this](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this)
3. [Reference bind](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_objects/Function/bind)

#### Q100. Which choice is a valid example of an arrow function, assuming c is defined in the outer scope?

- [ ] `a, b => { return c; }`
- [ ] `a, b => c`
- [ ] `{ a, b } => c`
- [x] `(a,b) => c`

[Reference arrow functions](https://webdoky.org/uk/docs/Web/JavaScript/Reference/Functions/Arrow_functions/)

#### Q101. Which statement correctly imports this code from some-file.js?

```js
//some-file.js
export const printMe = (str) => console.log(str);
```

- [ ] `import printMe from './some-file';`
- [x] `import { printMe } from './some-file';`
- [ ] `import default as printMe from './some-file';`
- [ ] `const printMe = import './some-file';`

[Reference importing libraries in javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import)

#### Q102. What will be the output of this code?

```js
const arr1 = [2, 4, 6];
const arr2 = [3, 5, 7];

console.log([...arr1, ...arr2]);
```

- [ ] `[2, 3, 4, 5, 6, 7]`
- [ ] `[3,5,7,2,4,6]`
- [ ] `[3, 5, 7, 2, 4, 6]`
- [ ] `[[2, 4, 6], [3, 5, 7]]`
- [x] `[2, 4, 6, 3, 5, 7]`

[Reference spread syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax)

#### Q103. Which method call is chained to handle a successful response returned by `fetch()`?

- [ ] `done()`
- [x] `then()`
- [ ] `finally()`
- [ ] `catch()`

[Reference fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch)

#### Q104. Which choice is not an array method?

- [ ] `array.slice()`
- [ ] `array.shift()`
- [ ] `array.push()`
- [x] `array.replace()`

[Reference working with arrays](https://www.w3schools.com/js/js_arrays.asp)

#### Q105. Which JavaScript loop ensures that at least a singular iteration will happen?

- [x] do…while
- [ ] forEach
- [ ] while
- [ ] for

[Reference loops in js](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/do...while)

#### Q106. What will be logged to the console?

```js
console.log(typeof 'blueberry');
```

- [x] `string`
- [ ] `array`
- [ ] `Boolean`
- [ ] `object`

[Reference what is typeof](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof)

#### Q107. What is the output that is printed when the div containing the text "Click Here" is clicked?

```html
//HTML Markup
<div id="A">
  <div id="B">
    <div id="C">Click Here</div>
  </div>
</div>
```

```js
//JavaScript
document.querySelectorAll('div').forEach((e) => {
  e.onclick = (e) => console.log(e.currentTarget.id);
});
```

- [x] C B A
- [ ] A
- [ ] C
- [ ] A B C

1. [Reference query selector](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelector)
2. [Reference events](https://developer.mozilla.org/en-US/docs/Web/Events)

#### Q108. What will this code log to the console?

```js
const myNumbers = [1, 2, 3, 4, 5, 6, 7];
const myFunction = (arr) => {
  return arr.map((x) => x + 3).filter((x) => x < 7);
};
console.log(myFunction(myNumbers));
```

- [ ] `[4,5,6,7,8,9,10]`
- [ ] `[4,5,6,7]`
- [ ] `[1,2,3,4,5,6]`
- [x] `[4,5,6]`

[Reference functions in javascript](https://www.w3schools.com/js/js_functions.asp)

#### Q109. What does this code print to the console?

```js
let rainForestAcres = 10;
let animals = 0;

while (rainForestAcres < 13 || animals <= 2) {
  rainForestAcres++;
  animals += 2;
}

console.log(animals);
```

- [ ] 2
- [ ] 4
- [x] 6
- [ ] 8

[Reference MDN JavaScript Looping code](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Looping_code)

#### Q110. Which snippet could you add to this code to print "YOU GOT THIS" to the console?

```js
let cipherText = [...'YZOGUT QGMORTZ MTRHTILS'];
let plainText = '';

/* Missing Snippet */

console.log(plainText); //Prints YOU GOT THIS
```

- [ ] A

```js
for (let key of cipherText.keys()) {
  plainText += key % 2 === 0 ? key : ' ';
}
```

- [ ] B

```js
for (let [index, value] of cipherText.entries()) {
  plainText += index % 2 !== 0 ? value : '';
}
```

- [x] C

```js
for (let [index, value] of cipherText.entries()) {
  plainText += index % 2 === 0 ? value : '';
}
```

- [ ] D

```js
for (let value of cipherText) {
  plainText += value;
}
```

1. [Reference MDN JavaScript Destructuring](https://webdoky.org/uk/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment/)
2. [Reference MDN JavaScript Array entries](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/entries)
3. [Reference MDN JavaScript Remainder/Modulo](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Remainder)

#### Q111. Which Pokemon will be logged to the console?

```js
var pokedex = ['Snorlax', 'Jigglypuff', 'Charmander', 'Squirtle'];
pokedex.pop();
console.log(pokedex.pop());
```

- [x] Charmander
- [ ] Jigglypuff
- [ ] Snorlax
- [ ] Squirtle

**Explanation**: `The pop() method removes the last element from an array and returns that element. This method changes the length of the array.`

[Reference Array.pop](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/pop)

#### Q112. Which statement can be used to select the element from the DOM containing the text "The LinkedIn Learning library has great JavaScript courses" from this markup?

```html
<h1 class="content">LinkedIn Learning</h1>
<div class="content">
  <span class="content">The LinkedIn Learning library has great JavaScript courses!</span>
</div>
```

- [ ] document.querySelector("div.content")
- [x] document.querySelector("span.content")
- [ ] document.querySelector(".content")
- [ ] document.querySelector("div.span")

#### Q113. Which value is not falsey?

- [x] `[]`
- [ ] `undefined`
- [ ] `0`
- [ ] `null`

[Reference Falsy](https://developer.mozilla.org/en-US/docs/Glossary/Falsy)

#### Q114. What line of code causes this code segment to throw an error?

```js
const lion = 1;
let tiger = 2;
var bear;

++lion;
bear += lion + tiger;
tiger++;
```

- [x] `line 5, because lion cannot be reassigned a value`
- [ ] `line 6, because the += operator cannot be used with the undefined variable bear`
- [ ] `line 5, because the prefix (++) operator does not exist in JavaScript`
- [ ] `line 3, because the variable bear is left undefined`

1. [Reference const in js](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const)
2. [Reference TypeError: invalid assignment to const "x"](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Invalid_const_assignment)

#### Q115. What will be the value of `result` after running this code?

```js
const person = { name: 'Dave', age: 40, hairColor: 'blue' };
const result = Object.keys(person).map((x) => x.toUpperCase());
```

- [ ] It will throw a TypeError.
- [ ] `["Name", "Age", "HairColor"]`
- [ ] `["DAVE", 40, "BLUE"]`
- [x] `["NAME", "AGE", "HAIRCOLOR"]`

1. [Reference Object.keys()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/keys)
2. [Reference Array.prototype.map()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map)
3. [Reference String.prototype.toUpperCase()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/toUpperCase)

#### Q116. Which snippet could you insert to this code to print "swim" to the console?

```js
let animals = ["eagle", "osprey", "salmon"];
let key = animal => animal === "salmon";

if(/* Insert Snippet Here */){
  console.log("swim");
}
```

- [ ] `animals.every(key)`
- [ ] `animals.some(key).length === 1`
- [ ] `animals.filter(key) === true`
- [x] `animals.some(key)`

[Reference Array.prototype.some](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/some)

#### Q117. What is the output of this code?

```js
class RainForest {
  static minimumRainFall = 60;
}

let congo = new RainForest();
RainForest.minimumRainFall = 80;
console.log(congo.minimumRainFall);
```

- [x] `undefined`
- [ ] `None of these answers, as static is not a feature in Javascript.`
- [ ] `60`
- [ ] `80`

[Reference Classes static](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/static)

#### Q118. How can you attempt to access the property `a.b` on `obj` without throwing an error if a is undefined?

```js
let obj = {};
```

- [ ] `obj?.a.b`
- [x] `obj.a?.b`
- [ ] `obj[a][b]`
- [ ] `obj.?a.?b`

[Reference Optional chaining (?.)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Optional_chaining)

#### Q119. What happens when you run this code?

```js
if (true) {
  var x = 5;
  const y = 6;
  let z = 7;
}
console.log(x + y + z);
```

- [ ] It will throw a `ReferenceError` about `x`.
- [ ] It will print `18`.
- [ ] It will print `undefined`.
- [x] It will throw a `ReferenceError` about `y`.

[Reference let statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let)

#### Q120. What does this code print to the console?

```js
const x = [1, 2];
const y = [5, 7];
const z = [...x, ...y];
console.log(z);
```

- [x] `[1,2,5,7]`
- [ ] `[[1, 2], [5, 7]]`
- [ ] `[2,7]`
- [ ] `[2,1,7,5]`

[Reference spread syntax (...)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax)

#### Q121. Given this code, which statement will be evaluated as false?

```js
const a = { x: 1 };
const b = { x: 1 };
```

- [ ] `a['x'] === b['x']`
- [ ] `a != b`
- [x] `a === b`
- [ ] `a.x === b.x`

[Reference](http://adripofjavascript.com/blog/drips/object-equality-in-javascript.html)

#### Q122. What will this code log to the console?

```js
console.log(typeof 41.1);
```

- [ ] `Nothing. It resuults in a ReferenceError.`
- [ ] `decimal`
- [ ] `float`
- [x] `number`

[Reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof#basic_usage)

#### Q123. What is the output of this code?

```js
let scores = [];
scores.push(1, 2);
scores.pop();
scores.push(3, 4);
scores.pop();
score = scores.reduce((a, b) => a + b);
console.log(score);
```

- [ ] `3`
- [x] `4`
- [ ] `6`
- [ ] `7`

1. [Reference Array.prototype.push()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/push)
2. [Reference Array.prototype.pop()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/pop)
3. [Reference Array.prototype.reduce()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce)

#### Q124. What does this code print to the console?

```js
let bear = {
  sound: 'roar',
  roar() {
    console.log(this.sound);
  },
};

bear.sound = 'grunt';
let bearSound = bear.roar;
bearSound();
```

- [ ] `Nothing is printed to the console.`
- [ ] `grunt`
- [x] `undefined`
- [ ] `roar`

[Reference](https://webdoky.org/uk/docs/Web/JavaScript/Guide/Working_with_objects/)

#### Q125. What is the output of this code?

```js
var cat = { name: 'Athena' };

function swap(feline) {
  feline.name = 'Wild';
  feline = { name: 'Tabby' };
}

swap(cat);
console.log(cat.name);
```

- [ ] undefined
- [x] Wild
- [ ] Tabby
- [ ] Athena

#### Q126. What will this code output to the log?

```js
var thing;
let func = (str = 'no arg') => {
  console.log(str);
};
func(thing);
func(null);
```

- [ ] null no arg
- [ ] no arg no arg
- [ ] null null
- [x] no arg null

#### Q127. What will this code print to the console?

```js
const myFunc = () => {
  const a = 2;
  return () => console.log('a is ' + a);
};
const a = 1;
const test = myFunc();
test();
```

- [ ] a is 1
- [ ] a is undefined
- [ ] It won't print anything.
- [x] a is 2

#### Q128. What will this code print to the console?

```js
const myFunc = (num1, num2 = 2, num3 = 2) => {
  return num1 + num2 + num3;
};
let values = [1, 5];
const test = myFunc(2, ...values);
console.log(test);
```

- [x] 8
- [ ] 6
- [ ] 2
- [ ] 12

#### Q129. Which code would you use to access the Irish flag?

```js
var flagsJSON =
  '{ "countries" : [' +
  '{ "country":"Ireland" , "flag":"🇮🇪" },' +
  '{ "country":"Serbia" , "flag":"🇷🇸" },' +
  '{ "country":"Peru" , "flag":"🇵🇪" } ]}';

var flagDatabase = JSON.parse(flagsJSON);
```

- [ ] flagDatabase.countries[1].flag
- [x] flagDatabase.countries[0].flag
- [ ] flagDatabase[1].flag
- [ ] flagsJSON.countries[0].flag

#### Q130. Which snippet allows the acresOfRainForest variable to increase?

```js
let conservation = true;
let deforestation = false;
let acresOfRainForest = 100;
if (/* Snipped goes here */){
    ++acresOfRainForest;
}
```

- [x] conservation && !deforestation
- [ ] !deforestation && !conservation
- [ ] !conservation || deforestation
- [ ] deforestation && conservation || deforestation

#### Q131. Which of these evaluate to true?

- [x] Boolean("false")
- [ ] Boolean("")
- [ ] Boolean(0)
- [ ] Boolean(NaN)

#### Q132. How would you add a data item named animal with a value of sloth to local storage for the current domain?

- [ ] LocalStorage.setItem("animal","sloth");
- [ ] document.localStorage.setItem("animal","sloth");
- [ ] localStorage.setItem({animal:"sloth"});
- [x] localStorage.setItem("animal","sloth");

[Reference](https://blog.logrocket.com/localstorage-javascript-complete-guide/#setitem)

#### Q133. What value is printed to the console after this code execute?

```js
let cat = Object.create({ type: 'lion' });
cat.size = 'large';

let copyCat = { ...cat };
cat.type = 'tiger';

console.log(copyCat.type, copyCat.size);
```

- [ ] tiger large
- [ ] lion undefined
- [x] undefined large
- [ ] lion large

[Reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/create)

#### Q134. What does this code print to the console?

```js
let animals = [{ type: 'lion' }, 'tiger'];
let clones = animals.slice();

clones[0].type = 'bear';
clones[1] = 'sheep';

console.log(animals[0].type, clones[0].type);
console.log(animals[1], clones[1]);
```

- [x] bear bear
      tiger sheep
- [ ] lion bear
      sheep sheep
- [ ] bear bear
      tiger tiger
- [ ] lion bear
      tiger sheep

[Reference](https://blog.logrocket.com/localstorage-javascript-complete-guide/#setitem)

#### Q135. What will be the output of the following code?

```js
a=5;
b=4;
alert(a++(+(+(+b))));
```

- [ ] 18
- [ ] 10
- [x] 9
- [ ] 20

#### Q136. Which snippet could you add to this code to print "{"type": "tiger"}" to the console?

```js
let cat = { type: "tiger", size: "large" };

let json = /* Snippet here */;

console.log(json); // print {"type":"tiger"}
```

- [ ] `cat.toJSON("type");`
- [x] `JSON.stringify(cat, ["type"]);`
- [ ] `JSON.stringify(cat);`
- [ ] `JSON.stringify(cat, /type/);`

[Reference](https://www.w3schools.com/jsref/jsref_stringify.asp)

#### Q137. Which document method is not used to get a reference to a DOM node?

- [x] document.getNode();
- [ ] document.getElementsByClassName();
- [ ] document.querySelectorAll();
- [ ] document.querySelector();

[Reference](<https://developer.mozilla.org/en-US/docs/Web/API/Document/getElementById#:~:text=querySelector()%20and%20Document.,element%20objects%20in%20the%20DOM.>)

#### Q138. In JavaScript, all objects inherit a built-in property from a **\*\*\*\***\_\_\_**\*\*\*\***.

- [ ] node
- [ ] instance variable
- [x] prototype
- [ ] accessor

[Reference](https://www.freecodecamp.org/news/javascript-prototype-explained-with-examples/)

#### Q139. Which of the following are not server-side Javascript objects?

- [ ] Date
- [x] FileUpload
- [ ] Function
- [ ] All of the above

[Reference](https://docs.oracle.com/cd/E19957-01/816-6411-10/jsserv.htm#1035757)

#### Q140. What will be the output of the following code snippet?

```javascript
const obj1 = { first: 20, second: 30, first: 50 };
console.log(obj1);
```

- [ ] first: 30 , second: 50
- [x] first: 50 , second: 30
- [ ] first: 30 , second: 20
- [ ] None of the above

#### Q141. Which object in Javascript doesn’t have a prototype?

- [x] Base Object
- [ ] All objects have prototype
- [ ] None of the objects have prototype
- [ ] None of the above

[Reference](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object_prototypes)

#### Q142. What does … operator do in JS?

- [x] Used to spread iterables to individual elements
- [ ] Describe datatype of undefined
- [ ] No such operator exists
- [ ] None of the above

#### Q143. How to stop an interval timer in Javascript?

- [x] clearInterval
- [ ] clearTimer
- [ ] intervalOver
- [ ] None of the above

[Reference](https://www.interviewbit.com/javascript-mcq/)

#### Q144. What will be the output of the following code snippet?

```javascript
print(typeof NaN);
```

- [ ] Object
- [x] Number
- [ ] String
- [ ] None of the above

#### Q145. What will be the output of the following code snippet?

```javascript
<script type="text/javascript">a = 5 + "9"; document.write(a);</script>
```

- [ ] Compilation Error
- [ ] 14
- [ ] Runtime Error
- [x] 59

#### Q146. Which of the following methods can be used to display data in some form using Javascript?

- [ ] document.write()
- [ ] console.log()
- [ ] window.alert()
- [x] all of the above

#### Q147. What value is assigned to total after this code executes?

```javascript
function sum(num1, num2 = 2, num3 = 3) {
  return num1 + num2 + num3;
}
let values = [1, 5];
let total = sum(4, ...values);
```

- [x] 10
- [ ] 6
- [ ] 7
- [ ] 8

[Reference: Rest parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters)

#### Q148. Which statement is applicable to the defer attribute of the HTML <script> tag?

- [x] defer allows the browser to continue processing the page while the script loads in the background.
- [ ] defer causes the script to be loaded from the backup content delivery network (CDN).
- [ ] defer blocks the browser from processing HTML below the tag until the script is completely loaded.
- [ ] defer lazy loads the script, causing it to download only when it is called by another script on the page.

[Reference: defer html script attribute](https://www.w3schools.com/tags/att_script_defer.asp)

#### Q149. Which method of a class is called to initialize an object of that class?

- [ ] init()
- [ ] create()
- [ ] new()
- [x] constructor()

[Reference: constructor method](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/constructor)

#### Q150. Which expression evaluates to true?

- [ ] Boolean(NaN)
- [ ] Boolean(0)
- [x] Boolean("false")
- [ ] Boolean("")

[Reference: Boolean object](https://www.w3schools.com/js/js_booleans.asp)

#### Q151. How would you check if the word "pot" is in the word "potato"?

- [ ] "pot".indexOf("potato") !== -1
- [ ] "potato".includes("Pot")
- [x] "potato".includes("pot")
- [ ] "potato".contains("pot");

[Reference: String.prototype.includes()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/includes)

#### Q152. Which collection object allows a unique value to be inserted only once?

- [ ] Map
- [ ] Array
- [x] Set
- [ ] Object

[Reference: developer.mozilla Set](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set)

#### Q153. How would you change the color of this header to pink?

```javascript
<h2 id="cleverest">girls</h2>
```

- [ ] document.getElementByName("cleverest").style.color = "pink";
- [ ] document.getElementsByTagName("h2").style.color = "pink";
- [ ] document.getElementByName("h2").style.color = "pink";
- [x] document.getElementById("cleverest").style.color = "pink";

[Reference: W3Schools HTML DOM Style color Property](https://www.w3schools.com/jsref/prop_style_color.asp)

#### Q154. Which line is missing from this code if you expect the code to evaluate to true?

```js
var compare = function (test1, test2) {
  // Missing line
};

compare(1078, '1078'); // yields true
```

- [ ] `test1==test2;`
- [ ] return test1===test2;
- [x] return test1==test2;
- [ ] return test1!=test2;

[Reference: MDN Equality Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Equality)

#### Q155. What is the output of this code?

```js
if (true) {
  var first = 'You';
}

function fScope() {
  var second = 'got this!';
}
fScope();
console.log(first);
console.log(second);
```

- [ ] You
       undefined
- [x] You
       ReferenceError
- [ ] undefined
       undefined
- [ ] You
       got this!

[Reference: W3schools JS Scoping](https://www.w3schools.com/js/js_scope.asp)

#### Q156. What is the output for the code given below?

```js
console.log('hello' + 'world' + '!');
```

- [x] helloworld!
- [ ] helloworld !
- [ ] hello world!
- [ ] hello world !

#### Q157. What is the output of this code?

```js
console.log(10 + 10);
```

- [ ] 10
- [x] 20
- [ ] 30
- [ ] 40

#### Q158. Events related to the browser window can be handled by?

- [ ] Onclicks
- [x] Window
- [ ] querySelector
- [ ] None of the above

[Reference: GeeksForGeeks](https://www.geeksforgeeks.org/javascript-course-quiz-1/)

#### Q159. How do you define a function in JavaScript?

- [x] function myFunction() {}
- [ ] def myFunction() {}
- [ ] var myFunction = () => {}
- [ ] func myFunction() {}

[Reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions)

#### Q160. Your code is producing the error: TypeError: Cannot read property 'reduce' of undefined. What does that mean?

- [x] You are calling a method named reduce on an object that's declared but has no value.
- [ ] You are calling a method named reduce on an object that does not exist.
- [ ] You are calling a method named reduce on an empty array.
- [ ] You are calling a method named reduce on an object that has a null value.

#### Q161. Which of the following methods can be used to display data in some form using Javascript?

- [ ] document.write()
- [ ] console.log()
- [ ] window.alert()
- [x] all of the above

#### Q162. Which document method is not used to get a reference to a DOM node?

- [x] document.getNode();
- [ ] document.getElementsByClassName();
- [ ] document.querySelectorAll();
- [ ] document.querySelector();

#### Q163. Which of these is a valid variable name?

- [ ] 5thItem
- [x] firstName
- [ ] grand total
- [ ] function

#### Q164. What function is used in JavaScript to schedule a function to run after a specified number of milliseconds?

- [x] setTimeout()
- [ ] setInterval()
- [ ] delay()
- [ ] wait()

[Reference](https://www.w3schools.com/js/js_timing.asp)

#### Q165. Which of the following is a server-side Java Script object?

- [ ] Function
- [x] File
- [ ] FileUpload
- [ ] Date

[Reference](https://www.wscubetech.com/quiz-result.html)

#### Q166. Which statement best describes the var keyword's scope in JavaScript?

- [ ] Block scope
- [x] Function scope
- [ ] Global scope
- [ ] Instance scope

#### Q167. What will be logged to the console?

```js
const foo = () => console.log('First');
const bar = () => setTimeout(() => console.log('Second'), 0);
foo();
bar();
console.log('Third');
```

- [ ] Second, First, Third
- [x] First, Third, Second
- [ ] First, Second, Third
- [ ] Third, First, Second

#### Q168. What will be the output of running this code?

```js
function scream(words) {
  return words.toUpperCase() + '!!!';
}

scream('yay');
```

- [x] YAY!!!
- [ ] ReferenceError
- [ ] Undefined
- [ ] TypeError