## Visual Basic for Applications (VBA)

#### Q1. Which two sets of values are printed by this function and sub?

```
Function GetVitals(ID As Long, Age As Long, Optional Weight As Long) As String
    GetVitals="ID=" & ID &"Age=" & Age & "Weight=" & Weight
End Function
Sub ShowVitals()
    Dim ID As Long, Age As Long,Weight as Long
    Debug.Print GetVitals(ID:=5,Age:=20)
    Debug.Print GetVitals(ID:=6,Age:=25,Weight:=130)
End Sub
```

- [ ]

```
ID=5 Age = 20 Weight=
ID=6 Age = 25 Weight=130
```

- [x]

```
ID=5 Age = 20 Weight=0
ID=6 Age = 25 Weight=130
```

- [ ]

```
ID=5 Age = 20 Weight=Null
ID=6 Age = 25 Weight=130
```

- [ ]

```
ID=5 Age = 20
ID=6 Age = 25 Weight=130
```

#### Q2. This code shows the first statement of CalledSub. Which calling statement will work properly?

`Sub CalledSub(Surname, Age)`

- [ ] call Calledsub "smith",26
- [ ] calledsub (surname="smith", Age = 26)
- [ ] calledsub (Surname:="Smith", Age:=26)
- [x] calledsub "smith", 26

#### Q3. What is the principal difference between a class and an object?

- [ ] There is no meaningful difference. The terms are used interchangeably.
- [ ] A dass declares an object's properties. An object completes the declaration by defining events and methods.
- [ ] An object is a template for a class.
- [x] A class describes the design of an object. An object is an instance of that design.

#### Q4. What value does the MsgBox statement display?

```
Sub MySub(VarA As Long, ParamArray VarB() As Variant)
MsgBox VarB(0)
End Sub
Sub ShowValue()
Call MySub(10, "First arg", 2, 3.1416)
End Sub
```

- [ ] 2
- [ ] 10
- [x] First arg
- [ ] 3.1416

#### Q5. What object is needed to put a userform module in a VBA project?

- [ ] associated standard code module
- [ ] UserForm
- [ ] associated class module
- [ ] userForm class

#### Q6. What is the output?

```
Sub UseSum()
Dim TestArray() As Integer, Total As Integer
ReDim TestArray(1)
TestArray(1) = 6
ReDim TestArray(2)
TestArray(2) = 3
Total = WorksheetFunction.Sum(TestArray)
End Sub
```

- [x] 3
- [ ] 0
- [ ] 9
- [ ] 6

#### Q7. The Driver subroutine is declared by Sub Driver (Y). Which statement results in a compile error?

- [ ] Driver x
- [ ] call Driver(x)
- [ ] call Driver x
- [ ] Driver (X)

#### Q8. You have several variables to display on a user form, and there are too many variables to display at once. Which control best enables the user to see all the variables?

- [ ] Frame
- [ ] multipage
- [ ] TabStrip
- [x] ListBox

#### Q9. Below is a function named SquareIt. Which version of the subroutine named Area results in a compile error?

```
Function SquareIt(ByRef Basis As Integer) As Long
SquareIt = Basis ^ 2
End Function
```

- [ ] sub Area()

```
Dim Result As Long, Side As Integer
Side = 5
Result = Squarelt(Side)
End Sub
```

- [ ] Sub Area()

```
Dim Result As Long, Side
Side = 5
Result = SquareIt(Cint(Side))
End Sub
```

#### Q10. EmailAddress() is an array. It is declared by Dim EmailAddress(10) As String, and option Base 1 is in effect. How many rows and columns are in EmailAddress()?

- [ ] 10 rows and 10 columns
- [x] 10 rows and 1 column
- [ ] 10 rows and 0 columns
- [ ] 1 row and 10 columns

#### Q11. Which cell is selected if you run this code?

`Range("E3:312").Range("B3").Select`

- [ ] F5
- [x] F3
- [ ] B3
- [ ] E3

#### Q12. Which variable name is valid in VBA?

- [ ] `_MyVar`
- [x] `My_Var`
- [ ] `My-Var`
- [ ] `1MyVar`

