## Microsoft Power Automate

#### Q1. How do you rename a template step?

- [ ] click the name and type over it
- [ ] highlight the step and, in the menu bar, select Rename step.
- [x] at the top-right corner of the step card, click the small ellipsis and select Rename
- [ ] from the flow's detail page, in the menu var, click Rename.

#### Q2. If you create the flow directly in Microsoft Teams, who can use the flow?

- [x] only members of the specific team channel in which you created the flow
- [ ] only people with whom you specifically share the flow
- [ ] anyone in your team
- [ ] anyone in your organization

#### Q3. You are using a scheeduled flow to copy information from one databse to another. What is an important caveat to keep in your mind?

- [x] All field names in both DB must match exactly and there must be the same number of records in each DB
- [ ] you must alays create a loop to verify your data has been successfully copied
- [ ] Power automate does not support two-way synchronization, so changes made in the destination are not copied back to the source.
- [ ] you can copy data only between DBs in the same environment.

#### Q4. The flow pictured saves new email attachments in SharePoint, adds a row to Excel to document the file save, and sends a message to TEAMS. What is the proper placement of steps B, D, and E?

![Image of footer](images/Q01.png?raw=png)

- [x] B, D and E belong inside C in the order listed.

#### Q5. Why would you use geofencing with Power Automate?

- [ ] to create areas within a business where flows do not process
- [x] to trigger automated flow when a device enters or exists a defined area
- [ ] to create flows that process whenever an emplotee moves from one region to another
- [ ] to create instant flows that sends a user's current location with the push of a button

