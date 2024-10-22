## PHP

#### Q1. What does this code output?

`echo 76 <=> '76 trombones';`

- [ ] 1
- [ ] -1
- [ ] a parser error
- [x] 0

**_Both sides of the "spaceship" are equal, so the answer is 0. PHP will convert '76 trombones' to 76 in this context, as the string starts with '76'. Try it!_**
**_For php 8.0 and forward the answer is [x] -1, for previous versions the answer is [x] 0._**
[PHP 8 changed the way non-strict comparison between numbers and non-numeric strings work.](https://www.php.net/manual/en/migration80.incompatible.php#migration80.incompatible.core.string-number-comparision)

#### Q2. Which is the most secure way to avoid storing a password in clear text in database?

- [ ] `$encrypted = shal($password);`
- [ ] `$encrypted = crypt($password, \$salt);`
- [ ] `$encrypted = md5($password);`
- [x] `$encrypted = password_hash($password, PASSWORD_DEFAULT);`

#### Q3. What does this script do?

```php
$email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);
if ($email === false) {
    $emailErr = "Please re-enter valid email";
}
```

- [ ] It makes sure the email address is a good and functioning address
- [ ] It makes an email safe to input into a database
- [ ] It assigns an email to a variable and then removes all illegal characters from the \$email variable
- [x] It verifies that an email address is well formed.

#### Q4. In the following script, which line(s) will cause an error(s)?

```php
1 <?php
2       $count = 0;
3       $_xval = 5;
4       $_yval = 1.0;
5       $some_string = "Hello there!";
6       $some_string = "How are you?";
7       $will i work = 6;
8       $3blindmice = 3;
9 ?>
```

- [ ] Line 6 will cause an error because you can't reassign a new value to a variable that has already been set.
- [x] Line 7 and 8 will cause an error. Line 7 has whitespace in $will i work and should be $will_i_work. Line 8 cannot start with a number befcause it is a variable.
- [ ] Line 5 will cause an error because some_string should be someString.
- [ ] Line 3 and 4 will cause an error because a variable cannot start with an underscore(\_).

#### Q5. In a conditional statement, you want to execute the code only if both value are true. Which comparison operator should you use?

- [ ] ||
- [ ] &
- [ ] <=>
- [x] &&

#### Q6. All variables in PHP start with which symbol?

- [ ] &
- [ ] %
- [ ] \_
- [x] $

#### Q7. What is a key difference between GET and POST?

- [ ] GET is used with the HTTP protocol. POST is used with HTTPS.
- [x] GET displays the submitted data as part of the URL. During POST, this information is not shown, as it's encoded in the request body.
- [ ] GET is intended for changing the server state and it carries more data than POST.
- [ ] GET is more secure than POST and should be used for sensitive information.

#### Q8. The **operator is useful for sorting operations. It compares two values and returns an integer less than, equal to, or greater than 0 depending on whether the value on the** is less than, equal to, or greater than the other

- [ ] greater-than; right
- [x] spaceship; left
- [ ] equality; right
- [ ] comparison; left

#### Q9. Which are valid PHP error handling keywords?

- [ ] try, throw, catch, callable
- [ ] try, yield, catch, finally
- [ ] yield, throw, catch, finally
- [x] try, throw, catch, finally

#### Q10. Which value equates to true?

- [ ] 0
- [ ] NULL
- [ ] ''
- [x] -1

#### Q11. What is missing from this code, which is supposed to create a test cookies?

```php
$string_name = "testcookie";
$string_value = "This is a test cookie";
$expiry_info = info()+259200;
$string_domain = "localhost.localdomain";
```

- [ ] The `$_REQUEST` is missing.
- [ ] The `$_COOKIES` array is missing.
- [ ] The cookie session is missing.
- [x] The call to `setcookie()` is missing.

#### Q12. What is the value of \$total in this calculation?

`$total = 2 + 5 * 20 - 6 / 3`

- [ ] 44
- [ ] 138
- [ ] 126
- [x] 100

#### Q13. What is the purpose of adding a lowercase "u" as a modifier after the final delimiter in a Perl-compatible regular expression?

- [ ] It makes the dot metacharacter match anything, including newline characters.
- [ ] It makes the pattern match uppercase letters.
- [x] Both the pattern and subject string are treated as UTF-8.
- [ ] It inverts the greediness of the quantifiers in the pattern so they are not greedy by default.

#### Q14. Which code snippet uses the correct syntax for creating an instance of the Pet class?

- [ ] `$dog = new Pet;`
- [x] all of these answers
- [ ] `$horse = (new Pet);`
- [ ] `$cat = new Pet();`

#### Q15. What is the best way to explain what this script does?

```php
if (!$_SESSION['myusername'])
{
  header('locaton: /login.php');
  exit;
}
```

- [ ] This script times out the session for myusername.
- [ ] Cookies are starting to be stored as a result of this script.
- [ ] This script validates the username and password.
- [x] This script is on a page that requires the user to be logged in. It checks to see if the user has a valid session.

#### Q16. Which is the correct format for adding a comment to a PHP script?

- [x] all of these answers
- [ ] #This is a comment
- [ ] `/* This is a comment */`
- [ ] // This is a comment

#### Q17. PHP supports multiple types of loops. If you wanted to loop through a block of code if and as long a specified condition is true, which type of loop would you use?

- [ ] for
- [ ] do-while
- [x] while
- [ ] foreach

#### Q18. The `ignore_user_abort( )` function sets whether a client disconnect should abort a script execution. In what scenario would you, as a web developer, use this function?

- [ ] You would use it to stop a user from clicking the back button if they decide not to view as a result of a click.
- [x] You would use this function if you have some important processing to do and you do not want to stop it, even if your users click Cancel.
- [ ] You would use this function if you wanted to abort the script for all logged-in users, not just the one who disconnected.
- [ ] You would use this function if you want a PHP script to run forever.

#### Q19. The PHP function array_reduce() takes a callback function that accepts a value carried over each iteration and the current item in the array, and reduces an array to a single value. Which code sample will sum and output the values in the provided array?

- [ ] &shy;

```php
  <?php
  echo array_reduce([1, 2, 5, 10, 11], function ($item, $carry) {
      $carry = $carry + $item;
  });
?>
```

- [ ] &shy;

```php
  <?php
  echo array_reduce([1, 2, 5, 10, 11], function ($carry, $item) {
      return $carry = $item + $item;
  });
?>
```

- [ ] &shy;

```php
  <?php
  array_reduce([11 2, 5, 10, 11], function ($item, $carry) {
      echo $carry + $item;
  });
?>
```

- [x] &shy;

```php
  <?php
  echo array_reduce([1, 2, 5, 10, 11], function ($carry, $item) {
      return $carry += $item;
  });
?>
```

#### Q20. Which PHP script uses a constructor to display the string "Winter is almost over!"?

- [x] &shy;

```php
  class MyClass {
  public function _construct()
  {
  echo 'Winter is almost over!'."\n";
  }
  }
  $userclass = new MyClass;
```

- [ ] &shy;

```php
  class MyClass {
  public function _construct()
  {
  echo 'Winter is almost over!.."\n";
  }
  }
  $userclass = new MyClass;
```

- [ ] &shy;

```php
  class MyClass {
  public function _construct()
  {
  echo 'Winter is almost over!.."\n";
  }
  }
  $userclass = new MyClass;
```

- [ ] &shy;

```php
  class MyClass {
  public function _construct()
  {
  echo 'Winter is almost over!'."n";
  }
  }
  $userclass = MyClass;
```

#### Q21. How might you troubleshoot a "call to undefined function" error?

- [ ] Make sure you have imported the file containing the function.
- [ ] Make sure you have spelled the function name correctly.
- [x] all of these answers
- [ ] Make sure the function declaration is at an earlier point in the code than the function call.

#### Q22. Which line could you NOT use to comment out "Space: the final frontier"?

- [ ] `/* Space: the final frontier */`
- [x] `*/ Space: the final frontier /*`
- [ ] `#Space: the final frontier`
- [ ] `// Space: the final frontier`

#### Q23. What displays in a browser when the following code is written? `<?php echo "How much are the bananas?"?>`

- [ ] The browser would display nothing due to a syntax error.
- [ ] The browser would display an error, since there are no parentheses around the string.
- [x] The browser would display `How much are the bananas?`
- [ ] The browser would display an error, since there is no semicolon at the end of the echo command.

#### Q24. Which operator would you use to find the remainder after division?

- [ ] /
- [x] %
- [ ] //
- [ ] DIV

#### Q25. What is the significance of the three dots in this function signature?

```php
function process(...$vals) {
    // do some processing
}
```

- [ ] It makes the function variadic, allowing it to accept as an argument an array containing an arbitrary number of values.
- [x] It makes the function variadic, allowing it to accept an arbitrary number of arguments that are converted into an array inside the function.
- [ ] It temporarily disables the function while debugging other parts of the script.
- [ ] It's a placeholder like a TO DO reminder that automatically triggers a notice when you run a script before completing the function definition.

#### Q26. Assuming the `Horse` class exists, which is a valid example of inheritance in PHP?

- [x] `class Pegasus extends Horse {}`
- [ ] `class Alicorn imports Pegasus, Unicorn {}`
- [ ] `class Unicorn implements Horse {}`
- [ ] `class Horse inherits Unicorn {}`

#### Q27. Both triple === and double == can be used to **variables in php. If you want to hear that string "33" and the number 33 are equal, you would use** . If you want to check if an array contains a particular string value at a particular index, you would use \_

- [x] compare; doubles; triples
- [ ] compare; triples; doubles
- [ ] assign; triples; doubles
- [ ] assign; doubles; triples

#### Q28. Your php page is unexpectedly rendering as totally blank. Which step will shed light on the problem?

- [ ] Add this code to the top of your script: `ini_set('display_errors',1);`
- [ ] check the server error logged
- [x] all of these answers
- [ ] make sure you are not missing any semicolons

#### Q29. Which is the way to create an array of "seasons"?

- [ ] &shy;

```php
seasons=array(
    1=>'spring',
    2=>'summer',
    3=>'autumn',
    4=>'winter',
);
```

- [ ] `$seasons=array(spring,summer,autumn,winter);`
- [ ] `$seasons=('spring','summer','autumn','winter');`
- [x] `$seasons=['spring','summer','autumn','winter'];`

#### Q30. Both `self` and `this` are keywords that can be used to refer to member variables of an enclosing class. The difference is that `$this->member` should be used for **members and `self::$member` should be used for** members

- [ ] private, public
- [ ] object,primitive
- [x] non-static,static
- [ ] concrete,abstract

#### Q31. What will this code print?

```php
$mathe=array('archi','euler','pythagoras');
array_push($mathe,'hypatia');
array_push($mathe,'fibonacci');
array_pop($mathe);
echo array_pop($mathe);
echo sizeof($mathe);
```

- [ ] euler3
- [ ] hypatia5
- [x] hypatia3
- [ ] fibonacci4

#### Q32. You are using the following code to find a users band, but it is returning false. Which step(s) would solve the problem?

`isset ($_GET['fav_band'])`

- [ ] check if `fav_band` is included in the query string at the top of your browser
- [x] all of the answers
- [ ] view the source of form and make sure there is an input field with the name 'fav_band'
- [ ] print everything that has been transmitted in the request: `print_r($_REQUEST);`

#### Q33. Which code would you use to print all the elements in an array called `$cupcakes`?

- [x] all of the answers
- [ ] `print_r($cupcakes);`
- [ ] `var_dump($cupcakes);`
- [ ] `foreach($cupcakes as &$cupcake) echo $cupcake;`

#### Q34. What is the cause of 'Cannot modify header information - headers already sent'?

- [ ] You are trying to modify a private value
- [ ] Semicolon missing
- [ ] Using a key on an array that does not exists
- [x] Some html is being sent before a `header()` command that you are using for a redirect

#### Q35. Which php control structure is used inside a loop to skip the rest of the current loops code and go back to the start of the loop for the next iteration

- [ ] `else`
- [ ] `break`
- [ ] `return`
- [x] `continue`

#### Q36. The php not operator is !. Given the snippet, is there an out put and what is it?

- [ ] there is an output '2 is an even number
- [x] output '21 is an odd number'
- [ ] no output. Syntax error do to missing semicolon at the end
- [ ] no output due to % in \$num%2!=0

#### Q37. You want to list the modules available in your PHP installation. What command should you run?

- [ ] `php -h`
- [ ] `php info`
- [ ] `php -v`
- [x] `php -m`

#### Q38. For the HTML form below, what is the correct functioning script that checks the input "mail" to be sure it is filled before proceeding?

```php
if (!empty($_POST["mail"])) {
echo "Yes, mail is set";
} else {
echo "No, mail is not set";
} (correct)
```

- [ ] ...

#### Q39. What is the value of `$result` in this calculation?

`$result = 25 % 6;`

- [ ] 4.167
- [ ] 1.5
- [ ] 4
- [x] 1

#### Q40. What is the job of the controller as a component in MVC?

- [x] The controller handles data passed to it by the view, and also passes data to the view. It interprets data sent by the view and disperses that data to the approrpiate models awaiting results to pass back to the view.
- [ ] The controller is a mechanism that allows you to create reusable code in languages such as PHP, where multiple inheritance is not supported.
- [ ] The controller presents content through the user interface, after communicating directly with the database.
- [ ] The controller handles specific tasks related to a specific area of functionality, handles business logic related to the results, and communicates directly with the database.

#### Q41. Why does this code trigger an error?

`$string = 'Shylock in a Shakespeare's "Merchant of Venice" demands his pound of flesh.';`

- [ ] Strings should always be wrapped in double quotes; and double quotes inside a string should be escaped by backslashes.
- [ ] All single and double quotes inside a string need to be escaped by backslashes to prevent a parse error.
- [ ] The opening and closing single quotes should be replaced by double quotes; and the apostrophe should be escaped by a backslash.
- [x] The apostrophe needs to be escaped by a backslash to prevent it from being treated as the closing quote.

#### Q42. A PDO object called `$db` has been set up to use for database operations, including user authentication. All user-related properties are set. The script line `public function __construct(&$db)` shows a constructor that initializes all user-related properties to \_ if no user has logged in. These parameters will be properly set by the login functions when a user logs in

- [x] NULL
- [ ] TRUE
- [ ] FALSE
- [ ] 0

#### Q43. Assuming that `$first_name` and `$family_name` are valid strings, which statement is invalid?

- [ ] `echo $first_name. ' '. $family_name;`
- [x] `print $first_name, ' ', $family_name;`
- [ ] `print $first_name. ' '. $family_name;`
- [ ] `echo $first_name, ' ', $family_name;`

#### Q44. Which code snippet demonstrates encapsulation?

- [ ] &shy;

```php
  class Cow extends Animal {
      private $milk;
  }
```

- [ ] &shy;

```php
  class Cow {
      public $milk;
  }
  $daisy = new Cow();
  $daisy->milk = "creamy";
```

- [ ] &shy;

```php
  class Cow {
      public $milk;
      function getMilk() {`
          return $this->milk;
      }
  }
