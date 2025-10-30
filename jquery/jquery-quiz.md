## jQuery

#### Q1. What is the difference between these two snippets?

```js
$('button').on('click', function () {
  alert('you clicked the button!');
});
$('button').click(function () {
  alert('you clicked the button!');
});
```

- [ ] Only the second one will work; jQuery does not have a function called `.on`.
- [ ] The second snippet will not function.
- [x] Nothing `.click(function)` is shorter way to write `.on('click', function)`.
- [ ] The first snippet will execute for every button on the page, the second will only apply to the first button.

#### Q2. What does the following line of code do?

`jQuery('p')`

- [ ] Loads a paragraph tag from a remote server using AJAX
- [ ] Aliases jQuery to a variable p
- [x] Selects all paragraphs on the page
- [ ] Creates a new paragraph tag and inserts it into the body tag

#### Q3. Given the following HTML, how could we use one line to hide or show the button?

```html
<button class="btn btn-primary" type="submit">Continue to checkout</button>
```

- [x] `$('.btn-primary').toggle();`
- [ ] `$('.btn-primary').showHide();`
- [ ] `$('.btn-primary').not(':visible').show();`
- [ ] `$('.btn-primary').css({ display: 'block'});`

#### Q4. Working with AJAX, we may run into situations where a piece of code should not be run until after multiple AJAX calls have completed successfully. Say we need to call two external services for JSON data (a list of students, and a list of classes). And only after retrieving those data will we perform some manipulations on a page. What is the preferred way for dealing with this scenario?

`https://example.com/json-api/students`  
`https://example.com/json-api/classes`

- [ ] A

```js
$.get(
  ['https://example.com/json-api/students', 'https://example.com/json-api/classes'],
  function (studentRequest, classRequest) {
    // the rest of the code goes here
  },
);
```

- [ ] B

```js
$.when(
  $.get('https://example.com/json-api/students'),
  $.get('https://example.com/json-api/classes'),
).done(function (studentRequest, classRequest) {
  // the rest of the code goes here
});
```

- [ ] C

```js
$.bind(
  $.get('https://example.com/json-api/students'),
  $.get('https://example.com/json-api/classes'),
).done(function (studentRequest, classRequest) {
  // the rest of the code goes here
});
```

- [x] D

```js
$.ajax('https://example.com/json-api/students', {
  success: function (studentRequest) {
    $.ajax('https://example.com/json-api/classes', {
      success: function (classRequest) {
        // the rest of the code goes here
      },
    });
  },
});
```

#### Q5. Given the snippet of HTML below, what is the difference between the two lines that follow it?

```html
<ul>
  <li>Item 1</li>
  <li>Item 2</li>
  <li>Item 3</li>
  <li>Item 4</li>
</ul>
```

```js
$('ul').find('li').get(2);
$('ul').find('li').eq(2);
```

- [x] .get() retrieves a DOM element, and can't be chained, eq() retrieves a jQuery object, and can be chained.
- [ ] .get() retrieves a jQuery object, and can't be chained, eq() retrieves a DOM element, and can be chained.
- [ ] .get() retrieves a jQuery object, and is zero-indexed, eq() retrieves a DOM element, and is 1-indexed.
- [ ] .get() retrieves a DOM element, and is zero-indexed, eq() retrieves a jQuery object, and is 1-indexed.

#### Q6. Suppose we want to have a ball created from an HTML element (id=ball) move down and to the right from its original location when clicked, and move back into its original place when finished. Given a starting point of this, which of these snippets would accomplish that goal?

```js
$('#ball').click(function () {
  // Our code goes here
});
```

- [x] A

```js
$(this).animate(
  { top: '+=100', left: '+=100' },
  {
    duration: 600,
    complete: function () {
      $(this).animate({ top: '-=100', left: '-=100' }, 600);
    },
  },
);
```

- [ ] B

```js
$(this).animate({ top: '-=100', left: '-=100' }, 600, function () {
  $(this).animate({ top: '+=100', left: '+=100' }, 600);
});
```

- [ ] C

```js
$(this).animate(
  { top: '=100', left: '=100' },
  {
    duration: 600,
    complete: function () {
      $(this).animate({ top: 0, left: 0 }, 600);
    },
  },
);
```

- [ ] D

```js
$(this).animate({ top: '100', left: '100' }, 600, function () {
  $(this).animate({ top: 0, left: 0 }, 600);
});
```

#### Q7. Given the following CSS and HTML codes below, how could you apply the success class to the feedback div?

```css
.success {
  color: green;
  background: #ddffdd;
}
```

```html
<div class="feedback">Thank you for answering this survey.</div>
```

- [ ] `$('.feedback').hasClass('.success');`
- [ ] `$.css('.feedback', '.success')`;
- [x] `$('.feedback').addClass('success');`
- [ ] `$('.feedback').css('.success');`

#### Q8. The following page snippet includes a couple of messages in a list, and a code snippet that retrieves a few hundred messages from an API endpoint using AJAX. How can you add these new items to the .message-area--list element in the most performant way?

```html
<div class="message-area">
  <ul class="message-area--list">
    <li>Existing message 1</li>
    <li>Existing message 2</li>
  </ul>
</div>

$.get('//example.com/api/v1/message').done(function (data) { var tonsOfItems = data.messages; // add
all these messages to a large page });
```

- [ ] A

```js
tonsOfItems.map(function (item) {
  $('.message-area--list').append('<li>' + item + '</li>');
});
```

- [x] B

```js
var tonsOfListItems = tonsOfItems.map(function (item) {
  return '<li>' + item + '</li>';
});
$('.message-area--list').append(tonsOfListItems.join(''));
```

- [ ] C

```js
CSS.$messageList = $('.message-area--list');
$.each(tonsOfItems, function (idx, item) {
  $('<li>' + item + '</li>').appendTo($messageList);
});
```

- [ ] D

```js
$.each(tonsOfItems, function (idx, item) {
  $('.message-area--list').append('<li>' + item + '</li>');
});
```

#### Q9. What is jQuery?

- [ ] jQuery is a bridge between Java and Javascript that makes native apps easier to write.
- [ ] jQuery is a plugin for JavaScript that makes database queries easier to write.
- [x] jQuery is a collection of JavaScript functions that makes finding and manipulating elements on a page, AJAX, and other things easier.
- [ ] jQuery is a Chrome extension that allows users to create their own extensions with just a few lines of JavaScript.

#### Q10. We want to create a new jQuery plugin called linkUpdater that can be chained onto other jQuery selector like a normal plugin. It should update all the links in the referenced collection so they open in new windows or tabs. Below is the first cut. What is one problem with this plugin?

```js
'user strict';
($.linkUpdater = function () {
  this.find('a').attr('target', '_blank');
})(jQuery);
```

- [ ] this needs to be wrapped, like `$(this)`, in order to be chained in a plugin.
- [ ] jQuery plugins can't be safely authored in strict mode.
- [ ] In order to be used by other code, plugins need to be added to the global namespace, not wrapped in a function expression.
- [x] Our plugin should extend jQuery.fn, not jQuery itself.

#### Q11. Generally speaking, when used on a web page, how should jQuery be installed, and why?

- [x] Just before the closing body tag, because we want to avoid blocking other resources from loading, and we use the ready method to make sure our code fires after the DOM is ready
- [ ] Using the highest version number possible because only jQuery 3 and up are compatible with Internet Explorer 7
- [ ] In the head tag because we want jQuery available as soon as possible
- [ ] From a CDN because we want to be able to use jQuery online or offline

#### Q12. Given the following HTML, how could we make this button disappear from the page using jQuery?

```html
<button class="btn btn-primary" type="submit">Continue to checkout</button>
```

- [x] `$('.btn-primary').hide();`
- [ ] `$('.btn-primary:visible').not();`
- [ ] `$('.btn-primary').visibility(false);`
- [ ] `$('.btn-primary').show(false);`

#### Q13. What is the difference between `$('header').html()` and `$('header').text()`?

- [x] `$('header').html()` returns the inner HTML of the header. `$('header').text()` returns only the text
- [ ] `$('header').html()` returns only the HTML tags used, without the text. `$('header').text()` returns only the text
- [ ] `$('header').html()` strips all HTML from the header. `$('header').text()` always returns an empty string.
- [ ] `$('header').html()` returns all headers in an HTML document. `$('header').text()` the first line of a text file.

#### Q14. When writing jQuery plugins, we often provide default options that may be overridden by the end user. What jQuery function is most useful for this purpose?

- [x] \$.extend
- [ ] \$.clone
- [ ] \$.fn.extend
- [ ] \$.merge

#### Q15. There are times when you might want to programmatically trigger an event, instead of simply reacting to user input directly. Given this markup, Which choice will NOT cause a click event to the select box when the button is clicked?

```html
<article>
  <div>Here's a button you can click: <button class="btn">Click Me</button></div>
  <form>
    <p>Further down the page, there's a select box.</p>
    <select>
      <option value="1">One</option>
      <option value="2">One</option>
      <option value="3">One</option>
      <option value="4">One</option>
    </select>
  </form>
</article>
```

- [x] `$('button').on('click.myApp', (function() { $('input[type=select]').trigger('click'); });`
- [ ] `$('button').on('click', (function() { $('input[type=select]').click()); });`
- [ ] `$('button').trigger(function() { $('input[type=select]').click(); });`
- [ ] `$('button').click(function() { $('input[type=select]').click(); });`

#### Q16. You have an absolutely positioned element inside a relatively positioned parent element, and you want to animate that element within its parent element. What jQuery function is most useful for finding the initial coordinates of the `.animate-me`?

```html
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
  <div class="animate-me">This box will move!</div>
</div>
```

- [x] `$('.animate-me').offset();`
- [ ] `$('.animate-me').each();`
- [ ] `$('.animate-me').position();`
- [ ] `$('.animate-me').offsetParent();`

#### Q17. You want to work with AJAX using a Promise-like interface instead of nested callback functions. What jQuery API should you use?

- [ ] `jQuery.sub`
- [ ] `jQuery.ajaxTransport`
- [x] `jQuery.Deferred`
- [ ] `jQuery.proxy`

#### Q18. What is tricky about jQuery's nth- filters (:nth-child, :nth-of-type, etc.) relative to other filters?

- [x] Referring to lists of items, they are 1-indexed (like CSS), not 0-indexed (like JavaScript).
- [ ] They don't return the jQuery object, and cannot be chained.
- [ ] They can return the wrong items if the DOM was recently manipulated.
- [ ] They are not part of CSS, so they don't get the performance benefits of passing through the `document.querySelectorAll`.

#### Q19. jQuery's AJAX functions return objects that implement the Promise API. As a result, you can chain promises and avoid nested callbacks. What does that look like?

- [x] A

```js
$.get('http://httpbin.org/delay/2')
  .then(function (response) {
    // Data from first GET is here as 'response'
    return $.get('http://httpbin.org/delay/2');
  })
  .then(function (response) {
    // Data from second GET is here as 'response'
  });
```

- [ ] B

