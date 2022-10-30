## Linux

#### Q1. To mount a drive by its ID, what command would you use first to retrieve it?

- [ ] df -h
- [ ] listid
- [ ] ls -l
- [x] blkid

#### Q2. Linux file access control lists (ACLs) are \_.

- [x] discretionary access control system permissions layered over standard Linux permissions
- [ ] mandatory access control system permissions layered over standard Linux permissions
- [ ] a type of firewall for Linux
- [ ] the same as standard Linux permissions

#### Q3. When using iproute2, how do you show routing information for an IPv6 network?

- [ ] route -ipv6
- [ ] route
- [x] ip -6 route show
- [ ] ip route show

#### Q4. What does this command string do?

```bash
find / -size +10M -exec ls -l {} ;
```

- [ ] It finds all files using ls -l and hands them off to the find command to display.
- [ ] It finds all files older than 10 minutes and long lists them using the ls command.
- [x] It finds all files larger than 10 MB and long lists them using the ls command.
- [ ] It uses the ls command to find all files in the filesystem matching the {} wildcard.

#### Q5. What would this locate command show?

```bash
locate --regexp '^/usr.*pixmaps.*jpg$'
```

- [ ] all files in a directory named pixmaps
- [ ] all files ending in ".jpg"
- [x] all file paths that start with "/usr", include the word "pixmaps", and end with ".jpg"
- [ ] all file paths that include "/usr/pixmaps" and end with ".jpg"

#### Q6. Which command allows you to do packet analysis from the command line?

- [ ] wireshark
- [ ] ethtool
- [ ] netstat
- [x] tcpdump

#### Q7. Which command will tell you how long a system has been running?

- [ ] log
- [x] uptime
- [ ] runtime
- [ ] access

#### Q8. How would you describe PCP (Performance Co-Pilot)?

- [ ] It is an application testing suite used to profile programming code.
- [ ] It is a local command used for monitoring local system resources in real time.
- [x] It is a set of tools, services, and libraries for gathering and analyzing performance measures.
- [ ] It is a tool designed to change system configuration for purposes of optimization.

#### Q9. You want to resolve a long list of DNS names using dig. What should you do?

- [x] Create a text file including all names and use the -f option of dig.
- [ ] Type in each query manually.
- [ ] Write a shell script to send multiple dig queries to the DNS server.
- [ ] Save the DNS names in an SQL database and process it with dig.

#### Q10. What would this command output?

```
ps -e --format uid,pid,ppid,%cpu,cmd
```

- [x] the user ID, process ID, parent process ID, CPU usage, and command name of a process
- [ ] the user ID, group ID, parent process ID, CPU usage, and command name of a process
- [ ] the UUID, process ID, parent process ID, CPU usage, and command name of a process
- [ ] all of these answers

#### Q11. Which command in Bash executes the last line in the shell history that starts with ls?

- [ ] !
- [ ] !!
- [ ] !\*
- [x] !ls

#### Q12. The ssh-copy-id command copies \_ to the remote host.

- [ ] both private and public keys
- [x] the ssh public key
- [ ] the ssh private key
- [ ] a fingerprint file

#### Q13. What command is used to determine the amount of disk usage for a directory?

- [ ] find
- [ ] fdisk
- [x] du
- [ ] df

#### Q14. A backup drive was created using dd to make a bit-for-bit copy. When the drive is inserted into an iSCSI target before it is booted up, the data appears to be missing. What happened?

- [ ] The backup drive is corrupted and needs to be re-created.
- [x] When the backup drive was duplicates, the label was as well. When booted, the system mounted the old duplicates drive by its identical label.
- [ ] There is a conflict between the physical location of the backup drive and the original drive.
- [ ] The backup process went wrong, and the old drive was duplicates over the original drive.

#### Q15. What is the key difference between a redirect (>) and piping to the tee command?