```

- [x] &shy;

```php
  class Cow {
      private $milk;
      public function getMilk() {
          return $this->milk;
      }
  }
```

#### Q45. The following XML document is in books.xml. Which code will output "Historical"?

```xml
<books>
    <book>
        <title>A Tale of Two Cities</title>
        <author>Charles Dickens</author>
        <categories>
            <category>Classics</category>
            <category>Historical</category>
        </categories>
    </book>
    <book>
        <title>Then There Were None</title>
        <author>Agatha Christies</author>
        <categories>
            <category>Mystery</category>
        </categories>
    </book>
</books>
```

- [ ] &shy;

```php
  $books = simplexml_load_string('books.xml');
  echo $books->book[0]->categories->category[1];
```

- [x] &shy;

```php
  $books = simplexml_load_file('books.xml');
  echo $books->book[0]->categories->category[1];
```

- [ ] &shy;

```php
  $books = SimpleXMLElement('books.xml');
  echo $books->book[0]->categories->category[1];
```

- [ ] &shy;

```php
  $books = SimpleXML('books.xml');
  echo $books->book[0]->categories->category[1];
```

#### Q46. When it comes to the value of a variable, what is the difference between NULL and empty?

- [ ] NULL is a blank value; empty is the lack of a value.
- [ ] A NULL value has an allocated address in memory; empty does not.
- [ ] NULL referes to the lack of a value for an integer; empty refers to the lack of a value for a string.
- [x] NULL is the lack of a value; empty is a blank value.

#### Q47. What would be a good name for this function?

```php
function doStuff($haystack, $needle) {
      $length = strlen($needle)
      if (substr($haystack, 0, $length) == $needle)
        return true;
      else
        return false;
}
```

- [ ] `equals`
- [ ] `endsWith`
- [x] `startsWith`
- [ ] `contains`

#### Q48. If you want to pass a formfield to another page when a button is clicked, you should use the **. If you want to store information across multiple pages, you should use the** ?

- [ ] request; response
- [ ] response; request
- [ ] session; request
- [x] request; session

#### Q49. You are using the following code to decide if a button is clicked, but it is never returning true. Which step is most likely to shed light on the problem?

```php
isset($_POST['submit'])
```

- [x] Make sure the input field displaying the button is named 'submit'
- [ ] Make sure you are not missing any semicolons
- [ ] Print everything in the session `print_r($_SESSION);`
- [ ] Look in the query string at the top of your browser to see if submit is assigned a value

#### Q50. Why should you follow a PSR standard?

- [x] because coding standards often vary between developers and companies
- [ ] because coding standards are monitored for compliance across developers and companies
- [ ] because there are mandatory coding standards among developers and companies
- [ ] if using certain platforms, because the PSR's apply to those platforms only

#### Q51. What are getters and setters?

- [ ] Getters and setters ensure that if a data member is declared private, then it can be accessed only within the same function, not by an outside class
- [ ] Getters and setters are utility functions within PHP that allow loading from, and saving to, a database
- [ ] Getters and setters encapsulate the fields of a class by making them acccessible only through its private methods, and keep the values themselves public
- [x] Getters and setters are methods used to declare or obtain the values of variables, usually private ones

#### Q52. What are the recommended settings in the PHP configuration file, php.ini, for a testing environment?

- [ ] &shy;

```php
  report_errors = E_ALL
  display_errors = On
