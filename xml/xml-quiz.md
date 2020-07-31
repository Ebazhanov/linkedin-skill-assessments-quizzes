## XML Assessment

#### Q1. You are working with this XML code snippet from the XML document cars.xml. You need to return the information about the cars built after the year 2000. What does your XQuery look like?

```xml
<cars>
    <car><make>Cadillac</make><model>Escalade</model><year>2007</year></car>
    <car><make>Cadillac</make><model>Escalade</model><year>2011</year></car>
    <car><make>Ford</make><model>Mustang</model><year>1968</year></car>
    <car><make>Ford</make><model>Mustang</model><year>1998</year></car>
    <car><make>Mercedes</make><model>C-Class</model><year>1999</year></car>
    <car><make>Mercedes</make><model>C-Class</model><year>2009</year></car>
</cars>
```

- [x] `doc("cars.xml")/cars/car[year>2000].data`
- [ ] `doc("cars.xml")/cars/car[xs:integer(year) gt 2000]`
- [ ] `doc("cars.xml")/cars/car[year gt 2000]`
- [ ] `doc("cars.xml")/cars/car[integer(year) > 2000]`

#### Q2. You are working with the following XSD fragment. What does it say about the `<car>` element?

```xml
<xs:element name="car">
    <xs:complexType>
        <xs:sequence>
            <xs:element name="make" type="xs:string"/>
            <xs:element name="model" type="xs:string"/>
            <xs:element name="year" type="xs:string"/>
        </xs:sequence>
        <xs:anyAttribute/>
    </xs:complexType>
</xs:element>
```

- [ ] The `<car>` element can be extended with only one attribute
- [ ] The `<car>` element can be extended with multiple attributes
- [ ] The `<car>` element have any attributes
- [ ] The `<car>` element has child elements which can appear in order

#### Q3. You are converting your HTML file into XHTML Strict. Which code snippet will validate without errors?

- [ ] Option 1

```xml
<html xmlns="http://www.w3.org/1999/xhtml">
    <head><title>XHTML Example</title></head>
    <body bgcolor="#FFFFFF" >
        <p>Content goes here ...</p>
    </body>
</html>
```
- [ ] Option 2

```xml
<html xmlns="http://www.w3.org/1999/xhtml">
    <head><title>XHTML Example</title></head>
    <body name="bodySection">
        <p><b>Content goes here ...</b></p>
    </body>
</html>
```

- [ ] Option 3

```xml
<html xmlns="http://www.w3.org/1999/xhtml">
    <head><title>XHTML Example</title></head>
    <body color="#333333">
        <p><i>Content goes here ...</i></p>
    </body>
</html>
```
- [x] Option 4

```xml
<html xmlns="http://www.w3.org/1999/xhtml">
    <head><title>XHTML Example</title></head>
    <body id="bodySelection">
        <p><strong>Content goes here ...</strong></p>
    </body>
</html>
```

#### Q4. When working with Ajax applications, which is faster, XML or JSON?

- [ ] XML, because it is extensible
- [x] JSON, because it transfers data without waiting for a sever response
- [ ] XML, because it supports namespaces
- [ ] JSON, because it is already parsed into a JavaScript object

#### Q5. Asynchronous Javascript and XML (Ajax) is technique for creating better, faster, and more interactive web applications. In addition to JavaScript and XML on the back end, which technologies are commonly used to craft AJAX experiences on the front end?

- [ ] PHP, .NET, and SQL
- [x] HTML, CSS, and DOM
- [ ] Python, Perl, and C++
- [ ] Java, ASP, and C#

#### Q6. What is this code an example of?

```xml
<x/>
```

- [ ] null element 
- [x] self-closing tag
- [ ] improperly named element
- [ ] incorrect XML syntax

#### Q7. Which XHTML syntax rule does NOT apply to XML?

- [x] XHTML attribute values must be quoted
- [ ] XHTML tags and attributes must be in lowercase
- [ ] XHTML elements must be properly nested within each other.
- [ ] XHTML tags must have an equivalent closing tag.

#### Q8. Which Ajax method is used to exchange data with a server, using a modern browser?

- [ ] request-XML
- [x] XMLHttRequest
- [ ] ActiveXObject
- [ ] responseXML

#### Q9. A markup language is a _____-readable language that ___ text so that the computer can ___ that text.

- [ ] processor; complies; process
- [ ] system; stores; retrieve
- [ ] non; processes; format
- [x] human; annotates; manipulate

#### Q10. What is this code an example of?

```xml
<x a="x" a="y"></x>
```

- [x] improperly named element
- [ ] self-closing tag
- [ ] null element
- [ ] incorrect XML syntax

#### Q11. XML provides a framework for specifying markup languages, while HTML is a predefined markup language. What is applicable to XML and not HTML?

- [x] It is mandatory to use closing tags with XML
- [ ] It is important for an XML document to be well formed
- [ ] XML elements start with an opening tag in angle brackets, such as `<p>`
- [ ] XML syntax uses tags, elements, and attributes

#### Q12. What is the last step in extending XHTML modules?

- [ ] The last step is to complete the extension of XHTML compound documents and make sure the documents and make sure the documents adhere to the defined namespaces.
- [x] The last step is to create the DTD for the XHTML extension, which references both the XHTML modules and the new modules.
- [ ] The last step is to run the XHTML extension through the XSLT processor, which will properly format it.
- [ ] The last step is to verify that the XHTML is well formed and valid, and compatible with most browsers.

#### Q13. In an XML DTD ATTLIST declaration, which default value is used to indicate that the attribute does not have to be included?

- [x] `#DEFAULT`
- [ ] `#OPTIONAL`
- [ ] `#IMPLIED`
- [ ] `#FIXED`

#### Q14. How does the XML DOM present an XML document?
- [ ] as a set of objects
- [x] as a tree structure
- [ ] as an array of nodes 
- [ ] as a dynamic program

#### Q15. You are working with an XML document that uses an XML schema. How do you specify that an element can appear multiple times inside its parent elemen t?
- [ ] Set the maxOccurs attribute to a large number, such as 1.000
- [ ] Set the maxOccurs attribute to 0
- [ ] Set the maxOccurs attribute to undefined.
- [x] Set the maxOccurs attribute to unbounded.
