## C++

#### F1. Was ist die Ausgabe dieses Codes?

```cpp
vector<int> v(22);
bool b = (v[6]);
printf("%d", !b);
```

- [ ] False
- [ ] 0
- [x] 1
- [ ] Dieser Code hat einen Fehler.

#### F2. Welcher der folgenden Gründe spricht dafür, dass die Verwendung dieser Zeile als schlechte Praxis gilt? (_Alternative_: Warum gilt die Verwendung dieser Zeile als schlechte Praxis?)

```cpp
using namespace std;
```

- [ ] Der kompilierte Code ist immer größer wegen all der importierten Symbole.
- [x] Wenn der Code eine Funktion verwendet, die in zwei verschiedenen Bibliotheken mit demselben Prototyp, aber möglicherweise unterschiedlichen Implementierungen definiert ist, wird es einen Kompilierfehler aufgrund von Mehrdeutigkeit geben.
- [ ] Es werden automatisch alle Header-Dateien der Standardbibliothek eingebunden (cstdint, cstdlib, cstdio, iostream, etc.).
- [ ] Es veranlasst den Compiler, die ausschließliche Einbindung von Header-Dateien der Standardbibliothek zu erzwingen und generiert einen Kompilierfehler, wenn eine andere Header-Datei eingebunden wird.

