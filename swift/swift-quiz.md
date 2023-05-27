## Swift

#### Q1. What is this code an example of?

```swift
let val = (Double)6
```

- [x] A syntax issue
- [ ] Typecasting
- [ ] Assignment
- [ ] Initialization

Reference: [_The Swift Programming Language: Language Guide: The Basics: Constants and Variables_](https://docs.swift.org/swift-book/LanguageGuide/TheBasics.html#ID310)

#### Q2. What is the error in this code?

```swift
let x = 5
guard x == 5 { return }
```

- [x] The `guard` is missing the `else`
- [ ] Nothing is wrong
- [ ] The `guard` is missing a `then`
- [ ] The comparison is wrong

Reference: [_The Swift Programming Language: Language Guide: Control Flow: Early Exit_](https://docs.swift.org/swift-book/LanguageGuide/ControlFlow.html#ID525)

#### Q3. What is the raw/underlying type of this enum?

```swift
enum Direction {
  case north, south, east, west
}
```

- [x] There is none
- [ ] `String`
- [ ] `Any`
- [ ] `Int`

Reference: [_The Swift Programming Language: Language Guide: Enumerations: Raw Values_](https://docs.swift.org/swift-book/LanguageGuide/Enumerations.html#ID149)

#### Q4. Why is dispatchGroup used in certain situations?

- [ ] It allows multiple synchronous or asynchronous operations to run on different queues.
- [ ] It allows track and control execution of multiple operations together.
- [ ] It allows operations to wait for each other as desired.
- [x] All of these answers.

Reference: [Apple Developer: Documentation: Dispatch: Dispatch Group](https://developer.apple.com/documentation/dispatch/dispatchgroup)

#### Q5. What is this code an example of?

```swift
let val = 5
print("value is: \(val)")
```

- [x] String interpolation
- [ ] String compilation
- [ ] Method chaining
- [ ] String concatenation

Reference: [_The Swift Programming Language: Language Guide: Strings and Characters: String Interpolation_](https://docs.swift.org/swift-book/LanguageGuide/StringsAndCharacters.html#ID292)

#### Q6. What are the contents of `vals` after this code is executed?

```swift
var vals = [10, 2]
vals.sort { (s1, s2) -> Bool in
  s1 > s2
}
```

- [x] `[10, 2]`
- [ ] `[2, 10]`
- [ ] `nil`
- [ ] This code contains an error

Reference: [Apple Developer: Documentations: Swift: Array: sort()](<https://developer.apple.com/documentation/swift/array/sort()>)

#### Q7. What does this code print?

```swift
typealias Thing = [String: Any]
var stuff: Thing
print(type(of: stuff))
```

- [x] `Dictionary<String, Any>`
- [ ] `Dictionary`
- [ ] `Error`
- [ ] `Thing`

Reference: [_The Swift Programming Language: Language Reference: Types: Type Identifier_](https://docs.swift.org/swift-book/ReferenceManual/Types.html#ID447)

#### Q8. What is the value of y?

```swift
let x = ["1", "2"].dropFirst()
let y = x[0]
```

- [x] This code contains an error
- [ ] `1`
- [ ] `2`
- [ ] `nil`

Reference: [Apple Developer: Documentation: Swift: Array: dropFirst(\_:)](<https://developer.apple.com/documentation/swift/array/dropfirst(_:)>)

#### Q9. What is the value of test in this code?

```swift
var test = 1 == 1
```

- [x] `true`
- [ ] `YES`
- [ ] `1`
- [ ] This code contains an error

Reference: [_The Swift Programming Language: Language Guide: Basic Operators: Comparison Operators_](https://docs.swift.org/swift-book/LanguageGuide/BasicOperators.html#ID70)

#### Q10. What is the value of y?

```swift
var x: Int?
let y = x ?? 5
```

- [x] `5`
- [ ] `0`
- [ ] `nil`
- [ ] This code contains an error

Reference: [_The Swift Programming Language: Language Guide: Basic Operators: Nil-Coalescing Operators_](https://docs.swift.org/swift-book/LanguageGuide/BasicOperators.html#ID72)

#### Q11. What is the type of this function?

```swift
func add(a: Int, b: Int) -> Int { return a+b }
```

- [ ] `Int`
- [x] `(Int, Int) -> Int`
- [ ] `Int<Optional>`
- [ ] Functions don't have types.

Reference: [_The Swift Programming Language: Language Guide: Functions: Function Types_](https://docs.swift.org/swift-book/LanguageGuide/Functions.html#ID174)

#### Q12. What is the correct way to call this function?

```swift
func myFunc(_ a: Int, b: Int) -> Int {
  return a + b
}
```

- [x] `myFunc(5, b: 6)`
- [ ] `myFunc(5, 6)`
- [ ] `myFunc(a: 5, b: 6)`
- [ ] `myFunc(a, b)`

Reference: [_The Swift Programming Language: Language Guide: Functions: Function Argument Labels and Parameter Names_](https://docs.swift.org/swift-book/LanguageGuide/Functions.html#ID166)

#### Q13. The Codable protocol is **\_**?

- [x] A combination of `Encodable` and `Decodable`
- [ ] Not a true protocol
- [ ] Required of all classes
- [ ] Automatically included in all classes

References:

- [Apple Developer: Documentation: Swift: Swift Standard Library: Encoding, Decoding, and Serialization: Codable](https://developer.apple.com/documentation/swift/codable/)
- [_The Swift Programming Language: Language Guide: Protocols: Protocol Composition_](https://docs.swift.org/swift-book/LanguageGuide/Protocols.html#ID282)

#### Q14. What is the type of value1 in this code?

```swift
let value1 = "\("test".count)"
```

- [x] `String`
- [ ] `Int`
- [ ] `null`
- [ ] `test.count`

Reference: [_The Swift Programming Language: Language Guide: Strings and Characters: String Interpolation_](https://docs.swift.org/swift-book/LanguageGuide/StringsAndCharacters.html#ID292)

#### Q15. When a function takes a closure as a parameter, when do you want to mark is as escaping?

- [x] When it's executed after the function returns
- [ ] When it's scope is undefined
- [ ] When it's lazy loaded
- [ ] All of these answers

Reference: [_The Swift Programming Language: Language Guide: Closures: Escaping Closures_](https://docs.swift.org/swift-book/LanguageGuide/Closures.html#ID546)

#### Q16. What's wrong with this code?

```swift
class Person {
  var name: String
  var address: String
}
```

- [x] Person has no initializers.
- [ ] Person has no base class.
- [ ] `var name` is not formatted correctly.
- [ ] `address` is a keyword.

Reference: [_The Swift Programming Language: Language Guide: Initialization: Class Inheritance and Initialization_](https://docs.swift.org/swift-book/LanguageGuide/Initialization.html#ID216)

#### Q17. What is the value of names after this code is executed?

```swift
let names = ["Bear", "Joe", "Clark"]
names.map { (s) -> String in
  return s.uppercased()
}
```

- [ ] `["BEAR", "JOE", "CLARK"]`
- [ ] `["B", "J", "C"]`
- [x] `["Bear", "Joe", "Clark"]`
- [ ] This code contains an error.

#### Q18. What describes this line of code?

```swift
let val = 5
```

- [x] A constant named val of type `Int`
- [ ] A variable named val of type `item`
- [ ] A constant named val of type `Number`
- [ ] A variable named val of type `Int`

Reference: [_The Swift Programming Language: Language Guide: The Basics: Type Safety and Type Inference_](https://docs.swift.org/swift-book/LanguageGuide/TheBasics.html#ID322)

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

- [x] Extensions can't add properties.
- [ ] Nothing is wrong with it.
- [ ] `didSet` takes a parameter.
- [ ] `c` is not a character.

Reference: [_The Swift Programming Language: Language Guide: Extensions: Computed Properties_](https://docs.swift.org/swift-book/LanguageGuide/Extensions.html#ID152)

#### Q20. didSet and willSet are examples of **\_**?

- [x] Property observers
- [ ] Key properties
- [ ] All of these answers
- [ ] `newOld` value calls

Reference: [_The Swift Programming Language: Language Guide: Properties_](https://docs.swift.org/swift-book/LanguageGuide/Properties.html#ID262)

#### Q21. What is wrong with this code?

```swift
self.callback = {
  self.attempts += 1
  self.downloadFailed()
}
```

- [x] Use of `self` inside the closure causes retain cycle.
- [ ] You cannot assign a value to a closure in this manner.
- [ ] You need to define the type of closure explicitly.
- [ ] There is nothing wrong with this code.

Reference: [_The Swift Programming Language: Language Guide: Automatic Reference Counting: Strong Reference Cycles for Closures_](https://docs.swift.org/swift-book/LanguageGuide/AutomaticReferenceCounting.html#ID56)

#### Q22. How many values does vals have after this code is executed?

```swift
var vals = Set<String> = ["4", "5", "6"]
vals.insert("5")
```

- [ ] Three
- [ ] Four
- [ ] Eight
- [x] This code contains an error.

Reference: [_The Swift Programming Language: Language Guide: Collection Types: Sets_](https://docs.swift.org/swift-book/LanguageGuide/CollectionTypes.html#ID484)

#### Q23. How can you avoid a strong reference cycle in a closure?

- [x] Use a capture list to set class instances of `weak` or `unowned`.
- [ ] You can't, there will always be a danger of strong reference cycles inside a closure.
- [ ] Initialize the closure as read-only.
- [ ] Declare the closure variable as `lazy`.

Reference: [_The Swift Programming Language: Language Guide: Automatic Reference Counting_](https://docs.swift.org/swift-book/LanguageGuide/AutomaticReferenceCounting.html#ID56)

#### Q24. What is wrong with this code?

```swift
if let s = String.init("some string") {
  print(s)
}
```

- [x] This `String` initializer does not return an optional.
- [ ] String does not have an initializer that can take a `String`.
- [ ] `=` is not a comparison.
- [ ] Nothing is wrong with this code.

Reference: [_The Swift Programming Language: Language Guide: The Basics: Optionals_](https://docs.swift.org/swift-book/LanguageGuide/TheBasics.html#ID330)

#### Q25. Which code snippet correctly creates a typealias closure?

- [x] `typealias CustomClosure = () -> ()`
- [ ] `typealias CustomClosure { () -> () }`
- [ ] `typealias CustomClosure -> () -> ()`
- [ ] `typealias CustomClosure -> () {}`

Reference: [_The Swift Programming Language: Language Reference: Declarations: Type Alias Declaration_](https://docs.swift.org/swift-book/ReferenceManual/Declarations.html#grammar_typealias-declaration)

#### Q26. How do you reference class members from within a class?

- [x] `self`
- [ ] `instance`
- [ ] `class`
- [ ] `this`

Reference: [_The Swift Programming Language: Language Guide: Methods: Instance Methods_](https://docs.swift.org/swift-book/LanguageGuide/Methods.html#ID235)

#### Q27. All value types in Swift are **\_** under the hood?

- [x] Structs
- [ ] Classes
- [ ] Optionals
- [ ] Generics

Reference: [_The Swift Programming Language: Language Guide: Structures and Classes_](https://docs.swift.org/swift-book/LanguageGuide/ClassesAndStructures.html#ID88)

#### Q28. What is the correct way to add a value to this array?

```swift
var strings = [1, 2, 3]
```

- [x] All of these answers
- [ ] `strings.append(4)`
- [ ] `strings.insert(5, at: 1)`
- [ ] `strings += [5]`

Reference: [_The Swift Programming Language: Language Guide: Collection Types: Arrays_](https://docs.swift.org/swift-book/LanguageGuide/CollectionTypes.html#ID107)

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

References:

- [_The Swift Programming Language: Language Guide: Control Flow: For-in Loops_](https://docs.swift.org/swift-book/LanguageGuide/ControlFlow.html#ID121)
- [_The Swift Programming Language: Language Guide: Basic Operators: Range Operators_](https://docs.swift.org/swift-book/LanguageGuide/BasicOperators.html#ID73)

#### Q30. What can AnyObject represent?

- [x] An instance of any class
- [ ] An instance of function type
- [ ] All of these answers
- [ ] An instance of an optional type

Reference: [_The Swift Programming Language: Language Guide: Type Casting: Type Casting for Any and AnyObject_](https://docs.swift.org/swift-book/LanguageGuide/TypeCasting.html#ID342)

#### Q31. What is the value of t after this code is executed?

```swift
let names = ["Larry", "Sven", "Bear"]
let t = names.enumerated().first().offset
```

- [x] This code does not compile. / This code is invalid.
- [ ] 0
- [ ] 1
- [ ] Larry

References:

- [Apple Developer: Documentation: Swift: Array: enumerated()](<https://developer.apple.com/documentation/swift/array/enumerated()>)
- [Apple Developer: Documentation: Swift: Array](https://developer.apple.com/documentation/swift/array/first)

#### Q32. What is the value of test after this code executes?

```swift
let vt = (name: "ABC", val: 5)
let test = vt.0
```

- [x] `ABC`
- [ ] `0`
- [ ] `5`
- [ ] `name`

References:

- [_The Swift Programming Language: Language Guide: The Basics: Tuples_](https://docs.swift.org/swift-book/LanguageGuide/TheBasics.html#ID329)
- [_The Swift Programming Language: Language Reference: Expressions: Primary Expressions: Tuple Expression_](https://docs.swift.org/swift-book/ReferenceManual/Expressions.html#grammar_tuple-expression)

#### Q33. What is the base class in this code?

```swift
class LSN: MMM {
}
```

- [x] MMM
- [ ] LSN
- [ ] There is no base class.
- [ ] This code is invalid.

Reference: [_The Swift Programming Language: Language Guide: Inheritance: Subclassing_](https://docs.swift.org/swift-book/LanguageGuide/Inheritance.html#ID195)

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

- [x] `About to set userLocation to Work... userLocation updated with new value!`
- [ ] `About to set userLocation to Work... userLocation already set to that value...`
- [ ] `About to set userLocation to Home... userLocation updated to new value!`
- [ ] `Error`

Reference: [_The Swift Programming Language: Language Guide: Properties: Property Observers_](https://docs.swift.org/swift-book/LanguageGuide/Properties.html#ID262)

#### Q35. What must a convenience initializer call?

- [ ] A base class convenience initializer
- [ ] Either a designated or another convenience initializer
- [x] A designated initializer
- [ ] None of these answers

Reference: [_The Swift Programming Language: Language Guide: Initialization: Class Inheritance and Initialization_](https://docs.swift.org/swift-book/LanguageGuide/Initialization.html#ID216)

#### Q36. Which object allows you access to specify that a block of code runs in a background thread?

- [ ] DispatchQueue.visible
- [x] DispatchQueue.global
- [ ] errorExample need to be labeled as `throws`.
- [ ] DispatchQueue.background

Reference: [Apple Developer: Documentation: Dispatch: DispatchQueue](https://developer.apple.com/documentation/dispatch/dispatchqueue/2300077-global)

#### Q37. What is the inferred type of x?

```swift
let x = ["a", "b", "c"]
```

- [ ] `String[]`
- [x] `Array<String>`
- [ ] `Set<String>`
- [ ] `Array<Character>`

Reference: [_The Swift Programming Language: Language Guide: Collection Types: Arrays_](https://docs.swift.org/swift-book/LanguageGuide/CollectionTypes.html#ID107)

#### Q38. What is the value of `oThings` after this code is executed?

```swift
let nThings: [Any] = [1, "2", "three"]
let oThings = nThings.reduce("") { "\($0)\($1)" }
```

- [ ] 11212three
- [ ] 115
- [x] 12three
- [ ] Nothing, this code is invalid.

Reference: [Apple Developer: Documentation: Swift: Array: reduce(\_:\_:)](<https://developer.apple.com/documentation/swift/array/reduce(_:_:)>)

#### Q39. How would you call a function that throws errors and also returns a value?

- [ ] `!try`
- [x] `try?`
- [ ] `try!`
- [ ] `?try`

Reference: [_The Swift Programming Language: Language Guide: Error Handling: Handling Errors_](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html#ID512)

#### Q40. What is wrong with this code?

```swift
protocol TUI {
  func add(x1: Int, x2: Int) -> Int {
    return x1 + x2
  }
}
```

- [ ] Protocol functions cannot have return types.
- [x] Protocol functions cannot have implementations.
- [ ] Nothing is wrong with it.
- [ ] `add` is a reserved keyword.

Reference:

- [_The Swift Programming Language: Language Guide: Protocols: Method Requirements_](https://docs.swift.org/swift-book/LanguageGuide/Protocols.html#ID270)
- [_The Swift Programming Language: Language Guide: Protocols: Protocol Extensions_](https://docs.swift.org/swift-book/LanguageGuide/Protocols.html#ID521)

#### Q41. In this code, what are `wheels` and `doors` examples of?

```swift
class Car {
  var wheels: Int = 4
  let doors = 4
}
```

- [ ] Class members
- [ ] This code is invalid
- [ ] Class fields
- [x] Class properties

Reference:

- [_The Swift Programming Language: Language Guide: Structures and Classes_](https://docs.swift.org/swift-book/LanguageGuide/ClassesAndStructures.html)
- [_The Swift Programming Language: Language Guide_](https://docs.swift.org/swift-book/LanguageGuide/Properties.html#ID255)

#### Q42. How do you designated a failable initializer?

- [ ] You cannot
- [ ] `deinit`
- [x] `init?`
- [ ] `init`

Reference:

- [_The Swift Programming Language: Language Guide: Initialization_](https://docs.swift.org/swift-book/LanguageGuide/Initialization.html#ID224)
- [_The Swift Programming Language: Language Guide: Deinitialization_](https://docs.swift.org/swift-book/LanguageGuide/Deinitialization.html)

#### Q43. What is printed when this code is executed?

```swift
let dbl = Double.init("5a")
print(dbl ?? ".asString()")
```

- [ ] `five`
- [ ] `5a`
- [x] `.asString()`
- [ ] `5`

Reference:

- [_The Swift Programming Language: Language Guide: Basic Operators: Nil-Coalescing Operator_](https://docs.swift.org/swift-book/LanguageGuide/BasicOperators.html#ID72)
- [_The Swift Programming Language: Language Guide: Initialization: Failable Initializers_](https://docs.swift.org/swift-book/LanguageGuide/Initialization.html#ID224)

#### Q44. In the function below, what are `this` and `toThat` examples of?

```swift
func add(this x: Int, toThat y: Int) { }
```

- [ ] None of these answers
- [ ] Local terms
- [x] Argument labels
- [ ] Parameters names

Reference: [_The Swift Programming Language: Language Guide: Functions_](https://docs.swift.org/swift-book/LanguageGuide/Functions.html#ID166)

#### Q45. What is wrong with this code?

```swift
for (key, value) in [1: "one", 2: "two"] {
  print(key, value)
}
```

- [ ] The interaction source is invalid
- [ ] The interaction variable is invalid
- [x] There is nothing wrong with this code
- [ ] The comma in the print is misplaced

Reference: [_The Swift Programming Language: Language Guide: Control Flow: For-In Loops_](https://docs.swift.org/swift-book/LanguageGuide/ControlFlow.html#ID121)

#### Q46. Which of these choices is associated with unit testing?

- [ ] `XCTest`
- [x] All of these answers
- [ ] `@testable`
- [ ] `XCTAssert`

Reference:

- [Apple Developer: Documentation: XCTest: XCTest](https://developer.apple.com/documentation/xctest/xctest)
- [Apple Developer: Documentation: XCTest: Boolean Assertions: XCTAssert(\_:\_:file:line:)](https://developer.apple.com/documentation/xctest/1500669-xctassert)
- [_The Swift Programming Language: Language Guide: Access Control: Access Levels_](https://docs.swift.org/swift-book/LanguageGuide/AccessControl.html#ID5)

#### Q47. In the code below, what is width an example of?

```swift
class Square {
  var height: Int = 0
  var width: Int {
    return height
  }
}
```

- [ ] This code contains error
- [ ] A closure
- [x] A computed property
- [ ] Lazy loading

Reference:

- [_The Swift Programming Language: Language Guide: Properties: Stored Properties_](https://docs.swift.org/swift-book/LanguageGuide/Properties.html#ID255)
- [_The Swift Programming Language: Language Guide: Properties: Computed Properties_](https://docs.swift.org/swift-book/LanguageGuide/Properties.html#ID259)
- [_The Swift Programming Language: Language Guide: Closures: Trailing Closures_](https://docs.swift.org/swift-book/LanguageGuide/Closures.html#ID102)

#### Q48. What data type is this an example of?

```swift
let vals = ("val", 1)
```

- [ ] A dictionary
- [x] A tuple
- [ ] An optional
- [ ] This code contains error

Reference:

- [_The Swift Programming Language: Language Guide: The Basics_](https://docs.swift.org/swift-book/LanguageGuide/TheBasics.html#ID329)
- [_The Swift Programming Language: Language Reference: Types_](https://docs.swift.org/swift-book/ReferenceManual/Types.html#grammar_tuple-type)

#### Q49. What is wrong with this code?

```swift
var x = 5
x = 10.0
```

- [x] You cannot assign a Double to a variable of type Int
- [ ] `x` is undefined
- [ ] `x` is a constant
- [ ] `x` has no type

Reference: [_The Swift Programming Language: Language Guide: The Basics_](https://docs.swift.org/swift-book/LanguageGuide/TheBasics.html#ID322)

#### Q50. What will this code print to the console?

```swift
var items = ["a": 1, "b": 2, "c": "test"] as [String: Any]
items["c"] = nil
print(items["c"] as Any)
```

- [ ] Any
- [ ] test
- [ ] 1,2,3
- [x] nil

References:

- [_The Swift Programming Language: Language Guide: Type Casting: Type Casting for Any and AnyObject_](https://docs.swift.org/swift-book/LanguageGuide/TypeCasting.html#ID342)
- [_The Swift Programming Language: Language Guide: Collection Types: Dictionaries_](https://docs.swift.org/swift-book/LanguageGuide/CollectionTypes.html#ID113)

#### Q51. What is wrong with this code?

```swift
let val = 5.0 + 10
```

- [x] There is nothing wrong with this code
- [ ] `val` is a constant and cannot be changed
- [ ] `5.0` and `10` are different types
- [ ] There is no semicolon

Reference: [_The Swift Programming Language: Language Guide: The Basics: Type Safety and Type Inference_](https://docs.swift.org/swift-book/LanguageGuide/TheBasics.html#ID322)

#### Q52. How many parameters does the initializer for Test have?

```swift
struct Test {
  var score: Int
  var date: Date
}
```

- [ ] Zero
- [ ] This code contains an error
- [x] Two
- [ ] Structs do not have initializers

Reference: [_The Swift Programming Language: Language Guide: Initialization_](https://docs.swift.org/swift-book/LanguageGuide/Initialization.html#ID213)

#### Q53. What prints to the console when executing this code?

```swift
let x = try? String.init("test")
print(x)
```

- [ ] nil
- [ ] Nothing - this code contains an error
- [x] Optional("test")
- [ ] test

References:

- [_The Swift Programming Language: Language Guide: Error Handling: Handling Errors_](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html#ID512)
- [_The Swift Programming Language: Language Guide: The Basics: Optionals_](https://docs.swift.org/swift-book/LanguageGuide/TheBasics.html#ID330)

#### Q54. How can you sort this array?

```swift
var vals = [1, 2, 3]
```

- [ ] `vals.sort { $0 < $1 }`
- [ ] `vals.sort { (s1, s2) in s1 < s2 }`
- [ ] `vals.sort(by: <)`
- [x] All of these answers

Reference: [Apple Developer: Documentation: Swift: Array: sort()](<https://developer.apple.com/documentation/swift/array/sort()>)

#### Q55. DispatchQueue.main.async takes a block that will be

- [ ] Not executed
- [x] Executed in the main queue
- [ ] None of these answers
- [ ] Executed on the background thread

Reference: [Apple Developer: Documentation: Dispatch: DispatchQueue: async(group:qos:flags:execute:)](https://developer.apple.com/documentation/dispatch/dispatchqueue/2016098-async)

#### Q56. When is deinit called?

- [ ] When a class instance needs memory
- [ ] All of these answers
- [ ] When the executable code is finished
- [x] When a class instance is being removed from memory

Reference: [_The Swift Programming Language: Language Guide: Deinitialization_](https://docs.swift.org/swift-book/LanguageGuide/Deinitialization.html)

#### Q57. How do you declare an optional String?

- [x] `String?`
- [ ] `Optional[String]`
- [ ] `[String]?`
- [ ] `?String`

Reference: [_The Swift Programming Language: Language Guide: The Basics: Optionals_](https://docs.swift.org/swift-book/LanguageGuide/TheBasics.html#ID330)

#### Q58. How many times this code will be executed? / How many times will this loop be performed?

```swift
for i in ["0", "1"] {
  print(i)
}
```

- [ ] One
- [x] Two
- [ ] Three
- [ ] This code does not compile

Reference: [_The Swift Programming Language: Language Guide: Control Flow: For-In Loops_](https://docs.swift.org/swift-book/LanguageGuide/ControlFlow.html#ID121)

#### Q59. What does this code print?

```swift
let names = ["Bear", "Tony", "Svante"]
print(names[1] + "Bear")
```

- [ ] 1Bear
- [ ] BearBear
- [x] TonyBear
- [ ] Nothing, this code is invalid

References:

- [_The Swift Programming Language: Language Guide: Collection Types: Arrays_](https://docs.swift.org/swift-book/LanguageGuide/CollectionTypes.html#ID107)
- [_The Swift Programming Language: Language Guide: Strings and Characters: Concatenating Strings and Characters_](https://docs.swift.org/swift-book/LanguageGuide/StringsAndCharacters.html#ID291)

#### Q60. What is true of this code?

```swift
let name: String?
```

- [ ] `name` can hold only a string value.
- [x] `name` can hold either a string or nil value.
- [ ] Optional values cannot be `let` constants.
- [ ] Only non-empty string variables can be stored in `name`.

Reference: [_The Swift Programming Language: Language Guide: The Basics: Optionals_](https://docs.swift.org/swift-book/LanguageGuide/TheBasics.html#ID330)

#### Q61. What is the value of `val` after this code is executed?

```swift
let i = 5
let val = i * 6.0
```

- [x] This code is invalid.
- [ ] 6
- [ ] 30
- [ ] 0

Reference: [_The Swift Programming Language: Language Guide: The Basics: Type Safety and Type Inference_](https://docs.swift.org/swift-book/LanguageGuide/TheBasics.html#ID322)

#### Q62. What does this code print?

```swift
enum Positions: Int {
  case first, second, third, other
}

print (Positions.other.rawValue)
```

- [x] 3
- [ ] 0
- [ ] other
- [ ] nil

Reference: [_The Swift Programming Language: Language Guide: The Basics: Raw Values_](https://docs.swift.org/swift-book/LanguageGuide/Enumerations.html#ID149)

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

References:

- [_The Swift Programming Language: Language Guide: Strings and Characters: Working with Characters_](https://docs.swift.org/swift-book/LanguageGuide/StringsAndCharacters.html#ID290)
- [Apple Developer: Documentation: Swift: String: forEach(\_:)](<https://developer.apple.com/documentation/swift/string/foreach(_:)>)

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

References:

- [Apple Developer: Documentation: Swift: Swift Standard Library: Collections: Sequence and Collection Protocols: Sequence: filter()](<https://developer.apple.com/documentation/swift/sequence/filter(_:)>)
- [Apple Developer: Documentation: Swift: Array: sorted()](<https://developer.apple.com/documentation/swift/array/sorted()>)

#### Q65. What enumeration feature allows them to store case-specific data?

- [x] Associated values
- [ ] Integral values
- [ ] Raw values
- [ ] Custom values

Reference: [_The Swift Programming Language: Language Guide: Enumerations: Associated Values_](https://docs.swift.org/swift-book/LanguageGuide/Enumerations.html#ID148)

#### Q66. In the code below, AOM must be a(n)?

```swift
class AmP: MMM, AOM { }
```

- [ ] Class
- [x] Protocol
- [ ] Enumeration
- [ ] Struct

References:

- [_The Swift Programming Language: Language Guide: Inheritance: Subclassing_](https://docs.swift.org/swift-book/LanguageGuide/Inheritance.html#ID195)
- [_The Swift Programming Language: Language Guide: Protocols: Protocol Syntax_](https://docs.swift.org/swift-book/LanguageGuide/Protocols.html#ID268)

#### Q67. What is the value of numbers in the code below?

```swift
let numbers = [1, 2, 3, 4, 5, 6].filter { $0 % 2 == 0 }
```

- [ ] [1, 3, 5]
- [ ] []
- [x] [2, 4, 6]
- [ ] nil

Reference: [Apple Developer: Documentation: Swift: Swift Standard Library: Collections: Sequence and Collection Protocols: Sequence: filter()](<https://developer.apple.com/documentation/swift/sequence/filter(_:)>)

#### Q68. What is the type of `vals` in this code?

```swift
let vals = ["a", 1, "Hi"]
```

- [ ] Array(char)
- [x] [Any]
- [ ] Array<char>
- [ ] [Generic]

Reference: [_The Swift Programming Language: Language Guide: Type Casting_](https://docs.swift.org/swift-book/LanguageGuide/TypeCasting.html#ID342)

#### Q69. How can you extract val to `x` in tuple `vt`

```swift
let vt = (name: "ABC", val: 5)
```

- [ ] let x = vt.1
- [x] All of these answers
- [ ] let x = vt.val
- [ ] let (`_`, x) = vt

Reference: [_The Swift Programming Language: Language Guide: The Basics: Tuples_](https://docs.swift.org/swift-book/LanguageGuide/TheBasics.html#ID329)

#### Q70. What is the type of x?

```swift
let x = try? String.init(from: decoder)
```

- [ ] String
- [x] String?
- [ ] String!
- [ ] try?

Reference: [_The Swift Programming Language: Language Guide: Error Handling: Handling Errors_](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html#ID512)

#### Q71. How many times is this loop executed?

```swift
let loopx = 5
repeat {
  print (loopx)
} while loopx < 6
```

- [ ] Six
- [ ] Zero
- [ ] Five
- [x] Infinite

Reference: [_The Swift Programming Language: Language Guide: Control Flow: While Loops_](https://docs.swift.org/swift-book/LanguageGuide/ControlFlow.html#ID124)

#### Q72. How many values does vals have after this code is executed?

```swift
var vals: Set<String> = ["4", "5", "6"]
vals.insert("5")
```

- [ ] This code contains an error.
- [ ] Eight
- [x] Three
- [ ] Four

Reference: [_The Swift Programming Language: Language Guide: Collection Types: Sets_](https://docs.swift.org/swift-book/LanguageGuide/CollectionTypes.html#ID484)
