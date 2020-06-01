CSS Assessment
--------------

#### Q1. In the following example, which selector has the highest specificity ranking for selecting the anchor link element?
```css
ul li a 
a 
.example a 
div a
```
- .example a
- div a 
- a
- ul li a

#### Q2. Using an attribute selector, how would you select an `<a>` element with a "title" attribute?
- a[title]{...}
- a > title {...}
- a.title {...}
- a=title {...}

#### Q3. CSS grid and flexbox are now becoming a more popular way to create page layouts. However, floats are still commonly used, especially when working with an older code base, or it you need to support older browser version. What are two valid techniques used to clear floats?
- Use the "clearfix hack" on the floated element and add a float to the parent element.
- Use the overflow property on the floated element or the "clearfix hack" on either the floated or parent element.
- Use the "clearfix hack" on the floated element or the overflow property on the parent element.
- Use the "clearfix hack" on the parent element or use the overflow property with a value other than "visible."

#### Q4. What element(s) do the following selectors match to?
`1) .nav {...}`
`2) nav {...}`
`3) #nav {...}`

- 
```
1) An element with an ID of "nav"
2) A nav element
3) An element with a class of "nav"
```
- 
```
They all target the same nav element.
```
- 
```
1) An element with an class of "nav"
2) A nav element
3) An element with a id of "nav"
```
- 
```
1) An element with an class of "nav"
2) A nav element
3) An div with a id of "nav"
```

#### Q5. When adding transparency styles, what is the difference between using the opacity property versus the background property with an rgba() value?
- Opacity applies transparency to the parent and child elements. Background with an rgba() value specifies the level of transparency of the parent element only.
- Opacity applies transparency to the background color only. Background with an rgba() value specifies the level of transparency of an element, as a whole, including its content.
- Opacity specifies the level of transparency of an element, including its content. Background with an rgba() value applies transparency to the background color only.
- Opacity specifies the level of transparency of the child elements. Background with an rgba() value applies transparency to the background color only.

#### Q6. When would you use the @font-face method?
- to load CSS into a webpage
- to change the name of the font declared in the font-family
- to load custom fonts into a webpage
- to make sure the font-family declaration displays the same for all users

#### Q7. In the shorthand example below, which individual background properties are represented?
`background: blue url(image.jpg) no-repeat scroll Opx Opx;`

- background-color: blue;\
  background-src: url(image.jpg);\
  background-repeat: no-repeat;\
  background-wrap: scroll;\
  background-position: 0px 0px;
- background-color: blue;\
  background-image: url(image.jpg);\
  background-repeat: no-repeat;\
  background-scroll: scroll;\
  background-position: 0px 0px:
- background-color: blue;\
  background-img: url (image.jpg);\
  background-position: no-repeat;\
  background-scroll: scroll;\
  background-size: 0px 0px;
- background-color: blue;\
  background-image: url (image.jpg);\
  background-repeat: no-repeat;\
  background-attachment: scroll;\
  background-position: 0px 0px;

#### Q8. To change the color of an SVG using CSS, which property is used?
- Use fill or background to set the color inside the object and stroke to set the color of the border.
- Use fill to set the color inside the object and stroke to set the color of the border.
- The color cannot be changed with CSS.
- Use background-fill to set the color inside the object and stroke or border to set the color of the border.

#### Q9. When using position: fixed, what wil the element always be positioned relative to?
- the wrapper element
- the closest element with position: relative
- the parent element
- the viewport

#### Q10. When using flexbox, the "justify-content" property can be used to distribute the space between the flex items along the main  axis. Which value should be used to evenly distribute the flex items within the container shown below?
`[[1]   [2]   [3]   [4]]`
- justify-content: space-around;
- justify-content: space-between;
- justify-content: auto;
- justify-content: center;

#### Q11. Which type of declaration will take precedence?
- important declaration in user stylesheets
- important declaration in author stylesheets
- any declarations in user-agent stylesheets
- normal declarations in author stylesheets

#### Q12. In this example, what is the selector, property, and value?
```
p {
   color: #000000;
 }
```
- "color" is the selector\
  "#000000#" is the property\
  "#p" is the value
- "p" is the selector\
  "color" is the property\
  "#000000" is the value
- "color" is the selector\
  "p" is the property\
  "#000000" is the value
- "p" is the selector\
  "#000000" is the property\
  "color" is the value

#### Q13. Which type of declaration will take precedence?
- any declarations in user-agent stylesheets
- important declarations in author stylesheets
- important declarations in user stylesheets
- normal declarations in author stylesheets

#### Q14. How would you make the first letter of every paragraph on the page red?
- first-letter:p { color: red; }
- p:first-letter { color: red; }
- first-letter::p { color: red; }
- p::first-letter { color: red; }

#### Q15. What is the difference between the margin and padding properties?
- Margin adds a line around an element, Padding adds space inside of an element.
- Margin adds space around an element; Padding adds space inside of an element.
- Margin adds space inside of an element; Padding adds space around an element.
- Margin adds space around and inside of an element; Padding only adds space inside of an element.

#### Q16. What are three valid ways of adding CSS to an HTML page?

-
```
1. External; CSS is written in a separate file and is linked within the <head> element of...
2. Inline; CSS is added to the HTML tag.
3. Internal; CSS is included within the <head> element of the HTML file.
```
-
```
1. External; CSS is written in a separate file and is linked within the <head> element of...
2. Internal; CSS is included within the <header> element of the HTML file.
3. Inline; CSS is added to the HTML tag.
```
-
```
1. External; CSS is written in a separate file and is linked within the <header> element of...
2. Inline; CSS is added to the HTML tag.
3. Internal; CSS is included within the <header> element of the HTML file.
```
-
```
1. External; CSS is written in a separate file.
2. Inline; CSS is added to the <head> of the HTML page.
3. Internal; CSS is included within the HTML tags.
```

#### Q17. The calc() CSS function is often used for calculating relative values. In the example below, what is the specified margin-left value?
```
.example {
    margin-left: calc (5% + 5px);
}
```
- The left margin value is equal to 5% of its parent element's width plus 5px.
- The left margin value is equal to 5% of the selected element's width (.example) plus 5px.
- The left margin value is equal to 5% of the viewport width plus 5px.
- The left margin value is equal to 5% of the closest positioned element's width plus 5px.

#### Q18. Review the HTML snippet below. What would be the most efficient way of using attribute selectors to select only the internal links?
```
<a href="#examplel">Internal link</a>
<a href="#example2">Internal link</a>
<a href="#example3">Internal link</a>
<a href="https://example.com">example.com</a>
```
- `a[href^="#"] {...}`
- `a[href*="example"] {...}`
- `a[href="#"] {...}`
-
```
a[href="#example1"],
a[href="#example2"],
a[href="#example3"] {...}
```

#### Q19. There are two sibling combinators that can be used to select elements contained within the same parent element; the general sibling combinator (~) and the adjacent sibling combinator (+). Referring to example below, which elements will the styles be applied to?
```
h2 ~ p {
  color: blue;
}
h2 + p {
  background: beige;
}
<section>
  <p>paragraph 1</p>
  <h2>Heading</h2>
  <p>paragraph 2</p>
  <p>paragraph 3</p>
</section>
```
- Paragraphs 2 and 3 will be blue. The h2 and paragraph 2 will have a beige background.
- Paragraphs 1, 2, and 3 will be blue, and paragraph 2 will have a beige background.
- Paragraph 2 will be blue. Paragraphs 2 and 3 will have a beige background.
- Paragraphs 2 and 3 will be blue. Paragraph 2 will have a beige background.
