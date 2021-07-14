## PHP

##### Q1. What does this code output?

`echo 76 <=> '76 trombones';`

- [ ] 1
- [ ] -1
- [ ] a parser error
- [x] 0

##### Q2. Which is the most secure way to avoid storing a password in clear text in database?

- [ ] `$encrypted = shal($password);`
- [ ] `$encrypted = crypt($password, \$salt);`
- [ ] `$encrypted = md5($password);`
- [x] `$encrypted = password_hash($password, PASSWORD_DEFAULT);`

##### Q3. What does this script do?

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

##### Q4. In the following script, which line(s) will cause an error(s)?

```
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

##### Q5. In a conditional statement, you want to execute the code only if both value are true. Which comparison operator should you use?

- [ ] ||
- [ ] &
- [ ] <=>
- [x] &&

##### Q6. All variables in PHP start with which symbol?

- [ ] &
- [ ] %
- [ ] _
- [x] $

##### Q7. What is a key difference between GET and POST?

- [ ] GET is used with the HTTP protocol. POST is used with HTTPS.
- [x] GET displays the submitted data as part of the URL. During POST, this information is not shown, as it's encoded in the request body.
- [ ] GET is intended for changing the server state and it carries more data than POST.
- [ ] GET is more secure than POST and should be used for sensitive information.

##### Q8. The __ operator is useful for sorting operations. It compares two values and returns an integer less than, equal to, or greater than 0 depending on whether on whether the value on the __ is less than, equal to, or greater than the other.

- [ ] greater-than; right
- [x] spaceship; left
- [ ] equality; right
- [ ] comparison; left

##### Q9. Which are valid PHP error handling keywords?

- [ ] try, throw, catch, callable
- [ ] try, yield, catch, finally
- [ ] yield, throw, catch, finally
- [x] try, throw, catch, finally

##### Q10. Which value equates to true?

- [ ] 0
- [ ] NULL
- [ ] ''
- [x] -1

##### Q11. What is missing from this code, which is supposed to create a test cookies?

```php
1 $string_name = "testcookie";
2 $string_value = "This is a test cookie";
3 $expiry_info = info()+259200;
4 $string_domain = "localhost.localdomain";
```

- [ ] The `$_REQUEST` is missing.
- [ ] The `$_COOKIES` array is missing.
- [ ] The cookie session is missing.
- [x] The call to `setcookie()` is missing.

##### Q12. What is the value of \$total in this calculation?

`$total = 2 + 5 * 20 - 6 / 3`

- [ ] 44
- [ ] 138
- [ ] 126
- [x] 100

##### Q13. What is the purpose of adding a lowercase "u" as a modifier after the final delimiter in a Perl-compatible regular expression?

- [ ] It makes the dot metacharacter match anything, including newline characters.
- [ ] It makes the pattern match uppercase letters.
- [x] Both the pattern and subject string are treated as UTF-8.
- [ ] It inverts the greediness of the quantifiers in the pattern so they are not greedy by default.

##### Q14. Which code snippet uses the correct syntax for creating an instance of the Pet class?

- [ ] `$dog = new Pet;`
- [x] all of these answers
- [ ] `$horse = (new Pet);`
- [ ] `$cat = new Pet();`

##### Q15. What is the best way to explain what this script does?

```php
1 if (!$_SESSION['myusername'])
2 {
3   header('locaton: /login.php');
4   exit;
5 }
```

- [ ] This script times out the session for myusername.
- [ ] Cookies are starting to be stored as a result of this script.
- [ ] This script validates the username and password.
- [x] This script is on a page that requires the user to be logged in. It checks to see if the user has a valid session.

##### Q16. Which is the correct format for adding a comment to a PHP script?

- [x] all of these answers
- [ ] #This is a comment
- [ ] /* This is a comment */
- [ ] // This is a comment

##### Q17. PHP supports multiple types of loops. If you wanted to loop through a block of code if and as long a specified condition is true, which type of loop would you use?

- [ ] for
- [ ] do-while
- [x] while
- [ ] foreach

##### Q18. The `ignore_user_abort( )` function sets whether a client disconnect should abort a script execution. In what scenario would you, as a web developer, use this function?

- [ ] You would use it to stop a user from clicking the back button if they decide not to view as a result of a click.
- [x] You would use this function if you have some important processing to do and you do not want to stop it, even if your users click Cancel.
- [ ] You would use this function if you wanted to abort the script for all logged-in users, not just the one who disconnected.
- [ ] You would use this function if you want a PHP script to run forever.

##### Q19. The PHP function array_reduce() takes a callback function that accepts a value carried over each iteration and the current item in the array, and reduces an array to a single value. Which code sample will sum and output the values in the provided array?

- [ ]
  ```php
  1 <?php
  2 echo array_reduce([1, 2, 5, 10, 11], function ($item, $carry) {
  3     $carry = $carry + $item;
  4 });
  5?>
  ```
- [ ]
  ```php
  1 <?php
  2 echo array_reduce([1, 2, 5, 10, 11], function ($carry, $item) {
  3     return $carry = $item + $item;
  4 });
  5?>
  ```
- [ ]
  ```php
  1 <?php
  2 array_reduce([11 2, 5, 10, 11], function ($item, $carry) {
  3     echo $carry + $item;
  4 });
  5?>
  ```
- [x]
  ```php
  1 <?php
  2 echo array_reduce([1, 2, 5, 10, 11], function ($carry, $item) {
  3     return $carry += $item;
  4 });
  5?>
  ```

##### Q20. Which PHP script uses a constructor to display the string "Winter is almost over!"?

- [x]
  ```php
  1 class MyClass {
  2 public function \_construct()
  3 {
  4 echo 'Winter is almost over!'."\n";
  5 }
  6 }
  7 \$userclass = new MyClass;
  ```
- [ ]
  ```php
  1 class MyClass {
  2 public function _construct()
  3 {
  4 echo 'Winter is almost over!.."\n";
  5 }
  6 }
  7 $userclass = new MyClass;
  ```
- [ ]
  ```php
  1 class MyClass {
  2 public function \_construct()
  3 {
  4 echo 'Winter is almost over!.."\n";
  5 }
  6 }
  7 \$userclass = new MyClass;
  ```
- [ ]
  ```php
  1 class MyClass {
  2 public function _construct()
  3 {
  4 echo 'Winter is almost over!'."n";
  5 }
  6 }
  7 $userclass = MyClass;
  ```

##### Q21. How might you troubleshoot a "call to undefined function" error?

- [ ] Make sure you have imported the file containing the function.
- [ ] Make sure you have spelled the function name correctly.
- [x] all of these answers
- [ ] Make sure the function declaration is at an earlier point in the code than the function call.

##### Q22. Which line could you NOT use to comment out "Space: the final frontier"?

- [ ] `/* Space: the final frontier */`
- [x] `*/ Space: the final frontier /*`
- [ ] `#Space: the final frontier`
- [ ] `// Space: the final frontier`

##### Q23. What displays in a browser when the following code is written? `<?php echo "How much are the bananas?"?>`

- [ ] The browser would display nothing due to a syntax error.
- [ ] The browser would display an error, since there are no parentheses around the string.
- [x] The browser would display `How much are the bananas?`
- [ ] The browser would display an error, since there is no semicolon at the end of the echo command.

##### Q24. Which operator would you use to find the remainder after division?

- [ ] /
- [x] %
- [ ] //
- [ ] DIV

##### Q25. What is the significance of the three dots in this function signature?

```php
function process(...$vals) {
        // do some processing
 }
```

- [ ] It makes the function variadic, allowing it to accept as an argument an array containing an arbitrary number of values.
- [x] It makes the function variadic, allowing it to accept an arbitrary number of arguments that are converted into an array inside the function.
- [ ] It temporarily disables the function while debugging other parts of the script.
- [ ] It's a placeholder like a TO DO reminder that automatically triggers a notice when you run a script before completing the function definition.

##### Q26. Assuming the `Horse` class exists, which is a valid example of inheritance in PHP?

- [x] `class Pegasus extends Horse {}`
- [ ] `class Alicorn imports Pegasus, Unicorn {}`
- [ ] `class Unicorn implements Horse {}`
- [ ] `class Horse inherits Unicorn {}`

##### Q27. Both triple === and double == can be used to __ variables in php. If you want to hear that string "33" and the number 33 are equal, you would use __ . If you want to check if an array contains a particular string value at a particular index, you would use __

- [x] compare; doubles; triples
- [ ] compare; triples; doubles
- [ ] assign; triples; doubles
- [ ] assign; doubles; triples

##### Q28. Your php page is unexpectedly rendering as totally blank. Which step will shed light on the problem?

- [ ] Add this code to the top of your script: `ini_set('display_errors',1);`
- [ ] check the server error logged
- [x] all of these answers
- [ ] make sure you are not missing any semicolons

##### Q29. Which is the way to create an array of "seasons"?

- [ ] 
  ```
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

##### Q30. Both `self` and `this` are keywords that can be used to refer to member variables of an enclosing class. The difference is that `$this->member` should be used for __ members and `self::$member` should be used for __ members.

- [ ] private, public
- [ ] object,primitive
- [x] non-static,static
- [ ] concrete,abstract

##### Q31. What will this code print?

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

##### Q32. You are using the following code to find a users band, but it is returning false. Which step(s) would solve the problem?

`isset ($_GET['fav_band'])`

- [ ] check if `fav_band` is included in the query string at the top of your browser
- [x] all of the answers
- [ ] view the source of form and make sure there is an input field with the name 'fav_band'
- [ ] print everything that has been transmitted in the request: `print_r($_REQUEST);`

##### Q33. Which code would you use to print all the elements in an array called `$cupcakes`?

- [x] all of the answers
- [ ] `print_r($cupcakes);`
- [ ] `var_dump($cupcakes);`
- [ ] `foreach($cupcakes as &$cupcake) echo $cupcake;`

##### Q34. What is the cause of 'Cannot modify header information - headers already sent'?

- [ ] You are trying to modify a private value
- [ ] Semicolon missing
- [ ] Using a key on an array that does not exists
- [x] Some html is being sent before a `header()` command that you are using for a redirect

##### Q35. Which php control structure is used inside a loop to skip the rest of the current loops code and go back to the start of the loop for the next iteration

- [ ] `else`
- [ ] `break`
- [ ] `return`
- [x] `continue`

##### Q36. The php not operator is !. Given the snippet, is there an out put and what is it?

- [ ] there is an output '2 is an even number
- [x] output '21 is an odd number'
- [ ] no output. Syntax error do to missing semicolon at the end
- [ ] no output due to % in \$num%2!=0

##### Q37. You want to list the modules available in your PHP installation. What command should you run?

- [ ] `php -h`
- [ ] `php info`
- [ ] `php -v`
- [x] `php -m`

##### Q38. For the HTML form below, what is the correct functioning script that checks the input "mail" to be sure it is filled before proceeding?

```php
if (!empty($_POST["mail"])) {
echo "Yes, mail is set";
} else {
echo "No, mail is not set";
} (correct)
```

##### Q39. What is the value of `$result` in this calculation?

`$result = 25 % 6;`

- [ ] 4.167
- [ ] 1.5
- [ ] 4
- [x] 1

##### Q40. What is the job of the controller as a component in MVC?

- [x] The controller handles data passed to it by the view, and also passes data to the view. It interprets data sent by the view and disperses that data to the approrpiate models awaiting results to pass back to the view.
- [ ] The controller is a mechanism that allows you to create reusable code in languages such as PHP, where multiple inheritance is not supported.
- [ ] The controller presents content through the user interface, after communicating directly with the database.
- [ ] The controller handles specific tasks related to a specific area of functionality, handles business logic related to the results, and communicates directly with the database.

##### Q41. Why does this code trigger an error?

`$string = 'Shylock in a Shakespeare's "Merchant of Venice" demands his pound of flesh.';`

- [ ] Strings should always be wrapped in double quotes; and double quotes inside a string should be escaped by backslashes.
- [ ] All single and double quotes inside a string need to be escaped by backslashes to prevent a parse error.
- [ ] The opening and closing single quotes should be replaced by double quotes; and the apostrophe should be escaped by a backslash.
- [x] The apostrophe needs to be escaped by a backslash to prevent it from being treated as the closing quote.

##### Q42. A PDO object called `$db` has been set up to use for database operations, including user authentication. All user-related properties are set. The script line `public function __construct(&$db)` shows a constructor that initializes all user-related properties to __ if no user has logged in. These parameters will be properly set by the login functions when a user logs in.

- [x] NULL
- [ ] TRUE
- [ ] FALSE
- [ ] 0

##### Q43. Assuming that `$first_name` and `$family_name` are valid strings, which statement is invalid?

- [ ] `echo $first_name. ' '. $familiy_name;`
- [x] `print $first_name, ' ', $familiy_name;`
- [ ] `print $first_name. ' '. $familiy_name;`
- [ ] `echo $first_name, ' ', $familiy_name;`

##### Q44. Which code snippet demonstrates encapsulation?

- [ ]
  ```php
  class Cow extends Animal {
      private $milk;
  }
  ```
- [ ]
  ```php
  class Cow {
      public $milk;
  }
  $daisy = new Cow();
  $daisy->milk = "creamy";
  ```
- [ ]
  ```php
  class Cow {
      public $milk;
      function getMilk() {`
          return $this->milk;
      }
  }
  ```
- [x]
  ```php
  class Cow {
      private $milk;
      public function getMilk() {
          return $this->milk;
      }
  }
  ```

##### Q45. The following XML document is in books.xml. Which code will output "Historical"?

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

- [ ] 
  ```php
  $books = simplexml_load_string('books.xml');
  echo $books->book[0]->categories->category[1];
  ```
- [x] 
  ```php
  $books = simplexml_load_file('books.xml');
  echo $books->book[0]->categories->category[1];
  ```
- [ ] 
  ```php
  $books = SimpleXMLElement('books.xml');
  echo $books->book[0]->categories->category[1];
  ```
- [ ] 
  ```php
  $books = SimpleXML('books.xml');
  echo $books->book[0]->categories->category[1];
  ```

##### Q46. When it comes to the value of a variable, what is the difference between NULL and empty?

- [ ] NULL is a blank value; empty is the lack of a value.
- [ ] A NULL value has an allocated address in memory; empty does not.
- [ ] NULL referes to the lack of a value for an integer; empty refers to the lack of a value for a string.
- [x] NULL is the lack of a value; empty is a blank value.

##### Q47. What would be a good name for this function?

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

##### Q48. If you want to pass a formfield to another page when a button is clicked, you should use the __ . If you want to store information across multiple pages, you should use the __ ?

- [ ] request; response
- [ ] response; request
- [ ] session; request
- [x] request; session

##### Q49. You are using the following code to decide if a button is clicked, but it is never returning true. Which step is most likely to shed light on the problem?

```php
isset($_POST['submit'])
```

- [x] Make sure the input field displaying the button is named 'submit'
- [ ] Make sure you are not missing any semicolons
- [ ] Print everything in the session `print_r($_SESSION);`
- [ ] Look in the query string at the top of your browser to see if submit is assigned a value

##### Q50. Why should you follow a PSR standard?

- [x] because coding standards often vary between developers and companies
- [ ] because coding standards are monitored for compliance across developers and companies
- [ ] because there are mandatory coding standards among developers and companies
- [ ] if using certain platforms, because the PSR's apply to those platforms only

##### Q51. What are getters and setters?

- [ ] Getters and setters ensure that if a data member is declared private, then it can be accessed only within the same function, not by an outside class
- [ ] Getters and setters are utility functions within PHP that allow loading from, and saving to, a database
- [ ] Getters and setters encapsulate the fields of a class by making them acccessible only through its private methods, and keep the values themselves public
- [x] Getters and setters are methods used to declare or obtain the values of variables, usually private ones

#### Q52. What are the recommended settings in the PHP configuration file, php.ini, for a testing environment?

- [ ]
  ```php
  report_errors = E_ALL
  display_errors = On
  ```
- [x]
  ```php
  error_reporting = E_ALL
  display_errors = On
  ```
- [ ]
  ```php
  error_reporting = E_ALL & ~E_NOTICE
  display_errors = Off
  ```
- [ ]
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
