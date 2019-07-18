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
$.get([])
