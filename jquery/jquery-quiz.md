## jQuery Assessment

#### Q1. What's the difference between these two snippets?

`$('button').on('click', function(){ alert('you clicked the button!'); }); $('button').click(function(){ alert('you clicked the button!'); });`

- Only the second one will work; jQuery does not have a function called .on.
- The second snippet will not function.
- Nothing - .click(function) is shorter way to write .on('click', function) <<<<---Correct
- The first snippet will execute for every button on the page, the second will only apply to the first button

#### Q2. What does the following line of code do?

`jQuery('p')`

- Loads a paragraph tag from a remote server using AJAX
- Aliases jQuery to a variable p
- Selects all paragraphs on the page <<<<---Correct
- Creates a new paragraph tag and inserts it into the body tag

#### Q3. Give the following HTML, how could we use one line to hide or show the button?

`<button class="btn btn-primary" type="submit">Continue to checkout</button>`

- \$('.btn-primary').toggle(); <<<<---Correct
- \$('.btn-primary').showHide();
- \$('.btn-primary').not(':visible').show();
- \$('.btn-primary').css({ display: 'block'});

#### Q4. Working with AJAX, we may run into situations where a piece of code should not be run until after multiple AJAX, calls have completed successfully. Say we need to call two external services for JSON data (a list of students, and a list of classes). And only after retrieving those data will we perform some manipulations on a page. What is the preferred way for dealing with this scenario?

[https://example.com/json-api/students https://example.com/json-api/classes](https://example.com/json-api/students https://example.com/json-api/classes)

- `$.get([ 'https://example.com/json-api/students', 'https://example.com/json-api/classes' ], function(studentRequest, classRequest) { // the rest of the code goes here });`
- `$.when( $.get('https://example.com/json-api/students'), $.get('https://example.com/json-api/classes') ).done(function(studentRequest, classRequest) { // the rest of the code goes here });`
- `$.bind( $.get('https://example.com/json-api/students'), $.get('https://example.com/json-api/classes') ).done(function(studentRequest, classRequest) { // the rest of the code goes here });`
- `$.ajax('https://example.com/json-api/students', { success: function(studentRequest) { $.ajax('https://example.com/json-api/classes', { success: function(classRequest) { // the rest of the code goes here } }); } });` <<<<<-CORRECT !

#### Q5. Given the snippet of HTML below, what is the difference between the two lines that follow it?

<ul>
    <li>Item 1</li>
    <li>Item 2</li>
    <li>Item 3</li>
    <li>Item 4</li>
</ul>

===================

$('ul').find('li').get(2);
$('ul').find('li').eq(2);

- .get() retrieves a DOM element, and can't be chained, eq() retrieves a jQuery object, and can be chained.
- .get() retrieves a jQuery object, and can't be chained, eq() retrieves a DOM element, and can be chained. <-- Correct
- .get() retrieves a jQuery object, and is zero-indexed, eq() retrieves a DOM element, and is 1-indexed.
- .get() retrieves a DOM element, and is zero-indexed, eq() retrieves a jQuery object, and is 1-indexed.

#### Q6. Suppose we want to have an ball created from an HTML element (id=ball) move down and to the right from its original location when clicked, and move back into its original place when finished. Given a starting point of this, which of these snippets would accomplish that goal?

\$('#ball').click(function() {
// Our code goes here
});

- `$(this).animate({ top: '+=100', left: '+=100', }, { duration: 600, complete: function() { $(this).animate({ top: '-=100', left: '-=100', }, 600) } });` <-- Correct

- `$(this).animate({ top: '-=100', left: '-=100', }, 600, function() { $(this).animate({ top: '+=100', left: '+=100', }, 600) } });`
- `$(this).animate({ top: '=100', left: '=100', }, { duration: 600, complete: function() { $(this).animate({ top: 0, left: 0, }, 600) } });`

- `$(this).animate({ top: '100', left: '100', }, 600, function() { $(this).animate({ top: 0, left: 0, }, 600) } });`

#### Q7. Given the following CSS and HTML codes below, how could you apply the success class to the feedback div?

.success {
color: green;
background: #ddffdd;
}

<div class="feedback">
        Thank you for answering this survey.
</div>

- `$('.feedback').hasClass('.success');`
- `$.css('.feedback', '.success')`;
- `$('.feedback').addClass('.success');` <<<<---Correct (you can only have class name without dot in-front of it)
- `$('.feedback').css('.success');`

#### Q8. Below an example page snippet that includes a couple of messages in a list, and a code snippet that retrieves a few hundred messages from a API endpoints using AJAX. How might we add these items to the page snippet in a way that avoids performance problems with DOM insertions?

<div class="message-area">
    <ul class="message-area--list">
        <li>Existing message 1</li>
        <li>Existing message 2</li>
    </ul>
</div>

\$.get('//example.com/api/v1/message')
.done(function(data) {
var tonsOfItems = data.messages;
// add all these messages to a large page
});

- `tonsOfItems.map(function(item) { $('.message-area--list').append('<li>'+item+'</li>'); });` <<<<---Correct

- `var tonsOfListItems = tonsOfItems.map(function(itme)) { return '<li>'+item+'</li>'; }); $('.message-area--list').append(tonsOfListItems.join(''));`

- `Removing the event handlers with JavaScript will be slower than removing them $.each(tonsOfItems, function(idx, item) { $('<li>'+item+'</li>').appendTo($messageList); });`

- `$.each(tonsOfItems, function(idx, item) { $('.message-area--list').append('<li>'+item+'</li>'); });`

#### Q9. What is jQuery?

- jQuery is a bridge between Java and Javascript that makes native apps easier to write.
- jQuery is a plugin for JavaScript that makes database queries easier to write.
- jQuery is a collection of JavaScript functions that makes finding and manipulating elements on a page, AJAX, and other things easier. <<<<---CORRECT !
- jQuery is a Chrome extension that allows users to create their own extensions with just a few lines of JavaScript.

#### Q10. We want to create a new jQuery plugin called linkUpdater that can be chained onto other jQuery selector like a normal plugin. It should updates all the links in the referenced collection so they open in new windows or tabs. Below is the first cut. What is one problem with this plugin?

"user strict";
\$.linkUpdater = function() {
this.find('a').attr('target', '\_blank');
}
) )( jQuery );

