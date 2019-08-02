jQuery Assessment
-----------------

#### Q1. What's the difference between these two snippets?
`$('button').on('click', function(){
     alert('you clicked the button!');
 });
 $('button').click(function(){
     alert('you clicked the button!');
 });`
- Only the second one will work; jQuery does not have a function called .on.
- The second snippet will not function.
- Nothing - .click(function) is shorter way to write .on('click', function)
- The first snippet will execute for every button on the page, the second will only apply to the first button

#### Q2. What does the following line of code do?
`jQuery('p')`
- Loads a paragraph tag from a remote server using AJAX
- Aliases jQuery to a variable p
- Selects all paragraphs on the page 
- Creates a new paragraph tag and inserts it into the body tag
 
#### Q3. Give the following HTML, how could we use one line to hide or show the button?
`<button class="btn btn-primary" type="submit">Continue to checkout</button>`
- $('.btn-primary').toggle();
- $('.btn-primary').showHide();
- $('.btn-primary').not(':visible').show();
- $('.btn-primary').css({ display: 'block'});

#### Q4. Working with AJAX, we may run into situations where a piece of code should not be run until after multiple AJAX,
#### calls have completed successfully. Say we need to call two external services for JSON data (a list of students, and 
#### a list of classes). And only after retrieving those data will we perform some manipulations on a page. What is the 
#### preferred way for dealing with this scenario?
#### https://example.com/json-api/students https://example.com/json-api/classes
`$.get([
      'https://example.com/json-api/students',
      'https://example.com/json-api/classes'
   ], function(studentRequest, classRequest) {
      // the rest of the code goes here
});`

`$.when(
      $.get('https://example.com/json-api/students'),
      $.get('https://example.com/json-api/classes')
   ).done(function(studentRequest, classRequest) {
      // the rest of the code goes here
});`

`$.bind(
      $.get('https://example.com/json-api/students'),
      $.get('https://example.com/json-api/classes')
   ).done(function(studentRequest, classRequest) {
      // the rest of the code goes here
});`

`$.ajax('https://example.com/json-api/students', {
   success: function(studentRequest) {
        $.ajax('https://example.com/json-api/classes', {
            success: function(classRequest) {
              // the rest of the code goes here
              }
        });
   }
});`   

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
- .get() retrieves a jQuery object, and can't be chained, eq() retrieves a DOM element, and can be chained.
- .get() retrieves a jQuery object, and is zero-indexed, eq() retrieves a DOM element, and is 1-indexed.
- .get() retrieves a DOM element, and is zero-indexed, eq() retrieves a jQuery object, and is 1-indexed.

#### Q6. Suppose we want to have an ball created from an HTML element (id=ball) move down and to the right
#### from its original location when clicked, and move back into its original place when finished. Given a starting
#### point of this, which of these snippets would accomplish that goal?
$('#ball').click(function() {
    // Our code goes here
});

`$(this).animate({
    top: '+=100',
    left: '+=100',
}, {
    duration: 600,
    complete: function() {
        $(this).animate({
            top: '-=100',
            left: '-=100',
        }, 600)
    }
});`

`$(this).animate({
    top: '-=100',
    left: '-=100',
}, 600, function() {
        $(this).animate({
            top: '+=100',
            left: '+=100',
        }, 600)
    }
});`       

`$(this).animate({
    top: '=100',
    left: '=100',
}, {
    duration: 600,
    complete: function() {
        $(this).animate({
            top: 0,
            left: 0,
        }, 600)
    }
});`

`$(this).animate({
    top: '100',
    left: '100',
}, 600, function() {
        $(this).animate({
            top: 0,
            left: 0,
        }, 600)
    }
});`

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
- `$('.feedback').addClass('.success');`
- `$('.feedback').css('.success');`

#### Q8. Below an example page snippet that includes a couple of messages in a list, and a code snippet that
#### retrieves a few hundred messages from a API endpoints using AJAX. How might we add these items to the 
#### page snippet in a way that avoids performance problems with DOM insertions?

<div class="message-area">
    <ul class="message-area--list">
        <li>Existing message 1</li>
        <li>Existing message 2</li>
    </ul>
</div>

$.get('//example.com/api/v1/message')
    .done(function(data) {
        var tonsOfItems = data.messages;
        // add all these messages to a large page
});

`tonsOfItems.map(function(item) {
     $('.message-area--list').append('<li>'+item+'</li>');
});`

var tonsOfListItems = tonsOfItems.map(function(itme))  {
     return '<li>'+item+'</li>';
});
$('.message-area--list').append(tonsOfListItems.join(''))  
