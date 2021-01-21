## CSS

#### Q1. In the following example, which selector has the highest specificity ranking for selecting the anchor link element?
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
- [x] a[title]{...}
- [ ] a > title {...}
- [ ] a.title {...}
- [ ] a=title {...}

#### Q3. CSS grid and flexbox are now becoming a more popular way to create page layouts. However, floats are still commonly used, especially when working with an older code base, or it you need to support older browser version. What are two valid techniques used to clear floats?
- [ ] Use the "clearfix hack" on the floated element and add a float to the parent element.
- [ ] Use the overflow property on the floated element or the "clearfix hack" on either the floated or parent element.
- [ ] Use the "clearfix hack" on the floated element or the overflow property on the parent element.
- [x] Use the "clearfix hack" on the parent element or use the overflow property with a value other than "visible."

#### Q4. What element(s) do the following selectors match to?
`1) .nav {...}`
`2) nav {...}`
`3) #nav {...}`
- [ ]
```markdown
1. An element with an ID of "nav"
2. A nav element
3. An element with a class of "nav"
```
- [ ]
```markdown
They all target the same nav element.
```
- [x]
```markdown
1. An element with an class of "nav"
2. A nav element
3. An element with a id of "nav"
```
- [ ]
```markdown
1. An element with an class of "nav"
2. A nav element
3. An div with a id of "nav"
```

#### Q5. When adding transparency styles, what is the difference between using the opacity property versus the background property with an `rgba()` value?
- [ ] Opacity specifies the level of transparency of the child elements. Background with an `rgba()` value applies transparency to the background color only.
- [ ] Opacity applies transparency to the background color only. Background with an `rgba()` value specifies the level of transparency of an element, as a whole, including its content.
- [x] Opacity specifies the level of transparency of an element, including its content. Background with an `rgba()` value applies transparency to the background color only.
- [ ] Opacity applies transparency to the parent and child elements. Background with an `rgba()` value specifies the level of transparency of the parent element only.

#### Q6. What is true of block and inline elements?
- [ ] By default, block elements are the same height and width as the content container between their tags; inline elements span the entire width of its container.
- [x] By default, block elements span the entire width of its container; inline elements are the same height and width as the content contained between their tags.
- [ ] A `<nav>` element is an example of an inline element. `<header>` is an example of a block element.
- [ ] A `<span>` is an example of a block element. `<div>` is an example of an inline element.

#### Q7. CSS grid introduced a new length unit, fr, to create flexible grid tracks. Referring to the code sample below, what will the widths of the three columns be?
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

#### Q8. What is the line-height property primarily used for?
- [x] to control the height of the space between two lines of content
- [ ] to control the height of the space between heading elements
- [ ] to control the height of the character size
- [ ] to control the width of the space between characters

#### Q9. Three of these choices are true about class selectors. Which is NOT true?
- [ ] Multiple classes can be used within the same element.
- [ ] The same class can be used multiple times per page.
- [ ] Class selectors with a leading period
- [x] Classes can be used multiple times per page but not within the same element.

#### Q10. There are many properties that can be used to align elements and create page layouts such as float, position, flexbox and grid. Of these four properties, which one should be used to align a global navigation bar which stays fixed at the top of the page?
- [x] position
- [ ] flexbox
- [ ] grid
- [ ] float

#### Q11. In the shorthand example below, which individual background properties are represented?
`background: blue url(image.jpg) no-repeat scroll 0px 0px;`
- [x]
```css
background-color: blue;
background-image: url(image.jpg);
background-repeat: no-repeat;
background-attachment: scroll;
background-position: 0px 0px;
```
- [ ]
```css
background-color: blue;
background-img: url(image.jpg);
background-position: no-repeat;
background-scroll: scroll;
background-size: 0px 0px;
```
- [ ]
```css
background-color: blue;
background-src: url(image.jpg);
background-repeat: no-repeat;
background-wrap: scroll;
background-position: 0px 0px;
```
- [ ]
```css
background-color: blue;
background-src: url(image.jpg);
background-repeat: no-repeat;
background-scroll: scroll;
background-position: 0px 0px;
```