- this needs to be wrapped, like \$(this), in order to be chained in a plugin.
- jQuery plugins can't be safety authored in strict mode.
- In order to be used by other code, plugins need to be added to the global namespace, not wrapped in
  function expression.
- Our plugin should extend jQuery.fn, not jQuery itself. <<<---CORRECT !

#### Q11. Generally speaking, when used on a web page, how should jQuery be installed, and why?

- Just before the closing body tag, because we want to avoid blocking other resources from loading, and we use the ready method to make sure our code fires after the DOM is ready <<<<---CORRECT!
- Using the highest version number possible because only jQuery 3 and up are compatible with Internet Explorer 7
- In the head tag because we want jQuery available as soon as possible
- From a CDN because we want to be able to use jQuery online or offline

#### Q12. Given the following HTML, How could we make this button disappear from the page using jQuery?

```html
<button>class="btn btn-primary" type="submit">Continue to checkout</button>
```

- \$('.btn-primary').hide(); <<<---CORRECT
- \$('.btn-primary:visible').not();
- \$('.btn-primary').visibility(false);
- \$('.btn-primary').show(false);

#### Q13. What is the difference between $('header').html() and $('header').text()?

- $('header').html() returns the inner HTML of the header. $('header').text() returns only the text <<<<--CORRECT
- $('header').html() returns only the HTML tags used, without the text. $('header').text() returns only the text
- $('header').html() strips all HTML from the header. $('header').text() always returns an empty string.
- $('header').html() returns all headers in an HTML document. $('header').text() the first line of a text file.

#### Q14. When writing jQuery plugins, we often provide default options that may be overridden by the end user. What jQuery function is most useful for this purpose?

- \$.extend <-- Correct
- \$.clone
- \$.fn.extend
- \$.merge

#### Q15. There are times when you might want to programmatically trigger an event, instead of simply reacting to user input directly. Given this markup, Which choice will NOT cause a click event to the select box when the button is clicked?

<article>
    <div>
      Here's a button you can click: <button class="btn">Click Me</button>
    </div>   
    <form>
        <p>
            Further down the page, there's a select box.
        </p>
        <select>
            <option value="1">One</option>
            <option value="2">One</option>
            <option value="3">One</option>
            <option value="4">One</option>
        </select>
    </form>    
