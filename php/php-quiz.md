## PHP Assessment

#### Q1. What does this code output?

`echo 76 &lt;=&gt; '76 trombones';`

- [ ] 1
- [ ] -1
- [x] a parser error
- [ ] 0

#### Q2. Which is the most secure way to avoid storing a password in clear text in database?

- [ ] `$encrypted = shal($password);`
- [ ] `$encrypted = crypt($password, \$salt);`
- [ ] `$encrypted = md5($password);`
- [x] `$encrypted = password_hash($password, PASSWORD_DEFAULT);`

#### Q3. What does this script do?

```
1 $email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);
2 if ($email === false) {
3  $emailErr = "Please re-enter valid email";
4 }
```

- [ ] It makes sure the email address is a good and functioning address
- [ ] It makes an email safe to input into a database
- [ ] It assigns an email to a variable and then removes all illegal characters from the \$email variable
- [x] It verifies that an email address is well formed.

#### Q4. In the following script, which line(s) will cause an error(s)?

```
1 <?php
2       $count = 0
3       $_xval = 5
4       $_yval = 1.0
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
- [x] \$

#### Q7. What is a key difference between GET and POST?

- [ ] GET is used with the HTTP protocol. POST is used with HTTPS.
- [x] GET displays the submitted data as part of the URL. During POST, this information is not shown, as it's encoded in the request body.
- [ ] GET is intended for changing the server state and it carries more data than POST.
- [ ] GET is more secure than POST and should be used for sensitive information.

#### Q8. The **_ operator is useful for sorting operations. It compares two values and returns an integer less than, equal to, or greater than 0 depending on whether on whether the value on the _**is less than, equal to, or greater than the other.

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

```
1 $string_name = " testcookie";
2 $string_value = "This is a test cookie";
3 $expiry_info = info()+259200;
4 $string_domain = "localhost.localdomain";
```

- [ ] The \$\_REQUEST is missing.
- [ ] The \$\_COOKIES array is missing.
- [ ] The cookie session is missing.
- [x] The call to setcookie() is missing.

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

```markdown
- [ ] \$dog = new Pet;
- [x] all of these answers
- [ ] \$horse = (new Pet);
- [ ] \$cat = new Pet();
```

#### Q15. What is the best way to explain what this script does?

```markdown
1 if (!\$\_SESSION['myusername'])
2 {
3 header('locaton: /login.php');
4 exit;
5 }
```

- [ ] This script times out the session for myusername.
- [ ] Cookies are starting to be stored as a result of this script.
- [ ] This script validates the username and password.
- [x] This script is on a page that requires the user to be logged in. It checks to see if the user has a valid session.

#### Q16. Which is the correct format for adding a comment to a PHP script?

- [x] all of these answers
- [ ] #This is a comment
- [ ] /\* This is a comment /
- [ ] // This is a comment

#### Q17. PHP supports multiple types of loops. If you wanted to loop through a block of code if and as long a specified condition is true, which type of loop would you use?

- [ ] for
- [ ] do-while
- [x] while
- [ ] foreach

#### Q18. The ignore_user_abort( ) function sets whether a client disconnect should abort a script execution. In what scenario would you, as a web developer, use this function?

- [ ] You would use it to stop a user from clicking the back button if they decide not to view as a result of a click. //Maybe
- [ ] You would use this function if you have some important processing to do and you do not want to stop it, even if your users click Cancel.
- [ ] You would use this function if you wanted to abort the script for all logged-in users, not just the one who disconnected.
- [ ] You would use this function if you want a PHP script to run forever.

### Q19. The PHP function array_reduce() takes a callback function that accepts a value carried over each iteration and the current item in the array, and reduces an array to a single value. Which code sample will sum and output the values in the provided array?

[ ] ```
1 <?php
2 echo array_reduce([1, 2, 5, 10, 11], function ($item, $carry) {
3 $carry = $carry + \$item;
4 });
5?>
```

[ ] ```
1 <?php
2 echo array_reduce([1, 2, 5, 10, 11], function ($carry, $item) {
3 return $carry = $item + \$item;
4 });
5?>
```

[ ] ```
1 <?php
2 array_reduce([11 2, 5, 10, 11], function ($item, $carry) {
3 echo $carry + $item;
4 });
5?>
```

[ ] ```
1 <?php --CORRECT
2 echo array_reduce([1, 2, 5, 10, 11], function ($carry, $item) {
3 return $carry += $item;
4 });
5?>
```

#### Q20. Which PHP script uses a constructor to display the string "Winter is almost over!"?

[ ] ```
1 class MyClass { //Maybe
2 public function \_construct()
3 {  
4 echo 'Winter is almost over!'."\n";
5 }
6 }
7 \$userclass = new MyClass;
```

[ ] ```
1 class MyClass {
2 public function _construct()
3 {
4 echo 'Winter is almost over!.."\n";
5 }
6 }
7 $userclass = new MyClass;
```

[ ] ```
1 class MyClass {
2 public function \_construct()
3 { 
4 echo 'Winter is almost over!.."\n";
5 }
6 }
7 \$userclass = new MyClass;
```

[ ] ```
1 class MyClass {
2 public function _construct()
3 {
4 echo 'Winter is almost over!'."n";
5 }
6 }
7 $userclass = MyClass;
```

#### Q21. How might you troubleshoot a "call to undefined function" error?

- [ ] Make sure you have imported the file containing the function.
- [ ] Make sure you have spelled the function name correctly.
- [ ] all of these answers //Maybe
- [ ] Make sure the function declaration is at an earlier point in the code than the function call.

#### Q22. Which line could you NOT use to comment out "Space: the final frontier"?

- [ ] /_ Space: the final frontier _/ 
- [x] _/ Space: the final frontier /_
- [ ] #Space: the final frontier
- [ ] // Space: the final frontier

#### Q23. What displays in a browser when the following code is written? <?php echo "How much are the bananas?"?>

- [ ] The browser would display nothing due to a syntax error.
- [ ] The browser would display an error, since there are no parentheses around the string.
- [x] The browser would display How much are the bananas?
- [ ] The browser would display an error, since there is no semicolon at the end of the echo command.

#### Q24. Which operator would you use to find the remainder after division?

- [ ] /  
- [x] %
- [ ] //
- [ ] DIV

#### Q25. What is the significance of the three dots in this function signature?

```
function process(...$vals) {
        // do some processing
 }