#### Q12. In the following example, according to cascading and specificity rules, what color will the link be?
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

#### Q13. When elements overlap, they are ordered on the z-axis (i.e., which element covers another). The z-index property can be used to specify the z-order of overlapping elements. Which set of statements about the z-index property are true?
- [x] Larger z-index values appear on top of elements with a lower z-index value. Negative and positive numbers can be used. z-index can only be used on positioned elements.
- [ ] Smaller z-index values appear on top of elements with a larger z-index value. Negative and positive numbers can be used. z-index must also be used with positioned elements.
- [ ] Larger z-index values appear on top of elements with a lower z-index value. Only positive numbers can be used. z-index must also be used with positioned elements.
- [ ] Smaller z-index values appear on top of elements with a larger z-index value. Negative and positive numbers can be used. z-index can be used with or without positioned elements.

#### Q14. What is the difference between the following line-height settings?
```css
line-height: 20px
line-height: 2
```
- [x] The value of 20px will set the line-height to 20px. The value of 2 will set the line-height to twice the size of the corresponding font-size value.
- [ ] The value of 20px will set the line-height to 20px. The value of 2 is not valid.
- [ ] The value of 20px will set the line-height to 20px. The value of 2 will default to a value of 2px.
- [ ] The value of 20px will set the line-height to 20px. The value of 2 will set the line-height to 20% of the corresponding font-size value.

#### Q15. In the following example, what color will paragraph one and paragraph two be?
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

#### Q16.What are three valid ways of adding CSS to an HTML page?
- [ ]
```markdown
1. External; CSS is written in a separate file.
2. Inline; CSS is added to the <head> of the HTML page.
3. Internal; CSS is included within the HTML tags.
```
- [ ]
```markdown
1. External; CSS is written in a separate file and is linked within the <header> element of the HTML file.
2. Inline; CSS is added to the HTML tag.
3. Internal; CSS is included within the <header> element of the HTML  file.
```
- [x]
```markdown
1. External; CSS is written in a separate file and is linked within the <head> element of the HTML file.
2. Internal; CSS is included within the <header> element of the HTML file.
3. Inline; CSS is added to the HTML tag.
```
- [ ]
```markdown
1. External; CSS is written in a separate file and is linked within the <head> element of the HTML file .
2. Inline; CSS is added to the HTML tag.
3. Internal; CSS is included within the <head> element of the HTML file.
```

#### Q17. Which of the following is true of the SVG image format?
- [ ] CSS can be applied to SVGs but JavaScript cannot be.
- [ ] SVGs work best for creating 3D graphics.
- [x] SVGs can be created as a vector graphic or coded using SVG specific elements such as &#x3C;svg&#x3E;, &#x3C;line&#x3E;, and &#x3C;ellipse&#x3E;.
- [ ] SVGs are a HAML-based markup language for creating vector graphics.

#### Q18. In the example below, when will the color pink be applied to the anchor element?
```css
a:active {
  color: pink;
}
```
- [ ] The color of the link will display as pink after its been clicked or if the mouse is hovering over the link.
- [ ] The color of the link will display as pink on mouse hover.
- [x] The color of the link will display as pink while the link is being clicked but before the mouse click is released.
- [ ] The color of the link will display as pink before it has been clicked.

#### Q19. To change the color of an SVG using CSS, which property is used?
- [ ] Use background-fill to set the color inside the object and stroke or border to set the color of the border.
- [ ] The color cannot be changed with CSS.
- [ ] Use fill or background to set the color inside the object and stroke to set the color of the border.
- [x] Use fill to set the color inside the object and stroke to set the color of the border.

#### Q20. When using position: fixed, what will the element always be positioned relative to?
- [ ] the closest element with position: relative
- [x] the viewport
- [ ] the parent element
- [ ] the wrapper element

#### Q21. By default, a background image will repeat `\_\_\_`
- [ ] only if the background-repeat property is set to repeat
- [x] indefinitely, vertically, and horizontally
- [ ] indefinitely on the horizontal axis only
- [ ] once, on the x and y axis

#### Q22. When using media queries, media types are used to target a device category. Which choice lists current valid media types?
- [ ] print, screen, aural
- [ ] print, screen, television
- [x] print, screen, speech
- [ ] print, speech, device

