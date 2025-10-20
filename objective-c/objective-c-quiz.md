## Objective-C

#### Q1. What is the value of s?

```
NSMutableString *s = [NSMutableString stringWithString: @"123"];
[s appendString: @"456"];
```

- [x] 123456
- [ ] 123
- [ ] 123
- [ ] 456
- [ ] This code contains an error.

#### Q2. What's the value of i after these statements?

```
NSString *str = nil;
NSInteger i = str.integerValue;
```

- [ ] nil
- [x] 0 (technically `nil` == 0 but i will have a literal value of `0` and not the `void*` value of `nil`)
- [ ] -1
- [ ] This code crashes.

#### Q3. What value is in str after this line in executed?

`NSString str = "test" + " " + "more";`

- [ ] test
- [ ] nil
- [ ] test more
- [x] This code contains an error

#### Q4. What is the output of the code given below?

```
    NSPredicate *p2 = [NSPredicate predicateWithBlock:^BOOL(NSString*  evaluatedObject, NSDictionary<NSString *,id> * _Nullable bindings) {
      return evaluatedObject.intValue % 2 == 0;
    }];
    NSArray *vals = @[@"1", @"2", @"3"];
    NSArray *n2 = [vals filteredArrayUsingPredicate:p2];
    NSLog(@"%@", n2.firstObject);
```

- [x] 2
- [ ] 1,2,3
- [ ] 1,2
- [ ] Nothing, since this code contains an error.

#### Q5. Property defaults include \_?

- [x] atomic/strong
- [ ] atomic/weak
- [ ] nonatomic/weak
- [ ] nonatomic/strong

#### Q6. What is the key difference between NSDictionary and NSMutableDictionary?

- [x] NSMutableDictionary's values can change
- [ ] NSMutableDictionary has not initializers.
- [ ] NSDictionary can't be copied.
- [ ] NSDictionary's values can change.

#### Q7. What is foo?

`-(float)foo;`

- [x] A function with a return type of float.
- [ ] This code contains an error.
- [ ] A variable declaration of type float.
- [ ] A property of type float.

#### Q8. What can you glean from this line?

`#import "NSString+NameHelper.h"`

- [x] NameHelper is a category of NSString.
- [ ] NameHelper is a subclass of NSString.
- [ ] NSString implements the NameHelper protocol.
- [ ] NSString has a helper class.

#### Q9. What's wrong with this code?

`float x = 5.;`

- [x] Nothing is wrong with this code.
- [ ] Declarations do not need semicolons.
- [ ] x=5 is an invalid float.
- [ ] Variables can't be declared and initialized in the same state.

#### Q10. How many times with this loop be executed?

```
for (int x=0; x<100; x++) {
  x = x + 1;
}
```

- [x] 50
- [ ] 99
- [ ] 100
- [ ] This code contains an error.

#### Q11. What is this code an example of?

`[self addObserver: self forKeyPath: @"val" options:0 context: nil];`

- [x] Key-Value Observing
- [ ] Class Value Observing
- [ ] Key-Data Observing
- [ ] KeyPath Observing

#### Q12. What does ARC stand for?

- [x] Automatic Reference Counting
- [ ] Automatic Retain Checking
- [ ] Async Retain Cycles
- [ ] Automatic Release Code

#### Q13. What is printed for this code?

```
int val = 0;
val = 1.5;
printf("%d", val);
```

- [x] 1
- [ ] 2
- [ ] 0
- [ ] This code contains an error.

#### Q14. What best describes class inheritance in Objective-C?

- [x] single inheritance but multiple protocol implementation
- [ ] Objective-C doesn't support inheritance
- [ ] dual class inheritance
- [ ] unlimited class inheritance and protocol adherence

#### Q15. How many keys does this NSDictionary have after this code is executed?

`NSDictionary *dict = [[NSDictionary alloc] initWithObjectsAndKeys: @"b", @"e", @"a", @"r", nil];`

- [x] 2
- [ ] 4
- [ ] 5
- [ ] This code contains an error.

#### Q16. What is the error in this code?

```
NSMutableDictionary *dict1 = [NSMutableDictionary dictionaryWithCapacity:5];
[dict1 setValue:@"key" forKey:@"value"];
```

- [ ] The key and value items are mixed
- [ ] You can't set the capacity of a dictionary
- [ ] NSMutableDictionary doesn't have a :setValue:forKey function.
- [x] Nothing is wrong with it

#### Q17. What is printed from this code?

