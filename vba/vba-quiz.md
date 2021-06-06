## Visual Basic for Applications (VBA)

#### Q1. Which two sets of values are printed by this function and sub?
```
Function GetVitals(ID As Long, Age As Long, ptional Weight As Long) As String
    GetVitals="ID=" & ID &"Age=" & Age & "Weight=" & Weight
End Function
Sub ShowVitals()
    Dim ID As Long, Age As Long,Weight as Long
    Debug.Print GetVitals(ID:=5,Age:=20)
    Debug.Print GetVitals(ID:=6,Age:=25,Weight:=130
End Sub
```
- [ ] id=5 Age = 20 Weight= ID=6 Age = 25 Weight=130
- [ ] id=5 Age = 20 Weight=0 ID=6 Age = 25 Weight=130
- [ ] id=5 Age = 20 Weight=Null ID=6 Age = 25 Weight=130
- [ ] id=5 Age = 20 ID=6 Age = 25 Weight=130

#### Q2. This code shows the first statement of CalledSub. Which calling statement will work properly?
`Sub CalledSub(Surname, Age)`
- [ ] call Calledsub "smith",26
- [ ] calledsub (surname="smith", Age = 26)
- [ ] calledsub (Surname:="Smith", Age:=26)
- [ ] calledsub "smith", 26

#### Q3. What is the principal difference between a class and an object?
- [ ] There is no meaningful difference. The terms are used interchangeably.
- [ ] A dass declares an object's properties. An object completes the declaration by defining events and methods.
- [ ] An object is a template for a class.
- [X] A class describes the design of an object. An object is an instance of that design.

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
- [ ] 3
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
- [ ] ListBox

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
- [ ] 10 rows and 1 column
- [ ] 10 rows and 0 columns
- [ ] 1 row and 10 columns

#### Q11. Which cell is selected if you run this code?
`Range("E3:312").Range("B3").Select`
- [ ] F5
- [X] F3
- [ ] B3
- [ ] E3
#### Q12. Which variable name is valid in VBA?
- [x] _MyVar
- [ ] My_Var
- [ ] My-Var
- [ ] 1MyVar
  
[Reference link](https://docs.microsoft.com/en-us/office/vba/language/concepts/getting-started/visual-basic-naming-rules)
```
Use the following rules when you name procedures, constants, variables, and arguments in a Visual Basic module:
You must use a letter as the first character.
You can't use a space, period (.), exclamation mark (!), or the characters @, &, $, # in the name.
Name can't exceed 255 characters in length.
```
