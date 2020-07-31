CSS Assessment
--------------

#### Q1. In the following example, which selector has the highest specificity ranking for selecting the anchor link element?
```css
ul li a 
a 
.examole a 
div a
```
- .example a  <<<<---Correct
- div a 
- a
- ul li a

#### Q2. Using an attribute selector, how would you select an `<a>` element with a "title" attribute?
- a[title]{...}    <<<<---Correct
- a > title {...}
- a.title {...}
- a=title {...}

#### Q3. CSS grid and flexbox are now becoming a more popular way to create page layouts. However, floats are still commonly used, especially when working with an older code base, or it you need to support older browser version. What are two valid techniques used to clear floats?
- Use the "clearfix hack" on the floated element and add a float to the parent element.
- Use the overflow property on the floated element or the "clearfix hack" on either the floated or parent element.
- Use the "clearfix hack" on the floated element or the overflow property on the parent element.
- Use the "clearfix hack" on the parent element or use the overflow property with a value other than "visible."     <<<<---Correct

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
1) An element with an class of "nav"     <<<<---Correct
2) A nav element
3) An element with a id of "nav"
```
- 
```
1) An element with an class of "nav"
2) A nav element
3) An div with a id of "nav"
```

#### Q5. When adding transparency styles, what is the difference between using the opacity property versus the background property with an `rgba()` value?
- Opacity specifies the level of transparency of the child elements. Background with an `rgba()` value applies transparency to the background color only.
- Opacity applies transparency to the background color only. Background with an `rgba()` value specifies the level of transparency of an element, as a whole, including its content. 
- Opacity specifies the level of transparency of an element, including its content. Background with an `rgba()` value applies transparency to the background color only.  <<<<---Correct
- Opacity applies transparency to the parent and child elements. Background with an `rgba()` value specifies the level of transparency of the parent element only.

#### Q6. What is true of block and inline elements?
- By default, block elements are the same height and width as the content container between their tags; inline elements span the entire width of its container.
- By default, block elements span the entire width of its container; inline elements are the same height and width as the content contained between their tags.
- A "<nav>" element is an example of an inline element. "<header>" is an example of a block element.  <<<<---Correct
- A "<span>" is an example of a block element. "<div>" is an example of an inline element.

#### Q7. CSS grid introduced a new lenght unit, fr, to create flexible grid tracks. Referring to the code sample below, what will the widths of the three columns be?
```css
.grid {
    display: grid;
    width: 500px;
    grid-template-columns: 50px 1fr 2fr;
}
```
- The first column will have a width of 50px. The second column will be 50px wide and the third column will be 100px wide.
- The first column will have a width of 50px. The second column will be 150px wide and the third column will be 300px wide.  <<<<---Correct
- The first column will have a width of 50px. The second column will be 300px wide and the third column will be 150px wide.
- The first column will have a width of 50px. The second column will be 500px wide and the third column will be 1000px wide.

#### Q8. What is the line-height property primarily used for?
- to control the height of the space between two lines of content      <<<<---Correct
- to control the height of the space between heading elements
- to control the height of the character size
- to control the width of the space between characters

#### Q9. Three of these choices are true about class selectors. Which is NOT true?
- Multiple classes can be used within the same element.
- The same class can be used multiple times per page.
- Class selectors with a leading period
- Classes can be used multiple times per page but not within the same element.  <<<<---Correct


#### Q10. There are many properties that can be used to align elements and create page layouts such as float, position, flexbox and grid. Of these four properties, which one should be used to align a global navigation bar which stays fixed at the top of the page?
- position   <<<<---Correct
- flexbox
- grid
- float

#### Q11. In the shorthand example below, which individual background properties are represented?
`background: blue url(image.jpg) no-repeat scroll 0px 0px;`

-
```
background-color: blue;                          <<<<---Correct
background-image: url(image.jpg);
background-repeat: no-repeat;
background-attachment: scroll;
background-position: 0px 0px;
```
-
```
background-color: blue;
background-img: url(image.jpg);
background-position: no-repeat;
background-scroll: scroll;
background-size: 0px 0px;
```
-
```
background-color: blue;
background-src: url(image.jpg);
background-repeat: no-repeat;
background-wrap: scroll;
background-position: 0px 0px;
```
-
```
background-color: blue;
background-src: url(image.jpg);
background-repeat: no-repeat;
background-scroll: scroll;
background-position: 0px 0px;
```

#### Q12. In the following example, according to cascading and specificity rules, what color will the link be?
```
.example {color: yellow;}
ul li a {color:  blue;}
ul a {color: green;}
a {color: red;}
<ul>
    <li><a href="#" class="example">link</a></li>
    <li>list item</li>
    <li>list item</li>