```
NSData *data = [@"print" dataUsingEncoding:NSASCIIStringEncoding];
NSLog(@"%@", [[NSString alloc] initWithData:data encoding:NSASCIIStringEncoding]);
```

- [x] print
- [ ] Nothing is printed from this code.
- [ ] nil
- [ ] This code is invalid.

#### Q18. What is different about this function?

`+(void)doSomething;`

- [x] It is static
- [ ] It is abstract.
- [ ] It is inline.
- [ ] This code contains an error.

#### Q19. Structs can have \_?

- [ ] functions
- [ ] initializers
- [x] fields
- [ ] All of the above

#### Q20. What is wrong with this code?

```
@interface MyClass : NSObject
    @property (strong, nonatomic, readonly) NSString *name;
  @end
```

- [x] There is nothing wrong with this code.
- [ ] There is not read-only directive.
- [ ] MyClass doesn't implement NSObject.
- [ ] Properties are declared in the implementation.

#### Q21. What is an enums base type for the code below?

`typedef enum { Foo1, Foo2} Foo;`

- [x] There is no base type.
- [ ] NSObject
- [ ] int
- [ ] NSNumber

#### Q22. If you want to store a small amount of information (e.g., user settings), whats the best, built-in way to go?

- [x] UserDefaults
- [ ] plist file
- [ ] CoreData
- [ ] TextFile

#### Q23. What are categories used for?

- [x] to extend other classes
- [ ] to manage access control
- [ ] to coordinate objects
- [ ] to group classes

#### Q24. What is this Objective-C code checking?

```
if ([keyPath isInstanceOf:[NSString class]]) {
}
```

- [x] This code contains an error
- [ ] if keyPath is an instance of NSString
- [ ] if keyPath's baseclass is the same as NSString's baseclass
- [ ] if keyPath implements the same methods as NSString

#### Q25. What is this a declaration of?

`int(^foo)(int);`

- [ ] an Extension
- [ ] a Generic
- [x] a block of code
- [ ] an abstract class

#### Q26. For observing changes to a property, which of these two statements cause the related method to be called and why?

```
1. _val = 1;
2. self.val= 100;
```

- [x] Statement 2, since it calls the auto-created setter on the property.
- [ ] Statement 1, since it uses the property directly.
- [ ] Statement 2, since it specifies the class instance to use.
- [ ] Statement 1, since it calls the auto-created setter on the property.

#### Q27. What is wrong with this code?

```
float x = 2.0;
int(^foo)(int) = ^(int n1) {
  return (int)(n1*x);
};
foo(5);
```

- [ ] Ints and floats can't be multiplied.
- [ ] The parameter isn't declared correctly.
- [ ] x is not in the right scope.
- [x] Nothing is wrong with this code.

#### Q28. What's the difference between an array and a set?

- [x] Arrays are ordered, non-unique values.
- [ ] Arrays are stored sorted.
- [ ] Sets are ordered, unique values.
- [ ] Sets can contain nils.

#### Q29. Dot notation can be used for \_?

- [ ] nothing, as they're never used in Objective-C
- [ ] function calls only
- [x] property getter/setter
- [ ] parameter delimiters

#### Q30. What is the value of newVals after this code is executed?

```
NSArray *vals = @[@"1", @"2", @"3"];
NSPredicate *pred = [NSPredicate predicateWithFormat:@"SELF.intValue > 1"];
NSArray *newVals = [vals filteredArrayUsingPredicate:pred];
```

- [x] 2,3
- [ ] nil
- [ ] 2,"3"
- [ ] This code contains an error

#### Q31. How would this function be called?

`-(int)foo:(int)a b:(int)c;`

- [ ] self.foo(5, b:10);
- [ ] This code contains an error.
- [ ] [self foo:5:10:20];
- [x] [self foo:5 b:10];

#### Q32. What is the type of the error return value stored in json?

```
NSError *error;
NSData *data;
id json = [NSJSONSerialization JSONObjectWithData:data options:NSJSONReadingAllowFragments error:&error];
```

- [ ] NSString
- [ ] NSArray
- [x] id
- [ ] NSDictionary

#### Q33. What is significant about this function declaration?

```
-(void)testFunc:(NSString**)str;
```

- [ ] The parameter is passed by value and can not be changed
- [ ] \*\* is not allowed on a parameter
- [ ] The parameter may be nil
- [x] The parameter is passed by reference and may be changed

#### Q34. What is printed from this code execution?

