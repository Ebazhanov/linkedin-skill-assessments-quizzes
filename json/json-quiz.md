## JSON

#### Q1. By convention, what name is used for the first key in a JSON schema?

- [ ] schema
- [x] \$schema
- [ ] JsonSchema
- [ ] JSONschema

[Reference](https://json-schema.org/learn/getting-started-step-by-step)

#### Q2. Which code is the closest JSON equivalent of the data shown?

```
[
    'red',
    'blue',
    'green'
]
```

- [ ] A

```json
["red", "green", "blue"]
```

- [x] B

```json
["red", "blue", "green"]
```

- [ ] C

```json
{
  "color": "red",
  "color": "blue",
  "color": "green"
}
```

- [ ] D

```json
{
  "red": "red",
  "blue": "blue"
}
```

#### Q3. Which JavaScript method converts a JavaScript value to Json?

- [ ] JSON.parse()
- [x] JSON.stringify()
- [ ] JSON.toString()
- [ ] JSON.objectify()

[Reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify)

#### Q4. Which data type is NOT part of JSON standard?

- [ ] string
- [ ] number
- [x] date
- [ ] array

[Reference](https://www.ibm.com/docs/en/baw/19.x?topic=format-json-properties-data-type-conversions)

#### Q5. Which term is commonly used to refer to converting data to JSON?

- [ ] unpacking
- [x] serialization
- [ ] deserialization
- [ ] parsing

#### Q6. Which code uses the correct JSON syntax to encode the key/value pair shown?

`accountNum: '000605802'`

- [x] "accountNum": "000605802"
- [ ] accountNum: "000605802"
- [ ] "accountNum": 000605802
- [ ] accountNum: 000605802

[Reference](https://www.microfocus.com/documentation/silk-performer/195/en/silkperformer-195-webhelp-en/GUID-6AFC32B4-6D73-4FBA-AD36-E42261E2D77E.html)

#### Q7. What character do you specify before a JSON control character when you want to use that control characters as a literal part of a string?

- [ ] `/`
- [x] `\`
- [ ] `:`
- [ ] `{`

[Reference](https://www.lambdatest.com/free-online-tools/json-escape)

#### Q8. Which data type is part of the JSON standard?

- [x] Boolean
- [ ] map
- [ ] promise
- [ ] function

[Reference](https://www.ibm.com/docs/en/baw/19.x?topic=format-json-properties-data-type-conversions)

#### Q9. Which key name is used to specify properties that must be included for JSON to be valid?

- [ ] important
- [ ] base
- [ ] core
- [x] required

#### Q10. Which is the valid JSON equivalent of the data shown?

```
{
	photo: {
	width: 1600,
	height: 900,
	binaries: {
	url: 'https://www.example.com/images/34097349843',
	thumbnail: 'https://www.example.com/images/thumbs/34097349843'
	},
	animated: false,
	tags: [116, 943, 234, 38793],
	}
}
```

- [ ] A

```json
{
  "photo": {
    "width": 1600,
    "height": 900,
    "binaries": {
      "url": "https://www.example.com/images/34097349843",
      "thumbnail": "https://www.example.com/images/thumbs/34097349843"
    },
    "animated": "false",
    "tags": [116, 943, 234, 38793]
  }
}
```

- [x] B

```json
{
  "photo": {
    "width": 1600,
    "height": 900,
    "binaries": {
      "url": "https://www.example.com/images/34097349843",
      "thumbnail": "https://www.example.com/images/thumbs/34097349843"
    },
    "animated": false,
    "tags": [116, 943, 234, 38793]
  }
}
```

- [ ] C

```json
{
  "photo": {
    "width": 1600,
    "height": 900,
    "binaries": {
      "url": "https://www.example.com/images/34097349843",
      "thumbnail": "https://www.example.com/images/thumbs/34097349843"
    },
    "animated": true,
    "tags": [116, 943, 234, 38793]
  }
}
```

- [ ] D

```json
{
  "photo": {
    "width": "1600",
    "height": "900",
    "binaries": {
      "url": "https://www.example.com/images/34097349843",
      "thumbnail": "https://www.example.com/images/thumbs/34097349843"
    },
    "animated": "false",
    "tags": ["116", "943", "234", "38793"]
  }
}
```

[Reference](https://www.geeksforgeeks.org/json-data-types/)

#### Q11. How do you store several paragraphs of text as a string in JSON?

- [ ] Escape all whitespaces except space characters.
- [x] Escape line breaks.
- [ ] Escape paragraphs.
- [ ] Remove all whitespaces

#### Q12. What data type is represented by the value of the key/value pair shown?

`loggedIn: true`

- [ ] string
- [x] Boolean
- [ ] number
- [ ] object

[Reference](https://www.w3schools.com/js/js_json_datatypes.asp)

#### Q13. If you need to store the loggedIn status of a user in JSON as a boolean, what is the correct syntax?

- [ ] "loggedIn": (true)
- [ ] loggedIn: "true"
- [x] "loggedIn": true
- [ ] loggedIn: {true}

[Reference](https://www.w3schools.com/js/js_json_datatypes.asp)

#### Q14. What does JSON with padding (JSON-P) use to make a request?

- [ ] an `<origin>` element
- [ ] a header request
- [x] the `<script>` element
- [ ] the XMLHttpRequest object

#### Q15. Which value is supported in the JSON specifications?

- [ ] undefined
- [ ] infinity
- [ ] NaN
- [x] null

[Reference](https://cswr.github.io/JsonSchema/spec/basic_types/#:~:text=JSON%20Documents%20can%20be%20either,can%20be%20any%20of%20these.)

#### Q16. Which JavaScript method converts JSON to a JavaScript value?

- [x] JSON.parse()
- [ ] JSON.stringify()
- [ ] JSON.toString()
- [ ] JSON.objectify()

[Reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse)

#### Q17. Transferring JSON information from client to server and back again often includes HTTP requests. Match each method with the best choice describing its use.

    1.Sends data to specific server to create or update information.
    2.Sends data to specific server to create or update information without the risk of creating the resource more than once.
    3.Previews what the GET request response might be without the body of the text.
    4.Learns the communication channels used by the target source.
    5.Requests information from a specific source.
    6.Removes information.

- [ ] 1.POST 2.DELETE 3.OPTIONS 4.HEADER 5.GET 6.PUT
- [x] 1.POST 2.PUT 3.HEADER 4.OPTIONS 5.GET 6.DELETE

#### Q18. Which code uses valid JSON syntax for the text "Centennial Olympics?

- [ ] A

```json
{
"host": "Atlanta",
"year": 1996
/_ Centennial Olympics _/
}
```

- [ ] B

```json
{
  "host": "Atlanta",
  "year": 1996
  // Centennial Olympics
}
```

- [ ] C

```json
{
  "host": "Atlanta",
  "year": 1996,
  "comment": "Centennial Olympics"
}
```

- [ ] D

```json
{
  "host": "Atlanta",
  "year": 1996,
  \"Centennial Olympics\"
}
```

- [x] E

```json
{
  "host": "Atlanta",
  "year": 1996,
  "comment": "\"Centennial Olympics"
}
```

[Reference](https://www.geeksforgeeks.org/json-data-types/)

#### Q19. Can trailing commas be used in objects and arrays?

- [ ] yes
- [ ] only if there is more than one item
- [x] no
- [ ] only when arrays and objects contain more than 10 items

[Reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Trailing_commas#:~:text=JSON%2C%20however%2C%20disallows%20all%20trailing%20commas.)

#### Q20. Which whitespace characters should be escaped within a string?

- [ ] All whitespace is allowed.
- [x] double quotes, slashes new lines, and carriage returns
- [ ] new lines and carriage returns only
- [ ] double quotes only

[Reference](https://www.lambdatest.com/free-online-tools/json-escape)

#### Q21. Which is supported by YAML but not supported by JSON?

- [ ] nested
- [x] comments
- [ ] arrays
- [ ] null values

[Reference](https://builtin.com/software-engineering-perspectives/yaml-vs-json)

#### Q22. Which is an invalid JSON value?

- [ ] `"'|=(_)(X 72(_)|\/||\*'"`
- [ ] `"|=(_)(X 72(_)|\/||\*"`
- [ ] `"|=(_)(X\" \"72(_)|\/||\*"`
- [x] `"\s(_)(X 72(_)|\/||\*"`

#### Q23. How do you encode a date in JSON?

- [ ] Convert the date to UTC and enclose in quotes.
- [x] Encode the date as string using the ISO-8601 date format.
- [ ] Wrap the date in double quotes.
- [ ] Add a "date" key to your object and include the date as string.

[Reference](https://www.w3docs.com/snippets/javascript/the-right-json-date-format.html#:~:text=To%20represent%20dates%20in%20JavaScript,JSON%20is%20serialized%20and%20deserialized.)

#### Q24. What’s wrong with this JavaScript?

`JSON.parse({"first": "Sarah", "last": "Connor"}) ;`

- [ ] JSON should be wrapped with curly braces.
- [ ] JSON.parse() is missing an argument.
- [x] The value supplied to JSON.parse() is not a string.
- [ ] Nothing is wrong with it.

[Reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse)

#### Q25. What does this JavaScript code print?

```js
printNullness(JSON.parse('{ "lemmings": [] }'));
printNullness(JSON.parse('{ "lemmings": null }'));
printNullness(JSON.parse('{ "lemmings": "null" }'));

function printNullness(testMe) {
  if (testMe.lemmings == null) console.log('null');
  else console.log('not null');
}
```

- [x] A

```
not null
null
not null
```

- [ ] B

```
null
null
not null
```

- [ ] C

```
not null
null
null
```

- [ ] D

```
null
null
null
```

#### Q26. What tool might you use to validate your JSON?

- [x] JSONLint
- [ ] ValidateJSON
- [ ] JSONFiddle
- [ ] TextEdit

[Reference](https://jsonlint.com/)

#### Q27. What characters denote strings in JSON?

- [x] double quotes
- [ ] smart (curly) quotes
- [ ] single or double quotes
- [ ] single quotes

[Reference](https://www.w3schools.com/js/js_json_datatypes.asp)

#### Q28. Which code is a valid JSON equivalent of the key/value pair shown that also preserves the data type? `constant: 6.022E23`

- [ ] `"constant": "6.022E23"`
- [ ] `"constant": "6\.022\E23"`
- [x] `"constant": 6.022E23`
- [ ] `constant: "6.022E23"`

[Reference](https://json-schema.org/understanding-json-schema/reference/numeric.html) **Explanation**: Scientific Notation is a valid JSON number. You can use `e` or `E`.

#### Q29. Which element is added to the DOM to create a JSON-P request?

- [ ] `<object>`
- [x] `<script>`
- [ ] `<json>`
- [ ] `<meta>`

#### Q30. Why do so many APIs use JSON?

- [ ] Because it's object-based.
- [x] Because it's a simple and adaptable format for sharing data.
- [ ] Because it's based on JavaScript.
- [ ] Because it is derived from SGML.

[Reference](https://www.oracle.com/in/database/what-is-json/#:~:text=JSON%20has%20gained%20momentum%20in,no%20additional%20code%20for%20parsing.)

#### Q31. You need to assemble a list of members, but your JSON is not parsing correctly. How do you change it?

```
{
  "avengers": [
    "iron man",
    "hulk",
    "thor",
    "black widow",
    "ant man",
    "spider man'
  ]
}
```

- [x] A

```json
{
  "avengers": ["iron man", "hulk", "thor", "black widow", "ant man", "spider man"]
}
```

- [ ] B

```json
{
  'avengers': [
  {'iron man',
  'hulk',
  'thor',
  'black widow',
  'ant man',
  'spider man'}
  ]
}
```

- [ ] C

```json
{
  "avengers": ["iron man", "hulk", "thor", "black widow", "ant man", "spider man"]
}
```

- [ ] D

```json
{
  "avengers": {[
    "iron man",
    "hulk",
    "thor",
    "black widow",
    "ant man",
    "spider man"
  ]}
}
```

#### Q32. When building dynamic web applications using AJAX, developers originally used the \_ data format, which has since been replaced by JSON.

- [x] XML
- [ ] GRAPHQL
- [ ] REST
- [ ] SOAP

#### Q33. How is a true boolean value represented in JSON?

- [ ] TRUE
- [ ] "true"
- [ ] 1
- [x] true

[Reference](https://www.w3schools.com/js/js_json_datatypes.asp)

#### Q34. Which array is valid JSON?

- [ ] ['tatooine', 'hoth', 'dagobah']
- [ ] [tatooine, hoth, dagobah]
- [ ] ["tatooine", "hoth", "dagobah",]
- [x] ["tatooine", "hoth", "dagobah"]

[Reference](https://www.w3schools.com/js/js_json_datatypes.asp)

#### Q35. What data type is encoded in the outermost component of the JSON shown?

```json
[
  {
    "year": 2024
  },
  {
    "location": "unknown"
  }
]
```

- [ ] object
- [x] array
- [ ] number
- [ ] string

[Reference](https://www.w3schools.com/js/js_json_datatypes.asp)

#### Q36. Which is ignored by JSON but treated as significant by YAML?

- [ ] trailing commas
- [ ] trailing decimals
- [x] whitespace
- [ ] leading zeroes

[Reference](https://www.geeksforgeeks.org/what-is-the-difference-between-yaml-and-json/)

#### Q37. When you need to set the value of a key in JSON to be blank, what is the correct syntax for the empty value?

- [ ] FALSE
- [ ] 0
- [ ] ""
- [x] null

[Reference](https://cswr.github.io/JsonSchema/spec/basic_types/#:~:text=JSON%20Documents%20can%20be%20either,can%20be%20any%20of%20these.)

#### Q38. How do you assign a number value in JSON?

- [ ] Escape the number with a backslash.
- [ ] Enclose the number in double quotes.
- [ ] Enclose the number in single quotes.
- [x] Leave the number as is.

#### Q39. Which code uses the correct JSON syntax for encoding a key/value pair with a null value?

- [x] "lastVisit": null
- [ ] lastVisit: null
- [ ] "lastVisit": 0
- [ ] "lastVisit": undefined

[Reference](https://json-schema.org/understanding-json-schema/reference/null.html)

#### Q40. Which reference to the Unicode character U+1F602 complies with the JSON standard?

- [ ] 128514
- [ ] d83dde02
- [x] \uD83D\uDE02
- [ ] \&#128514;

#### Q41. Which code uses the correct JSON syntax for a key/Value pair containing a string?

- [x] "largest": "blue whale"
- [ ] largest: 'blue whale'
- [ ] 'largest': 'blue whale'
- [ ] largest: "blue whale"

[Reference](https://cswr.github.io/JsonSchema/spec/basic_types/#:~:text=JSON%20Documents%20can%20be%20either,can%20be%20any%20of%20these.)

#### Q42. Which key name is used to specify data type in a JSON schema?

- [ ] data
- [ ] schemadata
- [ ] schematype
- [x] type

[Reference](https://json-schema.org/understanding-json-schema/reference/type)

#### Q43. Which code is a valid JSON equivalent of the key/value pair shown that also preserves the original value?

- [ ] "UPC": \043875
- [x] UPC: "043875"
- [ ] "UPC": 043875
- [ ] UPC: '043875'

[Reference](https://cswr.github.io/JsonSchema/spec/basic_types/#:~:text=JSON%20Documents%20can%20be%20either,can%20be%20any%20of%20these.)

#### Q44. Which data format is a JSON schema written in?

- [ ] markdown
- [ ] YAML
- [ ] XML
- [x] JSON

#### Q45. Which code is valid JSON equivalent of the key/value pair shown that also preserves the data type?

- [x] "variance": -0.0823
- [ ] variance: "-0.0823"
- [ ] "variance": "\-0.0823"
- [ ] variance: -0.0823

[Reference](https://json-schema.org/understanding-json-schema/reference/numeric.html)

#### Q46. With what character should key/value pairs be separated?

- [x] colon
- [ ] space
- [ ] semicolon
- [ ] comma

[Reference](https://www.microfocus.com/documentation/silk-performer/195/en/silkperformer-195-webhelp-en/GUID-6AFC32B4-6D73-4FBA-AD36-E42261E2D77E.html)

#### Q47. What character separates keys from values?

- [x] :
- [ ] ->
- [ ] ::
- [ ] .

[Reference](https://www.microfocus.com/documentation/silk-performer/195/en/silkperformer-195-webhelp-en/GUID-6AFC32B4-6D73-4FBA-AD36-E42261E2D77E.html)

#### Q48. If a string contains line breaks, what should you do?

- [ ] Wrap line breaks in single quotation marks
- [ ] Make no changes, because whitespace is allowed
- [ ] Replace any line breaks with `\r`
- [x] Replace any line breaks with `\n`

#### Q49. Which number types are available in javascript but not supported in json?

- [ ] Fractional and Transcendental
- [ ] Infinity or Rational
- [ ] Rational and Irrational
- [x] Infinity or NaN

#### Q50. How should a date value be stored in JSON?

- [ ] As a string with quotes
- [ ] As a string without quotes
- [ ] As a string in ISO 8583 format
- [x] As a string in ISO 8601 format

[Reference](https://www.w3docs.com/snippets/javascript/the-right-json-date-format.html#:~:text=To%20represent%20dates%20in%20JavaScript,JSON%20is%20serialized%20and%20deserialized.)

#### Q51. Is the JSON code shown here valid?

![JSON object with key "Vehicles" containing an array of emojis](images/Q51/Q51.jpeg)

- [ ] No, emojis must be escaped with a backslash.
- [ ] No, JSON strings are not allowed to use emojis.
- [ ] No, emojis should never be enclosed with double quotes.
- [x] Yes, emojis are valid characters because JSON strings are unicode.

#### Q52. What data structure do you use to encode ordered information?

- [ ] list
- [x] array
- [ ] struct
- [ ] indexed hash

[Reference](https://www.w3schools.com/js/js_json_datatypes.asp)

#### Q53. What are valid values in JSON?

- [ ] arrays, strings, numbers, true/false
- [ ] hashes, arrays, strings, numbers, booleans, null
- [ ] arrays, objects, lists, strings, numbers, booleans
- [x] objects, arrays, strings, numbers, booleans, null

#### Q54. Which key format is valid JSON?

- [ ] key: "value"
- [x] "key": "value"
- [ ] key, "value"
- [ ] 'key': 'value'

[Reference](https://www.microfocus.com/documentation/silk-performer/195/en/silkperformer-195-webhelp-en/GUID-6AFC32B4-6D73-4FBA-AD36-E42261E2D77E.html)

#### Q55. What data type is encoded in the outermost component of the JSON shown?

```json
{
  "result": [
    {
      "year": 2024
    },
    {
      "location": "unknown"
    }
  ]
}
```

- [ ] number
- [ ] array
- [ ] string
- [x] object

#### Q56. What's wrong with this JSON object?

```json
{
  "series": "Star Trek",
  "episodes": "The Trouble with Tribbles",
  "season": 3
}
```

- [ ] Key/value pairs should be separated by semicolons.
- [x] Keys should be enclosed with double quotes.
- [ ] Key/value pairs should always have a trailing comma.
- [ ] Keys and values should be enclosed with single quotes.

#### Q57. How should comments be formatted in JSON?

- [ ] Wrap the comments in single quotes and place it at the bottom of the file.
- [ ] Wrap the comments in double parentheses.
- [ ] Escape comments by placing two slashes at the start of the comment.
- [x] JSON does not support comments.

#### Q58. How would you make the following string valid in JSON?

`"name": 'bb-8'`

- [ ] name: "bb-8"
- [ ] "name": \'bb-8\'
- [x] "name": "bb-8"
- [ ] "name": bb-8

#### Q59. How are values separated in JSON?

- [ ] with brackets
- [ ] with colons
- [x] with commas
- [ ] with parentheses

#### Q60. With which programming language is JSON best used?

- [x] any language, as JSON is language agnostic.
- [ ] Ruby
- [ ] JavaScript
- [ ] Python

#### Q61. What values can arrays contain?

- [ ] only numbers
- [x] any valid JSON value
- [ ] only strings and numbers
- [ ] only strings

#### Q62. What technique can be used to represent complex objects with JSON?

- [ ] reserialization
- [x] nesting
- [ ] memorization
- [ ] minimization

#### Q63. What characters are used to enclose an array?

- [x] `[]`
- [ ] `{}`
- [ ] `""`
- [ ] `()`

#### Q64. What is the official MIME type for JSON?

- [ ] text/json
- [ ] text/javascript
- [x] application/json
- [ ] data/json

#### Q65. Which character cannot be part of string within JSON without additional formatting?

- [ ] /
- [x] "
- [ ] -
- [ ] :

#### Q66. What is the purpose of JSON?

- [x] to provide a simple way to serialize and deserialize data between different sources
- [ ] to provide a way to store data for machine learning
- [ ] to provide an archival solution for data warehousing
- [ ] to provide a way for JavaScript to run other languages

#### Q67. Can you assume the order of keys in an object?

- [ ] No, but you can sort the keys with `JSON.sort()`.
- [ ] Yes, object keys are always ordered alphabetically.
- [ ] Yes, but only when the object is first parsed.
- [x] No, you can never assume object keys will be in order.

#### Q68. With what character should object keys be enclosed?

- [ ] `*`
- [ ] `#`
- [ ] `^`
- [x] `"`

#### Q69. What is the maximum number of key/value pairs that JSON supports?

- [ ] 10,000
- [ ] 1000
- [x] There is no defined limit.
- [ ] 1 million

#### Q70. What is the recommended term used to refer to multiple resources?

- [ ] a swarm
- [x] multiple resources
- [ ] a collection
- [ ] a group

#### Q71. Does JSON support signed numbers?

- [ ] yes, but only if they are enclosed in quotes
- [ ] only with integers
- [x] yes
- [ ] no

#### Q72. What two nonnumerical characters can numbers contain?

- [x] dash and dot
- [ ] dash and comma
- [ ] comma and exclamation point
- [ ] dot and comma

#### Q73. What JavaScript method is used to load JSON data?

- [ ] JSON.ingest()
- [ ] JSON.convert()
- [ ] JSON.read()
- [x] JSON.parse()

#### Q74. How are the values in an array separated?

- [ ] with right arrows
- [ ] with colons
- [ ] with semicolons
- [x] with commas

#### Q75. What is the minimum number of values in an array?

- [x] zero
- [ ] one
- [ ] two
- [ ] three

#### Q76. In JSON, a set of brackets ([]) is used to denote **\_**, whereas curly braces ({}) denote **\_**.

- [x] arrays; objects
- [ ] objects; functions
- [ ] arrays; functions
- [ ] key/value pairs; arrays

#### Q77. How does JSON represent truth, falsity and nullness?

- [x] true, false, null
- [ ] true, false
- [ ] TRUE, FALSE, NULL

#### Q78. If an object key contains spaces, how can you access its value in JavaScript?

- [ ] Remove spaces from the key before accessing the value.
- [ ] Use dot notation to access the value.
- [ ] Use object key index to access the value.
- [x] Use bracket notation to access the value.

#### Q79. When parsing JSON, "caching" is a method used to \_.

- [ ] remove duplicate data from a server
- [x] temporarily store data for faster access
- [ ] store excess information in chunks to be reviewed later
- [ ] clog up a web browser with useless information

#### Q80. What is the only valid whitespace character within a string that does not require an escape character?

- [ ] line break
- [x] space
- [ ] tab
- [ ] return

#### Q81. What technique can you use to safely encode very large numbers?

- [x] Store the number as a string
- [ ] Convert the number into an exponent.
- [ ] Round the number to the nearest 10-digit number.
- [ ] Split the number into smaller parts.

#### Q82. Which code is a valid JSON equivalent of the key/value pair shown that also preserves the data type?

`variance: -0.0823`

- [ ] variance: "-0.0823"
- [ ] variance: -0.0823
- [x] "variance": "-0.0823"
- [ ] "variance": "\-0.0823"

[Reference](https://www.w3schools.com/js/js_json_datatypes.asp)

#### Q83. Based on the JSON object shown, which JavaScript code would you use to find out what is in this vehicle's glove box while assigning the glove box contents to a new variable?

```js
myVehicleContents = {
  van: {
    inside: {
      'glove box': 'maps',
      'passenger seat': 'crumbs',
    },
    exterior: {
      trunk: 'jack',
    },
  },
};
```

- [ ] A

```js
myVehicleContents.van.inside['glove box'] = gloveBoxContents;
```

- [x] B

```js
var gloveBoxContents = myVehicleContents.van.inside['glove box'];
gloveBoxContents;
```

- [ ] C

```js
var gloveBoxContents = myVehicleContents.van.glove box.contents;
gloveBoxContents;
```

- [ ] D

```js
myVehicleContents.van.inside['inside'] = gloveBoxContents;
```

[Source](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_Objects)

#### Q84. What characters are used to define an object?

- [ ] ||
- [x] {}
- [ ] ()
- [ ] []

#### Q85. The JSON structure features nested objects and arrays. Sometimes the data containing these features exists in relational databases. How is the relational structure different that JSON?

- [ ] It has a flat architecture.
- [ ] It has a rewritable structure.
- [x] It has an array-only structure.
- [ ] It has a table structure.

#### Q86. What is supported by YAML but not supported by JSON?

- [ ] arrays
- [ ] null values
- [x] comments
- [ ] nested

`YAML supports # comments but not JSON`

#### Q87. Which is an invalid JSON value? (same as previous question, but different possible answers)

- [ ] `"'|=(_)(X 72(_)|\/||*'"`
- [x] `"\s(_)(X 72(_)|\/||*"`
- [ ] `"|=(_)(X\" \"72(_)|\/||*"`
- [ ] `"|=(_)(X 72(_)|\/||*"`

#### Q88. How can you change this array to make it valid?

`{"rey",'leia',"ashoka",}`

- [ ] `['rey', 'leia', "ashoka",}`
- [ ] `['rey', 'leia', 'ashoka',}`
- [x] `["rey", "leia", "ashoka"]`
- [ ] `{"rey", "leia", "ashoka"}`

#### Q89. If a non-zero number starts with a zero, what character should immediately follow the zero?

- [ ] zero or more digits
- [ ] one or more digits
- [x] a period
- [ ] a dollar sign

#### Q90. Who would you modify the array below to store additional attributes for each student?

```json
{
  "students": ["Tess", "Erin", "June"]
}
```

- [x] Convert each student to an object, then add key/value paris to each student object as needed.
- [ ] Add additional name/value pairs, separated by commas, after "students".
- [ ] Convert each student into an array and add extra elements to the array.
- [ ] Wrap the existing "students" key with curly braces.

#### Q91. Which is _not_ a valid JSON number

- [ ] `99999999999999999999`
- [ ] `"42"`
- [ ] `-32`
- [x] `1111.00.110011`

#### Q92. What is the maximum string length in JSON?

- [ ] 512 characters
- [x] There is no defined limit.
- [ ] 2,056 characters
- [ ] 1,024 characters

#### Q94. How would you update this JSON to indicate that Jane is now available for part-time work ?

```json
{
  "name": "Jane",
  "job": "developer",
  "skills": ["ruby", "rails", "javascript"],
  "available": false
}
```

- [x] A

```json
{
  "name": "Jane",
  "job": "developer",
  "skills": ["ruby", "rails", "javascript"],
  "available": true,
  "seeking": "part-time"
}
```

- [ ] B

```json
{
  "name": "Jane",
  "job": "developer",
  "skills": ["ruby", "rails", "javascript"],
  "available": "true",
  "seeking": "part-time"
}
```

- [ ] C

```json
{
  "name": "Jane",
  "job": "developer",
  "skills": ["ruby", "rails", "javascript"],
  "available": false,
  "seeking": "part-time"
}
```

- [ ] D

```json
{
  "name": "Jane",
  "job": "developer",
  "skills": ["ruby", "rails", "javascript"],
  "available": "true",
  "seeking": "part-time"
}
```

Hint: true needs to be a boolean and part-time a string so in double quotes.

#### Q95. When you need to set the value of a key in JSON to be blank, what is the correct syntax for the empty value?

- [ ] ""
- [ ] 0
- [ ] FALSE
- [x] null

**Explanation:** The other options won't work as well, as demonstrated by [this StackOverflow post](https://stackoverflow.com/questions/21120999/representing-null-in-json).

#### Q96. What is true about paginated reports? (Select all that apply.)

A. They are formatted to fit well on a page.

B. They shrink the report data to fit on a page.

C. They truncate the report data to fit on a single page.

D. They are both printable and shareable.

- [x] A,D
- [ ] B OR C
- [ ] A,B,D
- [ ] A,C,D

**Explanation:** The true statements about paginated reports are:
A. They are formatted to fit well on a page.
D. They are both printable and shareable.
So the correct options are A and D.

#### Q97. As a Scrum Master you have noticed a pattern that the most interesting stories on the sprint backlog get started right away, and the least interesting stories languish or don't get done. What should you do?

- [ ] During story point estimation, increase the points assigned to the least interesting stories so the team can boost their velocity.
- [x] Share your observation with the team and invite them to own and solve the problem.
- [ ] Ask the team to use a lottery system to assign each story.
- [ ] Ask the Tech Lead to assign every story to a developer so they all get done efficiently and with accountability.

**Explanation:** Encourage open communication within the team and involve them in problem-solving to find a solution that works best for their specific context and helps address the issue of disinterest in certain stories.

#### Q99. When you need to set the value of a key in JSON to be blank, what is the correct syntax for the empty value?

- [ ] FALSE
- [ ] 0
- [ ] ""
- [x] null

#### Q100. What does JSON with padding (JSON-P) use to make a request?

- [ ] an `<origin>` element
- [ ] a header request
- [x] the `<script>` element
- [ ] the XMLHttpRequest object

#### Q102. What’s wrong with this JavaScript?

`JSON.parse({"first": "Sarah", "last": "Connor"}) ;`

- [ ] JSON should be wrapped with curly braces.
- [ ] JSON.parse() is missing an argument.
- [x] The value supplied to JSON.parse() is not a string.
- [ ] Nothing is wrong with it.

#### Q103. You need to assemble a list of members, but your JSON is not parsing correctly. How do you change it?

`{"avengers": ["iron man", "hulk", "thor", "black widow", "ant man", "spider man" ]}`

- [x] `{"avengers": ["iron man", "hulk", "thor", "black widow", "ant man", "spider man"]}`

- [ ] `{'avengers': {'iron man', 'hulk', 'thor', 'black widow', 'ant man', 'spider man'}]}`

- [ ] `{"avengers": ["iron man", "hulk", "thor", "black widow", "ant man", "spider man"]}`

- [ ] `{"avengers": {["iron man", "hulk", "thor", "black widow", "ant man", "spider man" ]}}`

#### Q104. Which reference to the Unicode character U+1F602 complies with the JSON standard?

- [ ] 128514
- [ ] d83dde02
- [x] \uD83D\uDE02
- [ ] \&#128514;

#### Q105. How should comments be formatted in JSON?

- [ ] Wrap the comments in single quotes and place it at the bottom of the file.
- [ ] Wrap the comments in double parentheses.
- [ ] Escape comments by placing two slashes at the start of the comment.
- [x] JSON does not support comments.

#### Q106. What is the purpose of JSON-P (JSON with padding) in web development, and how is it typically used?

- [ ] To validate JSON data before parsing it in JavaScript.
- [ ] To provide additional padding for JSON objects to improve readability.
- [x] To overcome the same-origin policy limitation when making cross-domain AJAX requests.
- [ ] To compress JSON data for faster transmission over the network.

Explanation:- JSON-P, or JSON with padding, serves the purpose of overcoming the same-origin policy limitation in web development. The same-origin policy restricts web pages from making AJAX requests to a different domain for security reasons. JSON-P works by wrapping JSON data in a JavaScript function call, allowing data to be retrieved from an external domain as if it were a script. This technique is commonly used for securely fetching data from external APIs, making it a valuable tool for cross-domain data exchange in web applications.

#### Q107. In a JSON document, how can you represent a key that contains special characters, such as spaces or hyphens, to ensure proper parsing and access in JavaScript?

- [ ] Wrap the key in single quotes.
- [ ] Enclose the key in square brackets.
- [ ] backslashes before special characters.
- [x] Enclose the key in double quotes.

Explanation:- When you have a key in a JSON document that contains special characters, spaces, or hyphens, it is essential to enclose the key in double quotes. JSON requires keys to be represented within double quotes to ensure proper parsing and access in JavaScript. This ensures that JavaScript can correctly interpret keys with special characters or spaces and access their associated values.

#### Q108. Which is ignored by JSON but treated as significant by YAML?

- [ ] trailing commas
- [ ] trailing decimals
- [x] whitespace
- [ ] leading zeroes

#### Q109. Which code uses valid JSON syntax for the text "Centennial Olympics?

- [ ] A

```json
{
"host": "Atlanta",
"year": 1996
/_ Centennial Olympics _/
}
```

- [ ] B

```json
{
  "host": "Atlanta",
  "year": 1996
  // Centennial Olympics
}
```

- [x] C

```json
{
  "host": "Atlanta",
  "year": 1996,
  "comment": "Centennial Olympics"
}
```

- [ ] D

```json
{
  "host": "Atlanta",
  "year": 1996,
  \"Centennial Olympics\"
}
```

- [ ] E

```json
{
  "host": "Atlanta",
  "year": 1996,
  "comment": "\"Centennial Olympics"
}
```

#### Q110. What data type is encoded in the outermost component of the JSON shown?

```json
[
  {
    "year": 2024
  },
  {
    "location": "unknown"
  }
]
```

- [ ] object
- [x] array
- [ ] number
- [ ] string

#### Q111. Which is an invalid JSON value?

- [ ] `"'|=(_)(X 72(_)|\/||\*'"`
- [ ] `"|=(_)(X 72(_)|\/||\*"`
- [ ] `"|=(_)(X\" \"72(_)|\/||\*"`
- [x] `"\s(_)(X 72(_)|\/||\*"`

#### Q112. What are the valid number types in JSON?

- [ ] Whole Numbers and Decimals
- [ ] Real Numbers and Fractions
- [x] Integer, Floating Points, and Exponents (Scientific Notation, e.g., 3e4)
- [ ] Prime Numbers and Complex Numbers

#### Q114. What is the purpose of JSON Web Tokens (JWT)?

- [ ] To validate JSON data
- [ ] To store sensitive information
- [x] To represent information between parties
- [ ] To create JSON schemas

#### Q115. What is JSON-RPC used for?

- [x] Remote procedure calls encoded in JSON
- [ ] Rendering graphics in web applications
- [ ] JavaScript execution control
- [ ] Data validation in JSON

#### Q116. Which of the following is a key difference between JSON and XML?

- [ ] JSON uses tags
- [ ] XML is more lightweight
- [x] JSON is easier for humans to read
- [ ] XML is used for programming, while JSON is for data exchange

#### Q117. Which HTTP header is commonly used to prevent cross-site scripting (XSS) attacks when working with JSON?

- [ ] Content-Encoding
- [x] Access-Control-Allow-Origin
- [ ] JSON-Security
- [ ] XSS-Prevention

#### Q118. What does the JSON Merge Patch format allow you to do?

- [ ] Combine multiple JSON documents into one
- [x] Partially update a JSON document
- [ ] Compress JSON data for storage
- [ ] Convert JSON to XML

#### Q119. Which method is used to parse a JSON string and return a JavaScript object in modern web browsers?

- [ ] parseJSON()
- [x] JSON.parse()
- [ ] evalJSON()
- [ ] loadJSON()

#### Q120. What is the primary purpose of JSON-LD (JSON Linked Data)?

- [ ] To enable two-way data binding in JavaScript
- [ ] To represent data in a more human-readable format
- [x] To express structured data that is linked to other data
- [ ] To create dynamic web pages with JSON

#### Q121. What is the correct way to represent an empty array in JSON?

- [x] `[]`
- [ ] `{}`
- [ ] `null`
- [ ] `""`

**Explanation:**
An empty array in JSON is represented by square brackets with nothing inside: `[]`. Curly braces `{}` represent an empty object, not an array.

[Reference](https://www.json.org/json-en.html)

#### Q122. What is the correct way to represent an empty object in JSON?

- [ ] `[]`
- [x] `{}`
- [ ] `null`
- [ ] `""`

**Explanation:**
An empty object in JSON is represented by curly braces with nothing inside: `{}`. Square brackets `[]` represent an empty array, not an object.

[Reference](https://www.json.org/json-en.html)

#### Q123. Can JSON keys contain spaces?

- [x] Yes, but they must be enclosed in quotes
- [ ] No, spaces are not allowed
- [ ] Yes, without quotes
- [ ] Only in JSON5

**Explanation:**
JSON keys can contain spaces, but like all JSON keys, they must be enclosed in double quotes. For example: `{"first name": "John"}` is valid JSON.

[Reference](https://www.json.org/json-en.html)

#### Q124. What is the maximum nesting depth recommended for JSON?

- [ ] 10 levels
- [ ] 50 levels
- [x] No official limit, but practical limits exist
- [ ] 100 levels

**Explanation:**
JSON specification doesn't define a maximum nesting depth, but practical limits exist based on parser implementations. Most parsers handle reasonable nesting (typically 100+ levels), but deeply nested structures can cause performance issues.

[Reference](https://tools.ietf.org/html/rfc8259)

#### Q125. Which of these is NOT a valid JSON number?

- [ ] `-42`
- [ ] `3.14159`
- [x] `0xFF`
- [ ] `1.5e-10`

**Explanation:**
Hexadecimal notation like `0xFF` is not valid in JSON. JSON only supports decimal numbers, including negative numbers, decimals, and scientific notation.

[Reference](https://www.json.org/json-en.html)

#### Q126. Can JSON represent dates natively?

- [ ] Yes, using the Date type
- [x] No, dates must be represented as strings or numbers
- [ ] Yes, using ISO 8601 format
- [ ] Only in JSON Schema

**Explanation:**
JSON has no native date type. Dates are typically represented as strings (often in ISO 8601 format like "2024-01-01T00:00:00Z") or as numbers (Unix timestamps).

[Reference](https://www.json.org/json-en.html)

#### Q127. What is JSON Schema used for?

- [ ] To compress JSON data
- [x] To define the structure and validation rules for JSON documents
- [ ] To convert JSON to XML
- [ ] To encrypt JSON data

**Explanation:**
JSON Schema is a vocabulary that allows you to annotate and validate JSON documents, defining the expected structure, data types, and constraints.

[Reference](https://json-schema.org/)

#### Q128. Which JSON Schema keyword is used to specify that a property is required?

- [ ] `mandatory`
- [x] `required`
- [ ] `necessary`
- [ ] `must`

**Explanation:**
The `required` keyword in JSON Schema specifies an array of property names that must be present in the JSON object.

[Reference](https://json-schema.org/understanding-json-schema/reference/object.html#required-properties)

#### Q129. What does the `$schema` keyword indicate in JSON Schema?

- [ ] The schema name
- [x] The JSON Schema version being used
- [ ] The schema author
- [ ] The schema description

**Explanation:**
The `$schema` keyword identifies which version of the JSON Schema specification the schema is written against.

[Reference](https://json-schema.org/understanding-json-schema/reference/schema.html)

#### Q130. Can JSON comments be included using `//` or `/* */`?

- [ ] Yes, both are supported
- [ ] Yes, but only `//`
- [x] No, JSON does not support comments
- [ ] Yes, but only `/* */`

**Explanation:**
Standard JSON does not support comments. However, JSON5 (an extension) does support comments. For standard JSON, you can use a special key like "\_comment" if you need annotations.

[Reference](https://www.json.org/json-en.html)

#### Q131. What is JSON5?

- [ ] JSON version 5
- [x] An extension of JSON with additional features like comments and trailing commas
- [ ] A compression format for JSON
- [ ] A JSON validation tool

**Explanation:**
JSON5 is an extension to JSON that aims to make it easier for humans to write and maintain by adding features like comments, trailing commas, unquoted keys, and more.

[Reference](https://json5.org/)

#### Q132. What is JSONP used for?

- [ ] JSON parsing
- [x] Cross-domain data requests (legacy technique)
- [ ] JSON compression
- [ ] JSON validation

**Explanation:**
JSONP (JSON with Padding) was a technique to request data from a server in a different domain, bypassing same-origin policy. It's now largely replaced by CORS.

[Reference](https://en.wikipedia.org/wiki/JSONP)

#### Q133. What is the correct MIME type for JSON?

- [ ] `text/json`
- [x] `application/json`
- [ ] `application/javascript`
- [ ] `text/javascript`

**Explanation:**
The official MIME type for JSON is `application/json`. While `text/json` was sometimes used historically, `application/json` is the standard.

[Reference](https://tools.ietf.org/html/rfc4627)

#### Q134. Can JSON keys be numbers?

- [ ] Yes, without quotes
- [x] No, keys must be strings
- [ ] Yes, but only integers
- [ ] Only in JSON5

**Explanation:**
In JSON, all keys must be strings enclosed in double quotes. Even if a key looks like a number, it must be quoted: `{"123": "value"}`.

[Reference](https://www.json.org/json-en.html)

#### Q135. What is the difference between `JSON.parse()` and `eval()` for parsing JSON?

- [ ] No difference
- [x] JSON.parse() is safer and only parses JSON, eval() executes any JavaScript
- [ ] eval() is faster
- [ ] JSON.parse() is deprecated

**Explanation:**
`JSON.parse()` is the safe way to parse JSON as it only parses JSON syntax. `eval()` executes any JavaScript code, making it a security risk if used with untrusted data.

[Reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse)

#### Q136. What does `JSON.stringify()` do with `undefined` values in objects?

- [ ] Converts them to `null`
- [ ] Converts them to `"undefined"`
- [x] Omits the property entirely
- [ ] Throws an error

**Explanation:**
When `JSON.stringify()` encounters `undefined` as a property value in an object, it omits that property from the output. However, `undefined` in arrays becomes `null`.

[Reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify)

#### Q137. What is the second parameter of `JSON.stringify()` used for?

- [ ] Indentation
- [x] Replacer function or array to filter/transform values
- [ ] Error handling
- [ ] Encoding

**Explanation:**
The second parameter (replacer) can be a function that transforms values or an array that specifies which properties to include in the output.

[Reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify)

#### Q138. What is the third parameter of `JSON.stringify()` used for?

- [x] Indentation (space) for pretty-printing
- [ ] Error handling
- [ ] Encoding
- [ ] Compression

**Explanation:**
The third parameter specifies the indentation for pretty-printing. It can be a number (spaces) or a string (like "\t" for tabs).

[Reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify)

#### Q139. Can JSON represent circular references?

- [ ] Yes, using special syntax
- [x] No, JSON.stringify() will throw an error
- [ ] Yes, but only in JSON5
- [ ] Yes, using $ref

**Explanation:**
JSON cannot represent circular references. Attempting to stringify an object with circular references will throw a "TypeError: Converting circular structure to JSON" error.

[Reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify)

#### Q140. What is JSON Pointer (RFC 6901)?

- [ ] A pointer to JSON files
- [x] A syntax for identifying a specific value within a JSON document
- [ ] A JSON compression technique
- [ ] A JSON validation tool

**Explanation:**
JSON Pointer defines a string syntax for identifying a specific value within a JSON document, like "/users/0/name" to access the name of the first user.

[Reference](https://tools.ietf.org/html/rfc6901)

#### Q141. What is JSON Patch (RFC 6902)?

- [ ] A JSON bug fix
- [x] A format for expressing a sequence of operations to apply to a JSON document
- [ ] A JSON compression format
- [ ] A JSON validation format

**Explanation:**
JSON Patch defines a format for expressing a sequence of operations (add, remove, replace, move, copy, test) to modify a JSON document.

[Reference](https://tools.ietf.org/html/rfc6902)

#### Q142. What is the `toJSON()` method used for?

- [ ] To convert objects to JSON
- [x] To customize how an object is serialized by JSON.stringify()
- [ ] To parse JSON strings
- [ ] To validate JSON

**Explanation:**
If an object has a `toJSON()` method, `JSON.stringify()` will call it and use its return value instead of the original object.

[Reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#tojson_behavior)

#### Q143. Can JSON represent binary data?

- [ ] Yes, using binary type
- [x] No, but it can be encoded as Base64 strings
- [ ] Yes, using hexadecimal
- [ ] Only in JSON5

**Explanation:**
JSON has no native binary type. Binary data must be encoded as strings, typically using Base64 encoding.

[Reference](https://www.json.org/json-en.html)

#### Q144. What is the maximum string length in JSON?

- [ ] 65,536 characters
- [ ] 1 MB
- [x] No official limit, depends on implementation
- [ ] 2^32 characters

**Explanation:**
The JSON specification doesn't define a maximum string length. Practical limits depend on the parser implementation and available memory.

[Reference](https://tools.ietf.org/html/rfc8259)

#### Q145. What is JSON-RPC?

- [ ] JSON Remote Procedure
- [x] A remote procedure call protocol encoded in JSON
- [ ] A JSON compression protocol
- [ ] A JSON validation protocol

**Explanation:**
JSON-RPC is a stateless, light-weight remote procedure call (RPC) protocol that uses JSON to encode calls and responses.

[Reference](https://www.jsonrpc.org/)

#### Q146. What is GeoJSON?

- [ ] JSON for geography classes
- [x] A format for encoding geographic data structures
- [ ] Geographical JSON compression
- [ ] A JSON validation tool for maps

**Explanation:**
GeoJSON is a format for encoding a variety of geographic data structures using JSON, commonly used in mapping applications.

[Reference](https://geojson.org/)

#### Q147. What is the purpose of the `reviver` parameter in `JSON.parse()`?

- [ ] To validate JSON
- [x] To transform values during parsing
- [ ] To handle errors
- [ ] To format output

**Explanation:**
The `reviver` parameter is a function that can transform the parsed values before they are returned, useful for converting strings to dates or other custom transformations.

[Reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse)

#### Q148. Can JSON property names be duplicate?

- [ ] Yes, all duplicates are kept
- [x] Technically yes, but behavior is undefined; last value typically wins
- [ ] No, parser will throw an error
- [ ] Yes, but only in JSON5

**Explanation:**
While JSON parsers typically accept duplicate keys, the behavior is undefined in the specification. Most implementations use the last value, but this should be avoided.

[Reference](https://tools.ietf.org/html/rfc8259#section-4)

#### Q149. What is BSON?

- [ ] Binary JSON
- [x] Binary JSON, a binary-encoded serialization of JSON-like documents
- [ ] Better JSON
- [ ] Basic JSON

**Explanation:**
BSON (Binary JSON) is a binary-encoded serialization format used by MongoDB. It extends JSON with additional data types like Date and Binary.

[Reference](http://bsonspec.org/)

#### Q150. What is MessagePack?

- [ ] A JSON messaging protocol
- [x] An efficient binary serialization format similar to JSON
- [ ] A JSON compression algorithm
- [ ] A JSON validation tool

**Explanation:**
MessagePack is an efficient binary serialization format that is more compact than JSON and supports additional types.

[Reference](https://msgpack.org/)

#### Q151. What is the correct way to represent a boolean true in JSON?

- [x] `true`
- [ ] `True`
- [ ] `"true"`
- [ ] `1`

**Explanation:**
JSON boolean values are lowercase: `true` and `false`. They are not strings and not capitalized.

[Reference](https://www.json.org/json-en.html)

#### Q152. What is the correct way to represent null in JSON?

- [x] `null`
- [ ] `NULL`
- [ ] `"null"`
- [ ] `undefined`

**Explanation:**
The null value in JSON is lowercase: `null`. It is not a string and not capitalized. `undefined` is not a valid JSON value.

[Reference](https://www.json.org/json-en.html)

#### Q153. Can JSON represent functions?

- [ ] Yes, using function type
- [x] No, JSON cannot represent functions
- [ ] Yes, as strings
- [ ] Only in JSON5

**Explanation:**
JSON cannot represent functions. If you try to stringify an object with function properties, those properties will be omitted.

[Reference](https://www.json.org/json-en.html)

#### Q154. What is JSON Web Token (JWT)?

- [ ] A JSON validation token
- [x] A compact, URL-safe means of representing claims between two parties
- [ ] A JSON encryption method
- [ ] A JSON compression token

**Explanation:**
JWT is a standard for creating access tokens that assert claims. It consists of three parts: header, payload (JSON), and signature.

[Reference](https://jwt.io/)

#### Q155. What are the three parts of a JWT?

- [ ] Header, Body, Footer
- [x] Header, Payload, Signature
- [ ] Type, Data, Hash
- [ ] Version, Content, Checksum

**Explanation:**
A JWT consists of three Base64-encoded parts separated by dots: Header (algorithm and type), Payload (claims), and Signature (verification).

[Reference](https://jwt.io/introduction)

#### Q156. What is JSON Schema's `type` keyword used for?

- [ ] To name the schema
- [x] To specify the data type of a value
- [ ] To define custom types
- [ ] To import types

**Explanation:**
The `type` keyword in JSON Schema specifies the data type: "string", "number", "integer", "boolean", "array", "object", or "null".

[Reference](https://json-schema.org/understanding-json-schema/reference/type.html)

#### Q157. What is the `enum` keyword in JSON Schema?

- [ ] To enumerate properties
- [x] To restrict a value to a fixed set of values
- [ ] To create enumerations
- [ ] To count items

**Explanation:**
The `enum` keyword restricts a value to one of a fixed set of values, like `{"enum": ["red", "green", "blue"]}`.

[Reference](https://json-schema.org/understanding-json-schema/reference/generic.html#enumerated-values)

#### Q158. What is the `pattern` keyword in JSON Schema?

- [ ] To define patterns
- [x] To validate strings against a regular expression
- [ ] To create patterns
- [ ] To match patterns

**Explanation:**
The `pattern` keyword specifies a regular expression that a string value must match to be valid.

[Reference](https://json-schema.org/understanding-json-schema/reference/string.html#regular-expressions)

#### Q159. What is the `minimum` keyword in JSON Schema?

- [ ] The smallest number
- [x] The minimum value a number can have
- [ ] The minimum length
- [ ] The minimum items

**Explanation:**
The `minimum` keyword specifies the minimum value (inclusive) that a numeric value can have.

[Reference](https://json-schema.org/understanding-json-schema/reference/numeric.html#range)

#### Q160. What is the `maxLength` keyword in JSON Schema?

- [ ] The maximum string
- [x] The maximum length of a string
- [ ] The maximum size
- [ ] The maximum value

**Explanation:**
The `maxLength` keyword specifies the maximum length (number of characters) that a string value can have.

[Reference](https://json-schema.org/understanding-json-schema/reference/string.html#length)

#### Q161. What is JSON-LD used for?

- [ ] JSON Loading
- [x] Linking data and adding semantic meaning to JSON
- [ ] JSON Linting
- [ ] JSON Debugging

**Explanation:**
JSON-LD (JSON for Linking Data) is a method of encoding linked data using JSON, adding semantic meaning and context to data.

[Reference](https://json-ld.org/)

#### Q162. What is the `@context` keyword in JSON-LD?

- [ ] The context menu
- [x] Defines how terms in the document map to IRIs
- [ ] The execution context
- [ ] The document context

**Explanation:**
The `@context` keyword in JSON-LD defines the context for interpreting the JSON document, mapping terms to IRIs (Internationalized Resource Identifiers).

[Reference](https://json-ld.org/spec/latest/json-ld/#the-context)

#### Q163. Can JSON represent infinity?

- [ ] Yes, using `Infinity`
- [x] No, JSON numbers cannot represent infinity
- [ ] Yes, using `"Infinity"`
- [ ] Only in JSON5

**Explanation:**
JSON numbers cannot represent infinity or NaN. Attempting to stringify these values results in `null`.

[Reference](https://www.json.org/json-en.html)

#### Q164. What is the correct way to escape a double quote in a JSON string?

- [ ] `""`
- [x] `\"`
- [ ] `'"`
- [ ] `&quot;`

**Explanation:**
Double quotes inside JSON strings must be escaped with a backslash: `\"`. For example: `"He said \"Hello\""`.

[Reference](https://www.json.org/json-en.html)

#### Q165. What is the correct way to represent a newline in a JSON string?

- [ ] `\r`
- [x] `\n`
- [ ] A literal newline
- [ ] `<br>`

**Explanation:**
Newlines in JSON strings are represented by the escape sequence `\n`. Literal newlines are not allowed in JSON strings.

[Reference](https://www.json.org/json-en.html)

#### Q166. What is the correct way to represent a tab in a JSON string?

- [ ] Four spaces
- [x] `\t`
- [ ] A literal tab
- [ ] `\tab`

**Explanation:**
Tabs in JSON strings are represented by the escape sequence `\t`. Literal tabs are not allowed in JSON strings.

[Reference](https://www.json.org/json-en.html)

#### Q167. What is the correct way to represent a backslash in a JSON string?

- [x] `\\`
- [ ] `/`
- [ ] `\`
- [ ] `//`

**Explanation:**
Backslashes in JSON strings must be escaped with another backslash: `\\`. For example: `"C:\\Users\\Name"`.

[Reference](https://www.json.org/json-en.html)

#### Q168. Can JSON represent Unicode characters?

- [x] Yes, using \uXXXX escape sequences or directly
- [ ] No, only ASCII
- [ ] Yes, but only in JSON5
- [ ] Yes, but only with special encoding

**Explanation:**
JSON supports Unicode characters either directly (if the file is UTF-8 encoded) or using `\uXXXX` escape sequences where XXXX is the hexadecimal code point.

[Reference](https://www.json.org/json-en.html)

#### Q169. What is the `additionalProperties` keyword in JSON Schema?

- [ ] To add more properties
- [x] To control whether properties not defined in the schema are allowed
- [ ] To define additional schemas
- [ ] To add property metadata

**Explanation:**
The `additionalProperties` keyword determines whether properties not explicitly defined in the schema are allowed in the JSON object.

[Reference](https://json-schema.org/understanding-json-schema/reference/object.html#additional-properties)

#### Q170. What is the `items` keyword in JSON Schema?

- [ ] To count items
- [x] To define the schema for array elements
- [ ] To list items
- [ ] To add items

**Explanation:**
The `items` keyword in JSON Schema defines the schema that array elements must conform to.

[Reference](https://json-schema.org/understanding-json-schema/reference/array.html#items)

#### Q171. What is the `$ref` keyword in JSON Schema?

- [ ] A reference number
- [x] To reference another schema or schema definition
- [ ] A reference type
- [ ] A reference counter

**Explanation:**
The `$ref` keyword allows you to reference another schema or a definition within the same schema, enabling schema reuse.

[Reference](https://json-schema.org/understanding-json-schema/structuring.html#ref)

#### Q172. What is the `definitions` keyword in JSON Schema?

- [ ] To define terms
- [x] To define reusable schema components
- [ ] To create definitions
- [ ] To list definitions

**Explanation:**
The `definitions` (or `$defs` in newer versions) keyword allows you to define reusable schema components that can be referenced with `$ref`.

[Reference](https://json-schema.org/understanding-json-schema/structuring.html#defs)

#### Q173. What is the `allOf` keyword in JSON Schema?

- [ ] All of the schemas
- [x] Requires the data to be valid against all of the given schemas
- [ ] All properties
- [ ] All items

**Explanation:**
The `allOf` keyword requires that the data validates against all of the schemas in the array, useful for combining schemas.

[Reference](https://json-schema.org/understanding-json-schema/reference/combining.html#allof)

#### Q174. What is the `anyOf` keyword in JSON Schema?

- [ ] Any of the properties
- [x] Requires the data to be valid against any (one or more) of the given schemas
- [ ] Any items
- [ ] Any values

**Explanation:**
The `anyOf` keyword requires that the data validates against at least one of the schemas in the array.

[Reference](https://json-schema.org/understanding-json-schema/reference/combining.html#anyof)

#### Q175. What is the `oneOf` keyword in JSON Schema?

- [ ] One of the properties
- [x] Requires the data to be valid against exactly one of the given schemas
- [ ] One item
- [ ] One value

**Explanation:**
The `oneOf` keyword requires that the data validates against exactly one (and only one) of the schemas in the array.

[Reference](https://json-schema.org/understanding-json-schema/reference/combining.html#oneof)

#### Q176. What is the `not` keyword in JSON Schema?

- [ ] To negate values
- [x] Requires the data to NOT be valid against the given schema
- [ ] To exclude properties
- [ ] To deny access

**Explanation:**
The `not` keyword requires that the data does not validate against the given schema, useful for excluding certain patterns.

[Reference](https://json-schema.org/understanding-json-schema/reference/combining.html#not)

#### Q177. What is Content Security Policy (CSP) and how does it relate to JSON?

- [ ] JSON security protocol
- [x] HTTP header that can restrict JSON loading from external sources
- [ ] JSON encryption standard
- [ ] JSON validation policy

**Explanation:**
Content Security Policy is an HTTP header that helps prevent XSS attacks. It can restrict which sources can load JSON and other resources.

[Reference](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP)

#### Q178. What is the purpose of the `format` keyword in JSON Schema?

- [ ] To format output
- [x] To specify semantic validation for strings (email, uri, date, etc.)
- [ ] To format JSON
- [ ] To create formats

**Explanation:**
The `format` keyword provides semantic validation for string values, like "email", "uri", "date-time", "ipv4", etc.

[Reference](https://json-schema.org/understanding-json-schema/reference/string.html#format)

#### Q179. What is JSON Hyper-Schema?

- [ ] A hyperlinked JSON
- [x] An extension of JSON Schema for describing hypermedia APIs
- [ ] A JSON compression format
- [ ] A JSON validation tool

**Explanation:**
JSON Hyper-Schema extends JSON Schema to describe hypermedia APIs, including links and link relations.

[Reference](https://json-schema.org/draft/2019-09/json-schema-hypermedia.html)

#### Q180. What is the best practice for handling large JSON files?

- [ ] Load everything into memory
- [x] Use streaming parsers for large files
- [ ] Compress before parsing
- [ ] Split into multiple files

**Explanation:**
For large JSON files, streaming parsers (like SAX-style parsers) are recommended as they process the file incrementally without loading everything into memory.

[Reference](https://en.wikipedia.org/wiki/JSON_streaming)

#### Q181. In JSON, how do you represent a tab character in a string?

- [ ] \tab
- [x] \t
- [ ] \\t
- [ ] <tab>

#### Q182. What is JSON API (jsonapi.org)?

- [ ] A JSON validation tool
- [x] A specification for building APIs in JSON
- [ ] A JSON compression format
- [ ] A JSON encryption method

#### Q183. Which of the following is true about JSON and GraphQL?

- [ ] They are identical
- [x] GraphQL uses JSON for data exchange but provides a query language
- [ ] GraphQL cannot use JSON
- [ ] JSON is a replacement for GraphQL

#### Q184. What is the purpose of the "dependencies" keyword in JSON Schema?

- [ ] To define external dependencies
- [x] To specify property dependencies (if one property exists, others must too)
- [ ] To define package dependencies
- [ ] To create circular references

#### Q185. In JSON, what is the correct way to represent a carriage return in a string?

- [ ] \cr
- [x] \r
- [ ] \\r
- [ ] <cr>

#### Q186. What is the purpose of JSON Schema's "const" keyword?

- [ ] To define constants
- [x] To specify that a value must be exactly equal to the given value
- [ ] To define immutable properties
- [ ] To create constant arrays

#### Q187. Which of the following is a valid JSON boolean value?

- [ ] "true"
- [ ] TRUE
- [x] true
- [ ] 1

#### Q188. What is the purpose of the "multipleOf" keyword in JSON Schema?

- [ ] To define arrays
- [x] To specify that a number must be a multiple of the given value
- [ ] To define multiple properties
- [ ] To create multiplication operations

#### Q189. In JSON, how do you represent a form feed character in a string?

- [ ] \ff
- [x] \f
- [ ] \\f
- [ ] <ff>

#### Q190. What is JSON Merge Patch (RFC 7396)?

- [ ] A JSON compression method
- [x] A format for expressing partial modifications to a JSON document
- [ ] A JSON validation tool
- [ ] A JSON encryption method

#### Q191. Which of the following is true about JSON and REST APIs?

- [ ] REST APIs cannot use JSON
- [x] JSON is the most common format for REST API data exchange
- [ ] REST APIs must use XML
- [ ] JSON and REST are incompatible

#### Q192. What is the purpose of the "if", "then", "else" keywords in JSON Schema?

- [ ] To define conditional logic in data
- [x] To apply conditional validation based on property values
- [ ] To create if-else statements
- [ ] To define optional properties

#### Q193. In JSON, what is the maximum number of properties an object can have?

- [ ] 255
- [ ] 65,536
- [x] No defined maximum, depends on implementation
- [ ] 1 million

#### Q194. What is the purpose of JSON Schema's "propertyNames" keyword?

- [ ] To list all property names
- [x] To validate the names of properties in an object
- [ ] To define required properties
- [ ] To create property aliases

#### Q195. Which of the following is true about JSON and NoSQL databases?

- [ ] NoSQL databases cannot store JSON
- [x] Many NoSQL databases natively support JSON documents
- [ ] JSON is only for SQL databases
- [ ] NoSQL requires XML instead of JSON

#### Q196. What is the purpose of the "contentMediaType" keyword in JSON Schema?

- [ ] To define the data type
- [x] To specify the MIME type of string content
- [ ] To compress content
- [ ] To encrypt content

#### Q197. In JSON, how do you represent a backspace character in a string?

- [ ] \bs
- [x] \b
- [ ] \\b
- [ ] <bs>

#### Q198. What is JSON-LD Context?

- [ ] A JSON compression context
- [x] A way to map terms to IRIs in JSON-LD
- [ ] A JSON validation context
- [ ] A JSON encryption context

#### Q199. Which of the following is true about JSON and microservices?

- [ ] Microservices cannot use JSON
- [x] JSON is commonly used for inter-service communication in microservices
- [ ] Microservices require XML
- [ ] JSON is too slow for microservices

#### Q200. What is the purpose of the "contentEncoding" keyword in JSON Schema?

- [ ] To define character encoding
- [x] To specify the encoding used for string content (e.g., base64)
- [ ] To compress content
- [ ] To encrypt content

#### Q201. In JSON, what is the correct way to represent an empty string?

- [ ] null
- [x] ""
- [ ] { }
- [ ] [ ]

#### Q202. What is JSON Feed?

- [ ] A JSON compression feed
- [x] A format for syndicating content similar to RSS/Atom but using JSON
- [ ] A JSON validation feed
- [ ] A JSON encryption feed

#### Q203. Which of the following is true about JSON and WebSockets?

- [ ] WebSockets cannot transmit JSON
- [x] JSON is commonly used as the message format in WebSocket communication
- [ ] WebSockets require binary data only
- [ ] JSON and WebSockets are incompatible

#### Q204. What is the purpose of the "readOnly" keyword in JSON Schema?

- [ ] To define read-only files
- [x] To indicate that a property should not be modified by clients
- [ ] To create immutable objects
- [ ] To define constants

#### Q205. In JSON, which of the following is a valid way to represent NaN (Not a Number)?

- [ ] NaN
- [ ] "NaN"
- [ ] 0/0
- [x] JSON does not support NaN

#### Q206. What is JSON Resume?

- [ ] A JSON compression tool
- [x] A JSON-based standard for resumes
- [ ] A JSON validation tool
- [ ] A JSON encryption method

#### Q207. Which of the following is true about JSON and CORS?

- [ ] JSON prevents CORS issues
- [x] CORS policies apply to JSON API requests from browsers
- [ ] JSON bypasses CORS
- [ ] CORS only applies to XML

#### Q208. What is the purpose of the "writeOnly" keyword in JSON Schema?

- [ ] To define write-only files
- [x] To indicate that a property should not be returned in responses
- [ ] To create write-protected objects
- [ ] To define mutable properties

#### Q209. In JSON, what is the maximum depth of nested arrays?

- [ ] 10 levels
- [ ] 100 levels
- [x] No defined maximum, depends on implementation
- [ ] 1000 levels

#### Q210. What is JSON-stat?

- [ ] A JSON validation tool
- [x] A JSON format for statistical data dissemination
- [ ] A JSON compression format
- [ ] A JSON encryption method

#### Q211. Which of the following is true about JSON and caching?

- [ ] JSON cannot be cached
- [x] JSON responses can be cached using HTTP caching headers
- [ ] JSON requires special caching mechanisms
- [ ] Caching is disabled for JSON

#### Q212. What is the purpose of the "examples" keyword in JSON Schema?

- [ ] To define required examples
- [x] To provide sample values that validate against the schema
- [ ] To create example objects
- [ ] To validate examples

#### Q213. In JSON, how do you represent a Unicode character?

- [ ] \u{1F600}
- [x] \u1F600 (for BMP) or \uD83D\uDE00 (surrogate pair for non-BMP)
- [ ] &#x1F600;
- [ ] U+1F600

#### Q214. What is JSON Table Schema?

- [ ] A JSON compression format
- [x] A specification for describing tabular data in JSON
- [ ] A JSON validation tool
- [ ] A JSON encryption method

#### Q215. Which of the following is true about JSON and ETags?

- [ ] JSON doesn't support ETags
- [x] ETags can be used with JSON responses for cache validation
- [ ] ETags are only for HTML
- [ ] JSON requires special ETag handling

#### Q216. What is the purpose of the "deprecated" keyword in JSON Schema?

- [ ] To delete properties
- [x] To indicate that a property or schema is deprecated
- [ ] To remove validation
- [ ] To create legacy schemas

#### Q217. In JSON, what is the correct way to represent a literal backslash?

- [ ] \
- [x] \\
- [ ] \\\\
- [ ] /

#### Q218. What is JSON-LD Frame?

- [ ] A JSON compression frame
- [x] A way to shape JSON-LD data into a specific structure
- [ ] A JSON validation frame
- [ ] A JSON encryption frame

#### Q219. Which of the following is true about JSON and pagination?

- [ ] JSON doesn't support pagination
- [x] JSON APIs commonly implement pagination using metadata fields
- [ ] Pagination requires XML
- [ ] JSON automatically paginates data

#### Q220. What is the purpose of the "title" and "description" keywords in JSON Schema?

- [ ] To define the data type
- [x] To provide human-readable information about the schema
- [ ] To validate titles
- [ ] To create documentation

#### Q221. What is the maximum nesting depth recommended for JSON objects to maintain readability?

- [ ] 3 levels
- [ ] 5 levels
- [x] No strict limit, but 5-7 levels is generally recommended
- [ ] 10 levels

#### Q222. Which of the following is a valid JSON representation of a date?

- [ ] { "date": new Date() }
- [x] { "date": "2024-01-15T10:30:00Z" }
- [ ] { "date": Date.now() }
- [ ] { "date": 2024-01-15 }

#### Q223. What does the term "JSON serialization" refer to?

- [ ] Compressing JSON data
- [x] Converting an object or data structure into a JSON string
- [ ] Encrypting JSON data
- [ ] Validating JSON syntax

#### Q224. In JSON, what is the difference between `null` and `undefined`?

- [ ] They are identical
- [x] `null` is a valid JSON value, `undefined` is not
- [ ] `undefined` is a valid JSON value, `null` is not
- [ ] Both are invalid in JSON

#### Q225. What is JSON Pointer (RFC 6901) used for?

- [ ] Encrypting JSON data
- [x] Defining a string syntax for identifying a specific value within a JSON document
- [ ] Compressing JSON files
- [ ] Converting JSON to XML

#### Q226. Which HTTP status code typically indicates successful JSON API response?

- [ ] 201
- [x] 200
- [ ] 204
- [ ] 202

#### Q227. What is the purpose of JSON Web Encryption (JWE)?

- [ ] To compress JSON data
- [ ] To validate JSON structure
- [x] To encrypt JSON data for secure transmission
- [ ] To convert JSON to binary format

#### Q228. In a RESTful API, which HTTP method is typically used to send JSON data for creating a new resource?

- [ ] GET
- [x] POST
- [ ] PUT
- [ ] DELETE

#### Q229. What is the recommended Content-Type header for JSON API responses?

- [ ] text/json
- [x] application/json
- [ ] application/x-json
- [ ] text/plain

#### Q230. Which tool can be used to validate JSON schema compliance?

- [ ] JSONLint only
- [ ] ESLint
- [x] JSON Schema validators like Ajv
- [ ] JSHint

#### Q231. What is the purpose of the `$schema` keyword in JSON Schema?

- [ ] To define the data type
- [x] To specify which version of JSON Schema the schema follows
- [ ] To encrypt the schema
- [ ] To compress the schema

#### Q232. In JSON, how do you represent an empty object?

- [ ] { null }
- [x] {}
- [ ] { "" }
- [ ] { empty }

#### Q233. What is BSON?

- [ ] A JSON compression algorithm
- [x] Binary JSON, a binary-encoded serialization of JSON-like documents
- [ ] A JSON validation tool
- [ ] A JSON encryption method

#### Q234. Which of the following is true about JSON and JSONP?

- [ ] They are identical
- [x] JSONP is a technique for requesting data by loading a script tag
- [ ] JSONP is more secure than JSON
- [ ] JSON cannot be used in browsers

#### Q235. What is the maximum string length in JSON?

- [ ] 255 characters
- [ ] 65,536 characters
- [x] No defined maximum, depends on implementation
- [ ] 1 million characters

#### Q236. Which character encoding is required for JSON?

- [ ] ASCII
- [ ] ISO-8859-1
- [x] UTF-8 (or UTF-16/UTF-32)
- [ ] ANSI

#### Q237. What is the purpose of JSON Patch (RFC 6902)?

- [ ] To compress JSON files
- [x] To define a format for expressing a sequence of operations to apply to a JSON document
- [ ] To encrypt JSON data
- [ ] To convert JSON to XML

#### Q238. In JSON Schema, what does the "required" keyword specify?

- [ ] The data type of a property
- [x] Which properties must be present in the object
- [ ] The maximum value of a number
- [ ] The format of a string

#### Q239. What is the difference between JSON.stringify() and JSON.parse()?

- [x] stringify converts objects to strings, parse converts strings to objects
- [ ] They perform the same function
- [ ] stringify validates JSON, parse creates JSON
- [ ] parse converts objects to strings, stringify converts strings to objects

#### Q240. Which of the following is a valid way to include comments in JSON?

- [ ] // comment
- [ ] /_ comment _/
- [ ] # comment
- [x] JSON does not support comments

#### Q241. What is JSON5?

- [ ] The fifth version of JSON
- [x] An extension to JSON that allows comments and other JavaScript features
- [ ] A compression format for JSON
- [ ] A JSON validation tool

#### Q242. In JSON, what is the correct way to represent a boolean false value?

- [ ] "false"
- [ ] FALSE
- [x] false
- [ ] 0

#### Q243. What is the purpose of the "additionalProperties" keyword in JSON Schema?

- [ ] To define required properties
- [x] To specify whether properties not defined in the schema are allowed
- [ ] To set default values
- [ ] To define the data type

#### Q244. Which of the following is true about JSON and JavaScript objects?

- [ ] They are identical
- [x] JSON is a subset of JavaScript object literal notation
- [ ] JavaScript objects are a subset of JSON
- [ ] They are completely different

#### Q245. What is the purpose of JSON Web Signature (JWS)?

- [ ] To compress JSON data
- [x] To digitally sign JSON data to ensure integrity and authenticity
- [ ] To encrypt JSON data
- [ ] To validate JSON syntax

#### Q246. In a JSON API, what does the HTTP status code 400 typically indicate?

- [ ] Success
- [x] Bad Request (invalid JSON or request)
- [ ] Not Found
- [ ] Server Error

#### Q247. What is the recommended way to handle large numbers in JSON that exceed JavaScript's Number.MAX_SAFE_INTEGER?

- [ ] Use scientific notation
- [x] Represent them as strings
- [ ] Split them into multiple numbers
- [ ] Use hexadecimal format

#### Q248. Which of the following is a valid JSON array?

- [ ] [1, 2, 3,]
- [x] [1, 2, 3]
- [ ] [1; 2; 3]
- [ ] {1, 2, 3}

#### Q249. What is the purpose of the "enum" keyword in JSON Schema?

- [ ] To define numeric types
- [x] To restrict a value to a fixed set of values
- [ ] To enable enumeration of properties
- [ ] To define array types

#### Q250. In JSON, how do you represent a null value?

- [ ] "null"
- [ ] NULL
- [x] null
- [ ] undefined

#### Q251. What is JSON-RPC?

- [ ] A JSON compression protocol
- [x] A remote procedure call protocol encoded in JSON
- [ ] A JSON validation standard
- [ ] A JSON encryption method

#### Q252. Which of the following is true about JSON key names?

- [ ] They must be valid JavaScript identifiers
- [x] They must be strings enclosed in double quotes
- [ ] They can be numbers
- [ ] They can be boolean values

#### Q253. What is the purpose of the "$ref" keyword in JSON Schema?

- [ ] To define references to external files
- [x] To reference and reuse schema definitions
- [ ] To create circular references
- [ ] To define relationships between objects

#### Q254. In JSON, what is the correct way to escape a double quote character?

- [ ] '"'
- [x] \"
- [ ] ""
- [ ] `"`

#### Q255. What is the maximum size of a JSON document?

- [ ] 1 MB
- [ ] 10 MB
- [x] No defined maximum, depends on implementation and available memory
- [ ] 100 MB

#### Q256. Which of the following is a valid use case for JSON?

- [ ] Storing binary data
- [ ] Executing code
- [x] Data interchange between client and server
- [ ] Creating user interfaces

#### Q257. What is the purpose of JSON Schema's "format" keyword?

- [ ] To define the data type
- [x] To specify semantic validation for strings (e.g., email, uri, date-time)
- [ ] To format output
- [ ] To compress data

#### Q258. In JSON, which of the following represents an empty array?

- [ ] { }
- [x] [ ]
- [ ] null
- [ ] ""

#### Q259. What is the difference between JSON and XML?

- [ ] They are identical
- [x] JSON is more lightweight and easier to parse than XML
- [ ] XML is more lightweight than JSON
- [ ] JSON supports attributes, XML doesn't

#### Q260. What is the purpose of the "oneOf" keyword in JSON Schema?

- [ ] To define a single property
- [x] To validate that data matches exactly one of the specified schemas
- [ ] To define optional properties
- [ ] To create unions of types

#### Q261. In JSON, how do you represent scientific notation?

- [ ] 1.5 \* 10^3
- [x] 1.5e3
- [ ] 1.5E+3 only
- [ ] Scientific notation is not supported

#### Q262. What is JSON Lines (JSONL)?

- [ ] A JSON compression format
- [x] A format where each line is a valid JSON value
- [ ] A JSON validation tool
- [ ] A JSON encryption method

#### Q263. Which HTTP header should be set when sending JSON data in a request?

- [ ] Accept: application/json
- [x] Content-Type: application/json
- [ ] Content-Encoding: json
- [ ] Transfer-Encoding: json

#### Q264. What is the purpose of JSON Schema's "allOf" keyword?

- [ ] To define all required properties
- [x] To validate that data matches all of the specified schemas
- [ ] To define all possible values
- [ ] To create arrays

#### Q265. In JSON, what is the correct way to represent a negative number?

- [ ] "-5"
- [x] -5
- [ ] (-5)
- [ ] minus 5

#### Q266. What is the purpose of the "default" keyword in JSON Schema?

- [ ] To define the data type
- [x] To specify a default value if the property is not present
- [ ] To define required properties
- [ ] To validate the schema

#### Q267. Which of the following is true about JSON and YAML?

- [ ] They are identical
- [x] YAML is a superset of JSON (all JSON is valid YAML)
- [ ] JSON is a superset of YAML
- [ ] They are completely incompatible

#### Q268. What is the purpose of JSON Schema's "anyOf" keyword?

- [ ] To define any data type
- [x] To validate that data matches at least one of the specified schemas
- [ ] To define optional properties
- [ ] To create arrays

#### Q269. In JSON, how do you represent a decimal number?

- [ ] "3.14"
- [x] 3.14
- [ ] 3,14
- [ ] 3.14f

#### Q270. What is the purpose of JSON Schema's "not" keyword?

- [ ] To define null values
- [x] To validate that data does NOT match the specified schema
- [ ] To negate boolean values
- [ ] To define optional properties

#### Q271. Which of the following is a valid JSON number?

- [ ] 0x1F
- [ ] 077
- [x] 31
- [ ] 31L

#### Q272. What is the purpose of the "minLength" and "maxLength" keywords in JSON Schema?

- [ ] To define array sizes
- [x] To specify minimum and maximum string lengths
- [ ] To define number ranges
- [ ] To define object sizes

#### Q273. In JSON, what is the correct way to represent an object with no properties?

- [ ] null
- [x] {}
- [ ] { "" }
- [ ] undefined

#### Q274. What is JSON Hyper-Schema?

- [ ] A JSON compression format
- [x] An extension of JSON Schema for defining hypermedia APIs
- [ ] A JSON validation tool
- [ ] A JSON encryption method

#### Q275. Which of the following is true about JSON property order?

- [ ] Properties must be in alphabetical order
- [x] JSON objects are unordered collections of key-value pairs
- [ ] Properties must be in the order they were defined
- [ ] JSON requires a specific property order

#### Q276. What is the purpose of the "minimum" and "maximum" keywords in JSON Schema?

- [ ] To define string lengths
- [x] To specify minimum and maximum numeric values
- [ ] To define array sizes
- [ ] To define date ranges

#### Q277. In JSON, which of the following is a valid way to represent infinity?

- [ ] Infinity
- [ ] "Infinity"
- [ ] 1/0
- [x] JSON does not support infinity

#### Q278. What is the purpose of JSON Schema's "pattern" keyword?

- [ ] To define design patterns
- [x] To specify a regular expression that a string must match
- [ ] To define repeating structures
- [ ] To create templates

#### Q279. Which of the following is true about JSON and MongoDB?

- [ ] MongoDB stores data in JSON format
- [x] MongoDB stores data in BSON (Binary JSON) format
- [ ] MongoDB cannot work with JSON
- [ ] JSON and BSON are identical

#### Q280. What is the purpose of the "uniqueItems" keyword in JSON Schema?

- [ ] To define unique object properties
- [x] To specify that all items in an array must be unique
- [ ] To create unique identifiers
- [ ] To validate unique keys

#### Q281. What is the purpose of JSON-P (JSON with padding) in web development, and how is it typically used?

- [ ] A. To validate JSON data before parsing it in JavaScript.
- [ ] B. To provide additional padding for JSON objects to improve readability.
- [x] C. To overcome the same-origin policy limitation when making cross-domain AJAX requests.
- [ ] D. To compress JSON data for faster transmission over the network.

#### Q282. In a JSON document, how can you represent a key that contains special characters, such as spaces or hyphens, to ensure proper parsing and access in JavaScript?

- [ ] A. Wrap the key in single quotes.
- [ ] B. Enclose the key in square brackets.
- [ ] C. Use backslashes before special characters.
- [x] D. Enclose the key in double quotes.

