## HTML

#### Q1. Для чого призначений тег `<track>` і коли його слід використовувати?

- [ ] Тег `<track>` використовується для визначення субтитрів. Зазвичай він використовується як дочірній елемент тегів `<audio> і <video>`.
- [ ] Тег `<track>` використовується для визначення субтитрів. Зазвичай він використовується як дочірній елемент тегу `<video>`.
- [ ] Тег `<track>` використовується для визначення субтитрів, титрів та інших типів тексту пов'язаних з часом. Зазвичай він використовується як дочірній елемент тегу `<video>`.
- [x] Тег `<track>` використовується для визначення субтитрів, підписів та інших типів тексту пов'язаних з часом. Зазвичай він використовується як дочірній елемент тегів `<audio>` і `<video>`.

#### Q2. Які найкращі приклади порожіх елементів?

- [ ] `<link><meta><title>`
- [x] `<br><base><source>`
- [ ] `<input><br><p>`
- [ ] `<area><embed><strong>`

#### Q3. Який тег чи теги в HTML5 вбудовують веб-сторінку всередину веб-сторінки?

- [ ] `<iframe>, <frame> та <frameset>`
- [ ] `<frame>`
- [x] `<iframe>`
- [ ] `<frame> and <frameset>`

#### Q4. Де зазвичай зустрічаються теги `<header>` та `<footer>`?

- [ ] як нащадки тегів `<body>, <article>, <aside> і <section>`
- [x] як нащадки тегів `<body>, <article> і <section>`
- [ ] як нащадки тегів `<body>, <article>, <aside>, <nav> і <section>`
- [ ] як нащадки тегів `<body>, <article>, <table> і <section>`

#### Q5. Який найкращий спосіб застосувати жирний стиль до тексту?

- [ ] `<strong>`
- [x] Скористатися CSS.
- [ ] `<bold>`
- [ ] `<b>`

#### Q6. Як використовується тег `<link>`?

- [ ] під час підключення таблиць стилів, JavaScript і піктограм для мобільних програм
- [x] під час підключення таблиць стилів, фавіконів і попереднього завантаження ресурсів
- [ ] під час посилання однієї веб-сторінки на іншу
- [ ] під час підключення таблиць стилів, зовнішніх URL-адрес і піктограм

#### Q7. Чим слід заповнити два порожні поля в HTML-коді нижче?

```HTML
<address ______ _____>
  <span itemprop="streetAddress">6410 Via Real</span><br/>
  <span itemprop="addressLocality">Carpinteria</span>,
  <span itemprop="addressRegion">CA</span>
  <span itemprop="addressCode">93013</span>
</address>
```

- [x] `itemscope` `itemtype="http://schema.org/PostalAddress"`
- [ ] `itemsref="http://schema.org/PostalAddress"` `itemid="address"`
- [ ] `itemscope` `itemref="http://schema.org/PostalAddress"`
- [ ] `itemid="address"` `itemtype="http://schema.org/PostalAddress"`

#### Q8. Для чого корисний елемент `<aside>`?

- [x] дозволяє видалити вміст, не відволікаючи від повідомлення сторінки
- [ ] для будь-чого, що ви хочете перемістити вбік, як-от поле цитат, бічна панель або зображення з обтіканням текстом
- [ ] для всього, що в дужках
- [ ] для будь-чого на бічній панелі

#### Q9. З якими тегами пов’язаний елемент `<source>`?

- [ ] `<svg>, <picture>, <audio>, and <video>`
- [x] `<picture>, <audio>, and <video>`
- [ ] Він взаємозамінний з атрибутом `src`, тому будь-який елемент, який використовує `src`, може використовувати `<source>`
- [ ] `<audio> and <video>`

#### Q10. Що НЕ є дійсним атрибутом для елемента `<textarea>`?

- [ ] readonly
- [x] max
- [ ] form
- [ ] spellcheck

#### Q11. Який найкращий спосіб закодувати показаний зразок?

![Sample text](images/ss-2.png?raw=true)

- [ ] A

```HTML
<details>
  <summary>Parmesan Deviled Eggs</summary>
  <p>
    These delectable little bites are made with organic eggs, fresh Parmesan, and chopped pine nuts.
  </p>
</details>
```

- [ ] B

```HTML
<h4>▸ Parmesan Deviled Eggs</h4>
<p>
  These delectable little bites are made with organic eggs, fresh Parmesan, and chopped pine nuts.
</p>
```

- [x] C

```HTML
<details open>
  <summary>Parmesan Deviled Eggs</summary>
  <p>
    These delectable little bites are made with organic eggs, fresh Parmesan, and chopped pine nuts.
  </p>
</details>
```

- [ ] D

```HTML
<details>
  <h4>▸ Parmesan Deviled Eggs</h4>
  <p>
    These delectable little bites are made with organic eggs, fresh Parmesan, and chopped pine nuts.
  </p>
</details>
```

#### Q12. Яке призначення елемента `<samp>`?

- [ ] Він підключає веб-браузер до сервера SA-MP.
- [ ] Визначає вкладений текст як зразок або приклад.
- [x] Ідентифікує вихідний зразок комп’ютерної програми.
- [ ] Використовує простий протокол обміну повідомленнями програми для підключення браузера до текстового пристрою.

#### Q13. Коли слід використовувати елементи `<ol> і <ul>`?

- [ ] Скористатися `<ul>`, якщо потрібен маркований список, і `<ol>`, якщо потрібен нумерований список.
- [ ] Скористатися `<ul>`, якщо є список елементів, у якому порядок елементів має значення. Скористатися `<ol>`, якщо є список елементів, які можна розмістити в будь-якому порядку.
- [ ] Скористатися `<ol>`, якщо потрібен маркований список, і `<ul>`, якщо потрібен нумерований список.
- [x] Скористатися `<ol>`, якщо є список елементів, у якому порядок елементів має значення. Скористатися `<ul>`, якщо є список елементів, які можна розмістити в будь-якому порядку.

#### Q14. Яка різниця між методами post і get у формі?

- [ ] post використовується для надсилання інформації на сервер. get використовується для отримання інформації форми з сервера.
- [ ] get використовується для надсилання інформації на сервер. post використовується для отримання інформації форми з сервера.
- [ ] За допомогою get дані включаються в тіло форми під час надсилання на сервер. З post дані передаються через URL-адресу.
- [x] З post дані включаються в тіло форми. За допомогою get дані проходять через URL-адресу.

#### Q15. Яка різниця між тегами `<div>` і `<span>`?

- [x] `<div>` використовується там, де потрібен загальний тег block, тоді як `<span>` - там, де потрібен загальний inline тег.
- [ ] `<div>` використовується для основних поділів на сторінці, тоді як `<span>` - для поділу на стовпці.
- [ ] `<div>` є галузевим стандартним тегом за замовчуванням, але ви можете використовувати `<span>` за бажанням.
- [ ] `<div>` використовується там, де потрібен загальний inline тег, тоді як `<span>` - там, де потрібен загальний тег block.

#### Q16. Що має заповнити порожнечу в HTML-коді нижче?

```HTML
<form method="post" action="mailto:info@linkedin.com" ____="text/plain"></form>
```

- [x] enctype
- [ ] media
- [ ] type
- [ ] rel

#### Q17. Яка правильна розмітка для атрибута `alt` зображення?

- [ ] A

```HTML
<img src="cubism.jpg" alt="Version of ""Whistler's Mother"" in cubist style">
```

- [ ] B

```HTML
<img src="cubism.jpg" alt="Version of "Whistler's Mother" in cubist style">
```

- [x] C

```HTML
<img src="cubism.jpg" alt='Version of "Whistler&apos;s Mother" in cubist style' />
```

- [ ] D

```HTML
<img src="cubism.jpg" alt="Version of \"Whistler's Mother\" in cubist style">
```

#### Q18. Яке призначення атрибута **id** у коді нижче?

```HTML
<p id="warning">Be careful when installing this product.</p>
```

- [x] id є унікальним ідентифікатором у документі, який використовується для стилізації CSS, сценаріїв і посилань на веб-сторінці.
- [ ] id є унікальним ідентифікатором у документі, який використовується для стилізації CSS і з кодом Javascript.
- [ ] id можна використовувати для стилізації CSS кілька разів на сторінці.
- [ ] id є унікальним ідентифікатором на веб-сайті, який використовується для стилізації CSS, сценаріїв і посилань на веб-сторінці.

#### Q19. Яка найкраща семантична розмітка для показаного речення?

```
On July 21, 1969, Neil Armstrong said, "One small step for man, one giant leap for mankind."
```

- [x] A

```HTML
<p>
  On <time datetime="1969-07-21">July 21, 1969</time>, Neil Armstrong said,
  <q cite="https://www.hq.nasa.gov/alsj/a11l/a11.html"
    >One small step for man, one giant leap for mankind.</q
  >
</p>
```

- [ ] B

```HTML
<p>
  On July 21, 1969, Neil Armstrong said,
  <q cite="https://www.hq.nasa.gov/alsj/a11l/a11.html"
    >"One small step for man, one giant leap for mankind."</q
  >
</p>
```

- [ ] C

