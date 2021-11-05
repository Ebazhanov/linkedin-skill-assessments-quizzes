## Swift

#### Q1. What is this code an example of?

```swift
let val = (Double)6
```

- [x] a syntax issue
- [ ] typecasting
- [ ] assignment
- [ ] initialization

#### Q2. What is the error in this code?

```swift
let x = 5
guard x == 5 { return }
```

- [x] The guard is missing the else.
- [ ] Nothing is wrong.
- [ ] The guard is missing a then.
- [ ] The comparison is wrong.

#### Q3. What is the raw/underlying type of this enum?

```swift
enum Direction {
  case north, south, east, west
}
```

- [x] There is none.
- [ ] String
- [ ] Any
- [ ] Int

#### Q4. Why is dispatchGroup used in certain situations?

- [ ] It allows multiple synchronous or asynchronous operations to run on different queues.
- [ ] It allows track and control execution of multiple operations together.
- [ ] It allows operations to wait for each other as desired.
- [x] all of these answers.

#### Q5. What is this code an example of?

```swift
let val = 5
print("value is: \(val)")
```

- [x] string interpolation
- [ ] string compilation
- [ ] method chaining
- [ ] string concatenation

#### Q6. What are the contents of `vals` after this code is executed?

```swift
var vals = [10, 2]
vals.sort { (s1, s2) -> Bool in
  s1 > s2
}
```

- [x] [10, 2]
- [ ] [2, 10]
- [ ] nil
- [ ] This code contains an error

#### Q7. What does this code print?

```swift
typealias Thing = [String:Any]
var stuff: Thing
print(type(of: stuff))
```

- [x] Dictionary<String, Any>
- [ ] Dictionary
- [ ] ERROR
- [ ] Thing

#### Q8. What is the value of y?

```swift
let x = ["1", "2"].dropFirst()
let y = x[0]
```

- [x] This code contains an error
- [ ] 1
- [ ] 2
- [ ] nil

#### Q9. What is the value of test in this code?

```swift
var test = 1 == 1
```

- [x] TRUE
- [ ] YES
- [ ] 1
- [ ] This code contains an error

#### Q10. What is the value of y?

```swift
var x: Int?
let y = x ?? 5
```

- [x] 5
- [ ] 0
- [ ] nil
- [ ] This code contains an error

#### Q11. What is the type of this function?

```swift
func add(a: Int, b: Int) -> Int { return a+b }
```

- [ ] Int
- [x] (Int, Int) -> Int
- [ ] Int<Optional>
- [ ] Functions don't have types.

#### Q12. What is the correct way to call this function?

```swift
func myFunc(_ a: Int, b: Int) -> Int {
  return a + b
}
```

- [x] myFunc(5, b: 6)
- [ ] myFunc(5, 6)
- [ ] myFunc(a: 5, b: 6)
- [ ] myFunc(a, b)

#### Q13. The Codable protocol is **\_**?

- [x] a combination of Encodable and Decodable
- [ ] not a true protocol <<<<---Possibly correct as it's a typealias of Encodable and Decodable
- [ ] required of all classes
- [ ] automatically included in all classes

#### Q14. What is the type of value1 in this code?

```swift
let value1 = "\("test".count)"
```

- [x] String
- [ ] Int
- [ ] null
- [ ] test.count

#### Q15. When a function takes a closure as a parameter, when do you want to mark is as escaping?

- [x] when it's executed after the function returns
- [ ] when it's scope is undefined
- [ ] when is's lazy loaded
- [ ] all of these answers

#### Q16. What's wrong with this code?

```swift
class Person {
  var name: String
  var address: String
}
```

- [x] Person has no initializers.
- [ ] Person has no base class.
- [ ] var name is not formatted corrrectly.
- [ ] address is a keyword.

#### Q17. What is the value of names after this code is executed?

```swift
let names = ["Bear", "Joe", "Clark"]
names.map { (s) -> String in
  return s.uppercased()
}
```