```

- [x] &shy;

```php
  error_reporting = E_ALL
  display_errors = On
```

- [ ] &shy;

```php
  error_reporting = E_ALL & ~E_NOTICE
  display_errors = Off
```

- [ ] &shy;

```php
  error_reporting = E_ALL & ~E_NOTICE
  display_errors = On
```

#### Q53. Which PHP variable name is invalid?

- [ ] `$Double`
- [ ] `$double`
- [ ] `$_2times`
- [x] `$2times`

#### Q54. Which command will extract the domain suffix ("com") from the string `$string = "https://cat-bounce.com";`?

- [ ] `sub($string, -3)`
- [x] `substr($string, -3)`
- [ ] `substr($string, 3)`
- [ ] `$string.substr(-3)`

#### Q55. Where is PHP code executed?

- [ ] in the client's browser
- [ ] in the virtual machine
- [ ] in the memory of the computer viewing the webpage
- [x] on a web server

#### Q56. Which is not a valid magic constant?

- [x] `__RESOURCE__`
- [ ] `__FUNCTION__`
- [ ] `__CLASS__`
- [ ] `__TRAIT__`

[Reference](https://www.php.net/manual/en/language.constants.magic.php)

#### Q57. What below script will print?

```php
  if( 1 == true){
        echo "1";
  }

  if( 1 === true){
      echo "2";
  }

  if("php" == true){
      echo "3";
  }

  if("php" === false){
      echo "4";
  }