[Referenz](https://www.geeksforgeeks.org/using-namespace-std-considered-bad-practice/)

#### F3. Welche kleinste Größe kann eine Variable des Typs child_t im Speicher einnehmen?

```cpp
typedef struct{
    unsigned int  age    : 4;
    unsigned char gender : 1;
    unsigned int  size   : 2;
}child_t;
```

- [ ] 7 Bits
- [ ] 25 Bytes
- [ ] 1 Bit
- [x] 1 Byte

[Referenz](https://en.cppreference.com/w/cpp/language/bit_field)

#### F4. Was sind die Vektoren v1 und v2 nach Ausführung des Codes?

```cpp
std::vector<int> v1{1,2,3},v2;
v2=v1;
v1.push_back(4);
v2.push_back(5);
```

- [ ] Fehler
- [ ] v1:{1,2,3,4}; v2:{5};
- [ ] v1:{1,2,3,4,5}; v2:{1,2,3,4,5};
- [x] v1:{1,2,3,4}; v2:{1,2,3,5};

#### F5. Welche der folgenden Aussagen über den Unterschied zwischen Zeigern und Iteratoren ist richtig?

- [ ] Während Zeiger Variablen sind, die Speicheradressen enthalten, sind Iteratoren generische Funktionen zum Durchlaufen von Containern. Diese Funktion ermöglicht es dem Programmierer, Lese- und Schreibcode zu implementieren, während der Container durchlaufen wird.
- [x] Das Inkrementieren eines Iterators bedeutet immer den Zugriff auf das nächste Element im Container (falls vorhanden), unabhängig vom Container. Das Inkrementieren eines Zeigers bedeutet, auf das nächste Element im Speicher zu zeigen, nicht immer auf das nächste Element.
- [ ] Zeiger sind Variablen, die Speicheradressen enthalten, während Iteratoren vorzeichenlose Ganzzahlen sind, die sich auf Offsets in Arrays beziehen.
- [ ] Alle Iteratoren werden mit Zeigern implementiert, sodass alle Iteratoren Zeiger sind, aber nicht alle Zeiger Iteratoren sind.

[Referenz](https://stackoverflow.com/a/31128162)

#### F6. Welchen Speicherplatz belegt u1?

```cpp
union {
    uint16_t a;
    uint32_t b;
    int8_t c;
} u1;
```

- [x] 4 Bytes
- [ ] 7 Bytes
- [ ] 8 Bytes
- [ ] 2 Bytes

[Referenz](https://en.cppreference.com/w/cpp/language/union)

#### F7. Welcher der folgenden Operatoren kann überladen werden?

- [ ] `?:`
- [x] `new`
- [ ] `::`
- [ ] `.`

[Referenz](https://www.tutorialspoint.com/operators-that-cannot-be-overloaded-in-cplusplus)

#### F8. Welcher der folgenden zeigt den Inhalt der Vektoren, auf die v1 und v2 nach Ausführung dieses Codes zeigen?

```cpp
std:: vector<int> *v1 = new std::vector<int>({1,2,3});
std:: vector<int> *v2;
v2=v1;
v1->push_back(4);
v2->push_back(5);
```

- [ ] `*v1:{1,2,3,4}; *v2:{5};`
- [x] `*v1:{1,2,3,4,5}; *v2:{1,2,3,4,5};`
- [ ] Fehler
- [ ] `*v1:{1,2,3,4}; *v2:{1,2,3,5};`

v1 und v2 zeigen auf denselben Vektor.

#### F9. Was ist kein Unterschied zwischen einer Klasse und einer Struktur?

- [ ] Da Strukturen Teil der Programmiersprache C sind, gibt es eine gewisse Komplexität zwischen C- und C++-Strukturen. Dies ist bei Klassen nicht der Fall.
- [ ] Klassen können Mitgliedsfunktionen haben; Strukturen sind privat.
- [ ] Der Standard-Zugriffsspezifizierer für Mitglieder einer Struktur ist public, während er für Mitglieder einer Klasse private ist.
- [x] Template-Typparameter können mit Klassen deklariert werden, aber nicht mit dem struct-Schlüsselwort.

Templates können sowohl mit Klassen als auch mit Strukturen verwendet werden  
[Referenz](https://docs.microsoft.com/en-us/cpp/cpp/struct-cpp?view=msvc-170)  
[Referenz](https://www.fluentcpp.com/2017/06/13/the-real-difference-between-struct-class/)

#### F10. Angenommen, Sie müssen eine Datenstruktur mit Berechtigung zum Zugriff auf eine Ressource basierend auf den Wochentagen führen, aber Sie können keine bool-Variable für jeden Tag verwenden. Sie müssen ein Bit pro Wochentag verwenden. Welche der folgenden ist eine korrekte Implementierung einer Struktur mit Bitfeldern für diese Anwendung?

- [x] A

```cpp
typedef struct {
    int sunday:1;
    int monday:1;
    // weitere Tage
    int friday:1;
    int saturday:1;
} weekdays;
```

- [ ] B

```cpp
typedef char[7]: weekdays;
```

- [ ] C

```cpp
typedef struct {
    bit sunday:1;
    bit monday:1;
    // weitere Tage
    bit friday:1;
    bit saturday:1;
} weekdays;

```

- [ ] D

```cpp
typedef struct {
    bit sunday;
    bit monday;
    // weitere Tage
    bit friday;
    bit saturday;
} weekdays;
```

[Referenz](https://en.cppreference.com/w/cpp/language/bit_field) _HINWEIS_: Die korrekte Syntax ist, dass jede Variable eine Größe von 1 Bit hat. `bit` ist kein Typ in C++.

#### F11. Was ist ein lvalue?

- [ ] Es ist ein konstanter Ausdruck, d.h. ein Ausdruck, der aus Konstanten und Operationen besteht.
- [ ] Es ist ein Ausdruck, der ein Objekt mit einer Adresse darstellt.
- [ ] Es ist ein Ausdruck, der für den linken Operanden in einer binären Operation geeignet ist.
- [x] Es ist ein Ortswert (location value), d.h. eine Speicheradresse, die für die Zuweisung an einen Zeiger oder eine Referenz geeignet ist.

#### F12. Was macht der auto-Typ-Spezifizierer in dieser Codezeile (seit C++11)?

```cpp
auto x = 4000.22;
```

- [x] Er gibt an, dass der Typ von x aus dem Initialisierer abgeleitet wird - in diesem Fall double.
- [ ] Er gibt an, dass der Typ von x automatisch ist, was bedeutet, dass ihm während des Programms verschiedene Datentypen zugewiesen werden können.
- [ ] Er gibt an, dass x eine Variable mit automatischer Speicherdauer ist.
- [ ] Er gibt an, dass mehr Speicher für x zugewiesen wird, falls mehr Platz benötigt wird, um Datenverlust durch Überlauf zu vermeiden.

#### F13. Was ist ein Klassen-Template?

- [x] Eine Klasse, die mit dem generischen Programmierparadigma geschrieben wurde und Verhalten in Bezug auf Typparameter anstelle spezifischer Typen spezifiziert.
- [ ] Eine leere Oberklasse, die für Vererbung und Polymorphismus vorgesehen ist.
- [ ] Eine Klasse, die nur aus einer Mitgliedsvariablen besteht, ohne Konstruktor, Destruktor oder Mitgliedsfunktionen.
- [ ] Quellcode-Skelett für eine Klasse, bei dem der Programmierer bestimmte Teile ausfüllen muss, um die verwendeten Datentypen und Algorithmen zu definieren.

[Referenz](https://www.mygreatlearning.com/blog/templates-in-cpp/)

#### F14. Was ist die ternäre Operator-Entsprechung zu diesem Code-Snippet?

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

[Referenz](https://www.w3schools.com/cpp/cpp_conditions_shorthand.asp)

#### F15. Was ist die Ausgabe des unten angegebenen Codes?

```cpp
#include <iostream>

int main(){
    int x=10, y=20;
    std::cout << "x = " << x++ << " and y = " << --y << std::endl;
    std::cout << "x = " << x-- << " and y = " << ++y << std::endl;
    return(0);
}
```

- [ ] `x = 10 and y = 20`  
       `x = 11 and y = 19`
- [ ] `x = 11 and y = 19`  
       `x = 10 and y = 20`
- [x] `x = 10 and y = 19`  
       `x = 11 and y = 20`
- [ ] `x = 11 and y = 20`  
       `x = 10 and y = 19`

#### F16. Was bedeuten die zwei Teile, die zwischen Klammern in einer bereichsbasierten For-Schleife angegeben sind, getrennt durch einen Doppelpunkt?

- [x] Der erste ist eine Variablendeklaration, die ein Element in einer Sequenz enthält. Der zweite ist die zu durchlaufende Sequenz.
- [ ] Der erste ist ein Iterator, und der zweite ist der Inkrementwert, der zum Iterator hinzugefügt werden soll.
- [ ] Der erste ist die iterierende Variable. Der zweite ist ein `std::pair`, das den Bereich (Start und Ende) angibt, in dem die Variable iteriert.
- [ ] Der erste ist ein Container-Objekt. Der zweite ist ein `std::pair`, das den Bereich (Start und Ende) angibt, in dem auf die Elemente innerhalb der Schleife zugegriffen wird.

#### F17. Was ist die Ausgabe des unten angegebenen Codes?

```cpp
int8_t a=200;
uint8_t b=100;
if(a>b)
    std::cout<<"greater";
else
    std::cout<<"less";
```

- [ ] Es gibt keine Ausgabe, weil es eine Ausnahme beim Vergleich eines int8_t mit einem uint8_t gibt.
- [ ] greater
- [x] less
- [ ] Es gibt keine Ausgabe, weil es einen Compilerfehler gibt.

Hinweis: Eine Variante der Frage unten.

#### F18. Was ist die Ausgabe dieses Codeblocks?

```cpp
int8_t a=200;
uint8_t b=100;
std::cout<<"a="<<(int)a;
std::cout<<", b="<<(int)b;
```

- [x] a=-56, b=100
- [ ] a=-55, b=100
- [ ] a=200, b=-156
- [ ] a=200, b=100

Hinweis: Implizite Konvertierung von 'int' zu 'int8_t' (auch bekannt als 'signed char') ändert den Wert von 200 zu -56

#### F19. Was ist die Ausgabe nach Ausführung dieses Code-Snippets?

```cpp
int x=5, y=2;
if(x & y) {
    /*_Teil A_*/
}
else {
    /*_Teil B_*/
}
```

- [ ] Teil A wird ausgeführt, weil x==5 (wahr) und y==2 (wahr), daher wertet die UND-Operation als wahr aus.
- [x] Teil B wird ausgeführt, weil (x & y) 0 oder falsch ergibt.
- [ ] Teil A wird ausgeführt, weil (x & y) einen Wert ungleich Null oder wahr ergibt.
- [ ] Teil B wird ausgeführt, weil die Anweisung (x & y) ungültig und daher falsch ist.

[Referenz](https://stackoverflow.com/questions/63867765/dont-understand-why-if-5-2-is-false)

#### F20. Was ist eine gültige Definition für die `get_length`-Funktion, die die Länge einer null-terminierten Zeichenkette zurückgibt?

- [x] A

```cpp
int get_length(char *str) {
    int count=0;
    while(str[count++]);
    return count-1;
}
```

- [ ] B

```cpp
int get_length(char *str) {
    int count=0;
    while(str!=NULL){
        count++;
        str++;
    }
    return count;
}
```

- [ ] C

```cpp
int get_length(char *str) {
    int count=0;
    while((*str)++)
        count++;
    return count;
}
```

- [ ] D

```cpp
int get_length(char *str) {
    int count=0;
    while(str++)
        count++;
    return count;
}
```

#### F21. Welche STL-Klasse ist am besten geeignet, um eine Sammlung von Daten zu implementieren, die immer sortiert ist, sodass die Pop-Operation immer das größte Element erhält? Angenommen, Sie sind nur an Push- und Pop-Operationen interessiert.

- [ ] `std::list`
- [ ] `std::vector`
- [x] `std::priority_queue`
- [ ] `std::map`

#### F22. Was bedeuten die drei Abschnitte, die zwischen Klammern in einer For-Schleife durch Semikolons getrennt sind?

- [ ] Der erste ist der Name der iterierenden Variablen, der zweite ist die Anzahl der Iterationen, und der dritte ist das gewünschte Inkrement oder Dekrement (angegeben mit einer vorzeichenbehafteten Ganzzahl).
- [x] Der erste ist der Initialisierungsblock, der zweite ist die Bedingung zum Iterieren, und der dritte ist der Inkrementblock.
- [ ] Der erste ist die iterierende Variable, der zweite ist der Container, in dem sie operieren soll, und der dritte ist eine Abbruchbedingung zum jederzeit Abbrechen.
- [ ] Der erste ist der Name der iterierenden Variablen, der zweite ist der Startwert für die iterierende Variable, und der dritte ist der Stoppwert (der letzte Wert plus eins).

#### F23. Was gibt dieser Code aus?

```cpp
int i = 0;
printf("%d", i++);
printf("%d", i--);
printf("%d", ++i);
printf("%d", --i);
```

- [x] 0,1,1,0
- [ ] 0,1,0,1
- [ ] 0,0,1,0
- [ ] 1,0,1,0

[Referenz](https://www.geeksforgeeks.org/pre-increment-and-post-increment-in-c/)

#### F24. Was ist wahr über die Variable namens `ptr`?

```cpp
void *ptr;
```

- [ ] Es ist ein Zeiger, der mit NULL initialisiert wurde.
- [ ] Es ist ein Zeiger auf eine void-Funktion.
- [ ] Diese Deklaration verursacht einen Compilerfehler, da Zeiger einen Typ angeben müssen.
- [x] Es ist ein Zeiger auf einen Wert ohne spezifischen Typ, sodass er auf jeden Typ gecastet werden kann.

[Referenz](https://en.cppreference.com/w/cpp/language/pointer)

#### F25. Was ist die Ausgabe des unten angegebenen Codes?

```cpp
int c=3; char d='A';
std::printf("c is %d and d is %c",c,d);
```

- [ ] c is d and d is c
- [ ] c is A and d is 3
- [x] c is 3 and d is A
- [ ] c is c and d is d

#### F26. Was ist die Ausgabe dieses Codes?

```cpp
printf("1/2 = %f",(float)(1/2));
```

- [ ] 1/2 = 0.499999
- [ ] 1/2 = 0
- [x] 1/2 = 0.000000
- [ ] 1/2 = 0.5

#### F27. Was ist der Unterschied zwischen einem öffentlichen und einem privaten Klassenmitglied?

- [ ] Öffentliche Mitglieder sind dasselbe wie globale Variablen, sodass jeder Teil des Codes auf sie zugreifen kann. Private Mitglieder sind dasselbe wie automatische Variablen, sodass nur ihre Klasse auf sie zugreifen kann.
- [ ] Öffentliche Mitglieder werden für jede laufende Anwendung zugänglich gemacht. Private Mitglieder werden nur für die Anwendung zugänglich gemacht, in der das Objekt instanziiert wird.
- [ ] Öffentliche Mitglieder werden in einer Multithread-Umgebung als gemeinsame Variablen kompiliert. Private Mitglieder werden als Thread-lokale Variablen kompiliert.
- [x] Öffentliche Mitglieder können von jeder Funktion aufgerufen werden. Private Mitglieder können nur von Mitgliedsfunktionen derselben Klasse und Freunden der Klasse aufgerufen werden.

[Referenz](https://www.geeksforgeeks.org/difference-between-public-and-private-in-c-with-example/)

#### F28. Was ist der Wert von `x` nach Ausführung dieses Codes?

```cpp
int x=10, a=-3;
x+=a;
```

- [ ] 3
- [x] 7
- [ ] -3
- [ ] 13

#### F29. Welche Aussage ist wahr?

- [ ] Nur Klassen können Mitgliedsvariablen und Methoden haben.
- [x] C++ unterstützt Mehrfachvererbung.
- [ ] C++ unterstützt nur Einfachvererbung.
- [ ] Nur Strukturen können erben.

#### F30. Betrachten Sie einen Zeiger auf void, genannt `ptr`, der so eingestellt wurde, dass er auf eine Gleitkommavariable `g` zeigt. Welche Wahl ist eine gültige Methode, um `ptr` zu dereferenzieren, um seinen Zeigerwert einer Float-Variablen `f` später im Programm zuzuweisen?

```cpp
float g;
void *ptr=&g;
```

- [ ] `float f=*(float)ptr;`
- [ ] `float f=(float *)ptr;`
- [ ] `float f=(float)*ptr;`
- [x] `float f=*(float *)ptr;`

#### F31. Was ist der `.*`-Operator und was macht er?

- [ ] Er ist derselbe wie der Klassenmitgliedszugriffsoperator oder Pfeiloperator `(->)`, der es Ihnen ermöglicht, auf ein Mitglied eines Objekts über einen Zeiger auf das Objekt zuzugreifen.
- [x] Er ist der Zeiger-auf-Mitglied-Operator und ermöglicht es Ihnen, auf ein Mitglied eines Objekts über einen Zeiger auf dieses spezifische Klassenmitglied zuzugreifen.
- [ ] Er ist der Mitgliedszugriff mit Adressoperator, der die Adresse eines Klassen- oder Strukturmitglieds zurückgibt.
- [ ] Er ist eine Kombination des Mitgliedszugriffsoperators `(.)` und des Dereferenzierungsoperators `(*)`, sodass er es Ihnen ermöglicht, auf das Objekt zuzugreifen, auf das ein Mitgliedszeiger zeigt.

[Referenz](https://en.cppreference.com/w/cpp/language/operator_member_access)

#### F32. Für diese Deklarationen, welche Wahl zeigt vier gleichwertige Möglichkeiten, das Zeichen "y" im String einer char-Variablen c zuzuweisen?

```cpp
char buff[50] = "strings as arrays of characters are fun!"
char *str = buff+11;
char c;
```

- [ ] A

```cpp
c = buff[16];
c = str[5];
c = *(buff+16);
c = *(str+5);
```

- [ ] B

```cpp
c = *(buff[15]);
c = *(str[4]);
c = buff+15;
c = str+4;
```

- [x] C

```cpp
c = buff[15];
c = str[4];
c = *(buff+15);
c = *(str+4);
```

- [ ] D

```cpp
c = *(buff[16]);
c = *(str[5]);
c = buff+16;
c = str+5;
```

#### F33. Welche Wahl ist die korrekte Deklaration für die Klasse namens Dog, abgeleitet von der Animal-Klasse?

```cpp
class Animal{
    //....
}
```

- [ ] A

```cpp
class Dog :: public Animal {
   //....
};
```

- [x] B

```cpp
class Dog : public Animal {
   //....
};
```

- [ ] C

```cpp
public class Animal :: Dog {
   //....
};
```

- [ ] D

```cpp
public class Dog extends Animal {
   //....
};
```

#### F34. Was ist die Ausgabe dieses unten angegebenen Codes?

```cpp
#include <cstdio>
using namespace std;

int main(){
    char c = 255;
    if(c>10)
        printf("c = %i, which is greater than 10", c);
    else
        printf("c = %i, which is less than 10", c);
    return 0;
}
```

- [x] c = -1, which is less than 10
- [ ] c = 255, which is greater than 10
- [ ] c = -1, which is greater than 10
- [ ] c = 255, which is less than 10

Technisch gesehen ist es implementierungsabhängig, ob ein `char` `signed` oder `unsigned` ist;
im letzteren Fall wäre die zweite Antwort korrekt.
[Referenz](https://en.cppreference.com/w/cpp/language/types)

#### F35. Wie kann C++-Code eine C-Funktion aufrufen?

- [ ] durch einfachen Aufruf des C-Codes
- [ ] Es gibt keine Möglichkeit für C++, eine C-Funktion aufzurufen
- [x] durch Verwendung von extern "C"
- [ ] durch Importieren des Quell-C-Codes

#### F36. Welche Wahl ist _keine_ gültige Typdefinition einer Struktur, die x- und y-Koordinaten als Ganzzahlen enthält und genau wie gezeigt für die Variable namens `center` verwendet werden kann?

```cpp
coord center;
center.x = 5;
center.y = 3;
```

- [x] A

```cpp
typedef struct coord {
    int x;
    int y;
};
```

- [ ] B

```cpp
typedef struct coord {
    int x;
    int y;
} coord;
```

- [ ] C

```cpp
typedef struct {
    int x;
    int y;
} coord;
```

- [ ] D

```cpp
struct coord {
    int x;
    int y;
};

typedef struct coord coord;
```

#### F37. Welche Wahl erzeugt _nicht_ dieselbe Ausgabe wie dieses Code-Snippet? Angenommen, die Variable `i` wird nirgendwo sonst im Code verwendet.

```cpp
for (i=1;i<10;i++){
    cout<<i<<endl;
}
```

- [x] A

```cpp
i=1;
while(i<10){
    cout<<++i<<endl;
}
```

- [ ] B

```cpp
for (int i:{1,2,3,4,5,6,7,8,9}) {
    cout<<i<<endl;
}
```

- [ ] C

```cpp
i = 1;
do {
    cout<<i++<<endl;
} while(i<10);
```

- [ ] D

```cpp
i = 1;
loop:
    cout<<i++<<endl;
    if(i<10) goto loop;
```

#### F38. Was macht dieser Teil einer main.cpp-Datei?

```cpp
#include "library.h"
```

- [ ] Es veranlasst die Toolchain, alle Inhalte von library.h zu kompilieren, sodass der ausführbare Code bei Bedarf für die endgültige Anwendung verfügbar ist.
- [ ] Es wählt library.h für die Deklarationen und Definitionen aller Daten und Funktionen aus, die im Rest der Quelldatei main.cpp verwendet werden, und ersetzt schließlich die `#include`-Direktive durch diese Deklarationen und Definitionen.
- [ ] Es informiert den Linker, dass einige Funktionen oder Daten, die in der Quelldatei main.cpp verwendet werden, in library.h enthalten sind, sodass sie zur Laufzeit aufgerufen werden können. Dies wird auch als dynamisches Linken bezeichnet.
- [x] Es verursacht den Ersatz der `#include`-Direktive durch den gesamten Inhalt der Quelldatei library.h. Dies ähnelt der Kopieren-Einfügen-Operation von library.h in main.cpp.

#### F39. Betrachten Sie diese Funktionsdeklaration von `is_even`, die eine Ganzzahl entgegennimmt und true zurückgibt, wenn das Argument eine gerade Zahl ist, und false sonst. Welche Deklarationen sind korrekt für überladene Versionen dieser Funktion zur Unterstützung von Gleitkommazahlen und Zeichenkettendarstellungen von Zahlen?

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

#### F40. Welche Wahl ist ein Include-Guard für die Header-Datei `my_library.h`?

- [ ] A

```cpp
#ifdef MY_LIBRARY_H
#define MY_LIBRARY_H

// my_library.h Inhalt

#endif /* MY_LIBRARY_H */
```

- [x] B

```cpp
#ifndef MY_LIBRARY_H
#define MY_LIBRARY_H

// my_library.h Inhalt

#endif /* MY_LIBRARY_H */
```

- [ ] C

```cpp
#ifdef MY_LIBRARY_H
#undef MY_LIBRARY_H

// my_library.h Inhalt

#endif /* MY_LIBRARY_H */
```

- [ ] D

```cpp
#define MY_LIBRARY_H
#include MY_LIBRARY_H

// my_library.h Inhalt

#undef MY_LIBRARY_H
```

#### F41. Was ist falsch an dieser Definition bei Verwendung eines Pre-C++11-Compilers?

```cpp
std::vector<std::vector<int>> thematrix;
```

- [ ] Es ist nichts falsch daran.
- [ ] Ein `std::vector` kann keine weiteren `std::vector`-Container als seine Elemente enthalten.
- [ ] Die korrekte Syntax sollte sein: `std::vector[std::vector[int]] thematrix;`
- [x] `>>` wird als Rechtsverschiebungsoperator geparst und führt somit zu einem Compilerfehler.

#### F42. Was ist die folgende Anweisung gleichwertig?

#### F42.b. Was ist die Anweisung gleichwertig?

```cpp
sprite->x
```

- [ ] `sprite.x`
- [ ] `sprite.*x`
- [x] `(*sprite).x`
- [ ] `*sprite.x`

#### F43. Betrachten Sie eine Klasse namens `complexNumber`. Welcher Code führt zu einem gleichwertigen Objekt?

```cpp
complexNumber(float real, float im)
: real_part(real),
 im_part(im){}
```

- [ ] A

```cpp
complexNumber(float real, float im) {
    this->real = real_part;
    this->im = im_part;
}
```

- [ ] B

```cpp
complexNumber(float real, float im) {
    this->real_part(real);
    this->im_part(im);
}
```

- [x] C

```cpp
complexNumber(float real, float im) {
    this->real_part = real;
    this->im_part = im;
}
```

- [ ] D

```cpp
complexNumber(float real, float im) {
    this->real_part = &real;
    this->im_part = &im;
}
```

#### F44. Was ist das Ergebnis der Ausführung dieses Code-Snippets?

```cpp
bool x=true, y=false;

if (~x || y) {
    /*Teil A*/
} else {
    /*Teil B*/
}
```

- [ ] Teil A wird ausgeführt, weil der Ausdruck `(~x || y)` immer wahr ist, wenn `y==false`.
- [ ] Teil B wird ausgeführt, weil die Anweisung `(~x || y)` ungültig und daher falsch ist.
- [x] Teil A wird ausgeführt, weil `~x` nicht null ist, was wahr bedeutet.
- [ ] Teil B wird ausgeführt, weil `~x` falsch ist und `y` falsch ist, daher wertet die OR-Operation als falsch aus.

#### F45. Was wäre die Ausgabe dieses Codes?

```cpp
int32_t nums[3]={2,4,3};
std::cout << ( nums[0] << nums[1] << nums[2] );
```

- [ ] Die Ausgabe sind die Adressen von `nums[0]`, `nums[1]` und `nums[2]`, in dieser Reihenfolge, ohne Leerzeichen.
- [x] 256
- [ ] `0`
- [ ] `243`

#### F46. Was ist die Ausgabe dieses Codes?

```cpp
float values[5]={0.54f, 2.71828f, 3.14159f, 5.499999f, 10.0f};
for(auto f:values)
    printf("%i ",(int)(f+0.5f));
```

- [ ] `0.54 2.71828 3.14159 5.499999 10.0`
- [ ] `1 3 4 6 11`
- [ ] `0 2 3 5 10`
- [x] `1 3 3 5 10`

#### F47. Welche der folgenden STL-Klassen ist am besten geeignet, um ein Telefonbuch zu implementieren? Angenommen, jeder Eintrag enthält einen Namen und eine Telefonnummer ohne Duplikate, und Sie möchten eine Suche nach Namen durchführen.

- [ ] `std::priority_queue`
- [ ] `std::list`
- [ ] `std::vector`
- [x] `std::map`

[Referenz](https://en.cppreference.com/w/cpp/container/map)

#### F48. Was macht dieses Programm?

```cpp
#include <iostream>
#include <fstream>
using namespace std;

int main(){
    ifstream file1("text1.txt", ios::binary);
    ofstream file2("text2.txt", ios::binary);
    file2 << file1.rdbuf();
}
```

- [ ] Es benennt text1.txt in text2.txt um.
- [ ] Es erstellt ein Verzeichnis namens text2.txt und verschiebt text1.txt dorthin.
- [x] Es kopiert den Inhalt von text1.txt in text2.txt - d.h., es erstellt eine Kopie von text1.txt mit dem Namen text2.txt.
- [ ] Es hängt den Inhalt von text1.txt an text2.txt an - d.h., ersetzt den Inhalt von text2.txt durch die Verkettung von text2.txt und text1.txt.

[Referenz](https://en.cppreference.com/w/cpp/header/fstream)

#### F49. Was ist _keine_ Konsequenz der Deklaration der Mitgliedsvariablen `count` von my_class als static? / Alt.: Welche Aussage ist wahr bei der Deklaration der Mitgliedsvariablen `count` als static?

```cpp
class my_class {
    public: static int count;
}
```

- [x] Die Variable kann von keinem Teil des Codes in derselben Anwendung oder Thread modifiziert werden. Andere Threads können sie jedoch modifizieren.
- [ ] Die Variable existiert auch dann, wenn keine Objekte der Klasse definiert wurden, sodass sie an jedem Punkt im Quellcode modifiziert werden kann.
- [ ] Die Variable wird nur einmal zugewiesen, unabhängig davon, wie viele Objekte instanziiert werden, da sie an die Klasse selbst gebunden ist, nicht an ihre Instanzen.
- [ ] Alle Objekte, die versuchen, auf ihre count-Mitgliedsvariable zuzugreifen, verweisen tatsächlich auf die einzige klassengebundene statische count-Variable.

[Referenz](https://en.cppreference.com/w/cpp/language/static)

#### F50. Was ist der angenommene Typ einer Konstante, die im Quellcode als `0.44` dargestellt wird?

- [x] double
- [ ] long float
- [ ] long double
- [ ] float

#### F51. Was ist ein geeigneter Weg, `my_object` wie unten gezeigt zu entfernen?

```cpp
my_class *my_object = new my_class();
```

- [x] `delete(my_object);`
- [ ] `free(my_object);`
- [ ] Der Garbage Collector wird das Objekt schließlich zerstören.
- [ ] Das Verlassen des Gültigkeitsbereichs wird das Objekt zerstören.

#### F52. Was ist der korrekte Weg, die `count`-Mitgliedsfunktion für den Objektzeiger namens `grades` aufzurufen?

```cpp
class my_array{
    public:
        int count();
};  // ... weitere Mitglieder oben

int main(){
    my_array *grades = new my_array();
};  // ... weiterer Code oben
```

- [ ] `grades.count();`
- [ ] `my_array->count();`
- [x] `grades->count();`
- [ ] `my_array.count();`

[Referenz](https://en.cppreference.com/w/c/language/operator_member_access)

#### F53. Was wäre die Ausgabe dieses Codes?

```cpp
int i0=4, i1=6, i2=8;
int& nums[3]={i2,i0,i1};
std::cout<<nums[0]<<nums[1]<<nums[2];
```

- [x] Es gibt keine Ausgabe. Der Code verursacht einen Compilerfehler, weil `nums` ein Array von Referenzen ist, was illegal ist.
- [ ] 846
- [ ] Die Ausgabe sind die Adressen von `i2`, `i0` und `i1`, in dieser Reihenfolge, ohne Leerzeichen.
- [ ] 468

[Referenz](https://en.cppreference.com/w/cpp/language/array)

#### F54. Verursacht dieser Code einen Compilerfehler? Wenn ja, warum, und wenn nicht, was ist `child_t`?

```cpp
typedef struct{
    unsigned int  age    : 4;
    unsigned char gender : 1;
    char                 : 0;
    unsigned int  size   : 2;
}child_t;
```

- [ ] Ja, es verursacht einen Compilerfehler, weil das Doppelpunktzeichen in Strukturdefinitionen nicht erlaubt ist.
- [x] Nein, und `child_t` ist ein Typ, der als Struktur mit Bitfeldern definiert ist. Es hat 4 Bits für age und 1 Bit für gender im ersten Byte und 2 Bits für size im zweiten Byte.
- [ ] Ja, es verursacht einen Compilerfehler, weil es ein unbenanntes Feld gibt.
- [ ] Ja, es verursacht einen Compilerfehler, weil ein Feld mit einer Größe von 0 definiert ist.

[Referenz](https://en.cppreference.com/w/cpp/language/bit_field)

#### F55. Wozu ist dieser Ausdruck gleichwertig?

```cpp
A->B
```

- [ ] `*(A.B)`
- [ ] `B=A`
- [x] `(*A).B`
- [ ] `&A.B`

Hinweis: Eine einfachere Variante der Frage unten.

#### F56. Wozu ist dieser Ausdruck gleichwertig?

```cpp
A->B->C->D
```

- [ ] `A.B.C.D`
- [ ] `*A.*B.*C.*D`
- [ ] `&A.&B.&C.&D`
- [x] `*(*((*A).B).C).D`

**Hinweis:** Eine komplexere Variante der Frage oben.

#### F57. Was macht diese Funktion?

```cpp
auto buff = new char[50];
std::memset(buff,20,50);
```

- [ ] Sie deklariert einen Speicherpuffer namens buff, der bei Adresse 20 beginnt und bei Adresse 70 endet.
- [ ] Sie setzt alle Bits im Array namens buffer von seinem Element bei Index 20 bis zu seinem Element bei Index 50.
- [x] Sie schreibt den Wert 20 in jede Speicheradresse von buff bis buff+49.
- [ ] Sie deklariert einen Speicherpuffer namens buff, der bei Adresse 20 beginnt und bei Adresse 50 endet.

[Referenz](https://en.cppreference.com/w/cpp/string/byte/memset)

#### F58. Betrachten Sie eine Klasse namens `CustomData`. Welche Wahl ist eine korrekte Deklarationssyntax zum Überladen des Postfix-`++`-Operators als Klassenmitglied?

- [ ] `CustomData& operator++();`
- [ ] `void operator++(CustomData);`
- [ ] `CustomData operator++(CustomData);`
- [x] `CustomData operator++(int);`

[Referenz](https://en.cppreference.com/w/cpp/language/operators)

#### F59. Sie möchten my_array sortieren, das unten deklariert ist. Welche Wahl ist der korrekte Aufruf von std::sort unter Verwendung eines Lambda-Ausdrucks als Vergleichsfunktion?

```cpp
std::array<uint32_t, 50> my_array;
```

- [x] A

```cpp
std::sort(my_array.begin(), my_array.end(),
    [](uint32_t a, uint32_t b) {
        return a < b;
    })
```

- [ ] B

```cpp
lambda(uint32_t a, uint32_t b){
    return a < b;
}
std::sort(my_array.begin(), my_array.end(), lambda);
```

- [ ] C

```cpp
std::sort(my_array.begin(), my_array.end(),
    lambda(uint32_t a, uint32_t b){
        return a < b;
    })
```

- [ ] D

```cpp
lambda(uint32_t a, uint32_t b){
    return a < b;
}
std::sort(my_array.begin(), my_array.end(), &lambda);
```

[Referenz](https://docs.microsoft.com/en-us/cpp/cpp/lambda-expressions-in-cpp?view=msvc-160)

#### F60. Welche Wahl ist die vernünftigste Implementierung der Funktion std::mutex::lock() unter Verwendung von std::mutex::try_lock()?

- [x] A

```cpp
void std::mutex::lock(){
    while(!this->try_lock());
}
```

- [ ] B

```cpp
void std::mutex::lock(){
    return (this->try_lock());
}
```

- [ ] C

```cpp
void std::mutex::lock(){
    while(1)
        this->try_lock();
}
```

- [ ] D

```cpp
void std::mutex::lock(){
    while(this->try_lock());
}
```

Hinweis: Variante der Frage unten.

#### F61. Was ist der Hauptunterschied zwischen diesen beiden Funktionen?

```cpp
std::mutex::lock()
std::mutex::try_lock()
```

- [ ] `lock()` hat eine höhere Priorität über `try_lock()`. Das bedeutet, dass Sie eine bessere Chance haben, einen Mutex mit `lock()` zu erwerben.
- [x] Beide versuchen, eine Sperre zu erwerben, aber `lock()` blockiert, wenn der Mutex nicht verfügbar ist, während `try_lock()` zurückgibt, ob der Mutex verfügbar ist oder nicht.
- [ ] `lock()` erzwingt Präemption, während `try_lock()` Präemption vorschlägt.
- [ ] Wenn der Mutex nicht verfügbar ist, gibt `try_lock()` mit einem entsprechenden Code zurück, während `lock()` den Mutex vom Thread stiehlt, der ihn derzeit hat.

Hinweis: Variante der Frage oben.

[Referenz](https://en.cppreference.com/w/cpp/thread/mutex/try_lock)

#### F62. Was ist der Zweck eines Destruktors?

- [x] Er ermöglicht es dem Programmierer, den notwendigen Code zu schreiben, um die vom Objekt erworbenen Ressourcen freizugeben, bevor das Objekt selbst gelöscht wird.
- [ ] Er löscht ein Objekt. Ein Beispiel für einen Destruktor ist die `delete()`-Funktion.
- [ ] Er beendet ein Programm. Dies kann als regulärer Funktionsaufruf oder als Ausnahme erreicht werden.
- [ ] Es gibt keine Destruktoren in C++.

#### F63. Was ist ein Vorteil der Deklaration des Parameters als `const`-Referenz anstelle der Deklaration als reguläres Objekt?

```cpp
int calculateMedian(const my_array& a)
```

- [ ] Tatsächlich können Objekte nicht als reguläre Variablen übergeben werden, weil sie einen Konstruktoraufruf erfordern. Daher ist eine `const`-Referenz die einzige Möglichkeit, Klasseninstanzen an Funktionen zu übergeben.
- [ ] Es gibt keine Vorteile, weil eine Referenz und ein Objekt als dasselbe behandelt werden.
- [x] Der `const`-Qualifier verbietet es dem Code, das Argument zu modifizieren, sodass der Programmierer sicher sein kann, dass das Quellobjekt unverändert bleibt. / Alt.: Das Argument wird als Referenz übergeben, also wenn das übergebene my_array-Objekt groß ist, benötigt das Programm weniger Zeit und Speicher.
- [ ] Das Argument wird als Referenz übergeben, sodass die Funktion eine Kopie erhält, die modifiziert werden kann, ohne die ursprüngliche Variable zu beeinflussen.

[Referenz](https://stackoverflow.com/a/2627179/10773894)

#### F64. Was ist ein Include-Guard?

- [ ] Eine Präprozessordirektive, die inkonsistente Verhaltensweisen in Zeilen verhindert, die die Direktiven #ifdef, #ifndef oder #elif enthalten
- [ ] Eine Compileroption, die verhindert, dass der Benutzercode zusätzliche Bibliotheken einbindet
- [x] Eine Präprozessoranweisung, die verhindert, dass eine Quelldatei mehr als einmal in einem Projekt eingebunden wird
- [ ] Eine Bibliothek, die Sicherheitsfunktionen wie Mutexe, Watchdog-Timer und Assertions zum Projekt hinzufügt

#### F65. Was wäre die korrekte Deklaration eines Standardkonstruktors für eine Klasse namens Sprite?

- [x] A
  ```cpp
  public: Sprite();
  ```
- [ ] B
  ```cpp
  private: void Sprite();
  ```
- [ ] C
  ```cpp
  public: void Sprite();
  ```
- [ ] D
  ```cpp
  private: Sprite();
  ```

#### F66. Was ist der Zweck dieser Zeile in einer Header-Datei?

```cpp
#pragma once
```

- [ ] Die Verwendung ihres Inhalts auf nur eine Quelldatei zu beschränken
- [ ] Dem Compiler mitzuteilen, dass nur eine Variable aus den in dieser Header-Datei enthaltenen Klassen oder Typen instanziiert werden kann
- [ ] Dem Compiler zu helfen, schneller fertig zu werden, indem sichergestellt wird, dass nur ein Compiler-Durchgang für den in dieser Header-Datei enthaltenen Code notwendig ist
- [x] Den Compiler zu veranlassen, diese Header-Datei nur einmal zu parsen, selbst wenn sie mehrfach in der Quelle eingebunden ist

[Referenz hier](https://en.cppreference.com/w/cpp/preprocessor/impl)

#### F67. Was ist eine Variable vom Typ double?

- [ ] Ein 2-Tupel
- [ ] Eine Ganzzahl
- [x] Eine Gleitkommazahl
- [ ] Eine Zeichenkette mit mehr als 255 Zeichen

[Referenz](https://www.educba.com/c-plus-plus-double/)

#### F68. Wofür wird der <<-Operator außer zum Verschieben von Bits nach links verwendet?

- [ ] Zum Verschieben von Zeichen nach links in einer Zeichenkette.
- [x] Zum Einfügen von Zeichen in einen Ausgabestrom wie std::cout.
- [ ] Zum Vergleichen von Gleitkommazahlen als kleiner-als.
- [ ] Zum Zuweisen einer Variablen zu einer Referenz.

#### F69. Welche Wahl ist ein Grund, den Typ eines Zeigers anzugeben, anstatt `void *` zu verwenden, das als Zeiger auf jeden Typ funktioniert?

- [ ] Der Compiler benötigt den Datentyp, um sicherzustellen, dass der Zeiger nicht für illegale nicht-zeigerfähige Typen wie Funktionen, Labels, Zeiger und Referenzen verwendet wird.
- [ ] `void *` funktioniert nicht für jeden Typ. Die Sprache erlaubt nicht die Zuweisung von etwas anderem als `void` an einen Zeiger auf `void *`.
- [x] Der Compiler benötigt den Datentyp, um zu wissen, wie viel Speicher für den Zeiger zugewiesen werden soll, da verschiedene Datentypen unterschiedliche Zeigerlängen erfordern.
- [ ] Ja, es verursacht einen Compilerfehler, weil ein Feld mit einer Größe von 0 definiert ist.

[Referenz](https://stackoverflow.com/questions/9802585/why-is-the-data-type-needed-in-pointer-declarations)

#### F70. Was ist falsch an diesem Code?

```cpp
#include <iostream>
char str[20];
int main(){
    std::cout << "What's your name? ";
    str << std::cin
    std::cout << "Hello, " << str;
    return 0;
}
```

- [ ] Die main-Funktion soll einen void-Rückgabetyp haben.
- [ ] `std::cin` und `std::cout` sind ungültig. Die korrekten Namen für die Zeicheneingabe- und Ausgabeströme sind `cin` und `cout`.
- [ ] Die Adresse von `str` soll verwendet werden. Das ist `&str` anstelle von `str`.
- [x] Der Eingabeoperatorfluss ist invertiert. Er sollte von `std::cin` ausgehen und dann (>>) in `str` fließen.

#### F71. Wenn in einem gültigen Ausführungskontext platziert, welche Anweisung wird dynamisch Speicher vom Heap für eine Ganzzahl mit dem Wert 11 zuweisen?

- [ ] `int anInt = new int(11);`
- [ ] `int* anInt = new int[11];`
- [ ] `int anInt = new int[11];`
- [x] `int* anInt = new int(11);`

#### F72. Welche Wahl beschreibt den Typ `long` am besten?

- [x] Eine Ganzzahl von mindestens 32 Bits
- [ ] Eine Zeichenkette mit mehr als 255 Zeichen
- [ ] Ein Zeiger
- [ ] Eine 64-Bit-Gleitkommazahl

#### F73. Welcher der folgenden Typen hat die engste Funktionalität zu einer Klasse?

- [x] `struct`
- [ ] `union`
- [ ] `enum`
- [ ] `namespace`

[Referenz](https://en.cppreference.com/w/c/language/struct)

#### F74. Bei diesen Einträgen in einer Map, wie werden Sie den Wert für den Schlüssel "Sinead" auf 22 aktualisieren?

![image](images/Q79.png?raw=png)

- [x] `marks["Sinead"] = 22`
- [ ] `marks["Sinead"].22`
- [ ] `marks["Sinead"] -> 22`
- [ ] `marks["Sinead"].value = 22`

#### F75. Warum kann std::sort ein Funktionsobjekt als einen seiner Parameter empfangen?

- [x] `Die std::sort-Funktion ist ein Template. Der Programmierer kann den Sortieralgorithmus in einem Funktionsobjekt als Argument eingeben.`
- [ ] `Tatsächlich nimmt std::sort nur ein Argument entgegen, nämlich den zu sortierenden Container.`
- [ ] `std::sort arbeitet auf einem Template-Container. Der Compiler weiß nicht, wie er die darin enthaltenen Werte relational vergleichen soll, daher muss eine Funktion zum Vergleich bereitgestellt werden.`
- [ ] `std::sort verwendet die Parameter-Funktion als Fehlerbehandler. Die Funktion wird aufgerufen, wenn ein Fehler auftritt.`

#### F76. Was passiert, wenn Sie dieses Code-Snippet ausführen?

```cpp
#include <iostream>

int main() {
float a = 5.51;
int b = static_cast<int>(a);
std::cout << b;
}
```

- [ ] `6 wird auf der Standardausgabe ausgegeben, ohne dass Kompilierungswarnungen generiert werden.`
- [x] `5 wird auf der Standardausgabe ausgegeben, ohne dass Kompilierungswarnungen generiert werden.`
- [ ] `6 wird auf der Standardausgabe ausgegeben, mit Kompilierungswarnungen.`
- [ ] `5 wird auf der Standardausgabe ausgegeben, mit Kompilierungswarnungen.`

#### F77. Welcher Zugriffsspezifizierer erlaubt es nicht, dass Klassenmitglieder von außerhalb der Klasse aufgerufen werden, erlaubt aber den Zugriff durch abgeleitete Klassen?

- [ ] guarded
- [x] protected
- [ ] public
- [ ] private

#### F78. Die standardmäßige ausführbare Generierung auf UNIX für ein C++-Programm ist \_

- [ ] a.exe
- [ ] a
- [x] a.out
- [ ] out.a

#### F79. Was wird die Ausgabe des folgenden Programms sein?

```cpp
#include <iostream>
using namespace std;
int main() {
  int a=1;
  cout<<(a++)*(++a)<<endl;
  return 0;
}
```

- [ ] 1
- [ ] 2
- [x] 3
- [ ] 6

#### F80. Wofür steht "c" in cout und cin?

- [ ] compiler
- [ ] console
- [x] character
- [ ] standard namespace

#### F81. Was ist die Verwendung von tellp()?

- [ ] Aktuelle Eingabezeigerposition
- [x] Aktuelle Ausgabezeigerposition
- [ ] Letzte Eingabezeigerposition
- [ ] Letzte Ausgabezeigerposition

#### F82. Was ist eine Callback-Funktion?

- [ ] Zeiger auf einen Zeiger
- [x] Zeiger auf eine Funktion
- [ ] Funktion für einen Zeiger
- [ ] Funktion für eine Klasse

#### F83. Was ist die korrekte Syntax, um "Hello World" in C++ auszugeben?

- [x] `cout << "Hello World";`
- [ ] `System.out.println("Hello World");`
- [ ] `print("Hello World");`
- [ ] Console.WriteLine("Hello World");```

#### F84. Wie viele Kategorien von Iteratoren gibt es in C++?

- [ ] 4
- [ ] 3
- [ ] 7
- [x] 5

#### F85. Was bedeutet Basisklasse in C++?

- [ ] Sie erbt andere Klassen
- [ ] Sie hat eine Zeigervariable
- [ ] Sie ist die erste deklarierte Klasse
- [x] Eine andere Klasse wurde von dieser Klasse geerbt

#### F86. Die Größe von C++-Objekten wird in Vielfachen der Größe eines ** ausgedrückt, und die Größe eines char ist **.

- [ ] char, 4
- [ ] float, 8
- [ ] int, 1
- [x] char, 1

#### F87. Implementierungsabhängige Aspekte über eine Implementierung können gefunden werden in

- [ ] `<numeric>`
- [ ] `<limit>`
- [x] `<limits>`
- [ ] `<implementation>`

#### F88. Was ist ein Standardkonstruktor?

- [x] Ein Konstruktor, der ohne Argumente verwendet werden kann
- [ ] Ein Konstruktor, der keinen Rückgabewert hat
- [ ] Ein Konstruktor, der von mehreren Klassen verwendet wird
- [ ] Ein Konstruktor, der alle Mitglieder einer Klasse initialisiert

#### F89. Warum würden Sie beim Schützen einer Header-Datei '#pragma once' anstelle von 'include guard' verwenden?

- [ ] Es gibt keinen Grund zu wählen, weil sie unterschiedlichen Zwecken dienen
- [x] Ein Include-Guard verwendet ein Makro, um eine einzige Einbindung zu erreichen, aber der Compiler kann nicht verhindern, dass der Programmierer dieses Makro anderswo definiert, was zu überhaupt keiner Einbindung führen würde
- [ ] '#pragma once' garantiert, dass der Header-Code niemals geändert wird, weil es vom Compiler erzwungen wird
- [ ] Include-Guards beziehen sich auf die Header-Datei im Dateisystem, nicht auf den Code, daher sind sie nicht hilfreich, wenn die Header-Datei mehr als einmal in einem Projekt existiert. Dies ist bei '#pragma once' kein Problem

#### F90. Welche der folgenden Aussagen ist gültig?

- [ ] Wir können einen neuen C++-Operator erstellen.
- [ ] Wir können die Vorrangstellung des C++-Operators ändern.
- [x] Wir können die Operator-Templates nicht ändern.
- [ ] Wir können die Assoziativität der C++-Operatoren ändern.

#### F91. Welches der folgenden wird/werden automatisch zu jeder Klasse hinzugefügt, wenn wir unsere eigenen nicht schreiben?

- [ ] Kopierkonstruktor
- [ ] Zuweisungsoperator
- [ ] Ein Konstruktor ohne Parameter
- [x] Alle oben genannten

#### F92. Die if-else-Anweisung kann durch welchen Operator ersetzt werden?

- [ ] bestimmte Struktur
- [ ] Auswahlstruktur
- [x] selektive Struktur
- [ ] Keine der oben genannten

#### F93. Welche Wahl wäre eine rekursive Lösung für das Fakultätsproblem n!?

- [ ] &shy;

```cpp
void fact(int n) {
    if (n <= 0)
        return 0;
    else
        return 1;
}
```

- [ ] &shy;

```cpp
int fact(int n) {
    if (n <= 0)
        return 1;
    else
        return (fact(n) * (n-1));
}
```

- [ ] &shy;

```cpp
int fact(int n) {
    if (n >= 0)
        return 1;
    else
        return (fact(n-1) * n);
}
```

- [x] &shy;

```cpp
int fact(int n) {
    if (n <= 0)
        return 1;
    else
        return (fact(n-1) * n);
}
```

#### F94. Ein Klassen-Destruktor kann in verschiedenen Situationen aufgerufen werden. Welche Wahl ist keine dieser Situationen?

- [ ] Das Programm wird beendet. Dies ruft den Destruktor von Objekten mit statischer Dauer auf.
- [ ] Die delete()-Funktion wird für einen Objektzeiger aufgerufen, der mit dem new-Operator zugewiesen wurde.
- [x] Der Garbage Collector erkennt, dass ein Objekt nicht mehr verwendet wird.
- [ ] Ein Objekt mit automatischer Speicherdauer verlässt den Gültigkeitsbereich.

#### F95. Sie entwerfen ein Devisenzahlungssystem in C++. Sie müssen eine Transaktion einer Währung modellieren, die eine Ganzzahl als Menge und einen Float als Preis hat. Dann möchten Sie ein tatsächliches Objekt dieses Typs deklarieren. Wie erreichen Sie dies?

- [x] A

```cpp
struct currencyDeal {
    float price;
    int quantity;
};

currencyDeal firstDeal;
```

- [ ] B

```cpp
union currencyDeal {
    float price;
    int quantity;
};

currencyDeal firstDeal;
```

- [ ] C

```cpp
struct currencyDeal {
    float price;
    int quantity;
};
```

- [ ] D

```cpp
union currencyDeal {
    float price;
    int quantity;
};
```

#### F96. Was passiert, wenn Sie versuchen, diese Funktion mit checkConcatThreshold("a"); aufzurufen?

```cpp
int checkConcatThreshold(string a, string b) {
    return (a + b).length () > 120;
}
```

- [ ] Eine Kompilierungswarnung tritt auf und das zweite Argument erhält einen Standardwert von b.
- [ ] Eine Kompilierungswarnung tritt auf und das zweite Argument erhält einen Standardwert der leeren Zeichenkette.
- [x] Ein Kompilierungsfehler tritt auf.
- [ ] Es treten keine Kompilierungsfehler und keine Kompilierungswarnungen auf.

#### F97. Sie müssen eine C++-Lambda-Funktion definieren. Sie möchten, dass die Funktion nur Zugriff auf die Variablen hat, die lokal für sie sind. Die Funktion soll einen einzigen Parameter, einen Namen, empfangen und eine einfache Begrüßung konstruieren. Wie erreichen Sie dies?

- [ ] A

```cpp
auto myVeryFirstLambda = [=] (string name) {
        return "Hello " + name + "!";
    };
```

- [ ] B

```cpp
myVeryFirstLambda = [&] (string name) {
        return "Hello " + name + "!";
    };
```

- [x] C

```cpp
auto myVeryFirstLambda = [] (string name) {
        return "Hello " + name + "!";
    };
```

- [ ] D

```cpp
myVeryFirstLambda = [] (string name) {
        return "Hello " + name + "!";
    };
```

[Referenz](https://docs.microsoft.com/en-us/cpp/cpp/lambda-expressions-in-cpp?view=msvc-160)

#### F98. Was ist der Wert von X nach Ausführung dieses Codes?

```cpp
int x=10, a=-3;
X+=a;
```

- [ ] -3
- [x] 7
- [ ] 13
- [ ] 3

**Erklärung:** `+=` bedeutet Werterhöhung. Also ist `x += a` gleichwertig mit `x = x + a`

#### F99. Sobald Sie mit dem Schreiben in eine Datei fertig sind, welche Methode werden Sie auf dem `ofstream` aufrufen, um das Betriebssystem zu benachrichtigen?

- [ ] printout()
- [x] close()
- [ ] destroy()
- [ ] flush()

#### F100. Welche Wahl ist kein C++-Schlüsselwort?

- [ ] static_assert
- [ ] reinterpret_cast
- [x] comPl
- [ ] alignas

#### F101. Die size_in_bits-Funktion scheint jeden Parametertyp zu akzeptieren. Dies kann durch Überladen der Funktion erreicht werden oder indem der Compiler sich darum kümmert, indem ein Template geschrieben wird. Welche Wahl ist eine Implementierung dieses Templates?

```cpp
int main()
{
cout « size_in_bits(21) « endl;
cout « size_in_bits('f') « endl;
cout « size_in_bits(32.1f) « endl;
cout « size_in_bits(32.1) « endl;
return 0;
}
```

- [x] A

```cpp
template <typename T>
size_t size_in_bits(const T& a){
return sizeof(a)*8;
}
```

- [ ] B

```cpp
template size_t size_in_bits(const {int,float,double,char,long}& a){
return sizeof(a)*8;
}
```

- [x] C

```cpp
template <typename T {int,float,double,char,long>
size_t size_in_bits(const T& a){
return sizeof(a)*8;
}
```

- [ ] D

```cpp
size_t size_in_bits(void * a){
return sizeof(a)*8;
}
```

#### F102. Um die Tastatur als Eingabe zu verwenden, wird die iostream-Bibliothek eingebunden. Um Eingaben aus Dateien zu lesen, welche Bibliothek wird benötigt?

- [x] fstream
- [ ] cstdlib
- [ ] filestream
- [ ] iostream

#### F103. Was wird dieses objektorientierte Programm ausgeben?

```cpp
#include <iostream>
#include <string>
using namespace std;

class Vehicle {
public:
	string fuel = "none";
};

class MotorizedVehicle : public Vehicle {
public:
	string fuel = "fossil";
};

class NextgenMotorizedVehicle : public MotorizedVehicle {
public:
	string fuel = "hydrogen";
};

int main() {
	MotorizedVehicle aCar;
	cout << aCar.fuel;
	return 0;
}
```

- [x] fossil
- [ ] fossil none
- [ ] hydrogen
- [ ] none

#### F104. Das folgende Programm verarbeitet einen Stack-Container. Was ist die Ausgabe beim Ausführen des Programms?

```cpp
#include <iostream>
#include <stack>

int main()
{
	std::stack<int> stack;
	stack.push(1);
	stack.push(2);
	stack.push(3);

	stack.pop();

	stack.push(4);

	stack.top();
	stack.pop();

	std::cout << stack.top();
}
```

- [ ] 1
- [x] 2
- [ ] 3
- [ ] 4

#Detaillierte Erklärung:

Hier sollen wir eine Stack-Datenstruktur implementieren, die dem **FILO**- oder (First IN Last Out) Prinzip folgt,
_stack.push()_ -> schiebt ein Element vom Ende in das Array.
_stack.pop()_ -> entfernt ein Element vom Ende des Arrays.
_stack.top()_ -> Gibt uns nur das oberste Element des Arrays.
Nach der Reihenfolge der Push- und Pop-Operationen: **[1,2,3]** dann wird die Pop-Funktion verwendet,
Das neu gebildete Array ist: **[1,2,4]** dann wird top verwendet, um das oberste Element '4' abzurufen, dann wird wieder die Pop-Funktion verwendet, die 4 entfernt.
Das resultierende Array ist also: 1,2.
Dann wird das oberste Element (d.h.: 2) ausgegeben.

#### F105. Welche Wahl ist eine gültige Möglichkeit, den ternären bedingten Operator zu überladen?

- [ ] `void& operator ?:(const bool cond, const void& iftrue, const void& iffalse);`
- [x] `Der ternäre Operator kann nicht überladen werden.`
- [ ] `void& operator conditional(const bool cond, const void& iftrue, const void& iffalse);`
- [ ] `void* operator ?:(const bool cond, const void* iftrue, const void* iffalse);`

[Referenz](https://en.cppreference.com/w/cpp/language/operators)

#### F106. Welche Klassenhierarchie repräsentiert ein Beispiel für Mehrfachvererbung?

- [ ] Im selben Programm leitet sich eine gegebene Klasse an verschiedenen Punkten individuell von mehr als einer verschiedenen Klasse ab.
- [ ] Eine erste Klasse leitet sich direkt und gleichzeitig von einer zweiten und dritten Klasse ab.
- [x] Im selben Programm leitet sich eine gegebene Klasse an verschiedenen Punkten individuell von mehr als zwei verschiedenen Klassen ab.
- [ ] Eine erste Klasse leitet sich von einer zweiten Klasse ab, und diese zweite Klasse ist bereits von einer dritten Klasse abgeleitet

#### F107. Was ist die korrekte Syntax, um die Nachricht in C++ auszugeben?

- [ ] Out <<"Hello world!
- [ ] Cout << Hello world! ;
- [x] cout <<"Hello world!";
- [ ] Keine der oben genannten

[Referenz](https://en.cppreference.com/w/cpp/io/cout)

#### F108. Betrachten Sie das folgende Programm. Was wird die Ausgabe/der Fehler sein?

```cpp
#include<iostream>
#include<algorithm>
#include<string.h>
using namespace std;
bool compare(char c1, char c2){
return tolower(c1) > tolower(c2);    //ZEILE-1
}
int main(){
char arr1[20] = "C++ Program", arr2[20] = "C Program";
cout << lexicographical_compare(arr1, arr1+strlen(arr1), arr2, arr2+strlen(arr2),
compare);
return 0;
}
```

- [x] 1
- [ ] 0
- [ ] -1
- [ ] Kompilierungsfehler: Funktion ist nicht definiert

[Referenz](https://www.geeksforgeeks.org/tolower-function-in-cpp/)

#### F109. Betrachten Sie das folgende Code-Segment. Füllen Sie die Lücke in ZEILE-1 aus, damit das Programm "not found" ausgibt?

```cpp
#include <iostream>
#include <algorithm>
using namespace std;
int main() {
int data[] = {1,2,3,4,5};
int key = 5;
if(binary_search(__________))    //ZEILE-1
cout << "found";
else
cout << "not found";
return 0;
}
```

- [ ] &data[0], &data[5], key
- [ ] data, data+5, key
- [x] &data[0], &data[4], key
- [x] data+1, data+4, key

[Referenz](https://www.geeksforgeeks.org/binary-search-algorithms-the-c-standard-template-library-stl/)

#### F110. Betrachten Sie das folgende Code-Segment. Was wird die Ausgabe sein?

```cpp
#include <iostream>
#include <algorithm>
using namespace std;
int main () {
int data[] = {50, 30, 40, 10, 20};
sort (&data[1], &data[4]);
for (int i = 0; i < 5; i++)
cout << data[i] << " ";
return 0;
}
```

- [ ] 10 20 30 40 50
- [ ] 10 30 40 50 20
- [x] 50 10 30 40 20
- [ ] 50 10 20 30 40

[Referenz](https://cplusplus.com/reference/algorithm/sort/)

#### F111. Betrachten Sie das folgende Code-Segment. Was wird die Ausgabe sein?

```cpp
#include <iostream>
#include <algorithm>
using namespace std;
int main() {
int element[5];
for(int i = 1; i <= 5; i++)
*(element + i - 1) = i * 5;
rotate(element, element + 4, element + 5);
rotate(element, element + 1, element + 4);
for (int i = 0; i < 5; ++i)
cout << element[i] << " ";
return 0;
}
```

- [ ] 5 10 15 20 25
- [x] 5 10 15 25 20
- [ ] 20 10 15 25 5
- [ ] 25 5 10 15 20

[Referenz](https://en.cppreference.com/w/cpp/algorithm/rotate)

#### F112. Betrachten Sie das folgende Code-Segment. Was wird die Ausgabe sein?

```cpp
#include <iostream>
#include <vector>
using namespace std;
int main() {
const int size = 3, c = 65;
vector<char> vc(size, 'A');
for (int i = 1; i <= 2; i++)
vc.push_back(65 + i);
vc.resize(10, 90);
vc.resize(8);
for (int i = 0; i < vc.size(); i++)
cout << vc[i] << " ";
return 0;
}
```

- [x] A A A B C Z Z Z
- [ ] A A B B C Z Z Z
- [ ] A A A B C Z Z
- [ ] A A A B C Z Z Z Z

[Referenz](https://en.cppreference.com/w/cpp/container/vector)

#### F113. Betrachten Sie das folgende Code-Segment. Wählen Sie die passende Option, um die Lücke in ZEILE-1 zu füllen, sodass die Ausgabe des Codes lautet: a C++ Program.

```cpp
#include <iostream>
#include <string>
using namespace std;
int main(void) {
string s1 = "C++ ";
string s2 = "Program";
__________________;    //ZEILE-1
cout << s1;
return 0;
}
```

- [x] s1 += s2
- [ ] strcat(s1, s2)
- [x] s1.append(s2)
- [ ] s1.insert(s2)

[Referenz](https://www.geeksforgeeks.org/stdstringappend-in-c/)

#### F114. Betrachten Sie das folgende Code-Segment. Füllen Sie die Lücke in ZEILE-1 aus, sodass die Ausgabe 5 2 3 4 5 ist

```cpp
#include <iostream>
#include <algorithm>
using namespace std;
int main() {
int data[] = { 1, 2, 3, 4, 5 };
for (int i = 0; i < 1; i++) {
int j = data[i];
replace(data, data + 5, j, *(_________________));    //ZEILE-1
}
for (int i = 0; i < 5; ++i)
cout << data[i] << " ";
return 0;
}
```

- [x] data + 4 - i
- [ ] data + 5 - i
- [ ] data + i - 4
- [ ] data + i - 5

[Referenz](https://www.geeksforgeeks.org/stdstringreplace-stdstringreplace_if-c/)

#### F115. Betrachten Sie das folgende Code-Segment. Was wird die Ausgabe sein?

```cpp
#include <iostream>
#include <cstring>
#include <stack>
using namespace std;
int main(){
char str[10] = "123456789";
stack<char> s1, s2;
int i;
for(i = 0; i < strlen(str)/2; i++)
s1.push(str[i]);
for(i=i-1; i < strlen(str); i++)
s2.push(str[i]);
while (!s1.empty()) {
s2.push(s1.top()); s1.pop();
}
while (!s2.empty()) {
cout << s2.top(); s2.pop();
}
return 0;
}
```

- [x] 1234987654
- [ ] 123498765
- [ ] 1234897654
- [ ] 123459876

[Referenz](https://en.cppreference.com/w/cpp/container/stack)

#### F116. Betrachten Sie das folgende Code-Segment. Welche Anweisung(en) ist/sind korrekt?

```cpp
int i = 5;
const int *p = &i;
int * const q = &i;
int const *r = &i;
int const * const s = &i;
*p = 10; //ANWEISUNG-1
*q = 10; //ANWEISUNG-2
*r = 10; //ANWEISUNG-3
*s = 10; //ANWEISUNG-4
```

- [ ] ANWEISUNG-1
- [x] ANWEISUNG-2
- [ ] ANWEISUNG-3
- [ ] ANWEISUNG-4

[Referenz](https://www.geeksforgeeks.org/const-keyword-in-cpp/)

#### F117. Betrachten Sie das folgende Programm. Was wird die Ausgabe/der Fehler sein?

```cpp
#include <iostream>
using namespace std;
char add(char c1 = 'a') { return c1; }
char add(char c1 = 'a', char c2 = 'b') { return c1 + c2 - 'a';}
char add(char c1 = 'a', int d1 = 100){ return c1 + d1 - 'a'; }
char add(char c1 = 'a', char c2 = 'b', char c3) { return c1 + c2 + c3 - 'a'; }
int main() {
char c = add('o', 'k');
cout << c << endl;
return 0;
}
```

- [ ] y
- [ ] z
- [x] Kompilierungsfehler: Standardargument fehlt für "char add(char, char, char)"
- [x] Kompilierungsfehler: Aufruf von Überladung "add(char, char)" ist mehrdeutig

[Referenz](https://learn.microsoft.com/en-us/cpp/cpp/function-overloading?view=msvc-170)

#### F118. Betrachten Sie das folgende Code-Segment. Was wird die Ausgabe sein?

```cpp
#include <iostream>
using namespace std;
#define SQR(x) (x)*(x)
int main() {
int a=3;
cout << SQR(a++) << endl;
return 0;
}
```

- [x] 12
- [ ] 25
- [ ] 9
- [ ] 16

[Referenz](https://www.geeksforgeeks.org/output-of-the-program-use-macros-carefully/)

#### F119. Betrachten Sie das folgende Code-Segment. Welche Zeile(n) wird/werden Ihnen einen Fehler geben?

```cpp
#include<iostream>
#define X 1
using namespace std;
int main(){
int i;
const int i1 = 2;
const int i2 = i1; //ZEILE-1
i2 = X;
i = i1;
i1 = i;
return 0;
//ZEILE-2
//ZEILE-3
//ZEILE-4
}
```

- [ ] ZEILE-1
- [x] ZEILE-2
- [ ] ZEILE-3
- [x] ZEILE-4

#### F120. Betrachten Sie das folgende Code-Segment. Was wird die Ausgabe/der Fehler sein?

```cpp
#include<iostream>
using namespace std;
int main(){
int a = 5;
int &b = a+1;
a = a*b;
cout << a << " " << b;
return 0;
}
```

- [ ] 36
- [ ] 30
- [ ] 25
- [x] Kompilierungsfehler: ungültige Initialisierung einer Nicht-const-Referenz

#Detaillierte Erklärung:
Der Fehler tritt auf, weil versucht wird, eine Referenz auf einen temporären Wert zu erstellen. In der Zeile int &b = a+1; versuchen wir, eine Referenz b auf das Ergebnis des Ausdrucks a + 1 zu erstellen, was ein temporärer Wert ist. Referenzen müssen an ein tatsächliches Objekt gebunden werden, nicht an einen temporären Wert oder einen Ausdruck, der keine Speicheradresse hat.

#### F121. Betrachten Sie das folgende Code-Segment. Was wird die Ausgabe sein?

```cpp
#include <iostream>
using namespace std;
int& func(int& i) {     //ZEILE-1
return i = i+5;
}
int main() {
int x = 1, y = 2;
int& z = func(x);
cout << x << " " << z << " ";
func(x) = y;
cout << x << " " << z;
return 0;
}
```

- [x] 6 6 2 2
- [ ] 6 6 7 7
- [ ] 1 1 2 2
- [ ] 1 1 7 7

[Referenz](https://www.ibm.com/docs/en/zos/2.4.0?topic=calls-pass-by-reference-c-only)

#### F122. Betrachten Sie das folgende Code-Segment. Wählen Sie die passende Option, um die Lücken in ZEILE-1 zu füllen, sodass die Ausgabe des Codes lautet: 300 20000.

```cpp
#include <iostream>
using namespace std;
void compute(int n1, int n2, ________, ________){ //ZEILE-1
n3 = n1 + n2;
*n4 = n1 * n2;
}
int main(){
int a = 100, b = 200, c = 0, d = 0;
compute(a, b, c, &d); //ZEILE-2
cout << c << ", ";
cout << d;
return 0;
}
```

- [ ] int n3, int\* n4
- [x] int& n3, int \*n4
- [ ] int* n3, int* n4
- [ ] int& n3, int& n4

#### F123. Betrachten Sie das folgende Code-Segment. Was wird die Ausgabe/der Fehler sein?

```cpp
#include <iostream>
using namespace std;
int main() {
int a = 2, *b;
*b = 5;
int * const ptr;    // ZEILE-1
// ZEILE-2
ptr = b;
cout << *ptr;
return 0;
}
```

- [ ] `<Müllwert>`
- [ ] 5
- [x] Kompilierungsfehler bei ZEILE-1: nicht initialisiertes const 'ptr'
- [x] Kompilierungsfehler bei ZEILE-2: Zuweisung der schreibgeschützten Variable 'ptr'

#### F124. Betrachten Sie das folgende Code-Segment. Was wird die Ausgabe/der Fehler sein?

```cpp
#include <iostream>
using namespace std;
void fun(int a = 5) { cout << a << endl; }
//ZEILE-1
int fun(int x = 10) { cout << x << endl; return 0; }    //ZEILE-2
int main() {
fun();
return 0;
}
```

- [ ] 5
- [ ] 10
- [ ] 5
- [x] Kompilierungsfehler bei ZEILE-2: mehrdeutige neue Deklaration von 'int fun(int)'

#### F125. Betrachten Sie das folgende Code-Segment. Füllen Sie die Lücke in ZEILE-1 aus, sodass das Programm 5 + i3 ausgibt

```cpp
#include<iostream>
using namespace std;
struct complex{
int re, im;
void show(){ cout << re << " + i" << im; }
};
______________________________________{ //Zeile-1
c2.re = c1.re+c2.re;
c2.im = c1.im+c2.im;
return c2;
}
int main(){
struct complex c1={2,5},c2{3,-2};
struct complex t = c1 + c2;
t.show();
return 0;
}
```

- [x] complex operator+(complex &c1, complex &c2)
- [ ] complex operator+(const complex &c1, const complex &c2)
- [ ] operator+(complex &c1, complex &c2)
- [ ] complex +(complex &c1, complex &c2)

[Referenz](https://www.w3schools.com/cpp/cpp_structs.asp)

#### F126. Betrachten Sie das folgende Programm. Welche Zeile(n) wird/werden einen Fehler erzeugen?

```cpp
#include<iostream>
using namespace std;
class myClass{
int pra = 5;
public:
int pub = 10;
void set_pr(int x){ pra = x; }
void set_pu(int x){ pub = x; }
};
int main(){
myClass m;
int a, b;
a = m.pra; //ZEILE-1
b = m.pub; //ZEILE-2
m.set_pr(100); //ZEILE-3
m.set_pu(200); //ZEILE-4
return 0;
}
```

- [x] ZEILE-1
- [ ] ZEILE-2
- [ ] ZEILE-3
- [ ] ZEILE-4

[Referenz](https://stackoverflow.com/questions/4855422/c-classes-public-private-and-protected)

#### F127. Betrachten Sie die folgende Klasse. Füllen Sie die Lücken mit geeigneten Zugriffsspezifizierern aus, sodass Mitglied y von außerhalb der Klasse zugegriffen werden kann, aber Mitglied x nicht.

```cpp
class Test{
________:
int x;
________:
int y;
/* Weiterer Code */
};
```

- [ ] public, public
- [ ] public, private
- [ ] private, public
- [x] private, private

#### F128. Welcher C++-Standard hat In-Class-Standard-Mitgliedsinitialisierungen hinzugefügt?

- [ ] C++98
- [x] C++11
- [ ] C++14
- [ ] C++17.

#### F129. Können Sie auto-Typ-Ableitung für nicht-statische Datenmitglieder verwenden?

- [ ] Ja, seit C++11
- [x] Nein
- [ ] Ja, seit C++20

#### F130. Müssen Sie ein static inline Datenmitglied in einer cpp-Datei definieren?

- [x] Nein, die Definition erfolgt an derselben Stelle, an der ein static inline Mitglied deklariert wird.
- [ ] Ja, der Compiler benötigt die Definition in einer cpp-Datei.
- [ ] Ja, der Compiler benötigt eine Definition in allen Übersetzungseinheiten, die diese Variable verwenden.

[Referenz](https://en.cppreference.com/w/cpp/language/bit_field)

#### F131. Was ist die Ausgabe des folgenden Codes:

```cpp
struct S {
    int a { 10 };
    int b { 42 };
};
S s { 1 };
std::cout << s.a << ", " << s.b;
```

- [ ] Ausgabe ist: 1, 0
- [ ] Ausgabe ist: 10, 42
- [x] Ausgabe ist: 1, 42

#### F132. Kann eine static inline Variable nicht-konstant sein?

- [x] Ja, es ist einfach eine reguläre Variable.
- [ ] Nein, inline Variablen müssen konstant sein.

#### F133. Betrachten Sie den folgenden Code:

```cpp
struct C {
    C(int x) : a(x) { }
    int a { 10 };
    int b { 42 };
};
C c(0);

```

- [ ] C::a wird zweimal initialisiert. Das erste Mal wird es mit 10 initialisiert, dann das zweite Mal mit 0 im Konstruktor.
- [x] C::a wird nur einmal mit 0 im Konstruktor initialisiert.
- [ ] Der Code kompiliert nicht, weil der Compiler nicht entscheiden kann, wie das Mitglied C::a initialisiert werden soll.
- [ ] 2 Bytes

#### F134. Was passiert, wenn Sie eine Ausnahme aus einem Konstruktor werfen?

- [ ] Das Objekt wird als "erstellt" betrachtet, sodass es dem regulären Lebenszyklus eines Objekts folgt.
- [x] Das Objekt wird als "teilweise erstellt" betrachtet, und daher wird der Compiler seinen Destruktor nicht aufrufen.
- [ ] Der Compiler ruft std::terminate auf, da Sie keine Ausnahmen aus Konstruktoren werfen können.

#### F135. Was passiert, wenn Sie diesen Code kompilieren?

```cpp
struct Point { int x; int y; };
Point pt {.y = 10, .x = 11 };
std::cout << pt.x << ", " << pt.y;
```

- [x] Der Code kompiliert nicht. Designatoren müssen in derselben Reihenfolge wie die Datenmitglieder in der Point-Klasse sein.
- [ ] Der Code kompiliert und gibt 11, 10 aus.
- [ ] Der Code kompiliert und gibt 10, 11 aus.

#### F136. Wird dieser Code in C++11 funktionieren?

```cpp
struct User { std::string name = "unknown"; unsigned age { 0 }; };
User u { "John", 101 };
```

- [ ] Ja, der Code kompiliert im C++11-Modus.
- [x] Der Code kompiliert ab C++14-Modus.
- [ ] Der Code kompiliert auch in C++20 nicht.

#### F137. Angenommen, Sie haben ein std::map<string, int> m;. Wählen Sie die einzige wahre Aussage über die folgende Schleife:

```cpp
for (const pair<string, int>& elem : m)
```

- [x] A Die Schleife iteriert ordnungsgemäß über die Map und erstellt keine zusätzlichen Kopien.

- [ ] B Die Schleife erstellt eine Kopie jedes Elements in der Map, da der Typ von elem nicht übereinstimmt.

- [ ] C Der Code kompiliert nicht, da ein const pair nicht an eine Map gebunden werden kann.

#### F138. Identifizieren Sie die korrekte Erweiterung der benutzerdefinierten Header-Datei in C++.

- [ ] .cpp
- [ ] .hg
- [x] .h
- [ ] .hf

#### F139. Identifizieren Sie den falschen Konstruktortyp.

```cpp
auto x = 4000.22;
```

- [x] Friend-Konstruktor
- [ ] Standard-Konstruktor
- [ ] Parametrisierter Konstruktor
- [ ] Kopierkonstruktor

#### F140. Welcher der folgenden Datentypen wird in C++ unterstützt, aber nicht in C?

- [x] bool
- [ ] int
- [ ] double
- [ ] float

[Referenz]: https://stackoverflow.com/questions/1608318/is-bool-a-native-c-type

#### F141. Identifizieren Sie die korrekte Syntax zum Deklarieren von Arrays in C++.

- [x] int arr[10]
- [ ] array arr[10]
- [ ] array{10}
- [ ] int arr

[Referenz]: (https://en.cppreference.com/w/cpp/language/array)

#### F142. Die Größe von wchat_t ist.

- [ ] 2
- [ ] 4
- [ ] 2 oder 4
- [x] Hängt von der Anzahl der Bits im System ab

#### F143. Welche der folgenden Schleifen ist am besten, wenn wir die Anzahl der Iterationen kennen?

- [ ] while
- [x] for
- [ ] do
- [ ] Alle oben genannten

#### F144. Welches Schlüsselwort wird verwendet, um Makros in C++ zu definieren?

- [ ] #macro
- [x] #define
- [ ] macro
- [ ] keyword

#### F145. Welche der folgenden Operatoren sollte vorzugsweise als globale Funktion anstelle einer Mitgliedsmethode überladen werden?

- [ ] Postfix ++
- [x] Vergleichsoperator
- [ ] Einfügeoperator <<
- [ ] Präfix++

#### F146. Wie können wir die dynamische Zuweisung von Objekten einer Klasse mit new einschränken?

- [ ] Durch Überladen des new-Operators
- [ ] Durch Erstellen eines leeren privaten new-Operators.
- [x] Durch Erstellen leerer privater new- und new[]-Operatoren
- [ ] Durch Überladen von new-Operatoren und new[]-Operatoren

#### F147. Was ist die Zeitkomplexität des folgenden Codes?

```cpp
for(int i=0;i<n;i++){
   for(int j=0;j<n;j++){
       cout<<"hello";
    }
}
```

- [ ] O(n^3)
- [x] O(n^2)
- [ ] O(n)
- [ ] O(1)

[Referenz](<https://medium.com/enjoy-algorithm/analysis-of-loop-in-programming-cc9a644ef8cd#:~:text=At%20each%20step%20of%20the%20iteration%2C%20the%20nested%20loop%20is,%20%3D%20O(n%C2%B2)>)

#### F148. Was ist die Ausgabe des unten angegebenen Codes?

```cpp
int a=10;
int k=++a;
int m=a++;
cout<<k+m;
```

- [ ] 20
- [ ] 21
- [x] 22
- [ ] 23

Sowohl **++a** als auch **a++** erhöhen den Wert von a um 1 (d.h.: 11) und daher wird k+m zu 22.

#### F149. Welches C++-Konstrukt wird für die Ausnahmebehandlung verwendet?

- [x] try-catch
- [ ] if-else
- [ ] for-Schleife
- [ ] switch-case

#### F150. Was ist der Zweck der `break`-Anweisung in einer Schleife in C++?

- [ ] Das Programm beenden
- [ ] Die aktuelle Iteration überspringen und mit der nächsten fortfahren
- [x] Die Schleife beenden
- [ ] Einen Wert zurückgeben

[Referenz]: (https://www.tutorialspoint.com/cprogramming/c_break_statement.htm)

#### F151. Was ist in C++ der Zweck des `const`-Schlüsselworts, wenn es mit einer Variablen verwendet wird?

- [x] Es macht die Variable unveränderlich
- [ ] Es ändert den Datentyp
- [ ] Es definiert eine konstante Funktion
- [ ] Es macht die Variable zu einem Zeiger

#### F152. Was ist effektiver beim Aufrufen von C++-Funktionen?

- [x] Call by reference
- [ ] Call by value
- [ ] Call by pointer
- [ ] Call by object

[Referenz]: (https://www.algbly.com/More/MCQs/Cpp-mcq/Cpp-functions.html)

#### F153. Was wird die Ausgabe des folgenden C++-Programms sein?

```cpp
#include <iostream>
using namespace std;
class A{
public:
	A(){
		cout<<"Constructor called\n";
	   }
	~A(){
		cout<<"Destructor called\n";
	    }
};
int main(int argc, char const *argv[])
{
	A *a = new A[5];
	delete[] a;
	return 0;
}
```

- [ ] Segmentierungsfehler
- [x] "Constructor called" fünfmal und dann "Destructor called" fünfmal
- [ ] "Constructor called" fünfmal und dann "Destructor called" einmal
- [ ] Fehler

#### F154. Welche Wahl steht _nicht_ im Zusammenhang mit der Deklaration der Mitgliedsvariablen count als static in my_class?

```cpp
class my_class{
    public: static int count;
}
```

- [ ] Alle Objekte, die versuchen, auf ihre count-Mitgliedsvariable zuzugreifen, verweisen tatsächlich auf die einzige klassengebundene statische count-Variable.
- [ ] Die Variable existiert auch dann, wenn keine Objekte der Klasse definiert wurden, sodass sie an jedem Punkt im Quellcode modifiziert werden kann.
- [x] Die Variable kann von keinem Teil des Codes in derselben Anwendung oder Thread modifiziert werden. Andere Threads können sie jedoch modifizieren.
- [ ] Die Variable wird nur einmal zugewiesen, unabhängig davon, wie viele Objekte instanziiert werden, da sie an die Klasse selbst gebunden ist, nicht an ihre Instanzen.

#### F155. Was ist der Zweck des `constexpr`-Schlüsselworts in C++?

- [ ] Es wird verwendet, um Konstanten in C++ zu definieren.
- [ ] `constexpr` wird verwendet, um anzugeben, dass eine Variable ein konstanter Zeiger ist.
- [x] `constexpr` wird verwendet, um anzuzeigen, dass ein Ausdruck zur Kompilierzeit ausgewertet werden kann, wodurch er für die Verwendung in konstanten Ausdrücken geeignet ist.
- [ ] Es ist ein Schlüsselwort, das zum Erstellen asynchroner Funktionen verwendet wird.

[Ref](https://learn.microsoft.com/en-us/cpp/cpp/constexpr-cpp?view=msvc-170#:~:text=constexpr%20indicates%20that%20the%20value,template%20arguments%20and%20array%20declarations.)

#### F156. Was ist ein Template-Metaprogramm in C++?

- Ref(https://www.geeksforgeeks.org/template-metaprogramming-in-c/)

- [ ] Ein Template-Metaprogramm ist eine hochrangige Programmiersprache.
- [ ] Es bezieht sich auf Metaprogrammierung, die Templates in C++ verwendet.
- [ ] Es ist eine Art Benutzeroberflächen-Designmuster.
- [x] Ein Template-Metaprogramm ist eine Kompilierzeitberechnung, bei der Templates und Template-Spezialisierung verwendet werden, um Berechnungen zur Kompilierzeit durchzuführen.

#### F157. Identifizieren Sie das korrekte Beispiel für einen Prä-Inkrement-Operator.

- [x] ++i
- [ ] i++
- [ ] --i
- [ ] +i

#### F158. Was wird die Ausgabe des folgenden Codes sein?

```cpp
{% raw %}
int matrix[3][3] = {{1, 2, 3},{4, 5, 6},{7, 8, 9}};
for(int i=0;i<3;i++){
    for(int j=0;j<3;j++){
        int a = matrix[i][j];
        matrix[i][j] = matrix[j][i];
        matrix[j][i] = a;
    }
}
{% endraw %}
```

- [ ] Transponierte der Matrix
- [x] Dieselbe Matrix
- [ ] Spiegelbild der Matrix
- [ ] Invertierte Matrix

#### F159. Was ist eine Race Condition in C++?

- [ ] Eine Bedingung, bei der das Programm schneller als erwartet läuft
- [x] Eine Bedingung, bei der mehrere Threads gleichzeitig auf gemeinsame Daten zugreifen und das Ergebnis vom Timing ihrer Ausführung abhängt
- [ ] Eine Bedingung, bei der zwei Threads um CPU-Zeit konkurrieren
- [ ] Eine Bedingung, bei der eine Schleife zu schnell ausgeführt wird und verlangsamt werden muss

[Referenz](https://en.cppreference.com/w/cpp/language/memory_model)

#### F160. Betrachten Sie den folgenden Code, der eine Race Condition hat. Was ist der richtige Weg, ihn zu beheben?

```cpp
#include <thread>
#include <vector>

int counter = 0;

void incrementCounter() {
    for(int i = 0; i < 1000; i++) {
        counter++;
    }
}

int main() {
    std::vector<std::thread> threads;
    for(int i = 0; i < 10; i++) {
        threads.push_back(std::thread(incrementCounter));
    }
    for(auto& t : threads) {
        t.join();
    }
    return 0;
}
```

- [ ] `volatile`-Schlüsselwort hinzufügen: `volatile int counter = 0;`
- [x] `std::mutex` verwenden, um um `counter++` im kritischen Abschnitt zu sperren/entsperren
- [ ] `std::this_thread::sleep_for()` verwenden, um jedes Inkrement zu verzögern
- [ ] `counter++` zu `++counter` ändern für atomare Operation

[Referenz](https://en.cppreference.com/w/cpp/thread/mutex)

#### Q161. Was ist der Zweck von `std::move` in C++11?

- [ ] Ein Objekt an einen neuen Speicherort zu kopieren
- [x] Ein Objekt in eine Rvalue-Referenz umzuwandeln, um Move-Semantik zu ermöglichen
- [ ] Speicher physisch von einer Adresse zu einer anderen zu verschieben
- [ ] Ein Objekt zu löschen und ein neues zu erstellen

**Erklärung:**
`std::move` ist eine Umwandlung, die eine Rvalue-Referenz auf ihr Argument erzeugt und ermöglicht, dass Ressourcen verschoben statt kopiert werden. Es verschiebt selbst nichts, sondern ermöglicht den Aufruf von Move-Konstruktoren und Move-Zuweisungsoperatoren.

[Referenz](https://en.cppreference.com/w/cpp/utility/move)

#### Q162. Was ist die Ausgabe dieses Codes?

```cpp
#include <iostream>
#include <vector>

int main() {
    std::vector<int> v1 = {1, 2, 3};
    std::vector<int> v2 = std::move(v1);
    std::cout << v1.size() << " " << v2.size();
    return 0;
}
```

- [ ] 3 3
- [x] 0 3
- [ ] 3 0
- [ ] Kompilierungsfehler

**Erklärung:**
Nach `std::move(v1)` befindet sich v1 in einem gültigen, aber nicht spezifizierten Zustand. Typischerweise wird es leer (Größe 0) und v2 übernimmt den Besitz der Elemente.

[Referenz](https://en.cppreference.com/w/cpp/utility/move)

#### Q163. Was ist ein Lambda-Ausdruck in C++?

- [ ] Eine mathematische Funktion
- [x] Ein anonymes Funktionsobjekt, das Variablen aus seinem umgebenden Bereich erfassen kann
- [ ] Eine Template-Funktion
- [ ] Eine Makro-Definition

**Erklärung:**
Lambda-Ausdrücke, eingeführt in C++11, ermöglichen das Schreiben von Inline-anonymen Funktionen. Sie können Variablen aus dem umgebenden Bereich erfassen und werden oft mit STL-Algorithmen verwendet.

[Referenz](https://en.cppreference.com/w/cpp/language/lambda)

#### Q164. Was macht das Schlüsselwort `auto` in C++11?

- [ ] Gibt einer Variablen automatische Speicherdauer
- [x] Leitet automatisch den Typ einer Variablen aus ihrem Initialisierer ab
- [ ] Macht eine Funktion inline
- [ ] Deklariert eine globale Variable

**Erklärung:**
Das Schlüsselwort `auto` in C++11 ermöglicht die automatische Typableitung aus dem Initialisierer, was den Code prägnanter und wartungsfreundlicher macht.

[Referenz](https://en.cppreference.com/w/cpp/language/auto)

#### Q165. Was ist der Unterschied zwischen `std::unique_ptr` und `std::shared_ptr`?

- [x] unique_ptr hat exklusiven Besitz, shared_ptr erlaubt mehrere Besitzer
- [ ] unique_ptr ist schneller, aber weniger sicher
- [ ] shared_ptr kann nur mit Klassen verwendet werden
- [ ] Es gibt keinen Unterschied

**Erklärung:**
`std::unique_ptr` bietet exklusiven Besitz - nur ein unique_ptr kann eine Ressource besitzen. `std::shared_ptr` verwendet Referenzzählung, um mehreren shared_ptrs den Besitz derselben Ressource zu ermöglichen.

[Referenz](https://en.cppreference.com/w/cpp/memory/unique_ptr)

#### Q166. Was ist RAII in C++?

- [ ] Random Access Iterator Interface
- [x] Resource Acquisition Is Initialization (Ressourcenerwerb ist Initialisierung)
- [ ] Recursive Algorithm Implementation Interface
- [ ] Runtime Allocation and Initialization

**Erklärung:**
RAII ist ein C++-Programmieridiom, bei dem der Ressourcenerwerb an die Objektlebensdauer gebunden ist. Ressourcen werden in Konstruktoren erworben und in Destruktoren freigegeben, was eine ordnungsgemäße Bereinigung sicherstellt.

[Referenz](https://en.cppreference.com/w/cpp/language/raii)

#### Q167. Was ist die Ausgabe dieses Codes?

```cpp
#include <iostream>

int main() {
    int x = 5;
    auto lambda = [x]() mutable { x += 10; return x; };
    std::cout << lambda() << " " << x;
    return 0;
}
```

- [ ] 5 5
- [x] 15 5
- [ ] 15 15
- [ ] 5 15

**Erklärung:**
Das Lambda erfasst x per Wert. Das Schlüsselwort `mutable` erlaubt die Änderung der erfassten Kopie. Das ursprüngliche x bleibt unverändert.

[Referenz](https://en.cppreference.com/w/cpp/language/lambda)

#### Q168. Was ist `constexpr` in C++11?

- [ ] Ein konstanter Ausdruck, der nur mit ganzen Zahlen verwendet werden kann
- [x] Spezifiziert, dass eine Funktion oder Variable zur Kompilierzeit ausgewertet werden kann
- [ ] Ein Makro zur Definition von Konstanten
- [ ] Ein Schlüsselwort zur Deklaration konstanter Zeiger

**Erklärung:**
`constexpr` gibt an, dass ein Wert oder eine Funktion zur Kompilierzeit ausgewertet werden kann, was Kompilierzeitberechnungen und Optimierungen ermöglicht.

[Referenz](https://en.cppreference.com/w/cpp/language/constexpr)

#### Q169. Was ist der Zweck von `std::forward`?

- [ ] Ein Objekt im Speicher nach vorne zu verschieben
- [x] Die Wertkategorie (Lvalue/Rvalue) eines weitergeleiteten Arguments zu bewahren
- [ ] Vorwärts durch einen Container zu iterieren
- [ ] Eine Vorwärtsdeklaration zu deklarieren

**Erklärung:**
`std::forward` wird in Template-Funktionen verwendet, um Argumente perfekt weiterzuleiten und dabei ihre Wertkategorie zu bewahren, was für die Implementierung der perfekten Weiterleitung wesentlich ist.

[Referenz](https://en.cppreference.com/w/cpp/utility/forward)

#### Q170. Was ist ein variadisches Template?

- [ ] Ein Template mit variierenden Rückgabetypen
- [x] Ein Template, das eine variable Anzahl von Template-Parametern akzeptiert
- [ ] Ein Template, das mehrfach instanziiert werden kann
- [ ] Ein Template mit optionalen Parametern

**Erklärung:**
Variadische Templates, eingeführt in C++11, ermöglichen Templates, eine beliebige Anzahl von Template-Argumenten zu akzeptieren, was flexible generische Programmierung ermöglicht.

[Referenz](https://en.cppreference.com/w/cpp/language/parameter_pack)

#### Q171. Was repräsentiert `nullptr`?

- [ ] Ein Null-Zeichen
- [x] Eine Nullzeiger-Konstante mit dem Typ std::nullptr_t
- [ ] Eine leere Zeichenkette
- [ ] Nullwert

**Erklärung:**
`nullptr` ist ein Schlüsselwort, das in C++11 eingeführt wurde und einen Nullzeiger repräsentiert. Es ist typsicher im Gegensatz zu NULL oder 0.

[Referenz](https://en.cppreference.com/w/cpp/language/nullptr)

#### Q172. Was ist die Ausgabe dieses Codes?

```cpp
#include <iostream>
#include <memory>

int main() {
    std::shared_ptr<int> p1 = std::make_shared<int>(42);
    std::shared_ptr<int> p2 = p1;
    std::cout << p1.use_count();
    return 0;
}
```

- [ ] 1
- [x] 2
- [ ] 42
- [ ] 0

**Erklärung:**
Sowohl p1 als auch p2 teilen sich den Besitz derselben ganzen Zahl, daher ist die Referenzzahl 2.

[Referenz](https://en.cppreference.com/w/cpp/memory/shared_ptr)

#### Q173. Was ist `std::optional` in C++17?

- [ ] Ein optionaler Parameter in einer Funktion
- [x] Ein Wrapper, der möglicherweise einen Wert enthält oder nicht
- [ ] Ein Template für optionale Kompilierung
- [ ] Ein Schlüsselwort für optionale Typen

**Erklärung:**
`std::optional` ist eine Template-Klasse, die einen optionalen Wert repräsentiert - sie enthält entweder einen Wert oder ist leer und bietet eine typsichere Möglichkeit, "kein Wert" darzustellen.

[Referenz](https://en.cppreference.com/w/cpp/utility/optional)

#### Q174. Was ist strukturierte Bindung in C++17?

```cpp
auto [x, y, z] = std::make_tuple(1, 2, 3);
```

- [ ] Eine Möglichkeit, Strukturen miteinander zu verbinden
- [x] Eine Funktion, die Tupel-ähnliche Objekte in einzelne Variablen entpackt
- [ ] Eine Methode zum Erstellen strukturierter Daten
- [ ] Eine Bindung für Strukturmitglieder

**Erklärung:**
Strukturierte Bindungen ermöglichen das Zerlegen von Objekten in ihre Bestandteile, was den Code lesbarer macht, wenn man mit Tupeln, Paaren oder Strukturen arbeitet.

[Referenz](https://en.cppreference.com/w/cpp/language/structured_binding)

#### Q175. Was ist `std::string_view` in C++17?

- [ ] Eine Ansicht einer Zeichenkette in einer GUI
- [x] Eine nicht-besitzende Referenz auf eine Zeichenkette, die Kopieren vermeidet
- [ ] Eine Zeichenkette, die nur angezeigt, nicht geändert werden kann
- [ ] Eine View-Klasse zur Anzeige von Zeichenketten

**Erklärung:**
`std::string_view` bietet eine leichtgewichtige, nicht-besitzende Referenz auf eine Zeichenkette, vermeidet unnötige Kopien und verbessert die Leistung.

[Referenz](https://en.cppreference.com/w/cpp/string/basic_string_view)

#### Q176. Was sind Konzepte in C++20?

- [ ] Abstrakte Ideen in der Programmierung
- [x] Benannte Anforderungssätze für Template-Parameter
- [ ] Konzeptionelle Entwurfsmuster
- [ ] Dokumentationskommentare

**Erklärung:**
Konzepte sind eine C++20-Funktion, die es ermöglicht, Einschränkungen für Template-Parameter zu spezifizieren, wodurch Template-Code lesbarer wird und bessere Fehlermeldungen bereitgestellt werden.

[Referenz](https://en.cppreference.com/w/cpp/language/constraints)

#### Q177. Was ist der Drei-Wege-Vergleichsoperator (<=>) in C++20?

- [ ] Ein Vergleich von drei Werten
- [x] Ein Operator, der Ordnungsinformationen zurückgibt (kleiner, gleich, größer)
- [ ] Drei separate Vergleichsoperatoren
- [ ] Ein ternärer Vergleich

**Erklärung:**
Der Spaceship-Operator (<=>) führt einen Drei-Wege-Vergleich durch und gibt eine Ordnungskategorie zurück, was die Definition von Vergleichsoperatoren vereinfacht.

[Referenz](https://en.cppreference.com/w/cpp/language/operator_comparison)

#### Q178. Was ist `std::span` in C++20?

- [ ] Eine Zeitspannenmessung
- [x] Eine nicht-besitzende Ansicht über eine zusammenhängende Sequenz von Objekten
- [ ] Eine Spanning-Tree-Datenstruktur
- [ ] Ein Span-Element in HTML

**Erklärung:**
`std::span` bietet eine Ansicht über eine zusammenhängende Sequenz von Objekten, ohne sie zu besitzen, nützlich zum Übergeben Array-ähnlicher Daten ohne Kopieren.

[Referenz](https://en.cppreference.com/w/cpp/container/span)

#### Q179. Was ist die Ausgabe dieses Codes?

```cpp
#include <iostream>
#include <vector>

int main() {
    std::vector<int> v = {1, 2, 3, 4, 5};
    for (auto& x : v) {
        x *= 2;
    }
    std::cout << v[2];
    return 0;
}
```

- [ ] 3
- [x] 6
- [ ] 2
- [ ] 12

**Erklärung:**
Die bereichsbasierte for-Schleife mit `auto&` ändert jedes Element direkt. v[2] (ursprünglich 3) wird zu 6.

[Referenz](https://en.cppreference.com/w/cpp/language/range-for)

#### Q180. Was ist `std::variant` in C++17?

- [ ] Eine Variable, die variieren kann
- [x] Eine typsichere Union, die einen von mehreren Typen enthalten kann
- [ ] Eine Variante einer Klasse
- [ ] Ein Variables-Template

**Erklärung:**
`std::variant` ist eine typsichere Union, die einen Wert von einem von mehreren angegebenen Typen enthalten kann und eine sicherere Alternative zu C-Unions bietet.

[Referenz](https://en.cppreference.com/w/cpp/utility/variant)

#### Q181. Was ist `std::any` in C++17?

- [ ] Jede Art von Variable
- [x] Ein typsicherer Container für einzelne Werte beliebigen Typs
- [ ] Ein Wildcard-Typ
- [ ] Ein optionaler Typ

**Erklärung:**
`std::any` kann einen einzelnen Wert beliebigen kopierkonstruierbaren Typs speichern und bietet typsichere Speicherung mit Laufzeit-Typprüfung.

[Referenz](https://en.cppreference.com/w/cpp/utility/any)

#### Q182. Was ist der Unterschied zwischen `std::array` und C-Style-Arrays?

- [x] std::array kennt seine Größe und bietet Mitgliedsfunktionen
- [ ] std::array ist langsamer
- [ ] C-Style-Arrays sind sicherer
- [ ] Es gibt keinen Unterschied

**Erklärung:**
`std::array` ist ein Container, der Arrays fester Größe kapselt, Größeninformationen und STL-Container-Schnittstelle bietet und gleichzeitig die Leistung von C-Style-Arrays beibehält.

[Referenz](https://en.cppreference.com/w/cpp/container/array)

#### Q183. Was ist perfekte Weiterleitung?

- [ ] Weiterleitung ohne Fehler
- [x] Bewahren der Wertkategorie von Argumenten beim Übergeben an eine andere Funktion
- [ ] Schnelle Parameterübergabe
- [ ] Vorwärtsdeklaration von Funktionen

**Erklärung:**
Perfekte Weiterleitung verwendet `std::forward` und universelle Referenzen, um Argumente an eine andere Funktion weiterzugeben und dabei ihre Wertkategorie (Lvalue oder Rvalue) zu bewahren.

[Referenz](https://en.cppreference.com/w/cpp/utility/forward)

#### Q184. Was ist die Ausgabe dieses Codes?

```cpp
#include <iostream>

template<typename T>
void func(T&& x) {
    std::cout << std::is_lvalue_reference<T>::value;
}

int main() {
    int a = 5;
    func(a);
    return 0;
}
```

- [x] 1
- [ ] 0
- [ ] 5
- [ ] Kompilierungsfehler

**Erklärung:**
Wenn ein Lvalue an eine universelle Referenz übergeben wird, wird T als Lvalue-Referenz abgeleitet, daher ist `std::is_lvalue_reference<T>::value` wahr (1).

[Referenz](https://en.cppreference.com/w/cpp/language/reference)

#### Q185. Was ist `std::invoke` in C++17?

- [ ] Eine Funktion zum Aufrufen von Programmen
- [x] Ein Hilfsmittel zum Aufrufen beliebiger aufrufbarer Objekte mit gegebenen Argumenten
- [ ] Ein Methodenaufrufoperator
- [ ] Ein Aufrufer für Konstruktoren

**Erklärung:**
`std::invoke` bietet eine einheitliche Möglichkeit, beliebige aufrufbare Objekte (Funktion, Funktionszeiger, Mitgliedsfunktion, Funktor) mit Argumenten aufzurufen.

[Referenz](https://en.cppreference.com/w/cpp/utility/functional/invoke)

#### Q186. Was ist `if constexpr` in C++17?

- [ ] Eine konstante if-Anweisung
- [x] Eine Kompilierzeit-Bedingung, die Zweige zur Kompilierzeit verwirft
- [ ] Eine if-Anweisung, die konstant sein muss
- [ ] Eine constexpr-Funktion mit if

**Erklärung:**
`if constexpr` wertet die Bedingung zur Kompilierzeit aus und instanziiert nur den genommenen Zweig, nützlich in der Template-Metaprogrammierung.

[Referenz](https://en.cppreference.com/w/cpp/language/if)

#### Q187. Was ist ein Fold-Ausdruck in C++17?

- [ ] Ein Ausdruck, der Code faltet
- [x] Eine Möglichkeit, einen binären Operator auf alle Elemente eines Parameterpakets anzuwenden
- [ ] Ein Faltungsalgorithmus
- [ ] Ein Ausdruck zum Falten von Containern

**Erklärung:**
Fold-Ausdrücke bieten eine prägnante Syntax zum Anwenden binärer Operatoren auf Parameterpakete in variadischen Templates.

[Referenz](https://en.cppreference.com/w/cpp/language/fold)

#### Q188. Was ist die Ausgabe dieses Codes?

```cpp
#include <iostream>

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int* p = arr;
    std::cout << *(p + 3);
    return 0;
}
```

- [ ] 1
- [ ] 2
- [ ] 3
- [x] 4

**Erklärung:**
Zeigerarithmetik: p + 3 zeigt auf das 4. Element (Index 3), das ist 4.

[Referenz](https://en.cppreference.com/w/cpp/language/operator_arithmetic)

#### Q189. Was ist `std::filesystem` in C++17?

- [ ] Ein Dateisystemtreiber
- [x] Eine Bibliothek zur Durchführung von Operationen auf Dateisystemen und Pfaden
- [ ] Ein virtuelles Dateisystem
- [ ] Eine Dateistream-Klasse

**Erklärung:**
`std::filesystem` bietet Funktionen zur Durchführung von Operationen auf Dateisystemen und ihren Komponenten, wie Pfaden, regulären Dateien und Verzeichnissen.

[Referenz](https://en.cppreference.com/w/cpp/filesystem)

#### Q190. Wofür wird `std::atomic` verwendet?

- [ ] Atomenergie-Berechnungen
- [x] Thread-sichere Operationen auf gemeinsamen Variablen ohne Sperren
- [ ] Atomare Datentypen
- [ ] Unteilbare Operationen auf Atomen

**Erklärung:**
`std::atomic` bietet atomare Operationen auf gemeinsamen Variablen und gewährleistet thread-sicheren Zugriff ohne explizite Sperrung.

[Referenz](https://en.cppreference.com/w/cpp/atomic/atomic)

#### Q191. Was ist der Unterschied zwischen `std::mutex` und `std::recursive_mutex`?

- [x] recursive_mutex kann mehrfach vom selben Thread gesperrt werden
- [ ] mutex ist schneller
- [ ] recursive_mutex ist veraltet
- [ ] Es gibt keinen Unterschied

**Erklärung:**
`std::recursive_mutex` erlaubt es demselben Thread, ihn mehrfach zu sperren, während `std::mutex` zum Deadlock führen würde, wenn derselbe Thread versucht, ihn zweimal zu sperren.

[Referenz](https://en.cppreference.com/w/cpp/thread/recursive_mutex)

#### Q192. Was ist `std::future` in C++11?

- [ ] Eine zukünftige Version von C++
- [x] Ein Objekt, das Zugriff auf das Ergebnis einer asynchronen Operation bietet
- [ ] Eine zeitbasierte Klasse
- [ ] Eine zukünftige Deklaration

**Erklärung:**
`std::future` wird verwendet, um das Ergebnis einer asynchronen Operation abzurufen, die mit `std::async` oder `std::promise` gestartet wurde.

[Referenz](https://en.cppreference.com/w/cpp/thread/future)

#### Q193. Was ist die Ausgabe dieses Codes?

```cpp
#include <iostream>

class Base {
public:
    virtual void show() { std::cout << "Base"; }
};

class Derived : public Base {
public:
    void show() override { std::cout << "Derived"; }
};

int main() {
    Base* b = new Derived();
    b->show();
    delete b;
    return 0;
}
```

- [ ] Base
- [x] Derived
- [ ] Kompilierungsfehler
- [ ] Undefiniertes Verhalten

**Erklärung:**
Aufgrund virtueller Funktionspolymorphie wird die show()-Methode der Derived-Klasse aufgerufen, obwohl der Zeiger vom Typ Base\* ist.

[Referenz](https://en.cppreference.com/w/cpp/language/virtual)

#### Q194. Wofür wird `std::enable_if` verwendet?

- [ ] Um if-Anweisungen zu aktivieren
- [x] Für SFINAE-basierte bedingte Template-Instanziierung
- [ ] Um Funktionen zu aktivieren
- [ ] Um zu prüfen, ob etwas aktiviert ist

**Erklärung:**
`std::enable_if` wird für SFINAE (Substitution Failure Is Not An Error) verwendet, um Template-Spezialisierungen bedingt zu aktivieren oder zu deaktivieren.

[Referenz](https://en.cppreference.com/w/cpp/types/enable_if)

#### Q195. Was ist `std::tuple` in C++11?

- [ ] Ein Zwei-Elemente-Paar
- [x] Eine Sammlung fester Größe von heterogenen Werten
- [ ] Ein Tripel von Werten
- [ ] Ein Tupel in der Mathematik

**Erklärung:**
`std::tuple` ist eine Sammlung fester Größe, die Elemente verschiedener Typen enthalten kann und `std::pair` auf eine beliebige Anzahl von Elementen verallgemeinert.

[Referenz](https://en.cppreference.com/w/cpp/utility/tuple)

#### Q196. Was ist die Ausgabe dieses Codes?

```cpp
#include <iostream>

int main() {
    int x = 10;
    int& ref = x;
    ref = 20;
    std::cout << x;
    return 0;
}
```

- [ ] 10
- [x] 20
- [ ] Kompilierungsfehler
- [ ] Undefiniert

**Erklärung:**
ref ist eine Referenz auf x. Das Ändern von ref ändert x direkt, daher wird x zu 20.

[Referenz](https://en.cppreference.com/w/cpp/language/reference)

#### Q197. Wofür wird `std::chrono` verwendet?

- [ ] Chronologische Anordnung
- [x] Zeit-Hilfsmittel einschließlich Uhren, Zeitpunkten und Dauern
- [ ] Chronometer-Funktionen
- [ ] Verwaltung chronischer Krankheiten

**Erklärung:**
`std::chrono` ist eine Bibliothek für zeitbezogene Operationen, die Uhren, Zeitpunkte und Dauern mit Typsicherheit bereitstellt.

[Referenz](https://en.cppreference.com/w/cpp/chrono)

#### Q198. Was ist `std::regex` in C++11?

- [ ] Eine Engine für reguläre Ausdrücke
- [x] Eine Bibliothek für Musterabgleich mit regulären Ausdrücken
- [ ] Ein Textersetzungswerkzeug
- [ ] Ein Zeichenkettenformatierer

**Erklärung:**
`std::regex` bietet Unterstützung für reguläre Ausdrücke für Musterabgleich und Textverarbeitung in C++.

[Referenz](https://en.cppreference.com/w/cpp/regex)

#### Q199. Was ist `std::initializer_list`?

- [ ] Eine Liste von Initialisierern
- [x] Ein leichtgewichtiges Proxy-Objekt für den Zugriff auf Arrays von const T
- [ ] Eine Initialisierungsfunktion
- [ ] Ein Listen-Konstruktor

**Erklärung:**
`std::initializer_list` ermöglicht es Funktionen, geschweifte Klammern umschlossene Wertelisten zu akzeptieren und ermöglicht einheitliche Initialisierungssyntax.

[Referenz](https://en.cppreference.com/w/cpp/utility/initializer_list)

#### Q200. Was ist die Ausgabe dieses Codes?

```cpp
#include <iostream>

int main() {
    const int x = 10;
    int* p = const_cast<int*>(&x);
    *p = 20;
    std::cout << x;
    return 0;
}
```

- [x] 10 (undefiniertes Verhalten)
- [ ] 20
- [ ] Kompilierungsfehler
- [ ] 0

**Erklärung:**
Dies ist undefiniertes Verhalten. Das Ändern eines const-Objekts durch const_cast führt zu unvorhersehbaren Ergebnissen. Der Compiler kann aufgrund der const-Annahme optimieren.

[Referenz](https://en.cppreference.com/w/cpp/language/const_cast)

#### Q201. Was ist `std::function` in C++11?

- [ ] Eine Funktionsdeklaration
- [x] Ein universeller polymorpher Funktions-Wrapper
- [ ] Ein Funktionszeiger
- [ ] Eine Bibliothek für funktionale Programmierung

**Erklärung:**
`std::function` ist ein typgelöschter Wrapper, der jedes aufrufbare Objekt (Funktion, Lambda, Funktor) mit einer bestimmten Signatur speichern kann.

[Referenz](https://en.cppreference.com/w/cpp/utility/functional/function)

#### Q202. Wofür wird `std::bind` verwendet?

- [ ] Um Variablen zusammenzubinden
- [x] Um ein neues aufrufbares Objekt durch Binden von Argumenten an eine Funktion zu erstellen
- [ ] Um Klassen zu binden
- [ ] Um Speicher zu binden

**Erklärung:**
`std::bind` erstellt ein neues Funktionsobjekt, indem einige Argumente an eine Funktion gebunden werden, nützlich für partielle Funktionsanwendung.

[Referenz](https://en.cppreference.com/w/cpp/utility/functional/bind)

#### Q203. Worauf basiert `std::unordered_map`?

- [ ] Binärer Suchbaum
- [x] Hash-Tabelle
- [ ] Verkettete Liste
- [ ] Array

**Erklärung:**
`std::unordered_map` ist mit einer Hash-Tabelle implementiert und bietet durchschnittlich O(1) Suchzeit im Vergleich zu O(log n) für `std::map`.

[Referenz](https://en.cppreference.com/w/cpp/container/unordered_map)

#### Q204. Was ist die Ausgabe dieses Codes?

```cpp
#include <iostream>

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    std::cout << sizeof(arr) / sizeof(arr[0]);
    return 0;
}
```

- [ ] 4
- [x] 5
- [ ] 20
- [ ] 1

**Erklärung:**
sizeof(arr) gibt die Gesamtbytes, sizeof(arr[0]) gibt Bytes pro Element. Die Division ergibt die Anzahl der Elemente: 5.

[Referenz](https://en.cppreference.com/w/cpp/language/sizeof)

#### Q205. Was ist `std::make_unique` in C++14?

- [ ] Ein eindeutiger Identifikator-Generator
- [x] Eine Funktion zum Erstellen von std::unique_ptr-Objekten
- [ ] Ein Eindeutigkeitsprüfer
- [ ] Ein Ersteller eindeutiger Werte

**Erklärung:**
`std::make_unique` ist eine Hilfsfunktion, die ein `std::unique_ptr` erstellt und zurückgibt und Ausnahmesicherheit und sauberere Syntax bietet.

[Referenz](https://en.cppreference.com/w/cpp/memory/unique_ptr/make_unique)

#### Q206. Was ist `std::exchange` in C++14?

- [ ] Ein Werteaustauschprogramm
- [x] Ersetzt einen Wert und gibt den alten Wert atomar zurück
- [ ] Ein Austauschoperator
- [ ] Eine Swap-Funktion

**Erklärung:**
`std::exchange` ersetzt den Wert eines Objekts und gibt seinen alten Wert in einer einzigen Operation zurück.

[Referenz](https://en.cppreference.com/w/cpp/utility/exchange)

#### Q207. Was ist `std::apply` in C++17?

- [ ] Ein Anwendungsstarter
- [x] Ruft ein aufrufbares Objekt mit einem Tupel von Argumenten auf
- [ ] Eine Apply-Funktion
- [ ] Ein Funktionsapplikator

**Erklärung:**
`std::apply` ruft ein aufrufbares Objekt mit einem Tupel von Argumenten auf und entpackt das Tupel als Funktionsargumente.

[Referenz](https://en.cppreference.com/w/cpp/utility/apply)

#### Q208. Was ist die Ausgabe dieses Codes?

```cpp
#include <iostream>

int main() {
    int x = 5;
    int y = ++x + x++;
    std::cout << y;
    return 0;
}
```

- [ ] 11
- [ ] 12
- [x] Undefiniertes Verhalten
- [ ] 13

**Erklärung:**
Das mehrfache Ändern von x zwischen Sequenzpunkten führt zu undefiniertem Verhalten. Das Ergebnis ist unvorhersehbar.

[Referenz](https://en.cppreference.com/w/cpp/language/eval_order)

#### Q209. Was ist `std::decay` in C++11?

- [ ] Eine Decay-Funktion
- [x] Wendet Array-zu-Zeiger, Funktion-zu-Zeiger an und entfernt cv-Qualifizierer
- [ ] Eine Veraltungsmarkierung
- [ ] Eine Zerfallskonstante

**Erklärung:**
`std::decay` wendet Typtransformationen ähnlich denen an, die beim Übergeben von Argumenten per Wert geschehen.

[Referenz](https://en.cppreference.com/w/cpp/types/decay)

#### Q210. Was ist `std::conditional` in C++11?

- [ ] Eine bedingte Anweisung
- [x] Wählt einen Typ oder einen anderen basierend auf einem Kompilierzeit-Boolean
- [ ] Ein bedingter Operator
- [ ] Ein Bedingungsprüfer

**Erklärung:**
`std::conditional` ist eine Metafunktion, die einen von zwei Typen basierend auf einer Kompilierzeit-booleschen Bedingung auswählt.

[Referenz](https://en.cppreference.com/w/cpp/types/conditional)

#### Q211. Wofür wird `std::is_same` verwendet?

- [ ] Um zu prüfen, ob Werte gleich sind
- [x] Um zur Kompilierzeit zu prüfen, ob zwei Typen gleich sind
- [ ] Um Objekte zu vergleichen
- [ ] Um Gleichheit zu prüfen

**Erklärung:**
`std::is_same` ist ein Type Trait, das zur Kompilierzeit prüft, ob zwei Typen identisch sind.

[Referenz](https://en.cppreference.com/w/cpp/types/is_same)

#### Q212. Was ist die Ausgabe dieses Codes?

```cpp
#include <iostream>

int main() {
    int x = 10;
    int* p = &x;
    int** pp = &p;
    std::cout << **pp;
    return 0;
}
```

- [x] 10
- [ ] Adresse von x
- [ ] Adresse von p
- [ ] Kompilierungsfehler

**Erklärung:**
pp ist ein Zeiger auf Zeiger. \*\*pp dereferenziert zweimal, um den Wert von x zu erhalten, der 10 ist.

[Referenz](https://en.cppreference.com/w/cpp/language/pointer)

#### Q213. Wofür wird `std::remove_if` verwendet?

- [ ] Um if-Anweisungen zu entfernen
- [x] Um Elemente aus einem Bereich zu entfernen, die ein Prädikat erfüllen
- [ ] Um Dateien bedingt zu entfernen
- [ ] Um Bedingungen zu entfernen

**Erklärung:**
`std::remove_if` entfernt Elemente aus einem Bereich, die ein gegebenes Prädikat erfüllen, wird mit erase für tatsächliches Löschen verwendet.

[Referenz](https://en.cppreference.com/w/cpp/algorithm/remove)

#### Q214. Wofür wird `std::transform` verwendet?

- [ ] Um Code zu transformieren
- [x] Um eine Funktion auf einen Bereich anzuwenden und Ergebnisse in einem anderen Bereich zu speichern
- [ ] Um Typen zu transformieren
- [ ] Um Transformationen durchzuführen

**Erklärung:**
`std::transform` wendet eine gegebene Funktion auf einen Bereich von Elementen an und speichert das Ergebnis in einem anderen Bereich.

[Referenz](https://en.cppreference.com/w/cpp/algorithm/transform)

#### Q215. Wofür wird `std::accumulate` verwendet?

- [ ] Um Fehler zu akkumulieren
- [x] Um die Summe zu berechnen oder einen Bereich von Elementen zu falten
- [ ] Um Daten zu akkumulieren
- [ ] Um Zahlen zu addieren

**Erklärung:**
`std::accumulate` berechnet die Summe eines Bereichs von Elementen oder wendet eine binäre Operation an, um den Bereich zu falten.

[Referenz](https://en.cppreference.com/w/cpp/algorithm/accumulate)

#### Q216. Was ist die Ausgabe dieses Codes?

```cpp
#include <iostream>

int main() {
    int x = 5;
    int y = 10;
    int z = x > y ? x : y;
    std::cout << z;
    return 0;
}
```

- [ ] 5
- [x] 10
- [ ] 1
- [ ] 0

**Erklärung:**
Der ternäre Operator prüft, ob x > y. Da dies falsch ist, wird z y zugewiesen, was 10 ist.

[Referenz](https://en.cppreference.com/w/cpp/language/operator_other)

#### Q217. Wofür wird `std::copy` verwendet?

- [ ] Um Dateien zu kopieren
- [x] Um Elemente von einem Bereich in einen anderen zu kopieren
- [ ] Um Objekte zu duplizieren
- [ ] Um Speicher zu kopieren

**Erklärung:**
`std::copy` kopiert Elemente von einem Quellbereich in einen Zielbereich.

[Referenz](https://en.cppreference.com/w/cpp/algorithm/copy)

#### Q218. Wofür wird `std::find` verwendet?

- [ ] Um Dateien zu finden
- [x] Um das erste Vorkommen eines Werts in einem Bereich zu finden
- [ ] Um nach Mustern zu suchen
- [ ] Um Objekte zu lokalisieren

**Erklärung:**
`std::find` sucht nach dem ersten Vorkommen eines Werts in einem Bereich und gibt einen Iterator darauf zurück.

[Referenz](https://en.cppreference.com/w/cpp/algorithm/find)

#### Q219. Worauf basiert `std::sort`?

- [ ] Bubble Sort
- [x] Introsort (Hybrid aus Quicksort, Heapsort und Insertion Sort)
- [ ] Nur Merge Sort
- [ ] Selection Sort

**Erklärung:**
`std::sort` verwendet typischerweise Introsort, das Quicksort, Heapsort und Insertion Sort für optimale Leistung kombiniert.

[Referenz](https://en.cppreference.com/w/cpp/algorithm/sort)

#### Q220. Was ist die Ausgabe dieses Codes?

```cpp
#include <iostream>
#include <algorithm>
#include <vector>

int main() {
    std::vector<int> v = {5, 2, 8, 1, 9};
    std::sort(v.begin(), v.end());
    std::cout << v[2];
    return 0;
}
```

- [ ] 8
- [ ] 2
- [x] 5
- [ ] 1

**Erklärung:**
Nach dem Sortieren wird der Vektor zu {1, 2, 5, 8, 9}. v[2] ist das dritte Element, was 5 ist.

[Referenz](https://en.cppreference.com/w/cpp/algorithm/sort)
