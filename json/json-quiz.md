Q1. By convention, what name is used for the first key in a JSON schema?
- schema
- $schema <<<<----Correct
- JsonSchema
- JSONschema


Q2. Which code is the closest JSON equivalent of the data shown?
- {
    "red",
    "blue",
    "green"
  }
- { <<<<----Correct
    "color": "red",
    "color": "blue",
    "color": "green"
  }

- {
    'red': 'red',
    'blue': 'blue',
}


Q3. Which JavaScript method converts a JavaScript value to Json?
- JSON.parse()
- JSON.stringify() <<<<----Correct
- JSON.toString()
- JSON.objectify()


Q4. Wich data type is NOT part of JSON standard?
- string
- number
- date <<<<----Correct
- array


Q5. Which term is commonly used to refer to converting data to JSON?
- unpacking
- serialization
- deserialization
- parsing <<<<----Correct


Q6. Which code uses the correct JSON syntax to encode the key/value pari shown?
```
accountNum: '000605802'
```
- "accountNum": "00060504" <<<<----Correct
- accountNum: "00060504"
- "accountNum": 00060504
- accountNum: 00060504


Q7. What character do you specify before a JSON control character when you want to use that control characters as a literal part of a string?
- /
- \ <<<<----Correct
- :
- {


Q8. Which date type is part of the JSON standard?
- Boolean <<<<----Correct
- map
- promise
- function


Q9. Which key name is used to specify properties that must be included for JSON to be valid?
- important
- base
- core
- required <<<<----May be


Q10. Which is the valid JSON equivalent of the data shown?
- { <<<<----Correct
    "photo": {
        "width": 1600,
        "hight": 900,
        "binaries": {
            "url": "https://....."
            "thumbernail": "https://....."
        },
        "animated": false,
        "tags": [116, 943, 234, 38793]
    }
}


Q11. How do you store several paragraphs of text as a string in JSON?
- Escape all whitespaces expet space characters.
- Escape line breaks.
- Escape paragraps. <<<<----Correct
- Remove all whitesapces


Q12. What data type is represented by the value of the key/value pair shown?
```
loggedIn: true
```
- string
- Boolean <<<<----Correct
- number
- object


Q13. If you need to store the loggedin status of a user in JSON as a boolean, what is the correct syntax?
- "loggedIn": (true)
- loggedIn: "true"
- "loggedIn": true <<<<----Correct
- loggedIn: {true}


Q14. What does JSON with padding (JSON-P) use to make a request?
- an <origin> element
- a header request 
- the <script> element <<<<----Correct
- the XMLHttpRequest object


Q15. Which value is supported in the JSON specifications?
- undefined
- infinity
- NaN
- null <<<<----Correct


Q16. Which JavaScript method converts a Json to JavaScript value?
- JSON.parse() <<<<----Correct
- JSON.stringify()
- JSON.toString()
- JSON.objectify()

Q17. Transferring JSON information from client to server and back again often includes HTTP requests. Match each method with the best choice describing its use.

    1.Sends data to spesific server to create or update information.

    2.Sends data to spesific server to create or update information without the risk of creating the resource more than once.

    3.Previews what the GET request response might be without the body of the text.

    4.Learns the communication channels used by the target source.

    5.Requests information from a spesific source.

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