- [ ] The tee command sends output only to STDOUT and STDERR.
- [ ] A redirect sends output to STDOUT and a file, whereas a tee sends output only to STDOUT.
- [ ] Nothing, they are the same.
- [x] The tee command sends output to STDOUT and a file, whereas a redirect sends output only to a file.

#### Q16. What does the /etc/nsswitch.conf file manage?

- [ ] priority of one DNS server over another
- [ ] per network interface DNS server configuration
- [ ] alternative DNS services
- [x] sources for name service information

#### Q17. Assume the variable myNumber holds a string consisting of 10 digits. What will this command output?

```bash
echo \$myNumber | sed -e 's/^[[:digit:]][[:digit:]][[:digit:]]/(&)/g'
```

- [ ] It will only match digits—and since the string has only digits, the command will output the same number without changes.
- [ ] It will output the same 10-digit number, but every digit will be inside parentheses.
- [ ] It will output the entire 10-digit number inside parentheses.
- [x] It will output the same 10-digit number, but the first 3 digits will be inside parentheses.

Note: check the question below for a variant of this sed expression.

#### Q18. What would this sed command do?

```bash
sed -E 's/[a-Z]{4}/(&)/'  textfile.txt
```

- [ ] It would substitute the letter with an ampersand (&).
- [ ] It would replace all letters in the textfile.txt file with ampersand (&).
- [ ] It would replace the first four letters with an ampersand (&).
- [x] It would place parentheses around the first four letters of each line of textfile.txt.

Note: check the question above for a variant of this sed expression.

Side note: this sed expression may fail with "sed: -e expression #1, char 15: Invalid range end" (for example on MINGW64 / Git Bash); if this is the case, you can try the alternative range `[A-z]`.

#### Q19. Packages can be downloaded but not installed with yum or dnf by specifying which option?

- [ ] None of these answers. yum does not support downloading packages without installing them.
- [ ] --downloaddir
- [ ] -d
- [x] --downloadonly

#### Q20. What character class is equal to this set?

`[0-9]`

- [ ] `[[:alnum:]]`
- [x] `[[:digit:]]`
- [ ] `[[:alpha:]]`
- [ ] `[[:num:]]`

#### Q21. When archiving files, which command will preserve all file attributes including ACLs and SELinux security context?

- [ ] zip
- [x] tar
- [ ] archive
- [ ] gzip

#### Q22. In a systemd-based OS, you can change the system hostname by editing /etc/hostname manually and then doing what?

- [ ] Restart dhcpd.
- [ ] Run /etc/hostname.
- [x] Nothing, the system notices automatically.
- [ ] Notify systemd to update it by restarting the systemd-hostnamed service.

#### Q23. What command would you use to resize an LVM volume group to include an additional physical volume?

- [ ] vgadd
- [ ] vgresize
- [ ] vgappend
- [x] vgextend

#### Q24. When would this system cron job run its task?

`0 1 \* \* \*`

- [ ] every minute of the hour
- [ ] every hour of every day
- [x] every day at 1:00 AM
- [ ] only on Mondays

#### Q25. ifconfig has been deprecated. What command is now recommended for changing IP addresses in the live config?

- [ ] netconf
- [ ] ipconfig
- [ ] ipman
- [x] ip

#### Q26. You are managing an Apache web server on a system using SELinux. By default it cannot read personal webpages in users' home directories. What SELinux boolean would you set to allow this?

- [ ] apache_enable_homedirs
- [ ] httpd_enable_userdirs
- [x] httpd_enable_homedirs
- [ ] httpd_enable_userhome_dirs

#### Q27. Why doesn't passwd -l keep a user from logging in via other methods?

- [ ] The passwd command is not used for locking passwords.
- [ ] There is no password -l option.
- [x] It locks only the password, not the account, so users can still authenticate with keys or other methods.
- [ ] It does lock the account, keeping users from logging in even if they are using other authentication methods.

#### Q28. In the Bash shell, what is the difference between piping into | and piping into |&?