[source](https://powerusers.microsoft.com/t5/Power-Automate-Cookbook/Power-Automate-flow-Location-Trigger-Geofence-Workout-tracking/td-p/426650)

#### Q6. What is a necessary requirement to using a flow template?

- [x] must have access to all connectors used in the flow
- [ ] must have Power Automate installed on your mobile device
- [ ] must have permission from template owner
- [ ] must have access to OneDrive

[source]'MT: lame qns, template are pre-set flows available freely for use. PA will have already been installed so not an issue. OneDrive is not specified so a non issue. Connectors include all nodes of the flow, including repos such as OneDrive, or SharePoint etc.'

#### Q7. What is the purpose of the flow?

![Image of footer](images/Q02.png?raw=png)

- [ ] to add events. to an Outlook calender if they are deleted in Google Calender
- [x] to delete Outlook calender events when they are deleted in Google Calender
- [ ] to send an email if there are discrepancies betweeb Outlook and Google calenders
- [ ] to delete Google calender events when they are deleted in Outlook

#### Q8. Which choice is an example of using an automated trigger?

- [ ] a flow that starts when a mobile button is pushed
- [x] a flow that starts when a new record is added to a SharePoint list
- [ ] a flow that starts when users request approval for documents
- [ ] a flow that starts at a specified time

[source](https://docs.microsoft.com/en-us/power-automate/triggers-introduction)

#### Q9. How do you make a flow available to a single team channel in Microsoft Teams?

- [x] in the channel, click 'Add a tab' and select 'Flow', then share flow with matching user group
- [ ] create a new channel called 'Shared Teams Flows' and post a link in the team chat
- [ ] you cannot restrict users at the channel level
- [ ] share the flow only with the users in the channel, then advise them to add the URL to their list of saved links in Teams.

[source](https://powerautomate.microsoft.com/en-us/blog/introducing-the-flow-tab-in-teams-and-new-teams-triggers/#:~:text=To%20get%20started%2C%20navigate%20to,choosing%20Install%2C%20followed%20by%20Save.)
'navigate to the Strategy and Planning team in Teams and add the Flow tab to the General channel.'

#### Q10. What is the difference between Delay and Delay until actions?

- [x] Delay until postpones an action until a specific date and time
- [ ] Delay until postpones an action until a field condition is reached in a loop (wrong)
- [ ] Delay postpones an action by a specific number of minutes (can be day, week etc)
- [ ] Delay postpones an action to give users time to input information (wrong)

[source](https://d365demystified.com/2020/06/17/pause-a-flow-using-delay-and-delay-until-power-automate/)

#### Q11. In the context of Power Automate, what is a solution?

- [ ] a flow thats created specifically to be shared with an entire organization
- [ ] a flow that prcesses more than 7% of the time
- [x] a portable container for flows that enables you to move and share them between environments
- [ ] a flow used to calculate numerical values

[source] (https://docs.microsoft.com/en-us/power-platform/alm/solution-concepts-alm)

#### Q12. what expression allows you to get details about the current workflow instance at run time?

- [x] workflow()
- [ ] details()
- [ ] workflowDetails()
- [ ] runDetails()

#### Q13. What are the prerequisites for creating solutions?

- [ ] Office 365 admins status - shared outside an organization
- [x] Common Data Service and an environment with version 9.1.0.267 or later
- [ ] an enterprise license for Msft Office 365
- [ ] certification in Msft Power Platform

[source](https://docs.microsoft.com/en-us/power-automate/overview-solution-flows)

#### Q14. you want to update multiple items in an excel spreadsheet with information from multiple email messages. How can you do this in a single flow?

- [ ] create auto flow that triggers when email received, add Update Excel action, then re-add it as many times as needed.
- [ ] create instant flow that updates a single record, then select multiple emails in your inox and start the flow from the menu bar
- [x] Add and Apply to each loop after the Get email actio, then add another action to write the records to Excel
- [ ] create scheduled flow that triggers when u submit a request, adda acondition that defines the info to extracted, add an Update Excel action and change the Advanced settings to repeat as needed.

#### Q15. What control would you use to build parallel branches of conditional logic based on a single value?

![Image of footer](images/Q03.png?raw=png)

- [x] Apply to each
- [ ] Scope
- [ ] Condition
- [ ] Switch

#### Q16. How do you modify a flow notifying your manager that you are working remotely to show your actual location?

- [ ] Using the appropriate template, modify the trigger so that it references your actual location instead of your profile information
- [ ] Using the appropriate template, modify the action that calls your Office 365 profile so that it references your actual location instead of your system information
- [x] Using the appropriate template, modify the action that emails your manager to include the Dynamic ContentManual > Full address in the email body
- [ ] Using the appropriate template, modify the action that emails your manager to include your location in the email body by manually entering it

#### Q17. How can you create an instant flow that requires user input?

- [ ] Start an instant flow with a manual trigger, then add conditions that include the needed input
- [x] Start an instant flow with a manual trigger. On the edit screen, click the manual trigger step and then click Add item
- [ ] Search for a manual trigger with input items in the button connector list
- [ ] Start the flow with the add input trigger, then add the manual button action after that

#### Q18. By default, the Apply to each action runs sequentially. How can you change this to run in parallel?

- [x] In the top-right corner of the card, click the small ellipsis and select Settings. Then turn on the Concurrency control setting
- [ ] In the top-right corner of the card, click the small ellipsis and select Settings. Then turn on run parallel setting
- [ ] In the top right corner of the card, click the small ellipsis and select Run Parallel
- [ ] This cannot be changed

#### Q19. How do you share a button flow from the mobile app?

- [ ] On your mobile device, from the button section in Power Automate, tap the small ellipsis to the lower right of the button, then select Share button. When prompted, enter their user information
- [x] On your mobile device, from the button section in Power Automate, tap the small ellipsis to the lower right of the button, then select Invite others. When prompted, enter their user information
- [ ] Button flows need to be created by users individually, not shared - otherwise, notifications sent by them would look as if they were coming from you
- [ ] From Power automate online, select the flow from your My flows list, and click the share icon to make them an owner so they can modify flow information

#### Q20. What can you use to process PDF forms and extract data for use in flows created with Power Automate?

- [x] AI builder
- [ ] Microsoft Forms connector
- [ ] process PDF template for Power Automate
- [ ] PDF connector

#### Q21. Can flows that have been created outside of a solution be shared in a solution?

- [ ] Yes, but only system admins have the ability to move flows into solutions after they are created
- [x] Yes, flows can be easily imported into solutions
- [ ] It is entirely dependent on the type of flow - for instance, instant flows cannot but most automated flows can.
- [ ] No, to be shared as part of a solution, they need to be created within the solution

#### Q22. You are using a scheduled flow to copy information from one database to another. what is an important caveat to keep in mind?

- [ ] Power automate does not support two-way synchronization, so changes made in the destination are not copied back to the source
- [ ] you can copy data only between databases in the same environment
- [x] All field names in both database must match exactly and there must be the same number of records in each database
- [ ] You must always create a loop to verify your data has been successfully copied

#### Q23. How do you share a template in Power Automate?

- [x] In the menu bar of the detail page for any succesfully run flow, click Submit as template
- [ ] Share tempaltes the same way you share flows: by selecting them in your My flows list and licking Share in the menu bar
- [ ] Zip the template file and email it to templates@powerautomate.com
- [ ] Export the template and post it to the Microsoft Power Automate site

#### Q24. Flows 1 and 2 both result in emails being sent. Is the difference between the flows Send email action steps significaton, and if so, why?

- [x] Yes. Number 2 will send the email from microsoft@powerapps.com; number 1 will send the email from your Outlook email address
- [ ] There is no significant difference between them
- [ ] Yes. Number 1 will permit more user inputs to be added to the message
- [ ] Yes. Number 2 will prompt the user to enter the email address to the recipient before it is sent

#### Q25. You are automating this suggestion review process: When a new suggestion is added to an SharePoint list, a staffer emails every member of the review committee, asking them to approve the suggestion. The staffer updates SharePoint as replies are received. A suggestion is approved or rejected when at least four of the seven committee members have approved or rejected it. In addition to Start and Wait for an approval, which components will be needed for your flow?

    A. Send an email
    B. Parallel branch
    C. Delay until
    D. Approvals - start an approval
    E. SharePoint - when an item is created or modified

- [ ] B,D
- [ ] A,B,D,E
- [ ] B,D,E
- [x] A,B,C,D

#### Q26. Whit whom can you share flows?

- [ ] people on the same Office 365 team as you
- [ ] fellow SharePoint site collection memebers
- [x] anyone in your organization and beyond
- [ ] people in your department

#### Q27. What control would you use to stop a flow?

- [ ] Do until
- [x] Terminate
- [ ] Scope
- [ ] Switch
