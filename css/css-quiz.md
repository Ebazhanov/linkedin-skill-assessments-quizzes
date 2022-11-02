## CSS

#### Q1. Among these selectors which selector has the highest specificity ranking for selecting the anchor link element?

```css
ul li a
a
.example a
div a
```

- [x] `.example a`
- [ ] `div a`
- [ ] `a`
- [ ] `ul li a`

#### Q2. Using an attribute selector, how would you select an `<a>` element with a "title" attribute?

- [x] `a[title]{...}`
- [ ] `a > title {...}`
- [ ] `a.title {...}`
- [ ] `a=title {...}`

**Note:** an alternative to the question below.

#### Q3. What is the CSS selector for an `<a>` tag containing the title attribute?

- [x] `a[title]`
- [ ] `a > title`
- [ ] `a=title`
- [ ] `a.title`

**Note:** an alternative to the question above.

#### Q4. CSS grid and flexbox are now becoming a more popular way to create page layouts. However, floats are still commonly used, especially when working with an older code base, or if you need to support older browser version. What are two valid techniques used to clear floats?

- [ ] Use the "clearfix hack" on the floated element and add a float to the parent element.
- [ ] Use the overflow property on the floated element or the "clearfix hack" on either the floated or parent element.
- [ ] Use the "clearfix hack" on the floated element or the overflow property on the parent element.
- [x] Use the "clearfix hack" on the parent element or use the overflow property with a value other than "visible."

#### Q5. What element(s) do the following selectors match to?

```css
1) .nav {
  ...;
}
2) nav {
  ...;
}
3) #nav {
  ...;
}
```

- [ ] A

```
  1. An element with an ID of "nav"
  2. A nav element
  3. An element with a class of "nav"
```

- [ ] B `They all target the same nav element.`
- [x] C

```
  1. An element with an class of "nav"
  2. A nav element
  3. An element with a id of "nav"
```

- [ ] D

```
  1. An element with an class of "nav"
  2. A nav element
  3. An div with a id of "nav"
```

#### Q6. When adding transparency styles, what is the difference between using the opacity property versus the background property with an `rgba()` value?

- [ ] Opacity specifies the level of transparency of the child elements. Background with an `rgba()` value applies transparency to the background color only.
- [ ] Opacity applies transparency to the background color only. Background with an `rgba()` value specifies the level of transparency of an element, as a whole, including its content.
- [x] Opacity specifies the level of transparency of an element, including its content. Background with an `rgba()` value applies transparency to the background color only.
- [ ] Opacity applies transparency to the parent and child elements. Background with an `rgba()` value specifies the level of transparency of the parent element only.

#### Q7. What is true of block and inline elements? (_Alternative_: Which statement about block and inline elements is true?)

- [ ] By default, block elements are the same height and width as the content container between their tags; inline elements span the entire width of its container.
- [x] By default, block elements span the entire width of its container; inline elements are the same height and width as the content contained between their tags.
- [ ] A `<nav>` element is an example of an inline element. `<header>` is an example of a block element.
- [ ] A `<span>` is an example of a block element. `<div>` is an example of an inline element.

#### Q8. CSS grid introduced a new length unit, fr, to create flexible grid tracks. Referring to the code sample below, what will the widths of the three columns be?

```css
.grid {
  display: grid;
  width: 500px;
  grid-template-columns: 50px 1fr 2fr;
}
```

- [ ] The first column will have a width of 50px. The second column will be 50px wide and the third column will be 100px wide.
- [x] The first column will have a width of 50px. The second column will be 150px wide and the third column will be 300px wide.
- [ ] The first column will have a width of 50px. The second column will be 300px wide and the third column will be 150px wide.
- [ ] The first column will have a width of 50px. The second column will be 500px wide and the third column will be 1000px wide.

**Note:**an alternative to the question below.`

#### Q9. If the width of the container is 500 pixels, what would the width of the three columns be in this layout?

`.grid { display: grid; grid-template-columns: 50px 1fr 2fr; }`

- [x] 50px, 150px, 300px
- [ ] 50px, 200px, 300px
- [ ] 50px, 100px, 200px
- [ ] 50px, 50px, 100px

**Note:**an alternative to the question above.`

#### Q10. What is the line-height property primarily used for?

- [x] to control the height of the space between two lines of content
- [ ] to control the height of the space between heading elements
- [ ] to control the height of the character size
- [ ] to control the width of the space between characters

#### Q11. Three of these choices are true about class selectors. Which is NOT true?

- [ ] Multiple classes can be used within the same element.
- [ ] The same class can be used multiple times per page.
- [ ] Class selectors begin with a leading period
- [x] Classes can be used multiple times per page but not within the same element.

**Note:**an alternative to the question below.`

#### Q12. What is not true about class selectors?

- [x] Only one class value can be assigned to an element.
- [ ] An element can have multiple class value.
- [ ] Class selectors are marked with a leading period.
- [ ] More than one element can have the same class value.

**Note:**an alternative to the question above.`

#### Q13. There are many properties that can be used to align elements and create page layouts such as float, position, flexbox and grid. Of these four properties, which one should be used to align a global navigation bar which stays fixed at the top of the page?

- [x] position
- [ ] flexbox
- [ ] grid
- [ ] float

#### Q14. In the shorthand example below, which individual background properties are represented?

```css
background: blue url(image.jpg) no-repeat scroll 0px 0px;
```

- [x] A
```css
  background-color: blue;
  background-image: url(image.jpg);
  background-repeat: no-repeat;
  background-attachment: scroll;
  background-position: 0px 0px;
```
- [ ] B
```css
  background-color: blue;
  background-img: url(image.jpg);
  background-position: no-repeat;
  background-scroll: scroll;
  background-size: 0px 0px;
```
- [ ] C
```css
  background-color: blue;
  background-src: url(image.jpg);
  background-repeat: no-repeat;
  background-wrap: scroll;
  background-position: 0px 0px;
```
- [ ] D
```css
  background-color: blue;
  background-src: url(image.jpg);
  background-repeat: no-repeat;
  background-scroll: scroll;
  background-position: 0px 0px;
```

#### Q15. In this example, according to cascading and specificity rules, what color will the link be?

```css
.example {
  color: yellow;
}
ul li a {
  color: blue;
}
ul a {
  color: green;
}
a {
  color: red;
}
```

```html
<ul>
  <li><a href="#" class="example">link</a></li>
  <li>list item</li>
  <li>list item</li>
</ul>
```

- [ ] green
- [x] yellow
- [ ] blue
- [ ] red

#### Q16. When elements overlap, they are ordered on the z-axis (i.e., which element covers another). The z-index property can be used to specify the z-order of overlapping elements. Which set of statements about the z-index property are true?

- [x] Larger z-index values appear on top of elements with a lower z-index value. Negative and positive numbers can be used. z-index can only be used on positioned elements.
- [ ] Smaller z-index values appear on top of elements with a larger z-index value. Negative and positive numbers can be used. z-index must also be used with positioned elements.
- [ ] Larger z-index values appear on top of elements with a lower z-index value. Only positive numbers can be used. z-index must also be used with positioned elements.
- [ ] Smaller z-index values appear on top of elements with a larger z-index value. Negative and positive numbers can be used. z-index can be used with or without positioned elements.

**Note:**an alternative to the question below.`

#### Q17. When elements within a container overlap, the z-index property can be used to indicate how those items are stacked on top of each other. Which set of statements is true?

- [x] A
```
  1. Larger z-index values appear on top elements with a lower z-index value.
  2. Negative and positive number can be used.
  3. z-index can be used only on positioned elements.
```
- [ ] B
```
  1. Smaller z-index values appear on top of elements with a larger z-index value.
  2. Negative and positive numbers can be used.
  3. z-index can be used with or without positioned elements.
```
- [ ] C
```
  1. Smaller z-index values appear on top of elements with a larger z-index value.
  2. Negative and positive number can be used.
  3. z-index must also be used with positioned elements.