- [ ] Piping into | pipes both stdout and stderr. Piping into |& pipes only stderr.
- [x] Piping into | pipes stdout. Piping into |& pipes stdout and stderr.
- [ ] Piping into | pipes both stdout and stderr. Piping into |& pipes only stdout.
- [ ] Piping into | pipes stdout. Piping into |& pipes all open file descriptors.

#### Q29. Why is the passwd command able to modify the /etc/passwd file?

- [ ] The kernel identifies it as one of the names of extended commands.
- [ ] It has the same name as the file it modifies.
- [x] It has the SUID permission mode and is owned by root.
- [ ] It is a system administration command.

#### Q30. When a user deletes a file using the rm command, Linux will \_.

- [ ] always ask for confirmation
- [ ] back up the file before it deletes the file
- [x] ask for confirmation if configured to do so
- [ ] never ask for confirmation

#### Q31. What is a major advantage of using Logical Volume Management (LVM)?

- [ ] Access to a drive is faster than with standard partitions.
- [ ] Volumes can be resized smaller without unmounting them.
- [ ] Repairing filesystem errors is easier than with standard partitions.
- [x] Volumes can be resized even if the free space is not contiguous.

#### Q32. What is one major difference between brace expansion and globs?

- [ ] Globs create a list; brace expansion matches pattern.
- [ ] Brace expansion requires files to exist; globs do not.
- [x] Brace expansion creates a list; globs match the list of pathnames.
- [ ] Globs get processes first and brace expansion later.

#### Q33. To remove all ACLs from a directory , use setfacl with which options?

- [ ] -d
- [ ] -k
- [x] -b
- [ ] -x

#### Q34. Which choice will _not_ print "Hello World" in the terminal?

- [ ] A

```bash
myVar = 5
[[ $myVar -lt 10 ]] && echo " Hello World"
```

- [x] B

```bash
myVar = 5
[[ $myVar -lt 10 ]] || echo " Hello World"
```

- [ ] C

```bash
myVar = 5
[[ ! $myVar -gt 10 ]] && echo " Hello World"
```

- [ ] D

```bash
myVar = 5
[[ $myVar -gt 10 ]] || echo " Hello World"
```

#### Q35. What is not inherited by child process?

- [x] shell aliases
- [ ] userid
- [ ] environmental variables
- [ ] scheduling priority

#### Q36. What NFS option allows the root user to access NFS shares as the root user?

- [ ] no_admin_squash
- [x] no_root_squash
- [ ] allow_root_access
- [ ] all_squash

#### Q37. You send an email to a remote client using the following syntax. What will be in the body of the email?

```bash
date | mail -s "This is a remote test" user1@rhhost1.localnet.com
```

- [ ] "This is a remote test"
- [ ] the date, the time, and the words "This is a remote test"
- [ ] The email subject shows "This is a remote test" but the body of the email will be empty.
- [x] the current date and time

#### Q38. What is the /etc/hosts file used for?

- [ ] resolving the local name
- [ ] blocking sites using iptables
- [ ] setting the hostname
- [x] configuring DNS name servers

#### Q39. In an extended regular expression, you would use (pattern){3} to match three instances of the pattern. How would you match the same thing with an extended glob?

- [ ] 3(pattern)
- [ ] {0,3}(pattern}
- [x] Occurrence quantifiers are not supported in Bash's version of extended globs, so this is not possible.
- [ ] {3}(pattern})

#### Q40. When configuring a Samba share, how would the engineering group be specified in the smb.conf?

- [ ] Samba uses Linux operating system groups from the /etc/group file; just specify the group name.
- [ ] It would be preceded by a percent sign (%), such as %engineers.
- [ ] Use the group name by itself; Samba checks for its existence.
- [x] It would be preceded by an @ symbol, such as @engineering.

#### Q41. To configure the Kerberos client, which command should you use to import the keytab file?

- [ ] krb5-workstation
- [x] ktutil
- [ ] pam_krb5
- [ ] kdb5_util