#### Q23. How would you make the first letter of every paragraph on the page red?
- [x] p::first-letter { color: red; }
- [ ] p:first-letter { color: red; }
- [ ] first-letter::p { color: red; }
- [ ] first-letter:p { color: red; }

#### Q24. In this example, what is the selector, property, and value?
```css
p {
  color: #000000;
}
```
- [ ]
```markdown
"p" is the selector
"#000000" is the property
"color" is the value
```
- [x]
```markdown
"p" is the selector
"color" is the property
"#000000" is the value
```
- [ ]
```markdown
"color" is the selector
"#000000" is the property
"#p" is the value
```
- [ ]
```markdown
"color" is the selector
"p" is the property
"#000000" is the value
```

#### Q25. What is the rem unit based on?
- [ ] The rem unit is relative to the font-size of the p element.
- [ ] You have to set the value for the rem unit by writing a declaration such as rem { font-size: 1 Spx; }
- [ ] The rem unit is relative to the font-size of the containing (parent) element.
- [x] The rem unit is relative to the font-size of the root element of the page.

#### Q26.Which of these would give a block element rounded corners?
- [ ] corner-curve: 10px
- [ ] border-corner: 10px
- [x] border-radius: 10px
- [ ] corner-radius: 10px

#### Q27. In the following media query example, what conditions are being targeted?
```css
@media (min-width: 1024px), screen and (orientation: landscape) { … }
```
- [x] The rule will apply to a device that has either a width of 1024px or wider, or is a screen device in landscape mode.
- [ ] The rule will apply to a device that has a width of 1024px or narrower and is a screen device in landscape mode.
- [ ] The rule will apply to a device that has a width of 1024px or wider and is a screen device in landscape mode.
- [ ] The rule will apply to a device that has a width of 1024px or narrower, or is a screen device in landscape mode.

#### Q28. CSS transform properties are used to change the shape and position of the selected objects. The transform-origin property specifies the location of the element's transformation origin. By default, what is the location of the origin?
- [x] the top left corner of the element
- [ ] the center of the element
- [ ] the top right corner of the element
- [ ] the bottom left of the element

#### Q29. Which of the following is not a valid color value?
- [ ] color: #000
- [ ] color: rgb(0,0,0)
- [ ] color: #000000
- [x] color: 000000

#### Q30. What is the vertical gap between the two elements below?
```html
<div style="margin-bottom: 2rem;">Div 1</div>
<div style="margin-top: 2rem;">Div 2</div>
```
- [x] 2rem
- [ ] 32px
- [ ] 64px
- [ ] 4rem

#### Q31. When using the Flexbox method, what property and value is used to display flex items in a column?
- [x] flex-flow: column; or flex-direction: column
- [ ] flex-flow: column;
- [ ] flex-column: auto;
- [ ] flex-direction: column;

#### Q32. Which type of declaration will take precedence?
- [ ] any declarations in user-agent stylesheets
- [x] important declarations in user stylesheets
- [ ] normal declarations in author stylesheets
- [ ] important declarations in author stylesheets

#### Q33. The flex-direction property is used to specify the direction that flex items are displayed. What are the values used to specify the direction of the items in the following examples?
- [x] Example 1: `flex-direction: row;`
      Example 2: `flex-direction: row-reverse;`
      Example 3: `flex-direction: column;`
      Example 4: `flex-direction: column-reverse;`
- [ ] Example 1: `flex-direction: row-reverse;`
      Example 2: `flex-direction: row;`
      Example 3: `flex-direction: column-reverse;`
      Example 4: `flex-direction: column;`
- [ ] Example 1: `flex-direction: row;`
      Example 2: `flex-direction: row-reverse;`
      Example 3: `flex-direction: column;`
      Example 4: `flex-direction: reverse-column;`
- [ ] Example 1: `flex-direction: column;`
      Example 2: `flex-direction: column-reverse;`
      Example 3: `flex-direction: row;`
      Example 4: `flex-direction: row-reverse;`

