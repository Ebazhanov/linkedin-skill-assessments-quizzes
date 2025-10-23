## Front-end Development

#### Q1. Which image matches the flex layout defined in this style rule?

```css
.container {
  display: flex;
}

.container div:last-child {
  margin-left: auto;
}
```

- [ ] ![A](images/Q1-A.jpg)
- [x] ![B](images/Q1-B.jpg)
- [ ] ![C](images/Q1-C.jpg)
- [ ] ![D](images/Q1-D.jpg)

[Sample](https://jsfiddle.net/mrvahid/zohd8k2n/)

#### Q2. Variables declared with the let keyword have what type of scope?

- [ ] function scope
- [x] block scope
- [ ] inline scope
- [ ] global scope

#### Q3. Why would you surround a piece of text with `<h1></h1>` tags?

- [x] to indicate that this text is the main heading on the page
- [ ] to make the text bold
- [ ] to ensure that search engines treat the keywords as being important for this page
- [ ] to demonstrate to screen readers that this text is important

#### Q4. When might an empty alt attribute be the correct value?

- [ ] when you cannot think of useful alt text
- [ ] when you don't think it would be interesting to someone who cannot see it
- [ ] when the image has come from a CMS
- [x] when the image is purely decorative

#### Q5. Which attribute must have a unique value each time it is used in an HTML document?

- [ ] title
- [ ] class
- [ ] style
- [x] id

#### Q6. Which CSS property will not trigger layout recalculation?

- [ ] top
- [x] opacity
- [ ] width
- [ ] height

#### Q7. What will be the value of selected?

```javascript
let pocket = ['turnip', 'stone', 'log', 'apple'];
let selected = pocket[1];
```

- [ ] log
- [ ] apple
- [x] stone
- [ ] turnip

#### Q8. What does the `===` comparison operator do?

- [ ] It sets one variable equal to another in both value and type
- [ ] It tests for equality of type only
- [ ] It tests for equality of value only
- [x] It tests for equality of value and type

#### Q9. In the following code, the variable `fruit` has been assigned a value of apple. How would you change the value to plum?

```javascript
let fruit = 'apple';
```

- [ ] `let fruit = 'plum'`
- [ ] `var fruit = 'plum'`
- [ ] `const fruit = 'plum'`
- [x] `fruit = 'plum'`

#### Q10. What is the `<label>` element used for?

- [ ] to identify the different parts of a figure
- [x] to explain what needs to be entered into a form field
- [ ] as a caption for images
- [ ] as a heading for tables

#### Q11. The browser finds some CSS that it does not understand. What is likely to happen?

- [ ] The page will not display
- [ ] An error message will be displayed
- [ ] The browser will not load the stylesheet
- [x] The browser will ignore the unknown CSS

#### Q12. In this code, what is the term for the h1?

```css
h1 {
  color: red;
  font-size: 5em;
}
```

- [x] selector
- [ ] combinator
- [ ] declarator
- [ ] markup

#### Q13. Which HTML will result in text being highlighted in yellow?

```css
.highlight {
  background-color: yellow;
}
```

- [x] `<span class="highlight">#BLM</span>`
- [ ] `<span style="highlight">#BLM</span>`
- [ ] `<highlight">#BLM</span>`
- [ ] `<div id="highlight">#BLM</span>`

#### Q14. Which choice is not a value of the type attribute of the `<input>` element?

- [ ] range
- [x] address
- [ ] date
- [ ] password

#### Q15. You have used `display: none` in your stylesheet. Which users will be able to see or hear this content?

- [ ] all users
- [ ] users who can see the content on the screen
- [x] no users
- [ ] screen reader users

#### Q16. Which choice is not part of CSS box model?

- [ ] margin
- [ ] border
- [ ] padding
- [x] paragraph

#### Q17. Which part of the URL `https://app.uniswap.org/pool` specifies the domain name?

- [ ] https
- [ ] org
- [x] uniswap.org
- [ ] app.uniswap

#### Q18. Which HTML element is not considered a landmark element?

- [ ] `<form>`
- [x] `<ul>`
- [ ] `<main>`
- [ ] `<nav>`

[Source: ARIA landmarks in HTML5](https://www.w3.org/TR/2017/NOTE-wai-aria-practices-1.1-20171214/examples/landmarks/HTML5.html)

#### Q19. Which statement is true when an HTML tag has been deprecated?

- [ ] It employs code that can be viewed only on a desktop computer
- [x] It is obsolete and is not recommended for use in marking web content
- [ ] It employs code that will require users to update their browsers
- [ ] It employs incorrect syntax that will cause the browser to crash

#### Q20. How does the rem unit represent a font size?

- [ ] Font sizes are expressed relative to the font size of the containing div element
- [ ] Font sizes are expressed relative to the font size of the parent elements
- [ ] Font sizes are relative to the base font size of the operating system.
- [x] Font sizes are relative to the root em unit used in the HTML element.

[Source: CSS units](https://www.w3schools.com/cssref/css_units.asp)

#### Q21. Which HTML element represents either a scalar value within a known range OR a fractional value?

- [x] `<meter>`
- [ ] `<range>`
- [ ] `<datalist>`
- [ ] `<optgroup>`

#### Q22. What is Webpack primarily used for?

- [ ] sharing JavaScript code with other people
- [ ] making JavaScript-reliant sites accessible to users who do not have JavaScript turned on
- [x] bundling individual JavaScript files for use on your website
- [ ] source control

#### Q23. How many columns will there be, given this code?

```css
.container {
  width: 600px;
  column-width: 200px;
  column-gap: 50px;
}
```

- [ ] one
- [ ] three
- [ ] four
- [x] two

#### Q24. Which style will change the color of the text?

```html
<cite>Noam Chomsky</cite>
```

- [ ] A

```css
cite {
  text-color: cyan;
}
```

- [ ] B

```css
cite {
  font-color: cyan;
}
```

- [x] C

```css
cite {
  color: cyan;
}
```

- [ ] D

```css
cite {
  text: cyan;
}
```

#### Q25. You find this code in a stylesheet. What is it being used for?

```css
.cf::after {
  content: '';
  display: block;
  clear: both;
}
```

- [ ] inserting content that cannot be seen by screen readers
- [ ] fixing an Internet Explorer 11 bug
- [x] clearing floats in float-based layouts
- [ ] creating a new block formatting context

#### Q26. What is the correct way to initialize an array of galaxies in JavaScript?

- [ ] `String[] galaxies = new Array("Milky Way", "Whirlpool", "Andromeda");`
- [ ] `let galaxies = {Milky Way, Whirlpool, Andromeda};`
- [x] `galaxies = ["Milky Way", "Whirlpool", "Andromeda"];`
- [ ] `var galaxies = {"Milky Way", "Whirlpool", "Andromeda"};`

#### Q27. Which description correctly describes the initial values of flex items if you have applied `display: flex` to their parent?

- [x] Items display in a row, lined up at the start, and do not stretch to fill the container
- [ ] Items display in a column, lined up at the start, and do not stretch to fill the container
- [ ] Items stay in a column until you add some flex properties.
- [ ] Items displayed in a row, lined up at the start and stretched to fill the container

#### Q28. Which line of code, if applied to all flex items in a flex container, would cause each flex item to take up an equal share of the total width of the container? For example, if there are four items, they would get 25% of each.

- [ ] `flex: 1 0 0;`
- [ ] `flex: initial;`
- [x] `flex: 1 1 auto;`
- [ ] `flex: 1 0 auto;`

#### Q29. A video on your webpage does not display and the console shows an error about mixed content. What is happening?

- [ ] The webpage is using a DOCTYPE, which renders it incapable of displayed video in addition to other web content.
- [ ] Your browser does not support HTML5 video.
- [ ] The video is from a source that cannot be displayed in your location for legal reasons.
- [x] The page is loaded via HTTPS, but the video is being served insecurely as HTTP and the browser is blocking it.

#### Q30. What will this loop print?

```
let max = 3;
for (i = 0; i > max; i++) {
  document.write("skrt ");
}
```

- [ ] skrt skrt skrt
- [ ] skrt skrt
- [ ] skrt skrt skrt skrt
- [x] nothing

#### Q31. You have placed an image in a directory named images and want to reference it from a page located at the root of your site. Which choice would correctly display the image on the page?

- [ ] `<img src="image.jpg">`
- [ ] `<a href="images/image.jpg"></a>`
- [x] `<img src="images/image.jpg">`
- [ ] `<img href="image.jpg">`

#### Q32. Which choice is a correct use of the parseInt() function in Javascript that parses a string and returns an integer?

- [ ] parseInt("six");
- [ ] parse_int('6');
- [x] parseInt("6");
- [ ] parseint("6");

#### Q33. How can you rewrite this function using arrow function syntax?

- [ ] `let product => (x,y) { <br /> x \* y; <br />}`
- [x] `let product = (x,y) => x\*y;`
- [ ] `let product => x\*y;`
- [ ] `let product = (x,y) -> x\*y;`

#### Q34. Lighthouse is a tool for auditing your website. Which choice is not a category of report offered by Lighthouse?

- [ ] performance
- [x] UX design
- [ ] accessibility
- [ ] SEO

#### Q35. In the context of this code, how would you describe user?

```
const user = {
  given_name: 'Joe',
  family_name: 'Bloggs',
  age: 40,
}
```

- [ ] function
- [ ] array
- [ ] variable
- [x] object

#### Q36. A webpage has `rel="preconnect"` added to a link resource. What will this do?

```html
<link rel="preconnect" href="https://example.com" />
```

- [ ] It will tell the browser that this link is a site belonging to the current domain.
- [ ] It will do nothing because this is a deprecated attribute that browsers do not support.
- [x] It will tell the browser that a connection will be made to another origin and to start getting ready as soon as possible.
- [ ] It will tell the browser that a resource is needed, and that it should start getting fetched as soon as possible.

[Source: web.dev](https://web.dev/preconnect-and-dns-prefetch/)

#### Q37. Which choice is _not_ a render blocking resource?

- [x] images
- [ ] HTML
- [ ] CSS
- [ ] JavaScript

[blog.logrocket](https://blog.logrocket.com/5-tricks-to-eliminate-render-blocking-resources/)

#### Q38. Which choice does _not_ provide information on browser support for a particular CSS property?

- [ ] the "Can I Use" website
- [x] the Web Platform Tests Suite
- [ ] the CSS specification
- [ ] MDN property pages

[Source: Web platform tests site](https://web-platform-tests.org/)

#### Q39. You have a set of images that are slightly different sizes and aspect ratios. You don't mind if you crop off some of the image, but you want each image to completely fill a square box without being distorted. Which property and value would achieve this?

- [ ] object-fit: contain
- [ ] object-fit: stretch
- [ ] object-fit: all
- [x] object-fit: cover

#### Q40. what does the CSS selector a[href$="org"] select?

- [ ] all \<a> tags whose href attribute begins with "org"
- [ ] all \<a> tags whose href attribute equals "org"
- [x] all \<a> tags whose href attribute ends with "org"
- [ ] all \<a> tags whose href attribute contains "org"

#### Q41. Which choice <em>is not a result</em> of invoking strict mode in JavaScript?

- [ ] It eliminates some JavaScript silent errors by changing them to throw errors.
- [ ] It prohibits some syntax likely to be defined in future versions of ECMAScript.
- [x] It forces the writing of valid HTML and CSS.
- [ ] It fixes mistakes that make it difficult for JavaScript engines to perform optimizations.

[Source: MDN docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode)

#### Q42. In normal flow, some elements display as block elements default and others inline. which choice contains only block-level by default elements?\*\*

- [ ] ul, li, a
- [ ] p, b, h3
- [ ] div, p, em
- [x] div, main, h1

#### Q43. Which line would you add to this code to add "Cosmos" to the list of currencies using JavaScript?

```javascript
var currencies = ['Bitcoin', 'Ethereum'];

/* Missing line */
console.log(currencies);
```

- [x] `currencies.push("Cosmos");`
- [ ] `Array.append("Cosmos", currencies);`
- [ ] `currencies.add("Cosmos");`
- [ ] `currencies(2) = "Cosmos";`

#### Q44. How would you change this code to make Vanilla selected by default?

```javascript
<input type="radio" value="strawberry">Strawberry
<input type="radio" value="vanilla">Vanilla
<input type="radio" value="chocolate">Chocolate
```

- [x] `<input type="radio" value="vanilla" checked>`
- [ ] `<input type="radio" value="vanilla" check>`
- [ ] `<input type="radio" value="vanilla" selected>`
- [ ] `<input type="radio" value="vanilla" on>`

#### Q45. **\_** moves an element completely out of the page's normal layout flow like it is sitting on its own separate layer. From there, you can fix it in a position relative to the edges of the page's `<html>` element (or its nearest positioned ancestor element).

- [ ] Sticky positioning
- [x] Absolute positioning
- [ ] Relative positioning
- [ ] Fixed positioning

[Source: W3Schools](https://www.w3schools.com/css/css_positioning.asp)

**position: absolute;**
`An element with position: absolute; is positioned relative to the nearest positioned ancestor (instead of positioned relative to the viewport, like fixed). However; if an absolute positioned element has no positioned ancestors, it uses the document body, and moves along with page scrolling.`

#### Q46. You have created a box that has a height set with CSS. Which line of CSS would add scroll bars if the content is taller than the box, but leave no visible scroll bars if the content fits into the box?

- [ ] .box { overflow: scroll; }
- [ ] .box { overflow: scroll-x; }
- [x] .box { overflow: auto; }
- [ ] .box { overflow: none; }

#### Q47. Which array method should you apply to run a function for every item within an array, returning an array of all items for which the function is true?

- [ ] every()
- [ ] map()
- [ ] forEach()
- [x] filter()

#### Q48. The image below has float: left applied. Text wraps the float on the right and bottom. How would you force the second paragraph to start underneath the float, leaving a gap after the preceding paragraph?

![CSS clear](images/Q48.png?raw=true)

- [ ] Apply `float: left` to the second paragraph.
- [ ] Apply `clear: right` to the floated item.
- [x] Apply `clear: left` to the second paragraph.
- [ ] Apply `clear: left` to the floated item.

[Source: W3Schools](https://www.w3schools.com/css/css_float_clear.asp)

**clear: left;**
`When we use the float property, and we want the next element below (not on the right or left), we will have to use the clear property. When clearing floats, you should match the clear to the float: If an element is floated to the left, then you should clear to the left. Your floated element will continue to float, but the cleared element will appear below it on the web page.`

#### Q49. You want to create striped table rows using CSS without adding a class to any element. Which CSS would correctly apply the background color to every odd row in your table?

- [ ] `tr:nth-child(2) { background-color: #ccc; }`
- [x] `tr:nth-child(2n+1) { background-color: #ccc; }`
- [ ] `tr:nth-child(2+1) { background-color: #ccc; }`
- [ ] `tr:nth-child(2n) { background-color: #ccc; }`

[Source: W3Schools](https://www.w3schools.com/cssref/sel_nth-child.asp)

#### Q50. You are designing a site and creating a navigation bar linking to the main sections. Which HTML element should you use to indicate that this is the main navigation?

- [x] `<nav>`
- [ ] `<navigation>`
- [ ] `<main>`
- [ ] `<ul>`

[Source: W3Schools](https://www.w3schools.com/tags/tag_nav.asp)

#### Q51. You discover that CSS is being loaded on a website using the following code. Why might a web developer have done this?

`<link rel="preload" href="styles.css" as="style" onload="this.onload=null;this.rel='stylesheet'"><noscript><link rel="stylesheet" href="style.css"></noscript>`

- [x] The CSS is being loaded asynchronously in order to prevent render blocking.
- [ ] This will stop the CSS from being loaded for old browsers that do not support the techniques in use.
- [ ] This is part of a stylesheet-switching script to load different themes for the site.
- [ ] This will stop the CCS from being loaded on slow data connections.

[Source: StackOverflow](https://stackoverflow.com/a/46750893)

#### Q52. The flex property is often applied to flex items with a value of 1. Using flex: 1 is a shorthand - what does it unpack to?

- [ ] flex: 0 0 100;
- [ ] flex: 1 0 0;
- [ ] flex: 0 0 auto;
- [x] flex: 1 1 auto;

[Source: stackoverflow](https://stackoverflow.com/questions/37386244/what-does-flex-1-mean)

#### Q53. What is the meaning of "tree shaking" in relation to JavaScript performance?

- [ ] only using code that is supported by the newest browsers, and serving the site without JavaScript to old browsers
- [x] removing unused code from the JavaScript files
- [ ] splitting code into various bundles so that decisions can be made on loading priority
- [ ] allowing the browser to ignore code it believes will perform badly

[Source: MDN Docs](https://developer.mozilla.org/en-US/docs/Glossary/Tree_shaking)

#### Q54. What is WebP?

- [ ] a method of auditing performance that gives your site a score, which is then used for Google ranking
- [x] a next-generation image format offering a smaller file size than equivalent PNG or JPEG images
- [ ] a new font format that allows a single font to display at different styles and weights
- [ ] a next-generation PDF format that offers a smaller file size and better accessibility than standard PDF documents

[Source: Google Developers](https://developers.google.com/speed/webp)

#### Q55. Your website uses CSS Grid Layout extensively, and a visitor who navigates using the keyboard tells you that they seem to jump erratically all over the screen when navigating. What is the most likely problem?

- [ ] The visitor's browser does not have full support for CSS Grid Layout.
- [x] Items have been positioned in such a way that they are in a different order to the source.
- [ ] The browser has a keyboard navigation bug.
- [ ] You need to add the tabindex attribute to elements.?

[Source: MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout/CSS_Grid_Layout_and_Accessibility)

#### Q56. What is the definition of the phrase "Time to Interactive"?

- [ ] when the browser displays the first bit of content from the DOM
- [x] when the user can consistently interact with all of the page elements
- [ ] when HTML has loaded, but not necessarily JavaScript, CSS, or images
- [ ] when the user can see the webpage on the screen

[Source: Web.dev](https://web.dev/interactive/)

#### Q57. What is yarn?

- [ ] a JavaScript framework that is leaner than React
- [ ] a JavaScript bundler
- [ ] a testing framework
- [x] a JavaScript package manager

[Source: Yarn Docs](https://yarnpkg.com/)

#### Q58. What is the name of the event that occurs when the mouse pointer hovers over an element?

- [ ] load
- [x] mouseover
- [ ] hover
- [ ] focus

[Source: MDN Docs](https://developer.mozilla.org/en-US/docs/Web/API/Element/mouseover_event)

#### Q59. What is meant by the term "polyfill" when used in web development?

- [x] It is a piece of code that provides modern functionality in browsers that do not support it.
- [ ] It is a piece of code that hides broken content from old browsers.
- [ ] It is a term for languages such as Saas that compile to CSS.
- [ ] It is a script that runs to add vendor prefixes to modern CSS.

[Source: Polyfill](https://developer.mozilla.org/en-US/docs/Glossary/Polyfill)

#### Q60. Which choice is _not_ a JavaScript framework?

- [ ] Angular
- [x] Laravel
- [ ] Vue
- [ ] React

[Source: Laravel](https://laravel.com/)

#### Q61. What does setting `aria-live=polite` on a live region achieve?

- [ ] The screen reader will not notify the user of changes to live regions.
- [x] The screen reader will wait until there is a pause to announce changes.
- [ ] The screen reader will announce all changes immediately.
- [ ] The screen reader will use a polite voice when announcing changes.

[Source: MDN Docs](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes/aria-live)

#### Q62. Review the CSS below. What color would you expect the background color of the element with a class of .box to be?

```css
.box {
  background-color: blue;
  background: url(images/star.png?raw=png) no-repeat left top;
}
```

- [ ] black
- [ ] blue
- [x] transparent
- [ ] white

#### Q63. Which CSS property and value would correctly remove the bullets from a list item?

- [ ] `list-tem: none`
- [ ] `bullets: hidden`
- [x] `list-style-type: none`
- [ ] `list-bullet: none`

#### Q64. Which code example would center `.box` inside `.container`?

```html
<div class="container">
  <div class="box">what a lovely box, very centered</div>
</div>
```

- [ ] A

```css
.container {
  display: flex;
  align-items: center;
}
```

- [x] B

```css
.container {
  display: flex;
  align-items: center;
  justify-content: center;
}
```

- [ ] C

```css
.box {
  align-items: center;
  justify-content: center;
}
```

- [ ] D

```css
.container {
  display: flex;
  align: center;
}
```

#### Q65. CSS Logical Properties and Values now have wide-ranging support in browsers. If you wanted to use the logical version of `width`, which property name would you choose?

- [ ] `block-width`
- [x] `inline-size`
- [ ] `inline-width`
- [ ] `block-size`

[Source: MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Logical_Properties/Sizing)

#### Q66. Which color value will create a background color that is semitransparent?

- [ ] `rgb(18, 138, 125)`
- [ ] `#128a7d`
- [x] `rgba(18, 138, 125,.5)`
- [ ] `hsl(174, 77%, 31%)`

#### Q67. In a grid layout, which property will create gaps between the rows in the grid?

- [x] `row-gap`
- [ ] `rowgap`
- [ ] `gutter`
- [ ] `row-gutter`

#### Q68. You are creating a responsive design, but when you view your site on a smaller screen, you notice that images are causing a horizontal scroll bar. How can you solve this problem without stretching any images out of shape?

- [ ] Set `object-fit: contain` on the images.
- [x] Set `max-width: 100%` on the images.
- [ ] Set `width: 100%` on the images.
- [ ] Set `resize: true` on the images.

#### Q69. The CSS box model describes how different parts of a box are calculated. Under the standard box model, what is the total width of the content box plus padding (excluding border and margin) in the following CSS?

```css
box {
  width: 200px;
  padding: 10px;
  margin: 0 15px;
  border: 2px solid black;
}
```

- [ ] 230px
- [x] 220px (200px content + 20px padding)
- [ ] 200px
- [ ] 260px

Note: In the standard box model (box-sizing: content-box), the width property defines the content width. The total width of the visible box is the sum of content width (200px) + left and right padding (2 × 10px = 20px) = 220px. Margin and border are not included in this calculation since the question specifically asks for content + padding.

#### Q70. How would you round the value 11.354 to the nearest full integer?

- [ ] round(11.354);
- [x] Math.round(11.354);
- [ ] Math.rnd(11.354);
- [ ] Maths.round(11.354);

#### Q70. What is the JavaScript compiler Babel used for?

- [x] converts ECMAScript 2015+ code into backward compatible version of JS to support older browsers
- [ ] used to bundle individual JS files for use in your website
- [ ] convert older JS code into modern ECMAScript 2015+ code
- [ ] it is a SSR library that can enhance SEO and accessibility of your site

#### Q71. What is the correct way to link to an external stylesheet from the head of an HTML document?

- [x] `<link rel="stylesheet" href="styles.css">`
- [ ] `<script type="text/css" href="styles.css"></script>`
- [ ] `<script type="text/css" src="styles.css">`
- [ ] `<link rel="css" href="styles.css">`

#### Q72. Which href attribute creates a link to the telephone number 1-(704) 555-1151?

- [x] href = "tel:+17045551151"
- [ ] href="17045551151"
- [ ] href="phone:+1704551151"
- [ ] href="call:+17045551151"

#### Q73. In the color value hsl(38, 90%, 60%), what does 38 represent?

- [x] the tint of the color matching 38 degrade on the color wheel
- [ ] the opacity of the color indicating 38% of fully opacity
- [ ] the brightness of the color matching a brightness of 38%
- [ ] the intensity of the color matching an intensity of 38%

[Source: W3 Schools](<[https://www.w3schools.com/accessibility/accessibility_skip_links.php](https://www.w3schools.com/colors/colors_hsl.asp)>)

#### Q74. What is a skiplink?

- [ ] a replacement for inaccessible navigation
- [ ] a method of allowing a screen-reader user to skip between headings
- [x] a link placed early in the <body> to allow the user to skip to the main content
- [ ] a link to allow users to skip video that automatically plays on a website

[Source: W3 Schools](https://www.w3schools.com/accessibility/accessibility_skip_links.php)

#### Q75. On a page with many images, what would be the effect of adding loading="lazy" to the <img> tag?

- [ ] It will speed up the loading of the image when used with a JavaScript library
- [ ] In supporting browsers, images will be highly compressed, therefore loading more quickly
- [x] In supporting browsers, images will load only when they are in or near the visible viewport
- [ ] In supporting browsers, images will not load unless the user explicitly requests image loading

#### Q76. What is GraphQL?

- [ ] a React library for storing data
- [ ] a Vue.js library for storing and manipulating data
- [x] a query language for fetching data from APIs
- [ ] a new database format designed to replace MySQL

[Source: GraphQL official website](https://graphql.org/)

#### Q77. Which choice will place a multiline text input field on the page?

- [ ] `<multiline></multiline>`
- [x] `<textarea></textarea>`
- [ ] `<input type="multiline">`
- [ ] `<input type="textarea">`

#### Q78. Which browser is not based on Chromium?

- [x] Firefox
- [ ] Opera
- [ ] Chrome
- [ ] Edge

#### Q79. In supporting browsers, what would be the effect of using font-display: swap, as in the example?

```css
@font-face {
  font-family: Helvetica;
  font-display: swap;
}
```

- [ ] The browser will show no content until the web font loads.
- [ ] The browser will ignore the web font.
- [ ] The browser will ignore the web font in a situation where the user has indicated they are saving data.
- [x] The browser will load a system font while waiting for the web font to load.

#### Q80. What does the term "code splitting" mean with regard to JavasScript performance?

- [ ] allowing the browser to ignore code that it believes will perform badly
- [x] splitting code into various bundles so that decisions can be made on loading priority
- [ ] removing unused code from JavaScript files
- [ ] only using code that is supported by the newest browsers, and serving the site without JavaScript to old browsers

#### Q81. The vertical-align property works only on certain elements, or on those that have a certain CSS applied. Which element by default will allow vertical-align to be used?

- [ ] div
- [x] td
- [ ] figure
- [ ] p

#### Q82. Which attribute is used to add text to an image that will be displayed if the image does not load and read out to screen reader users?

- [ ] title
- [ ] data
- [ ] src
- [x] alt

#### Q83.Which pseudo-class allows you to selectively show a focus ring on elements only if keyboard navigation is detected?

- [ ] focus-show
- [x] :focus-visible
- [ ] :focus-ring
- [ ] focus-keyboard

[Reference](https://www.freecodecamp.org/news/focus-rings-for-keyboard-interactions-only/)

#### Q84. To create a collection of radio buttons associated with the same field, each <input> tag must \_\_\_\_.

- [ ] have the same value as the id attribute
- [x] have the same value of the name attribute
- [ ] belong to the same field set
- [ ] have the same value as the class attribute

#### Q85. Which statement about HTML syntax is _false_?

- [x] The value of a class attribute should be unique in an HTML document.
- [ ] The `<img>` element does not have a closing `</img>` tag.
- [ ] The `<h1>` element is the most important heading on the page.
- [ ] The value of an id attribute should be unique in an HTML document.

#### Q86. Which command has no Syntax error in CSS?

- [ ] `p {font-size: 16em;}`
- [ ] `h2 {colour: yellow;}`
- [ ] `div {border-radius: 5px}`
- [x] `#my-div {background-color: blue;}`

#### Q87. What type of CSS is the following snippet?

```
<h1 style="color:blue;">
  A Blue Heading
</h1>
```

- [x] Inline
- [ ] Internal
- [ ] External
- [ ] None of the above

#### Q88. How would you set the value of a property—in this example,—back to the default value, as listed in the specification?

- [x] color: initial
- [ ] color: default
- [ ] color: reset
- [ ] color: inherit

[Reference: W3 Schools](https://www.w3schools.com/cssref/css_initial.php#:~:text=The%20initial%20keyword%20is%20used,property%20to%20its%20default%20value.)

#### Q89. What are the four core principles of web accessibility according to WCAG (Web Content Accessibility Guidelines)?

- [ ] Perceivable, Operational, Universal, Responsive
- [x] Perceivable, Operable, Understandable, Robust
- [ ] Practical, Operable, Usable, Reliable
- [ ] Portable, Organized, Understandable, Responsive

[Reference: WCAG 2 Overview](https://www.w3.org/WAI/WCAG21/Understanding/intro#understanding-the-four-principles-of-accessibility)

#### Q90. Which element creates an ordered list, shown with numbers in the browser by default?

- [x] `<ol>`
- [ ] `<li>`
- [ ] `<ul>`
- [ ] `<list>`

[Reference: MDN Web Docs - ol element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ol)

#### Q91. Which choice is not a valid value for the contain property?

- [ ] content
- [ ] all
- [ ] layout
- [x] all

[Reference: MDN Web Docs - contain property](https://developer.mozilla.org/en-US/docs/Web/CSS/contain)

#### Q92. What is the default value of the display property of a `<div>` element in CSS?

- [ ] inline
- [x] block
- [ ] inline-block
- [ ] flex

[Reference: MDN Web Docs - div element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/div)
