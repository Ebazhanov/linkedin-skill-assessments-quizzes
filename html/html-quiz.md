## HTML Assessment

#### Q1. What is the purpose of the `<track>` tag, and when should it be used?

- [ ] The `<track>` tag is used for specifying subtitles. It is typically applied as a child of the `<audio>` and `<video>` tags.
- [ ] The `<track>` tag is used for specifying subtitles. It is typically applied as a child of the `<video>` tag.
- [ ] The `<track>` tag is used for specifying subtitles, captions, and other types of time-based text. It is typically applied as a child of the `<video>` tag.
- [x] The `<track>` tag is used for specifying subtitles, captions, and other types of time-based text. It is typically applied as a child of the `<audio>` and `<video>` tag.

#### Q2. What are the best examples of void elements?

- [ ] `<link><meta><title>`
- [x] `<wbr><base><source>`
- [ ] `<input><br><p>`
- [ ] `<area><embed><strong>`

#### Q3. In HTML5, which tag or tags embed a webpage inside of a webpage?

- [ ] `<iframe>, <frame>, and <frameset>`
- [ ] `<frame>`
- [x] `<iframe>`
- [ ] `<frame> and <frameset>`

#### Q4. Where do `<header>` and `<footer>` tags typically occur?

- [ ] as children of `<body>, <article>, <aside>, and <section>` tags
- [x] as children of `<body>, <article>, and <section>` tags
- [ ] as children of `<body>, <article>, <aside>, <nav>, and <section>` tags
- [ ] as children of `<body>, <article>, <table>, and <section>` tags

#### Q5. What's the best way to apply bold styling to text?

- [x] `<strong>`
- [ ] Use CSS.
- [ ] `<bold>`
- [ ] `<b>`

#### Q6. When is the <link> tag used?

- [ ] when linking style sheets, JavaScript, and icons for mobile apps
- [ ] when linking style sheets, favicons, and preloading assets
- [x] when linking style sheets and favicons
- [ ] when linking style sheets, external URLs, and favicons

#### Q7. The "value" attribute is associated with which set of tags?

- [ ] `<button><input><form>`
- [ ] `<input><label><meter>`
- [ ] `<input><option><textarea>`
- [x] `<li><input><option>`
  
#### Q8. What should fill the two blanks in the HTML code below?

```css
<address ______  _____>
    <span itemprop="streetAddress">
    6410 Via Real
    </span><br>
    <span itemprop="addressLocality">Carpinteria</span>,
    <span itemprop="addressRegion">CA</span>
    <span itemprop="addressCode">93013</span>
</address>
```

- [x]  `itemscope` `itemtype="http://schema.org/PostalAddress"`
  
- [ ]  `itemsref="http://schema.org/PostalAddress"` `itemid="address"`
  
- [ ]  `itemscope` `itemref="http://schema.org/PostalAddress"`
  
- [ ]  `itemid="address"` `itemtype="http://schema.org/PostalAddress"`

#### Q9. When should you use the `<aside>` element?

- [x] when the content can be removed without detracting from the page's message
- [ ] for anything you want to move to the side, like a pull quote box, a sidebar, or an image with text wrapping around it
- [ ] for anything in parentheses
- [ ] for anything in a sidebar

#### Q10. With which tags is the `<source>` element associated?
- [ ] `<svg>, <picture>, <audio>, and <video>`
- [x] `<picture>, <audio>, and <video>`
- [ ] It is iterchangeable with the src attribute, so any element which uses src may use <source..... 
- [ ] `<audio> and <video>`

#### Q11. What is NOT a valid attribute for the `<textarea>` element?

- [ ] readonly
- [x] max
- [ ] form 
- [ ] spellcheck