</article>

- `$('button').on('click.myApp', (function() { $('input[type=select]').trigger('click'); });` <<<<<----CORRECT ! \*\*\*see option 3

- `$('button').on('click', (function() { $('input[type=select]').click()); });`

- `$('button').trigger(function() { $('input[type=select]').click(); });` <-- I think this may be more correct https://api.jquery.com/trigger/

- `$('button').click(function() { $('input[type=select]').click(); });`

#### Q16. You have an absolutely positioned element inside a relatively positioned parent element, and you want to animate that element within its parent element. What jQuery function is most useful for finding the initial coordinates of the .animate-me?

```jQuery
<style>
	.parent {
		position: relative;
		top: 3em;
		width: 50%;
		min-height: 50vh;
		margin: 0 auto;
	}

	.animate-me {
		position: absolute;
		top: 40px;
		right: 30px;
	}
</style>

<div class="parent">
	<div class="animate-me">
		This box will move!
	</div>
</div>

```

- `$('.animate-me').offset();`<-- Correct relative to Document
- `$('.animate-me').each();`
- `$('.animate-me').position();` <-- WRONG relative to parent
- `$('.animate-me').offsetParent();`

#### Q17. You want to work with AJAX using a Promise-like interface instead of nested callback functions. What jQuery API should you use?

- `jQuery.sub`
- `jQuery.ajaxTransport`
- `jQuery.Deferred` <-- Correct
- `jQuery.proxy`

#### Q18. What is tricky about jQuery's nth- filters (:nth-child, :nth-of-type, etc.) relative to other filters?

- Referring to lists of items, they are 1-indexed (like CSS), not 0-indexed (like JavaScript). <-- Correct
- They don't return the jQuery object, and cannot be chained.
- They can return the wrong items if the DOM was recently manipulated.
- They are not part of CSS, so they don't get the performance benefits of passing through the document.querySelectorAll.

#### Q19. jQuery's AJAX functions return objects that implement the Promise API. As a result, you can chain promises and avoid nested callbacks. What does that look like?

- Option 1 <-- Correct

```jQuery
$.get('hhttp://httpbin.org/delay/2')
	.then(function(response) {
		// Data from first GET is here as 'response'
		return $.get('http://httpbin.org/delay/2');
	})
	.then(function(response) {
		// Data from second GET is here as 'response'
	});
```

- Option 2

```jQuery
$.get('hhttp://httpbin.org/delay/2')
	.catch(function(response) {
		// Data from first GET is here as 'response'
		return $.get('http://httpbin.org/delay/2');
	})
	.done(function(response) {
		// Data from second GET is here as 'response'
	});
```

- Option 3

```jQuery
$.get('hhttp://httpbin.org/delay/2', function(response1) {
	// Data from first GET is here as 'response1'

	$.get('http://httpbin.org/delay/2', function(response2) {
		// Data from second GET is here as 'response2'
	});
});
```

- Option 4

```jQuery
$.get('hhttp://httpbin.org/delay/2')
	.then(function(response) {
		// Data from first GET is here as 'response'
		return response;
	})
	.get('http://httpbin.org/delay/2', function(response) {
		// Data from second GET is here as 'response'
	});
```

#### Q20. You want to have a ball that is created from an HTML element (id=ball) move down and to the right of its original location when clicked, and move back to its original place when finished. What snippet, added to the code below, would do this?

```jQuery
$('#ball').click(function() {
	// Our code goes here
});
```

- Option 1

```jQuery
$(this).animate({
	top: '-=100',
	left: '-=100',
}, 600, function() {
	$(this).animate({
	top:  '+=100',
	left: '+=100',
	}, 600)
});
```

- Option 2 <-- Correct

```jQuery
$(this).animate({
	top: '+=100',
	left: '+=100',
}, {
	duration: 600,
	complete: function() {
	$(this).animate({
	top:  '-=100',
	left: '-=100',
	}, 600)
	}
});
```

- Option 3

```jQuery
$(this).animate({
	top: 100,
	left: 100,
}, 600, function() {
	$(this).animate({
	top:  0,
	left: 0,
	}, 600)
});
```

- Option 4