```js
$.get('http://httpbin.org/delay/2')
  .catch(function (response) {
    // Data from first GET is here as 'response'
    return $.get('http://httpbin.org/delay/2');
  })
  .done(function (response) {
    // Data from second GET is here as 'response'
  });
```

- [ ] C

```js
$.get('http://httpbin.org/delay/2', function (response1) {
  // Data from first GET is here as 'response1'

  $.get('http://httpbin.org/delay/2', function (response2) {
    // Data from second GET is here as 'response2'
  });
});
```

- [ ] D

```js
$.get('http://httpbin.org/delay/2')
  .then(function (response) {
    // Data from first GET is here as 'response'
    return response;
  })
  .get('http://httpbin.org/delay/2', function (response) {
    // Data from second GET is here as 'response'
  });
```

#### Q20. You want to have a ball that is created from an HTML element (id=ball) move down and to the right of its original location when clicked, and move back to its original place when finished. What snippet, added to the code below, would do this?

```js
$('#ball').click(function () {
  // Our code goes here
});
```

- [ ] A

```js
$(this).animate(
  {
    top: '-=100',
    left: '-=100',
  },
  600,
  function () {
    $(this).animate(
      {
        top: '+=100',
        left: '+=100',
      },
      600,
    );
  },
);
```

- [x] B

```js
$(this).animate(
  {
    top: '+=100',
    left: '+=100',
  },
  {
    duration: 600,
    complete: function () {
      $(this).animate(
        {
          top: '-=100',
          left: '-=100',
        },
        600,
      );
    },
  },
);
```

- [ ] C

```js
$(this).animate(
  {
    top: 100,
    left: 100,
  },
  600,
  function () {
    $(this).animate(
      {
        top: 0,
        left: 0,
      },
      600,
    );
  },
);
```

- [ ] D

```js
$(this).animate(
  {
    top: 100,
    left: 100,
  },
  {
    duration: 600,
    complete: function () {
      $(this).animate(
        {
          top: 0,
          left: 0,
        },
        600,
      );
    },
  },
);
```

#### Q21. The way `.wrap()` works is sometimes misunderstood. Given the DOM and jQuery snippets below, what does the modified DOM snippet look like?

```html
<div id="container">
  <div class="item">Here's an item</div>
</div>
```

```js
$('#container').wrap('<div class="wrapper"></div>').css('border', '2px solid red');
```

- [ ] A

```html
<div class="wrapper" style="border: 2px solid red;">
  <div id="container">
    <div class="item">Here's an item</div>
  </div>
</div>
```

- [x] B

```html
<div class="wrapper">
  <div id="container" style="border: 2px solid red;">
    <div class="item">Here's an item</div>
  </div>
</div>
```

- [ ] C

```html
<div id="container" style="border: 2px solid red;">
  <div class="wrapper">
    <div class="item">Here's an item</div>
  </div>
</div>
```

- [ ] D

```html
<div id="container">
  <div class="wrapper" style="border: 2px solid red;">
    <div class="item">Here's an item</div>
  </div>
</div>
```

#### Q22. How can you select the following blockquote AND the list in a single call to jQuery() without chaining?

```html
<div class="quotes">
  <blockquote data-favorite="false">A quote</blockquote>
  <blockquote data-favorite="true">A favorite quote</blockquote>
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

- [ ] `$('.quotes + .menu-first')`
- [ ] `$('.quotes .menu-first')`
- [x] `$('.quotes, .menu-first')`
- [ ] `$('.quotes' + '.menu-first')`

#### Q23. Effects like show, hide, fadIn, and fadeOut can be called with no arguments, but can also take arguments for how long they should last. Which is NOT a duration argument supported by these functions?

- [ ] "fast"
- [x] "extreme"
- [ ] 2000
- [ ] "slow"

#### Q24. Though jQuery offers visual effects, it is considered a best practice to use CSS to set up different states triggered by classes, where it makes sense. What's the easiest way to enable and disable a class bounce on an element with the ID dialog?

- [ ] `$('#dialog').classToggle('bounce')`
- [ ] `$('#dialog.bounce').removeClass().addClass()`
- [ ] `$('#dialog').addOrRemoveClass('bounce')`
- [x] `$('#dialog').toggleClass('bounce')`

#### Q25. What is the main difference between selectors and filters?

- [ ] Selectors are used to refine the content that filters have been applied to.
- [x] Selectors are used to find and select content in a page. Filters are used to refine the results of selectors.
- [ ] Filters are used to remove content from the page. Selectors are used to add content to the page
- [ ] There is no real difference. They are both used to build up lists of page content.

#### Q26. You want to create a custom right-click menu. How might you start the code?

- [ ] `$('#canvas').on('click.right', function(){ console.log('Handled a right-click') });`
- [ ] `$('#canvas').on('contextual', function(){ console.log('Handled a right-click') });`
- [x] `$('#canvas').on('contextmenu', function(){ console.log('Handled a right-click') });`
- [ ] `$('#canvas').on('rightclick', function(){ console.log('Handled a right-click') });`

#### Q27. What is the correct way to check how many paragraphs exist on a page using jQuery?

- [ ] `$('p').count()`
- [x] `$('p').length`
- [ ] `$('*').find('p')`
- [ ] `$('p').length()`

#### Q28. As with many areas of JavaScript, keeping track of the meaning of `this` is important and sometimes tricky. What does `this` mean at each of the two points in this custom plugin snippet?

```js
$.fn.customPlugin = function () {
  // Point 1

  return this.each(function () {
    // Point 2
  });
};
$(document).customPlugin();
```

- [ ] At Point 1, `this` means a jQuery object. At Point 2, it means a DOM element.
- [ ] In this case, they mean the same thing: a jQuery object.
- [ ] In this case, they mean the same thing: a DOM element.
- [x] At Point 1, `this` means a DOM element. At Point 2, it means a jQuery object.

#### Q29. How can you make the first list item bold and the next item oblique, in a single statement chain?

```html
<ul class="menu-first">
  <li>Item 1</li>
  <li>Item 2</li>
  <li>Item 3</li>
  <li>Item 4</li>
</ul>
```

- [ ] A

```js
$('.menu-first > li').eq(0).css('font-weight', 'bold').eq(1).css('font-style', 'oblique');
```

- [ ] B

```js
$('.menu-first > li').first().css('font-weight', 'bold').after().css('font-style', 'oblique');
```

- [ ] C

```js
$('.menu-first > li').first().css('font-weight', 'bold').second().css('font-style', 'oblique');
```

- [x] D

```js
$('.menu-first > li').eq(0).css('font-weight', 'bold').next().css('font-style', 'oblique');
```

#### Q30. Which CSS selectors can you NOT use in jQuery?

- [ ] You cannot use multiple class selectors such as `.class1.class2`.
- [ ] You cannot use pseudo-classes such as `:not` or `:last-of-type`.
- [ ] You cannot use IDs and classes together, such as `#element.class`.
- [x] None. All CSS selectors are compatible in jQuery.

#### Q31. Starting with some DOM elements in the nested structure below, you assign listeners for the same event to a child element and one of the parents using the JavaScript that follows. You want to ensure that when `.leaf` is clicked, only its event handler will be fired, instead of the click bubbling up and also firing the parent's click handler. What do you need to add to its handler function?

```html
<ul class="items" id="main-menu">
  <li>
    Item 1
    <ul>
      <li class="leaf">Sub Item 1</li>
      <li>Sub Item 2</li>
    </ul>
  </li>
</ul>
```

```js
$('.leaf').click(function (event) {
  console.log('Sub Item 1 got a click');
});
$('#main-menu').click(function (event) {
  console.log('Main menu got a click');
});
```

- [ ] `event.capture();`
- [x] `event.stopPropagation();`
- [ ] `event.preventDefault();`
- [ ] `event.stop();`