```HTML
<p>
  On July 21, 1969, Neil Armstrong said,
  <q>"One small step for man, one giant leap for mankind."</q>
</p>
```

- [ ] D

```HTML
<p>
  On <time datetime="07-21-1969">July 21, 1969</time>, Neil Armstrong said,
  <q cite="https://www.hq.nasa.gov/alsj/a11l/a11.html"
    >One small step for man, one giant leap for mankind.</q
  >
</p>
```

#### Q20. Що має заповнити порожнечу в цьому HTML-коді?

```HTML
<a href="https://es.yahoo.com/" hreflang="____" target="_blank">Visita Yahoo</a>
```

- [x] es
- [ ] es-spanish
- [ ] es-es
- [ ] spanish

#### Q21. Перегляньте текст у червоному полі на зображенні. Який найкращий спосіб закодувати це в HTML?

![Image of footer](images/ss-3.png?raw=true)

- [ ] впорядкований список
- [ ] невпорядкований список всередині навігаційного елемента
- [ ] впорядкований список всередині навігаційного елемента
- [x] невпорядкований список

#### Q22. Який найкращий спосіб закодувати три варіанти у формі, щоб користувач міг вибрати лише один елемент?

- [ ] A

```HTML
<label for="example">Make a choice:</label>
<datalist id="example">
  <option value="Choice 1"></option>
  <option value="Choice 2"></option>
  <option value="Choice 3"></option>
</datalist>
```

- [ ] B

```HTML
<p>Make a choice:</p>
<input id="choices" name="example" />

<datalist value="choices">
  <option value="Choice 1"></option>
  <option value="Choice 2"></option>
  <option value="Choice 3"></option>
</datalist>
```

- [ ] C

```HTML
<label for="example">Make a choice:</label>
<input list="example" id="choices" name="choices" />

<datalist id="choices">
  <option value="Choice 1">Choice 1</option>
  <option value="Choice 2">Choice 2</option>
  <option value="Choice 3">Choice 3</option>
</datalist>
```

- [x] D

```HTML
<label for="example">Make a choice:</label>
<input list="choices" id="example" name="example" />

<datalist id="choices">
  <option value="Choice 1"></option>
  <option value="Choice 2"></option>
  <option value="Choice 3"></option>
</datalist>
```

#### Q23. Як підтвердити, що документ написаний у HTML5?

- [ ] Сервер загортає веб-сторінку в оболонку HTML5.
- [x] Скористатися декларацією `<!DOCTYPE html>`, яка починає документ.
- [ ] Браузер отримує кодування від сервера для відображення документа з HTML5.
- [ ] Він укладений у тег `<html>`.

#### Q24. Що виконує наведений нижче код?

```html
<picture>
  <source srcset="image1.jpg" media="(min-width: 1000px)" />
  <source srcset="image2.jpg" media="(min-width: 750px)" />
  <img src="image3.jpg" />
</picture>
```

- [x] відображає image1.jpg з роздільною здатністю екрану 1000px та вище, image2.jpg з 750-999px та image3.jpg з 749px та менше.
- [ ] відображає image1.jps з роздільною здатністю 1000px і більше, а image2.jpg — з 750-999px, image3.jpg є типовим, якщо `<picture>` не підтримується.
- [ ] відображає image1.jpg з роздільною здатністю 1000px та вище та image2.jpg з 750px та вище, image3.jpg є типовим, якщо `<picture>` не підтримується.
- [ ] відображає image1.jpg, image2.jpg і image3.jpg з роздільною здатністю 1000px і вище.