```

- [ ] It makes the function variadic, allowing it to accept as an argument an array containing an arbitrary number of values.
- [x] It makes the function variadic, allowing it to accept an arbitrary number of arguments that are converted into an array inside the function.
- [ ] It temporarily disables the function while debugging other parts of the script.
- [ ] It's a placeholder like a TO DO reminder that automatically triggers a notice when you run a script before completing the function definition.

#### Q26. Assuming the Horse class exists, which is a valid example of inheritance in PHP?

- [x] class Pegasus extends Horse {}
- [ ] class Alicorn imports Pegasus, Unicorn {}
- [ ] class Unicorn implements Horse {}
- [ ] class Horse inherits Unicorn {}

#### Q27. Both triple === and double == can be used to **\_ variables in php. If you want to hear that string "33" and the number 33 are equal, you would use ** . If you want to check if an array contains a particular string value at a particular index, you would use \_\_\_

- [x] compare; doubles;triples
- [ ] compare; triples;doubles
- [ ] assign; triples;doubles
- [ ] assign;doubles;triples

#### Q28. Your php page is unexpectedly rendering as totally blank. Which step will shed light on the problem?

- [ ] Add this code to the top of your script:ini_set('display_errors',1);
- [ ] check the server error logged
- [x] all of these answers
- [ ] make sure you are not missing any semicolons

#### Q29. Which is the way to create an array of "seasons"?

- [ ] seasons=array(
  1=>'spring',
  2=>'summer',
  3=>'autumn',
  4=>'winter',
  ); 
- [ ] $seasons=array(spring,summer,autumn,winter);
- [ ] $seasons=('spring','summer','autumn','winter');
- [x] $seasons=['spring','summer','autumn','winter'];

#### Q30. Both self and this are keywords that can be used to refer to member variables of an enclosing class. The difference is that $this->member should be used for __ members and self::$member should be used for \_\_ members.

- [ ] private, public
- [ ] object,primitive
- [x] non-static,static
- [ ] concrete,abstract

#### Q31. What will this code print?

```
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

`isset (\$\_GET['fav_band'])`

- [ ] check if fav_band is included in the query string at the top of your browser
- [x] all of the answers
- [ ] view the source of form and make sure there is an input field with the name 'fav_band'
- [ ] print everything that has been transmitted in the request:print_r(\$\_REQUEST);

#### Q33. Which code would you use to print all the elements in an array called $cupcakes?

- [x] all of the answers
- [ ] print_r($cupcakes);
- [ ] var_dump($cupcakes);
- [ ] foreach($cupcakes as &$cupcake) echo $cupcake;

#### Q34. What is the cause of 'Cannot modify header information - headers already sent'?

- [ ] You are trying to modify a private value
- [ ] Semicolon missing
- [ ] Using a key on an array that does not exists
- [x] Some html is being sent before a header() command that you are using for a redirect

#### Q35. Which php control structure is used inside a loop to skip the rest of the current loops code and go back to the start of the loop for the next iteration

- [ ] else
- [ ] break
- [ ] return
- [x] continue

#### Q36. The php not operator is !. Given the snippet, is there an out put and what is it?

- [ ] there is an output '2 is an even number
- [x] output '21 is an odd number'
- [ ] no output. Syntax error do to missing semicolon at the end
- [ ] no output due to % in \$num%2!=0

### Q37. You want to list the modules available in your PHP installation. What command should you run?

- [ ] php -h
- [ ] php info
- [ ] php -v
- [x] php -m

### Q38. For the HTML form below, what is the correct functioning script that checks the input "mail" to be sure it is filled before proceeding?

```
if (!empty(\$\_POST["mail"])) {
echo "Yes, mail is set";
} else {
echo "No, mail is not set";
} (correct)
```

### Q29. What is the value of '$result' in this calculation?

`$result = 25 % 6;`

- [ ] 4.167
- [ ] 1.5
- [ ] 4
- [x] 1