#### Q34. There are two sibling combinators that can be used to select elements contained within the same parent element; the general sibling combinator (~) and the adjacent sibling combinator (+). Referring to example below, which elements will the styles be applied to?
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
- [x] Paragraphs 2 and 3 will be blue. Paragraph 2 will have a beige background.
- [ ] Paragraph 2 will be blue. Paragraphs 2 and 3 will have a beige background.

#### Q35. When using flexbox, the "justify-content" property can be used to distribute the space between the flex items along the main axis. Which value should be used to evenly distribute the flex items within the container shown below?
- [x] justify-content: space-around;
- [ ] justify-content: center;
- [ ] justify-content: auto;
- [ ] justify-content: space-between;

#### Q36. There are many advantages to using icon fonts. What is one of those advantages?
- [ ] Icon fonts increase accessibility.
- [ ] Icon fonts can be used to replace custom fonts.
- [x] Icon fonts can be styled with typography related properties such as font-size and color.
- [ ] Icon fonts are also web safe fonts.

#### Q37. What is the difference between `display:none` and `visibility:hidden`?
- [ ] Both will hide the element on the page, but display:none has greater browser support. visibility:hidden is a new property and does not have the best browser support
- [ ] display:none hides the elements but maintains the space it previously occupied. visibility:hidden will hide the element from view and remove it from the normal flow of the document
- [x] display:none hides the element from view and removes it from the normal flow of the document. visibility:hidden will hide the element but maintains the space it previously occupied.
- [ ] There is no difference; both will hide the element on the page

### Q38. What selector and property would you use to scale an element to be 50% smaller on hover?
- [ ] element:hover {scale: 0.5;}
- [x] element:hover {transform: scale(0.5);}
- [ ] element:hover {scale: 50%;}
- [ ] element:hover {transform: scale(50%);}

### Q39. Which statement regarding icon fonts is true?
- [ ] Icon fonts can be inserted only using JavaScript.
- [ ] Icon fonts are inserted as inline images.
- [ ] Icon fonts require browser extensions.
- [x] Icon fonts can be styled with typography-related properties such as font-size and color.

### Q40. The values for the font-weight property can be keywords or numbers. For each numbered value below, what is the associated keyword?
`font-weight: 400; font-weight: 700;`
- [ ] bold; normal
- [x] normal; bold
- [ ] light; normal
- [ ] normal; bolder

### Q41. If the width of the container is 500 pixels, what would the width of the three columns be in this layout?
`.grid { display: grid; grid-template-columns: 50px 1fr 2fr; }`
- [x] 50px, 150px, 300px
- [ ] 50px, 200px, 300px
- [ ] 50px, 100px, 200px
- [ ] 50px, 50px, 100px

### Q42. Using the :nth-child pseudo class, what would be the most efficient way to style every third item in a list, no matter how many items are present, starting with item 2?
- [ ]
```css
li:nth-child(3 + 2n) {
  margin: 0 5 px;
}
```
- [x]
```css
li:nth-child(3n + 2) {
  margin: 0 5 px;
}
```
- [ ]
```css
li:nth-child(2),
li:nth-child(5),
li:nth-child(8) {
  margin: 0 5 px;
}
```
- [ ]
```css
li:nth-child(2n + 3) {
  margin: 0 5 px;
}
```

### Q43. Which selector would select only internal links within the current page?
- [ ] a[href="#"] {...}
- [ ] a[href~="#"]
- [ ] a[href^="#"]
- [x] a[href="#"]

### Q44. What is not true about class selectors?
- [x] Only one class value can be assigned to an element.
- [ ] An element can have multiple class value.
- [ ] Class selectors are marked with a leading period.
- [ ] More than one element can have the same class value.

### Q45. What is the difference between the margin and padding properties?
- [ ] Margin adds space around and inside of an element; padding adds space only inside of an element.
- [x] Margin adds space around an element; padding adds apace inside of an element.
- [ ] Margin adds a line around an element, padding adds space inside of an element.
- [ ] Margin adds space inside of an element, padding adds space around an element.

### Q46. What is not a valid way of declaring a padding value of 10 pixels on the top and bottom, and 0 pixels on the left and right?
- [x] padding: 10px 10px 0px 0px;
- [ ] padding: 10px 0px;
- [ ] padding: 10px 0;
- [ ] padding: 10px 0px 10px 0px;

