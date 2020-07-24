## Bash Assessment

#### Q1. Which of the three methods will copy the directory named "photo dir" recursively from the user's home directory to /backups?

```bash
cp -R "~/photo dir" /backups #method1
cp -R ~"/photo dir" /backups #method2
cp -R ~/"photo dir" /backups #method3
```

- [ ] None of the three methods will expand to the user's home directory. Only using `"$HOME/photo dir"`will be successful.
- [ ] Only method 1 will expand `"~/"` to the user's home directory and then append the quoted directory name that includes a space.
- [ ] Only method 2 will expand `"~/"` to the user's home directory and then append the quoted directory name that includes a space.
- [x] Only method 3 will expand `"~/"` to the user's home directory and then append the quoted directory name that includes a space.

#### Q2. If script.sh is run in the current directory, it will fail. Why?

```bash
$ ls -1
Beach photo1.jpg
Photo1.jpg
Photo2.jpg
Script.sh

$ cat script.sh
for i in $(ls *.jpg); do
	mv $i ${i}.bak
done  
```

- [ ] ls: cannot access nonexistentfile: No such file or directory
- [x] The for loop will split on word boundaries and Beach photo1.jpg has a space in it.
- [ ] The mv command will fail because the curly bracket is a special character in Bash and cannot be used in the names of files.
- [ ] Running script.sh will be successful as the ls command builds a list of files in the current directory and for loops through that list renaming files with a .bak extension.

#### Q3. To run a copy command in a subshell, which syntax would you use?

- [x] ( command )
- [ ] sh command
- [ ] { command }
- [ ] (( command ))

#### Q4. Using "awk", what would the output of this command string be?

```bash
echo "1 2 3" | awk '{for (i=1; i<=NF; i++) s=s+$i};END {print s}'
```

- [x] 6
- [ ] 123
- [ ] 3
- [ ] 600

#### Q5. The command below will search the root filesystem for files named "finance.db". In this context, what information is being sent to /dev/null?

```bash
find / -name "finance.db" 1>results.txt 2>/dev/null
```

- [ ] the names of files that do not match finance.db
- [x] information sent to the standard error-for example, errors that the find command displays as it runs
- [ ] the names of files that match finance.db
- [ ] information sent to the standard output-that is, the path to files the find command has located

#### Q6. To permanently remove empty lines from a file called textfile, which command could you use?

- [x] `sed -i '/^$/d' textfile`
- [ ] `sed '/^$/d' textfile`
- [ ] `cat textfile | sed '/^$/d`
- [ ] `sed -i 's/^$//' textfile`

#### Q7. Assuming that user1 existed, what would be the result of this command string?

```bash
awk -F: '/user1/{print $1 "-" $3 "-" $6}' /etc/passwd
```

- [ ] It would show the username, UID, and home directory of user1 separated by colons.
- [ ] It would print the UID, GID, and home directory of user1 separated by hyphens.
- [ ] It would print the UID, comment, and home directory of user1 separated by hyphens.
- [x] It would show the username, UID, and home directory of user1 separated by hyphens.

#### Q8. What happens if you use the `"set -e"` in a Bash script?

- [ ] It will cause Bash to exit if a function or subshell returns a nonzero status code.
- [ ] It will cause Bash to exit if a conditional returns a non-zero status code.
- [ ] It will cause Bash to exit if local, declare, or typeset assignments return a nonzero status code.
- [x] It will cause Bash to exit if a command, list of commands, compound command, or potentially a pipeline returns a nonzero status code.

#### Q9. The ______ keyword pauses the script to get input from standard input.

- [ ] get
- [ ] argument
- [x] read
- [ ] input

#### Q10. If file.sql holds SQL statements to be executed, what will be in file.txt?

##### I cannot reproduce this question, but at first sight I don't see correct answer, because no-one write to file.txt and content doesn't change 
##### I suppose the correct script is *mysql < file.sql > file.txt* then the correct answer is fourth option.

```bash
mysql < file.sql < file.txt
```

- [ ] a copy of the contents of file.sql
- [ ] an error indicating that this is invalid syntax
- [ ] the error output of the MySQL command
- [ ] the non-error output of the MySQL command

#### Q11. How does the SUID or setuid affect executable commands?

- [ ] When the command creates files, they will be owned by the group owner of the command.
- [ ] The SUID bit allows anyone to execute the command no matter what other permissions are set.
- [x] When the command is executed, its running privileges elevate to the user owner  of the command.
- [ ] When the command is executed, its running privileges elevate to the group owner of the command.

#### Q12. In order to extract text from the first column of file called textfile, which command would you use?

- [ ] `cat {$1,textfile}`
- [ ] `cat textfile | awk [print $1]`
- [x] `cat textfile | awk '{print $1}'`
- [ ] `awk textfile {print $1}`

#### Q13. What is the keyboard shortcut to call up the Bash history search as shown below?