</ul>
```

- green
- yellow  <<<<---Correct
- blue
- red

#### Q13. When elements overlap, they are ordered on the z-axis (i.e., which element covers another). The z-index property can be used to specify the z-order of overlapping elements. Which set of statements about the z-index property are ture?
- Larger z-index values appear on top of elements with a lower z-index value. Negative and positive numbers can be used. z-index can only be used on positioned elements.     <<<<---Correct
- Smaller z-index values appear on top of elements with a larger z-index value. Negative and positive numbers can be used. z-index must also be used with positioned elements.
- Larger z-index values appear on top of elements with a lower z-index value. Only positive numbers can be used. z-index must also be used with positioned elements.
- Smaller z-index values appear on top of elements with a larger z-index value. Negative and positive numbers can be used. z-index can be used with or without positioned elements.

#### Q14. What is the difference between the following line-height settings?
```css
line-height: 20px
line-height: 2
```
- The value of 20px will set the line-height to 20px. The value of 2 will set the line-height to twice the size of the corresponding font-size value.   <<<<---Correct
- The value of 20px will set the line-height to 20px. The value of 2 is not valid.
- The value of 20px will set the line-height to 20px. The value of 2 will default to a value of 2px.
- The value of 20px will set the line-height to 20px. The value of 2 will set the line-height to 20% of the corresponding font-size value.

#### Q15. In the following example, what color will paragraph one and paragraph two be?
```javascript
<section>
    <p>paragraph one</p>
</section>

<p>paragraph two</p>