#### Q42. To search from the current cursor position up to the beginning of the file using VIM, type \_ and then the search criteria.

- [x] `?`
- [ ] `\`
- [ ] `/`
- [ ] `/search`

#### Q43. What is the job of the NetworkManager daemon?

- [ ] It is a graphical tool that manages network connections, including bonding and wireless networks.
- [ ] It is a security service that manages user access control of local network-aware services.
- [ ] It attempts to keep an active network connection available at all times.
- [x] It is a command-line tool that manages network connections.

#### Q44. Why might would you use the usermod command ?

- [ ] to log out a user
- [ ] to lock a user's account
- [x] to change global user account settings
- [ ] to set a user's password

#### Q45. Extending an LVM volume group does what to the formatted filesystem?

- [ ] It prepares the filesystem for use by defragmenting it.
- [ ] It resizes the filesystem to match the volume group size.
- [x] It does nothing.
- [ ] It remounts the filesystem with the new size.

#### Q46. Which kernel module do you need to load to use interface bonding?

- [x] bonding.
- [ ] team.
- [ ] netbond.
- [ ] bond.

#### Q47. What does this command string do?

```bash
find / -size -10K -exec ls -l {} \;
```

- [ ] It finds all files larger than 10k and long lists them using the ls command.
- [ ] It finds all files of size 10k using ls -l and hands them off to the find command to display.
- [ ] It finds all files in the / directory of size 10k and long lists them.
- [x] It finds all files in the file system smaller than 10k and long lists them using the ls command.

#### Q48. To change the priority of multiple swap partitions, which file would you edit?

- [ ] /proc/swapiness
- [x] /etc/fstab
- [ ] /etc/mounts
- [ ] /etc/swaps

#### Q49. What would you type to list all systemd service unit files, whether they are enabled or not?

- [ ] systemctl list-services.
- [ ] chkconfig --list-all
- [x] systemctl list-unit-files -at service
- [ ] systemctl list-unit-files -t service

#### Q50. You can set Linux group passwords using which command?

- [x] gpasswd
- [ ] passwd
- [ ] editsam
- [ ] grouppass

#### Q51. With most GNU commands, if an option is a word, what will it be preceded by?

- [x] two dashes
- [ ] a backslash
- [ ] one dash
- [ ] nothing

#### Q52. What would happen if you have a script file named script that takes a long time to complete, and you type `nohup ./script &` in the command line?

- [ ] The script will remain running in the background even if you reboot the system.
- [ ] The script will run in your terminal and you will not be able to do anything until it completes.
- [ ] The script will run in the background until you end the session.
- [x] The script will run in the background and will continue running even if you end the session.

Reference: [Wikipedia](https://en.wikipedia.org/wiki/Nohup)

> nohup is a POSIX command which means "no hang up". Its purpose is to execute a command such that it ignores the HUP (hangup) signal and therefore does not stop when the user logs out.

#### Q53. To elevate privileges using the `sudo` command, a user must **\_**.

- [ ] enter the root user's password
- [x] enter their own password
- [ ] enter the sudo user's password
- [ ] change to the root group

[A Cloud Guru's Blog](https://acloudguru.com/blog/engineering/linux-commands-for-beginners-sudo#:~:text=Sudo%20asks%20for%20your%20user%20password.%C2%A0%20Note%20that%20it%20is%20asking%20for%20your%20password%2C%20not%20the%20root%20password.)

#### Q54. When would this system cron job run its task?

`0 22 * * 1-5`

- [ ] on the 22nd of every month from June to May
- [x] at 10:00 PM Monday to Friday
- [ ] every 22 minutes every day except weekends
- [ ] from 1:00 AM to 5:00 AM on the 22nd of every month

#### Q55. How does TCP Wrappers differ from a firewall?

- [ ] Firewalls are only service specific, whereas TCP Wrappers can block all traffic.
- [ ] TCP Wrappers works at the network layer, so it blocks traffic before the firewall even sees it.
- [ ] Firewalls easily spawn commands to operate on connection data, whereas TCP Wrappers cannot.
- [x] TCP Wrappers works at the application layer, so it can make access decisions on encrypted data.

**Note:** TCP Wrapper works on Application Layer but answer is not too much confirmed.

#### Q56. As root, you set execute permissions for user, group, and other on a directory. Now users can do what?

- [ ] They can execute files in it.
- [x] They can traverse it.
- [ ] They can read files in it.
- [ ] They can delete files in it.

**Note:** This is correct because of the keyword "directory". More info at: https://www.tutorialspoint.com/unix/unix-file-permission.htm

#### Q57. What will this command print?

`echo "Thu Jun 4 15:45:45 PDT 2020" | cut -f3 -d" "`

- [ ] It will print nothing.
- [ ] Thu Jun 4 15:45:45 PDT 2020
- [ ] 0.6567708333333333
- [x] 4

#### Q58. How can you improve this code snippet?

```
if ls /etc/passwd &> /dev/null
then
    echo "exists"
