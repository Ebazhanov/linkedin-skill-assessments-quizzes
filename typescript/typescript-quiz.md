## TypeScript

#### Q1. What is TypeScript?

- [ ] A JavaScript runtime environment
- [x] A superset of JavaScript that adds static type definitions
- [ ] A JavaScript framework for building web applications
- [ ] A database query language

[Reference TypeScript Overview](https://www.typescriptlang.org/docs/)

#### Q2. Which command is used to compile TypeScript files?

- [ ] `node filename.ts`
- [x] `tsc filename.ts`
- [ ] `npm run typescript`
- [ ] `ts-compile filename.ts`

[Reference TypeScript Compiler](https://www.typescriptlang.org/docs/handbook/compiler-options.html)

#### Q3. What is the correct way to define a variable with a specific type in TypeScript?

- [ ] `var name: string = "John";`
- [x] `let name: string = "John";`
- [ ] `string name = "John";`
- [ ] `name: string = "John";`

[Reference Variable Declarations](https://www.typescriptlang.org/docs/handbook/variable-declarations.html)

#### Q4. Which of the following is a valid TypeScript interface?

```typescript
interface User {
  name: string;
  age: number;
  email?: string;
}
```

- [x] The above interface is valid
- [ ] Interfaces cannot have optional properties
- [ ] Interfaces must use `class` keyword
- [ ] Interfaces cannot define property types

[Reference Interfaces](https://www.typescriptlang.org/docs/handbook/interfaces.html)

#### Q5. What does the `?` symbol mean in TypeScript when used with properties?

- [ ] It makes the property required
- [x] It makes the property optional
- [ ] It makes the property nullable
- [ ] It makes the property readonly

[Reference Optional Properties](https://www.typescriptlang.org/docs/handbook/interfaces.html#optional-properties)

#### Q6. Which TypeScript feature allows you to define a type that can be one of several types?

- [ ] Intersection types
- [x] Union types
- [ ] Generic types
- [ ] Mapped types

```typescript
type Status = 'loading' | 'success' | 'error';
```

[Reference Union Types](https://www.typescriptlang.org/docs/handbook/unions-and-intersections.html)

#### Q7. What is the output of this TypeScript code after compilation?

```typescript
enum Color {
  Red,
  Green,
  Blue,
}

console.log(Color.Red);
```

- [x] `0`
- [ ] `"Red"`
- [ ] `1`
- [ ] `undefined`

[Reference Enums](https://www.typescriptlang.org/docs/handbook/enums.html)

#### Q8. Which keyword is used to create a generic function in TypeScript?

```typescript
function identity<T>(arg: T): T {
  return arg;
}
```

- [ ] `generic`
- [x] `<T>`
- [ ] `template`
- [ ] `type`

[Reference Generics](https://www.typescriptlang.org/docs/handbook/generics.html)

#### Q9. What is the correct way to extend an interface in TypeScript?

- [ ] `interface Child implements Parent`
- [x] `interface Child extends Parent`
- [ ] `interface Child inherits Parent`
- [ ] `interface Child : Parent`

[Reference Extending Interfaces](https://www.typescriptlang.org/docs/handbook/interfaces.html#extending-interfaces)

#### Q10. Which TypeScript utility type makes all properties of a type optional?

- [x] `Partial<T>`
- [ ] `Required<T>`
- [ ] `Optional<T>`
- [ ] `Nullable<T>`

[Reference Utility Types](https://www.typescriptlang.org/docs/handbook/utility-types.html)

#### Q11. What is the purpose of the `readonly` modifier in TypeScript?

- [ ] It makes properties writable only once
- [x] It prevents properties from being modified after initialization
- [ ] It makes properties private
- [ ] It makes properties static

[Reference Readonly](https://www.typescriptlang.org/docs/handbook/interfaces.html#readonly-properties)

#### Q12. Which statement about TypeScript classes is correct?

- [ ] TypeScript classes cannot have constructors
- [x] TypeScript classes support access modifiers like private, protected, and public
- [ ] TypeScript classes cannot extend other classes
- [ ] TypeScript classes are compiled to functions

[Reference Classes](https://www.typescriptlang.org/docs/handbook/classes.html)

#### Q13. What is the correct syntax for a function type in TypeScript?

- [ ] `function(x: number, y: number): number`
- [x] `(x: number, y: number) => number`
- [ ] `func(x: number, y: number) -> number`
- [ ] `number function(x: number, y: number)`

[Reference Function Types](https://www.typescriptlang.org/docs/handbook/functions.html)

#### Q14. Which TypeScript feature allows you to create a type based on another type?

- [ ] Type aliases
- [ ] Interfaces
- [x] Mapped types
- [ ] Union types

```typescript
type Readonly<T> = {
  readonly [P in keyof T]: T[P];
};
```

[Reference Mapped Types](https://www.typescriptlang.org/docs/handbook/mapped-types.html)

#### Q15. What does the `never` type represent in TypeScript?

- [ ] A type that can be anything
- [ ] A type that is null or undefined
- [x] A type that represents values that never occur
- [ ] A type that is always false

[Reference Never Type](https://www.typescriptlang.org/docs/handbook/basic-types.html#never)

#### Q16. Which operator is used for non-null assertion in TypeScript?

- [ ] `?`
- [x] `!`
- [ ] `??`
- [ ] `?.`

```typescript
let name: string | null = getName();
console.log(name!.length); // Non-null assertion
```

[Reference Non-null Assertion](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-2-0.html#non-null-assertion-operator)

#### Q17. What is the correct way to define a tuple type in TypeScript?

- [ ] `type Tuple = string, number;`
- [x] `type Tuple = [string, number];`
- [ ] `type Tuple = {string, number};`
- [ ] `type Tuple = <string, number>;`

[Reference Tuple Types](https://www.typescriptlang.org/docs/handbook/basic-types.html#tuple)

#### Q18. Which TypeScript configuration file is used to specify compiler options?

- [ ] `package.json`
- [x] `tsconfig.json`
- [ ] `typescript.config.js`
- [ ] `tsc.config.json`

[Reference tsconfig.json](https://www.typescriptlang.org/docs/handbook/tsconfig-json.html)

#### Q19. What is the purpose of the `keyof` operator in TypeScript?

- [ ] It creates a new object with specified keys
- [x] It produces a union of known, public property names of a type
- [ ] It checks if a key exists in an object
- [ ] It deletes a key from an object

[Reference keyof Operator](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-2-1.html#keyof-and-lookup-types)

#### Q20. Which statement about TypeScript modules is correct?

- [ ] TypeScript only supports CommonJS modules
- [x] TypeScript supports multiple module systems including ES6, CommonJS, and AMD
- [ ] TypeScript modules cannot export types
- [ ] TypeScript modules are always compiled to global scope

[Reference Modules](https://www.typescriptlang.org/docs/handbook/modules.html)

#### Q21. What is the correct way to define a string literal type in TypeScript?

- [ ] `type Status = string;`
- [x] `type Status = "pending" | "completed" | "failed";`
- [ ] `type Status = String("pending", "completed", "failed");`
- [ ] `type Status = ["pending", "completed", "failed"];`

[Reference Literal Types](https://www.typescriptlang.org/docs/handbook/literal-types.html)

#### Q22. Which TypeScript utility type creates a type with all properties set to required?

- [ ] `Partial<T>`
- [x] `Required<T>`
- [ ] `Complete<T>`
- [ ] `Mandatory<T>`

[Reference Required Utility Type](https://www.typescriptlang.org/docs/handbook/utility-types.html#requiredtype)

#### Q23. What is the purpose of type guards in TypeScript?

- [ ] To prevent type errors at compile time
- [x] To narrow down types within conditional blocks
- [ ] To create new types
- [ ] To guard against null values

```typescript
function isString(value: any): value is string {
  return typeof value === 'string';
}
```

[Reference Type Guards](https://www.typescriptlang.org/docs/handbook/advanced-types.html#type-guards-and-differentiating-types)

#### Q24. Which operator provides null coalescing in TypeScript?

- [ ] `||`
- [x] `??`
- [ ] `?.`
- [ ] `!`

[Reference Nullish Coalescing](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-7.html#nullish-coalescing)

#### Q25. What is the correct syntax for optional chaining in TypeScript?

- [ ] `obj.prop.subprop || undefined`
- [x] `obj?.prop?.subprop`
- [ ] `obj.?prop.?subprop`
- [ ] `obj..prop..subprop`

[Reference Optional Chaining](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-7.html#optional-chaining)

#### Q26. Which TypeScript feature allows you to create conditional types?

- [ ] Union types
- [ ] Intersection types
- [x] Conditional types with `extends`
- [ ] Mapped types

```typescript
type NonNullable<T> = T extends null | undefined ? never : T;
```

[Reference Conditional Types](https://www.typescriptlang.org/docs/handbook/conditional-types.html)

#### Q27. What is the purpose of the `abstract` keyword in TypeScript classes?

- [ ] It makes the class private
- [x] It prevents the class from being instantiated directly
- [ ] It makes all methods static
- [ ] It makes the class immutable

[Reference Abstract Classes](https://www.typescriptlang.org/docs/handbook/classes.html#abstract-classes)

#### Q28. Which TypeScript utility type picks specific properties from a type?

- [x] `Pick<T, K>`
- [ ] `Select<T, K>`
- [ ] `Extract<T, K>`
- [ ] `Choose<T, K>`

[Reference Pick Utility Type](https://www.typescriptlang.org/docs/handbook/utility-types.html#picktype-keys)

#### Q29. What is the correct way to define a generic constraint in TypeScript?

- [ ] `function func<T implements Constraint>(arg: T): T`
- [x] `function func<T extends Constraint>(arg: T): T`
- [ ] `function func<T : Constraint>(arg: T): T`
- [ ] `function func<T inherits Constraint>(arg: T): T`

[Reference Generic Constraints](https://www.typescriptlang.org/docs/handbook/generics.html#generic-constraints)

#### Q30. Which statement about TypeScript decorators is correct?

- [ ] Decorators are enabled by default
- [x] Decorators are an experimental feature that must be enabled
- [ ] Decorators can only be used with classes
- [ ] Decorators are compiled to regular functions

[Reference Decorators](https://www.typescriptlang.org/docs/handbook/decorators.html)

#### Q31. What is the purpose of the `infer` keyword in TypeScript?

- [ ] To infer types automatically
- [x] To introduce a type variable within conditional types
- [ ] To create intersection types
- [ ] To make properties optional

[Reference Infer Keyword](https://www.typescriptlang.org/docs/handbook/conditional-types.html#type-inference-in-conditional-types)

#### Q32. Which TypeScript utility type excludes certain types from a union?

- [ ] `Remove<T, U>`
- [x] `Exclude<T, U>`
- [ ] `Without<T, U>`
- [ ] `Omit<T, U>`

[Reference Exclude Utility Type](https://www.typescriptlang.org/docs/handbook/utility-types.html#excludetype-excludedunion)

#### Q33. What is the correct way to define an index signature in TypeScript?

- [ ] `interface Obj { string: any; }`
- [x] `interface Obj { [key: string]: any; }`
- [ ] `interface Obj { key[string]: any; }`
- [ ] `interface Obj { [string]: any; }`

[Reference Index Signatures](https://www.typescriptlang.org/docs/handbook/interfaces.html#indexable-types)

#### Q34. Which TypeScript feature allows you to merge multiple types into one?

- [x] Intersection types (`&`)
- [ ] Union types (`|`)
- [ ] Conditional types
- [ ] Mapped types

[Reference Intersection Types](https://www.typescriptlang.org/docs/handbook/unions-and-intersections.html#intersection-types)

#### Q35. What is the purpose of the `declare` keyword in TypeScript?

- [ ] To declare new variables
- [x] To tell TypeScript about code that exists elsewhere
- [ ] To make variables immutable
- [ ] To create type aliases

[Reference Declaration Files](https://www.typescriptlang.org/docs/handbook/declaration-files/introduction.html)

#### Q36. Which TypeScript utility type creates a type by omitting specific properties?

- [ ] `Remove<T, K>`
- [x] `Omit<T, K>`
- [ ] `Exclude<T, K>`
- [ ] `Without<T, K>`

[Reference Omit Utility Type](https://www.typescriptlang.org/docs/handbook/utility-types.html#omittype-keys)

#### Q37. What is the correct syntax for a rest parameter in TypeScript?

- [ ] `function func(args: ...any[]): void`
- [x] `function func(...args: any[]): void`
- [ ] `function func(args...: any[]): void`
- [ ] `function func(args: any...): void`

[Reference Rest Parameters](https://www.typescriptlang.org/docs/handbook/functions.html#rest-parameters)

#### Q38. Which statement about TypeScript namespaces is correct?

- [ ] Namespaces are the preferred way to organize code
- [x] Modules are generally preferred over namespaces for code organization
- [ ] Namespaces cannot contain types
- [ ] Namespaces are compiled to classes

[Reference Namespaces](https://www.typescriptlang.org/docs/handbook/namespaces.html)

#### Q39. What is the purpose of the `as` keyword in TypeScript?

- [ ] To create type aliases
- [x] To perform type assertions
- [ ] To extend interfaces
- [ ] To import modules

[Reference Type Assertions](https://www.typescriptlang.org/docs/handbook/basic-types.html#type-assertions)

#### Q40. Which TypeScript utility type extracts the return type of a function?

- [ ] `Returns<T>`
- [x] `ReturnType<T>`
- [ ] `Result<T>`
- [ ] `Output<T>`

[Reference ReturnType Utility Type](https://www.typescriptlang.org/docs/handbook/utility-types.html#returntypetype)
