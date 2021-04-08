## Linux

#### Q1. To mount a drive by its ID, what command would you use first to retrieve it?

- [ ] df -h
- [ ] listid
- [ ] ls -l
- [x] blkid

#### Q2. Linux file access control lists (ACLs) are **\_**.

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

#### Q12. The ssh-copy-id command copies **\_** to the remote host.

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
- [x] When the backup drive was duplicated, the label was as well. When booted, the system mounted the old duplicated drive by its identical label.
- [ ] There is a conflict between the physical location of the backup drive and the original drive.
- [ ] The backup process went wrong, and the old drive was duplicated over the original drive.

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


#### Q18. Packages can be downloaded but not installed with yum or dnf by specifying which option?

- [ ] None of these answers. yum does not support downloading packages without installing them.
- [ ] --downloaddir
- [ ] -d
- [x] --downloadonly


#### Q19. What character class is equal to this set?
[0-9]

- [ ] [[:alnum:]]
- [x] [[:digit:]]
- [ ] [[:alpha:]]
- [ ] [[:num:]]

#### Q20. When archiving files, which command will preserve all file attributes including ACLs and SELinux security context?
- [ ] zip
- [x] tar
- [ ] archive
- [ ] gzip

#### Q21. In a systemd-based OS, you can change the system hostname by editing /etc/hostname manually and then doing what?

- [ ] Restart dhcpd.
- [ ] Run /etc/hostname.
- [x] Nothing, the system notices automatically.
- [ ] Notify systemd to update it by restarting the systemd-hostnamed service.

#### Q22. What command would you use to resize an LVM volume group to include an additional physical volume?

- [ ] vgadd
- [ ] vgresize
- [ ] vgappend
- [x] vgextend


#### Q23. When would this system cron job run its task?
0 1 \* \* \*

- [ ] every minute of the hour
- [ ] every hour of every day
- [x] every day at 1:00 AM
- [ ] only on Mondays

#### Q24. ifconfig has been deprecated. What command is now recommended for changing IP addresses in the live config?

- [ ] netconf
- [ ] ipconfig
- [ ] ipman
- [x] ip 

#### Q25. You are managing an Apache web server on a system using SELinux. By default it cannot read personal webpages in users' home directories. What SELinux boolean would you set to allow this?

- [ ] apache_enable_homedirs
- [ ] httpd_enable_userdirs
- [x] httpd_enable_homedirs
- [ ] httpd_enable_userhome_dirs

#### Q26. Why doesn't passwd -l keep a user from logging in via other methods?

- [ ] The passwd command is not used for locking passwords.
- [ ] There is no password -l option.
- [x] It locks only the password, not the account, so users can still authenticate with keys or other methods.
- [ ] It does lock the account, keeping users from logging in even if they are using other authentication methods.

#### Q27. In the Bash shell, what is the difference between piping into | and piping into |&?

- [ ] Piping into | pipes both stdout and stderr. Piping into |& pipes only stderr.
- [x] Piping into | pipes stdout. Piping into |& pipes stdout and stderr.
- [ ] Piping into | pipes both stdout and stderr. Piping into |& pipes only stdout.
- [ ] Piping into | pipes stdout. Piping into |& pipes all open file descriptors.

#### Q28. Why is the passwd command able to modify the /etc/passwd file?

- [ ] The kernel identifies it as one of the names of extended commands.
- [ ] It has the same name as the file it modifies.
- [x] It has the SUID permission mode and is owned by root.
- [ ] It is a system administration command.

#### Q29. When a user deletes a file using the rm command, Linux will **\_**.

- [ ] always ask for confirmation
- [ ] back up the file before it deletes the file
- [x] ask for confirmation if configured to do so
- [ ] never ask for confirmation

#### Q30. What is a major advantage of using Logical Volume Management (LVM)?

- [ ] Access to a drive is faster than with standard partitions.
- [ ] Volumes can be resized smaller without unmounting them.
- [ ] Repairing filesystem errors is easier than with standard partitions.
- [x] Volumes can be resized even if the free space is not contiguous.

#### Q31. What is one major difference between brace expansion and globs?

- [ ] Globs create a list; brace expansion matches pattern.
- [ ] Brace expansion requires files to exist; globs do not.
- [x] Brace expansion creates a list; globs mart the list of pathnames.
- [ ] Globs get processes first and brace expansion later.

#### Q32. To remove all ACLs from a directory , use setfacl with which options?

- [ ] -d
- [ ] -k
- [x] -b
- [ ] -x

#### Q33. Which choice will not print "Hello World" in the terminal?

- [ ]
```bash
myVar = 5
[[ $myVar -lt 10 ]] && echo " Hello World"
```
- [X] 
```bash
myVar = 5
[[ $myVar -lt 10 ]] || echo " Hello World"
```
- [X] 
```bash
myVar = 5
[[ $myVar -gt 10 ]] && echo " Hello World"
```
- [ ]
```bash
myVar = 5
[[ $myVar -gt 10 ]] || echo " Hello World"
```

#### Q34. What is not inherited by child process?
- [x] shell aliases
- [ ] userid
- [ ] environmental variables
- [ ] scheduling priority

#### Q35. What NFS option allows the root user to access NFS shares as the root user?
- [ ] no_admin_squash
- [ ] no_root_squash
- [x] allow_root_access
- [ ] all_squash

#### Q36. You send an email to a remote client using the following syntax. What will be in the body of the email?
```bash
date | mail -s "This is a remote test" user1@rhhost1.localnet.com
```
- [ ] "This is a remote test"
- [ ] the date, the time, and the words "This is a remote test"
- [ ] The email subject shows "This is a remote test" but the body of the email will be empty. 
- [x] the current date and time

#### Q37. What is the /etc/hosts file used for?
- [ ] resolving the local name
- [ ] blocking sites using iptables
- [x] setting the hostname
- [ ] configuring DNS name servers

#### Q38. In an extended regular expression, you would use (pattern){3} to match three instances of the pattern. How would you match the same thing with an extended glob?
- [ ] 3(pattern)
- [ ] {0,3}(pattern}
- [x] Occurrence quantifiers are not supported in Bash's version of extended globs, so this is not possible.
- [ ] {3}(pattern})

#### Q39. When configuring a Samba share, how would the engineering group be specified in the smb.conf?
- [ ] Samba uses Linux operating system groups from the /etc/group file; just specify the group name.
- [x] It would be preceded by a percent sign (%), such as %engineers.
- [ ] Use the group name by itself; Samba checks for its existence.
- [ ] It would be preceded by an @ symbol, such as @engineering.

#### Q40. To configure the Kerberos client, which command should you use to import the keytab file?
- [ ] krb5-workstation
- [x] ktutil
- [ ] pam_krb5
- [ ] kdb5_util

#### Q41. To search from the current cursor position up to the beginning of the file using VIM, type ______ and then the search criteria.
- [x] ?
- [ ] \
- [ ] /
- [ ] /search

#### Q42. What is the job of the NetworkManager daemon?
- [ ] It is a graphical tool that manages network connections, including bonding and wireless networks.
- [ ] It is a security service that manages user access control of local network-aware services.
- [ ] It attempts to keep an active network connection available at all times.
- [x] It is a command-line tool that manages network connections.

#### Q43. Why might would you use the usermod command ?
- [ ] to log out a user
- [ ] to lock a user's account
- [x] to change global user account settings
- [ ] to set a user's password