### Q47. Is there an error in this code? If so, find the best description of the problem
```css
@font-face {
  font-family: 'Avenir', sans-serif;
  src:  url('avenir.woff2') format('woff2'),
        url('avenir.woff') format('woff');
}
```
- [ ] The font file formats are not supported in modern browsers.
- [ ] The src attribute requires a comma between the URL and format values.
- [ ] There are no errors in the example.
- [x] The sans-serif inclusion is problematic.

### Q48. Which style places an element at a fixed location within its container?
- [x] position: absolute;
- [ ] display: flex;
- [ ] display: block;
- [ ] float: left;

### Q49. The calc() CSS function is often used for calculating relative values. In the example below, what is the specified margin-left value?
```css
.example{
  margin-left: calc(5% + 5px);
}
```
- [x] The left margin value is equal to 5% of its parents element's width plus 5px
- [ ] The left margin value is equal to 5% of the viewport width plus 5px
- [ ] The left margin value is equal to 5% of the closest positioned element's width plus 5px
- [ ] The left margin value is equal to 5% of the selected element's width (.example) plus 5px

### Q50. What is the CSS selector for an `<a>` tag containing the title attribute?
- [x] a[title]
- [ ] a > title
- [ ] a=title
- [ ] a.title

### Q51. Which code would you use to absolutely position an element of the logo class?
- [x] `.logo { position: absolute; left: 100px; top: 150px; }`
- [ ] `.logo { position: absolute; margin-left: 100px; margin-top: 150px; }`
- [ ] `.logo { position: absolute; padding-left: 100px; padding-top: 150px; }`
- [ ] `.logo { position: absolute; left-padding: 100px; top-padding: 150px; }`

#### Q52. In this example, what color will Paragraph 1 be?
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

### Q53. What is the `::placeholder pseudo-element` used for?
- [x] It is used to format the appearance of placeholder text within a form control.
- [ ] It specifies the default input text for a form control.
- [ ] It writes text content into a hyperlink tooltip.
- [ ] It writes text content into any page element.

### Q54. Which statement is true of the single colon (`:`) or double colon (`::`) notations for pseudo-elements-for example, `::before` and `:before`?
- [ ] All browsers support single and double colons for new and older pseudo-elements. So you can use either but it is convention to use single colons for consistency.
- [ ] In CSS3, the double colon notation (`::`) was introduced to create a consistency between pseudo-elements from pseudo-classes. For newer browsers, use the double colon notation. For IE8 and below, using single colon notation (`:`).
- [ ] Only the new CSS3 pseudo-elements require the double colon notation while the CSS2 pseudo-elements do not.
- [x] In CSS3, the double colon notation (`::`) was introduced to differentiate pseudo-elements from pseudo-classes. However, modern browsers support both formats. Older browsers such as IE8 and below do not.

#### Q55. Which choice is not valid value for the font-style property?
- [ ] normal
- [ ] italic
- [x] none
- [ ] oblique

#### Q56. When would you use the @font-face method?
- [ ] to set the font size of the text
- [x] to load custom fonts into stylesheet
- [ ] to change the name of the font declared in the font-family
- [ ] to set the color of the text

#### Q57. When elements within a container overlap, the z-index property can be used to indicate how those items are stacked on top of each other. Which set of statements is true?
- [x]
```markdown
1. Larger z-index values appear on top elements with a lower z-index value.
2. Negative and positive number can be used.
3. z-index can be used only on positioned elements.
```
- [ ]
```markdown
1. Smaller z-index values appear on top of elements with a larger z-index value.
2. Negative and positive numbers can be used.
3. z-index can be used with or without positioned elements.
```
- [ ]
```markdown
1. Smaller z-index values appear on top of elements with a larger z-index value.
2. Negative and positive number can be used.
3. z-index must also be used with positioned elements.
```
- [ ]
```markdown
1. Larger z-index values appear on top of elements with a lower z-index value.
2. Only positive number can be used.
3. z-index must also be used with positioned elements.
```
