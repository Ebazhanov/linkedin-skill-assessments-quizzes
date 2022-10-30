## C++

#### Q1. Betrachten Sie diese Funktionsdeklaration von `is_even`, die einen ganzzahligen Wert nimmt und "wahr" zurückgibt, wenn das Argument eine gerade Zahl ist, ansonsten "falsch". Welche Deklarationen sind korrekt für überladene Versionen dieser Funktion, um auch Gleitkomma- und String-Darstellungen von Zahlen zu unterstützen?

```cpp
bool is_even(int);
```

- [x] A

```cpp
bool is_even(float f);
bool is_even(char *str);
```

- [ ] B

```cpp
bool is_even(float f);
bool is_even(char str);
```

- [ ] C

```cpp
bool is_even_float(float f);
bool is_even_str(char *str);
```

- [ ] D

```cpp
float is_even(float f);
char *is_even(char *str);
```

#### Q2. Was gibt dieser Code aus?

```cpp
int c=3; char d='A';
std::printf("c is %d and d is %c",c,d);
```

- [ ] c is d and d is c
- [ ] c is A and d is 3
- [x] c is 3 and d is A
- [ ] c is c and d is d

#### Q3. Welcher ternäre Operator entspricht diesem Codestück?

```cpp
if(x)
    y=a;
else
    y=b;
```

- [ ] `y=a?b:x;`
- [ ] `y=if(x?a:b);`
- [ ] `y=(x&a)?a:(x&b)?b:0;`
- [x] `y=x?a:b;`

#### Q4. Warum ist diese Codezeile schlechter Programmierstil?

`using namespace std;`

- [ ] Wenn der Code eine Funktion aufruft, die in zwei verschiedenen Bibliotheken mit demselben Prototypen, aber womöglich unterschiedlichen Implementierungen definiert ist, tritt wegen Mehrdeutigkeit ein Kompilierfehler auf.
- [ ] Sie bindet automatisch alle Headerdateien in die Standardbibliothek ein (cstdint, cstdlib, cstdio, iostream usw.).
- [ ] Sie veranlasst den Compiler dazu zu erzwingen, dass ausschließlich Headerdateien aus der Standardbibliothek eingebunden werden, und führt zu Kompilierfehlern, wenn eine andere Headerdatei eingebunden wird.
- [ ] Der kopilierte Code ist wegen all der importierten Symbole immer größer.

#### Q5. Welche Aktion führt der Operator ^ aus?

- [ ] Er berechnet das bitweise xor zwischen seinen Operanden.
- [ ] Er berechnet das logische xor zwischen seinen Operanden.
- [ ] Er nimmt die linke Seite des Operators hoch der Potenz auf der rechten Seite des Operators.
- [ ] Er tut zweierlei: Er deklariert einen Zeiger und dereferenziert einen Zeiger.

#### Q6. Welchen Speicher belegt u1?

```cpp
union {
    unit16_t a;
    unit32_t b;
    int8_t c;
} u1;
```

- [x] 4 Bytes
- [ ] 7 Bytes
- [ ] 8 Bytes
- [ ] 2 Bytes

