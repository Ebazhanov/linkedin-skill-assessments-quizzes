#Linux

1)To mount a drive by its ID, what command would you use first to retrieve it?

•df -h
•listid
•ls -l
•blkid \*\*correct

2)Linux file access control lists (ACLs) are **\_**.

•discretionary access control system permissions layered over standard Linux permissions \*\*correct

•mandatory access control system permissions layered over standard Linux permissions

•a type of firewall for Linux

•the same as standard Linux permissions



3)When using iproute2, how do you show routing information for an IPv6 network?

•route -ipv6
•route
•ip -6 route show \*\*correct
•ip route show

4)What does this command string do?
find / -size +10M -exec ls -l {} ;

•It finds all files using ls -l and hands them off to the find command to display.

•It finds all files older than 10 minutes and long lists them using the ls command.

•It finds all files larger than 10 MB and long lists them using the ls command. \*\*correct

•It uses the ls command to find all files in the filesystem matching the {} wildcard.

5)What would this locate command show?
locate --regexp '^/usr.*pixmaps.*jpg\$'

•all files in a directory named pixmaps

•all files ending in ".jpg"all files ending in ".jpg"

•all file paths that start with "/usr", include the word "pixmaps", and end with ".jpg" \*\*correct

•all file paths that include "/usr/pixmaps" and end with ".jpg"

6)Which command allows you to do packet analysis from the command line?

•wireshark

•ethtool

•netstat

•tcpdump \*\*correct

7)Which command will tell you how long a system has been running?

•log

•uptime \*\*correct

•runtime

•access

8)How would you describe PCP (Performance Co-Pilot)?

•It is an application testing suite used to profile programming code.

•It is a local command used for monitoring local system resources in real time.

•It is a set of tools, services, and libraries for gathering and analyzing performance measures. \*\*correct

•It is a tool designed to change system configuration for purposes of optimization.

9)You want to resolve a long list of DNS names using dig. What should you do?

•Create a text file including all names and use the -f option of dig. \*\*correct
•Type in each query manually.
•Write a shell script to send multiple dig queries to the DNS server.
•Save the DNS names in an SQL database and process it with dig.

10)What would this command output?
ps -e --format uid,pid,ppid,%cpu,cmd

•the user ID, process ID, parent process ID, CPU usage, and command name of a process \*\*correct

•the user ID, group ID, parent process ID, CPU usage, and command name of a process

•the UUID, process ID, parent process ID, CPU usage, and command name of a process

•all of these answers



11)Which command in Bash executes the last line in the shell history that starts with ls?

•!

•!!

•!\*

•!ls \*\*correct

12)The ssh-copy-id command copies **\_** to the remote host.

•both private and public keys

•the ssh public key \*\*correct

•the ssh private key

•a fingerprint file

13)What command is used to determine the amount of disk usage for a directory?

•find

•fdisk

•du \*\*correct

•df

14)A backup drive was created using dd to make a bit-for-bit copy. When the drive is inserted into an iSCSI target before it is booted up, the data appears to be missing. What happened?

•The backup drive is corrupted and needs to be re-created.

•When the backup drive was duplicated, the label was as well. When booted, the system mounted the old duplicated drive by its identical label. \*\*correct(I guess)

•There is a conflict between the physical location of the backup drive and the original drive.

•The backup process went wrong, and the old drive was duplicated over the original drive.

15)What is the key difference between a redirect (>) and piping to the tee command?

•The tee command sends output only to STDOUT and STDERR.

•A redirect sends output to STDOUT and a file, whereas a tee sends output only to STDOUT.

•Nothing, they are the same. \*\*correct

•The tee command sends output to STDOUT and a file, whereas a redirect sends output only to a file.

16)What does the /etc/nsswitch.conf file manage?

•priority of one DNS server over another

•per network interface DNS server configuration

•alternative DNS services

•sources for name service information \*\*correct

17)Assume the variable myNumber holds a string consisting of 10 digits. What will this command output?

echo \$myNumber | sed -e 's/^[[:digit:]][[:digit:]][[:digit:]]/(&)/g'

•It will only match digits—and since the string has only digits, the command will output the same number without changes.