#### Q12. What is the best way to code the sample shown?
![Sample](https://i.ibb.co/HVwStTZ/sample.png)

- 
```
<details>
   <summary>Parmesan Deviled Eggs</summary>
   <p>These delectable little bites are made with organic eggs, fresh Parmesan, and chopped pine nuts. </p>
</details>
```

- 
```
<h4>▸ Parmesan Deviled Eggs</h4>
<p>These delectable little bites are made with organic eggs, fresh Parmesan, and chopped pine nuts. </p>
```

- 
```
<details open>
   <summary>Parmesan Deviled Eggs</summary>
   <p>These delectable little bites are made with organic eggs, fresh Parmesan, and chopped pine nuts. </p>
</details>
```
^^ CORRECT ^^

- 
```
<details>
	<h4>▸ Parmesan Deviled Eggs</h4>
	<p>These delectable little bites are made with organic eggs, fresh Parmesan, and chopped pine nuts. </p>
</details>	
```


#### Q13. What is the purpose of the `<samp>` element?

- [ ] It connects the web browser to a SA-MP server
- [ ] It identifies enclosed text as a sampler or an example.
- [x] It identifies sample output from a computer program.
- [ ] It uses a simple application messaging protocol to connect the browser to a texting device.

#### Q14. When should you use `<ol>` and `<ul>` elements?

- [x] Use `<ul>` when you want a bulleted list and `<ol>` when you want a numbered list.
- [ ] Use `<ul>` when you have a list of items in which the order of the items matters. Use `<ol>` when you have a list of items that
could go in any order.
- [ ] Use `<ol>` when you want a bulleted list and `<ul>` when you want a numbered list.
- [ ] Use `<ol>` when you have a list of items in which the order of the items matters.

#### Q15. What is the difference between the post and get methods in a form?

- [ ] post is used for sending information to the server. get is used for retrieving form information from the server.
- [ ] get is used for sending information to the server. post is used for retrieving form information from the server.
- [ ] With get, data is included in the form body when send to the server. With post, the data goes through the URL
- [x] With post, data is included in the form body when send to the server. With get, the data goes through the URL

#### Q16. What is the difference between the `<div>` and `<span>` tags?

- [x] <div> is used where a generic block-level tag is needed, while <span> is used where a generic inline tag is needed.
- [ ] <div> is used for major divisions on a page, while <span> is used to span across columns.
- [ ] <div> is the industry-standard default tag, but you could use <span> if you prefer.
- [ ] <div> is used where a generic inline tag is needed, , while <span> is usedwhere a generic block-level tag is needed
  
#### Q17. What should fill the blank in the HTML code bellow?

```
<form method="post" action="mailto:info@linkedin.com" ____="text/plain" >
```
- [x] enctype
- [ ] media
- [ ] type
- [ ] rel

#### Q18. What is the correct markup for tha alt attribute of an image?

-  
```
js
  <img src="cubism.jpg"
   alt="Version of ""Whistler's Mother"" in cubist style">
```  
-  
```
js
  <img src="cubism.jpg"
    alt="Version of "Whistler's Mother" in cubist style">
``` 
-  
```
js
   <img src="cubism.jpg"
     alt='Version of "Whistler\'s Mother" in cubist style'> 
``` 
^^ CORRECT (NOT SURE) ^^

- 
```
js
   <img src="cubism.jpg"
     alt="Version of  \"Whistler's Mother\" in cubist style">
```
  
#### Q19. In the code below, what is the purpose of the id attribute?

```js
<p id="warnig" >Be careful when installing this product.</p>
```

- [x] It establishes that id is a unique identifier in the document, used for styling CSS, scripting, and linking within a webpage.
- [ ] It establishes that id is a unique identifier in the document, used for styling CSS and with Javascript code.
- [ ] It establishes that id may be used for styling CSS several times per page.
- [ ] It establishes that id is a unique identifier in the website, used for styling CSS, scripting, and linking within a webpage.

#### Q20. What is the best semantic markup for the sentence shown?

```markdown
On July 21, 1969, Neil Armstrong said, "One small step for man, one giant leap for mankind."
```

- [x] `<p> On <time datetime="1969-07-21">July 21, 1969</time>, Neil Armstrong said, <q cite="https://www.hq.nasa.gov/alsj/a11l/a11.html">One small step for man, one giant leap for mankind.</q>`
- [ ] `<p> On July 21, 1969, Neil Armstrong said, <q cite="https://www.hq.nasa.gov/alsj/a11l/a11.html">One small step for man, one giant leap for mankind.</q>`
- [ ] `<p> On July 21, 1969, Neil Armstrong said, <q>One small step for man, one giant leap for mankind.</q>`
- [ ] `<p> On <time datetime="07-21-1969">July 21, 1969</time>, Neil Armstrong said, <q cite="https://www.hq.nasa.gov/alsj/a11l/a11.html">One small step for man, one giant leap for mankind.</q>`
  
#### Q21. What should fill the blank in the HTML code below?

```
<a href="https://es.yahoo.com/" hreflang="____" target="_blank">Visita Yahoo</a>
```

- [ ] es
- [ ] es-spanish
- [x] es-es
- [ ] spanish

#### Q22. Review the text in the red box in the image shown. What is the best way to code this in HTML
![Image of  footer](https://i.imgur.com/WaKvL9d.png)

- [ ] ordered list
- [x] unordered list inside a nav element
- [ ] ordered list inside a nav eleme
- [ ] unordered list

#### Q23. What is the best way to code three choices within a form so that the user can select only one item?

- 
```
<label for="example">Make a choice:</label>
<datalist id="example">
	<option value="Choice 1">
	<option value="Choice 2">
	<option value="Choice 3">
</datalist>
```

- 
```
<p>Make a choice:</p>
<input id="choices" name="example" />

<datalist value="choices">
	<option value="Choice 1">
	<option value="Choice 2">
	<option value="Choice 3">
</datalist>
```

- 
```
<label for="example">Make a choice:</label>
<input list="example" id="choices" name="choices" />

<datalist id="choices">
	<option value="Choice 1"> Choice 1</option>
	<option value="Choice 2"> Choice 2</option>
	<option value="Choice 3"> Choice 3</option>
</datalist>
```

- 
```
<label for="example">Make a choice:</label>
<input list="choices" id="example" name="example" />

<datalist id="choices">
	<option value="Choice 1">
	<option value="Choice 2">
	<option value="Choice 3">
</datalist>
```
^^ CORRECT ^^

#### Q24. How do you confirm that a document is written in HTML5?

- [ ] The server wraps the webpage in an HTML5 wrapper.
- [x] Use the "<!DOCTYPE html>" declaration that starts the document.
- [ ] The browser receives encoding from the server to display the document with HTML5.
- [ ] It is enclosed in a "<html>" tag.

#### Q25. What does the code shown below accomplish?

```
<picture>
	<source srcset="image1.jpg" media="(min-width: 1000px)">
	<source srcset="image2.jpg" media="(min-width: 750px)">
	<img src="image3.jpg" />
</picture>
```
	
- [ ] It displays image1.jpg at 1000px and higher, image2.jpg at 750-999px, and image3.jpg at 749px and lower.
- [ ] It displays image1.jps at 1000px and higher and image2.jpg at 750-999px, image3.jpg is a default in case `<picture>` is not supported.
- [x] It displays image1.jpg at 1000px and higher and image2.jpg at 750px and higher, image3.jpg is a default in case `<picture>` is not supported.
- [ ] It displays image1.jpg, image2.jpg and image3.jpg at 1000px and higher.
  
#### Q26. What code will produce the table shown below?

- 
```
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

- 
```
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
^^ CORRECT ^^

- 
```
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

- 
```
<table>
	<columns colspqn="2" style="background-color: yellow">
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

#### Q27. What is the `<hr>`tag typically used for?

- [ ] This tag is depreciated and should not be used.
- [x] It designates a topic shift within a section at the paragraph level.
- [ ] It draws a horizontal line.
- [ ] It designates a shift of topic at the section level.

#### Q28. What should fill the two blanks in the HTML code below?

```
<section itemscope itemtype="http://schema.org/Restaurant">
	<h1 itemprop="name">Nadia's Garden</h1>
	<p itemscope ______ ______>
		<span itemprop="ratingValue">4.5</span> reviews
	</p>
</section>
```

- [ ] `itemprop="aggregateRating" itemref="http://schema.org/AggregateRating"`
- [x] `itemprop="aggregateRating" itemtype="http://schema.org/AggregateRating`
- [ ] `itemid="aggregateRating" itemtype="http://schema.org/AggregateRating`
- [ ] `itemid="aggregateRating" itemref="http://schema.org/AggregateRating`

#### Q29. Which HTML snippet links back to the very top of a webpage?

- 
```
<a id="top"></a> <!-- placed at the top of the page -->  
<a href="#top">back to top</a>
```
^^ CORRECT ^^

- 
```
<a name="top"></a> <!-- placed at the top of the page -->  
<a href="#top">back to top</a>
```

- 
```
<a href="#">back to top</a>  
<a href="#top">back to top</a>
```

- 
```
<button href="#">back to top</button>  
<button href="#top">back to top</button>
```

#### Q30. Which three tags where deprecated in HTML4 but returned to HTML5?

- 
```
<rb>
<rp>
<rt>
```
^^ CORRECT ^^

- 
```
<acronym>
<code>
<wbr>
```

- 
```
<hgroup>
<q>
<wbr>
```

- 
```
<b>
<i>
<u>
```

#### Q31. The "______"tag is used for marking up a short code snippet, while the ______ tag is used for marking up a longer block of code.

- 
```
"<kdb>";
<pre>
```

- 
```
"<pre>";
<code>
```

- 
```
"<kdb>";
<mark>
```

- 
```
"<code>";
<pre>
```
^^ CORRECT ^^

#### Q32. What does the `<label>` tag do?

- [ ] It labels webpages with important information.
- [ ] It visually associates a text label with an interface element.
- [ ] It visually labels from fields.
- [x] It programmatically associates a text label with an interface element.

#### Q33. To get a link to open in a new window or tab, use the ______ attribute.

- [x] _blank
- [ ] _self
- [ ] _new
- [ ] _parent