[Referenz](https://en.cppreference.com/w/cpp/language/union)

#### Q7. Was gibt dieses Programm aus?

```cpp
#include <iostream>
char str[20]="Hi, there!";
int main(){
    char *p=&str[4];
    std::count<<*p++;
    std::count<<p;
    return 0;
    }
```

- [ ] tthere!
- [ ] uhere!
- [ ] there!
- [ ] tuhere!

#### Q8. Wie könnte eine gültige Überladung für den ternären Bedingungsoperator erreicht werden?

- [ ] void\* operator conditional(const bool cond, const void& iftrue, const void& iffalse);
- [ ] void& operator ?:(const bool cond, const void& iftrue, const void& iffalse);
- [x] Der ternäre Operator kann nicht überladen werden.
- [ ] void* operator ?:(const bool cond, const void* iftrue, const void\* iffalse);

#### Q9. Welche Option zeigt den Inhalt der Vektoren, auf die v1 und v2 zeigen, nach der Ausführung dieses Codes?

```cpp
std:: vector<int> *v1 = new std::vector<int>({1,2,3});
std:: vector<int> *v2;
v2=v1;
v1->push_back(4);
v2->push_back(5);
```

- [ ] `*v1:{1,2,3,4}; *v2:{5};`
- [x] `*v1:{1,2,3,4,5}; *v2:{1,2,3,4,5};`
- [ ] Error
- [ ] `*v1:{1,2,3,4}; *v2:{1,2,3,5};`

v1 und v2 zeigen auf denselben Vektor.

#### Q10. Wie rufen Sie korrekt die Mitgliedfunktion count für den Objektzeiger grades auf?

```cpp
class my_array{
    public:
        int count();
};  // ... weitere Member darüber

int main(){
    my_array *grades = new my_array();
};  // ... weitere Code darüber
```

- [ ] `grades.count();`
- [ ] `my_array->count();`
- [x] `grades->count();`
- [ ] `my_array.count();`

#### Q11. Was ist der Zweck eines Konstrukteurs?

- [x] Damit kann beim Programmieren der nötige Code geschrieben werden, um die vom Objekt belegten Ressourcen freizugeben, bevor das Objekt selbst gelöscht wird.
- [ ] Er löscht ein Object. Ein Beispiel eines Zerstörers ist die Funktion `delete()`
- [ ] Er beendet ein Programm. Das kann mit einem regulären Funktionsaufruf oder mit einer Ausnahme erreichen werden.
- [ ] Es gibt keine Zerstörer in C++.

#### Q12. Was ist eine geeignete Weise, um `my_object` wie unten gezeigt zu entfernen?

```cpp
my_class *my_object = new my_class();
```

- [x] `delete(my_object);`
- [ ] `free(my_object);`
- [ ] Der Speicherbereiniger wird das Object irgendwann zerstören.
- [ ] Das Object wird zerstört, wenn der Gültigkeitsbereich verlassen wird.

#### Q13. Warum ist es nicht möglich, ein Array von Verweisen, einen Zeiger auf einen Verweis oder einen Verweis auf einen Verweis zu deklarieren?

- [ ] Verweise sind Zeiger und keiner der genannten Typen ist für Zeiger sinnvoll.
- [ ] Tatsächlich ist das möglich, aber diese Typen müssen bei der Deklaration als `const` oder `volatile` spezifiziert werden.
- [ ] Verweise sind weder Objekte noch Variablen, daher ist nicht garantiert, dass sie Speicher belegen und eine Adresse haben.
- [ ] Verweise müssen initialisiert werden, damit sie bei der Deklaration auf ein gültiges Objekt oder eine gültige Funktion verweisen.

#### Q14. Welche Aussage über die Variable `ptr` ist wahr?

```cpp
void *ptr;
```

- [ ] Sie ist ein mit NULL initialisierter Zeiger.
- [ ] Sie ist ein Zeiger auf eine Void-Funktion.
- [ ] Diese Deklaration verursacht einen Kompilierfehler, weil Zeiger immer einen Typ angeben müssen.
- [x] Da sie ein Zeiger auf einen Wert ohne spezifischen Typ ist, kann sie per Typumwandlung als Zeiger auf jeden Typ genutzt werden.

#### Q15. Wie kann C++-Code eine C-Funktion aufrufen?

- [ ] durch Verwendung von extern "C"
- [ ] indem er den C-Quellcode importiert
- [ ] Es gibt keine Möglichkeit, mit C++ eine C-Funktion aufzurufen.
- [ ] indem er einfach den C-Code aufruft

#### Q16. What is a class template?

- [x] It’s a class written with the generic programming, specifying behavior in terms of type parameter rather than specific type.
- [ ] It’s a blank superclass intended for inheritance and polymorphism.
- [ ] It’s class that only consists of member variable, with no constructor, destructor nor member functions.
- [ ] It’s skelton source code for a class where the programmer has to fill in specific parts to define the data types and algorithms used.

[References](https://www.ibm.com/docs/en/zos/2.2.0?topic=only-class-templates-c)