```bash
(reverse-i-search)`':
```

- [ ] Esc + R
- [ ] Ctrl + H
- [x] Ctrl + R
- [ ] Alt + R

#### Q14. Which arithmetic expression will give the most precise answer?

- [ ] `var=$( expr 10 / 8 )`
- [ ] `(( var= 10 /8 ))`
- [ ] `var=$(( 10 / 8 ))`
- [x] `var=$(echo 'scale=2; 10 / 8' | bc)`

#### Q15. What is the result of this script? - TODO add script

- [ ] 0, representing 'true', because the variable "txt" contains eight letters
- [ ] 0, representing 'true', because everybody loves penguins!
- [ ] 1, representing 'false', because the variable "txt" is longer than eight characters
- [ ] 1, representing 'false', because the variable "txt" does not contain eight lowercase letters between a and z

#### Q16. How would you change your Bash shell prompt to the following?

```bash
HAL>
```

- [ ] `SHELL="HAL\>"`
- [ ] `SHELL="HAL>"`
- [x] `export PS1="HAL>"`
- [ ] `PS1="HAL\>"`

#### Q17. What is the output of this code?

```bash
VAR="/var/www/html/website.com/html/"
echo "${VAR#*/html}"
```

- [x] `/website.com/html/`
- [ ] `/html/website.com/html/`
- [ ] `/var/www/html/website.com/`
- [ ] Nothing will be echoed on the screen.

#### Q18. If prompted for text at the standard input, you can tell the command you're done entering text with what key combination?

- [ ] Ctrl + A (Windows) or Command + A (Mac)
- [ ] Ctrl + E (Windows) or Command + E (Mac)
- [x] Ctrl + D (Windows) or Command + D (Mac)
- [ ] Ctrl + Z (Windows) or Command + Z (Mac)

#### Q19. In order for a Bash script to be executed like an OS command, it should start with a shebang line. What does this look like?

- [x] `#!/usr/bin/env bash`
- [ ] `~/usr/bin/env bash`
- [ ] `'$!/usr/bin/env bash`
- [ ] `#/usr/bin/env bash`

#### Q20. What line of Bash script probably produced the output shown below?

```bash
The date is: Sun Mar 24 12:30:06 CST 2019!
```

- [ ] `echo "The date is: !"`
- [ ] `echo "The date is: date!"`
- [ ] `echo "The date is:  (date)!"`
- [x] `echo "The date is: $(date)!"`

#### Q21. Suppose your current working directory is your home directory. How could you run the script demo.sh that is located in your home directory? Find three correct answers.

```bash
A. /home/demo.sh
B. ./demo.sh
C. ~/demo.sh
D. bash /home/demo.sh
E. bash demo.sh
```

- [x] B, C, E
- [ ] A, B, C
- [ ] C, D, E
- [ ] B, D, E

#### Q22. How could you get a list of all .html files in your tree?

#### Idk both of them work
- [ ] `find . -type html`
- [x] `find . -name *.html`
- [ ] `find *.html`
- [x] `find . -name \*.html -print`

#### Q23. What would be in out.txt?

```bash
cat < in.txt > out.txt
```

- [ ] The output from the command line. By default STDIN comes from the keyboard.
- [ ] Nothing because you can't redirect from file (in.txt) to another file (out.txt). You can only redirect from a command to a file.
- [x] It would be the contents of in.txt.
- [ ] Nothing. The redirect will create a new empty file but there will not be any output from the cat command to redirect.

#### Q24. What does this bash statement do?

```bash
(( $a == $b ))
echo $?
```

- [ ] It loops between the values of `$a` and `$b`.
- [x] It tests whether the values of variables `$a` and `$b` are equal.
- [ ] It returns `$b` if it is larger than `$a`.
- [ ] It returns `$a` if it is larger than `$b`.

#### Q25. What do you use in a case statement to tell Bash that you're done with a specific test?

- [x] `; ;`
- [ ] `: :`
- [ ] `done`
- [ ] `$$`

#### Q26. What does the asterisk represent in this statement?

```bash
<em>#!/usr/bin/env bash</em>
case $num in
	1)
	echo "one"
	; ;
	2)
	echo "two"
	; ;
	*)
	echo "a mystery"
	; ;
esac	
```

- [x] a case that matches any value, providing a default option if nothing else catches that value
- [ ] a case only for what happens when the asterisk character is passed into the script
- [ ] the action of all of the other cases combined together
- [ ] an action that is taken for any input, even if it matches a specified condition

#### Q27. What Bash script will correctly create these files?

- [ ] `touch file{1+10}.txt`
- [ ] `touch file{1-10}.txt`
- [x] `touch file{1..10}.txt`
- [ ] `touch file(1..10).txt`

#### Q28. Which variable would you check to verify that the last command executed successfully?

- [ ] `$$`
- [x] `$?`
- [ ] `$!`
- [ ] `$@`