```
- [ ] D
```
  1. Larger z-index values appear on top of elements with a lower z-index value.
  2. Only positive number can be used.
  3. z-index must also be used with positioned elements.
```

**Note:**an alternative to the question above.`

#### Q18. What is the difference between the following line-height settings?

```css
line-height: 20px;
line-height: 2;
```

- [x] The value of 20px will set the line-height to 20px. The value of 2 will set the line-height to twice the size of the corresponding font-size value.
- [ ] The value of 20px will set the line-height to 20px. The value of 2 is not valid.
- [ ] The value of 20px will set the line-height to 20px. The value of 2 will default to a value of 2px.
- [ ] The value of 20px will set the line-height to 20px. The value of 2 will set the line-height to 20% of the corresponding font-size value.

#### Q19. In the following example, what color will paragraph one and paragraph two be? (_Alternative_: In this example, what color will paragraphs one and two be?)

```html
<section>
  <p>paragraph one</p>
</section>

<p>paragraph two</p>
```

```css
section p {
  color: red;
}
section + p {
  color: blue;
}
```

- [ ] Paragraph one will be blue, paragraph two will be red.
- [ ] Both paragraphs will be blue.
- [x] Paragraphs one will be red, paragraph two will be blue.
- [ ] Both paragraphs will be red.

#### Q20. What are three valid ways of adding CSS to an HTML page?

- [ ] A
```
  1. External; CSS is written in a separate file.
  2. Inline; CSS is added to the <head> of the HTML page.
  3. Internal; CSS is included within the HTML tags.
```
- [ ] B
```
  1. External; CSS is written in a separate file and is linked within the <header> element of the HTML file.
  2. Inline; CSS is added to the HTML tag.
  3. Internal; CSS is included within the <header> element of the HTML file.
```
- [ ] C
```
  1. External; CSS is written in a separate file and is linked within the <head> element of the HTML file.
  2. Internal; CSS is included within the <header> element of the HTML file.
  3. Inline; CSS is added to the HTML tag.
```
- [x] D
```
  1. External; CSS is written in a separate file and is linked within the <head> element of the HTML file.
  2. Inline; CSS is added to the HTML tag.
  3. Internal; CSS is included within the <head> element of the HTML file.
```

#### Q21. Which of the following is true of the SVG image format? (_Alternative_: Which statement about the SVG image format is true?)

- [ ] CSS can be applied to SVGs but JavaScript cannot be.
- [ ] SVGs work best for creating 3D graphics.
- [x] SVGs can be created as a vector graphic or coded using SVG specific elements such as &#x3C;svg&#x3E;, &#x3C;line&#x3E;, and &#x3C;ellipse&#x3E;.
- [ ] SVGs are a HAML-based markup language for creating vector graphics.

#### Q22. In the example below, when will the color pink be applied to the anchor element?

```css
a:active {
  color: pink;
}
```

- [ ] The color of the link will display as pink after its been clicked or if the mouse is hovering over the link.
- [ ] The color of the link will display as pink on mouse hover.
- [x] The color of the link will display as pink while the link is being clicked but before the mouse click is released.
- [ ] The color of the link will display as pink before it has been clicked.

#### Q23. To change the color of an SVG using CSS, which property is used?

- [ ] Use background-fill to set the color inside the object and stroke or border to set the color of the border.
- [ ] The color cannot be changed with CSS.
- [ ] Use fill or background to set the color inside the object and stroke to set the color of the border.
- [x] Use fill to set the color inside the object and stroke to set the color of the border.

#### Q24. When using position: fixed, what will the element always be positioned relative to?

- [ ] the closest element with position: relative
- [x] the viewport
- [ ] the parent element
- [ ] the wrapper element

#### Q25. By default, a background image will repeat \_

- [ ] only if the background-repeat property is set to repeat
- [x] indefinitely, vertically, and horizontally
- [ ] indefinitely on the horizontal axis only
- [ ] once, on the x and y axis

#### Q26. When using media queries, media types are used to target a device category. Which choice lists current valid media types?

- [ ] print, screen, aural
- [ ] print, screen, television
- [x] print, screen, speech
- [ ] print, speech, device

#### Q27. How would you make the first letter of every paragraph on the page red?

- [x] p::first-letter { color: red; }
- [ ] p:first-letter { color: red; }
- [ ] first-letter::p { color: red; }
- [ ] first-letter:p { color: red; }

#### Q28. In this example, what is the selector, property, and value?

```css
p {
  color: #000000;
}
```

- [ ] A
```
  "p" is the selector
  "#000000" is the property
  "color" is the value
```
- [x] B

```
  "p" is the selector
  "color" is the property
  "#000000" is the value
```
- [ ] C
```
  "color" is the selector
  "#000000" is the property
  "#p" is the value
```
- [ ] D
```
  "color" is the selector
  "p" is the property
  "#000000" is the value
```

#### Q29. What is the rem unit based on?

- [ ] The rem unit is relative to the font-size of the p element.
- [ ] You have to set the value for the rem unit by writing a declaration such as rem { font-size: 1 Spx; }
- [ ] The rem unit is relative to the font-size of the containing (parent) element.
- [x] The rem unit is relative to the font-size of the root element of the page.

#### Q30. Which choice would give a block element rounded corners?

- [ ] `corner-radius: 10px;`
- [ ] `border-corner: 10px;`
- [ ] `corner-curve: 10px;`
- [x] `border-radius: 10px;`