```

- [ ] 134
- [x] 13
- [ ] 1
- [ ] 123

#### Q58. When should this php script be used?

```php
$secret_word = 'if i ate spinach';
setcookie('login', $_REQUEST['username']. ','. md5($_REQUEST['username'].$secret_word));
```

- [ ] when a user goes to pay for an item online
- [ ] when items are placed in a cart
- [ ] at first registration
- [x] at every login, for security

#### Q59. A PHP "variable variable" takes the value of a variable and treats that as the name of a variable. For example, if `$var` is a variable then `$$var` is a variable variable whose name is the value of `$var`. Which script produces the output below, using variable variables?

```plaintext
Cat
Dog
Dog
```

- [ ] :

```php
  $name = "Cat";
  $name = "Dog";
  echo $name . "<br/>";
  echo $$name . "<br/>";
  echo $Dog;
```

- [ ] :

```php
  $name = "Cat";
  $$name = "Dog";
  echo $name . "<br/>";
  echo $$name . "<br/>";
  echo $Dog;
```

- [x] :

```php
  $name = "Cat";
  $$name = "Dog";
  echo $name . "<br/>";
  echo $$name . "<br/>";
  echo $Cat;
```

- [ ] :

```php
  $name = "Cat";
  $$name = "Dog";
  echo $name . "<br/>";
  echo $name . "<br/>";
  echo $Cat;
```

#### Q60. Imagine a web application, built following a MVC architecture, that contains a quiz and a button to score it, When the user presses the Score button, which component should handle the request?

- [ ] router
- [x] controller
- [ ] model
- [ ] view

#### Q61. Which script might be used to continue a user's search for music, across different webpages?

- [ ] &shy;

```php
  <?php
      start_session();
      $music = $_SESSION['music'];
  ?>
```

- [ ] &shy;

```php
  <?php
      session_start();
      $music = $SESSION['music'];
  ?>
```

- [ ] &shy;

```php
  <?php
      start_session();
      $music =$session['music'];
  ?>
```

- [x] &shy;

```php
  <?php
      session_start();
      $music = $_SESSION['music'];
  ?>
```

#### Q62. Which PHP script finds the earliest and latest dates from an array?

- [x] &shy;

```php
  <?php
  $dates = array('2018-02-01', '2017-02-02', '2015-02-03');
  echo "Latest Date: ". max($dates)."\n";
  echo "Earliest Date: ". min($dates)."\n";
  ?>
```

- [ ] &shy;

```php
  <?php
  $dates = array('2018-02-01', '2017-02-02', '2015-02-03');
  echo "Latest Date: ". min($dates)."\n";
  echo "Earliest Date: ". max($dates)."\n";
  ?>
```

- [ ] &shy;

```php
  <?php
  $dates = array('2018-02-01', '2017-02-02', '2015-02-03');
  echo "Latest Date: ". ($dates)."\n";
  echo "Earliest Date: ". ($dates)."\n";
  ?>
```

- [ ] &shy;

```php
  <?php
  $dates = array('2018-02-01', '2017-02-02', '2015-02-03');
  echo "Latest Date: " max($dates)."\n";
  echo "Earliest Date: " min($dates)."\n";
  ?>
```

#### Q63. What is the resulting output of this for statement?

```php
$kilometers = 1;
for (;;) {
    if ($kilometers > 5) break;
       echo "$kilometers kilometers = ".$kilometers*0.62140. " miles. <br />";
    $kilometers++;
}
```

- [x] &shy;

```
  kilometers = 0.6214 miles.
  kilometers = 1.2428 miles.
  kilometers = 1.8642 miles.
  kilometers = 2.4856 miles.
  kilometers = 3.107 miles.
```

- [ ] &shy;

```
  kilometers = 0.6214 miles.
  kilometers = 1.2428 miles.
  kilometers = 1.8642 miles
  kilometers = 2.4856 miles.
  kilometers = 3.107 miles.
  kilometers = 3.7284 miles.
```

- [ ] &shy;

```
  kilometers = 1.2428 miles.
  kilometers = 1.8642 miles.
  kilometers = 2.4856 miles.
  kilometers = 3.107 miles.