fi
```

- [ ] The code snippet cannot be improved, this is a valid way of checking for the existence of a file.
- [x] Use Bash's built-in `[[ ]]` test conditions instead of the ls command.
- [ ] The redirect to `/dev/null` will silence the return code invalidating the conditional. Removing the redirect will solve this.
- [ ] The ls command will output the name of the file to the screen. Running ls in quiet mode will improve the code snippet.

#### Q59. Using a systemd-based distribution, you want to restrict the cron service from running either automatically or manually. Which command would you run?

- [ ] systemctl disable crond
- [ ] systemctl disallow crond
- [x] systemctl mask crond
- [ ] systemctl stop crond

**Note:** This is the correct answer because "mask" prohibits all kinds of activation of the unit, including manual activation.
[Reference](https://www.commandlinux.com/man-page/man1/systemctl.1.html) : search "mask".

#### Q60. What issue might a user have when they mount a filesystem by partition path such as /dev/sdal in the /etc/fstab file?

- [x] The device order may change on boot, resulting in a system that will not boot properly.
- [ ] The user may run out of device letters.
- [ ] There are no issues with referring to partitions by their partition path.
- [ ] It is more difficult identifying mounted devices by partition path.

[Reference](https://access.redhat.com/discussions/6004221)

#### Q61. Which option would you choose to force grep to use a basic regular expression (BRE)?

- [ ] grep -E
- [ ] grep -B
- [ ] grep -e
- [x] grep -G

**Explanation**: Man page of grep command.

#### Q62. An rsyslogd filter determines which items in a log file to act on. What is it made up of?

- [ ] a facility and an action
- [x] a filter and an action
- [ ] a facility and a priority
- [ ] a filter and a priority

[Reference](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/system_administrators_guide/ch-viewing_and_managing_log_files)

#### Q63. Which choice is a Network Manager tool used to configure network connections from the GUI?

- [ ] nmcli
- [ ] ip
- [ ] Onmtui
- [x] nm-connection-editor

#### Q64. What will not happen if you run the make command without parameters?

- [x] It will clean up all previously generated binaries and perform a new build.
- [ ] It will run rules of compilation and building.
- [ ] It will look for a file called makefile in your current directory.
- [ ] It will build only programs that need to be rebuilt.

#### Q65. Most commands that support SELinux use which option to display SELinux security context?

- [ ] -S
- [ ] --selinux
- [ ] --MAC
- [x] -Z

#### Q66. What is the difference between the whoami and logname commands?

- [ ] whoami and logname provide the same information.
- [x] whoami tells who are you currently, and logname tells who you were when you logged in initially.
- [ ] logname specifies the name of the login log file, and whoami prints the logged in username.
- [ ] whoami shows you who logged in as initially, and logname shows who are you currently.

#### Q67. What is the command to create an associative array in Bash?

- [ ] declare -a
- [ ] aarray
- [ ] array -a
- [x] declare -A

#### Q68. What tool Should you use to replace a physical volum in LVM?

- [ ] lvcopy
- [ ] tar
- [x] pvmove
- [ ] cp

#### Q69. What is the difference the `==` and `=~` comparison operators when used in BASH double square bracket `if` conditionals?

- [x] The `==` operator performs a string comparison; `=~` performs a regex comparison.
- [ ] The `==` operator performs a string comparison; `=~` performs a glob pattern comparison.
- [ ] The `=~` operator performs a string comparison; `==` performs a regex comparison.
- [ ] There is no `=~` operator in BASH `if` conditionals.

#### Q70. What is the difference between these two lines of code?

```shell
   echo "data" | tee -a file.txt
   echo "data" >> file.txt
