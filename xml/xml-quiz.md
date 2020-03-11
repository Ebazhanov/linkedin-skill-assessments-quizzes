XML Assessment
-----------------

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

- `doc("cars.xml")/cars/car[year>2000].data`
- `doc("cars.xml")/cars/car[xs:integer(year) gt 2000]`
- `doc("cars.xml")/cars/car[year gt 2000]`
- `doc("cars.xml")/cars/car[integer(year) > 2000]`

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

- The `<car>` element can be extended with only one attribute