- [ ] ["BEAR", "JOE", "CLARK"]
- [ ] ["B", "J", "C"]
- [x] ["Bear", "Joe", "Clark"]
- [ ] This code contains an error.

#### Q18. What describes this line of code?

```swift
let val = 5
```

- [x] a constant named val of type Int
- [ ] a variable named val of type item
- [ ] a constant named val of type Number
- [ ] a variable named val of type Int

#### Q19. What is the error in this code?

```swift
extension String {
  var firstLetter: Character = "c" {
    didSet {
      print("new value")
    }
  }
}
```

- [x] Extensions can't add properties. // although extensions technically can't contain stored properties
- [ ] Nothing is wrong with it.
- [ ] didSet takes a parameter.
- [ ] c is not a character.

#### Q20. didSet and willSet are examples of **\_**?

- [x] property observers
- [ ] key properties
- [ ] all of these answers
- [ ] newOld value calls

#### Q21. What is wrong with this code?

```swift
self.callback = {
  self.attempts += 1
  self.downloadFailed()
}
```

- [x] Use of self inside the closure causes retain cycle.
- [ ] You cannot assign a value to closure in this manner.
- [ ] You need to define the type of closure explicitly.
- [ ] There is nothing wrong with this code.

#### Q22. How many values does vals have after this code is executed?

```swift
var vals = Set<String> = ["4", "5", "6"]
vals.insert("5")
```

- [x] three
- [ ] four
- [ ] eight
- [ ] This code contains an error.

#### Q23. How can you avoid a strong reference cycle in a closure?

- [x] Use a capture list to set class instances of weak or unowned.
- [ ] You can't, there will always be a danger of strong reference cycles inside a closure.
- [ ] Initialize the closure as read-only.
- [ ] Declare the closure variable as lazy.

#### Q24. What is wrong with this code?

```swift
if let s = String.init("some string") {
  print(s)
}
```

- [x] This String initializer does not return an optional.
- [ ] String does not have an initializer that can take a String.
- [ ] = is not a comparison.
- [ ] Nothing is wrong with this code.

#### Q25. Which code snippet correctly creates a typealias closure?

- [x] typealias CustomClosure: () -> ()
- [ ] typealias CustomClosure { () -> () }
- [ ] typealias CustomClosure -> () -> ()
- [ ] typealias CustomClosure -> () {}

#### Q26. How do you reference class members from within a class?

- [x] self
- [ ] instance
- [ ] class
- [ ] this

#### Q27. All value types in Swift are **\_** under the hood?

- [x] structs
- [ ] classes
- [ ] optionals
- [ ] generics

#### Q28. What is the correct way to add a value to this array?

```swift
var strings = [1, 2, 3]
```

- [x] all of these answers
- [ ] strings.append(4)
- [ ] strings.insert(5, at: 1)
- [ ] strings += [5]

#### Q29. How many times will this loop be executed?

```swift
for i in 0...100 {
  print(i)
}
```

- [ ] 0
- [x] 101
- [ ] 99
- [ ] 100

#### Q30. What can AnyObject represent?

- [ ] an instance of any class
- [ ] an instance of function type
- [x] all of these answers
- [ ] an instance of an optional type

#### Q31. What does this code print?

```swift
typealias Thing = [String:Any]
var stuff : Thing
print(type(of:stuff))
```

- [ ] Dictionary
- [ ] ERROR
- [ ] Thing
- [x] Dictionary<String, Any>

#### Q32. What is the value of t after this code is executed?

```swift
let names = ["Larry", "Sven", "Bear"]
let t = names.enumerated().first().offset
```

- [x] This code is invalid.
- [x] This code does not compile.
- [ ] 0
- [ ] 1
- [ ] Larry

#### Q32. What is the value of test after this code executes?

```swift
let vt = (name: "ABC", val: 5)
let test = vt.0
```

- [x] ABC
- [ ] 0
- [ ] 5
- [ ] name

#### Q33. What is the base class in this code?

```swift
class LSN : MMM {
}
```

- [x] MMM
- [ ] LSN
- [ ] There is no base class.
- [ ] This code is invalid.