[Джерело: HTML &lt;picture> Tag](https://www.w3schools.com/tags/tag_picture.asp)

#### Q25. Який код створить цю таблицю?

![Table with yellow background](images/ss-4.png?raw=true)

- [ ] A

```HTML
<table>
  <scope cols="2" style="background-color: yellow">
  <tr>
    <th>Col 1</th>
    <th>Col 2</th>
    <th>Col 3</th>
  </tr>
  <tr>
    <td>first</td>
    <td>second</td>
    <td>third</td>
  </tr>
</table>
```

- [x] B

```HTML
<table>
  <colgroup span="2" style="background-color: yellow">
  <tr>
    <th>Col 1</th>
    <th>Col 2</th>
    <th>Col 3</th>
  </tr>
  <tr>
    <td>first</td>
    <td>second</td>
    <td>third</td>
  </tr>
</table>
```

- [ ] C

```HTML
<table>
  <group cols="2" style="background-color: yellow">
  <tr scope="row">
    <th>Col 1</th>
    <th>Col 2</th>
    <th>Col 3</th>
  </tr>
  <tr scope="row">
    <td>first</td>
    <td>second</td>
    <td>third</td>
  </tr>
</table>
```

- [ ] D

```HTML
<table>
  <columns colspan="2" style="background-color: yellow">
  <tr>
    <th>Col 1</th>
    <th>Col 2</th>
    <th>Col 3</th>
  </tr>
  <tr>
    <td>first</td>
    <td>second</td>
    <td>third</td>
  </tr>
</table>
```

#### Q26. Для чого зазвичай використовується тег `<hr>`? / Альт.: Яке семантичне значення тегу `<hr>`?

- [ ] Цей тег застарів (альт.: застарілий) і не повинен використовуватися.
- [x] Позначає зміну теми в межах розділу на рівні абзацу.
- [ ] Малює горизонтальну лінію.
- [ ] Позначає зміну теми на рівні розділу. / Альт.: позначає поділ розділів у межах `<article>`.

`Це заплутане запитання, і можуть бути аргументи на користь того, що другий і третій варіанти є правильними.`

[MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/hr): Елемент HTML `<hr>` представляє тематичний розрив між елементами рівня абзацу. Історично його було представлено як горизонтальну лінію. Хоча він все ще може відображатися як горизонтальна лінія візуально у браузерах, цей елемент тепер визначається в семантичних термінах, а не в термінах представлення, тому, якщо ви хочете намалювати горизонтальну лінію, ви повинні зробити це за допомогою відповідного CSS.

#### Q27. Чим слід заповнити два порожні поля в HTML-коді нижче?

```HTML
<section itemscope itemtype="http://schema.org/Restaurant">
  <h1 itemprop="name">Nadia's Garden</h1>
  <p itemscope ______ ______>
    <span itemprop="ratingValue">4.5</span> stars - based on
    <span itemprop="reviewCount">120</span> reviews
  </p>
</section>
```

- [ ] `itemprop="aggregateRating" itemref="http://schema.org/AggregateRating"`
- [x] `itemprop="aggregateRating" itemtype="http://schema.org/AggregateRating"`
- [ ] `itemid="aggregateRating" itemtype="http://schema.org/AggregateRating"`
- [ ] `itemid="aggregateRating" itemref="http://schema.org/AggregateRating"`

#### Q28. Який фрагмент HTML посилається на самий верх веб-сторінки?

- [x] A

```HTML
<a id="top"></a>

<!-- розміщено у верхній частині сторінки -->

<a href="#top">back to top</a>
```

- [ ] B

```HTML
<a name="top"></a>

<!-- розміщено у верхній частині сторінки -->

<a href="#top">back to top</a>
```

- [ ] C

```HTML
<a href="#">back to top</a> <a href="#top">back to top</a>
```

- [ ] D

```HTML
<button href="#">back to top</button> <button href="#top">back to top</button>
```

#### Q29. Які три теги застаріли в HTML4, але повернулися в HTML5?

- [ ] `<rb> <rp> <rt>`
- [ ] `<acronym> <code> <wbr>`
- [ ] `<hgroup> <q> <wbr>`
- [x] `<b> <i> <u>`

#### Q30. Тег **\_** використовується для розмітки короткого фрагмента коду, тоді як тег \_ використовується для розмітки довшого блоку коду

- [ ] `<kdb>`, `<pre>`
- [ ] `<pre>`, `<code>`
- [ ] `<kdb>`, `<mark>`
- [x] `<code>`, `<pre>`

1. [Джерело: MDN Web Docs code](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/code)
2. [Джерело: MDN Web Docs pre](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/pre)

#### Q31. Що робить елемент `<label>`?

- [ ] Позначає веб-сторінки важливою інформацією.
- [ ] Створює ідентифікатор для відповідного елемента input.
- [ ] Замінює значення атрибута name у дочірньому елементі input.
- [x] Програмно пов’язує текстову мітку з елементом інтерфейсу.

#### Q32. Щоб відкрити посилання в новому вікні чи вкладці, використовуйте атрибут **\_**

- [x] `_blank`
- [ ] `_self`
- [ ] `_new`
- [ ] `_parent`

#### Q33. Який семантично найточніший спосіб позначити наведене нижче речення? Примітка: "TLAs" розшифровується як "акроніми з трьох літер".

**We are fond of our TLAs in web design.**

- [ ] A

```HTML
<p>We are fond of our <span title="three-letter acronyms">TLAs</span> in web design.</p>
```

- [ ] B

```HTML
<p>We are fond of our TLAs in web design.</p>
```

- [x] C

```HTML
<p>we are fond of our <abbr title="three-letter acronyms">TLAs</abbr> in web design.</p>
```

- [ ] D

```HTML
<p>we are fond of our <acronym title="three-letter acronym">TLAs</acronym> in web design.</p>
```

`<acronym>` видалено в HTML5, і його більше не слід використовувати. Натомість веб-розробники повинні використовувати елемент `<abbr>`.

#### Q34. Яка правильна вкладена розмітка для цього списку?

![Sample list](images/ss-6.png?raw=true)

- [ ] A

```HTML
<ul>
  <li>
    office
    <ol style="circle">
      <li>staple</li>
      <li>paper</li>
    </ol>
  </li>
  <li>
    groceries
    <ol style="circle">
      <li>milk</li>
    </ol>
  </li>
</ul>
```

- [x] B

```HTML
<ul>
  <li>
    Office Supplies
    <ul>
      <li>Stapler</li>
      <li>Paper clips</li>
    </ul>
  </li>
  <li>
    Groceries
    <ul>
      <li>Milk</li>
    </ul>
  </li>
</ul>
```

- [ ] C

```HTML
<ul>
  <li>office</li>
  <li>staple</li>
  <li>paper</li>
  <li>groceries</li>
  <li>milk</li>
</ul>
```

#### Q35. Чим слід заповнити пусте поле нижче?

```HTML
<link href="phone.css" rel="stylesheet" _____="print" />
```

- [ ] title
- [ ] type
- [ ] device
- [x] media

#### Q36. Який семантично правильний спосіб розмітки цього макета?

![quote](images/ss-5.png?raw=true)

- [ ] A

```HTML
<p>
  "Making money is what you have to do to sustain a business—being driven to make something of value
  and purpose is much more powerful."
</p>
<p><em>Lynda Weinman</em></p>
```

- [ ] B

```HTML
<blockquote>
  <q
    >"Making money is what you have to do to sustain a business—being driven to make something of
    value and purpose is much more powerful."</q
  >
  <cite><em>Lynda Weinman</em></cite>
</blockquote>
```

- [x] C

```html
<blockquote>
  <p>
    "Making money is what you have to do to sustain a business—being driven to make something of
    value and purpose is much more powerful."
  </p>
  <cite>Lynda Weinman</cite>
</blockquote>
```

- [ ] D

```html
<section>
  <q
    >"Making money is what you have to do to sustain a business—being driven to make something of
    value and purpose is much more powerful."</q
  >
  <cite>Lynda Weinman</cite>
</section>
```

#### Q37. У якому варіанті використовується правильна термінологія в описі цієї розмітки: `<p>info</p>`?

- [ ] Елемент відкривач  — `<p>`, елемент, що закриває — `</p>`, інформація про елемент — info.
- [ ] Початковий тег - `<p>`, кінцевий тег - `</p>`, вкладений HTML - info.
- [x] Початковий тег - `<p>`, кінцевий тег - `</p>`, вміст елемента - info.
- [ ] Початковий елемент — `<p>`, кінцевий — `</p>`, вміст тегу — info.

#### Q38. Яка різниця між `<input type="submit" value="Натисни мене">` і `<button type="submit">Натисни мене</button>`?

- [ ] Немає різниці. Обидва відображатимуть кнопку, яка надсилає форму.
- [x] Обидва надішлють форму. Однак `<button>` може мати вміст, відмінний від тексту, як-от зображення або вкладені елементи HTML, тоді як `<input>` не може.
- [ ] `<input type="button">` не підтримується в HTML5. Замість цього слід використовувати тег `<button>`.
- [ ] Обидва надішлють форму. Однак `<input>` може мати вміст, відмінний від тексту, наприклад зображення або вкладені елементи HTML, тоді як `<button>` не може.

#### Q39. Який найкращий семантичний спосіб вказати, що текст стосується введення з клавіатури?

- [ ] `<p>Натисніть клавішу <tt>Enter</tt>, щоб продовжити.</p>`
- [x] `<p>Натисніть клавішу <kbd>Enter</kbd>, щоб продовжити.</p>`
- [ ] `<p>Натисніть клавішу <samp>Enter</samp>, щоб продовжити.</p>`
- [ ] `<p>Натисніть клавішу Enter, щоб продовжити.</p>`

#### Q40. Що робить цей код?

```html
<audio controls>
  <source src="sound.mp3" type="audio/mpeg" />
  <source src="sound.ogg" type="audio/ogg" />
  <source src="sound.wav" type="audio/wav" />
</audio>
```

- [x] Браузер вибирає перший підтримуваний формат для відтворення за допомогою елементів керування браузера за замовчуванням.
- [ ] Браузер вибирає найкращий аудіоформат для відтворення за допомогою елементів керування JavaScript.
- [ ] Браузер автоматично відтворює кожен звуковий файл по порядку. Користувач має елементи керування для зупинки відтворення.
- [ ] Браузер вибирає перший підтримуваний звуковий файл і повторюватиме звук, доки користувач не зупинить його.

#### Q41. Який атрибут застосовує підказку про комбінацію клавіш до поточного елемента?

- [x] `accesskey`
- [ ] `shortcut`
- [ ] `keyboard`
- [ ] `access`

#### Q42. Який правильний спосіб закодувати посилання, яке після натискання надсилатиме електронний лист на адресу `email@example.com` із темою "Hello"?

- [ ] `<a href="mailto:email@example.com&subject=Hello">Click me</a>`
- [ ] `<a href="mailto:email@example.com">Hello</a>`
- [x] `<a href="mailto:email@example.com?subject=Hello">Click me</a>`
- [ ] `<a href="mailto:email@example.com?&subject=Hello">Click me</a>`

#### Q43. Який тег є кореневим елементом документа HTML?

- [ ] `<!DOCTYPE html>`
- [x] `<html>`
- [ ] `<body>`
- [ ] `<root>`

`Тег <html> є кореневим елементом документа HTML, що означає, що він містить увесь вміст і теги документа HTML. Елемент HTML представляє корінь документа.`

1. [Джерело](https://www.interviewbit.com/html-mcq/)
2. [Джерело](https://www.w3.org/TR/2010/WD-html-markup-20100624/html.html)

#### Q44. Який фрагмент коду створює показаний макет, починаючи з `<table>` і закінчуючи `</table>`?

![Table](images/ss-1.png?raw=true 'table')

- [ ] A

```HTML
<tr>
  <td>Table cell 1</td>
  <td>Table cell 2</td>
</tr>
<tr>
  <td rowspan="2">Table cell 3</td>
</tr>
```

- [ ] B

```HTML
<tr>
  <td>Table cell 1</td>
  <td>Table cell 2</td>
  <td>Table cell 3</td>
</tr>
```

- [x] C

```HTML
<tr>
  <td>Table cell 1</td>
  <td>Table cell 2</td>
</tr>
<tr>
  <td colspan="2">Table cell 3</td>
</tr>
```

- [ ] D

```HTML
<tr>
  <td>Table cell 1</td>
  <td>Table cell 2</td>
</tr>
<tr>
  <td>Table cell 3</td>
</tr>
```

#### Q45. Який вибір НЕ є допустимим значенням для атрибута **name** у тегу `<meta>`?

- [x] charset
- [ ] viewport
- [ ] generator
- [ ] author

#### Q46. Яка форма закодована правильно?

- [ ] A

```HTML
<form>
  <legend>Title</legend>
  <fieldset>
    <label for="name">Your name:</label>
    <input type="text" name="name" id="name" />
    <button type="submit">Submit</button>
  </fieldset>
</form>
```

- [ ] B

```HTML
<form>
  <fieldset>
    <legend>Title</legend>
    <p>Your name:</p>
    <input type="text" name="name" id="name" />
    <input type="submit" value="Submit" />
  </fieldset>
</form>
```

- [x] C

```HTML
<form>
  <fieldset>
    <legend>Title</legend>
    <label for="name">Your name:</label>
    <input type="text" name="name" id="name" />
    <button type="submit">Submit</button>
  </fieldset>
</form>
```

- [ ] D

```HTML
<form>
  <legend>Title</legend>
  <label for="name">Your name:</label>
  <input type="text" name="name" id="name" />
  <input type="submit" value="Submit" />
</form>
```

#### Q47. Що робить атрибут **poster** у тегу `<video>`?

- [x] Визначає зображення, яке має відображатися під час завантаження та до відтворення відео.
- [ ] Визначає зображення, яке відображається, лише якщо є проблема з відео.
- [ ] Визначає зображення, яке має відображатися до відтворення відео.
- [ ] Визначає зображення, яке має відображатися під час завантаження відео.

#### Q48. Що робить цей код?

```HTML
<audio controls src="sound.mp3" type="audio/mpeg">Коли відображається цей текст?</audio>
```

- [ ] Текст відображається над елементами керування звуком, якщо CSS не використовується для розміщення його в іншому місці.
- [ ] Текст відображається під елементами керування звуком.
- [x] Текст відображається, коли браузер не може відтворити звук.
- [ ] Текст ніколи не відображається.

#### Q49. Яке основне призначення тегу `<canvas>`?

- [ ] Дозволяє відображати растрові зображення на веб-сторінці.
- [ ] Відображає анотовані зображення.
- [x] Дозволяє малювати на растровому зображенні за допомогою JavaScript.
- [ ] Дозволяє відображати векторні зображення на веб-сторінці.

#### Q50. Який варіант містить три дійсні елементи рівня block?

- [ ] `<details> <abbr> <figcaption>`
- [ ] `<canvas> <select> <noscript>`
- [x] `<dt> <table> <pre>`
- [ ] `<kbd> <p> <main>`

#### Q51. Яке призначення атрибута **lang** у коді нижче?

```HTML
<p lang="en-GB">Welcome to our wonderful website.</p>
```

- [ ] Він визначає мову для веб-сайту — у цьому випадку англійську.
- [ ] Він встановлює мову та діалект веб-сайту — у цьому випадку британську англійську.
- [x] Встановлює мову та діалект абзацу — у цьому випадку британську англійську.
- [ ] Встановлює мову для абзацу—у цьому випадку англійську.

#### Q52. Які формати зображень можуть відображатися всіма веб-браузерами?

- [ ] JPG, GIF, TIF
- [ ] JPG, TIF, BMP
- [ ] TIF, BMP, GIF
- [x] PNG, GIF, JPG

#### Q53. Перегляньте наведений нижче код. Яка абсолютна URL-адреса сторінки під назвою **page.html**?

```HTML
<base href="http://www.linkedin.com/dir/" />
```

- [x] `http://www.linkedin.com/dir/page.html`
- [ ] `page.html`
- [ ] `http://www.linkedin.com/page.html`
- [ ] `dir/page.html`

#### Q54. Який правильний спосіб включити таблицю стилів під назвою **style.css** у <head> вашого документа?

- [ ] `<style link="style.css">`
- [x] `<link rel="stylesheet" href="style.css">`
- [ ] `<style src="style.css"></style>`
- [ ] `<link style="style.css">`

#### Q55. Ви хочете мати однаковий інтервал між деякими рядками, як у вірші чи адресі. Який підхід слід використовувати?

- [ ] Перенести текст у рамку потрібної ширини, щоб усе було правильно. Встановіти ширину поля за допомогою CSS.
- [x] Розділити рядки за допомогою `<p>`, потім скористатися CSS, щоб створити однаковий інтервал.
- [ ] Скористатися тегом `<pre>`, щоб міжрядковий інтервал виглядав саме так, як потрібно.
- [ ] Розділити рядки тегом `<br>`.

[З MDN (`<br>`: елемент розриву рядка)](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/br#accessibility_concerns):

```
Проблеми доступності

Створення окремих абзаців тексту за допомогою <br> не тільки погана практика, але й проблематична для людей, які орієнтуються за допомогою технології зчитування з екрана. Програми зчитування екрана можуть повідомляти про присутність елемента, але не про будь-який вміст, що міститься в <br>. Це може заплутати та розчарувати людину, яка використовує програму зчитування з екрана.

Використовуйте елементи <p> та властивості CSS, як-от margin, щоб контролювати інтервали.
```

#### Q56. Що робить тег `<wbr>`?

- [ ] Вимагає, щоб браузер переніс поточний рядок у цю точку.
- [ ] Розбиває слово на дві частини, використовуючи дефіс для з’єднання слів.
- [ ] Форматує речення, щоб його було легко розбити.
- [x] Надає можливість розірвати дуже довге слово, якщо це необхідно для правильного відображення сторінки.

#### Q57. Перегляньте наведений нижче код. Як включити вкладену навігацію для Link 2, яке містить Link?

```HTML
<nav>
  <ul>
    <li><a href="#">Link 1</a></li>
    <li><a href="#">Link 2</a></li>
    <li><a href="#">Link 3</a></li>
  </ul>
</nav>
```

- [ ] A

```HTML
<nav>
  <ul>
    <li><a href="#">Link 1</a></li>
    <li><a href="#">Link 2</a></li>
    <ul>
      <li><a href="#">Link 2a</a></li>
    </ul>
    <li><a href="#">Link 3</a></li>
  </ul>
</nav>
```

- [x] B

```HTML
<nav>
  <ul>
    <li><a href="#">Link 1</a></li>
    <li>
      <a href="#">Link 2</a>
      <ul>
        <li><a href="#">Link 2a</a></li>
      </ul>
    </li>
    <li><a href="#">Link 3</a></li>
  </ul>
</nav>
```

- [ ] C

```HTML
<ul>
  <nav>
    <li><a href="#">Link 1</a></li>
    <li>
      <a href="#">Link 2</a>
      <ul>
        <nav>
          <li><a href="#">Link 2a</a></li>
        </nav>
      </ul>
    </li>
    <li><a href="#">Link 3</a></li>
  </nav>
</ul>
```

- [ ] D

```HTML
<nav>
  <ul>
    <li><a href="#">Link 1</a></li>
    <li><a href="#">Link 2</a></li>
    <nav>
      <ul>
        <li><a href="#">Link 2a</a></li>
      </ul>
    </nav>
    <li><a href="#">Link 3</a></li>
  </ul>
</nav>
```

#### Q58. Який правильний спосіб закодувати коментар у HTML?

- [ ] `//this is a comment`
- [ ] `/* this is a comment */`
- [ ] `<! this is a comment ->`
- [x] `<!-- this is a comment -->`

#### Q59. Яке твердження є **хибним**?

- [ ] Inline елементи можуть бути вкладені всередині inline елементів.
- [ ] Block елементи можуть бути вкладені в block елементи.
- [ ] Inline елементи можуть бути вкладені в block елементи.
- [x] Block елементи можуть бути вкладені всередині inline елементів.

#### Q60. Яка найкраща семантика для використання лапок у HTML?

`Steve Kruz said: "He will Win"`

- [x] `<q>`
- [ ] `<quote>`
- [ ] `<blockquote>`
- [ ] `<notation>`

[Довідка (w3schools)](https://www.w3schools.com/html/html_quotation_elements.asp)

#### Q61. Як відео виглядатиме на повністю завантаженій веб-сторінці, якщо використовується тег `<video>` і не встановлено атрибут **autoplay**?

- [ ] Відображатиме випадковий кадр із відео, якщо не встановлено атрибут **poster**.
- [x] Відображатиме перший кадр відео, якщо не встановлено атрибут **poster**.
- [ ] Нічого не відображатиме, якщо не встановлено атрибут **poster**.
- [ ] Відображатиме чорне вікно, якщо не встановлено атрибут **poster**.

[Довідка (w3schools)](https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_video)

#### Q62. Як правильно описати порожній елемент / Альтернативний варіант: Як правильно описати порожній елемент, наприклад тег розриву рядка?

- [ ] Він має відкриваючі та закриваючі теги, але не має дочірнього вмісту.
- [ ] Він нічого не відображає на веб-сайті.
- [x] Він не має дочірнього вмісту та закриваючого тегу.
- [ ] Він має дочірній вміст, але не має закриваючого тегу.

[Довідка (MDN Web Docs)](https://developer.mozilla.org/en-US/docs/Glossary/Empty_element)

#### Q63. Яка мета async в цьому коді?

`<script async src="myscript.js"></script>`

- [ ] Він завантажує сценарій із сервера, коли дозволяють ресурси.
- [ ] Він запускає сценарій після завершення аналізу HTML.
- [x] Він запускає сценарій, коли сценарій готовий.
- [ ] Він призупиняє розбір HTML-коду під час виконання сценарію.

#### Q64. Що цей код робить на сторінці, яку ви відвідуєте вперше?

`<audio autoplay loop src="sound.mp3" type="audio/mpeg"></audio>`

- [ ] Коли натиснуто кнопку **Відтворити**, браузер відтворює звук знову і знову, доки користувач не зупинить його.
- [ ] Браузер автоматично відтворює звук у фоновому режимі. Користувач не може контролювати звук.
- [ ] Браузер автоматично та постійно відтворює звук у фоновому режимі. Користувач може в будь-який момент зупинити звук.
- [x] Нічого не робить. Сучасні браузери вимагають певної форми взаємодії, перш ніж дозволити автовідтворення сторінки зі звуком.

1. [(MDN) audio](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/audio),
2. [(MDN) autoplay](https://developer.mozilla.org/en-US/docs/Web/Media/Autoplay_guide)

#### Q65. Яка різниця між тегами `<head>` і `<header>`?

- [ ] Існує лише один тег `<head>` на сторінці, тоді як тегів `<header>` може бути багато.
- [ ] Тег `<head>` може містити посилання на CSS і Javascript, тоді як тег `<header>` може містити заголовки та навігаційні посилання.
- [ ] Тег `<head>` містить метаінформацію, а тег `<header>` містить навігацію, логотипи та інший вміст, що ідентифікує сторінку.
- [x] Все вищезазначене.

#### Q66. Яка мета defer у цьому коді?

`<script defer src="myscript.js"></script>`

- [ ] Він завантажує сценарій із сервера, коли дозволяють ресурси.
- [x] Він запускає сценарій після завершення аналізу HTML.
- [ ] Він запускає сценарій, коли сценарій готовий.
- [ ] Він призупиняє розбір HTML-коду під час виконання сценарію.

#### Q67. Наведений нижче код містить деякі помилки. Який варіант виправляє всі помилки?

```HTML
<table>
  <tr>
    Cell 1
  </tr>
  <td>Cell 2</td>
  <caption>
    A table
  </caption>
</table>
```

- [ ] A

```HTML
<caption>
  A table
</caption>
<table>
  <td>
    <tr>
      Cell 1
    </tr>
    <tr>
      Cell 2
    </tr>
  </td>
</table>
```

- [ ] B

```HTML
<caption>
  A table
</caption>
<table>
  <tr>
    <td>Cell 1</td>
    <td>Cell 2</td>
  </tr>
</table>
```

- [x] C

```HTML
<table>
  <caption>
    A table
  </caption>
  <tr>
    <td>Cell 1</td>
    <td>Cell 2</td>
  </tr>
</table>
```

- [ ] D

```HTML
<table>
  <tr>
    <td>Cell 1</td>
    <td>Cell 2</td>
  </tr>
  <caption>
    A table
  </caption>
</table>
```

#### Q68. Враховуючи наведену тут структуру файлів та каталогів, який правильний елемент розмістити у файлі profit.html для посилання на info.html?

![Image of footer](images/ss-7.png?raw=true)

- [ ] `<a href="../work/info.html">See Information </a>`
- [x] `<a href="../info.html">See Information </a>`
- [ ] `<a href="../../info.html">See Information </a>`
- [ ] `<a href="info.html">See Information </a>`

#### Q69. Коли слід використовувати елемент `<article>`?

- [ ] Для публікацій у блогах та інших елементах соціальних мереж
- [ ] Для основної області вмісту веб-сайту
- [x] Коли вміст є окремою одиницею, придатний для синдикації або багаторазового використання
- [ ] Щоб пов’язати коментарі з публікацією в блозі

[Довідка (MDN)](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/article)

#### Q70. Який список складається з трьох порожніх елементів?

- [ ] A

```HTML
<area />
<embed />
<strong></strong>
```

- [ ] B

```HTML
<input />
<br />
<p></p>
```

- [ ] C

```HTML
<link>
<meta>
<title>
```

- [x] D

```HTML
<wbr />
<base />
<source />
```

#### Q71. Після натискання якого фрагмента HTML здійснюється телефонний дзвінок на мобільному пристрої?

- [x] `<a href="tel:802-555-1212">Call me</a>`
- [ ] `<a href="phone">802-555-1212</a>`
- [ ] `<a href="tel">802-555-1212</a>`
- [ ] `<a href="phone:802-555-1212">Call me</a>`

#### Q72. Яке призначення атрибута `class`?

- [ ] Класи дозволяють CSS вибирати певні елементи на сторінці. Ви можете перерахувати скільки завгодно імен класів в атрибуті класу,
 розділені пробілами.
- [ ] Класи дозволяють CSS і JavaScript вибирати певні елементи на сторінці. Ви можете вказати лише одну назву класу для атрибута класу.
- [ ] Класи дозволяють CSS вибирати певні елементи на сторінці. Ви можете вказати лише одну назву класу для атрибута класу.
- [x] Класи дозволяють CSS і JavaScript вибирати певні елементи на сторінці. Ви можете перерахувати скільки завгодно назв класів в      атрибуті класу
 як завгодно, розділені пробілами.

[Довідка (MDN)](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/class)

#### Q73. Який вибір не є допустимим атрибутом типу для тегу `<input>`?

- [ ] `<input type="color">`
- [ ] `<input type="tel">`
- [ ] `<input type="week">`
- [x] `<input type="num">`

[Довідка (MDN)](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/Input)

#### Q74. Який найбільш семантичний спосіб позначити це речення, щоб «happy talk must die» відтворювалося як вбудована цитата?

As Steve Krug once said, happy talk must die.

- [ ] `<p>`As Steve Krug once said, `<b>`happy talk must die.`</b>` `</p>`
- [ ] `<p>`As Steve Krug once said, `<i>`happy talk must die.`</i>` `</p>`
- [ ] `<p>`As Steve Krug once said, `<blockquote>`happy talk must die.`</blockquote>` `</p>`
- [x] `<p>`As Steve Krug once said, `<q>`happy talk must die.`</q>` `</p>`

[Джерело: W3Schools](https://www.w3schools.com/tags/tag_q.asp)

**`<q>` тег**
`Більшість браузерів відображатимуть теги q як вбудовані елементи в лапках`

#### Q75. Який найбільш семантично точний спосіб створити головну навігаційну панель, що відображається в горизонтальному напрямку?

- [ ] A

```html
<p>
  <a href="index.html">Home</a>
  <a href="about.html">About</a>
  <a href="contact.html">Contact</a>
</p>
```

- [ ] B

```html
<nav>
  <a href="index.html">Home</a>
  <a href="about.html">About</a>
  <a href="contact.html">Contact</a>
</nav>
```

- [ ] C

```html
<nav>
  <ol>
    <li><a href="index.html">Home</a></li>
    <li><a href="about.html">About</a></li>
    <li><a href="contact.html">Contact</a></li>
  </ol>
</nav>
```

- [x] D

```html
<nav>
  <ul>
    <li><a href="index.html">Home</a></li>
    <li><a href="about.html">About</a></li>
    <li><a href="contact.html">Contact</a></li>
  </ul>
</nav>
```

#### Q76. Який вибір є найкращим способом розмітки цього макета?

![Image of footer](images/ss-8.png?raw=true)

- [x] A

```HTML
<h4>Mailing Address</h4>
<address>
  6410 Via Real <br />
  Carpinteria, CA 93013<br />
  <a href="mailto:info@linkedin.com">info@linkedin.com</a>
</address>
```

- [ ] B

```HTML
<h4><strong>Mailing Address</h4>
<address><em>
  6410 Via Real <br>
  Carpinteria, CA 93013<br>
  <a href="mailto:info@linkedin.com">info@linkedin.com</a>
</em></address>
```

- [ ] C

```HTML
<h4>Mailing Address</h4>
<p>
  <em>
    6410 Via Real <br />
    Carpinteria, CA 93013<br />
    <a href="mailto:info@linkedin.com">info@linkedin.com</a>
  </em>
</p>
```

- [ ] D

```HTML
<p><strong>Mailing Address</strong></p>
<p>
  <em>
    6410 Via Real <br />
    Carpinteria, CA 93013<br />
    <a href="mailto:info@linkedin.com">info@linkedin.com</a>
  </em>
</p>
```

[Джерело: W3Schools](https://www.w3schools.com/tags/tag_address.asp)

`Тег <address> визначає контактну інформацію автора/власника документа чи статті. Контактною інформацією може бути адреса електронної пошти, URL-адреса, фізична адреса, номер телефону, ідентифікатор соціальної мережі тощо. Текст в елементі <address> зазвичай відображається курсивом, і браузери завжди додають розрив рядка перед і після елементу <address>.`

#### Q77. Яке основне призначення HTML?

- [x] HTML структурує веб-сторінку, ідентифікуючи її елементи, такі як абзаци, заголовки та списки.
- [ ] HTML структурує та забезпечує елементарний вигляд веб-сторінок.
- [ ] HTML відповідає за структуру, стиль та інтерактивність веб-сторінок.
- [ ] HTML відповідає за структуру та стиль веб-сторінок.

#### Q78. Коли для наведеного нижче HTML-коду у браузері відобразиться «Sample Text»?

```html
<noscript>Sample Text</noscript>
```

- [ ] коли на цій веб-сторінці не використовується JavaScript
- [x] коли JavaScript не підтримується браузером або якщо JavaScript вимкнено в браузері
- [ ] коли JavaScript вимкнено у веб-браузері
- [ ] коли JavaScript не підтримується веб-браузером

[Довідка (MDN)](https://www.w3schools.com/tags/tag_noscript.asp)

#### Q79. Як цей код відображатиметься за замовчуванням у більшості браузерів?

```HTML
<details>
  <h4>Mixed Berry Tart.</h4>
  <p>
    Raspberries, blueberries, and strawberries on top of a creamy filling served in a crispy tart.
  </p>
</details>
```

- [ ] A
      ![A](images/Q84-1.jpg)
- [x] B
      ![B](images/Q84-2.jpg)
- [ ] C
      ![C](images/Q84-3.jpg)
- [ ] D
      ![D](images/Q84-4.jpg)

#### Q80. Яка різниця між `<svg>` і `<canvas>`?

- [x] `<svg>` створює векторну графіку, тоді як `<canvas>` створює растрову графіку.
- [ ] `<svg>` інтегрується з JavaScript, а `<canvas>` — ні.
- [ ] `<svg>` створює растрову графіку, тоді як `<canvas>` створює векторну графіку.
- [ ] `<svg>` не можна використовувати як фонове зображення, тоді як `<canvas>` можна використовувати як фонове зображення

#### Q81. Яка різниця між атрибутами _readonly_ і _disabled_ для елемента `<textarea>`?

- [x] _readonly_ дозволяє клацати елемент `<textarea>`. _disabled_ запобігає будь-якій взаємодії з елементом.
- [ ] _readonly_ є недійсним атрибутом для `<textarea>`, тоді як _disabled_ є дійсним атрибутом.
- [ ] _disabled_ дозволяє клацати елемент `<textarea>`. _readonly_ запобігає будь-якій взаємодії з елементом.
- [ ] _disabled_ є недійсним атрибутом для `<textarea>`, тоді як _readonly_ є дійсним атрибутом.

1. [Джерело: readonly](https://www.w3schools.com/tags/att_readonly.asp)
2. [Джерело: disabled](https://www.w3schools.com/tags/att_disabled.asp)

#### Q82. In this code, what is _target_?

`<a target="_blank">...</a>`

- [x] an attribute
- [ ] a tag
- [ ] content
- [ ] an element

#### Q83. What is the correct way to add a submit URL to a `button` element?

- [ ] A

```HTML
<button submit="http://example.com/process">Process data</button>
```

- [ ] B

```HTML
<button action="http://example.com/process">Process data</button>
```

- [x] C

```HTML
<button formaction="http://example.com/process">Process data</button>
```

- [ ] D

```HTML
<button method="http://example.com/process">Process data</button>
```

`formation — The URL that processes the information submitted by the button. Overrides the action attribute of the button's form owner. Does nothing if there is no form owner.` [Source](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/button#attr-formaction)

#### Q84. Which is the best markup to produce this text?

`x<y&z>w`

- [ ] `<p>x<y&z>w</p>`
- [x] `<p>x\<y&z\>w</p>`
- [ ] `<p>x<<y&&z>>w`
- [ ] `<p>x<y&z>w</p>`

`This question has an issue, however this answer will count as correct`
`It's too strange a question because all of that methods doesn't work. The good method is &amp, &lt, &gt using.`

#### Q85. What is wrong with this code snippet?

```HTML
<label>Address:</label> <input type="text" name="address" id="address-input" />
```

- [ ] The `<label>` and `<input>` should be nested inside of a `<fieldset>` element.
- [ ] **"address"** is not a valid value for the attribute **name** on an `<input>` element.
- [ ] The `<label>` element is missing an **id** set to "address-input".
- [x] The `<label>` element is missing a **for** attribute set to "address-input".

#### Q86. What is the default method for form submission?

- [x] GET
- [ ] POST
- [ ] PUT
- [ ] SUBMIT

#### Q87. Which is the most semantically correct markup for a side comment in small print?

- [x] `<p>` Get 10% discount `<small>`not valid in France`</small></p>`
- [ ] `<p>` Get 10% discount `<!--not valid in France--> </p>`
- [ ] `<p>` Get 10% discount `<comment>`not valid in France`</comment></p>`
- [ ] `<p>` Get 10% discount `<aside>`not valid in France`</aside></p>`

#### Q88. Which choice will produce the Spanish word <i>canción</i>?

- [x] `<p lang="es">canción</p>`
- [ ] `<p lang="es">canci&oacuten</p>`
- [ ] `<p lang="es">cancio'n</p>`
- [ ] `<p lang="es">canci'on</p>`

#### Q89. What is the purpose of `<caption>`?

- [ ] `<caption>` provides captions for `<audio>`,`<video>`,`<img>`, and `<table>`.
- [x] `<caption>` provides captions to `<table>`.
- [ ] `<caption>` provides captions for `<audio>`, `<video>`, and `<table>`.
- [ ] `<caption>` provides captions for `<img>`, `<audio>`, and `<video>`.

#### Q90. The `value` attribute is associated with which set of tags?

- [x] A

```HTML
<li>
  <input />
  <option></option>
</li>
```

- [ ] B

```HTML
<input>
<option>
<textarea>
```

- [ ] C

```HTML
<button>
  <input />
  <form></form>
</button>
```

- [ ] D

```HTML
<input /> <label> <meter></meter></label>
```

#### Q91. What is wrong with this code?

`<img src="https://source.unsplash.com/random">`

- [ ] `<img>` should be paired with a `<caption>` tag.
- [x] The `<img>` element is missing an alt attribute.
- [ ] `<img>` is not a valid HTML element. Instead, use `<image src="..."/>`.
- [ ] `<img>` should be nested within a `<figure>` tag.

#### Q92. Which choice is the most semantically correct markup for specifying the first definition of a term?

- [ ] `<p>`The `<dl>`focal length`</dl>` of a lens gives the distance from the lens to the image sensor.`</p>`
- [x] `<p>`The `<dfn>`focal length`<dfn>` of a lens gives the distance from the lens to the image sensor.`</p>`
- [ ] `<p>`The `<dt>`focal length`</dt>` of a lens gives the distance from the lens to the image sensor.`</p>`
- [ ] `<p>`The `<dd>`focal length`</dd>` of a lens gives the distance from the lens to the image sensor.`</p>`

**Definition** `element => The <dfn> HTML element is used to indicate the term being defined within the context of a definition phrase or sentence.`<br>`**Description Term element => The <dt> HTML element specifies a term in a description or definition list, and as such must be used inside an <dl> element.`<br>`**Description Details element =>The <dd> HTML element provides the description, definition, or value for the preceding term (<dt>) in a description list (<dl>).`

[Source](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dfn)

#### Q93. Which choice is the best way to code three choices within a form so that the user can select multiple items?

- [ ] :

```HTML
<input type="radio" name="example" /> Choice 1 <br />
<input type="radio" name="example" /> Choice 2 <br />
<input type="radio" name="example" /> Choice 3
```

- [ ] :

```HTML
<input type="checkbox" name="example" /> Choice 1 <br />
<input type="checkbox" name="example" /> Choice 2 <br />
<input type="checkbox" name="example" /> Choice 3
```

- [x] :

```HTML
<label><input type="checkbox" name="example" /> Choice 1</label><br />
<label><input type="checkbox" name="example" /> Choice 2</label><br />
<label><input type="checkbox" name="example" /> Choice 3</label>
```

- [ ] :

```HTML
<label><input type="radio" name="example" /> Choice 1</label><br />
<label><input type="radio" name="example" /> Choice 2</label><br />
<label><input type="radio" name="example" /> Choice 3</label>
```

`<input> elements of type checkbox are rendered by default as boxes that are checked (ticked) when activated as you might see in an official government paper form. The exact appearance depends upon the operating system configuration under which the browser is running. Generally, this is a square but it may have rounded corners.`

[Source](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/checkbox)

#### Q94. How would you mark up a piece of ASCII art (an emoticon) in an accessible way?

- [x] `<pre role="emoticon" aria-label="ASCII emoticon of a shrug">¯\_(ツ)_/¯</pre>`
- [ ] `<pre role="img" aria-label="ASCII emoticon of a shrug">¯\_(ツ)_/¯</pre>`
- [ ] `<dfn title="ASCII emoticon of a shrug">¯\_(ツ)_/¯</dfn>`
- [ ] `<label for="art">ASCII emoticon of a shrug</label><pre role="img" id="art">¯\_(ツ)_/¯</pre>`

#### Q95. Which example is a standard way in HTML5 for adding author metadata to a page?

- [ ] `<metadata name="author" content="Author Name">`
- [ ] `<meta name="author">Author Name</meta>`
- [ ] `<meta name="creator" content="Author Name">`
- [x] `<meta name="author" content="Author Name">`

#### Q96. Given the following requirements, select the correct `input` configuration: An `input` that allows the user to select from a range of integer values between 0 and 100 (inclusive) in increments of 5

- [ ] `<input type="range" min="0" max="100" by="5" />`
- [x] `<input type="range" min="0" max="100" step="5" />`
- [ ] `<input type="number" min="0" max="100" step="5" />`
- [ ] `<input type="number" min="0" max="100" by="5" />`

`<input> elements of type range let the user specify a numeric value which must be no less than a given value and no more than another given value. The step attribute is a number that specifies the granularity that the value must adhere to.`

[Source](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/Input/range)

#### Q97. Which choice is a valid markup for a `<head>` element?

- [x] `<head class="Page Section Information" id="head"><title>Page Title</title></head>`
- [ ] `<head><title>Page Title</title> <img src="favicon.icon" alt=""></head>`
- [ ] `<head><title>Page Title</title> <data value="email">email@example.com</data></head>`
- [ ] `<head><title>Page Title</title><address>email@example.com</address></head>`

`The <head> HTML element contains machine-readable information (metadata) about the document, like its title. The <data> tag is used to add a machine-readable translation of a given content.`
[Source 1](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/head)/
[Source 2](https://www.w3schools.com/tags/tag_data.asp)

#### Q98. You need to add comments to the company blog. What is the most semantic markup for a list of comments?

- [x] A

```html
<aside>
  <h3>Comments</h3>
  <article>First comment.</article>
  <article>Second comment.</article>
</aside>
```

- [ ] B

```html
<div aria="dpub-comments">
  <h3>Comments</h3>
  <div aria="dpub-comment">First comment.</div>
  <div aria="dpub-comment">Second comment.</div>
</div>
```

- [ ] C

```html
<aside>
  <h3>Comments</h3>
  <aside>First comment.</aside>
  <aside>Second comment.</aside>
</aside>
```

- [ ] D

```html
<div typeof="comments">
  <h3>Comments</h3>
  <div typeof="comment">First comment.</div>
  <div typeof="comment">Second comment.</div>
</div>
```

`The <article> HTML element represents a self-contained composition in a document, page, application, or site, which is intended to be independently distributable or reusable (e.g., in syndication). Example: a user-submitted comment.`
[Source](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/article)

#### Q99. To make something editable by the user, you need to set the **\_** attribute to **\_**

- [ ] `access`; allow
- [ ] `designMode`; true
- [x] `contenteditable`; true
- [ ] `contenteditable`; yes

`The contenteditable global attribute is an enumerated attribute indicating if the element should be editable by the user. If so, the browser modifies its widget to allow editing. The attribute must take one of the following values: true or an empty string, which indicates that the element is editable; false, which indicates that the element is not editable.`
[Source](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/contenteditable)

#### Q100. Which choice is the standard way to include a value in a form without making it visible to or editable by the user?

- [ ] `<input type="invisible" name="important" value="information">`
- [ ] `<input type="text" style="display: none;" name="important" value="information">`
- [x] `<input type="hidden" name="important" value="information">`
- [ ] `<input type="text" hidden name="important" value="information">`

`<input> elements of type hidden let web developers include data that cannot be seen or modified by users when a form is submitted. For example, the ID of the content that is currently being ordered or edited, or a unique security token. Hidden inputs are completely invisible in the rendered page, and there is no way to make it visible in the page's content.` [Source](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/hidden)

#### Q101. What is the semantic way to add an identifying title to a table?

- [ ] `<table><label>Heading</label>...</table>`
- [ ] `<table><title>Heading</title>...</table>`
- [ ] `<table><legend>Heading</legend>...</table>`
- [x] `<table><caption>Heading</caption>...</table>`

`The <caption> HTML element specifies the caption (or title) of a table.` [Source](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/caption)

#### Q102. Which image file referenced in this `img` element's `srcset` attribute should a browser on a small mobile phone load?

```html
<img
  srcset="medium.jpg 320w, large.jpg 1280w"
  src="small.jpg"
  alt="Our favorite image"
  sizes="(min-width: 1200px) 640px, 100vw"
/>
```

- [ ] small.jpg
- [ ] medium.jpg
- [ ] none of them
- [x] large.jpg

`The browser will: 1. Look at its device width. 2. Work out which media condition in the sizes list is the first one to be true. 3. Look at the slot size given to that media query. 4. Load the image referenced in the srcset list that has the same size as the slot or, if there isn't one, the first image that is bigger than the chosen slot size.` [Source](https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Responsive_images)

#### Q103. Which description is coded correctly?

- [x] A

```HTML
<dl>
  <dt>Server</dt>
  <dd>Software used to serve webpages, like Apache.</dd>
  <dd>Hardware used to provide data to other computers.</dd>
  <!-- Other terms and descriptions -->
</dl>
```

- [ ] B

```HTML
<dt>
  <dl>Server</dl>
  <dd>Software used to serve webpages, like Apache.</dd>
  <dd> Hardware used to provide data to other computers.</dd>
  <!-- Other terms and descriptions -->
</dt>
```

- [ ] C

```HTML
<dl>
  <dt>Server</dt>
  <dd>Software used to serve webpages, like Apache.</dd>
  <dt>Hardware used to provide data to other computers.</dt>
  <!-- Other terms and descriptions -->
</dl>
```

- [ ] D

```HTML
<dl>
  <dd>Server</dd>
  <dt>Software used to serve webpages, like Apache.</dt>
  <dt>Hardware used to provide data to other computers.</dt>
  <!-- Other terms and descriptions -->
</dl>
```

[Source 1](https://html.spec.whatwg.org/multipage/grouping-content.html#the-dl-element)
[Source 2](https://www.w3schools.com/tags/tag_dl.asp)

#### Q104. What is wrong with this code?

```html
<ul>
  <h2>Espresso Drinks</h2>
  <li>Espresso</li>
  <li>Latte</li>
  <li>Cappuccino</li>
  <li>Mocha</li>
</ul>
```

- [ ] Nothing is wrong.
- [x] `<ul>` cannot contain a heading element as a direct child.
- [ ] An `<h1>` should be used here instead of an `<h2>` tag.
- [ ] Only `<ol>` allows direct descendants to contain elements other than an `<li>`, so use an `<ol>` here instead.

`ul content model only accepts "Zero or more li and script-supporting elements".` [Source](https://html.spec.whatwg.org/multipage/grouping-content.html#the-ul-element)

#### Q105. A designer gave you CSS code that should run only when the device rendering the page is in dark mode. How would you embed that code?

- [ ] `<style media="light-mode: false">/* CSS code */</style>`
- [ ] `<style media="color-mode: dark">/* CSS code */</style>`
- [x] `<style media="prefers-color-scheme: dark">/* CSS code */</style>`
- [ ] `<style media="color-scheme: dark">/* CSS code */</style>`

#### Q106. How would you mark up a header for a table row?

- [ ] A

```HTML
<table>
  <thead scope="row">
    <th row="1">Header</th>
  </thead>
  <tr>
    <td>10</td>
    <td>18</td>
  </tr>
</table>
```

- [x] B

```HTML
<table>
  <tr>
    <th scope="row">Header</th>
    <td>10</td>
    <td>18</td>
  </tr>
</table>
```

- [ ] C

```HTML
<table>
  <tr>
    <thead scope="row">
      Header
    </thead>
    <td>10</td>
    <td>18</td>
  </tr>
</table>
```

- [ ] D

```HTML
<table>
  <tr>
    <th>Header</th>
    <td>10</td>
    <td>18</td>
  </tr>
</table>
```

#### Q107. Which statement is correct?

- [ ] The `<main>` element represents the dominant content of an `<article>` in a document.
- [ ] The `<main>` element represents the dominant content of a `<section>` of a document. You may have one `<main>` element per section.
- [x] The `<main>` element represents the dominant content of your document. There can be only one `<main>` element that is not hidden.
- [ ] The `<article>` element represents the dominant content of your document. There can be only one `<article>` element that is not hidden.

[Source](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/main)

#### Q108. Users report that a form is not working. What is the culprit?

```HTML
<form action="/choices" disabled>
  <fieldset disabled>
    <legend>choices</legend>
    <label>Choice 1 <input type="radio" name="choice" value="choice1" /></label>
    <label>Choice 2 <input type="radio" name="choice" value="choice1" /></label>
    <label>Choice 3 <input type="radio" name="choice" value="choice1" /></label>
    <label>Choice 4 <input type="radio" name="choice" value="choice1" /></label>
    <button>Choose!</button>
  </fieldset>
</form>
```

- [ ] The form element is disabled.
- [ ] There is no <input type="submit"> element.
- [x] The fieldset is disabled.
- [ ] There is no method set on the form.

A disabled fieldset is unusable and un-clickable. [Source](https://www.w3schools.com/tags/att_fieldset_disabled.asp)

#### Q109. Which description list is coded correctly?

- [x] A

```HTML
<dl>
  <dt>Server</dt>
  <dd>Software used to server webpages, like Apache.</dd>
  <dd>Hardware used to provide data to other computers.</dd>
  <!--Other terms and descriptions -->
</dl>
```

- [ ] B

```HTML
<dl>
  <dd>Server</dd>
  <dt>Software used to server webpages, like Apache.</dt>
  <dt>Hardware used to provide data to other computers.</dt>
  <!--Other terms and descriptions -->
</dl>
```

- [ ] C

```HTML
<dt>
    <dl>Server</dl>
    <dd>Software used to server webpages, like Apache.</dd>
    <dd>Hardware used to provide data to other computers.</dd>
    <!--Other terms and descriptions -->
</dt>
```

- [ ] D

```HTML
<dl>
  <dt>Server</dt>
  <dd>Software used to server webpages, like Apache.</dd>
  <dt>Hardware used to provide data to other computers.</dt>
  <!--Other terms and descriptions -->
</dl>
```

#### Q110. what does the a in the HTML tag stand for?

- [ ] assign
- [ ] add tag
- [x] anchor tag
- [ ] None of the above

[Source](https://stackoverflow.com/questions/39434659/what-does-the-a-in-the-html-a-tag-stand-for)

#### Q111. What is the correct HTML element for inserting a line break?

- [ ] `<break>`
- [ ] `<lb>`
- [x] `<br>`
- [ ] `<a>`

#### Q112. The HTML global attribute, "contenteditable" is used to

- [ ] Update content from the server
- [ ] Specifies a context menu for an element. The menu appears when a user right-clicks on the element.
- [x] Specify whether the content of an element should be editable or not
- [ ] Return the position of the first found occurrence of content inside a string

#### Q113. HTML elements that aren't meant to store content or other elements are called **\_** elements

- [x] void
- [ ] independent
- [ ] empty
- [ ] paragraph

[Source](https://www.w3.org/TR/2011/WD-html-markup-20110113/syntax.html#syntax-elements)

#### Q114. The **\_** attribute of an HTML label element is a referencing mechanism to state what input or element the label is tied to

- [ ] to
- [ ] of
- [ ] with
- [x] for

[Source](https://www.w3schools.com/tags/att_label_for.asp)

#### Q115. Coding in HTML provides which of the following?

- [ ] The responsiveness of the website
- [ ] The style of the website
- [x] The core website structure
- [ ] The behavior of web elements

#### Q116. Which HTML element is the container for all the renderable aspects of the document?

- [ ] head
- [x] body
- [ ] title
- [ ] meta

#### Q117. The "h" in the HTML h1 tag is short for **\_**

- [ ] head
- [ ] horizontal
- [ ] hypertext
- [x] heading

[Source](https://www.w3schools.com/html/html_headings.asp)

#### Q118. Which is an invalid use of the `<a>` element?

- [ ] A

```HTML
<a href="#additional-information" class="Card">
  <video src="media.mp4" width="400" height="300"></video>
</a>
```

- [x] B

```HTML
<a href="#additional-information" class="Card">
  <details>
    <summary>Additional Information</summary>
  </details>
</a>
```

- [ ] C

```HTML
<a href="#additional-information" class="Card">
  <p>Additional Information</p>
  <p></p
></a>
```

- [ ] D

```html
<a href="#additional-information" class-"Card">
  <img src="media.jpeg" alt="More information"></video>
</a>
```

#### Q119. How to display preformatted text in HTML?

- [ ] `<p>`
- [x] `<pre>`
- [ ] `<hr>`
- [ ] All of the above

#### Q120. Which is a valid title element?

- [ ] `<title><em>Exciting</em> title</title>`
- [ ] `<title></title>`
- [ ] `<title name="Exciting Title" />`
- [x] `<title>Exciting title</title>`

[Source](https://www.w3schools.com/tags/tag_title.asp)

#### Q121. Which link contains a valid URL?

- [ ] `<link rel="stylesheet" href="/styles for me/styles.css">`
- [ ] `<link rel="stylesheet" href="/styles|for|me/styles.css">`
- [ ] `<link rel="css" href="\styles for me\styles.css">`
- [x] `<link rel="stylesheet" href="/styles%20for%20me/styles.css">`

[Source 1](https://www.w3schools.com/tags/att_link_href.asp)
[Source 2](https://www.sistrix.com/ask-sistrix/technical-seo/site-structure/do-i-have-to-convert-the-spaces-in-urls)

#### Q122. Which example is missing a mandatory closing tag, making it invalid?

- [ ] `<p>Simple paragraph`
- [x] `<ul><li>Simple list</li>`
- [ ] `<ul><li>Simple list<ul>`
- [ ] `<dl><dt>Simple term<dd>Simple description</dl>`

[Source](https://blog.teamtreehouse.com/to-close-or-not-to-close-tags-in-html5)

#### Q123. What is the semantic method for marking up a video with a caption in browsers that support it?

- [ ] `<video src="video.mp4" caption="video.vtt"></video>`
- [ ] `<video src="video.mp4"><track caption="video.vtt" /></video>`
- [x] `<video src="video.mp4"><track default kind="captions" srclang="en" src="video.vtt" /></video>`
- [ ] `<video src="video.mp4"><caption default srclang="en" src="video.vtt" /></video>`

[Source](https://developer.mozilla.org/en-US/docs/Web/Guide/Audio_and_video_delivery/Adding_captions_and_subtitles_to_HTML5_video)

#### Q124. A white paper has a sidebar and endnotes, both of which are complementary to the main text. How would you mark them up to make their distinct roles more broadly accessible?

- [ ] A

```HTML
<custom-sidebar aria-label-"Sidebar"›Sidebar...</custom-sidebar><custom-footnote aria-
label="Endnotes">Endnotes...</custom-footnote>
```

- [x] B

```HTML
<aside role="sidebar">Sidebar...</aside>
<aside role="notes">Endnotes...</aside>
```

- [ ] C

```HTML
<aside role="complementary">Sidebar...</aside>
<aside role="supplementary">Endnotes...</aside>
```

- [ ] D

```HTML
<aside aria-label-"Sidebar">Sidebar...</aside><aside aria-label="Endnotes">Endnotes...</aside>
```

[Source](https://www.w3.org/TR/wai-aria-practices-1.2/#doc_noteref)

#### Q125. A white paper has a sidebar and endnotes, both of which are complementary to the main text. How would you mark them up to make their distinct roles more broadly accessible?

- [x] `<aside aria-label="Sidebar">Sidebar...</aside><aside aria-label="Endnotes">Endnotes...</aside>`
- [ ] `<custom-sidebar aria-label="Sidebar">Sidebar...</custom-sidebar><custom-footnote aria-label="Endnotes">Endnotes...</custom-footnote>`
- [ ] `<aside role="Sidebar">Sidebar...</aside><aside role="Endnotes">Endnotes...</aside>`
- [ ] `<aside role="complementary">Sidebar...</aside><aside role="supplementary">Endnotes...</aside>`

[Source](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Roles)

#### Q126. Which video example will autoplay in most browsers?

- [x] `<video src="video.mp4" autoplay muted></video>`
- [ ] `<video src="video.mp4" background></video>`
- [ ] `<video src="video.mp4" autoplay></video>`
- [ ] `<video src="video.mp4" autoplay="force"></video>`

[Source](https://stackoverflow.com/questions/65157672/force-html5-video-autoplay-unmuted)

#### Q127. In which order will these scripts execute, assuming they all take the same time to download?

```HTML
<script type="module" src="module.js"></script>
// external module
<script type="async" src="module.js"></script>
// async
<script type="defer" src="module.js"></script>
// defer
<script type="module" src="module.js">
  // inline module
</script>
```

- [ ] async, external module, defer, inline module
- [ ] async, inline module, external module, defer
- [x] external module, async, defer, inline module
- [ ] inline module, external module, defer, async

#### Q128. What is the backward-compatible method of turning a circle in an SVG into a link?

- [ ] `<html:a href="/our-circle/"><circle cx="10" cy="10" r="5"/></html:a>`
- [ ] `<a svg:href="/our-circle/"><circle cx="10" cy="10" r="5"/></a>`
- [ ] `<a href="/our-circle/"><circle cx="10" cy="10" r="5"/></a>`
- [x] `<a href="/our-circle/" xlink:href="/our-circle/"><circle cx="10" cy="10" r="5"/></a>`

[Source](https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/xlink:href)

#### Q129. Users report that a form is not working. What is the culprit?

```HTML
  <form action="/choices" disabled>
    <fieldset disabled>
      <legend>Choices</legends>
      <label>Choice 1 <input type="radio" name="choice" value="choice1" /></label>
      <label>Choice 2 <input type="radio" name="choice" value="choice2" /></label>
      <label>Choice 3 <input type="radio" name="choice" value="choice3" /></label>
      <label>Choice 4 <input type="radio" name="choice" value="choice4" /></label>
      <button>Choose!</button>
    </fieldset>
  </form>
```

- [x] There is no <input type="submit"> element.
- [ ] There is no method set on the form.
- [ ] The form element is disabled.
- [ ] The fieldset is disabled.

#### Q130. What is wrong with this table?

```HTML
<table>
  <legend>A two body table!</legend>
  <col />
  <col />
  <tbody>
    <tr>
      <td>Cell 1</td>
      <td>Cell 1</td>
    </tr>
  </tbody>
  <tbody>
    <tr>
      <td>Cell 1</td>
      <td>Cell 1</td>
    </tr>
  </tbody>
</table>
```

- [ ] A table can only have one tbody element.
- [ ] legend must appear at the end of a table element.
- [ ] legend is not allowed in a table element.
- [x] All col elements must be wrapped in a colgroup element.

[Source](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/col)

#### Q131. In this code, what is the purpose of the `id` attribute?

```HTML
<p id="warning">Be careful when installing this product.</p>
```

- [x] It establishes that `warning` is a unique identifier in the document, used for styling CSS, scripting, and linking within a webpage.
- [ ] It establishes that `warning` is a unique identifier in the document, used for styling CSS and with JavaScript code.
- [ ] It establishes that `warning` may be used for styling CSS several times per page.
- [ ] It establishes that `warning` is a unique identifier in the website, used for styling CSS, scripting, and linking within a webpage.

[Source](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/id)

### Q132. What does the HTML `<em>` element represent?

- [x] Stress emphasis, usually displayed as italic text
- [ ] Italic text
- [ ] A hyperlink
- [ ] A line break

[Source](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/em)

### Q133. The \***\*\_\*\*** element is used to render simple graphics such as line art, graphs, and other custom graphical elements on the client side.

- [ ] metadata
- [ ] css
- [x] canvas
- [ ] art

### Q134. Which attribute is not essential under <iframe>?

- [x] frameborder
- [ ] width
- [ ] height
- [ ] src

### Q135.What does HTML stands for?

- [ ] Hypertext Machine language.

- [ ] Hypertext and links markup language.

- [x] Hypertext Markup Language.

- [ ] Hightext machine language.

[Source]: https://www.geeksforgeeks.org/aptitude-html-course-practice-quiz-1-question-1/

### Q136.Which of the following HTML element is used for creating an unordered list?

- [ ] `<ui>`

- [ ] `<i>`

- [ ] `<em>`

- [x] `<ul>`

[Source]: https://www.geeksforgeeks.org/web-technologies-questions-html-course-practice-quiz-1-question-4/