[Official doc:](https://www.w3schools.com/css/css3_borders.asp)

#### Q31. In the following media query example, what conditions are being targeted?

```css
@media (min-width: 1024px), screen and (orientation: landscape) { … }
```

- [x] The rule will apply to a device that has either a width of 1024px or wider, or is a screen device in landscape mode.
- [ ] The rule will apply to a device that has a width of 1024px or narrower and is a screen device in landscape mode.
- [ ] The rule will apply to a device that has a width of 1024px or wider and is a screen device in landscape mode.
- [ ] The rule will apply to a device that has a width of 1024px or narrower, or is a screen device in landscape mode.

#### Q32. CSS transform properties are used to change the shape and position of the selected objects. The transform-origin property specifies the location of the element's transformation origin. By default, what is the location of the origin?

- [x] the top left corner of the element
- [ ] the center of the element
- [ ] the top right corner of the element
- [ ] the bottom left of the element

#### Q33. Which of the following is not a valid color value? (_Alternative:_ Which choice is not a valid color value?)

- [ ] `color: #000`
- [ ] `color: rgb(0,0,0)`
- [ ] `color: #000000`
- [x] `color: 000000`

#### Q34. What is the vertical gap between the two elements below?

```html
<div style="margin-bottom: 2rem;">Div 1</div>
<div style="margin-top: 2rem;">Div 2</div>
```

- [x] 2rem
- [ ] 32px
- [ ] 64px
- [ ] 4rem

[Reference MDN Webdocs](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Box_Model/Mastering_margin_collapsing)

#### Q35. When using the Flexbox method, what property and value is used to display flex items in a column?

- [x] flex-flow: column; or flex-direction: column
- [ ] flex-flow: column;
- [ ] flex-column: auto;
- [ ] flex-direction: column;

#### Q36. Which type of declaration will take precedence?

- [ ] any declarations in user-agent stylesheets
- [x] important declarations in user stylesheets
- [ ] normal declarations in author stylesheets
- [ ] important declarations in author stylesheets

#### Q37. The flex-direction property is used to specify the direction that flex items are displayed. What are the values used to specify the direction of the items in the following examples?

![quote](https://raw.githubusercontent.com/ram-sah/LinkedIn-Assessments/master/CSS/images/rm-1.png?raw=png)

- [x]
  - Example 1: `flex-direction: row;`
  - Example 2: `flex-direction: row-reverse;`
  - Example 3: `flex-direction: column;`
  - Example 4: `flex-direction: column-reverse;`
- [ ]
  - Example 1: `flex-direction: row-reverse;`
  - Example 2: `flex-direction: row;`
  - Example 3: `flex-direction: column-reverse;`
  - Example 4: `flex-direction: column;`
- [ ]
  - Example 1: `flex-direction: row;`
  - Example 2: `flex-direction: row-reverse;`
  - Example 3: `flex-direction: column;`
  - Example 4: `flex-direction: reverse-column;`
- [ ]
  - Example 1: `flex-direction: column;`
  - Example 2: `flex-direction: column-reverse;`
  - Example 3: `flex-direction: row;`
  - Example 4: `flex-direction: row-reverse;`

#### Q38. There are two sibling combinators that can be used to select elements contained within the same parent element; the general sibling combinator (~) and the adjacent sibling combinator (+). Referring to example below, which elements will the styles be applied to?

```css
h2 ~ p {
  color: blue;
}
h2 + p {
  background: beige;
}
```

```html
<section>
  <p>paragraph 1</p>
  <h2>Heading</h2>
  <p>paragraph 2</p>
  <p>paragraph 3</p>
</section>
```

- [ ] Paragraphs 2 and 3 will be blue. The h2 and paragraph 2 will have a beige background.
- [x] Paragraphs 2, and 3 will be blue, and paragraph 2 will have a beige background.
- [ ] Paragraph 2 will be blue. Paragraphs 2 and 3 will have a beige background.

Note: a variant of the question below.

#### Q39. Which element(s) will be blue?

```css
h2 ~ p {
  color: blue;
}
```

```html
<section>
  <p>P1</p>
  <h2>H2</h2>
  <p>P3</p>
  <p>P4</p>
</section>
```

- [ ] P3
- [ ] P1, P3 and P4
- [x] P3 and P4
- [ ] P1

[Reference](https://www.w3docs.com/snippets/css/what-does-the-css-tilde-selector-mean.html)

#### Q40. When using flexbox, the "justify-content" property can be used to distribute the space between the flex items along the main axis. Which value should be used to evenly distribute the flex items within the container shown below?

![quote](https://raw.githubusercontent.com/ram-sah/LinkedIn-Assessments/master/CSS/images/rm-2.png?raw=png)

- [ ] justify-content: space-around;
- [ ] justify-content: center;
- [ ] justify-content: auto;
- [x] justify-content: space-between;

#### Q41. There are many advantages to using icon fonts. What is one of those advantages?

- [ ] Icon fonts increase accessibility.
- [ ] Icon fonts can be used to replace custom fonts.
- [x] Icon fonts can be styled with typography related properties such as font-size and color.
- [ ] Icon fonts are also web safe fonts.

#### Q42. What is the difference between `display:none` and `visibility:hidden`?

- [ ] Both will hide the element on the page, but display:none has greater browser support. visibility:hidden is a new property and does not have the best browser support
- [ ] display:none hides the elements but maintains the space it previously occupied. visibility:hidden will hide the element from view and remove it from the normal flow of the document
- [x] display:none hides the element from view and removes it from the normal flow of the document. visibility:hidden will hide the element but maintains the space it previously occupied.
- [ ] There is no difference; both will hide the element on the page

#### Q43. What selector and property would you use to scale an element to be 50% smaller on hover?

- [ ] element:hover {scale: 0.5;}
- [x] element:hover {transform: scale(0.5);}
- [ ] element:hover {scale: 50%;}
- [ ] element:hover {transform: scale(50%);}

#### Q44. Which statement regarding icon fonts is true?

- [ ] Icon fonts can be inserted only using JavaScript.
- [ ] Icon fonts are inserted as inline images.
- [ ] Icon fonts require browser extensions.
- [x] Icon fonts can be styled with typography-related properties such as font-size and color.

#### Q45. The values for the font-weight property can be keywords or numbers. For each numbered value below, what is the associated keyword?

```css
font-weight: 400;
font-weight: 700;
```

- [ ] bold; normal
- [x] normal; bold
- [ ] light; normal
- [ ] normal; bolder

#### Q46. Using the :nth-child pseudo class, what would be the most efficient way to style every third item in a list, no matter how many items are present, starting with item 2?

- [ ] A
```css
  li:nth-child(3 + 2n) {
    margin: 0 5 px;
  }
```
- [x] B
```css
  li:nth-child(3n + 2) {
    margin: 0 5 px;
  }
```
- [ ] C
```css
  li:nth-child(2),
  li:nth-child(5),
  li:nth-child(8) {
    margin: 0 5 px;
  }
```
- [ ] D
```css
  li:nth-child(2n + 3) {
    margin: 0 5 px;
  }
```

#### Q47. Which selector would select only internal links within the current page?

- [ ] `a[href="#"] {...}`
- [ ] `a[href~="#"]`
- [x] `a[href^="#"]`
- [ ] `a[href="#"]`

#### Q48. What is the difference between the margin and padding properties?

- [ ] Margin adds space around and inside of an element; padding adds space only inside of an element.
- [x] Margin adds space around an element; padding adds space inside of an element.
- [ ] Margin adds a line around an element, padding adds space inside of an element.
- [ ] Margin adds space inside of an element, padding adds space around an element.

#### Q49. What is not a valid way of declaring a padding value of 10 pixels on the top and bottom, and 0 pixels on the left and right?

- [x] padding: 10px 10px 0px 0px;
- [ ] padding: 10px 0px;
- [ ] padding: 10px 0;
- [ ] padding: 10px 0px 10px 0px;

#### Q50. Is there an error in this code? If so, find the best description of the problem

```css
@font-face {
  font-family: 'Avenir', sans-serif;
  src: url('avenir.woff2') format('woff2'), url('avenir.woff') format('woff');
}
```

- [ ] The font file formats are not supported in modern browsers.
- [ ] The src attribute requires a comma between the URL and format values.
- [ ] There are no errors in the example.
- [x] The sans-serif inclusion is problematic.

#### Q51. Which style places an element at a fixed location within its container?

- [x] position: absolute;
- [ ] display: flex;
- [ ] display: block;
- [ ] float: left;

#### Q52. The calc() CSS function is often used for calculating relative values. In the example below, what is the specified margin-left value?

```css
.example {
  margin-left: calc(5% + 5px);
}
```

- [x] The left margin value is equal to 5% of its parents element's width plus 5px
- [ ] The left margin value is equal to 5% of the viewport width plus 5px
- [ ] The left margin value is equal to 5% of the closest positioned element's width plus 5px
- [ ] The left margin value is equal to 5% of the selected element's width (.example) plus 5px

#### Q53. Which code would you use to absolutely position an element of the logo class?

- [x] `.logo { position: absolute; left: 100px; top: 150px; }`
- [ ] `.logo { position: absolute; margin-left: 100px; margin-top: 150px; }`
- [ ] `.logo { position: absolute; padding-left: 100px; padding-top: 150px; }`
- [ ] `.logo { position: absolute; left-padding: 100px; top-padding: 150px; }`

#### Q54. In this example, what color will Paragraph 1 be?

```css
p:first-of-type {
  color: red;
}
p {
  color: blue;
}
.container {
  color: yellow;
}
p:first-child {
  color: green;
}
```

```html
<div class="container">
  <h1>Heading</h1>
  <p>Paragraph1</p>
  <p>Paragraph2</p>
</div>
```

- [ ] blue
- [ ] green
- [x] red
- [ ] yellow

#### Q55. What is the `::placeholder pseudo-element` used for?

- [x] It is used to format the appearance of placeholder text within a form control.
- [ ] It specifies the default input text for a form control.
- [ ] It writes text content into a hyperlink tooltip.
- [ ] It writes text content into any page element.

#### Q56. Which statement is true of the single colon (`:`) or double colon (`::`) notations for pseudo-elements-for example, `::before` and `:before`?

- [ ] All browsers support single and double colons for new and older pseudo-elements. So you can use either but it is convention to use single colons for consistency.
- [ ] In CSS3, the double colon notation (`::`) was introduced to create a consistency between pseudo-elements from pseudo-classes. For newer browsers, use the double colon notation. For IE8 and below, using single colon notation (`:`).
- [ ] Only the new CSS3 pseudo-elements require the double colon notation while the CSS2 pseudo-elements do not.
- [x] In CSS3, the double colon notation (`::`) was introduced to differentiate pseudo-elements from pseudo-classes. However, modern browsers support both formats. Older browsers such as IE8 and below do not.

#### Q57. Which choice is not valid value for the font-style property?

- [ ] normal
- [ ] italic
- [x] none
- [ ] oblique

#### Q58. When would you use the @font-face method?

- [ ] to set the font size of the text
- [x] to load custom fonts into stylesheet
- [ ] to change the name of the font declared in the font-family
- [ ] to set the color of the text

#### Q59. You have a large image that needs to fit into a 400 x 200 pixel area. What should you resize the image to if your users are using Retina displays?

- [ ] 2000 x 1400 pixels
- [ ] 200 x 100 pixels
- [x] 800 x 400 pixels
- [ ] 400 x 200 pixels

#### Q60. In Chrome's Developer Tools view, where are the default styles listed?

- [x] under the User Agent Stylesheet section on the right
- [ ] in the third panel under the Layout tab
- [ ] under the HTML view on the left
- [ ] in the middle panel

#### Q61. While HTML controls document structure, CSS controls `___`.

- [ ] semantic meaning
- [ ] content meaning
- [ ] document structure
- [x] content appearance

#### Q62. What is the recommended name you should give the folder that holds your project's images?

- [x] images
- [ ] #images
- [ ] Images
- [ ] my images

#### Q63. What is an advantage of using inline CSS?

- [ ] It is easier to manage.
- [x] It is easier to add multiple styles through it.
- [ ] It can be used to quickly test local CSS overrides.
- [ ] It reduces conflict with other CSS definition methods.

#### Q64. Which W3C status code represents a CSS specification that is fully implemented by modern browsers?

- [ ] Proposed Recommendation
- [ ] Working Draft
- [x] Recommendation
- [ ] Candidate Recommendation

#### Q65. Are any of the following declarations invalid?

```css
color: red; /* declaration A */
font-size: 1em; /* declaration B */
padding: 10px 0; /* declaration C */
```

- [ ] Declaration A is invalid.
- [ ] Declaration B is invalid.
- [ ] Declaration C is invalid.
- [x] All declarations are valid.

#### Q66. Which CSS will cause your links to have a solid blue background that changes to semitransparent on hover?

- [x] A

```css
  a:link {
    background: #0000ff;
  }
  a:hover {
    background: rgba(0, 0, 255, 0.5);
  }
```
- [ ] B

```css
  a {
    color: blue;
  }
  a:hover {
    background: white;
  }
```
- [ ] C

```css
  a:link {
    background: blue;
  }
  a:hover {
    color: rgba(0, 0, 255, 0.5);
  }
```
- [ ] D

```css
  a:hover {
    background: rgba(blue, 50%);
  }
  a:link {
    background: rgba(blue);
  }
```

#### Q67. Which CSS rule takes precedence over the others listed?

- [ ] `div.sidebar {}`
- [ ] `* {}`
- [x] `div#sidebar2 p {}`
- [ ] `.sidebar p {}`

#### Q68. The body of your page includes some HTML sections. How will it look with the following CSS applied?

```css
body {
  background: #ffffff; /* white */
}
section {
  background: #0000ff; /* blue */
  height: 200px;
}
```

- [x] blue sections on a white background
- [ ] Yellow sections on a blue background
- [ ] Green sections on a white background
- [ ] blue sections on a red background

#### Q69. Which CSS keyword can you use to override standard source order and specificity rules?

- [ ] `!elevate!`
- [ ] `*prime`
- [ ] `override`
- [x] `!important`

#### Q70. You can use the `___` pseudo-class to set a different color on a link if it was clicked on.

- [x] `a:visited`
- [ ] `a:hover`
- [ ] `a:link`
- [ ] `a:focus`

#### Q71. Which color will look the brightest on your screen, assuming the background is white?

- [ ] `background-color: #aaa;`
- [ ] `background-color: #999999;`
- [ ] `background-color: rgba(170,170,170,0.5);`
- [x] `background-color: rgba(170,170,170,0.2);`

#### Q72. Which CSS selector can you use to select all elements on your page associated with the two classes header and clear?

- [ ] `."header clear" {}`
- [ ] `header#clear {}`
- [x] `.header.clear {}`
- [ ] `.header clear {}`

#### Q73. A universal selector is specified using a(n) `___`.

- [ ] "h1" string
- [ ] "a" character
- [ ] "p" character
- [x] "\*" character

#### Q74. In the following CSS code, `'h1'` is the `___`, while `'color'` is the `___`.

```css
h1 {
  color: red;
}
```

- [ ] property; declaration
- [ ] declaration; rule
- [ ] "p" character
- [x] selector; property

#### Q75. What is an alternate way to define the following CSS rule?

```css
font-weight: bold;
```

- [ ] font-weight: 400;
- [ ] font-weight: medium;
- [x] font-weight: 700;
- [ ] font-weight: Black;

#### Q76. You want your styling to be based on a font stack consisting of three fonts. Where should the generic font for your font family be specified?

- [ ] It should be the first one on the list.
- [ ] Generic fonts are discouraged from this list.
- [x] It should be the last one on the list.
- [ ] It should be the second one on the list.

#### Q77. When using a font stack to declare the font family, in what order should the values appear?

- [x] The first value is the first choice, followed by alternative options, ordered by preference. The last option should be a generic font.
- [ ] The first value is the first choice. The order of the alternative options does not matter. It depends on what is available on the user's computer.
- [ ] The first value is the first choice, and must be followed by at least one alternative option before adding the generic font.
- [ ] The first value is the first choice, followed by a maximum of three alternatives.

#### Q78. What is one disadvantage of using a web font service?

- [ ] It requires you to host font files on your own server.
- [ ] It uses more of your site's bandwidth.
- [ ] It offers a narrow selection of custom fonts.
- [x] It is not always a free service.

#### Q79. How do you add Google fonts to your project?

- [x] by using an HTML link element referring to a Google-provided CSS
- [ ] by embedding the font file directly into the project's master JavaScript
- [ ] by using a Google-specific CSS syntax that directly links to the desired font file
- [ ] by using a standard font-face CSS definition sourcing a font file on Google's servers

#### Q80. Using the following HTML and CSS example, what will equivalent pixel value be for .em and .rem elements?

```css
html {
  font-size: 10px;
}
body {
  font-size: 2rem;
}
.rem {
  font-size: 1.5rem;
}
.em {
  font-size: 2em;
}
```

```html
<body>
  <p class="rem"></p>
  <p class="em"></p>
</body>
```

- [ ] The .rem will be equivalent to 25px; the .em value will be 20px.
- [ ] The .rem will be equivalent to 15px; the .em value will be 20px.
- [x] The .rem will be equivalent to 15px; the .em value will be 40px.
- [ ] The .rem will be equivalent to 20px; the .em value will be 40px.

#### Q81. What property is used to adjust the space between text characters?

- [ ] `font-style`
- [ ] `text-transform`
- [ ] `font-variant`
- [x] `letter-spacing`

#### Q82. What is the correct syntax for changing the cursor from an arrow to a pointing hand when it interacts with a named element?

- [x] `.element {cursor: pointer;}`
- [ ] `.element {cursor: hand;}`
- [ ] `.element {cursor: move-hand;}`
- [ ] `.element {cursor: pointer-hand;}`

#### Q83. What is the effect of this style?

```css
background-position: 10% 50%;
```

- [x] The background image is placed 10% from the left and 50% from the top of its container
- [ ] The background image is placed 10% from the bottom and 50% from the left of its container
- [ ] The background image is placed 10% from the right and 50% from the bottom of its container
- [ ] The background image is placed 10% from the top and 50% from the left of its container

#### Q84. How will the grid items display?

```css
grid-template-columns: 2fr 1fr;
```

- [ ] The first column will be twice the height of the second column, and will be as wide as the content.
- [ ] The first column will be half the size of the container, and the second column will absorb the remaining space.
- [x] The first column will be twice as wide as the second column, and will fit proportionally within the grid container.
- [ ] The first column will be twice the width and height of the second column, and will fit proportionally within the grid container.

#### Q85. Which style rule would make the image 50% smaller during a hover?

```html
<img id="photo" alt="" src="..." />
```

- [ ] img#photo:hover {scale: 0.5;}
- [x] img#photo:hover {transform: scale(0.5);}
- [ ] img#photo {hover-scale: 0.5;}
- [ ] img#photo:hover {size: smaller;}

#### Q86. Which CSS properties can you use to create a rounded corner on just the top-left and top-right corners of an element?

```css
A. border-radius: 10px 10px 0 0;
B. border-top-left-radius: 10px; and border-top-right-radius: 10px;
C. border-radius: 10px 0;
D. border-top-radius: 10px;
```

- [ ] A and C
- [ ] C and D
- [ ] B and C
- [x] A and B

#### Q87. Review the HTML example below. Then choose the list of selectors that select the \<p>, from lowest to highest specificity.

```html
<section>
  <p class="example">...</p>
</section>
```

- [ ] A
```css
  1. section \* {
    ...;
  }
  2. [class*='example'] {
    ...;
  }
  3. p.example {
    ...;
  }
  4. section p {
    ...;
  }
```
- [ ] B
```css
  1. p {
    ...;
  }
  2. p.example {
    ...;
  }
  3. section p {
    ...;
  }
  4. [class*='example'] {
    ...;
  }
```
- [ ] C
```css
  1. p.example {
    ...;
  }
  2. section p {
    ...;
  }
  3. [class*='example'] {
    ...;
  }
  4. section \* {
    ...;
  }
```
- [x] D
```css
  1. p {
    ...;
  }
  2. section p {
    ...;
  }
  3. [class*='example'] {
    ...;
  }
  4. p.example {
    ...;
  }
```

#### Q88. Which property is used to create a drop shadow effect on an HTML element?

- [ ] element-shadow
- [ ] outer-shadow
- [ ] dropbox-shadow
- [x] box-shadow

#### Q89. What is the correct selector for targeting all text inputs that are not disabled?

- [x] `input[type="text"]:not([disabled]) {...}`
- [ ] `input[type="text"]:not("disabled") {...}`
- [ ] `input[type*="text"]:not([disabled="disabled"]) {...}`
- [ ] `input[type="text"]:not([type="disabled"]) {...}`

`input[type="text"]` selects all the input with type text, and `:not([disabled])` selects all the elements not having the attribute "disabled". Combining both only selects all the input elements with type attribte as "text" and not having "disabled" attribute.`

1. [Reference link attribute-selector](https://www.w3schools.com/css/css_attribute_selectors.asp)
2. [Reference link-:not()](https://developer.mozilla.org/en-US/docs/Web/CSS/:not)

#### Q90. How can you create a semi-transparent background color?

- [ ] `background-color: hsl(0, 0, 0, 0.5);`
- [ ] `background-color: rgbx(0, 0, 0, 0.5);`
- [x] `background-color: rgba(0, 0, 0, 0.5);`
- [ ] `background-color: rgba(0, 0, 0, 1);`

`rgba` is a funtion in css. rgba stands for red, green, blue and alpha. The value of alpha can be between 0 and 1 both inclusive with 0 being fully transparent and 1 being fully opaque.

[Reference link-rgba](https://www.w3schools.com/cssref/func_rgba.asp)

#### Q91. Using this HTML markup, how would you select only the headings contained within the `<header>` element?

```html
<header>
  <H1>Heading 1</H1>
  <H2>Heading 2</H2>
</header>
<h2>Heading 2</h2>
```

- [x] `header h1, header h2 {...}`
- [ ] `header h1 + header h2 {...}`
- [ ] `header h1, h2 {...}`
- [ ] `h1, h2 {...}`

#### Q92. Suppose you want to have a list of items (.item) displayed in a row and in reverse order using flexbox. What is the error in the CSS below?

```css
.container {
  display: flex;
}
.item {
  border: 1px solid red;
  flex-direction: row-reverse;
}
```

- [ ] The value for flex-direction should be reverse-row.
- [ ] The .container element should have a property of flex: display.
- [x] The flex-direction property should be declared in the container.
- [ ] The display value should be flex-inline to display the items in a row.

#### Q93. Which choice is not a valid transition?

- [ ] `transition: margin 1000ms ease-in-out;`
- [ ] `transition: color 1.3s ease-in;`
- [x] `transition: position 400ms linear;`
- [ ] `transition: opacity 1s ease-in;`

1. [MDN:](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_animated_properties)
2. [MDM:](https://developer.mozilla.org/en-US/docs/Web/CSS/position#formal_definition)
3. [W3s](https://www.w3schools.com/cssref/pr_class_position.asp)
4. [W3s](https://www.w3schools.com/cssref/css_animatable.asp)

#### Q94. In this example, what color will the paragraphs be and why?

```css
article p {
  color: blue;
}
article > p {
  color: green;
}
```

```html
<article>
  <p>Paragraph 1</p>

  <aside>
    <p>Paragraph 2</p>
  </aside>
</article>
```

- [ ] Paragraph 1 will be blue. Paragraph 2 will be green.
- [ ] Both paragraphs will be green.
- [x] Paragraph 1 will be green. Paragraph 2 will be blue.
- [ ] Both paragraphs will be blue.

#### Q95. Review the declaration of border style shown below. What is the corresponding longhand syntax?

```css
border: 1px solid red;
```

- [ ] A

```css
  border-size: 1px;
  border-style: solid;
  border-color: red;
```
- [ ] B

```css
  border-size: 1px;
  border-type: solid;
  border-color: red;
```
- [x] C

```css
  border-width: 1px;
  border-style: solid;
  border-color: red;
```
- [ ] D

```css
  border-width: 1px;
  border-line: solid;
  border-color: red;
```

#### Q96. Pseudo-classes are used to `_`.

- [x] style the state of the selected element
- [ ] insert presentational content
- [ ] style a specific part of the selected element
- [ ] style the elements using class selectors

#### Q97. In this example, what styles will be applied to which elements?

```css
section {
  color: gray;
}
```

```html
<section>
  <p>paragraph</p>
  <a href="#">link</a>
</section>
```

- [ ] The paragraph and link will be gray.
- [ ] The background color of the section element will be gray.
- [ ] The paragraph will be gray. The link will be the browser default, black.
- [x] Only the paragraph will be gray.

#### Q98. Which answer is an example of a type selector (also sometimes referred to as an element selector)?

- [ ] `.header {...}`
- [x] `header {...}`
- [ ] `#header {...}`
- [ ] `header > h1 {...}`

#### Q99. What is the correct order for listing different link states in a website so those states display correctly on the page?

- [ ] A

```css
  a
  a:hover
```
- [ ] B

```css
  :link
  :visited
  :hover
  :active
  :focus
```
- [ ] C

```css
  :active
  :focus
  :hover
  :link
  :visited
```
- [x] D

```css
  :link
  :visited
  :focus
  :hover
  :active
```

#### Q100. Which selector is used to select the paragraph element that is a direct descendent of section?

- [ ] `section * p`
- [ ] `section + p`
- [ ] `section ~ p`
- [x] `section > p`

[Child combinator](https://developer.mozilla.org/en-US/docs/Web/CSS/Child_combinator)

#### Q101. For this code, what is the font color of the hypertext link?

```css
ul {
  --color: red;
}
p {
  color: var(--color);
}
a {
  color: var(--color, orange);
}
```

```html
<p>Paragraph</p>
<ul>
  <li>
    <a href="#">list item a link </a>
  </li>
  <li>list item</li>
</ul>
```

- [x] red
- [ ] orange
- [ ] blue
- [ ] black

[Reference](https://www.sitepoint.com/how-to-use-variables-in-css/)

#### Q102. Which statement is not true?

- [ ] Specificity determines which CSS rule is applied by the browsers.
- [x] When two selectors apply to the same element, the one with lower specificity wins.
- [ ] The last rule defined overrides all previous rules and even conflicting rules.
- [ ] Rules with more specific selectors have greater specificity.

[Reference](https://www.smashingmagazine.com/2007/07/css-specificity-things-you-should-know/)

#### Q103. What is the output of the margin value when used within this context, assuming that its containing element is larger than 800px?

```css
.example {
  width: 800px;
  margin: 0 auto;
}
```

- [ ] The example element will have 0 margin space around the whole element. The auto value will center align the element horizontally and vertically within its container.
- [ ] The example element will have 0 margin space on the left and right. It will be sized automatically on the top and bottom, which will center align the element within its container.
- [x] The example element will have 0 margin space on the top and bottom. The margin will be sized automatically on the left and right, which may center align the element within its container.
- [ ] The margin value is invalid because its missing a unit measurement after the 0.

[Source: SOW](https://stackoverflow.com/questions/3170772/what-does-auto-do-in-margin-0-auto)

#### Q104. There are currently four viewport-percentage lengths that can be used to define the value relative to the viewport size: vw, vh, vmin, and vmax. If the current viewport size has a width of 800px and a height of 600px, what will these values be equivalent to in pixels?

```css
10vw = ?px
10vh = ?px
10vmin = ?px
10vmax = ?px
```

- [x] 10vw = 80px
      10vh = 60px
      10vmin = 60px
      10vmax = 80px
- [ ] 10vw = 60px
      10vh = 80px
      10vmin = 80px
      10vmax = 60px
- [ ] 10vw = 8px
      10vh = 6px
      10vmin = 6px
      10vmax = 8px
- [ ] 10vw = 6px
      10vh = 8px
      10vmin = 8px
      10vmax = 6px

#### Q105. Referring to the HTML markup and CSS example below, which element(s) will be targeted?

```css
p:first-of-type:first-letter {
  color: red;
}
```

```html
<body>
  <p>Paragraph 1.</p>
  <p>Paragraph 2.</p>

  <article>
    <h1>Heading</h1>
    <p>Paragraph 3.</p>
    <p>paragraph 4.</p>
  </article>

  <section>
    <p>Paragraph 5.</p>
    <p>Paragraph 6.</p>
  </section>
</body>
```

- [ ] The first letter in all paragraphs will be red.
- [ ] Only the first letter in paragraphs 1 and 5 will be red.
- [x] The first letter in paragraphs 1, 3, and 5 will be red.
- [ ] Only the first letter in paragraph 1 will be red.Only

#### Q106. Which five style features are associated with the box model?

- [x] margin, padding, border, width, height
- [ ] width, height, z-index, overflow, font size
- [ ] margin, padding, font size, line height, border
- [ ] font size, line height, letter spacing, width, height

#### Q107. Which choice will not set all links that include domain.com to pink?

- [ ] A

```css
a[href$='domain.com'] {
  color: pink;
}
```

- [x] B

```css
a[href='*domain.com'] {
  color: pink;
}
```

- [ ] C

```css
a[href*='domain.com'] {
  color: rgb(255, 155, 155);
}
```

- [ ] D

```css
a[href*='domain.com'] {
  color: pink;
}
```

[Reference](https://www.smashingmagazine.com/2007/07/css-specificity-things-you-should-know/)

#### Q108. Which property and value pair could be used to apply a linear gradient effect?

- [x] `css background: linear-gradient(#648880, #293f50);`
- [ ] `css background-image: linear(#648880, #293f50);`
- [ ] `css background: gradient(linear, #648880, #293f50);`
- [ ] `css background-color: linear-gradient(#648880, #293f50);`

#### Q109. You want to add a background circle behind an icon. Which style declaration is correct?

- [ ] A

```css
.glyphicon-bgcircle {
  circle-radius: 50%;
  margins: 50px;
  background-color: #fdadc6;
  color: rgba(255, 255, 255, 1);
  font-size: 24px;
}
```

- [ ] B

```css
glyphicon-bgcircle {
  border-circle: 50%;
  padding: 50px;
  background-color: #fdadc6;
  color: rgba(255, 255, 255, 1);
  font-size: 24px;
}
```

- [x] C

```css
.glyphicon-bgcircle {
  border-radius: 50%;
  padding: 50px;
  background-color: #fdadc6;
  color: rgba(255, 255, 255, 1);
  font-size: 24px;
}
```

- [ ] D

```css
.glyphicon-bgcircle {
  radius-rounded: 50%;
  margins: auto;
  background-color: #fdadc6;
  color: rgba(255, 255, 255, 1);
  font-size: 24px;
}
```

#### Q110. Which items are valid values for the font-size property?

```css
A. font-size: xsmall
B. font-size: 50%
C. font-size: 1em
D. font-size: 20px
```

- [ ] C, D
- [x] B, C, D
- [ ] A, C
- [ ] A, B, C, D

#### Q111. In this image, the blue box and sample text are both contained within the same parent element. The blue box is floated on the left margin of the container. Why is it not contained with the container?

![Sample text](https://raw.githubusercontent.com/ram-sah/LinkedIn-Assessments/master/CSS/images/rm-3.png?raw=png)

- [ ] Floating the blue box increased its height.
- [ ] Floating the blue box on the left also moves it down.
- [ ] Floating the blue box actually shifts it to the right and down.
- [x] Floating the blue box took it out of document flow and the container is sized only to the sample text.

#### Q112. Given this code, which CSS declaration of .overlay will span the entire width and height of its container?

```css
<style>
.container {
  position: relative;
  height: 200px;
  width: 200px;
  border: 1px solid black;
}
</style>
<div class="container"><div class="overlay"></div></div>
```

- [ ] A

```css
.overlay {
  position: static;
  top: 200px;
  bottom: 200px;
  right: 200px;
  left: 200px;
  background-color: rgba(0, 0, 0, 0.5);
}
```

- [ ] B

```css
.overlay {
  position: absolute;
  top: 200px;
  bottom: 200px;
  right: 200px;
  left: 200px;
  background-color: rgba(0, 0, 0, 0.5);
}
```

- [ ] C

```css
.overlay {
  position: static;
  top: 0;
  bottom: 0;
  right: 0;
  left: 0;
  background-color: rgba(0, 0, 0, 0.5);
}
```

- [x] D

```css
.overlay {
  position: absolute;
  top: 0;
  bottom: 0;
  right: 0;
  left: 0;
  background-color: rgba(0, 0, 0, 0.5);
}
```

#### Q113. Which missing line of code would place the text on top of the image?

```js
<div class="container">
  <img src="grumpy-cat.gif" />
  <p>The z-index property is cool!</p>
</div>
```

```css
img {
  position: absolute;
  left: 0px;
  top: 0px;
  // Missing line
}
```

- [ ] `z-index: 1;`
- [x] `z-index: -1;`
- [ ] `z-index: 0;`
- [ ] `z-index: true;`

#### Q114. To make the font size of an element one size smaller than the font size of the element's container, which style property would you apply?

- [ ] `font-size: reduce;`
- [ ] `font-size: 8px;`
- [ ] `font-size: -1em;`
- [x] `font-size: smaller;`

#### Q115. Given this markup, which selector would result in the text being highlighted in yellow?

```js
<span class="highlight">#BLM</span>
```

- [x] A

```css
.highlight {
  background-color: yellow;
}
```

- [ ] B

```css
#highlight {
  background-color: yellow;
}
```

- [ ] C

```css
.highlight {
  color: yellow;
}
```

- [ ] D

```css
#highlight {
  color: yellow;
}
```

[Highlight Background](<https://alvarotrigo.com/blog/css-highlight-text/#:~:text=Highlight%20text%20(CSS)%20is%20used,text%20is%20the%20most%20popular>)

#### Q116. To prevent a background image from tiling in any direction, which style property would you apply?

- [x] A

```css
background-repeat: no-repeat;
```

- [ ] B

```css
background-repeat: fixed;
```

- [ ] C

```css
background-repeat: none;
```

- [ ] D

```css
background-tile: none;
```

#### Q117. To rotate an object 30 degrees counterclockwise, which style property would you apply?

- [x] `transform: rotate(-30deg);`
- [ ] `transform: rotate(30deg);`
- [ ] `rotate: 30deg;`
- [ ] `spin: 30deg;`

[Reference](<https://developer.mozilla.org/en-US/docs/Web/CSS/transform-function/rotate()>)

#### Q118. Which style rule would you apply to set the background image to display the contents of the wood.png file?

- [ ] `background-image: file('wood.png');`
- [x] `background-image: url('wood.png');`
- [ ] `background-image: wood.png;`
- [ ] `image: wood.png`

#### Q119. What style rule would set the font color of only paragraph two to blue?

```js
<section><p>paragraph one</p></section><p>paragraph two</p>
```

- [ ] A

```css
section > p {
  color: blue;
}
```

- [ ] B

```css
p {
  color: blue;
}
```

- [x] C

```css
section + p {
  color: blue;
}
```

- [ ] D

```css
p + section {
  color: blue;
}
```

[Reference](https://www.w3schools.com/cssref/sel_element_pluss.asp)

#### Q120. You want to move an element up 100px. Which CSS property would you use?

- [ ] `transform: translateX(-100px)`
- [x] `transform: translateY(-100px)`
- [ ] `transform: translateY(100px)`
- [ ] `transform: translateX(100px)`

#### Q121. Which style will horizontally center the inner &lt;div&gt; within the outer &lt;div&gt;?

```js
<div id="outer">
  <div id="inner">Center Me!</div>
</div>
```

- [ ] A

```css
#inner {
  width: 50%;
}

#outer {
  width: 100%;
}
```

- [ ] B

```css
#inner {
  left: 0;
  right: 0;
  position: center;
}
```

- [ ] C

```css
#inner {
  text-align: center;
}
```

- [x] D

```css
#inner {
  width: 50%;
  margin: 0 auto;
}
```

#### Q122. Which corner will the puppy be in when these CSS rules are applied?

```css
.pen {
  height: 100px;
  width: 100px;
  border: 2px dashed brown;
  position: relative;
}

#puppy {
  position: absolute;
  right: 80px;
  bottom: 0px;
}
```

```html
<div class="pen">
  <span id="puppy">:dog:</span>
</div>
```

- [ ] top-right corner
- [ ] bottom-right corner
- [ ] top-left corner
- [x] bottom-left corner

#### Q123. Which choice uses the correct syntax for adding a hover pseudo class to \<a> element?

- [x] `a:hover {...}`
- [ ] `a :hover {...}`
- [ ] `a.hover {...}`
- [ ] `a hover {...}`

[Reference](https://stackoverflow.com/questions/1935820/set-ahover-based-on-class)

#### Q124. Which missing code will give "Cellar Door" a shadow?

```css
  <style>
    #cellar-door {
      box-shadow: 3px 5px 10px #000;
    }
    .text-shadow {
      text-shadow: 3px 5px 10px #000;
    }
  </style>

  <h1 _____> Cellar Door</h1>
```

- [x] `class="text-shadow"`
- [ ] `id="cellar-door"`
- [ ] `id="text-shadow"`
- [ ] `class="cellar-door"`

[Reference](https://www.w3schools.com/html/html_classes.asp)

#### Q125. Which choice is a valid example of a comment in CSS?

- [ ] `-- This line has been cancelled.`
- [x] `/* This line has been cancelled. */`
- [ ] `// This line has been cancelled.`
- [ ] `# This line has been cancelled.`

[Reference](https://www.w3schools.com/css/css_comments.asp)

#### Q126. Which element(s) will be displayed in blue text?

```css
    h2 ~ p {
      color: blue;
    }
  <section>
    <p>P1</p>
    <h2>H2</h2>
    <p>P3</p>
    <p>P4</p>
  </section>
```

- [ ] P3
- [ ] P1, P3 and P4
- [x] P3 and P4
- [ ] P1

[Reference](https://www.w3docs.com/snippets/css/what-does-the-css-tilde-selector-mean.html)

#### Q127. When these pseudo class selectors are applied to a link, what states will the styles be applied to?

```css
a:visited {
  ...;
}
a:active {
  ...;
}
a:hover {
  ...;
}
a:focus {
  ...;
}
```

- [ ] `:visited` styles are applied after the link has been opened.
      `:active` styles are applied on mouse click and hold.
      `:hover` styles are applied on mouse over or mouse click and hold.
      `:focus` styles are applied when a Tab key on a keyboard is used to navigate through links.
- [ ] `:visited` styles are applied after the link has been opened.
      `:active` styles are applied on mouse click.
      `:hover` styles are applied on mouse over.
      `:focus` styles are applied on mouse click and hold, or when a Tab key on a keyboard is used to navigate through links.
- [x] `:visited` styles are applied after the link has been opened.
      `:active` styles are applied on mouse click only and before mouse release.
      `:hover` styles are applied on mouse over.
      `:focus` styles are applied when a Tab key on a keyboard is used to navigate through links.
- [ ] `:visited` styles are applied on mouse hold.
      `:active` styles are applied when the link has been opened.
      `:hover` styles are applied on mouse over.
      `:focus` styles are applied when a Tab key on a keyboard is used to navigate through links.

[Reference](https://developer.mozilla.org/pt-BR/docs/Web/CSS/Pseudo-classes)

#### Q128. What style rule should you use to display all input elements that have failed the validation test with a red font?

- [ ] A

```css
input.valid[false] {
  color: red;
}
```

- [x] B

```css
input:invalid {
  color: red;
}
```

- [ ] C

```css
input.not(valid) {
  color: red;
}
```

- [ ] D

```css
input.invalid {
  color: red;
}
```

[Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/:invalid)

#### Q129. What style rule should you apply to the img element to display the element in grayscale with no color?

- [ ] A

```css
img {
  transform: grayscale(1);
}
```

- [ ] B

```css
img {
  filter: grayscale(0);
}
```

- [ ] C

```css
img {
  transform: grayscale(0);
}
```

- [x] D

```css
img {
  filter: grayscale(1);
}
```

[Reference](https://www.w3schools.com/cssref/tryit.asp?filename=trycss3_filter_grayscale)

#### Q130. Why might you create a reset style sheet?

- [ ] to reduce page size by removing browser styles from the page rendering.
- [x] to start designing a page style by overriding any built-in browser styles
- [ ] to make it easier to minify the content of your web page design
- [ ] to increase execution time by not relying on built-in browser styles

[Reference](http://web.simmons.edu/~grovesd/comm244/notes/week4/css-reset)

#### Q131. Which option is an invalid way of declaring a padding value of 10 pixels on the top and bottom, and 0 pixels on the left and right?

- [ ] padding: 10px 0px;
- [x] padding: 10px 10px 0px 0px;
- [ ] padding: 10px 0;
- [ ] padding: 10px 0px 10px 0px;

[Reference](https://www.w3schools.com/css/css_padding.asp)

#### Q132. How would you absolutely position an element of the logo class inside of a relatively positioned container?

- [ ] A

```css
.logo {
  position: absolute;
  padding-left: 100px;
  padding-top: 150px;
}
```

- [ ] B

```css
.logo {
  position: absolute;
  left: 100px;
  top: 150px;
}
```

- [ ] C

```css
.logo {
  position: absolute;
  left-padding: 100px;
  top-padding: 150px;
}
```

- [x] D

```css
.logo {
  position: absolute;
  margin-left: 100px;
  margin-top: 150px;
}
```

#### Q133. How would the `<div>` with the class .child be positioned within its container?

```html
<style>
  .container {
    height: 200px;
    width: 200px;
  }
  .child {
    margin: auto 0;
    height: 100px;
  }
</style>
<div class="container">
  <div class="child">...</div>
</div>
```

- [ ] horizontally centered
- [ ] vertically centered, spanning the container's width
- [ ] at the bottom of the container, spanning the container's width
- [x] at the top of the container, spanning the container's width

[Reference](https://codepen.io/harsh1x4/pen/poVaQVz)

#### Q134. By default, a CSS transition is \_\_

- [ ] asymmetric, so that the transition going from the initial state to the end state is different from the transition going from the end state back to the initial state.
- [ ] one sided, so that there is only one transition and it goes from the initial state to the end state.
- [x] symmetric, so that the transition going from the initial state to the end state is the reverse of the transition going from the end state back to the initial state.
- [ ] one-sided, so that there is only one transition and it goes from the end state to the initial state.

[Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Transitions/Using_CSS_transitions)

#### Q135. Which style rule will extend the header element across an entire grid row from the first column through the last column?

- [ ] A

```css
header {
  grid-column: 1 / auto;
}
```

- [x] B

```css
header {
  grid-column: 1/-1;
}
```

- [ ] C

```css
header {
  grid-column: -1/1;
}
```

- [ ] D

```css
header {
  grid-column: 1/100%;
}
```

[Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/grid-column)

#### Q136. To center the content of a grid cell horizontally and vertically within the cell, which style rule should you apply?

- [ ] A

```css
align-items: start;
justify-items: end;
```

- [x] B

```css
align--items: center;
justify-items: center;
```

- [ ] C

```css
align-items: middle;
justify-items: middle;
```

- [ ] D

```css
align-items: stretch;
justify-items: stretch;
```

[Reference for align-items](https://developer.mozilla.org/en-US/docs/Web/CSS/align-items) [Reference for justify-items](https://developer.mozilla.org/en-US/docs/Web/CSS/justify-items)

#### Q137. What style rule should you use to display all input elements that have failed the validation test with a red font?

- [ ] A

```css
input.valid[false] {
  color: red;
}
```

- [x] B

```css
input:invalid {
  color: red;
}
```

- [ ] C

```css
input.not(valid) {
  color: red;
}
```

- [ ] D

```css
input.invalid {
  color: red;
}
```

[Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/:invalid)

#### Q139. To insert an external style sheet file into another style sheet file, which rule should you use?

- [x] `@import`
- [ ] `@link`
- [ ] `@insert`
- [ ] `@style`

[Reference for import](https://developer.mozilla.org/en-US/docs/Web/CSS/@import)

#### Q140. Given this code, how tall will the following element be in pixels?

```html
<style>
  #tall-text {
    display: inline;
    font-size: 20px;
    height: 200px;
  }
</style>

<p id="tall-text">Did I grow?</p>
```

- [ ] 200px
- [x] 20px
- [ ] 180px
- [ ] 220px

[Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/height#:~:text)

#### Q141. Which style rule will place an X within the grid to win the game?

![A](img/Q-141.png?raw=png)

- [ ] row: 3;
      column: 3;
- [x] grid-row: 3;
      grid-column: 3;
- [ ] row: 2;
      column: 2;
- [ ] grid-row: 2;
      grid-column: 2;

[Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/grid-column)

#### Q142. Which CSS property is used to create an image reflection ?

- [x] box-relect
- [ ] img-reflect
- [ ] None of the above
- [ ] reflect-img

#### Q143. What is the general syntax of writing the var() function ?

- [x] var(--name, value)
- [ ] var(--name)
- [ ] var(value)
- [ ] None of the Above

#### Q143. How many layout modes were there before the Flexbox Layout Module was introduced in CSS ?

- [ ] 2
- [ ] 1
- [x] 4
- [ ] 3

#### Q144. Which of the following components of the CSS box model are transparent ?

- [ ] Padding
- [ ] Margin
- [x] Both A and B
- [ ] None

#### Q145. How are custom fonts defined using CSS ?

- [x] @Font-Face Rule
- [ ] Custom font cannot be defined
- [ ] src tags
- [ ] None of the above

#### Q146. Which of the following CSS property sets what kind of line decorations are added to an element, such as underlines, overlines, etc?

- [ ] text-decoration
- [ ] text-style
- [x] text-decoration-line
- [ ] text-line

#### Q147. Which of the following CSS Property sets the stacking order of positioned elements?

- [ ] y-index
- [x] z-index
- [ ] x-index
- [ ] all of the mentioned

#### Q148. Which of the following property allows a marquee to be used in the case of a text-overflow?

- [ ] overflow-marquee
- [x] overflow-style
- [ ] overflow-text
- [ ] none of the mentioned

#### Q149. Which of the following Cascading order has the highest precedence?

- [x] user agent declarations
- [ ] user normal declarations
- [ ] author normal declarations
- [ ] author important declarations

#### Q150. The CSS cascade assigns a weight to each style rule ?

- [x] True
- [ ] False

#### Q151. The \***\*\_\_\_\_\*\*** represents the result of the cascade: it is the declared value that wins the cascade.

- [ ] specified Value
- [ ] actual value
- [ ] computed value
- [x] cascaded value

#### Q152. Using negative text-indent is also known as **\_** ?

- [ ] The Scott Kellum method
- [x] The Phark method
- [ ] Radu Darvas Technique
- [ ] The Langridge method

#### Q153. Using margin is also known as **\_** ?

- [ ] Fahrner image replacement
- [ ] The Lindsay method
- [x] Radu Darvas Technique
- [ ] The Langridge method

#### Q154. If a particular rule should never be overridden by another rule, the \***\*\_\_\_\_\*\*** indication should be used.

- [ ] @important
- [ ] !important!
- [x] !important
- [ ] important!

#### Q155. What does CSS stand for?

- [ ] Creative Style Sheets
- [ ] Colourful Style Sheets
- [x] Cascading Style Sheets
- [ ] Colourful Style Sheets

[Reference](https://www.w3schools.com/quiztest/quiztest.asp?qtest=CSS)

#### Q156. What color would rgb(255,0,0) give?

- [ ] Blue
- [ ] Green
- [x] Red
- [ ] Yellow

#### Q157. What is the correct HTML for referring to an external style sheet?

- [x] `<link rel="stylesheet" type="text/css" href="mystyle.css">`
- [ ] `<stylesheet>mystyle.css</stylesheet>`
- [ ] `<style src= "mystyle.css">`
- [ ] None of these.

#### Q158. The \<link> tag goes inside:

- [ ] the title section
- [ ] the body section
- [x] the head section
- [ ] None of the above

#### Q159. What CSS define in HTML?

- [ ] How to send HTML elements
- [x] How to display HTML elements
- [ ] How to save HTML elements
- [ ] How to make HTML elements

#### Q160. Which of the following statements is TRUE for CSS?

- [ ] An inline style sheet should be used when a single document has a unique style
- [x] An external style sheet is ideal when the style is applied to many pages
- [ ] Both and b above
- [ ] An external style sheet can be written in HTML

#### Q161. In CSS, margin collapsing only happens with?

- [ ] The horizontal margins of inline elements in the normal flow.
- [x] The vertical margins of block elements in the normal flow.
- [ ] The horizontal margins of block elements in the normal flow.
- [ ] The vertical margins of inline elements in the normal flow.