#### Q34. What does this code print to the console?

```swift
var userLocation: String = "Home" {
  willSet(newValue) {
  print("About to set userLocation to \(newValue)...")
  }

  didSet {
  if userLocation != oldValue {
  print("userLocation updated with new value!")
  } else {
  print("userLocation already set to that value...")
  }
  }
 }

 userLocation = "Work"
```

- [x] About to set userLocation to Work… userLocation updated with new value!
- [ ] About to set userLocation to Work… userLocation already set to that value…
- [ ] About to set userLocation to Home… userLocation updated to new value!
- [ ] ERROR

#### Q35. What must a convenience initializer call?

- [ ] a base class convenience initializer
- [ ] either a designated or another convenience initializer
- [x] a designated initializer
- [ ] none of these answers

#### Q36. Which object allows you access to specify that a block of code runs in a background thread?

- [ ] DispatchQueue.visible
- [x] DispatchQueue.global
- [ ] errorExample need to be labeled as `throws`.
- [ ] DispatchQueue.background

#### Q37. What is the inferred type of x?

```swift
let x = ["a", "b", "c"]
```

- [ ] `String[]`
- [x] `Array<String>`
- [ ] `Set<String>`
- [ ] `Array<Character>`

#### Q38. What is the value of `oThings` after this code is executed?

```swift
let nThings: [Any] = [1, "2", "three"]
let oThings = nThings.reduce("") { "\($0)\($1)" }
```

- [ ] 11212three
- [ ] 115
- [x] 12three
- [ ] Nothing, this code is invalid.

#### Q39. How would you call a function that throws errors and also returns a value?

- [ ] `!try`
- [x] `try?`
- [ ] `try!`
- [ ] `?try`

#### Q40. What is wrong with this code?

```swift
protocol TUI {
  func add(x1 : Int, x2 : Int) -> Int {
    return x1 + x2
  }
}
```

- [ ] Protocol functions cannot have return types.
- [x] Protocol functions cannot have implementations.
- [ ] Nothing is wrong with it.
- [ ] `add` is a reserved keyword.

#### Q41. In this code, what are `wheels` and `doors` examples of?

```swift
class Car {
  var wheels: Int = 4
  let doors = 4
}
```

- [ ] class members
- [ ] This code is invalid.
- [ ] class fields
- [x] class properties

#### Q42. How do you designated a failable initializer?

- [ ] You cannot
- [ ] deinit
- [x] `init?`
- [ ] init

#### Q43. What is printed when this code is executed?

```swift
let dbl = Double.init("5a")
print(dbl ?? ".asString()")
```

- [ ] five
- [ ] 5a
- [x] `.asString()`
- [ ] 5

#### Q44. In the function below, what are `this` and `toThat` examples of?

```swift
func add(this x: Int, toThat y: Int)->{}
```

- [ ] none of these answers
- [ ] local terms
- [x] argument labels
- [ ] parameters names

#### Q45. What is wrong with this code?

```swift
for (key, value) in [1: "one", 2: "two"]{
  print(key, value)
}
```

- [ ] The interaction source is invalid
- [ ] The interaction variable is invalid
- [x] There is nothing wrong with this code
- [ ] The comma in the print is misplaced

#### Q46. Which of these choices is associated with unit testing?

- [ ] XCTest
- [x] all of these answers
- [ ] @testable
- [ ] XCAssert

#### Q47. In the code below, what is width an example of?

```swift
class Square{
  var height: Int = 0
  var width : Int {
    return height
  }
}
```

- [ ] This code contains error
- [ ] a closure
- [x] a computed property
- [ ] lazy loading

#### Q48. What data type is this an example of?

```swift
let vals = ("val", 1)
```

- [ ] a dictionary
- [x] a tuple
- [ ] an optional
- [ ] This code contains error

#### Q49. What is wrong with this code?

```swift
var x = 5
x = 10.0
```

- [x] You cannot assign a Double to a variable of type Int
- [ ] x is undefined
- [ ] x is a constant
- [ ] x has no type

#### Q50. What will this code print to the console?