```

- [ ] FATAL ERROR syntax error, unexpected ')', expecting ';' on line number 2

#### Q64. In PHP 7, What is the correct way to import multiple classes from namespace in a single declaration ?

- [x] use myApp\myNamespace\{ClassA, ClassB, ClassC};
- [ ] use myApp\myNamespace\ClassA, ClassB, ClassC;
- [ ] use myApp\myNamespace\[ClassA, ClassB, ClassC];
- [ ] use myApp\myNamespace\(ClassA, ClassB, ClassC);

#### Q65. Which is the most complete list of data types that PHP supports?

- [x] string, integer, float, boolean, array, object, NULL, resource
- [ ] string, integer, boolean, array, object, NULL, resource
- [ ] string, integer, float, array, object, NULL, resource
- [ ] string, integer, float, boolean, array, object, NULL

[reference](https://www.w3schools.com/php/php_datatypes.asp)

#### Q66. What type of computer language is PHP?

- [x] server-side scripting language
- [ ] compiled language
- [ ] machine language
- [ ] algorithmic language

[reference](https://www.quora.com/Which-programming-language-is-used-to-create-PHP)

#### Q67. Which superglobal variable holds information about headers, paths, and script locations?

- [x] `$_SERVER`
- [ ] `$SERVER_VARIABLES`
- [ ] `$_ENV`
- [ ] `$GLOBALS`

[reference](http://www-db.deis.unibo.it/courses/TW/DOCS/w3schools/php/php_superglobals.asp.html)

#### Q68. Describe what happens if you run this code in a testing environment

```php
$capitals = ['UK' => 'London', 'France' => 'Paris'];
echo "$capitals['france'] is the capital of France.";
```

- [ ] It displays: "Paris is the capital of France."
- [ ] It displays: " is the capital of France."
- [ ] It triggers a syntax error because the array keys on line 1 are in quotes.
- [x] It triggers a syntax error because the array key on line 2 is in quotes.

**_Also, 'france' key must be capitalized!_**

#### Q69. DRY (Don't Repeat Yourself) is a principle of software development aimed at reducing repetition of software patterns. Which choice is not a way to write DRYer code with PHP?

- [ ] inheritance
- [ ] classes
- [x] namespacing
- [ ] dependency injection

#### Q70. Which code will return the IP address of the client?

- [ ] `$HTTP_SERVER_VARS("REMOTE_IP")`
- [x] `$_SESSION["REMOTE_ADDR"];`
- [ ] `$_SERVER["HTTP_X_FORWARDED_FOR"]`
- [x] `getenv("REMOTE_ADDR")`

**_Both 2 and 4 are correct!_**

#### Q71. Your site must allow uploading of large files. What might you need to do?

- [ ] Make sure the user has the proper permissions.
- [ ] Keep a count of upload file sizes and log them.
- [x] Change the `upload_max_filesize` configuration parameter.
- [ ] Be sure to use chunked transfer encoding.

#### Q72. What is the output of this script?

```php
$my_text = 'The quick grey [squirrel].';
preg_match('#\[(.*?)\]#', $my_text, $match);
print $match[1]."\n";
```

- [x] squirrel
- [ ] The quick grey [squirrel].
- [ ] [squirrel]
- [ ] The quick grey squirrel.

#### Q73. What is the output of this script?

`$fruits = ['apple', 'orange', 'pear', 'mango', 'papaya'];`
`$i = 0;`
`echo $fruits[$i+=3];`

- [x] mango
- [ ] apple
- [ ] a parse error
- [ ] pear

#### Q74. What are some of the main types of errors in PHP?

- [x] notices, warnings, fatal
- [ ] runtime, logical, compile
- [ ] semantic, logical, syntax
- [ ] warnings, syntax, compile

#### Q75. What is the correct way to include the file gravy.php in the middle of HTML code?

- [ ] `<!-- include file="gravy.php"; -->`
- [ ] `<?php include gravy.php; ?>`
- [x] `<?php include "gravy.php"; ?>`
- [ ] `<?php include file="gravy.php"; ?>`

#### Q76. Which two functions can sanitize text and validate text formats?

- [ ] `session_start()` and `filter_input()`
- [x] `filter_var()` and `filter_input()`
- [ ] `preg_match()` and `strstr()`

#### Q77. Why is it not recommended to make all of a class's variables public?

- [ ] Doing so makes your code tightly coupled.
- [ ] The attribute may be accessed only by the class that defines the member.
- [x] You will have no control over which values the attribute can take. Any external code will be able to change it without any constraint.
- [ ] You can then access the attribute only within the class itself, and by inheriting and parent classes.

#### Q78. You want to use wildcard characters when searching for records in a MySQL/MariaDB database using a PDO prepared statement. Which code should you use?

- [x] `$statement->bindValue(':name', '%' . $_GET['name'] . '%');`
- [ ] `$statement->bindValue('%' . $_GET['name'] . '%', ':name');`
- [ ] `$statement->bindParam(':name', '%' . $_GET['name'] . '%');`
- [ ] `$statement->bindParam('%' . $_GET['name'] . '%', ':name');`

#### Q79. Create an associative array using `$array1` as the keys and `$array2` as the values

`$array1 = ['country', 'capital', 'language'];`
`$array2 = ['France', 'Paris', 'French'];`

- [ ] `$array3 = array_merge($array1, $array2);`
- [ ] `$array3 = array_union($array1, $array2);`
- [ ] `$array3 = array_keys($array1, $array2);`
- [x] `$array3 = array_combine($array1, $array2);`

#### Q80. Assume that `$r` is 255, and `$g` and `$b` are both 0. What is the correct code to output `"#ff0000"`?

- [ ] `printf('#%2x%2x%2x', 255, 0, 0);`
- [ ] `printf('#%2X%2X%2X', $r, 0, 0);`
- [ ] `printf('#%x%x%x', 255, 0, 0);`
- [x] `printf('#%02x%02x%02x', 255, 0, 0);`

#### Q81. You want to find out what day Twelfth Night falls on after Christmas 2018. Which code should you use?

- [ ] `$xmas = new DateTime('Dec 25, 2018');`
      `$twelfth_night = $xmas->add(new DateInterval('P12D'));`
      `echo $twelfth_night->format('l');`
- [ ] `$twelfth_night = strtotime('December 25, 2018 + 12 days');`
      `echo date('d', $twelfth_night);`

- [x] `$twelfth_night = strtotime('December 25, 2018 + 12 days');`
      `echo strftime('%d', $twelfth_night);`

- [ ] `$xmas = new DateTime('Dec 25, 2018');`
      `$twelfth_night = $xmas->add(strtotime('12 days'));`
      `echo $twelfth_night->format('D');`

**_1 seems correct, but the question asks for "day", not day of the week. Twelfth Night is the "06" day of January, 2019._**

#### Q82. Which loop displays all numbers from 1 to 10 inclusive?

- [ ] `$i = 1;`
      `while ($i < 10) {`
      `echo $i++ . '<br/>';`
      `}`

- [ ] `$i = 0;`
      `while ($i <= 10) {`
      `echo $i++ . '<br/>';`
      `}`

- [ ] `while ($i &lt;= 10) {`
      `echo ++$i . '<br/>';`
      `}`

- [x] `$i = 0;`
      `while ($i < 10) {`
      `echo ++$i . '<br/>';`
      `}`

#### Q83. Which are types of control structures in PHP?

- [x] `break`, `continue`, `do-while`, `exception`, `for`, `foreach`, `if`, `switch`, `throw`, `while`
- [ ] `values`, `operators`, `expressions`, `keywords`, `comments`
- [ ] `for`, `foreach`, `if`, `else`, `else if`, `switch`, `tries`, `throws`, `while`
- [ ] `if-then-else`, `do-while`, `for-each`, `go-to`, `stop-when`

[reference](https://www.php.net/manual/en/language.control-structures.php)

#### Q84. Which function can you use in error handling to stop the execution of a script and is equivalent to exit()?

- [x] `die`
- [ ] `return`
- [ ] `throw`
- [ ] `break`

#### Q85. Is the output of this code in descending order, shown vertically, and with spaces between numbers? And what is the output?

```php
$numbers = array(4,6,2,22,11);
sort($numbers);
$arrlength = count($numbers);
for($x = 0; $x < $arrlength; $x++){
    echo $numbers[$x];
    echo "<br />";
    }
