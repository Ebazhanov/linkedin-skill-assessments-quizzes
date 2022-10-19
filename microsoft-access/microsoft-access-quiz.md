## Microsoft Access Assessment

#### Q1. Which form view mode allows you to preview live data while you work on the design of the form?

- [ ] **Preview** view
- [x] **Layout** view
- [ ] **Design** view
- [ ] **Form** view

#### Q2. How can you add multiple view button controls to a form at once?

- [ ] Double-click the button control to lock it on, then left-click in the form to add each button
- [x] Right-click the button control and select Drop Multiple Controls. Then left-click to add each button to a form
- [ ] Select the Multiple Object check box in the Design tab before selecting the button control
- [ ] Left-click the button control to select it, then add multiples to the form by right-clicking in the position you'd like to add them

#### Q3. What is the Access string operator that joins or concatenates text strings together?

- [x] `&`
- [ ] `!`
- [ ] `#`
- [ ] `-`

[Caveat:](https://support.microsoft.com/en-us/office/string-functions-and-how-to-use-them-965efa84-7009-4603-9765-2eb4a099ec72)
"In a desktop database, you can also use the ampersand operator (&) for concatentation. In an Access app, you must use the plus sign (+)."\_

#### Q4. The relationship field in this table has been created with what feature?

`<p align="center"><img src="./images/question_4.png"></p>`

- [x] lookup
- [ ] reference integrity
- [ ] pick list
- [ ] validation rule

#### Q5. On a report, you want to display a header for each change in month name. How should you set up the Group and Sort options so that they are in the proper chronological order?

- [ ] Sort on month number, then sort on month name
- [ ] Sort on month number, then group on month name
- [ ] Group on month number, then sort by month name
- [x] Group on month number, then sort on month number

#### Q6. What kind of query will display data with both column headers and row headers?

- [x] crosstab
- [ ] select
- [ ] simple
- [ ] spreadsheet

[Reference](https://support.microsoft.com/en-us/office/make-summary-data-easier-to-read-by-using-a-crosstab-query-8465b89c-2ff2-4cc8-ba60-2cd8484667e8)

#### Q7. What currency format displays a thousand separator, but not a currency symbol, such as $ or €?

- [ ] Scientific
- [x] Standard
- [ ] General Number
- [ ] Fixed

[Reference](https://support.microsoft.com/en-us/office/format-a-number-or-currency-field-e48f2312-67f0-4921-aca0-15d36b7f9c3b#bkmk_examples_predefined)

#### Q8. In Access Option > Current Database, what does turning off the Allow Full Menus option do?

- [ ] removes the ribbon interface
- [ ] removes all ribbon tabs except Home and Print Preview
- [ ] disable the right-click menu when working with objects
- [x] removes the **Design** view contextual tabs, which forces most design changes to be made in **Layout** view

[Reference](https://support.microsoft.com/en-us/office/allowfullmenus-property-d1cf24ab-ca65-4450-8917-93d83319b678)

#### Q9. You want to create a form to view customer's details, as well as some information about all order that the customer has placed with your company. What is the best way to display this information on a single screen?

- [ ] Use a form to display the customer details with a subform linked to their order information
- [x] Create a split form that displays the customer information at the top and the order history in the table below
- [ ] Create a navigation form that includes a form for the customer details and a separate form for the order history
- [ ] Create a continous form that uses a query to gather all of the customer details and order history in a single record source

#### Q10. You want a form to appear automatically, whenever the database starts. How do you do this?

- [ ] In the **Access Options** dialog box, click **Current Database**, then select the form you want to open in the **Display Form** property
- [x] Open the form you want to display automatically in **Design** view. Then in the property sheet, set **Open on Launch** to **true**
- [ ] Right-click the form you want to open automatically and select **Startup Form**
- [ ] On the **Database Tools** tab, click **Database Options**, then set the form you want to open as the **Initial View** object

[Reference](https://support.microsoft.com/en-us/office/set-the-default-form-that-appears-when-you-open-an-access-database-94961011-392f-4c3b-8dbc-e5d5adbff1df)

#### Q11. In Design view, which area of a form is the primary location for text boxes, buttons, and other control objects?

- [ ] **Page Layout**
- [ ] **View** section
- [ ] Form body
- [x] **Detail** section

#### Q12. What tool builds a report containing detailed information about the object in the database?

- [ ] Object dependencies
- [ ] Table analyzer
- [ ] Access database manager
- [x] Database documenter

[Reference](https://support.microsoft.com/en-gb/office/learn-the-structure-of-an-access-database-001a5c05-3fea-48f1-90a0-cccaa57ba4af?rs=en-gb#bm1)

#### Q13. You want to validate a proposed modification to a record's value before the table is saved to the database. What data macro can you add to the table to do this?

- [ ] After Insert
- [x] Before Change
- [ ] After Update
- [ ] Before Delete

#### Q14. When you add a group to a report, what automatically gets added to the structure?

- [x] a group header
- [ ] nothing
- [ ] a group header and footer
- [ ] a group footer

[Reference](https://support.microsoft.com/en-us/office/create-a-grouped-or-summary-report-f23301a1-3e0a-4243-9002-4a23ac0fdbf3#__add_or_modify)

#### Q15. A table contains a field with the lookup properties set as shown. What will be the value of the field when the end user clicks Normal from the combo box when entering a record into the table?

| General         | Lookup                          |
| --------------- | ------------------------------- |
| Display Control | Combo Box                       |
| Raw Source Type | Value List                      |
| Raw Source      | 1:"High"; 2 :"Normal"; 3: "Low" |
| Bound Column    | 1                               |
| Column Count    | 2                               |
| Column Heads    | No                              |
| Column Widths   | 0; 1                            |
| List Rows       | 16                              |
| List Width      | Auto                            |

- [ ] 1
- [ ] 3
- [x] 2
- [ ] Normal

#### Q16. What program flow function evaluates a condition and either returns a truepart or a falsepart?

- [ ] `Switch()`
- [ ] `IsError()`
- [x] `IIf()`
- [ ] `Choose()`

[Reference](https://support.microsoft.com/en-us/office/iif-function-32436ecf-c629-48a3-9900-647539c764e3)

#### Q17. The display for numerical data defaults to a **\_alignment, and text data defaults to **\_aligntment

- [ ] left; right
- [x] right; left
- [ ] left; left
- [ ] right; right

1. [Text:](https://support.microsoft.com/en-us/office/format-a-text-field-a5e5bcde-85da-4c7a-8164-1fe286636668)
2. [Numerical:](https://support.microsoft.com/en-us/office/format-a-number-or-currency-field-e48f2312-67f0-4921-aca0-15d36b7f9c3b)

#### Q18. Which data type is a modern replacement for the OLE Object data type?

- [x] Attachment
- [ ] Replication ID
- [ ] BLOB
- [ ] Hyperlink

[Reference](https://support.microsoft.com/en-us/office/attach-files-and-graphics-to-the-records-in-your-database-d40a09ad-a753-4a14-9161-7f15baad6dbd)

#### Q19. How can you ensure that each value saved in a particular field is unique from all other values in the field?

- [ ] Set the Indexed property to No
- [ ] Set the Required property to Yes (Unique Values)
- [ ] Set the Validation Rule property to No Duplicates
- [x] Set the Indexed property to Yes (No Duplicates)

[Reference](https://support.microsoft.com/en-us/office/prevent-duplicate-values-in-a-table-field-using-an-index-b5eaace7-6161-4edc-bb90-39d1a1bc5576)

#### Q20. Which Access database tool will help you split a single, large, unnormalized data table into multiple related tables that follow the best practices of good database design?

- [ ] Database Documenter
- [ ] Compact and Repair Database
- [ ] Database Splitter Wizard
- [x] Table Analyzer Wizard

[Reference](https://support.microsoft.com/en-us/office/normalize-your-data-using-the-table-analyzer-8edbb763-5bab-4fbc-b62d-c17b1a40bbe2)

#### Q21. When backing up an Access database, what is added to the file name automatically?

- [ ] `A serialized backup number, such as "_Backup_2"`
- [x] `The current date, such as "_2019-08-21"`
- [ ] `The characters "_bu"`
- [ ] `The word "_Archive"`

#### Q22. Which table field property, if supplied, will display instead of the field name as a column header when viewing the datasheet of as a label when the field is added toa form or report?

- [ ] Popup Text
- [ ] Description
- [x] Caption
- [ ] Tool Tip

[Reference](https://support.microsoft.com/en-us/office/introduction-to-data-types-and-field-properties-30ad644f-946c-442e-8bd2-be067361987c#typereference)

#### Q23. Which form control property creates a small pop-up flag that contains text when a user hovers the mouse cursor over the object?

- [x] ControlTip Text
- [ ] Status Text
- [ ] Tool Text
- [ ] Help Text

#### Q24. The expression values <=, <>, and > are found in what expression category?

- [x] comparison operators
- [ ] logical operators
- [ ] string operators
- [ ] arithmetic operators

[Reference](https://support.microsoft.com/en-us/office/guide-to-expression-syntax-ebc770bc-8486-4adc-a9ec-7427cce39a90#bm3)

#### Q25. Which section of a report appears at the top of every page in the printed report?

- [x] page header
- [ ] group header
- [ ] detail header
- [ ] report header

[Reference](https://support.microsoft.com/en-ie/office/pageheader-property-8c6e6fe7-45fe-4f71-bd5d-71325275a812)

#### Q26. When would you use a left join query?

- [x] When you want to retrieve every record from the left table, plus any matching information from the right table where it exists
- [ ] When you want to retrieve all of the records from the right table that have matching records in the left table
- [ ] When you want to retrieve just the records from the left table that have matching records in the right table
- [ ] When you want to retrieve just the records from the left table that do not have any matching records in the right table

#### Q27. How can you run a submacro saved in a macro?

- [ ] Use an If container in the macro.
- [ ] Call the submacro with the [MacroName]![SubMacroName] syntax.
- [x] Use a RunMacro or OnError macro action.
- [ ] Expand the macro in the **Navigation Pane** and double-click the submacro name.

#### Q28. Which combo box property defines what values appear when the user clicks the drop-down arrow?

- [ ] Control Source
- [x] Row Source
- [ ] Value List
- [ ] Data Source

#### Q29. What does the expression Now() evaluate to?

- [ ] the current system date
- [ ] the current system date, time, and time zone
- [x] the current system date and time
- [ ] the current system time

#### Q30. Certain words have special meaning to Access, and you should avoid using them as table or field names. What are these words called?

- [ ] discouraged terms
- [x] reserved words
- [ ] retired objects
- [ ] system names