```

- [x] The first line will append the word `data` to file.txt and output it on the screen. The second line will append the word `data` only to file.txt.
- [ ] They are the same.
- [ ] The first line will append the word `data` to file.txt and there will be no output on the screen. The second line will output the word `data` on the screen and append it to `file.txt`
- [ ] Both lines will overwrite file.txt with the word data.

#### Q71. Using backreferences in a POSIX regular expression, which word would this pattern match?

```shell
(ss).*\1
```

- [ ] addressee
- [x] possess
- [ ] barrenness
- [ ] successfully

#### Q72. To run CGI scripts with Apache, you need to **\_**.

- [ ] compile the script with a CGI compiler
- [ ] make the script executable
- [x] make the script executable and set the `httpd_enable_cgi` SELinux boolean
- [ ] change the ownership of the script to Apache

[reference here](https://selinuxproject.org/page/ApacheRecipes#Allow_the_Apache_HTTP_Server_to_run_CGI_scripts)

#### Q73. To permanently add NAT to the default zone using firewalld, you would use which command string?

- [ ] `firewall-cmd --permanent --add-nat`
- [x] `firewall-cmd --permanent --add-masquerade`
- [ ] `firewall-cmd --zone=default --add-nat`
- [ ] `firewall-cmd --zone=default --add-masquerade`

[reference here](https://www.rootusers.com/how-to-use-firewalld-rich-rules-and-zones-for-filtering-and-nat)

#### Q74. What is the difference between using `=` and `==` in a BASH double square bracket `if` conditional?

```
if [[ $FILE == $GLOB ]] ;then