[Reference link](https://docs.microsoft.com/en-us/office/vba/language/concepts/getting-started/visual-basic-naming-rules)

`Use the following rules when you name procedures, constants, variables, and arguments in a Visual Basic module: You must use a letter as the first character. You can't use a space, period (.), exclamation mark (!), or the characters @, &, $, # in the name. Name can't exceed 255 characters in length.`

#### Q13. Which is a valid definition of a user-defined data type?

- [x]

Type CBC
Name As String
Next As String
End Type

- [ ]

Type CBC
Name As String
\_Next As String
End Type

- [ ]

Type CBC
Name As String
@Option As String
End Type

- [ ]

Type CBC
Name As String
%For As String
End Type

#### Q14. What is one way to duplicate a user form from one project into a different project?

- [ ]

1. Save and close the project with the existing user form.
2. Click Insert > File.
3. Browse to the location of the existing project.
4. Right-click it and select the user-form you want to duplicate.

- [ ]

1. Open the existing user form in Desing Mode.
2. Right-click the form and select Copy.
3. Switch to the other project.
4. Right-click Module and select Paste.

- [ ]

1. In the Project Explorer, right-click the user form and select Copy.
2. Switch to the new project.
3. Right-click UserForms and select Paste.

- [x]

1. Open the existing user form in Design Mode.
2. Click File > Export File.
3. Switch to the other project.
4. Click File > Import File.

#### Q15. The recording of a macro in Word is likely to be an incomplete record of the user's actions. Why?

- [ ] Word's Macro Recorder does not record actions initiated by keyboard shortcuts.
- [ ] Word's Macro Recorder does not support Find & Replace edits.
- [ ] Word's Macro Recorder does not record actions initiated by clicking a button on the Ribbon's Developer tab.
- [x] Word's Macro Recorder does not record actions that inlove selection of text by pointing with the mouse pointer.

#### Q16. Which statement should precede a subroutuine's error handler?

- [ ] End
- [ ] Return
- [x] Exit Sub
- [ ] Stop

#### Q17. How many values can MyArray hold?

```
Option Base 0
Sub BuildArray()
Dim MyArray(5) As Integer
```

- [ ] 0
- [ ] 32,769
- [ ] 5
- [x] 6

#### Q18. Which statement is true?

- [ ] Set establishes a value in a class; Let returns a value from a class.
- [ ] Let establishes a value in a class; Set returns a value from a class.
- [x] Let establishes a value in a class; Get returns a value from a class.
- [ ] Get establishes a value in a class; Set returns a value from a class.

#### Q19. A declaration has scope, which has three levels. What are they?

- [ ] Module, Project and Automation
- [x] Procedure, Private Module and Public Module
- [ ] Subroutine, Module and Project
- [ ] Procedure, Project and Global

#### Q20. There are two references that must be selected in the Visual Basic Editor in order for any Visual Basic code to run in Excel. What are these two references?

- [ ] MS Excel object library and MS Office object library
- [ ] VBA and MS Office object library
- [x] VBA and Excel object library
- [ ] MS Excel object library and OLE automation

#### Q21. Which action will cause your project to reset its variables?

- [ ] Edit the list of arguments of the current routine while in debug mode.
- [x] Click End in a run-time error dialog.
- [ ] Add an ActiveXcontrol to a worksheet.
- [ ] all of these answers

#### Q22. Which keyboard shortcut causes VBE to locate the declaration of a procedure?

- [ ] Shift+F3
- [ ] Alt+F (Windows) or Option+F (Mac)
- [x] Shift+F2
- [ ] Ctrl+F (Windows) or Command+F (Mac)

#### Q23. When you define a new class of object, where do you assign a name to it?

- [ ] in the class module's name
- [ ] in the class module's code
- [ ] in a standard module's code
- [x] in a standard module's Properties

#### Q24. How does a class module indicate that it uses a particular interface?

- [ ] The interface itself is part of the class module.
- [ ] by means of the Interface keyword and the name of the interface
- [ ] by means of the Implements keyword and the name of the interface
- [x] The name of the interface is passed as a parameter.

#### Q25. What is needed for the contents of Module1 to be availble to other modules in a VBA project, but not to any other VBA project?

- [ ] Set Option Global at the top of Module1
- [ ] Declare module-level variables as Private
- [ ] Set Module Level Scope at the top of Module1
- [x] Set Option Private Module at the top of Module1

#### Q26. When used with an array named MyArray, what is the preerred way to set beginning and ending values of a loop control variable?

- [ ] For i = 0 To UBound(MyArray,1)
- [ ] For i = 1 To UBound(MyArray,1)
- [x] For i = LBound(MyArray,1) To UBound(MyArray,1)
- [ ] It depends on whether Option Base 0 or Option Base 1 is in use.

#### Q27. What is the value of Test3?

```
Enum TestEnum
    Test1
    Test2
    Test3
End Enum
```

- [ ] 0
- [ ] 1
- [ ] 3
- [x] 2

#### Q28. Which statement declares an array?

- [ ] Dim MyArray() As Integer
- [x] Dim MyArray() As Array
- [ ] Dim MyArray As Integer
- [ ] Dim MyArray As Array

#### Q29. To use VBA code to maintain a different VBA project, you can make use of VBA's extensibility. What is needed to enable extensibility?

- [ ] Set Macro Security to Trust Access to the VBA Project Object Model
- [ ] The project's workbook should be protected in the Ribbon's Review tab
- [x] Include a reference to Microsoft VBA Extensibility 5.3
- [ ] Include a reference to Microsoft VBA Extensibility 5.3 and set Macro Security to Trust Access to the VBA Project Object Model

#### Q30. How do you add a user form to a VBA project?

- [ ]

1. Select the project in the Project window of the Visual Basic Editor
2. Click the Design Mode button and select Insert Mode

- [ ]

1. Select the project in the Project window of the Visual Basic Editor
2. Click the Toolbox button and select UserForm

- [ ]

1. Select the project in the Project window of the Visual Basic Editor
2. Right-click the Run menu and select Customize

- [x]

1. Select the project in the Project window of the Visual Basic Editor
2. Click Insert > UserForm

#### Q31. Explicit variable declaration is required. MyVar is declared at both the module and the procedure level. What is the value of MyVar after first AAA() and then BBB() are run?

```
Dim MyVar As String
Sub AAA()
Dim MyVar As String
MyVar = "Procedure AAA Scope"
End Sub
Sub BBB()
MyVar = "Procedure BBB Scope"
End Sub
```

- [ ] MyVar equals "Procedure AAA Scope"
- [ ] ISNULL(MyVar) is TRUE
- [x] MyVar equals "Procedure BBB Scope"
- [ ] MyVar is NULL

#### Q32. Which code block from class modules returns a compile error?

- [ ]

```
Public Property Get HDL() As Double
HDL = pHDL
End Property
Public Property Let HDL(Value As Double)
pHDL = Value
End Property
```

- [ ]

```
Property Get HDL() As Double
HDL = Value
End Property
Property Let HDL(Value As Double)
pHDL = Value
End Property
```

- [ ]

```
Public Property Get HDL() As Double
HDL = Value
End Property
Public Property Let HDL(Value As Double)
pHDL = Value
End Property
```

- [x]

```
Public Property Get HDL() As Single
HDL = pHDL
End Property
Public Property Let HDL(Value As Double)
pHDL = Value
End Property
```

#### Q33. If VBA code declares FileCount as a constant rather than a variable, the code tends to run faster. Why is this?

- [ ] The scope of constants is limited to the procedure that declares them
- [ ] Constants are declared at compile time, but variables are declared at run time
- [ ] Once declared in a project, the value of a constant cannot be changed. There is no need to look up the current value of FileCount when it is a constant.
- [x] The Const declaraton specifies the most efficient type given the constant's value

#### Q34. A VBA project must declare four classes. How many class modules are needed?

- [ ] two (one for the properties and one for the methods)
- [ ] one (each class is declared in the same module)
- [ ] four (one for each class)
- [x] as many as are required by the variable types that the objects return

#### Q35. What does this code display?

```
Sub MakeErrors()
Dim Y As Variant, Z As Variant
On Error Resume Next
Y = 1 / 0
MsgBox "Y = " & Y
On Error GoTo 0
Z - (0 - 3) ^ 0.5
MsgBox "Z = " & Z
End Sub
```

- [ ] an error message
- [ ] Y and Z
- [x] Z = in a message box and then a subsequent errpr message
- [ ] Y = in a message box and then a subsequent errpr message

#### Q36. The VBA code block shown in the following four options runs when UserForm1's CommandButton1 button is clicked. Which block of code leaves UserFrom1 loaded but not visible until the FoundErrors function has checked it, and then enables processing to continue if no errors are found?

- [ ]

```
Private Sub CommandButton1_Click()
If FoundErrors(Me) Then _
Me.Show
End Sub
```

- [ ]

```
Private Sub CommandButton1_Click()
If Not FoundErrors(UserForm1) Then _
Unload UserForm1
End Sub
```

- [x] <- not sure

```
Private Sub CommandButton1_Click()
Me.Hide
Do While FoundErrors(Me)
Me.Show
Loop
End Sub
```

- [x] <- not sure

```
Private Sub CommandButton1_Click()
Do While FoundErrors(UserForm1)
UserForm1.show
Loop
End Sub
```