```

- [ ] This does not meet all the criteria because the resulting numbers will be "2461122", which is in no particular order.
- [ ] This meets the criteria because the <br /> is present and sort() lists in descending order
- [x] This does not meet all the criteria because the sort() function sorts an indexed array in ascending order. Thus this code will display "2 4 6 11 22" shown vertically, but the numbers are spaced.
- [ ] does not meet all the criteria because the echo simply result in showing the array numbers in the order shown within the $numbers array, which is ascending

#### Q86. Which is not true of the `toString()` in PHP?

- [ ] It saves a lot of work of using setters methods to access the values of objects.
- [ ] It saves a lot of work of using getters methods to access the values of objects.
- [x] It allows you to call an object and see its components as a string.
- [ ] It is automatically called when you use echo or print.

#### Q87. What is a generator and how is it used in PHP?

- [ ] A generator is a function that produces a series of random values for unit testing code.
- [ ] A generator is a simple iterator capable of producing a series of results. It has the same syntax as a function, except it uses "next" instead of "return".
- [x] A generator is a simple iterator capable of producing a series of results. It has the same syntax as a function, except it uses "yield" instead of "return".
- [ ] A generator is a function capable of producing a series of results. At the end of the series, it automatically starts from the first one again.

#### Q88. What is the best description of what this script is/does?

```php
if( isset($user_info['url']) ) {
  $_SESSION["loggedIn"] = true;
  $_SESSION["username"] = $myusername;
  header('Location: ' . $user_info['url']); //Redirects to the supplied url from the DB
} else {
  header("Location: error.htm");
}
```

- [ ] It directs all users to the same page when they log in.
- [x] It is a login script for a user portal on a website.
- [ ] It keeps the user logged in across different browsers.
- [ ] It sends the user to an error page if they enter the wrong URL

#### Q89. What is the output of this code?

`echo 5 % 0.75;`

- [ ] 0
- [ ] 0.6666666666667
- [ ] 1
- [x] fatal error (division by zero)

#### Q90. Can you extend a final defined class?

- [x] No, because a final class or method declaration prevents child class or method overriding.
- [ ] Specialized versions of built-in classes can be extended by calling the parent's constructor.
- [ ] Yes, if a final class is defined as private in parent class.
- [ ] Yes, a final defined class can be used to declare constants.

#### Q91. How can you test if a checkbox is set?

- [x] Use `!empty($_GET['test'])`
- [x] Use `isset($_GET['test'])`
- [ ] Use `$_GET['test'] == ''`
- [ ] all other answers

`Actually both are correct, option 3 is actually testing if a checkbox is not set`

#### Q92. A form to subscrive to a newsletter is submitted using the POST method. The form has only one field: an input text field named "email". How would you check if the field is empty and, if it is, print "The email cannot be empty"?

- [x] &shy;

```php
if(empty($_POST['email'])) {
    echo "The email cannot be empty";
}
```

- [ ] &shy;

```php
if(empty($_GET['email'])) {
    echo "The email cannot be empty";
}
```

- [ ] &shy;

```php
if(empty($_POST('email'))) {
    echo "The email cannot be empty";
}
```

- [ ] &shy;

```php
if(isset($email)) {
    echo "The email cannot be empty";
}
```

#### Q93. What is the PHP fatal error type?

- [ ] This type of error causes a termination of the script execution when it occurs.
- [ ] This type of error's causes are not detected by compiler and causes incorrect results.
- [ ] This type of error causes erroneous results or may cause termination of program.
- [x] This type of error causes termination after showing the list of errors and the line number where the errors have occured.

1. [reference1](https://www.geeksforgeeks.org/php-types-of-errors/#:~:text=an%20error%20message.-,Fatal%20Error,-%3A%20It%20is)
2. [reference2](https://www.c-sharpcorner.com/UploadFile/051e29/types-of-error-in-php/#:~:text=2.-,Fatal%20Errors,-Fatal%20errors%20are)

#### Q94. Which script properly validates the IP address given?

- [ ] &shy;

```php
$valid = ip2long($ip) !== false;
```

- [x] &shy;

```php
$ip_address = "164.12.2540.1";
if(filter_var($ip_address, FILTER_VALIDATE_IP)){
  echo "$ip_address is a valid IP address";
} else {
  echo "$ip_address is not a valid IP address";
}
```

- [ ] &shy;

```php
$ip_address = "164.12.2540.1";
if(validate_ip($ip_address)){
  echo "$ip_address is a valid IP address";
} else {
  echo "$ip_address is not a valid IP address";
}
```

- [ ] &shy;

```php
$ip_address = "164.12.2540.1"
echo is_valid($ip_address, VALIDATE_IP);
```

#### Q95. What is the output of this code?

```php
    $i = 0;
    while($i < 6) {
    if($i++ == 3) break;
    }
    echo "loop stopped at $i by break statement";