•It will output the same 10-digit number, but every digit will be inside parentheses.

•It will output the entire 10-digit number inside parentheses.

•It will output the same 10-digit number, but the first 3 digits will be inside parentheses. \*\*correct

18)Packages can be downloaded but not installed with yum or dnf by specifying which option?

•None of these answers. yum does not support downloading packages without installing them.

•--downloaddir

•-d

•--downloadonly \*\*correct

19)What character class is equal to this set?
[0-9]

•[[:alnum:]]
•[[:digit:]] \*\*correct
•[[:alpha:]]
•[[:num:]]

20)When archiving files, which command will preserve all file attributes including ACLs and SELinux security context?

•zip
•tar \*\*correct
•archive
•gzip

21)In a systemd-based OS, you can change the system hostname by editing /etc/hostname manually and then doing what?

•Restart dhcpd.
•Run /etc/hostname.
•Nothing, the system notices automatically. \*\*correct
•Notify systemd to update it by restarting the systemd-hostnamed service.

22)What command would you use to resize an LVM volume group to include an additional physical volume?

•vgadd
•vgresize
•vgappend
•vgextend \*\*correct

23)When would this system cron job run its task?
0 1 \* \* \*

•every minute of the hour
•every hour of every day  
•every day at 1:00 AM \*\*correct
•only on Mondays

24)ifconfig has been deprecated. What command is now recommended for changing IP addresses in the live config?

•netconf
•ipconfig
•ipman
•ip \*\*correct



25)You are managing an Apache web server on a system using SELinux. By default it cannot read personal webpages in users' home directories. What SELinux boolean would you set to allow this?

•apache_enable_homedirs
•httpd_enable_userdirs
•httpd_enable_homedirs \*\*correct
•httpd_enable_userhome_dirs

26)Why doesn't passwd -l keep a user from logging in via other methods?

•The passwd command is not used for locking passwords.
•There is no password -l option.
•It locks only the password, not the account, so users can still authenticate with keys or other methods. \*\*correct(I guess)
•It does lock the account, keeping users from logging in even if they are using other authentication methods.

27)In the Bash shell, what is the difference between piping into | and piping into |&?

•Piping into | pipes both stdout and stderr. Piping into |& pipes only stderr.
•Piping into | pipes stdout. Piping into |& pipes stdout and
stderr. \*correct

•Piping into | pipes both stdout and stderr. Piping into |& pipes only stdout.
•Piping into | pipes stdout. Piping into |& pipes all open file descriptors.

28)Why is the passwd command able to modify the /etc/passwd file?

•The kernel identifies it as one of the names of extended commands.
•It has the same name as the file it modifies.
*Correct* •It has the SUID permission mode and is owned by root.
•It is a system administration command.

29)When a user deletes a file using the rm command, Linux will **\_**.

•always ask for confirmation
•back up the file before it deletes the file
•ask for confirmation if configured to do so \*\*correct
•never ask for confirmation

30)What is a major advantage of using Logical Volume Management (LVM)?

•Access to a drive is faster than with standard partitions.
•Volumes can be resized smaller without unmounting them.
•Repairing filesystem errors is easier than with standard partitions.
•Volumes can be resized even if the free space is not contiguous. \*\*correct

31)What is one major difference between brace expansion and globs?

•Globs create a list; brace expansion matches pattern.
•Brace expansion requires files to exist; globs do not. ( I dont know the answer)
•Brace expansion creates a list; globs mart the list of pathnames.
•Globs get processes first and brace expansion later.

32)To remove all ACLs from a directory , use setfacl with which options?

•-d
•-k
•-b \*\*correct
•-x

33)Which choice will not print "Hello World" in the terminal?

•myVar = 5
[[ $myVar -lt 10 ]] && echo " Hello World" \*\* I dont know the answer
•myVar = 5
[[ $myVar -lt 10 ]] || echo " Hello World"
•myVar = 5
[[ $myVar -gt 10 ]] && echo " Hello World"
•myVar = 5
[[ $myVar -gt 10 ]] || echo " Hello World"

34. What is not inherited by child process?

•shell aliases ( I dont know the answer)
•userid
•environmental variables
•scheduling priority
