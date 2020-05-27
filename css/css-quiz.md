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