```

- [ ] loop stopped at 3 by break statement
- [x] loop stopped at 4 by break statement
- [ ] loop stopped at 6 by break statement
- [ ] loop stopped at 2 by break statement

#### Q96. After creating your objects, you can call member functions related to that object, such as setting the names and prices for three "Pet" objects. What is the likely output of this code snippet?

```php
    $dof->setTitle("Spot");
    $cat->setTitle("Mimi");
    $horse-?setTitle("Trigger");
    $dog->setPrice(10);
    $cat->setPrice(15);
    $horse->setPrice(7);
    print_r($cat);
```

- [ ] Pet Object ( [title]=> Spot[price]=>10)
- [x] Pet Object ( [title]=> Mimi [price]=>15 )
- [ ] Pet Object ( [title]=> Mimi[price]=>10 )
- [ ] Pet Object ( [title]=> Trigger [price]=> 7)

#### Q97. Given the associative array below, wich PHP code determines wich element(s) of the array is/are apple?

```php
$array = array(
'fruit1' => 'apple',
'fruit2' => 'orange',
'fruit3' => 'grape',
'fruit4' => 'apple',
'fruit5' => 'apple');
```

- [x] &shy;

```php
while ($fruit_name = current($array)) {
    if ($fruit_name == 'apple') {
        echo key($array).'<br />';
    }
    next($array);
}
```

- [ ] &shy;

```php
while ($fruit_name = current($array)) {
    if ($fruitname == 'apple') {
        echo key($array).'<br />';
    }
    next($array);
}
```

- [ ] &shy;

```php
while ($fruit_name = current($array)) {
    if ($fruit_name == 'apple')
        echo key($array).'<br />';
    }
    next($array);
}
```

- [ ] &shy;

```php
while ($fruit_name = current($array)) {
    if ($fruit_name == 'apple') {
        echo key($array).'<br />';
    }
```

#### Q98. What does this code return?

#### Q98. What does this code print?

```php
class Smurf {

  public $name = "Papa Smurf";

  public function __construct($name) {
    $this->name = $name;
  }

  public function set_name($name) {
    $name = $name;
  }
}

$smurf = new Smurf("Smurfette");
$smurf->set_name("Handy Smurf");
echo $smurf->name;
```

- [ ] nothing
- [ ] Handy Smurf
- [x] Smurfette
- [ ] Papa Smurf

#### Q99. You have an online form with a file input field called "image" for uploading files. Assuming the path to the upload directory is $path, which code should you use to make sure the file is uploaded from your form to the correct location?

- [x] &shy;

```php
if ($_FILES['image']['error'] === 0) {
      move_uploaded_file($_FILES)['image']['temp_name'],
          $path . $_FILES['image']['name']);
 )
```

- [ ] &shy;

```php
if ($_FILES['image']['error'] === false) {
      move_uploaded_file($_FILES)['image']['temp_name'],
          $path . $_FILES['image']['name']);
 )
```

- [ ] &shy;

```php
if ($_FILES['image']['error'] == 0) {
      copy($_FILES)['image']['temp_name'],
          $path . $_FILES['image']['name']);
 )
```

- [ ] &shy;

```php
if ($_FILES['image']['error'] == false) {
      upload_file($_FILES)['image']['temp_name'],
          $path . $_FILES['image']['name']);
 )
```

#### Q100. Which super global variable holds information about headers, paths, and script locations?

- [ ] `$_GET`
- [ ] `$GLOBALS`
- [ ] `$_SESSION`
- [x] `$_SERVER`

#### Q101. Using a for loop, how would you write PHP code to count backward from 10 to 1, in that order?

- [ ] &shy;

```php
<?
for ($i=1; $i <= 10; $i++) {
    echo $i;
}
?>
```

- [ ] &shy;

```php
<?
$i = 10;
while($i>=0) {
    echo $i;
    $i--;
}
?>
```

- [ ] &shy;

```php
<?
    for($i = 10; $i > 0; $i++) {
        print "$i <br />\n";
    } // end for loop '''
?>
```

- [x] &shy;

```php
<?
    for($i = 10; $i > 0; $i--) {
        print "$i <br />\n";
    } // end for loop
?>
```

#### Q102. What is the output of this code?

```php
function knights(){
return "a shrubbery";
}