```swift
var items = ["a":1, "b":2, "c":"test"] as [String: Any]
items["c"] = nil
print(items["c"] as Any)
```

- [ ] Any
- [ ] test
- [ ] 1,2,3
- [x] nil

#### Q51. What is wrong with this code?

```swift
let val = 5.0 + 10
```

- [x] There is nothing wrong with this code
- [ ] val is a constant and cannot be changed
- [ ] 5.0 and 10 are different types
- [ ] There is no semicolon

#### Q52. How many parameters does the initializer for Test have?

```swift
struct Test{
  var score: Int
  var date: Date
}
```

- [ ] zero
- [ ] This code contains an error
- [x] two
- [ ] Structs do not have initializers

#### Q53. What prints to the console when executing this code?

```swift
let x = try? String.init("test")
print(x)
```

- [ ] nil
- [ ] Nothing - this code contains an error
- [x] Optional("test")
- [ ] test

#### Q54. How can you sort this array?

```swift
var vals = [1,2,3]
```

- [ ] `vals.sort { $0 < $1 }`
- [ ] `vals.sort { (s1, s2) in s1 < s2 }`
- [ ] `vals.sort(by: <)`
- [x] all of these answers

#### Q55. DispatchQueue.main.async takes a block that will be

- [ ] not executed
- [x] executed in the main queue
- [ ] none of these answers
- [ ] executed on the background thread

#### Q56. When is deinit called?

- [ ] When a class instance needs memory
- [x] All of these answers
- [ ] When the executable code is finished
- [ ] When a class instance is being removed from memory

#### Q57. How do you declare an optional String?

- [x] String?
- [ ] Optional[String]
- [ ] [String]?
- [ ] ?String

#### Q58. How many times this code will be executed? —OR— How many times will this loop be performed?

```swift
for i in ["0", "1"]{
  print(i)
}
```

- [ ] one
- [x] two
- [ ] three
- [ ] This code does not compile

#### Q59. What does this code print?

```swift
let names = ["Bear", "Tony", "Svante"]
print(names[1]+"Bear")
```

- [ ] 1Bear
- [ ] BearBear
- [x] TonyBear
- [ ] Nothing, this code is invalid

#### Q60. What is true of this code?

```swift
let name: String?
```

- [ ] name can hold only a string value.
- [x] name can hold either a string or nil value.
- [ ] Optional values cannot be `let` constants.
- [ ] Only non-empty string variables can be stored in name.

#### Q61. What is the value of `val` after this code is executed?

```swift
let i = 5
let val = i * 6.0
```

- [x] This code is invalid.
- [ ] 6
- [ ] 30
- [ ] 0

#### Q62. What does this code print?

```swift
enum Positions : Int {
  case first, second, third, other
}
print (Positions.other.rawValue)
```

- [x] 3
- [ ] 0
- [ ] other
- [ ] nil

#### Q63. What is printed to the console when this code is executed?

```swift
"t".forEach { (char) in
    print(char)
}
```

- [ ] nil
- [ ] Nothing, since the code contains an error
- [x] t
- [ ] zero

#### Q64. What prints when this code is executed?

```swift
let s1 = ["1", "2", "3"]
    .filter { $0 > "0" }
    .sorted { $0 > $1 }
print(s1)
```

- [ ] []
- [x] ["3", "2", "1"]
- [ ] [321]
- [ ] ["1", "2", "3"]

#### Q65. What enumeration feature allows them to store case-specific data?

(Question does not make that much sense though. )

- [x] associated values
- [ ] integral values
- [ ] raw values
- [ ] custom values

#### Q66. In the code below, AOM must be a(n)?

```swift
class AmP : MMM, AOM {
  }
```

- [ ] class
- [x] protocol
- [ ] enumeration
- [ ] struct

#### Q67. What is the value of numbers in the code below?

```swift
let numbers = [1,2,3,4,5,6].filter{ $0 % 2 == 0}
```

- [ ] [1,3,5]
- [ ] []
- [x] [2,4,6]
- [ ] nil
