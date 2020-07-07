PHP Assessment
-----------------

#### Q1. What does this code output?
`echo 76 &lt;=&gt; '76 trombones';`
- 1
- -1
- a parser error //Correct
- 0

#### Q2. Which is the most secure way to avoid storing a password in clear text in database?
```markdown
- $encrypted = shal($password)
- $encrypted = crypt($password, $salt);
- $encrypted = md5($password);
- $encrypted = password_hash($password, PASSWORD_DEFAULT); //Correct
```

#### Q3. What does this script do?
```
1 $mail = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);
2 if ($email === false) {
3  $emailErr = "Please re-enter valid email";
4 }
```
- It makes sure the email address is a good and functioning address
- It makes an email safe to input into a database
- It assigns an email to a variable and then removes all illegal characters from the $email variable
- It verifies that an email address is well formed. //Correct

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
- Line 6 will cause an error because you can't reassign a new value to a variable that has already been set.
- Line 7 and 8 will cause an error. Line 7 has whitespace in $will i work and should be $will_i_work. Line 8 cannot start with a number befcause it is a variable. // Correct  
- Line 5 will cause an error because some_string should be someString.
- Line 3 and 4 will cause an error because a variable cannot start with an underscore(_).

#### Q5. In a conditional statement, you want to execute the code only if both value are true. Which comparison operator should you use?
- ||
- &
- <=>
- && //Correct

#### Q6. All variables in PHP start with which symbol?
- &
- %
- _
- $ //Correct

#### Q7. What is a key difference between GET and POST?
- GET is used with the HTTP protocol. POST is used with HTTPS.
- GET displays the submitted data as part of the URL. During POST, this information is not shown, as it's encoded in the request body. //Correct
- GET is intended for changing the server state and it carries more data than POST.
- GET is more secure than POST and should be used for sensitive information.

#### Q8. The ___ operator is useful for sorting operations. It compares two values and returns an integer less than, equal to, or greater than 0 depending on whether on whether the value on the ___is less than, equal to, or greater than the other.
- greater-than; right
- spaceship; left //Correct
- equality; right
- comparison; left

#### Q9. Which are valid PHP error handling keywords?
- try, throw, catch, callable
- try, yield, catch, finally
- yield, throw, catch, finally
- try, throw, catch, finally //Correct

#### Q10. Which value equates to true?
- 0
- NULL
- ''
- -1 //Correct

#### Q11. What is missing from this code, which is supposed to reate a test cookies?
```
1 $string_name = " testcookie";
2 $string_value = "This is a test cookie";
3 $expiry_info = info()+259200;
4 $string_domain = "localhost.localdomain";
```
- The $_REQUEST is missing.
- The $_COOKIES array is missing.
- The cookie session is missing.
- The call to setcookie() is missing. //Correct

#### Q12. What is the value of $total in this calculation?
`$total = 2 + 5 * 20 - 6 / 3`
- 44
- 138
- 126
- 100 //Correct

#### Q13. What is the purpose of adding a lowercase "u" as a modifier after the final delimiter in a Perl-compatible regular expression?
- It makes the dot metacharacter match anything, including newline characters.
- It makes the pattern match uppercase letters.
- Both the pattern and subject string are treated as UTF-8. //Correct
- It inverts the greediness of the quantifiers in the pattern so they are not greedy by default.

#### Q14. Which code snippet uses the correct syntax for creating an instance of the Pet class?
```markdown
- $dog = new Pet;
- all of these answers //Correct
- $horse = (new Pet);
- $cat = new Pet();
```

#### Q15. What is the best way to explain what this script does?
```markdown
1 if (!$_SESSION['myusername'])
2 {
3    header('locaton: /login.php');
4    exit;
5 }
```
- This script times out the session for myusername.
- Cookies are starting to be stored as a result of this script.
- This script validates the username and password.
- This script is on a page that requires the user to be logged in. It checks to see if the user has a valid session. //Correct