if (knights())
printf "you are just and fair";
else
printf "NI!";
```

- [ ] NI!
- [ ] a syntax error
- [ ] a shrubbery
- [x] you are just and fair

#### Q103. Which script defines the United States of America as a constant and prints this code?

**Our country is United States of America**
**Our country has a total of 50 states**

- [ ] &shy;

```php
define('country',"United States of America");
define('states',50);
echo "Our country is "country"<br>";
echo "Our country has a total of ".states." states";
```

- [x] &shy;

```php
define('country',"United States of America");
define('states',50);
echo "Our country is ".country."<br>";
echo "Our country has a total of ".states." states";
```

- [ ] &shy;

```php
define(country,"United States of America");
define('states',50);
echo "Our country is ".country."<br>";
echo "Our country has a total of ".states." states";
```

- [ ] &shy;

```php
define('country',"United States of America");
define('states','fifty');
$K = 'strval'; echo "Our {$K(Country)} has {$K(FIFTY)} states.";
```

#### Q104. What does this code output?

```php
try{
echo "bodacious";
throw new Exception();
} catch (Exception $e) {
echo "egregious";
} finally {
echo "excellent";
}
```

- [ ] bodacious
      excellent
- [ ] egregious
      excellent
- [x] bodacious
      egregious
      excellent
- [ ] bodacious
      egregious

#### Q105. Passing by reference is a way to pass a variable to a function and modify it inside the function, and have that modification stick when the variable is used outside the function. Which code correctly uses passing by reference to modify the variable for use outside the function?

- [ ] 1 function append($initial){ return $newString = $initial . ' belong to us'; }
      2 $initialString = 'All your base are’;
      3 $initialString = append($initialString);
      4 echo $initialString;

- [ ] 1 function append(&$initial){ return $newString = $initial . ' belong to us'; }
      2 $initialString = 'All your base are’;
      3 append($initialString);
      4 echo $initialString;

- [ ] 1 function append(&$initial){ return $newString = $initial . ' belong to us'; }
      2 $initialString = 'All your base are’;
      3 $initialString = append($initialString);
      4 echo $initialString;

- [x] 1 function append(&$initial){ $initial = $initial . ' belong to us'; }
      2 $initialString = 'All your base are’;
      3 append($initialString);
      4 echo $initialString;

#### Q106. What is the output of this script?

```php
$believable = 'false';
$myth = 'The moon is made of green cheese';
$calc = 10**3+1;
if ($believable) {
    echo $myth;
}
else {
    echo $calc;
}
```

- [ ] 10000
- [ ] 31
- [ ] 1001
- [x] The moon is made of green cheese

Explanation : 'false' evaluates to true since it is a string so the if condition is met.

#### Q107. What PHP control structure is used inside of a loop to skip the rest of the current loop's code and go back to the start of the loop for the next iteration?

- [ ] return

- [ ] else

- [ ] break

- [x] continue

### Q108. What is the output of this code?

```php
$x = "5";
$y = &$x;
$y = "2$y";
echo $x;
```

- [ ] 5
- [ ] 2
- [x] 25
- [ ] An error occurs

### Q109. Which function is used to check if a file exists in PHP?

- [ ] file_exists()
- [ ] is_file()
- [ ] file_check()
- [x] Both file_exists() and is_file()

### Q110. What does the following code output?

```php
$array = array(1, 2, 3, 4, 5);
echo array_sum($array) / count($array);
```

- [ ] 15
- [x] 3
- [ ] 5
- [ ] An error occurs

### Q111. Which of the following is NOT a valid way to start a PHP session?

- [ ] session_start();
- [ ] $\_SESSION = array();
- [x] session_begin();
- [ ] ini_set('session.auto_start', 1);

### Q112. What is the purpose of the 'finally' block in a try-catch-finally structure?

- [ ] To handle exceptions that weren't caught in the catch block
- [ ] To define custom exceptions
- [x] To execute code regardless of whether an exception was thrown or caught
- [ ] To end the try-catch block

### Q113. Which function would you use to remove HTML tags from a string?

- [ ] html_clean()
- [x] strip_tags()
- [ ] remove_html()
- [ ] sanitize_string()

### Q114. What is the output of this code?

```php
$str = "Hello";
$str[0] = "J";
echo $str;
```

- [ ] Hello
- [x] Jello
- [ ] An error occurs
- [ ] H

### Q115. Which of the following is NOT a magic method in PHP?

- [ ] \_\_construct()
- [ ] \_\_destruct()
- [ ] \_\_toString()
- [x] \_\_change()

### Q116. What does the 'yield' keyword do in PHP?

- [ ] It's used to define abstract methods
- [ ] It's used to pause the execution of a function
- [x] It's used to define generator functions
- [ ] It's used to force garbage collection

### Q117. Which function would you use to get the ASCII value of a character?

- [ ] ascii()
- [ ] char_to_ascii()
- [x] ord()
- [ ] ascii_val()

### Q118. What is the output of this code?

```php
$a = array(1, 2, 3);
$b = array("one", "two", "three");
$c = array_combine($a, $b);
print_r($c);
```

- [ ] Array ( [0] => 1 [1] => 2 [2] => 3 )
- [ ] Array ( [0] => one [1] => two [2] => three )
- [x] Array ( [1] => one [2] => two [3] => three )
- [ ] An error occurs

### Q119. Which of the following is NOT a valid PHP comparison operator?

- [ ] ===
- [ ] !==
- [ ] <>
- [x] =>

### Q120. What does the 'static' keyword do when used inside a function?

- [ ] It makes the function available globally
- [x] It preserves the value of the variable between function calls
- [ ] It prevents the function from being called more than once
- [ ] It makes the function run faster

### Q121. Which function would you use to get the current timestamp in PHP?

- [ ] now()
- [ ] current_time()
- [x] time()
- [ ] timestamp()

### Q122. What is the output of this code?

```php
$str = "abcdef";
echo substr($str, -2, 1);
```

- [ ] f
- [x] e
- [ ] ef
- [ ] de

### Q123. Which of the following is NOT a valid way to comment in PHP?

- [ ] // Single line comment
- [ ] /_ Multi-line comment _/
- [ ] # Shell-style comment
- [x] ' Single quote comment

### Q124. What does the 'instanceof' operator do in PHP?

- [ ] It checks if a variable is an instance of a class
- [ ] It creates a new instance of a class
- [ ] It checks if a class exists
- [x] It checks if an object is an instance of a class or interface

### Q125. Which function would you use to check if a variable is an array?

- [ ] is_array()
- [ ] array_check()
- [ ] typeof()
- [x] is_array()

### Q126. What is the output of this code?

```php
$x = 5;
$y = 10;
function myTest() {
    global $x, $y;
    $y = $x + $y;
}
myTest();
echo $y;
```

- [ ] 10
- [ ] 5
- [x] 15
- [ ] An error occurs

### Q127. Which of the following is NOT a valid PHP array function?

- [ ] array_push()
- [ ] array_pop()
- [ ] array_shift()
- [x] array_delete()

### Q128. What does the 'final' keyword do when used before a class declaration?

- [ ] It makes the class abstract
- [x] It prevents the class from being inherited
- [ ] It makes the class static
- [ ] It makes all methods in the class private

### Q129. Which function would you use to get the length of a string in PHP?

- [ ] count()
- [ ] length()
- [x] strlen()
- [ ] size()

### Q130. What is the output of this code?

```php
$a = "Hello";
$b = &$a;
$b = "World";
echo $a;
```

- [ ] Hello
- [x] World
- [ ] HelloWorld
- [ ] An error occurs