section p{
    color: red;
}
section + p {
    color: blue;
}
```
- Paragraph one will be blue, paragraph two will be red.
- Both paragraphs will be blue.
- Paragraphs one will be red, paragraph two will be blue.  <<<<---Correct
- Both paragraphs will be red.

#### Q16.What are three valid ways of adding CSS to an HTML page?
-
```
1. External; CSS is written in a separate file.
2. Inline; CSS is added to the <head> of the HTML page.
3. Internal; CSS is included within the HTML tags.
```
-
```
1. External; CSS is written in a separate file and is linked within the <header> element of the HTIML  file . 
2. Inline; CSS is added to the HTML tag.
3. Internal; CSS is included within the <header> element of the HTML  file.
```
-
```
1. External; CSS is written in a separate file and is linked within the <head> element of the HTML file . 
2. Internal; CSS is included within the <header> element of the HTML file.
3. Inline; CSS is added to the HTML tag.
```
-
```
1. External; CSS is written in a separate file and is linked within the <head> element of the HTML file .
2. Inline; CSS is added to the HTML tag.
3. Internal; CSS is included within the <head> element of the HTML file.
```
#### Q17. Which of the following is true of the SVG image format?
- CSS can be applied to SVGs but JavaScript cannot be.
- SVGs work best for creating 3D graphics.
- SVGs can be created as a vector graphic or coded using SVG specific elements such as <svg>, <line>, and <ellipse>.  <<<<---Correct
- SVGs are a HAML-based markup language for creating vector graphics.


#### Q18.In the example below, when will the color pink be applied to the anchor element?   
    a:active { 
        color: pink;
    }
    
- The color of the link will display as pink after its been clicked or if the mouse is hovering over the link.
- The color of the link will display as pink on mouse hover.
- The color of the link will display as pink while the link is being clicked but before the mouse 
click is released.  <<<<---Correct
- The color of the link will display as pink before it has been clicked.

#### Q19. To change the color of an SVG using CSS, which property is used?
- Use background-fill to set the color inside the object and stroke or border to set the color of the border. 
- The color cannot be changed with CSS.
- Use fill or background to set the color inside the object and stroke to set the color of the border.
- Use fill to se t the color inside the object and stroke to set the color of the border.  <<<<---Correct

#### Q20. When using position: fixed, what will the element always be positioned relative to?
- the closest element with position: relative
- the viewport <<<<---Correct
- the parent element
- the wrapper element

#### Q21. By default, a background image will repeat ________
- only if the background-repeat property is set to repeat
- indefinitely, vertically, and horizontally  <<<<---Correct
- indefinitely on the horizontal axis only 
- once, on the x and y axis

#### Q22. When using media queries, media types are used to target a device category. Which choice lists current valid media types?
- print, screen, aural <<<<---Correct
- print, screen, television
- print, screen, speech 
- print, speech, device 

#### Q23. How would you make the first letter of every paragraph on the page red?
- p::first-letter { color: red; }  <<<<---Correct
- p:first-letter { color: red; }
- first-letter::p { color: red; }
- first-letter:p { color: red; }

#### Q24.In this example, what is the selector, property, and value?
```css
p {
color: #000000;
}
```
-
``` 
"p" is the selector
"#000000" is the property 
"color" is the value
```
-
```
"p" is the selector      <<<<---Correct
"color" is the property 
"#000000" is the value
```
-
```
"color" is the selector
"#000000" is the property 
"#p" is the value
```
-
```
"color" is the selector
"p" is the property 
"#000000" is the value
```

#### Q25. What is the rem unit based on?
- The rem unit is relative to the font-size of the p element.
- You have to set the value for the rem unit by writing a declaration such as rem { font-size: 1 Spx; }
- The rem unit is relative to the font-size of the containing (parent) element.
- The rem unit is relative to the font-size of the root element of the page. <<<<---Correct

#### Q26.Which of these would give a block element rounded corners?
- corner-curve: 10px
- border-corner: 10px
- border-radius: 10px  <<<<---Correct
- corner-radius: 10px
 
#### Q27. In the following media query example, what conditions are being targeted?
`@media (min-width: 1024px), screen and (orientation: landscape) { … }`
- The rule will apply to a device that has either a width of 1024px or wider, or is a screen device in landscape mode.
- The rule will apply to a device that has a width of 1024px or narrower and is a screen device in landscape mode.
- The rule will apply to a device that has a width of 1024px or wider and is a screen device in landscape mode. <<<<---Correct
- The rule will apply to a device that has a width of 1024px or narrower, or is a screen device in landscape mode.
 
#### Q28. CSS transform properties are used to change the shape and position of the selected objects. The transform-origin property specifies the location of the element's transformation origin. By default, what is the location of the origin?
 
- the top left corner of the element
- the center of the element  <<<<---Correct
- the top right corner of the element
- the bottom left of the element

#### Q29. Which of the following is not a valid color value?
- color: #000
- color: rgb(0,0,0)
- color: #000000
- color: 000000 <<<<---Correct

#### Q30. What is the vertical gap between the two elements below?
```css
<div style="margin-bottom: 2rem;">Div 1</div>
<div style="margin-top: 2rem;">Div 2</div>
```
- 2rem
- 32px
- 64px
- 4rem <<<<---Correct

#### Q31. When using the Flexbox method, what property and value is used to display flex items in a column?
- flex-flow: column; or flex-direction: column <<<<---Correct
- flex-flow: column;
- flex-column: auto;
- flex-direction: column;

#### Q32. Which type of declaration will take precedence?
- any declarations in user-agent stylesheets <<<<---Correct
- important declarations in user stylesheets
- normal declarations in author stylesheets
- important declarations in author stylesheets

#### Q33. The flex-direction property is used to specify the direction that flex items are displayed. What are the values used to specify the direction of the items in the folowing examples?
- Example 1: flex-direction: row;
Example 2; flex-direction: row-reverse;
Example 3: flex-direction: column;
Example 4: flex-direction: column-reverse;   <<<<---Correct
- Example 1: flex-direction: row-reverse;
Example 2; flex-direction: row;
Example 3: flex-direction: column-reverse;
Example 4: flex-direction: column;
- Example 1: flex-direction: row;
Example 2; flex-direction: row-reverse;
Example 3: flex-direction: column;
Example 4: flex-direction: reverse-column;
- Example 1: flex-direction: column;
Example 2; flex-direction: column-reverse;
Example 3: flex-direction: row;
Example 4: flex-direction: row-reverse;

#### Q34. There are two sibling combinators that can be used to select elements contained within the same parent element; the general sibling combinator (~) and the adjacent sibling combinator (+). Referring to esample below, which elements will the styles be applied to?
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
- Paragraphs 2 and 3 will be blue. The h2 and paragraph 2 will have a beige background.
- Paragraphs 1, 2, and 3 will be blue, and paragraph 2 will have a beige background.   <<<<---Correct
- Paragraphs 2 and 3 will be blue. Paragraph 2 will have a beige background.
- Paragraph 2 will be blue. Paragraphs 2 and 3 will have a beige background.

#### Q35. When using flexbox, the "justify-content" property can be used to distribute the space between the flex items along the main axis. Which value should be used to evenly distribute the flex items within the container shown below?
- justify-content: space-around;
- justify-content: center;
- justify-content: auto;
- justify-content: space-between;   <<<<---Correct

#### Q36. There are many advantages to using icon fonts. What is one of those advantages?
- Icon fonts increase accessibility.
- Icon fonts can be used to replace custom fonts.
- Icon fonts can be styled with typography related properties such as font-size and color. <<<<---Correct
- Icon fonts are also web safe fonts.
