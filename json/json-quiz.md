#### Q1. By convention, what name is used for the first key in a JSON schema?

- schema
- \$schema <<<<----Correct
- JsonSchema
- JSONschema

#### Q2. Which code is the closest JSON equivalent of the data shown?

```
[
	'red',
	'blue',
	'green'
]
```

- ```
  [
    "red",
    "blue",
    "green"
  ]
  ```

  <<<<----Correct

- ```
  {
    "color": "red",
    "color": "blue",
    "color": "green"
  }
  ```

- ```
  {
    'red': 'red',
    'blue': 'blue',
  }
  ```

#### Q3. Which JavaScript method converts a JavaScript value to Json?

- JSON.parse()
- JSON.stringify() <<<<----Correct
- JSON.toString()
- JSON.objectify()

#### Q4. Which data type is NOT part of JSON standard?

- string
- number
- date <<<<----Correct
- array

#### Q5. Which term is commonly used to refer to converting data to JSON?

- unpacking
- serialization <<<<----Correct
- deserialization
- parsing

#### Q6. Which code uses the correct JSON syntax to encode the key/value pair shown?

```

accountNum: '000605802'

```

- "accountNum": "00060504" <<<<----Correct
- accountNum: "00060504"
- "accountNum": 00060504
- accountNum: 00060504

#### Q7. What character do you specify before a JSON control character when you want to use that control characters as a literal part of a string?