[Difference between preventDefault, stopPropagation & return false](https://www.educative.io/answers/difference-between-preventdefault-stoppropagation-return-false)

#### Q32. Using event delegation, you can listen for events on a lot of different items without having to attach separate listeners to each one. But there are times when you may want to check the type of item receiving the event before doing anything, such as checking if an image was clicked versus a text field. Given the starter code below, which choice shows what jQuery provides to help with that process?

```html
<div id="sidebar">
  <img src="fancy-button.png" alt="Pick Me" />
  <input type="text" placeholder="Fill in something" />
</div>
```

```js
$('#sidebar').click(function (evt) {
  var $target = $(evt.target);

  // What goes here?
});
```

- [ ] `$($target.get(0) + ':image')`
- [ ] `$('img').is($target)`
- [ ] `$target.filter('img')`
- [x] `$target.is('img')`

#### Q33. There are many ways to create elements that can be added to the page. Which answer is NOT one of those ways, assuming you have the following on the page?

```html
<div id="elements"></div>
```

- [ ] A

```js
$('#elements').append($('<p class="appended">As an HTML string</p>'));
```

- [ ] B

```js
var p = document.createElement('p');
var text = document.createTextNode('As a DOM element');
p.appendChild(text);
$('#elements').append(p);
```

- [x] C

```js
$('#elements').append(<p class="appended">As a JSX object</p>);
```

- [ ] D

```js
$('#elements').append(
  $('<p>', {
    class: 'appended',
    text: 'As an attribute object',
  }),
);
```

#### Q34. The `.addClass()` and `.removeClass()` methods can accept functions as arguments. What does this function do?

```js
$('#menu').addClass(function () {
  return $('body').attr('class');
});
```

- [ ] It adds the first class found on the body element to the #menu element.
- [ ] It adds all classes found on the #menu element to the body tag.
- [ ] It replaces any classes on the #menu element with all classes from the body tag.
- [x] It adds all classes found on the body element to the #menu element.

#### Q35. You're working on a site that uses an old version of jQuery, and you want to update to a newer version. What's the most efficient way to do so?

- [ ] Install the newer version of jQuery, go through each script one by one, and fix what looks broken.
- [ ] Read the change notes for the newer version of jQuery, fix all scripts, install the newer version, and fix anything that remains broken.
- [x] Install the newer version of jQuery as well as its Migrate plugin, fix all warnings, and uninstall the Migrate plugin.
- [ ] Install the newer version of jQuery at the same time, and use `jQuery.noConflict()` on pages that need the older version.

#### Q36. Let's say you have a page with just one link on it. How can you change the anchor tag so it links to example.com?

- [ ] `$('a').attribute('href', 'http://www.example.com')`
- [x] `$('a').attr('href', 'http://www.example.com')`
- [ ] `$('a').data('href', 'http://www.example.com')`
- [ ] `$('a').href('http://www.example.com')`

#### Q37. What does `$()` mean in jQuery?

- [x] It is an alias to the main core method of jQuery itself—the same as writing jQuery().
- [ ] It is a utility function that selects the first element from the document.
- [ ] It is a shorter way to write `document.getElementById()`.
- [ ] It is a utility function that selects the last element from the document.

#### Q38. Along with DOM traversal and manipulation, jQuery offers several general-purpose helper functions that fill in some JavaScript gaps, especially before ES2015. Which is NOT a jQuery utility function?

- [ ] `jQuery.each`, a general purpose iterator for looping over arrays or objects
- [ ] `jQuery.isNumeric`, which can check whether its argument is, or looks like, a number
- [ ] `jQuery.extend`, which can merge objects and make complete deep copies of objects
- [x] `jQuery.isMobile`, which can tell whether the user is using a mobile browser

#### Q39. Given this set of checkboxes, how can you select the ones that have the phrase "sun" as part of the value?

```html
<input type="checkbox" name="artists[]" value="sun-ra" />
<input type="checkbox" name="artists[]" value="otis-redding" />
<input type="checkbox" name="artists[]" value="captain-beefheart" />
<input type="checkbox" name="artists[]" value="king-sunny-ade" />
<input type="checkbox" name="artists[]" value="weather-report" />
```

- [ ] `$('checkbox').val(/sun/);`
- [x] `$('input[value*="sun"]');`
- [ ] `$('input[value|="sun"]');`
- [ ] `$('input:checkbox').attr('value', '*sun*');`

#### Q40. How can you get an AJAX request to go through without triggering any of jQuery's AJAX events?

- [ ] Set the type option to "none".
- [ ] Set the processData option to false.
- [ ] Set a success callback that returns false.
- [x] Set the option "global" to false.

#### Q41. How do you change the current value of a text field with the class `.form-item` to "555-1212"?

- [ ] `$.val('.form-item', '555-1212');`
- [x] `$('.form-item').val('555-1212');`
- [ ] `$('.form-item').data('value', '555-1212');`
- [ ] `$('.form-item').set('value', '555-1212');`

#### Q42. How would you fire a callback when any AJAX request on a page has completed?

- [ ] `$('body').ajaxComplete(function() { console.count('An AJAX request completed'); });`
- [ ] `$(document).on('ajax-complete', function() { console.count('An AJAX request completed'); });`
- [ ] `$('body').on('ajaxComplete', function() { console.count('An AJAX request completed'); });`
- [x] `$(document).ajaxComplete(function() { console.count('An AJAX request completed'); });`

[Source: ajaxComplete](https://www.w3schools.com/jquery/ajax_ajaxcomplete.asp)
**Explanation**: `Note: As of jQuery version 1.8, this method should only be attached to document.`

#### Q43. Given this set of checkboxes, how can you select the one with the value "blimp"?

```html
<input type="checkbox" name="songs[]" value="satisfaction" />
<input type="checkbox" name="songs[]" value="respect" />
<input type="checkbox" name="songs[]" value="blimp" />
<input type="checkbox" name="songs[]" value="saturn" />
<input type="checkbox" name="songs[]" value="penguins" />
```

- [x] `$('input[value="blimp"]');`
- [ ] `$('input[value!="blimp"]');`
- [ ] `$('checkbox').val('blimp');`
- [ ] `$('input:checkbox').attr('value', 'blimp');`

#### Q44. Given this snippet of HTML and jQuery code, what does the jQuery do?

```html
<ul class="menu">
  <li><a href="#" class="active">Home</a></li>
  <li><a href="#">Page 2</a></li>
</ul>
<ul class="active submenu">
  <li><a href="#">Subpage 1</a></li>
  <li><a href="#">Subpage 2</a></li>
</ul>
```

```js
var m = $('.menu'),
  sm = $('.submenu');
m.add(sm);
m.css('font-weight', 'bold');
```

- [ ] It makes all the menu items bold.
- [ ] It throws an exception on line 3.
- [x] It makes the first set of menu items, not the second, bold.
- [ ] It makes the second set of menu items, not the first, bold.

#### Q45. You want to take a block of type and animate it to a larger size with jQuery. The following HTML and JavaScript behaves strangely. What is the issue?

```html
<div id="type" style="font: 1em/1.5 helvetica, arial, sans-serif; background: #ffc; padding: 0">
  Animate me!
</div>
```

```js
$('#type').animate(
  {
    fontSize: '+=1em',
  },
  3000,
);
```

- [ ] jQuery does not support ems and will make the type 1 pixel larger instead of 1 em larger.
- [ ] jQuery cannot override CSS in a style attribute, so the font size will not change.
- [ ] The font size was set with a shorthand property, so jQuery will not animate the font size at all.
- [x] The font size was set with a shorthand property, so jQuery will start the animation from 0 instead of from 1 em.

#### Q46. When using the `clone()` function to duplicate an element, what is one of the main concerns your code needs to watch out for?

- [ ] The `clone()` function may ignore data attributes on the original elements.
- [x] The `clone()` function may result in elements with duplicate ID attributes.
- [ ] The `clone()` function may remove CSS classes from the cloned elements.
- [ ] The `clone()` function may not respect the attribute order of the original elements.

#### Q47. When incorporating a plugin into a project, what are the important steps for basic installation and usage?

- [x] The jQuery script tag must come first, followed by the plugin, followed by your custom scripts, all preferably at or near the bottom of the page.
- [ ] Your custom scripts must appear first in the document `<head>`, followed by jQuery, followed by the plugin.
- [ ] The jQuery script tag and the plugin script tag must appear in the document `<head>`, and your custom scripts can follow anywhere on the page.
- [ ] The jQuery script tag must appear in the document `<head>`, but the plugin and your custom scripts can appear anywhere else in any order.

#### Q48. These two script tags show different ways of using jQuery's `ready()` method. What is true about both approaches?

```js
<script>
  $(function() {
    // The rest of my code goes here
  });
</script>

<script>
  jQuery(document).ready(function($) {
    // The rest of my code goes here
  });
</script>
```

- [x] The code inside them can manipulate the DOM safely, knowing the browser has loaded it fully.
- [ ] The code inside them can manipulate images on the page safely, knowing they have fully downloaded to the browser.
- [ ] The code inside them will be run exactly once per user session.
- [ ] The code inside them is not aware of the DOM.

#### Q49. Which describes how jQuery makes working with the DOM faster?

- [ ] jQuery optimizes the DOM in a background thread, making updates faster.
- [ ] jQuery avoids using the DOM at all.
- [ ] jQuery uses a virtual DOM that batches updates, making inserts and deletes faster.
- [x] jQuery code to perform DOM manipulation is shorter and easier to write, but does not make DOM operations faster.

#### Q50. There are some issues with this snippet of jQuery. First, it is manipulating CSS directly, rather than manipulating classes and leaving the CSS in stylesheets. What else in this code is best to avoid?

```js
$('.item').css('background-color', 'red');
// some other code here
var firstSubItem = $('.item').find('.sub-item').get(0);
// some other code here too
$('.item').parents('.navigation').css('font-weight', 'bold');
```

- [ ] The `.css()` method accepts only an object, not two separate arguments. This will trigger an exception that should be caught.
- [ ] The `$('.item')` selection is being made several times. This should be cached in a variable for (however slightly) better performance and easier maintainability.
- [x] The call to `.parents()` is in an inefficient place.
- [ ] All the calls to `$('.item')` should be chained together as a single executable line for better performance.

#### Q51. Which choice is an example of statement chaining?

- [ ] `var $p = $('p'); console.log($p.length);`
- [x] `$('p').find('a').children('li');`
- [ ] `$('p > a > li');`
- [ ] `$('p'); $('a'); $('li');`

#### Q52. How can you ensure that some code executes only when a class `active` appears on an element?

- [ ] `$('.element').attr('class', 'active')`
- [ ] `$('.element').with('.active')`
- [x] `$('.element').hasClass('active')`
- [ ] `$('.active').then()`

#### Q53. jQuery has a main function for handling AJAX, and several shorthand function including `load()` that make calling that main function easier. Given this HTML snippet, how can you insert only the second snippet from the source.html file (`div#one`) into the `#load-me` div on-demand via AJAX?

```html
<div id="load-me">This area will be replaced with AJAX loaded content.</div>

<div id="one">
  <h1>First Piece</h1>

  <p>Lorem ipsum duis maximus quam condimentum dolor eleifend scelerisque.</p>
</div>

<div id="two">
  <h1>Second Piece</h1>

  <p>Lorem ipsum proin facilisis augue in risus interdum ornare.</p>
</div>
```

- [ ] `$('#load-me').get('source.html#one');`
- [ ] `$('#load-me').get('source.html #one');`
- [x] `$('#load-me').load('source.html #one');`
- [ ] `$('#load-me').load('source.html', '#one');`

#### Q54. Given this HTML list and subsequent two lines of jQuery, what is the difference in the behavior of `.closest()` and `.parents()`?

```html
<ul class="items" id="main-menu">
  <li>
    Item 1
    <ul id="sub-menu">
      <li class="leaf">Sub Item 1</li>
      <li>Sub Item 2</li>
    </ul>
  </li>
</ul>
```

```js
$('.leaf').closest('.items');
$('.leaf').parents('.items');
```

- [x] `.closest()` returns `.leaf` and `#main-menu`; `.parents()` returns `#main-menu` and `#sub-menu`.
- [ ] `.closest()` returns `.leaf` and `#sub-menu`; `.parents()` returns `#main-menu` and `#sub-menu`.
- [ ] `.closest()` returns only `#main-menu`; `.parents()` returns `#main-menu` and `#sub-menu`.
- [ ] `.closest()` returns only `#sub-menu`; `.parents()` returns `#main-menu` and `#sub-menu`.

[Source: jQuery closest Method](https://www.w3schools.com/jquery/traversing_closest.asp)

**Explanation**: `Considering current HTML code, .closest() returns only #main-menu; .parents() returns only #main-menu; cause both of them are looking for .items class which only exist in the #main-menu. Thus all choices are incorrect. This can be seen using this snippet: $('.leaf').closest('.items').each(function(i, obj) {console.log(obj)}); $('.leaf').parents('.items').each(function(i, obj) {console.log(obj)}); `

#### Q55. What does this line of code do?

```js
$('ul > li:first-child');
```

- [x] selects the first list item inside all unordered lists on the page
- [ ] selects the first list item inside the first unordered list on the page
- [ ] selects the first element inside any list items on the page
- [ ] creates a predefined CSS selector that can be reused later

#### Q56. Below is a list of items that you want to be clickable and an event handler function. How can you assign the event handler to every item in the list in a way that is most performant, and also that ensures that the handler is called even if more items are added to the list programmatically?

```html
<ul class="clickable-list">
  <li>First Item</li>
  <li>Second Item</li>
  <li>Third Item</li>
  <li>Fourth Item</li>
  <li>Fifth Item</li>
</ul>
```

```js
function listResponder(evt) {
  console.log('You clicked a list item that says', evt.target.innerText);
}
```

- [ ] `$('.clickable-list').click(listResponder);`
- [x] `$('.clickable-list').on('click', 'li', listResponder);`
- [ ] `$('.clickable-list').on('click, append', listResponder);`
- [ ] `$('.clickable-list').each(function() { $(this).click(listResponder); });`

#### Q57. What is the difference between $('p').find('a') and $('p').children('a')?

- [ ] `find() traverses only one level down, whereas children() selects anything inside the original element`
- [ ] `$('p').find('a') finds all paragraphs inside links, whereas $('p').children('a') finds links within paragraph tags`
- [ ] `.find() always searches the entire DOM tree, regardless of the original selection .children() searches only the immediate childern of an element`
- [x] `children() traverses only one level down, whereas find() selects anything inside the original element`

[Source: https://api.jquery.com/find/](https://api.jquery.com/find/)

**Explanation**:`Given a jQuery object that represents a set of DOM elements, the .find() method allows us to search through the descendants of these elements in the DOM tree and construct a new jQuery object from the matching elements. The .find() and .children() methods are similar, except that the latter only travels a single level down the DOM tree.`

#### Q58. Consider the following markup, used to lay out three balls on the page, all hidden. How can you select the green ball, make it faded in over the course of three seconds, and log a console message when the animation has finished?

```html
<div class="balls">
  <div class="ball ball--red" style="display: none"></div>
  <div class="ball ball--green" style="display: none"></div>
  <div class="ball ball--blue" style="display: none"></div>
</div>
```

- [x] A

```JavaScript
$('.ball--green').fadeIn(3000, function(){
    console.log("Animation is done!");
});
```

- [ ] B

```JavaScript
$('.ball--green').fade('in',3000).done(function(){
    console.log("Animation is done!");
});
```

- [ ] C

```JavaScript
$('.ball--green').fadeIn(3).console().log("Animation is done!");
```

- [ ] D

```JavaScript
$('.ball--green').fadeIn("3s", function(){
    console.log("Animation is done!");
});
```

[Source: jQuery Docs: fadeIn](https://api.jquery.com/fadeIn/)

`Durations are given in milliseconds; higher values indicate slower animations, not faster ones. The strings 'fast' and 'slow' can be supplied to indicate durations of 200 and 600 milliseconds, respectively. If any other string is supplied, or if the duration parameter is omitted, the default duration of 400 milliseconds is used.`

#### Q59. Why might you use custom events instead of shared helper functions? For example

```JavaScript
$(document).on('myCustomEvent', function(){
    // act on my custom event
});

//and later...
$(document).trigger('myCustomEvent');
```

- [ ] `Custom events are at least an order of magnitude faster than helper functions`
- [x] `Custom events can be listened for and acted upon across one or more scripts without needing to keep helper functions in scope`
- [ ] `Handler functions for custom events are less likely to be mangled by minification and obfuscation build tools`
- [ ] `It is easier to write documentation for custom events than it is for helper functions`

[Source: learn.jquery.com](https://learn.jquery.com/events/introduction-to-custom-events/)

`Instead of focusing on the element that triggers an action, custom events put the spotlight on the element being acted upon. This brings a bevy of benefits, including: Behaviors of the target element can easily be triggered by different elements using the same code. Behaviors can be triggered across multiple, similar, target elements at once. Behaviors are more clearly associated with the target element in code, making code easier to read and maintain.`

#### Q60. In the HTML and JavaScript below, the animations will all fire at once. How can you make them fire in sequence instead?

```html
<div id="element-1" class="animel"></div>
<div id="element-2" class="animel"></div>
<div id="element-3" class="animel"></div>

$('#element-1').animate({ top: '+=100' }); $('#element-2').animate({ top: '+=100' });
$('#element-3').animate({ top: '+=100' });
```

- [ ] A

```JavaScript
$('#element-1').animate({ top: '+=100' })
    .pushStack('#element-2')
    .animate({ top: '+=100' })
    .pushStack('#element-3').animate({ top: '+=100' })
```

- [x] B

```JavaScript
$('#element-1').animate({ top: '+=100' }, function() {
    $('#element-2').animate({ top: '+=100' }, function() {
        $('#element-3').animate({ top: '+=100' });
    })
});
```

- [ ] C

```JavaScript
$('#element-1').animate({ top: '+=100' })
    .add('#element-2').animate({ top: '+=100' })
    .add('#element-3').animate({ top: '+=100' })
```

- [ ] D

```JavaScript
$('#element-1').animate({ top: '+=100' }, {queue: 'custom'});
$('#element-2').animate({ top: '+=100' }, {queue: 'custom'});
$('#element-3').animate({ top: '+=100' }, {queue: 'custom'});
$('custom').dequeue();
```

[Source: jQuery Docs: animate](https://api.jquery.com/animate/)

`the .animate() method can take in a function to call once the animation is complete, called once per matched element. Which is called the complete option for the animate method`

#### Q61. Given this checkbox, how can you determine whether a user has selected or cleared the checkbox?

`<input type="checkbox" id="same-address" checked>`

- [ ] by checking the value of `$('#same-address').val()`
- [x] by checking the value of `$('#same-address').prop('checked')`
- [ ] by checking the value of `$('#same-address').attr('checked')`
- [ ] by checking the value of `$('#same-address').checked`

#### Q62. In some projects, jQuery is not included as a file with an obvious version number (if it has been run through a minifier or other code bundler, for example). How can you detect programmatically what version of jQuery is active?

- [ ] `jQuery.version()`
- [ ] `jQuery.jquery`
- [ ] `jQuery.prototype.version`
- [x] `jQuery.fn.jquery`

#### Q63. Given this snippet of HTML, how can you get the value of the text field using jQuery?

`<input type="text" class="form-control" id="firstName" placeholder="" value="" required="">`

- [ ] `$('input[type=text]').val()`
- [ ] `$('.form-control').val()`
- [x] `all of these answers`
- [ ] `$('#firstName').val()`

`all the listed selectors will target the text field since it has a type=text, a class=form-control, and an id=firstName`

#### Q64. Which property of the jQuery event object references the DOM object that dispatched an event?

- [x] target
- [ ] self
- [ ] source
- [ ] object

[Source: jQuery Docs: event.target](https://api.jquery.com/event.target/)

`The target property can be the element that registered for the event or a descendant of it. It is often useful to compare event.target to this in order to determine if the event is being handled due to event bubbling.`

[Extra reading: Event Bubbling and capturing](https://stackoverflow.com/questions/4616694/what-is-event-bubbling-and-capturing)

#### Q65. You want to write a plugin that creates a new traversal function—such as parent() and children()—and behaves like the ones jQuery includes out of the box. It needs to correctly modify the list of selections jQuery tracks internally, build up a list of additional items, and return the merged collection. What do you need to return on the last line of the function in order for this plugin to work correctly?

```JavaScript
$.fn.myTraverse = function() {
   // ... setup

   var additionalItems = [ /* some additional items for jQuery */ ];

   return // return what?
}
```

- [ ] `return this.append(additionalItems);`
- [ ] `return additionalItems.appendTo(this);`
- [x] `return this.pushStack(additionalItems);`
- [ ] `return this.add(additionalItems);`

[Source: jQuery Docs](https://api.jquery.com/pushStack/)

`When you call pushStack() off of the current collection, it will take the given collection and associate it to the current collection such that calling the end() method (after the plugin exits) will return the programmer to the current collection.`

[Extra Reading: bennadel.com](https://www.bennadel.com/blog/1739-using-pushstack-in-jquery-plugins-to-create-new-collections.htm)

#### Q66. Given this snippet of HTML and jQuery code, what will the result look like?

```html
<ul class="items">
  <li class="active">Item 1</li>
  <li>Item 2</li>
  <li>
    Item 3
    <ul>
      <li>Sub Item 1</li>
      <li>Sub Item 2</li>
    </ul>
  </li>
</ul>
```

`$('.items').find('.active').nextAll().addClass('after-active');`

- [x] A

```html
<ul class="items">
  <li class="active">Item 1</li>
  <li class="after-active">Item 2</li>
  <li class="after-active">
    Item 3
    <ul>
      <li>Sub Item 1</li>
      <li>Sub Item 2</li>
    </ul>
  </li>
</ul>
```

- [ ] B

```html
<ul class="items">
  <li class="active">Item 1</li>
  <li class="after-active">Item 2</li>
  <li class="after-active">
    Item 3
    <ul class="after-active">
      <li>Sub Item 1</li>
      <li>Sub Item 2</li>
    </ul>
  </li>
</ul>
```

- [ ] C

```html
<ul class="items">
  <li class="active">Item 1</li>
  <li class="after-active">Item 2</li>
  <li class="after-active">
    Item 3
    <ul>
      <li class="after-active">Sub Item 1</li>
      <li class="after-active">Sub Item 2</li>
    </ul>
  </li>
</ul>
```

- [ ] D

```html
<ul class="items">
  <li class="active">Item 1</li>
  <li class="after-active">Item 2</li>
  <li class="after-active">
    Item 3
    <ul class="after-active">
      <li class="after-active">Sub Item 1</li>
      <li class="after-active">Sub Item 2</li>
    </ul>
  </li>
</ul>
```

[Source: jQuery Docs](https://api.jquery.com/nextall/)

**.nextAll([selector]) method**
`Gets all following siblings of each element in the set of matched elements, optionally filtered by a selector.`

#### Q67. You have an element with a series of code (not CSS) animations applied to it that could be triggered by code you control, or other code elsewhere (such as plugins). How can you fire some code when all those animations have completed?

- [x] A

```js
$('#element').on('animationend', function () {
  console.log('Finally, everything is done!');
});
```

- [ ] B

```js
$('#element')
  .on('promise')
  .then(function () {
    console.log('Finally, everything is done!');
  });
```

- [ ] C

```js
$('#element')
  .promise()
  .catch(function () {
    console.log('Finally, everything is done!');
  });
```

- [ ] D

```js
$('#element')
  .promise()
  .then(function () {
    console.log('Finally, everything is done!');
  });
```

1. [Source: HTMLElement: animationend event | MDN ](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/animationend_event)
2. [Example: Stackoverflow](https://stackoverflow.com/questions/49580666/check-if-an-css-animation-is-completed-with-jquery-or-js)

**Explanation**: `Although A is not complete as it could include animationend webkitAnimationEnd oAnimationEnd, other choices are incorrect. The last choice could be also correct if it were .promise().done instead`

#### Q68. HTML5 data attributes allow you to create valid custom attributes to store arbitrary data within DOM elements. jQuery has an API to interface with custom data such as the series of quotes below. How can you mark the second quote as your favorite?

```html
<div class="quotes">
  <blockquote data-favorite="false">A quote</blockquote>
  <blockquote data-favorite="false">A favorite quote</blockquote>
  <blockquote data-favorite="false">A quote</blockquote>
  <blockquote data-favorite="false">A quote</blockquote>
</div>
```

- [ ] `$('blockquote'):second().attr('favorite', true);`
- [x] `$('blockquote:nth-child(2)').data('favorite', true);`
- [ ] `$('blockquote').second().data('favorite', true);`
- [ ] `$('blockquote:nth-child(2)').attr('favorite', true);`

1. [Source: .data() | jQuery API Documentation](https://api.jquery.com/data/)
2. [Source: :nth-child() | MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/:nth-child)

#### Q69. jQuery can create event handlers that execute exactly once. How is this done?

- [ ] `$('button').click(function() { console.log('this will only happen once'); }, false);`
- [ ] `$('button').on('click', function() { console.log('this will only happen once'); }).off('click');`
- [ ] `$('button').once('click', function() { console.log('this will only happen once'); });`
- [x] `$('button').one('click', function() { console.log('this will only happen once'); });`

[Source: .one() | jQuery API Documentation](https://api.jquery.com/one/)

#### Q70. You want to implement the behavior of an effect like `slideDown()` manually using `animate()`. What is one critical point you need to remember?

- [ ] `slideDown()` requires animating the background color; doing so with `animate()` requires the jQuery Color plugin.
- [x] `slideDown()` includes toggling visibility automatically. `animate()` does not automatically set any properties.
- [ ] `slideDown()` requires the element to have a height set in pixels. `animate()` does not.
- [ ] Effects created with `animate()` must be run over at least 100 milliseconds, where `slideDown()` can run as quickly as 50ms.

1. [Source: .slideDown() | jQuery API Documentation](https://api.jquery.com/slidedown/)
2. [Source: .animate() | jQuery API Documentation](https://api.jquery.com/animate/)\

#### Q71. What is the main difference between the `contents()` and `children()` functions?

- [ ] They both return the content of selected nodes, but `children()` also includes text and comment nodes.
- [ ] The `contents()` function only includes text nodes of the selected elements.
- [ ] The `children()` function only includes text nodes of the selected elements.
- [x] They both return the content of selected nodes, but `contents()` also includes text and comment nodes.

1. [Source: .children() | jQuery API Documentation](https://api.jquery.com/children/)
2. [Source: .contents() | jQuery API Documentation](https://api.jquery.com/contents/)

#### Q72. If your JavaScript project involves a lot of DOM manipulation, but no AJAX or animation, which version of jQuery should you use?

- [ ] jQuery 3 compressed
- [x] jQuery 3 slim
- [ ] jQuery 2
- [ ] None of these - jQuery requires AJAX

#### Q73. The `.ready()` function is one of the most basic parts of jQuery, but jQuery also provides a mechanism for executing code when both one or more Promises have resolved and the DOM is ready. Which code snippet accomplishes this?

- [ ] A

```js
$(function({
    getData : $.get('http://httpbin.org/get'),
    delayedData : $.get('http://httpbin.org/delay/3')
})  {
    //DOM is ready, getData and delayedData are available
});
```

- [ ] B

```js
$($.get('http://httpbin.org/get'), $.get('http://httpbin.org/delay/3')).then(
  function (getData, delayedData) {
    //DOM is ready, getData and delayedData are available
  },
);
```

- [ ] C

```js
$.when($.get('http://httpbin.org/get'), $.get('http://httpbin.org/delay/3')).then(
  function (getData, delayedData) {
    //DOM is ready, getData and delayedData are available
  },
);
```

- [x] D

```js
$.ready($.get('http://httpbin.org/get'), $.get('http://httpbin.org/delay/3')).then(
  function (getData, delayedData) {
    //DOM is ready, getData and delayedData are available
  },
);
```

#### Q74. You want to take an element and any event handlers that go with it out of the DOM to do some work—without the changes affecting the rest of the page—and then move it somewhere else in the DOM, like right after the opening tag. What should go on the first line of this code snippet?

```js
// what goes here?
// ... do some other hidden work on $example
$example.prependTo(document.body);
```

- [ ] `var $example = $('#example').remove();`
- [ ] `var $example = $('#example').clone();`
- [x] `var $example = $('#example').detach();`
- [ ] `var $example = $('#example').addBack().empty();`

https://api.jquery.com/detach/

#### Q75. Review the HTML below. You want to select the first item in the list and fade it out, then select the subsequent items up to (but not including) the active item, and fade them out halfway. How can you set up a single chain to do this?

```html
<ul class="items">
  <li>Item 1</li>
  <li>Item 2</li>
  <li>Item 3</li>
  <li class="active">Item 4</li>
  <li>Item 5</li>
  <li>Item 6</li>
</ul>
```

- [x] A

```js
$('.items > li').first().fadeOut().nextUntil('.active').fadeTo('fast', 0.5);
```

- [ ] B

```js
$('.items').children(':first-child').fadeOut().filter('.active').fadeTo('fast', 0.5);
```

- [ ] C

```js
$('.items > li').first().fadeOut().nextAll('.active').fadeOut(50);
```

- [ ] D

```js
$('.items').find('li:first-child').fadeOut().next('.active').fadeTo('fast', 0.5);
```

1. https://api.jquery.com/fadeTo/
2. https://api.jquery.com/fadeOut/
3. https://api.jquery.com/nextUntil/

#### Q76. What is a particular performance concern when dealing with event handlers, and how can you cope with it?

- [ ] Finding which element an event occurred on is expensive. Assign most events to document.body and use .is() to act on the element of interest.
- [x] Some events, such as mousemove and scroll, happen a lot on a typical page. Debounce or throttle their handlers to make sure the handlers are not called more than you actually need.
- [ ] Listening for an event that does not exist can create serious memory leaks. Be careful to spell event names correctly to avoid consuming too much memory.
- [ ] DOM elements with an ID wil fire events more efficiently than with classes. Always use IDs instead of classes where possible.

#### Q77. What is the purpose of the jQuery.fx.off global property?

- [ ] It turns off animations that are used to provide motion effect, but appearance effects remain enabled.
- [ ] It causes animation effects that are triggered via functions to instead be executed using CSS.
- [x] It globally disables all animations. When animations are run, all animation methods will immediately set elements to their final state when called, rather than displaying an effect.
- [ ] It globally disables animations that are triggered by CSS class changes.

[Source: jQuery.fx.off Property](https://www.w3schools.com/jquery/prop_jquery_fx_off.asp)

#### Q78. When you use custom Jquery selection extensions, such as :animated, on a page with lots of DOM elements, you can run into performance issues. What is the best practice for managing those issues?

- [ ] Select `$(document.body)` first, then use .filter with the custom extension.
- [ ] Use the custom extension with `.has()`.
- [ ] Start with the custom extension, then use `.find` with a selector that exists in CSS to limit the selection.
- [x] Start with a selection that exists in CSS, then refine the selection using `.filter()` with the custom extension.

#### Q79. What is the main difference between the ajaxStop and ajaxComplete global handlers?

- [x] ajaxStop fires when all open requests have completed, while ajaxComplete fires when an individual request completes.
- [ ] There is no difference. They are aliases of each other.
- [ ] ajaxStop fires when an error has been encountered, while ajaxComplete fires when a successful request completes.
- [ ] ajaxComplete fires when all open requests have completed, while ajaxStop fires when an individual request completes.

#### Q80. The :only-child selector selects **\_**.

- [ ] all elements that are child elements.
- [ ] elements that have no siblings.
- [ ] elements that have only one child element.
- [x] only the child elements of a given element.

#### Q81. Because querySelectorAll and querySelector are in the native DOM API of modern browsers, you don't need jQuery to do many kinds of DOM selections. But the jQuery selector engine does provide extensions that browsers do not support natively. Which extension is supported only by jQuery and _not_ by querySelector or querySelectorAll?

- [ ] :parent, which can select elements that have children
- [x] :visible, which can select elements that jQuery considers to be visible
- [ ] :contains, which can select elements by the text they contain
- [ ] :nth-of-type, which can select elements that are the nth element of their type within their parent

[Source: Selectors Level 4](https://drafts.csswg.org/selectors/)

#### Q82. jQuery is quite large, and developers often do not use all of its functionality on a project. Beyond using the slim build of jQuery 3, how can you use some of jQuery, but not all?

- [ ] None of these--the only viable options are the full build or slim build of jQuery.
- [ ] Download the minified build from the JQuery CDN and strip out functions manually.
- [x] Download the source code from GitHub and build a custom version that excludes the unnecessary modules.
- [ ] Download the developer build from code.jquery.com and gzip it.

[Source: jQuery GitHub repo](https://github.com/jquery/jquery#modules)

**Explanation**: Special builds can be created that exclude subsets of jQuery functionality. This allows for smaller custom builds when the builder is certain that those parts of jQuery are not being used.

#### Q83. jQuery UI includes many animation features not found in jQuery core. Which choice is not one of the features that jQuery UI adds to jQuery?

- [x] forced CSS-equivalent hardware acceleration of all jQuery animations
- [ ] animation of color transitions (background or foreground) without using CSS
- [ ] duration for .addClass() and .removeClass(), so CSS properties can be animated over time simply by adding a class
- [ ] more easing options for timing animations

#### Q84. Given this snippet of HTML and jQuery, which answer accurately describes what the line of jQuery does?

```html
<ul class="menu">
  <li><a href="#" class="active">Home</a></li>
  <li><a href="#">Page 2</a></li>
</ul>
<ul class="active submenu">
  <li><a href="#">Subpage 1</a></li>
  <li><a href="#">Subpage 2</a></li>
</ul>
```

```js
$('.menu').find('a').css('color', 'red').end().find('.active').hide();
```

- [ ] It changes the menu items in the first list to red, then hides the second list of menu items.
- [ ] It changes all menu items in both lists to red, then hides all items with the active class.
- [x] It changes the menu items in the first list to red, then hides the item in the first list with the active class.
- [ ] It changes the menu items in the first list to red, then returns the selection with no further changes.

#### Q85. A jQuery selection acts on the HTML below, which selects the active menu item. What can you chain onto this selection to select the #main nav tag and add a class called "processed" to it?

```html
<nav id="main">
  <ul>
    <li><a href="/" class="active">Home</a></li>
    <li><a href="/about">About</a></li>
  </ul>
</nav>
```

```javascript
$('a.active').addClass('hover');
```

- [ ] .parent('#main').addClass('processed');
- [x] .parents('#main').addClass('processed');
- [ ] .find('#main').addClass('processed');
- [ ] .up('#main').addClass('processed');

#### Q86. When might you want to use custom queues for animations instead of relying on the built-in FX queue?

- [ ] when you want to have multiple sequences of animations on a single element that run with independent timings
- [ ] when you want to time jQuery animations and CSS animations, since addClass has no duration setting
- [x] all of these answers
- [ ] when you want to time custom animations of several different elements without lots of nested callbacks

#### Q87. Which symbol is commonly used to represent the jQuery object?

- [x] $
- [ ] #
- [ ] %
- [ ] &

[Source: Stack Overflow](https://stackoverflow.com/questions/8667736/what-does-the-sign-mean-in-jquery-or-javascript)

#### Q88. Along with standard DOM events like click, focus, or blur, you can register and listen for custom events with jQuery. If you have an external API at `http://example.com/api/v1` and you want to use custom events to ping that API from various places throughtout your codebase, what would that look like?

- [x] A

```js
// listens
$('body').on('myEvent', function () {
  $.get('http://example.com/api/v1/ping');
});
// triggers
$('body').trigger('myEvent');
```

- [ ] B

```js
// listens
$('body').on('custom', 'myEvent', function () {
  $.get('http://example.com/api/v1/ping');
});
// triggers
$('document').trigger('custom', 'myEvent');
```

- [ ] C

```js
// listens
$('body').on(function (event) {
  if (event === 'myEvent') {
    $.get('http://example.com/api/v1/ping');
  }
});
// triggers
$('body').triggerHandler('myEvent');
```

- [ ] D

```js
// listens
$.on('myEvent', function () {
  $.get('http://example.com/api/v1/ping');
});
// triggers
$.trigger('myEvent');
```

[Source: Introducing Custom Events](https://learn.jquery.com/events/introduction-to-custom-events/)

#### Q89. Given the HTML code between `<form>` and `</form>` below, what does the snippet between `<script>` and `</script>` do?

```js
<form class="needs-validation" novalidate="">
  <div class="custom-control custom-checkbox">
    <input type="checkbox" class="custom-control-input" id="checkbox-opt-in">
    <label class="custom-control-label" for="checkbox-opt-in">I totally read and accept the terms, really.</label>
  </div>
</form>

<script>
  $(function() {
    $('form').submit(function(evt) {
      if ($(this).find('.checkbox-opt-in').prop('checked') === false) {
        evt.preventDefault();

        alert("Please read and accept the terms.")
      }
    });
  });
</script>
```

- [x] When the form is submitted, look at whether the checkbox is selected. If it is, let the form submit normally. If not, show an alert.
- [ ] When the form is submitted, jQuery looks for information about the checkbox in the submit event (the value of `this`). If the checkbox is selected, the form is allowed to submit.
- [ ] The function triggers the form to submit programmatically, then looks at the checkbox. If it is not selected, display an alert.
- [ ] jQuery submits the form, and then asks for confirmation on the terms if the checkbox was not clicked.

[Source: .preventDefault()](https://www.w3schools.com/jsref/event_preventdefault.asp)

#### Q90. jQuery has an internal function used to prepare data that are submitted with AJAX requests, and it is available to you as well. Suppose you have a page with a simple button. Based on various conditions on the page, you build up an object that will alter the URL. If you want the presented URL, how can you get a complete representation of the data into the URL?

```js
<div class="actions">
  <a href="//example.com/action">Let's go!</a>
</div>;

var data = {
  username: 'jaffacakes',
  message: {
    date: '2018-07-05 13:14:00 GMT-07:00',
    text: `I have a whole lot to say, everyone, and I'm gonna say it!`,
  },
  tags: ['discourse', 'thoughts', 'messageOfTheDay'],
};

//example.com/action?username=jaffacakes&message%5Bdate%5D=2018-07-05+13%3A14%3A00+GMT-07%3A00
```

- [ ] `$(data).serializeArray();`
- [x] `$.param(data, false);`
- [ ] `$.param(data, true);`
- [ ] `$(data).serialize();`

[Source: jQuery.param()](https://api.jquery.com/jQuery.param/)

#### Q91. What is the difference between `.wrap()` and `.wrapAll()`?

- [ ] `.wrap()` wraps each element separately, while `.wrapAll()` requires at least two elements to work.
- [x] `.wrap()` wraps each matched element individually, while `.wrapAll()` wraps all matched elements together in a single wrapper.
- [ ] `.wrap()` can only wrap one element, while `.wrapAll()` can wrap multiple elements.
- [ ] There is no difference; they are aliases of each other.

[Source: .wrap()](https://api.jquery.com/wrap/) and [.wrapAll()](https://api.jquery.com/wrapAll/)

#### Q92. What does the `.end()` method do?

```js
$('ul.first')
  .find('.foo')
  .css('background-color', 'red')
  .end()
  .find('.bar')
  .css('background-color', 'green');
```

- [x] It terminates the current chain and starts a new one on the original selection.
- [ ] It ends all jQuery animations on the selected elements.
- [ ] It returns the last element from the collection.
- [ ] It destroys the jQuery object and releases memory.

[Source: .end()](https://api.jquery.com/end/)

#### Q93. When would you use `.promise()` without arguments versus `.promise('fx')`?

- [ ] `.promise()` returns immediately, while `.promise('fx')` waits for animations to complete.
- [x] `.promise()` returns a promise resolved when all animations on all matched elements complete, while `.promise('fx')` explicitly waits for the FX queue.
- [ ] There is no difference between them.
- [ ] `.promise()` is used for AJAX, while `.promise('fx')` is used for animations.

[Source: .promise()](https://api.jquery.com/promise/)

#### Q94. What is the difference between `.slideToggle()` and `.slideUp()` / `.slideDown()` combined?

```js
// Option A
$('.element').slideToggle();

// Option B
if ($('.element').is(':visible')) {
  $('.element').slideUp();
} else {
  $('.element').slideDown();
}
```

- [ ] `.slideToggle()` only works on elements that are already visible.
- [ ] There is no difference; `.slideToggle()` is just a shorthand for the if/else block.
- [x] `.slideToggle()` tracks the current state internally and toggles based on visibility, while the manual approach may have issues with display styles.
- [ ] `.slideToggle()` is deprecated and the manual approach should be used instead.

[Source: .slideToggle()](https://api.jquery.com/slideToggle/)

#### Q95. How can you ensure that a jQuery selector only searches within a specific container element for better performance?

```html
<div class="container">
  <p>Some text</p>
  <div class="nested">
    <p>More text</p>
  </div>
</div>
```

- [x] `$('.container').find('p')`
- [ ] `$('.container p')`
- [ ] Both approaches are equivalent in performance and behavior.
- [ ] `$('p', '.container')`

[Source: .find()](https://api.jquery.com/find/) - Using `.find()` is more explicit and can be better for performance when working with large documents.

#### Q96. What does the `.stop()` method do when called with no arguments versus `.stop(true, true)`?

- [ ] `.stop()` pauses the animation, `.stop(true, true)` completely removes it from the queue.
- [x] `.stop()` stops the current animation on the element, `.stop(true, true)` clears the queue and jumps to the end of the current animation.
- [ ] `.stop()` is a deprecated method, `.stop(true, true)` is the new syntax.
- [ ] Both are identical in functionality.

[Source: .stop()](https://api.jquery.com/stop/)

#### Q97. How do you bind a single event handler that works for elements added dynamically to the page?

```html
<div class="container">
  <button class="dynamic-btn">Click me</button>
</div>
```

- [ ] `$('.dynamic-btn').on('click', function() { console.log('clicked'); });` - This works automatically for dynamic elements.
- [x] `$(document).on('click', '.dynamic-btn', function() { console.log('clicked'); });` - Delegated event handler.
- [ ] `$('.dynamic-btn').live('click', function() { console.log('clicked'); });` - The `.live()` method.
- [ ] You cannot bind to dynamically added elements without using a library.

[Source: .on()](https://api.jquery.com/on/) - Event delegation is key for dynamic elements.

#### Q98. What is the correct way to remove all event handlers and data from a jQuery object before reusing it in a long-running application?

- [x] `$('#element').off().empty().removeData();`
- [ ] `$('#element').unbind().removeData();`
- [ ] `$('#element').detach();`
- [ ] jQuery automatically cleans up everything when the page unloads.

[Source: .off()](https://api.jquery.com/off/) and [.removeData()](https://api.jquery.com/removeData/)

#### Q99. How can you check if an element is animating in jQuery?

- [ ] `$('.element').is(':animating');`
- [x] `$('.element').is(':animated');`
- [ ] `$('.element').hasClass('animating');`
- [ ] You cannot check for animation state in jQuery.

[Source: :animated selector](https://api.jquery.com/animated-selector/)

#### Q100. What is the difference between using `.attr()` and `.prop()` for boolean attributes like "checked" or "disabled"?

```js
// Setting checked state
$('#checkbox').attr('checked', 'checked');
$('#checkbox').prop('checked', true);
```

- [x] `.attr()` manipulates HTML attributes (reflecting initial state), while `.prop()` manipulates DOM properties (current state).
- [ ] There is no difference; both methods are identical in behavior.
- [ ] `.attr()` is deprecated and `.prop()` should always be used.
- [ ] `.attr()` only works for string values, `.prop()` only works for boolean values.

[Source: .attr() vs .prop()](https://api.jquery.com/attr/) vs [.prop()](https://api.jquery.com/prop/)

#### Q101. What is the purpose of jQuery's `.end()` method?

- [ ] To end a jQuery chain
- [x] To return to the previous set of elements in a chaining sequence
- [ ] To terminate event handlers
- [ ] To end animations

**Explanation:**
The `.end()` method returns the previous set of matched elements in the chain, allowing you to back up one step in a chain of jQuery operations.

[Reference](https://api.jquery.com/end/)

#### Q102. What does the `.andSelf()` method do (deprecated in jQuery 1.8)?

- [ ] Adds self to the selection
- [x] Adds the previous set of elements to the current set
- [ ] Selects the element and its siblings
- [ ] Selects the element and its parent

**Explanation:**
`.andSelf()` (now `.addBack()`) adds the previous set of elements on the stack to the current set. It was deprecated in jQuery 1.8 and replaced with `.addBack()`.

[Reference](https://api.jquery.com/addBack/)

#### Q103. How do you select all elements with a data attribute in jQuery?

- [ ] `$('[data]')`
- [x] `$('[data-*]')` or `$('[data-attribute]')` for specific attribute
- [ ] `$('.data-*')`
- [ ] `$('data-*')`

**Explanation:**
To select elements with any data attribute, use `$('[data-*]')`. For a specific data attribute, use `$('[data-attribute]')` where attribute is the name.

[Reference](https://api.jquery.com/attribute-starts-with-selector/)

#### Q104. What is the difference between `.text()` and `.html()`?

- [x] `.text()` gets/sets text content only, `.html()` gets/sets HTML markup
- [ ] `.text()` is faster
- [ ] `.html()` is deprecated
- [ ] There is no difference

**Explanation:**
`.text()` gets or sets the text content of elements (escaping HTML), while `.html()` gets or sets the HTML content (parsing HTML tags).

[Reference](https://api.jquery.com/text/)

#### Q105. How do you prevent event bubbling in jQuery?

- [ ] `event.cancel()`
- [x] `event.stopPropagation()`
- [ ] `event.preventBubbling()`
- [ ] `return false;` (this stops both propagation and default)

**Explanation:**
`event.stopPropagation()` prevents the event from bubbling up the DOM tree. `return false` stops both propagation and default action.

[Reference](https://api.jquery.com/event.stopPropagation/)

#### Q106. What is the purpose of `.serialize()` method?

- [ ] To serialize objects
- [x] To encode form elements as a string for submission
- [ ] To convert JSON to string
- [ ] To save form data

**Explanation:**
`.serialize()` creates a URL-encoded text string from a set of form elements, useful for AJAX form submissions.

[Reference](https://api.jquery.com/serialize/)

#### Q107. What is the difference between `.serialize()` and `.serializeArray()`?

- [x] `.serialize()` returns a string, `.serializeArray()` returns an array of objects
- [ ] `.serializeArray()` is faster
- [ ] `.serialize()` is deprecated
- [ ] There is no difference

**Explanation:**
`.serialize()` returns a URL-encoded string, while `.serializeArray()` returns an array of objects with name and value properties.

[Reference](https://api.jquery.com/serializeArray/)

#### Q108. How do you check if an element exists in jQuery?

- [ ] `if ($('#element'))`
- [x] `if ($('#element').length > 0)`
- [ ] `if ($('#element').exists())`
- [ ] `if ($('#element') !== null)`

**Explanation:**
jQuery always returns an object, even if no elements match. Check the `.length` property to see if elements were found.

[Reference](https://api.jquery.com/length/)

#### Q109. What is the purpose of `.queue()` method?

- [ ] To queue animations
- [x] To show or manipulate the queue of functions to be executed on elements
- [ ] To create a queue
- [ ] To manage event queues

**Explanation:**
`.queue()` shows or manipulates the queue of functions to be executed on the matched elements, typically used with animations.

[Reference](https://api.jquery.com/queue/)

#### Q110. What is the purpose of `.dequeue()` method?

- [ ] To remove from queue
- [x] To execute the next function on the queue for the matched elements
- [ ] To clear the queue
- [ ] To stop the queue

**Explanation:**
`.dequeue()` executes the next function on the queue for the matched elements, advancing the queue.

[Reference](https://api.jquery.com/dequeue/)

#### Q111. How do you stop all animations on an element?

- [ ] `$('.element').stop()`
- [x] `$('.element').stop(true, true)`
- [ ] `$('.element').stopAll()`
- [ ] `$('.element').clearQueue()`

**Explanation:**
`.stop(true, true)` stops the animation, clears the queue, and jumps to the end. The first parameter clears the queue, the second jumps to the end.

[Reference](https://api.jquery.com/stop/)

#### Q112. What is the purpose of `.promise()` method?

- [ ] To create promises
- [x] To return a Promise object to observe when all actions on a collection have finished
- [ ] To handle async operations
- [ ] To create deferred objects

**Explanation:**
`.promise()` returns a Promise object that resolves when all queued actions on a collection have finished.

[Reference](https://api.jquery.com/promise/)

#### Q113. What is jQuery's `.Deferred()` object?

- [ ] A delayed function
- [x] A chainable utility object for managing callbacks and promises
- [ ] A deferred execution method
- [ ] A promise implementation

**Explanation:**
`$.Deferred()` creates a chainable utility object for managing callback queues, providing a way to handle asynchronous operations.

[Reference](https://api.jquery.com/jQuery.Deferred/)

#### Q114. What is the difference between `.done()` and `.then()` on a Deferred object?

- [ ] `.done()` is for success, `.then()` is for failure
- [x] `.then()` returns a new promise, `.done()` returns the original deferred
- [ ] `.done()` is deprecated
- [ ] There is no difference

**Explanation:**
`.then()` returns a new promise and allows chaining with transformation, while `.done()` returns the original deferred object.

[Reference](https://api.jquery.com/deferred.then/)

#### Q115. How do you create a custom event in jQuery?

- [ ] `$.createEvent('myEvent')`
- [x] `$('#element').trigger('myEvent')` or `$.Event('myEvent')`
- [ ] `new Event('myEvent')`
- [ ] `$('#element').fire('myEvent')`

**Explanation:**
You can trigger custom events with `.trigger('myEvent')` or create event objects with `$.Event('myEvent')`.

[Reference](https://api.jquery.com/trigger/)

#### Q116. What is the purpose of `.triggerHandler()`?

- [ ] To handle triggers
- [x] To trigger an event without bubbling or default actions
- [ ] To create event handlers
- [ ] To manage triggers

**Explanation:**
`.triggerHandler()` triggers an event but doesn't cause bubbling, doesn't trigger default browser behavior, and only affects the first matched element.

[Reference](https://api.jquery.com/triggerHandler/)

#### Q117. How do you namespace events in jQuery?

- [ ] `$('#element').on('namespace.click')`
- [x] `$('#element').on('click.namespace')`
- [ ] `$('#element').on('click', 'namespace')`
- [ ] Event namespacing is not supported

**Explanation:**
Event namespaces are added after the event name with a dot: `'click.namespace'`. This allows selective unbinding of events.

[Reference](https://api.jquery.com/on/#event-names)

#### Q118. What is the purpose of `$.proxy()`?

- [ ] To create proxies
- [x] To bind a function to a specific context (this value)
- [ ] To proxy AJAX requests
- [ ] To create proxy objects

**Explanation:**
`$.proxy()` takes a function and returns a new one that will always have a particular context, similar to Function.prototype.bind().

[Reference](https://api.jquery.com/jQuery.proxy/)

#### Q119. What is the difference between `.width()` and `.outerWidth()`?

- [x] `.width()` gets content width, `.outerWidth()` includes padding and optionally border/margin
- [ ] `.outerWidth()` is for outer elements
- [ ] `.width()` is deprecated
- [ ] There is no difference

**Explanation:**
`.width()` returns the content width. `.outerWidth()` includes padding and border by default. `.outerWidth(true)` also includes margin.

[Reference](https://api.jquery.com/outerWidth/)

#### Q120. What is the purpose of `.innerWidth()`?

- [ ] To get inner element width
- [x] To get width including padding but not border
- [ ] To get content width
- [ ] To get total width

**Explanation:**
`.innerWidth()` returns the width including padding but excluding border and margin.

[Reference](https://api.jquery.com/innerWidth/)

#### Q121. How do you get the position of an element relative to the document?

- [ ] `$('#element').position()`
- [x] `$('#element').offset()`
- [ ] `$('#element').documentPosition()`
- [ ] `$('#element').getPosition()`

**Explanation:**
`.offset()` gets the current coordinates of the element relative to the document. `.position()` gets coordinates relative to the offset parent.

[Reference](https://api.jquery.com/offset/)

#### Q122. What is the purpose of `.scrollTop()`?

- [ ] To scroll to top
- [x] To get or set the vertical scroll position
- [ ] To get top position
- [ ] To scroll upward

**Explanation:**
`.scrollTop()` gets the current vertical position of the scroll bar. `.scrollTop(value)` sets it.

[Reference](https://api.jquery.com/scrollTop/)

#### Q123. How do you select elements by attribute value that contains a specific substring?

- [ ] `$('[attr~="value"]')`
- [x] `$('[attr*="value"]')`
- [ ] `$('[attr|="value"]')`
- [ ] `$('[attr^="value"]')`

**Explanation:**
The `*=` selector matches elements with an attribute value containing the specified substring anywhere.

[Reference](https://api.jquery.com/attribute-contains-selector/)

#### Q124. What is the `:has()` selector used for?

- [ ] To check if element has a class
- [x] To select elements that contain at least one element matching the selector
- [ ] To check if element has attributes
- [ ] To select elements that have content

**Explanation:**
`:has()` selects elements which contain at least one element that matches the specified selector.

[Reference](https://api.jquery.com/has-selector/)

#### Q125. What is the difference between `:contains()` and `:has()`?

- [x] `:contains()` matches text content, `:has()` matches descendant elements
- [ ] `:contains()` is case-sensitive
- [ ] `:has()` is deprecated
- [ ] There is no difference

**Explanation:**
`:contains()` selects elements containing specific text. `:has()` selects elements containing specific descendant elements.

[Reference](https://api.jquery.com/contains-selector/)

#### Q126. How do you select the first child element of a specific type?

- [ ] `$('parent > :first')`
- [x] `$('parent > element:first-of-type')`
- [ ] `$('parent > element:first-child')`
- [ ] `$('parent').first('element')`

**Explanation:**
`:first-of-type` selects the first element of its type among siblings. `:first-child` selects if it's the first child regardless of type.

[Reference](https://api.jquery.com/first-of-type-selector/)

#### Q127. What is the purpose of `.is()` method?

- [ ] To check if element is visible
- [x] To check if elements match a selector, element, or jQuery object
- [ ] To check element type
- [ ] To validate elements

**Explanation:**
`.is()` checks the current matched set of elements against a selector, element, or jQuery object and returns true if at least one matches.

[Reference](https://api.jquery.com/is/)

#### Q128. How do you select elements that are currently visible?

- [ ] `$('.element:shown')`
- [x] `$('.element:visible')`
- [ ] `$('.element:display')`
- [ ] `$('.element').visible()`

**Explanation:**
The `:visible` selector selects all elements that are visible (not display:none, visibility:hidden, or type="hidden").

[Reference](https://api.jquery.com/visible-selector/)

#### Q129. What is the purpose of `$.contains()`?

- [ ] To check if string contains substring
- [x] To check if a DOM element is a descendant of another
- [ ] To check if array contains value
- [ ] To check if object contains property

**Explanation:**
`$.contains(container, contained)` checks whether a DOM element is a descendant of another DOM element.

[Reference](https://api.jquery.com/jQuery.contains/)

#### Q130. How do you get all sibling elements of an element?

- [ ] `$('#element').siblings()`
- [x] `$('#element').siblings()` (correct)
- [ ] `$('#element').getSiblings()`
- [ ] `$('#element').brothers()`

**Explanation:**
`.siblings()` gets all siblings of each element in the matched set, optionally filtered by a selector.

[Reference](https://api.jquery.com/siblings/)

#### Q131. What is the difference between `.next()` and `.nextAll()`?

- [x] `.next()` gets the immediately following sibling, `.nextAll()` gets all following siblings
- [ ] `.nextAll()` is faster
- [ ] `.next()` is deprecated
- [ ] There is no difference

**Explanation:**
`.next()` gets the immediately following sibling. `.nextAll()` gets all following siblings.

[Reference](https://api.jquery.com/next/)

#### Q132. How do you select elements until a specific element?

- [ ] `$('#start').to('#end')`
- [x] `$('#start').nextUntil('#end')`
- [ ] `$('#start').until('#end')`
- [ ] `$('#start').range('#end')`

**Explanation:**
`.nextUntil()` gets all following siblings up to but not including the element matched by the selector.

[Reference](https://api.jquery.com/nextUntil/)

#### Q133. What is the purpose of `.closest()`?

- [ ] To get the closest sibling
- [x] To get the first ancestor element that matches the selector
- [ ] To get the nearest element
- [ ] To find close elements

**Explanation:**
`.closest()` traverses up the DOM tree and returns the first ancestor element (including the element itself) that matches the selector.

[Reference](https://api.jquery.com/closest/)

#### Q134. What is the difference between `.closest()` and `.parents()`?

- [x] `.closest()` returns first match and includes self, `.parents()` returns all ancestors
- [ ] `.closest()` is faster
- [ ] `.parents()` is deprecated
- [ ] There is no difference

**Explanation:**
`.closest()` begins with the current element and travels up, returning the first match. `.parents()` begins with the parent and returns all ancestors.

[Reference](https://api.jquery.com/closest/)

#### Q135. How do you wrap each element in a set individually?

- [ ] `$('.element').wrap('<div>')`
- [x] `$('.element').wrap('<div>')` (wraps each individually)
- [ ] `$('.element').wrapEach('<div>')`
- [ ] `$('.element').wrapIndividual('<div>')`

**Explanation:**
`.wrap()` wraps each element in the matched set individually. `.wrapAll()` wraps all elements together as a group.

[Reference](https://api.jquery.com/wrap/)

#### Q136. What is the purpose of `.wrapInner()`?

- [ ] To wrap inner elements
- [x] To wrap the content (children) of each element
- [ ] To wrap inside a container
- [ ] To create inner wrappers

**Explanation:**
`.wrapInner()` wraps an HTML structure around the content (child elements) of each element in the matched set.

[Reference](https://api.jquery.com/wrapInner/)

#### Q137. How do you unwrap an element (remove its parent)?

- [ ] `$('#element').removeParent()`
- [x] `$('#element').unwrap()`
- [ ] `$('#element').parent().remove()`
- [ ] `$('#element').deparent()`

**Explanation:**
`.unwrap()` removes the parents of the matched elements from the DOM, leaving the matched elements in their place.

[Reference](https://api.jquery.com/unwrap/)

#### Q138. What is the purpose of `$.parseHTML()`?

- [ ] To parse HTML files
- [x] To parse a string into an array of DOM nodes
- [ ] To validate HTML
- [ ] To format HTML

**Explanation:**
`$.parseHTML()` parses a string into an array of DOM nodes, providing a safer alternative to using innerHTML.

[Reference](https://api.jquery.com/jQuery.parseHTML/)

#### Q139. What is the purpose of `$.parseJSON()`?

- [ ] To parse JSON files
- [x] To parse a JSON string (deprecated, use JSON.parse())
- [ ] To create JSON
- [ ] To validate JSON

**Explanation:**
`$.parseJSON()` parses a JSON string and returns the resulting JavaScript value. It's deprecated in favor of native `JSON.parse()`.

[Reference](https://api.jquery.com/jQuery.parseJSON/)

#### Q140. How do you make an AJAX request with custom headers?

```js
$.ajax({
  url: '/api/data',
  headers: { 'X-Custom-Header': 'value' },
});
```

- [x] Use the `headers` option in $.ajax()
- [ ] Use the `customHeaders` option
- [ ] Use `.setHeader()` method
- [ ] Custom headers are not supported

**Explanation:**
The `headers` option in `$.ajax()` allows you to set custom HTTP headers for the request.

[Reference](https://api.jquery.com/jQuery.ajax/)

#### Q141. What is the purpose of `$.ajaxSetup()`?

- [ ] To setup AJAX
- [x] To set default values for future AJAX requests
- [ ] To configure AJAX globally
- [ ] To initialize AJAX

**Explanation:**
`$.ajaxSetup()` sets default values for future AJAX requests. However, it's generally recommended to use specific options for each request instead.

[Reference](https://api.jquery.com/jQuery.ajaxSetup/)

#### Q142. How do you abort an AJAX request?

```js
var xhr = $.ajax({ url: '/api/data' });
xhr.abort();
```

- [x] Call `.abort()` on the jqXHR object
- [ ] Call `.cancel()` on the request
- [ ] Call `.stop()` on the request
- [ ] AJAX requests cannot be aborted

**Explanation:**
The jqXHR object returned by `$.ajax()` has an `.abort()` method that can cancel the request.

[Reference](https://api.jquery.com/jQuery.ajax/)

#### Q143. What is the purpose of the `context` option in $.ajax()?

- [ ] To set request context
- [x] To specify the context (this value) for all AJAX-related callbacks
- [ ] To define execution context
- [ ] To set the request scope

**Explanation:**
The `context` option sets the value of `this` within all AJAX-related callbacks for that request.

[Reference](https://api.jquery.com/jQuery.ajax/)

#### Q144. How do you send data as JSON in an AJAX request?

```js
$.ajax({
  url: '/api/data',
  method: 'POST',
  contentType: 'application/json',
  data: JSON.stringify({ key: 'value' }),
});
```

- [x] Set contentType to 'application/json' and stringify the data
- [ ] jQuery automatically converts to JSON
- [ ] Use dataType: 'json'
- [ ] Use jsonData option

**Explanation:**
To send JSON data, set `contentType` to 'application/json' and use `JSON.stringify()` on the data object.

[Reference](https://api.jquery.com/jQuery.ajax/)

#### Q145. What is the difference between `dataType` and `contentType` in $.ajax()?

- [x] `dataType` is expected response type, `contentType` is sent request type
- [ ] They are the same
- [ ] `dataType` is deprecated
- [ ] `contentType` is for headers only

**Explanation:**
`dataType` specifies the type of data you expect from the server. `contentType` specifies the type of data you're sending to the server.

[Reference](https://api.jquery.com/jQuery.ajax/)

#### Q146. How do you handle AJAX errors globally?

```js
$(document).ajaxError(function (event, jqXHR, settings, error) {
  console.log('AJAX error:', error);
});
```

- [x] Use `$(document).ajaxError()`
- [ ] Use `$.ajaxError()`
- [ ] Use `window.onerror`
- [ ] Global error handling is not supported

**Explanation:**
`$(document).ajaxError()` registers a handler to be called when AJAX requests complete with an error.

[Reference](https://api.jquery.com/ajaxError/)

#### Q147. What is the purpose of `$.ajaxPrefilter()`?

- [ ] To prefilter AJAX responses
- [x] To modify or filter AJAX options before each request is sent
- [ ] To validate AJAX requests
- [ ] To cache AJAX responses

**Explanation:**
`$.ajaxPrefilter()` allows you to modify or filter AJAX options before each request is sent and before they are processed by `$.ajax()`.

[Reference](https://api.jquery.com/jQuery.ajaxPrefilter/)

#### Q148. How do you create a custom jQuery plugin?

```js
$.fn.myPlugin = function () {
  return this.each(function () {
    // Plugin code
  });
};
```

- [x] Extend `$.fn` with your plugin function
- [ ] Extend `$.plugin` with your function
- [ ] Use `$.createPlugin()`
- [ ] Extend `jQuery.prototype`

**Explanation:**
jQuery plugins are created by extending `$.fn` (which is an alias for `jQuery.prototype`) with your plugin function.

[Reference](https://learn.jquery.com/plugins/basic-plugin-creation/)

#### Q149. What is the purpose of returning `this` in a jQuery plugin?

- [ ] To return the plugin
- [x] To enable method chaining
- [ ] To return the jQuery object
- [ ] To prevent errors

**Explanation:**
Returning `this` (the jQuery object) from a plugin enables method chaining, allowing users to call other jQuery methods after your plugin.

[Reference](https://learn.jquery.com/plugins/basic-plugin-creation/)

#### Q150. How do you make a plugin accept options?

```js
$.fn.myPlugin = function (options) {
  var settings = $.extend(
    {
      color: 'red',
      size: 10,
    },
    options,
  );
  // Use settings
};
```

- [x] Use `$.extend()` to merge default options with user options
- [ ] Use `Object.assign()`
- [ ] Use `$.merge()`
- [ ] Options are not supported

**Explanation:**
`$.extend()` merges default options with user-provided options, allowing users to override defaults.

[Reference](https://api.jquery.com/jQuery.extend/)

#### Q151. What is the purpose of `$.noConflict()`?

- [ ] To prevent conflicts
- [x] To release control of the $ variable to other libraries
- [ ] To disable jQuery
- [ ] To resolve naming conflicts

**Explanation:**
`$.noConflict()` releases jQuery's control of the `$` variable, allowing other libraries that use `$` to work alongside jQuery.

[Reference](https://api.jquery.com/jQuery.noConflict/)

#### Q152. How do you use jQuery after calling `$.noConflict()`?

```js
var jq = $.noConflict();
jq('#element').hide();
```

- [x] Use the returned alias or use `jQuery` instead of `$`
- [ ] jQuery cannot be used after noConflict
- [ ] Use `window.$`
- [ ] Reload jQuery

**Explanation:**
After `$.noConflict()`, you can use the returned alias or use `jQuery` instead of `$` to access jQuery functionality.

[Reference](https://api.jquery.com/jQuery.noConflict/)

#### Q153. What is the purpose of `$.fn.extend()`?

- [ ] To extend functions
- [x] To add multiple methods to jQuery.fn (for plugins)
- [ ] To extend jQuery core
- [ ] To create extensions

**Explanation:**
`$.fn.extend()` adds multiple methods to `jQuery.fn`, useful for creating plugins with multiple methods.

[Reference](https://api.jquery.com/jQuery.fn.extend/)

#### Q154. What is the difference between `$.extend()` and `$.fn.extend()`?

- [x] `$.extend()` extends jQuery itself, `$.fn.extend()` extends jQuery.fn (prototype)
- [ ] `$.fn.extend()` is for functions
- [ ] `$.extend()` is deprecated
- [ ] There is no difference

**Explanation:**
`$.extend()` adds methods to the jQuery object itself (utility functions). `$.fn.extend()` adds methods to jQuery.fn (instance methods).

[Reference](https://api.jquery.com/jQuery.extend/)

#### Q155. How do you check the jQuery version?

- [ ] `$.version`
- [x] `$.fn.jquery` or `jQuery.fn.jquery`
- [ ] `jQuery.version`
- [ ] `$().version`

**Explanation:**
The jQuery version is stored in `$.fn.jquery` (or `jQuery.fn.jquery`).

[Reference](https://api.jquery.com/jquery-2/)

#### Q156. What is jQuery Migrate plugin used for?

- [ ] To migrate to jQuery
- [x] To restore deprecated features and provide warnings about removed features
- [ ] To migrate from other libraries
- [ ] To update jQuery version

**Explanation:**
jQuery Migrate plugin restores deprecated features removed from jQuery and provides console warnings to help identify deprecated code.

[Reference](https://github.com/jquery/jquery-migrate)

#### Q157. How do you create a deep copy of an object in jQuery?

```js
var copy = $.extend(true, {}, original);
```

- [x] Use `$.extend(true, {}, original)`
- [ ] Use `$.clone(original)`
- [ ] Use `$.copy(original)`
- [ ] Use `$.deepCopy(original)`

**Explanation:**
`$.extend(true, target, source)` performs a deep copy when the first parameter is `true`.

[Reference](https://api.jquery.com/jQuery.extend/)

#### Q158. What is the purpose of `$.grep()`?

- [ ] To search text
- [x] To filter an array using a filter function
- [ ] To grep files
- [ ] To search DOM

**Explanation:**
`$.grep()` filters an array using a filter function, returning a new array with elements that pass the test.

[Reference](https://api.jquery.com/jQuery.grep/)

#### Q159. What is the purpose of `$.map()`?

- [ ] To create maps
- [x] To translate all items in an array or object to new array of items
- [ ] To map DOM elements
- [ ] To create mappings

**Explanation:**
`$.map()` translates all items in an array or object to a new array of items using a translation function.

[Reference](https://api.jquery.com/jQuery.map/)

#### Q160. How do you merge two arrays in jQuery?

```js
var result = $.merge(array1, array2);
```

- [x] Use `$.merge(first, second)`
- [ ] Use `$.concat(first, second)`
- [ ] Use `$.join(first, second)`
- [ ] Use `first + second`

**Explanation:**
`$.merge()` merges the contents of two arrays into the first array, modifying the first array and returning it.

[Reference](https://api.jquery.com/jQuery.merge/)