```

- [ ] The single equal sign (`=`) is an assignment operator; the double equal sign (`==`) checks equality.
- [x] There is no difference.
- [ ] The single equal sign (`=`) checks equality; the double equal sign (`==`) checks string equality.
- [ ] The double equal sign (`==`) is an assignment operator; the single equal sign (`=`) checks equality.

[reference here](https://stackoverflow.com/a/12948608)

#### Q75. `journald` differs from traditional logging services such as `rsyslogd` and `syslogd` because its logs are **\_** by default.

- [ ] stored remotely
- [ ] text
- [x] persistent
- [ ] not persistent

[reference here](https://sematext.com/blog/journald-logging-tutorial/#toc-journald-storage-4)

#### Q76. What is the purpose of a Mail Transport Agent (MTA)?

- [ ] It transports the mail from user's computer to the mail server.
- [ ] It accepts mail and adds it to the mail queue for further processing.
- [ ] It stores the mail in a mail queue waiting for the MUA to download it.
- [x] It transports mail from one mail server to another.

#### Q77. What do you need to do before you can perform SSH passwordless logins?

- [x] Generate RSA or DSA key pairs using ssh-keygen.
- [ ] Change the remote user's password.
- [ ] Create a local SSL certificate.
- [ ] Change the remote SSH configure to allow it.

[Reference](https://phoenixnap.com/kb/setup-passwordless-ssh)

#### Q78. When installing a downloaded package on the RedHat-based distribution manual using RPM, what may you have to do first?

- [ ] Compile the package source code.
- [x] Download all dependencies and install them before installing the desired package.
- [ ] Agree to an end-user license agreement.
- [ ] provide the --resolve option so RPM resolves all packages dependency.

**[Explanation:](https://access.redhat.com/discussions/2026743)** Rpm is not meant to resolve dependencies. It checks whether required software (versions) are installed and fails when software is missing and when the wrong version of software is installed.

#### Q79. With GNU tools such as a GNU grep, awk, and sed, what is the difference between basic regular expressions (BREs) and extended regular expressions (EREs)?

- [ ] EREs can match the groups.
- [ ] EREs support occurrence operators.
- [ ] ERE's support alternation.
- [x] only the syntax differs.

[Reference](https://www.gnu.org/software/sed/manual/html_node/BRE-vs-ERE.html)

#### Q80. What is the difference between reading the list of disk partitions from `/proc/partitions` and getting it using `fdisk -l`?

- [ ] `/proc/partitions` represents the disk partition table more accurately than `fdisk -l`
- [ ] `/proc/partitions` shows only mounted drives. `fdisk -l` shows all drivers.
- [ ] There is no difference between the two, and both lists contain the same data.
- [x] `/proc/partitions` is the kernel's list of partitions held in ram. `fdisk -l` reads the partition table from the drive itself.

#### Q81. What would be in out.txt?

    cat < in.txt > out.txt

- [x] the content of in.txt.
- [ ] the output from the command line.
- [ ] Nothing, because you cannot redirect from a file (in.txt) to another file (out.txt). You can redirect only from a command to a file.
- [ ] Nothing, The redirect will create a new empty file, but there will not be any output from the cat command to redirect.

#### Q82. Using alternation in a POSIX-extended regular expression, which numbers would this pattern match?

```
^(([0-9][0-9]?)|(2[0-9][0-9]))$
```

- [x] 0-99 and 200-299
- [ ] 0-99
- [ ] 200-299
- [ ] 0-299

#### Q83. Typing `systemctl enable crond` does what to the crond service?

- [ ] Starts the crond service now.
- [ ] Allows user to start the crond service.
- [ ] Unmasks the crond service.
- [x] Ensures that the crond service starts automatically on bootup.

#### Q84. Which of these features is missing from the Bash Language?

- [ ] associative arrays.
- [ ] extended regular expressions.
- [ ] debug traps.
- [x] object orientation.

#### Q85. What is the first step to integrate extended globs into your command-line workflow?

- [ ] Nothing, extended globs are already integrated into the shell and turned on automatically.
- [x] Make extended globs persistent by adding `shopt -s extglob` to a shell startup file.
- [ ] Type `shopt -s extglob` into a shell one time to set the option on permanently.
- [ ] Make extended globs persistent by adding `shopt +s extglob` to a shell startup file.

#### Q86. Which statement about default ACLs is true?

- [x] They provide inheritance for user and group permissions.
- [ ] They work only on files.
- [ ] They provide inheritance for group ownership.
- [ ] They grant access to the directory on which they are set.

[reference:](https://www.redhat.com/sysadmin/linux-access-control-lists#setting-an-acl)

#### Q87. The object that `systemd` uses to manage services is called a \_ file.

- [x] unit
- [ ] service
- [ ] single
- [ ] process

#### Q88. What tool should you use to replace a physical volume in LVM?What tool should you use to replace a physical volume in LVM?

- [ ] cpcp
- [ ] pvmovepvmove
- [ ] tartar
- [ ] lvcopy

#### Q89. What is the difference between the apt remove and apt autoremove commands?

- [ ] The apt remove command is a link to apt autoremove, so there are no differences.
- [x] Both uninstall software. The apt autoremove command also uninstalls the dependencies.
- [ ] Both uninstall software. The apt remove command also uninstalls the dependencies.
- [ ] The apt autoremove command is a system service that routinely removes unused software packages.

[reference](https://dannyda.com/2021/08/19/whats-the-difference-between-apt-remove-and-apt-autoremove-what-is-apt-purge-when-to-use-debian-ubuntu-kali-linux-etc/)

#### Q90. You want to extract the contents from an rpm package. Which command do you use?

- [ ] rpm --update
- [ ] rpm -ivh --force
- [ ] rpm --reinstall
- [x] rpm2cpio

1. [reference:](https://stackoverflow.com/questions/18787375/how-do-i-extract-the-contents-of-an-rpm)
2. [reference:](https://man7.org/linux/man-pages/man8/rpm2cpio.8.html)

#### Q91. Which variable contains last background job process id ?

- [x] `$!`
- [ ] `$$`
- [ ] `$?`
- [ ] `$*`

[reference:](https://www.globalguideline.com/interview_questions/Answer.php?a=Which_variable_contains_last_background_job_process_ida_b_c_d_)

#### Q92. Which feature does LVM2 included in most distributions not support?

- [ ] volume mirroring
- [x] volume striping
- [ ] increasing LV size while mounted
- [ ] reducing LV size while mounted

#### Q93. Which improvements do access control lists (ACLs) have over standard Linux permissions?

- [x] ACLs allow permissions to be set for more than one user or group on a file or directory.
- [ ] ACLs provide mandatory access control (MAC) functionality through SELinux for files and directories.
- [ ] ACLs allow a file to be owned by more than one user and group.
- [ ] ACLs provide additional flags such as append-only and immutable.

#### Q94. What is a maximum length for a filename under Linux?

- [ ] 256 bytes
- [ ] 1084 bytes
- [x] 255 bytes
- [ ] 1023 bytes

#### Q95. Which command do you use to rename a file in Linux?

- [x] mv
- [ ] rn
- [ ] rename
- [ ] ren

#### Q96. Which file is backup file of /etc/passwd ?

- [x] /etc/passwd-
- [ ] /etc/passwd
- [ ] /etc/paaswd.
- [ ] We can not recover

#### Q97. Which Vim command writes your changes to the currently open file and quits the Vim editor?

- [ ] :q!
- [x] :wq
- [ ] :sq
- [ ] :w

#### Q98. Just like IP addresses identify hosts on a network, **\_** identify the services on a host.

- [ ] DHCPs
- [ ] subnet masks
- [x] ports
- [ ] broadcast addresses

#### Q99. Which command shows the free disk space on one or more Linux filesystems?

- [ ] ls
- [ ] cd
- [ ] du
- [x] df

#### Q100. In Linux, the Epoch is the number of seconds that have elapsed since January 1st, **\_**.

- [ ] 1950
- [ ] 1965
- [ ] 1960
- [x] 1970

#### Q101. In which Linux shell script positional parameter is the script itself stored?

- [ ] $2
- [ ] $1
- [x] $0
- [ ] $9

#### Q102. VirtualBox provides **\_**, which are installed on guests and allow the guest operating system to access shared folders on the host system, share the clipboard, and some other similar actions.

- [ ] projects
- [ ] guest configurations
- [ ] SSHs
- [x] guest additions

#### Q103. Given an IP address of 199.83.131.0 and a subnet mask of 255.255.255.0, what is the broadcast address?

- [ ] 199.83.131.1
- [ ] 10 Downing Street
- [ ] 199.83.131.0
- [x] 199.83.131.255

#### Q104. Which Linux command shows a list of processes associated with the current user and the current terminal?

- [x] ps
- [ ] ls
- [ ] pidof
- [ ] ps -e

#### Q105. In a shell script, to create an infinite while loop, make the condition always return true by using the **\_** command for the while loop condition.

- [ ] return
- [ ] continue
- [x] true
- [ ] always

#### Q106. In Linux, which option is used with the uname command to print the processor architecture name?

- [x] -p
- [ ] -arch
- [ ] -ps
- [ ] -pname