- /
- \ <<<<----Correct
- :
- {

#### Q8. Which date type is part of the JSON standard?

- Boolean <<<<----Correct
- map
- promise
- function

#### Q9. Which key name is used to specify properties that must be included for JSON to be valid?

- important
- base
- core
- required <<<<----Correct

#### Q10. Which is the valid JSON equivalent of the data shown? \*\*\* MISSING OPTIONS & "DATA SHOWN"

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

- ```
  {
  	'photo': {
  	'width': 1600,
  	'height': 900,
  	'binaries': {
  	'url': 'https://www.example.com/images/34097349843',
  	'thumbnail': 'https://www.example.com/images/thumbs/34097349843'
  	},
  	'animated': 'false',
  	'tags': [116, 943, 234, 38793],
  	}
  }
  ```

- ```
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

- ```
  {
  	"photo": {
  	"width": 1600,
  	"height": 900,
  	"binaries": {
  	"url": "https://www.example.com/images/34097349843",
  	"thumbnail": "https://www.example.com/images/thumbs/34097349843"
  	},
  	"animated": false,
  	"tags": [116, 943, 234, 38793],
  	}
  }
  ```

  <<<<--- Correct

- ```
  {
  	"photo": {
  	"width": "1600",
  	"height": "900",
  	"binaries": {
  	"url": "https://www.example.com/images/34097349843",
  	"thumbnail": "https://www.example.com/images/thumbs/34097349843"
  	},
  	"animated": "false",
  	"tags": ["116", "943", "234", "38793"],
  	}
  }
  ```

#### Q11. How do you store several paragraphs of text as a string in JSON?

- Escape all whitespaces expect space characters. <<<<----Correct
- Escape line breaks.
- Escape paragraphs.
- Remove all whitespaces

#### Q12. What data type is represented by the value of the key/value pair shown?

```

loggedIn: true

```

- string
- Boolean <<<<----Correct
- number
- object

#### Q13. If you need to store the loggedin status of a user in JSON as a boolean, what is the correct syntax?

- "loggedIn": (true)
- loggedIn: "true"
- "loggedIn": true <<<<----Correct
- loggedIn: {true}

#### Q14. What does JSON with padding (JSON-P) use to make a request?

- an <origin> element
- a header request
- the <script> element <<<<----Correct
- the XMLHttpRequest object

#### Q15. Which value is supported in the JSON specifications?

- undefined
- infinity
- NaN
- null <<<<----Correct

#### Q16. Which JavaScript method converts a Json to JavaScript value?

- JSON.parse() <<<<----Correct
- JSON.stringify()
- JSON.toString()
- JSON.objectify()

#### Q17. Transferring JSON information from client to server and back again often includes HTTP requests. Match each method with the best choice describing its use.

    1.Sends data to specific server to create or update information.

    2.Sends data to specific server to create or update information without the risk of creating the resource more than once.

    3.Previews what the GET request response might be without the body of the text.

    4.Learns the communication channels used by the target source.

    5.Requests information from a specific source.

    6.Removes information.

- 1.POST
  2.DELETE
  3.OPTIONS
  4.HEADER
  5.GET
  6.PUT

- 1.POST
  2.PUT
  3.HEADER
  4.OPTIONS
  5.GET
  6.DELETE

- 1.POST
  2.DELETE
  3.OPTIONS
  4.HEADER
  5.GET
  6.PUT

- 1.POST
  2.PUT
  3.HEADER
  4.OPTIONS
  5.GET
  6.DELETE <<<<----Correct

#### Q18. Which code uses valid JSON syntax for the text "Centennial Olympics?

-{
"host": "Atlanta",
"year": 1996
/_ Centennial Olympics _/
}
-{
"host": "Atlanta",
"year": 1996,
/_ Centennial Olympics _/
}
-{
"host": "Atlanta",
"year": 1996
// Centennial Olympics
}
-{
"host": "Atlanta",
"year": 1996,
"comments": "Centennial Olympics" <<<<----Correct
}

#### Q19. Can trailing commas be used in objects and arrays?

- yes
- only if there is more than one item
- no <<<<----Correct
- only when arrays and objects contain more than 10 items

#### Q20. Which whitespace characters should be escaped within a string?

- All whitespace is allowed.
- double quotes, slashes new lines, and carriage returns
- new lines and carriage returns only <<<<----Correct
- double quotes only

#### Q21. Which is supported by YAML but not supported by JSON?

- nested
- comments <<<<----Correct
- arrays
- null values

#### Q22. Which is an invalid JSON value?

- "'|=(_)(X 72(_)|\/||\*'"
- "|=(_)(X 72(_)|\/||\*"
- "|=(_)(X\" \"72(_)|\/||\*"
- "\s(_)(X 72(_)|\/||\*" <<<<----Correct

#### Q23. How do you encode a date in JSON?

- Convert the date to UTC and enclose in quotes.
- Encode the date as string using the ISO-8601 date format. <<<<----Correct
- Wrap the date in double quotes.
- Add a "date" key to your object and include the date as string.

#### Q24. What’s wrong with this JavaScript?

JSON.parse({"first": "Sarah", "last": "Connor"}) ;

- JSON should be wrapped with curly braces.
- JSON.parse() is missing an argument.
- The value supplied to JSON.parse() is not a string. <<<<----Correct
- Nothing is wrong with it.

#### Q25. What does this JavaScript code print?

printNullness(JSON.parse('{ "lemmings": [] }'));
printNullness(JSON.parse('{ "lemmings": null }'));
printNullness(JSON.parse('{ "lemmings": "null" }'));

    function printNullness(){
      if (testMe.lemmings == null)
        console.log("null");
      else
        console.log("not null");
    }

- not null <<<<----Correct
  null
  not null

- null
  null
  not null
- not null
  null
  null
- null
  null
  null

#### Q26. What tool might you use to validate your JSON?

- JSONLint <<<<----Correct
- ValidateJSON
- JSONFiddle
- TextEdit

#### Q27. What characters denote strings in JSON?

- double quotes <<<<----Correct
- smart (curly) quotes
- single or double quotes
- single quotes

#### Q28. Which code is a valid JSON equivalent of the key/value pair shown that also preserves the data type?

**constant: 6.022E23**

- "constant": "6.022E23" <<<<----Correct
- "constant": "6\.022\E23"
- constant: 6.022E23
- constant: "6.022E23"

(\*\*\*note it should be mentioned that Scientific Notation is a valid JSON number. You can use `e` or `E`. https://json-schema.org/understanding-json-schema/reference/numeric.html)

#### Q29. Which element is added to the DOM to create a JSON-P request?

- `<object>`
- `<script>` <<<<----Correct
- `<json>`
- `<meta>`

#### Q30. Why do so many APIs use JSON?

- Because it's object-based.
- Because it's a simple and adaptable format for sharing data.
- Because it's based on JavaScript. <<<<----Correct
- Because it is derived from SGML.

#### Q31. You need to assemble a list of members, but your JSON is not parsing correctly. How do you change it?

**{
"avengers": [
"iron man",
"hulk",
"thor",
"black widow",
"ant man",
"spider man'
]
}**

- **{
  "avengers": [
  "iron man",
  "hulk",
  "thor",
  "black widow",
  "ant man",
  "spider man"
  ]
  }** <<<<----Correct

- **{
  'avengers': [
  {'iron man',
  'hulk',
  'thor',
  'black widow',
  'ant man',
  'spider man'}
  ]
  }**

- **{
  'avengers': [
  'iron man',
  'hulk',
  'thor',
  'black widow',
  'ant man',
  'spider man'
  ]
  }**

- **{
  "avengers": {[
  "iron man",
  "hulk",
  "thor",
  "black widow",
  "ant man",
  "spider man"
  ]}
  }**

#### Q32. When building dynamic web applications using AJAX, developers originally used the \_\_\_\_ data format, which has since been replaced by JSON.

- XML <<<<----Correct
- GRAPHQL
- REST
- SOAP

#### Q33. How is a true boolean value represented in JSON?

- TRUE
- "true"
- 1
- true <<<<----Correct

#### Q34. Which array is valid JSON?

- ['tatooine', 'hoth', 'dagobah']
- [tatooine, hoth, dagobah]
- ["tatooine", "hoth", "dagobah",]
- ["tatooine", "hoth", "dagobah"] <<<<----Correct

#### Q35. What data type is encoded in the outermost component of the JSON shown?

[
{
"year": 2024
},
{
"location": "unknown"
}
]

- object
- array <<<<----Correct
- number
- string

#### Q36. Which is ignored by JSON but treated as significant by YAML?

- trailing commas
- trailing decimals
- whitespace
- leading zeroes <<<<----Correct

#### Q37. When you need to set the value of a key in JSON to be blank, what is the correct syntax for the empty value?

- FALSE
- 0
- ""
- null <<<<----Correct

#### Q38. How do you assign a number value in JSON?

- Escape the number with a backslash.
- Enclose the number in double quotes.
- Enclose the number in single quotes.
- Leave the number as is. <<<<----Correct

#### Q39. Which code uses the correct JSON syntax for encoding a key/value pair with a null value?

- "lastVisit": "nul1"
- lastVisit: null
- "lastVisit": 0
- "lastVisit": undefined
  **NONE OF THESE ARE CORRECT A CORRECT ANSWER WOULD LOOK LIKE `"lastVisit": null`**

#### Q40. Which reference to the Unicode character U+1F602 complies with the JSON standard?

- 128514
- d83dde02
- \uD83D\uDE02 <<<<----Correct
- \&#128514;

#### Q41. Which code uses the correct JSON syntax for a key/Value pair containing a string?

- "largest": "blue whale" <<<<----Correct
- largest: 'blue whale'
- 'largest': 'blue whale'
- largest: "blue whale"

#### Q42. Which key name is used to specify data type in a JSON schema?

- data
- schemadata
- schematype
- type <<<<----Correct

#### Q43. Which code is a valid JSON equivalent of the key/value pair shown that also preserves the original value?

**UPC: 043875**

- "UPC": \043875
- UPC: "043875"
- "UPC": 043875
- UPC: '043875'
  **NONE OF THESE ARE CORRECT A CORRECT ANSWER WOULD LOOK LIKE `"UPC": "043875"`**

#### Q44. Which data format is a JSON schema written in?

- markdown
- YAML
- XML
- JSON <<<<----Correct

#### Q45. Which code is valid JSON equivalent of the key/value pair shown that also preserves the data type?

**variance: -0.0823**

- "variance": "-0.0823" <<<<----Correct
- variance: "-0.0823"
- "variance": "\-0.0823"
- variance: -0.0823

#### Q46. With what character should key/value pairs be separated?

- colon <<<<----Correct
- space
- semicolon
- comma

#### Q47. What character separates keys from values?

- `:`
- `->`
- `::`
- `.` <<<<---- Correct