```
typedef enum {
    thing1,
    thing2,
    thing3
} Thing;


-(void) enumStuff {
    NSLog(@"%d", thing2);
}
```

- [ ] 0
- [x] 1
- [ ] thing2
- [ ] This code does not print anything

#### Q35. You are worried about threaded access to a property and possible collision in writing. What directive should you use on the property?

- [ ] non-atomic
- [ ] strong
- [ ] weak
- [x] atomic

#### Q36. What is wrong with this line of code?

```
int temp = 1==1;
```

- [ ] `temp` is a keyword.
- [ ] 1==1 is invalid.
- [ ] 1==1 evaluates to a Boolean.
- [x] Nothing is wrong with it.

#### Q37. What is special about the code within this block?

```
dispatch_async(dispatch_get_main_queue(), ^{
// code
});
```

- [x] It executes on the main queue.
- [ ] It is the last code to run before the app goes inactive.
- [ ] It executes on a background thread.
- [ ] It is queued to execute in the background.

#### Q38. How many items are in set1 after this code executes?

```
NSMutableSet *set1 = [NSMutableSet setWithObjects: @1,@2, @3, @4, @5, nil];
[set1 add0bject:@3];
```

- [ ] zero
- [ ] six
- [ ] one
- [x] five

#### Q39. What is wrong with this code?

```
NSDictionary *d1 = @[@"v1", @4, @"v2", @5.6, @"v3"];
NSlog(@"d1: %@", d1);
```

- [ ] NSDictionary cannot be printed this way.
- [x] The last key is missing a value.
- [ ] Dictionaries cannot have mixed types as values.
- [ ] d1 is assigned an NSArray of values.

#### Q40. What is the initial value of the property `val`?

```
@property (nonatomic, readonly) int val;
```

- [ ] 8
- [ ] nil
- [ ] -1
- [x] undefined

#### Q41. Which thread should UI updates be processed on to avoid crashes and application lag?

- [x] UI
- [ ] dispatch
- [ ] background
- [ ] main

#### Q42. What is the value of val after this code is executed?

```
NSString *val = @"1.23";
BOOL tf = val.boolValue;
```

- [ ] YES
- [x] NO
- [ ] 1
- [ ] This code is invalid

#### Q43. In this code, what does ThatOne refer to?

```
@interface TestClass : ThisOne <ThatOne>
```

- [ ] the parent class of TestClass
- [ ] the name of the category being created for ThisOne
- [x] a protocoL impLemented by ThisOne
- [ ] a helper file's name

#### Q44. What is the value of result after this code is executed?

```
NSString *result = [Ftest"
    stringByTrimmingCharactersInSet.NSCharacterSet.alphanumericCharacterSet];
```

- [ ] ""
- [ ] "es"
- [x] "test"
- [ ] None of the above

#### Q45. When will self receive the notification based on this code?

```
MyClass .classObj = [[MyClass allot] init];
[class0bj add0bserver:self forKeyPath:@"name"
              options:NSKeyValueObservingOptionNew context:NULL];
```

- [ ] class0bj will recieve the notification, not self.
- [ ] when class0bj is set to "name"
- [x] when the name property in the class0bj instance changes
- [ ] None of the above

#### Q46. What is wrong with this code?

```
[*"true" boolValue];
```

- [ ] String literal are not created with\*.
- [x] NSString doesn't have a boolValue function.
- [ ] "true" has no meaning.
- [ ] There is nothing wrong with this code.

#### Q47. How many times does this loop execute?

```
int loopVal = 0;
for (int i=0; i>loopVal; i--){
    i--;
}
```

- [ ] an infinite number of times
- [x] zero
- [ ] one
- [ ] This code is invalid.

#### Q48. What will this code print?

```
NSLog(@"%lu", @"test".length);
```

- [ ] "test"
- [x] 4
- [ ] 0
- [ ] Nothing, this code is invalid.

#### Q49. What is the value of numVtoInt after this code is executed?

```
NSNumber *numV = [NSNumber numberWithFloat:6.7];
int numVtoInt = numV.intValue;
```

- [ ] 6
- [ ] 0
- [ ] 6.7
- [x] 7

#### Q50. What does this code print?

```
NSString *val = @"1.23";
NSLog(@"%.04f", val.floatValue);
```

- [x] 1.2300
- [ ] .04
- [ ] 1
- [ ] This code is invalid

#### Q51. What is the maximum possible value of r1 in this code?

```
int r1 = arc4random() % 10;
```

- [ ] 0
- [x] 9
- [ ] 1
- [ ] 10
