
## Q1. You are reviewing previously used PowerShell code. You come across a command that was intended to change “PowerShell” to “PowerShell ISE”. Based on the command below, what is causing this error?

Ps > “PowerShell” -replace “[Shell]”,”Shell ISE”

PowerShell ISerShell ISeShell IseShell IseShell IseShell ISE

- [] The -replace cmdlet cannot be use on characters.

- [] The quotation marks prior to the square brackets need to be removed

- [x] The square brackets around “Shell” are causing all characters to be matched and replaced

- [] The text “Shell ISE” needs to be placed right before -replace “[Shell]"

- [x] Use Get-PsProvider a*, b*, c* | Format-List

- [] Use Get-PSProvider a, b, c | Format List)

- [] Use Get-PsProvider a, b, c (Format List)

## Q2 You need to establish a constant remote PowerShell session with two virtual machines to execute a few commands. How can you accomplish this?

- [] $sessions = Enter-PSSession -ComputerName vm1, vm2
- [x] $sessions=New-PSSession -ComputerName vm1,vm2
- [] $sessions=Start-Session -ComputerName vm1, vm2

- [] $sessions=Add-Session -ComputerName vm1, vm2

## Q3. What is an example of a PowerShell script that uses late filtering?

- [x] A script that uses the where-object Command

- [] A script that uses the NET filtering library
- [] A script that uses the -filter parameter

- [] A script that uses the parsing module

## Q5. You want to suppress the PowerShell command prompt window until a PowerShell job named "Server Sync” is complete. What steps would you need to take to accomplish this?

- [] Create a foreach loop with a conditional to check the status of the "Server Sync” job until it returns a code of 200.

- [] Create a switch statement with the default case conditional executing the | check-job command waiting for a status of
done.

- [] Execute the stop-job command with the name of the job for the first parameter and the wait flag for the second parameter.
- [x] Find the Job ID by executing get-job and pass the "Server Sync" job ID to wait-job

## Q6. You are creating a PowerShell script on an older Windows virtual machine that has out-of-date help files for its commandlets. What would successfully update all the help files for PowerShell modules that include the word "PowerShell"?

- [] get-help -Modules PowerShell

- [] windows-help -Module PowerShel1*

- [x] update-help -module *PowerShel1*
- [] set-help -Module *PowerShell

## Q8. What notation can be used to access the value of an object's properties?

- [] hyphen notation

- [] boolean notation

- [] not notation
- [x] dot notation

## Q9. What command imports data from an xml file and creates an object in PowerShell?

- [x] Import-Clixml

- [] Import-XML

- [] Import-File

- [] Import-Data

## Q10. Why should error and exception handling measures be implemented in all PowerShell code?

- [] To ensure program termination is achieved for every error

- [] To ensure the script restarts each time an error is received

- [] To change the error message received when something goes wrong

- [x] To prevent all errors from halting ongoing actions when desired

## Q12. Why would you need to use .ToLower() or .ToUpper() in PowerShell?

- [x] To create consistent text to return exact parameter searches
- [] To change the order that specific scripts are run

- [] To move text and scripts around within your current session

- [] To change the order and default selection of your repositories

## Q13 Why would you want to create a simple parameter in PowerShell?

- [] To more easily interpret terminating errors that occur

- [] To prevent all additional input from being run at runtime

- [x] To build reusable scripts that require hardly any code maintenance
- [] To ensure that no function’s behavior can be modified

## Q14 You are using newly installed modules in PowerShell, but they are not being imported correctly. Any cmdlet and function you use returns an error. What might be causing this issue?

- [] The imported modules were used after you ran a script in the current session.

- [] PowerShell only allows for one module to be used per session.

- [] The version of PowerShell is not currently set to PowerShell.exe Version 2.0 or lower
- [x] The PSModulePath environment variable default is not where the new modules are installed

## Q16 What is a good practice for scripting in PowerShell?

- [] Shorten and abbreviate all parameter names

- [] Use “New-Alias as often as possible
- [] Frequently use “Write-Host
- [] Use consistent indentation

## Q17 What type of measurements can the measure-object command handle for strings?

- [] File, Directory, Drive

- [] Ascii, Dot Notation, Pointers

- [x] Line, Word, Character

- [] Encryption, Decryption, FileSharing

## Q18 Why do the commands man and help generate the same information

- [] help is a sudo command for “man

- [x] man is an alias of help
- [] man is a child commandlet of help
- [] help is a recursive commandlet of man

19.What does the * parameter flag accomplish when paired with the get-help command?

- [] It provides a hyperlink to the PowerShell documentation for the command

- [] It provides information for the arguments required to execute the command

- [] It autocompletes to execute the first command
- [] It displays all help information for available parameters

## Q20. You have a displayed list of all available providers from the Get-PSProvider cmdlet in PowerShell. However, the list is extensive and you want to only see providers whose names begin with the letters a, b, and c. How could you accomplish this