```jQuery
$(this).animate({
	top: 100,
	left: 100,
}, {
	duration: 600,
	complete: function() {
	$(this).animate({
	top:  0,
	left: 0,
	}, 600)
	}
});
```

#### Q21. The way `.wrap()` works is sometimes missunderstood. Given the DOM and jQuery snippets below, what does the modified DOM snippet look like?

```jQuery
<div id="container">
	<div class="item">Here's an item</div>
</div>

$('#container').wrap('<div class="wrapper"></div>').css('border', '2px solid red');
```

- Option 1

```jQuery
<div class="wrapper" style="border: 2px solid red;">
	<div id="container">
		<div class="item">Here's an item</div>
	</div>
</div>
```

- Option 2 <-- Correct

```jQuery
<div class="wrapper">
	<div id="container" style="border: 2px solid red;">
		<div class="item">Here's an item</div>
	</div>
</div>
```

- Option 3

```jQuery
<div id="container" style="border: 2px solid red;">
	<div class="wrapper">
		<div class="item">Here's an item</div>
	</div>
</div>
```

- Option 4

```jQuery
<div id="container">
	<div class="wrapper" style="border: 2px solid red;">
		<div class="item">Here's an item</div>
	</div>
</div>
```

#### Q22. How can you select the following blockquote AND the list in a single call to jQuery() without chaining?

```jQuery
<div class="quotes">
	<blockquote data-favorite="false">A quote</blockquote>
	<blockquote data-favorite="false">A favorite</blockquote>
	<blockquote data-favorite="false">A quote</blockquote>
	<blockquote data-favorite="false">A quote</blockquote>
</div>

<ul class="menu-first">
	<li>Item 1</li>
	<li>Item 2</li>
	<li>Item 3</li>
	<li>Item 4</li>
</ul>
```

- `$('.quotes + .menu-first')`
- `$('.quotes .menu-first')`
- `$('.quotes, .menu-first')` <-- correct
- `$('.quotes' + '.menu-first')`

#### Q23. Given the CSS and HTML code below, how could you apply the success class to the feedback div?

```jQuery
.succes {
	colour: green;
	background: #ddffdd
}

<div class="feedback">
	Thank you for answering this survey.
</div>
```

- `$('.feedback').hasClass('.success');`
- `$('.feedback').addClass('.success');` <-- most correct however it should be ('success')
- `$.css('.feedback', '.success');`
- `$('.feedback').css('.success');`

#### Q24. Effects like show, hide, fadIn, and fadeOut can be called with no arguments, but can also take arguments for how long they should last. Which is NOT a duration argument supported by these functions?

- [ ] "fast"
- [x] "extreme" <-- Correct
- [ ] 2000
- [ ] "slow"

#### Q25. Though jQuery offers visual effects, it is considered a best practice to use CSS to se up different states triggered by classes, where it makes sense. What's the easiest way to enable and disable a class bounce on an element with the ID dialog?

- [ ] `$('#dialog').classToggle('bounce')`
- [ ] `$('#dialog.bounce').removeClass().addClass()`
- [ ] `$(#dialog').addOrRemoveClass('bounce')`
- [x] `$(#dialog').toggleClass('bounce') <-- Correct`

#### Q26. What is the main difference between selectors and filters?

- [ ] Selectors are used to refine the content that filters have been applied to.
- [x] Selectors are used to find and select content in a page. Filters are used to refine the results of selectors. <-- Correct
- [ ] Filters are used to remove content from the page. Selectors are used to add content to the page
- [ ] There is no real difference. They are both used to build up lists of page content.

#### Q27. You want to create a custom right-click menu. How might you start the code?

- [ ] `$('#canvas').on('click.right', function(){ console.log('Handled a right-click') });`
- [ ] `$('#canvas').on('contextual', function(){ console.log('Handled a right-click') });`
- [x] `$('#canvas').on('contextmenu', function(){ console.log('Handled a right-click') });`
- [ ] `$('#canvas').on('rightclick', function(){ console.log('Handled a right-click') });`

#### Q28. What is the correct way to check how many paragraphs exist on a page using jQuery?

- [ ] `$('p').count()`
- [x] `$('p').length` <-- Correct
- [ ] `$('*').find('p')`
- [ ] `$('p').length()`
