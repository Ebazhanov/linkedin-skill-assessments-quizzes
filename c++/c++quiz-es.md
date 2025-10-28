## C++

#### Q1. ¿Cuál es la salida de este código?

```cpp
vector<int> v(22);
bool b = (v[6]);
printf("%d", !b);
```

- [ ] False
- [ ] 0
- [x] 1
- [ ] Este código tiene un error.

#### Q2. ¿Cuál de las siguientes es una razón por la que usar esta línea se considera una mala práctica? (_Alternativa_: ¿Por qué usar esta línea se considera una mala práctica?)

```cpp
using namespace std;
```

- [ ] El código compilado siempre es más grande debido a todos los símbolos importados.
- [x] Si el código usa una función definida en dos bibliotecas diferentes con el mismo prototipo pero posiblemente con diferentes implementaciones, habrá un error de compilación debido a la ambigüedad.
- [ ] Incluye automáticamente todos los archivos header de la biblioteca estándar (cstdint, cstdlib, cstdio, iostream, etc).
- [ ] Hace que el compilador imponga la inclusión exclusiva de archivos header que pertenecen a la biblioteca estándar, generando un error de compilación cuando se incluye un archivo header diferente.

[Reference](https://www.geeksforgeeks.org/using-namespace-std-considered-bad-practice/)

#### Q3. ¿Cuál es el tamaño más pequeño que una variable del tipo child_t puede ocupar en memoria?

```cpp
typedef struct{
    unsigned int  age    : 4;
    unsigned char gender : 1;
    unsigned int  size   : 2;
}child_t;
```

- [ ] 7 bits.
- [ ] 25 bytes.
- [ ] 1 bit.
- [x] 1 byte.

[Reference](https://en.cppreference.com/w/cpp/language/bit_field)

#### Q4. ¿Cuáles son los vectores v1 y v2 después de ejecutar el código?

```cpp
std::vector<int> v1{1,2,3},v2;
v2=v1;
v1.push_back(4);
v2.push_back(5);
```

- [ ] Error
- [ ] v1:{1,2,3,4}; v2:{5};
- [ ] v1:{1,2,3,4,5}; v2:{1,2,3,4,5};
- [x] v1:{1,2,3,4}; v2:{1,2,3,5};

#### Q5. ¿Cuál de las siguientes es una declaración verdadera sobre la diferencia entre pointers e iterators?

- [ ] Mientras que los pointers son variables que contienen direcciones de memoria, los iterators son funciones genéricas usadas para recorrer contenedores. Esta función permite al programador implementar código de lectura y escritura mientras se recorre el contenedor.
- [x] Incrementar un iterator siempre significa acceder al siguiente elemento en el contenedor (si existe), sin importar el contenedor. Incrementar el pointer significa apuntar al siguiente elemento en memoria, no siempre el siguiente elemento.
- [ ] Los pointers son variables que contienen direcciones de memoria mientras que iterator es un entero sin signo que se refiere a desplazamientos en arrays.
- [ ] Todos los iterators están implementados con pointers, por lo que todos los iterators son pointers pero no todos los pointers son iterators.

[Reference](https://stackoverflow.com/a/31128162)

#### Q6. ¿Cuál es el almacenamiento ocupado por u1?

```cpp
union {
    uint16_t a;
    uint32_t b;
    int8_t c;
} u1;
```

- [x] 4 bytes
- [ ] 7 bytes
- [ ] 8 bytes
- [ ] 2 bytes

[Reference](https://en.cppreference.com/w/cpp/language/union)

#### Q7. ¿Cuál de los siguientes operadores puede ser sobrecargado?

- [ ] `?:`
- [x] `new`
- [ ] `::`
- [ ] `.`

[Reference](https://www.tutorialspoint.com/operators-that-cannot-be-overloaded-in-cplusplus)

#### Q8. ¿Cuál de los siguientes muestra el contenido del vector apuntado por v1 y v2 después de ejecutar este código?

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

v1 y v2 apuntan al mismo vector.

#### Q9. ¿Cuál de las siguientes no es una diferencia entre una class y una struct?

- [ ] Debido a que las structs son parte del lenguaje de programación C, existe cierta complejidad entre las structs de C y C++. Este no es el caso con las classes.
- [ ] Las classes pueden tener funciones miembro; las structs son privadas.
- [ ] El especificador de acceso por defecto para miembros de una struct es public, mientras que, para miembros de una class, es private.
- [x] Los parámetros de tipo template pueden ser declarados con classes, pero no con la palabra clave struct.

Los templates se pueden usar tanto con classes como con structs  
[Reference](https://docs.microsoft.com/en-us/cpp/cpp/struct-cpp?view=msvc-170)  
[Reference](https://www.fluentcpp.com/2017/06/13/the-real-difference-between-struct-class/)

#### Q10. Suponga que necesita mantener una estructura de datos con permisos para acceder a algún recurso basado en los días de la semana, pero no puede usar una variable bool para cada día. Necesita usar un bit por día de la semana. ¿Cuál de las siguientes es una implementación correcta de una estructura con bit fields para esta aplicación?

- [x] A

```cpp
typedef struct {
    int sunday:1;
    int monday:1;
    // more days
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
    // more days
    bit friday:1;
    bit saturday:1;
} weekdays;

```

- [ ] D

```cpp
typedef struct {
    bit sunday;
    bit monday;
    // more days
    bit friday;
    bit saturday;
} weekdays;
```

[Reference](https://en.cppreference.com/w/cpp/language/bit_field) _NOTA_: La sintaxis correcta es que cada variable tiene un tamaño de 1 bit. `bit` no es un tipo en C++.

#### Q11. ¿Qué es un lvalue?

- [ ] Es una expresión constante, es decir, una expresión compuesta de constantes y operaciones.
- [ ] Es una expresión que representa un objeto con una dirección.
- [ ] Es una expresión adecuada para el operando del lado izquierdo en una operación binaria.
- [x] Es un valor de ubicación, es decir, una dirección de memoria adecuada para asignar a un pointer o reference.

#### Q12. ¿Qué hace el especificador de tipo auto en esta línea de código (desde C++11)?

```cpp
auto x = 4000.22;
```

- [x] Especifica que el tipo de x será deducido del inicializador - en este caso, double.
- [ ] Especifica que el tipo de x es automático, lo que significa que puede asignársele diferentes tipos de datos a lo largo del programa.
- [ ] Especifica que x es una variable con duración de almacenamiento automático.
- [ ] Especifica que se asignará más memoria para x en caso de que necesite más espacio, evitando la pérdida de datos debido al desbordamiento.

#### Q13. Una class template es un \_?

- [x] class escrita con el paradigma de programación genérica, especificando comportamiento en términos de parámetros de tipo en lugar de tipos específicos.
- [ ] superclass en blanco destinada para herencia y polimorfismo.
- [ ] class que solo consiste en una variable miembro, sin constructor, destructor o funciones miembro.
- [ ] código fuente esqueleto para una class donde el programador tiene que completar partes específicas para definir los tipos de datos y algoritmos utilizados.

[Reference](https://www.mygreatlearning.com/blog/templates-in-cpp/)

#### Q14. ¿Cuál es el operador ternario equivalente a este fragmento de código?

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

[Reference](https://www.w3schools.com/cpp/cpp_conditions_shorthand.asp)

#### Q15. ¿Cuál es la salida del código dado a continuación?

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

#### Q16. ¿Cuál es el significado de las dos partes especificadas entre paréntesis en un range-based for loop, separadas por dos puntos?

- [x] La primera es una declaración de variable que contendrá un elemento en una secuencia. La segunda es la secuencia a recorrer.
- [ ] La primera es un iterator, y la segunda es el valor de incremento a agregar al iterator.
- [ ] La primera es la variable de iteración. La segunda es un `std::pair` que especifica el rango (inicio y fin) en el que la variable iterará.
- [ ] La primera es un objeto contenedor. La segunda es un `std::pair` que especifica el rango (inicio y fin) en el que los elementos serán accedidos dentro del loop.

#### Q17. ¿Cuál es la salida del código dado a continuación?

```cpp
int8_t a=200;
uint8_t b=100;
if(a>b)
    std::cout<<"greater";
else
    std::cout<<"less";
```

- [ ] No hay salida porque hay una excepción al comparar un int8_t con un uint8_t.
- [ ] greater
- [x] less
- [ ] No hay salida porque hay un error del compilador.

Nota: una variante de la pregunta a continuación.

#### Q18. ¿Cuál es la salida de este bloque de código?

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

Nota: La conversión implícita de 'int' a 'int8_t' (aka 'signed char') cambia el valor de 200 a -56

#### Q19. ¿Cuál es la salida después de ejecutar este fragmento de código?

```cpp
int x=5, y=2;
if(x & y) {
    /*_part A_*/
}
else {
    /*_part B_*/
}
```

- [ ] La parte A se ejecuta porque x==5 (verdadero) y y==2 (verdadero), por lo tanto la operación AND evalúa como verdadero.
- [x] La parte B se ejecuta porque (x & y) resulta en 0, o falso.
- [ ] La parte A se ejecuta porque (x & y) resulta en un valor distinto de cero, o verdadero.
- [ ] La parte B se ejecuta porque la declaración (x & y) es inválida, por lo tanto falsa.

[Reference](https://stackoverflow.com/questions/63867765/dont-understand-why-if-5-2-is-false)

#### Q20. ¿Cuál es una definición válida para la función `get_length`, que devuelve la longitud de una cadena terminada en null?

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

#### Q21. ¿Cuál clase STL es la mejor opción para implementar una colección de datos que siempre esté ordenada de manera que la operación pop siempre obtenga el mayor de los elementos? Suponga que solo está interesado en las operaciones push y pop.

- [ ] `std::list`
- [ ] `std::vector`
- [x] `std::priority_queue`
- [ ] `std::map`

#### Q22. ¿Cuál es el significado de las tres secciones especificadas entre paréntesis en un for loop separadas por punto y coma?

- [ ] La primera es el nombre de la variable de iteración, la segunda es el número de veces a iterar, y la tercera es el incremento o decremento deseado (especificado con un entero con signo).
- [x] La primera es el bloque de inicialización, la segunda es la condición para iterar, y la tercera es el bloque de incremento.
- [ ] La primera es la variable de iteración, la segunda es el contenedor en el que debe operar, y la tercera es una condición de salida para abortar en cualquier momento.
- [ ] La primera es el nombre de la variable de iteración, la segunda es el valor inicial para la variable de iteración, y la tercera es el valor de parada (el último valor más uno).

#### Q23. ¿Qué imprime este código?

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

[Reference](https://www.geeksforgeeks.org/pre-increment-and-post-increment-in-c/)

#### Q24. ¿Qué es verdadero sobre la variable llamada `ptr`?

```cpp
void *ptr;
```

- [ ] Es un pointer inicializado en NULL.
- [ ] Es un pointer a una función void.
- [ ] Esa declaración causa un error del compilador, ya que los pointers deben especificar un tipo.
- [x] Es un pointer a un valor sin tipo específico, por lo que puede ser convertido para apuntar a cualquier tipo.

[Reference](https://en.cppreference.com/w/cpp/language/pointer)

#### Q25. ¿Cuál es la salida del código dado a continuación?

```cpp
int c=3; char d='A';
std::printf("c is %d and d is %c",c,d);
```

- [ ] c is d and d is c
- [ ] c is A and d is 3
- [x] c is 3 and d is A
- [ ] c is c and d is d

#### Q26. ¿Cuál es la salida de este código?

```cpp
printf("1/2 = %f",(float)(1/2));
```

- [ ] 1/2 = 0.499999
- [ ] 1/2 = 0
- [x] 1/2 = 0.000000
- [ ] 1/2 = 0.5

#### Q27. ¿Cuál es la diferencia entre un miembro de clase public y private?

- [ ] Los miembros public son lo mismo que las variables globales, por lo que cada parte del código tiene acceso a ellos. Los miembros private son lo mismo que las variables automáticas, por lo que solo su clase tiene acceso a ellos.
- [ ] Los miembros public se hacen accesibles a cualquier aplicación en ejecución. Los miembros private se hacen accesibles solo a la aplicación donde se instancia el objeto.
- [ ] Los miembros public se compilarán como variables compartidas en un entorno multihilo. Los miembros private se compilarán como variables Thread-local.
- [x] Los miembros public pueden ser accedidos por cualquier función. Los miembros private pueden ser accedidos solo por las funciones miembro de la misma clase y los friends de la clase.

[Reference](https://www.geeksforgeeks.org/difference-between-public-and-private-in-c-with-example/)

#### Q28. ¿Cuál es el valor de `x` después de ejecutar este código?

```cpp
int x=10, a=-3;
x+=a;
```

- [ ] 3
- [x] 7
- [ ] -3
- [ ] 13

#### Q29. ¿Qué afirmación es verdadera?

- [ ] Solo las classes pueden tener variables y métodos miembro.
- [x] C++ soporta herencia múltiple.
- [ ] C++ soporta solo herencia simple.
- [ ] Solo las structs pueden heredar.

#### Q30. Considere un pointer to void, llamado `ptr`, que ha sido configurado para apuntar a una variable de punto flotante `g`. ¿Cuál opción es una forma válida de desreferenciar `ptr` para asignar su valor apuntado a una variable float `f` más adelante en el programa?

```cpp
float g;
void *ptr=&g;
```

- [ ] `float f=*(float)ptr;`
- [ ] `float f=(float *)ptr;`
- [ ] `float f=(float)*ptr;`
- [x] `float f=*(float *)ptr;`

#### Q31. ¿Qué es el operador `.*` y qué hace?

- [ ] Es lo mismo que el operador de acceso a miembro de clase, u operador flecha `(->)`, que te permite acceder a un miembro de un objeto a través de un pointer al objeto.
- [x] Es el operador pointer to member, y te permite acceder a un miembro de un objeto a través de un pointer a ese miembro de clase específico.
- [ ] Es el acceso a miembro con dirección del operador, que devuelve la dirección de un miembro de clase o struct.
- [ ] Es una combinación del operador de acceso a miembro `(.)` y el operador de desreferencia `(*)`, por lo que te permite acceder al objeto al que apunta un pointer a miembro.

[Reference](https://en.cppreference.com/w/cpp/language/operator_member_access)

#### Q32. Para estas declaraciones, ¿cuál opción muestra cuatro formas equivalentes de asignar el carácter "y" en la cadena a una variable char c?

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

#### Q33. ¿Cuál opción es la declaración correcta para la clase llamada Dog, derivada de la clase Animal?

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

#### Q34. ¿Cuál es la salida de este código dado a continuación?

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

Técnicamente, si un `char` es `signed` o `unsigned` está definido por la implementación;
en el último caso, la segunda respuesta sería correcta.
[Reference](https://en.cppreference.com/w/cpp/language/types)

#### Q35. ¿Cómo puede el código de C++ llamar a una función de C?

- [ ] simplemente llamando al código C
- [ ] No hay forma de que C++ llame a una función C
- [x] usando extern "C"
- [ ] importando el código fuente C

#### Q36. ¿Cuál opción _no_ es una definición de tipo válida de una estructura que contiene coordenadas x e y como enteros, y que puede usarse exactamente como se muestra para la variable llamada `center`?

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

#### Q37. ¿Cuál opción _no_ produce la misma salida que este fragmento de código? Asuma que la variable `i` no será usada en ningún otro lugar del código.

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

#### Q38. ¿Qué hace esta parte de un archivo main.cpp?

```cpp
#include "library.h"
```

- [ ] Hace que la toolchain compile todo el contenido de library.h para que su código ejecutable esté disponible cuando sea necesario por la aplicación final.
- [ ] Selecciona de library.h las declaraciones y definiciones de todos los datos y funciones usados en el resto del archivo fuente main.cpp, finalmente reemplazando la directiva `#include` con esas declaraciones y definiciones.
- [ ] Informa al linker que algunas funciones o datos usados en el archivo fuente main.cpp están contenidos en library.h, para que puedan ser llamados en tiempo de ejecución. Esto también se conoce como enlace dinámico.
- [x] Causa el reemplazo de la directiva `#include` por todo el contenido del archivo fuente library.h. Esto es similar a la operación Copiar-Pegar de library.h en main.cpp.

#### Q39. Considere esta declaración de función de `is_even`, que toma un entero y devuelve true si el argumento es un número par y false en caso contrario. ¿Cuáles declaraciones son correctas para versiones sobrecargadas de esa función para soportar números de punto flotante y representaciones de cadena de números?

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

#### Q40. ¿Cuál opción es un include guard para el archivo header `my_library.h`?

- [ ] A

```cpp
#ifdef MY_LIBRARY_H
#define MY_LIBRARY_H

// my_library.h content

#endif /* MY_LIBRARY_H */
```

- [x] B

```cpp
#ifndef MY_LIBRARY_H
#define MY_LIBRARY_H

// my_library.h content

#endif /* MY_LIBRARY_H */
```

- [ ] C

```cpp
#ifdef MY_LIBRARY_H
#undef MY_LIBRARY_H

// my_library.h content

#endif /* MY_LIBRARY_H */
```

- [ ] D

```cpp
#define MY_LIBRARY_H
#include MY_LIBRARY_H

// my_library.h content

#undef MY_LIBRARY_H
```

#### Q41. ¿Qué está mal con esta definición cuando se usa un compilador pre-C++11?

```cpp
std::vector<std::vector<int>> thematrix;
```

- [ ] No hay nada mal con ella.
- [ ] Un `std::vector` no puede contener más contenedores `std::vector` como sus elementos.
- [ ] La sintaxis correcta debería ser: `std::vector[std::vector[int]] thematrix;`
- [x] `>>` se interpreta como el operador shift-right, y por lo tanto resulta en un error de compilación.

#### Q42. ¿A qué es equivalente la declaración de abajo?

#### Q42.b. ¿A qué es equivalente la declaración?

```cpp
sprite->x
```

- [ ] `sprite.x`
- [ ] `sprite.*x`
- [x] `(*sprite).x`
- [ ] `*sprite.x`

#### Q43. Considere una clase llamada `complexNumber`. ¿Qué código resultará en un objeto equivalente?

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

#### Q44. ¿Cuál es el resultado de ejecutar este fragmento de código?

```cpp
bool x=true, y=false;

if (~x || y) {
    /*part A*/
} else {
    /*part B*/
}
```

- [ ] La parte A se ejecuta porque la expresión `(~x || y)` siempre resulta en true si `y==false`.
- [ ] La parte B se ejecuta porque la declaración `(~x || y)` es inválida, por lo tanto false.
- [x] La parte A se ejecuta porque `~x` no es cero, lo que significa true.
- [ ] La parte B se ejecuta porque `~x` es false y `y` es false, por lo tanto la operación `OR` evalúa como false.

#### Q45. ¿Cuál sería la salida de este código?

```cpp
int32_t nums[3]={2,4,3};
std::cout << ( nums[0] << nums[1] << nums[2] );
```

- [ ] La salida son las direcciones de `nums[0]`, `nums[1]` y `nums[2]`, en ese orden, sin espacios.
- [x] 256
- [ ] `0`
- [ ] `243`

#### Q46. ¿Cuál es la salida de este código?

```cpp
float values[5]={0.54f, 2.71828f, 3.14159f, 5.499999f, 10.0f};
for(auto f:values)
    printf("%i ",(int)(f+0.5f));
```

- [ ] `0.54 2.71828 3.14159 5.499999 10.0`
- [ ] `1 3 4 6 11`
- [ ] `0 2 3 5 10`
- [x] `1 3 3 5 10`

#### Q47. ¿Cuál de las siguientes clases STL es la mejor opción para implementar una agenda telefónica? Suponga que cada entrada contiene un nombre y un número de teléfono, sin duplicados, y desea tener una búsqueda por nombre.

- [ ] `std::priority_queue`
- [ ] `std::list`
- [ ] `std::vector`
- [x] `std::map`

[Reference](https://en.cppreference.com/w/cpp/container/map)

#### Q48. ¿Qué hace este programa?

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

- [ ] Renombra text1.txt a text2.txt.
- [ ] Crea un directorio llamado text2.txt y mueve text1.txt allí.
- [x] Copia el contenido de text1.txt en text2.txt - es decir, hace una copia de text1.txt, llamada text2.txt.
- [ ] Agrega el contenido de text1.txt en text2.txt - es decir, reemplaza el contenido de text2.txt por la concatenación de text2.txt y text1.txt.

[Reference](https://en.cppreference.com/w/cpp/header/fstream)

#### Q49. ¿Cuál de las siguientes _no_ es una consecuencia de declarar la variable miembro `count` de my_class como static? / Alt.: ¿Qué afirmación es verdadera al declarar la variable miembro `count` como static?

```cpp
class my_class {
    public: static int count;
}
```

- [x] La variable no puede ser modificada por ninguna parte del código en la misma aplicación o thread. Sin embargo, otros threads pueden modificarla.
- [ ] La variable existe incluso cuando no se han definido objetos de la clase, por lo que puede modificarse en cualquier punto del código fuente.
- [ ] La variable se asigna solo una vez, independientemente de cuántos objetos se instancien porque está vinculada a la clase misma, no a sus instancias.
- [ ] Todos los objetos que intentan acceder a su variable miembro count realmente se refieren a la única variable static count vinculada a la clase.

[Reference](https://en.cppreference.com/w/cpp/language/static)

#### Q50. ¿Cuál es el tipo asumido de una constante representada en el código fuente como `0.44`?

- [x] double
- [ ] long float
- [ ] long double
- [ ] float

#### Q51. ¿Cuál es una forma apropiada de eliminar `my_object` como se muestra a continuación?

```cpp
my_class *my_object = new my_class();
```

- [x] `delete(my_object);`
- [ ] `free(my_object);`
- [ ] El garbage collector destruirá el objeto eventualmente.
- [ ] Salir del scope destruirá el objeto.

#### Q52. ¿Cuál es la forma correcta de llamar a la función miembro `count` para el pointer de objeto llamado `grades`?

```cpp
class my_array{
    public:
        int count();
};  // ... more members above

int main(){
    my_array *grades = new my_array();
};  // ... more code above
```

- [ ] `grades.count();`
- [ ] `my_array->count();`
- [x] `grades->count();`
- [ ] `my_array.count();`

[Reference](https://en.cppreference.com/w/c/language/operator_member_access)

#### Q53. ¿Cuál sería la salida de este código?

```cpp
int i0=4, i1=6, i2=8;
int& nums[3]={i2,i0,i1};
std::cout<<nums[0]<<nums[1]<<nums[2];
```

- [x] No hay salida. El código causa un error del compilador porque `nums` es un array de references, lo cual es ilegal.
- [ ] 846
- [ ] La salida son las direcciones de `i2`, `i0` e `i1`, en ese orden, sin espacios.
- [ ] 468

[Reference](https://en.cppreference.com/w/cpp/language/array)

#### Q54. ¿Este código causa un error del compilador? Si es así, ¿por qué?, y si no, ¿qué es `child_t`?

```cpp
typedef struct{
    unsigned int  age    : 4;
    unsigned char gender : 1;
    char                 : 0;
    unsigned int  size   : 2;
}child_t;
```

- [ ] Sí, causa un error del compilador porque el carácter de dos puntos no está permitido en definiciones de struct.
- [x] No, y `child_t` es un tipo definido como una estructura con bit fields. Tiene 4 bits para age y 1 bit para gender en el primer byte, y 2 bits para size en el segundo byte.
- [ ] Sí, causa un error del compilador porque hay un campo sin nombre.
- [ ] Sí, causa un error del compilador porque un campo está definido con un tamaño de 0.

[Reference](https://en.cppreference.com/w/cpp/language/bit_field)

#### Q55. ¿A qué es equivalente esta expresión?

```cpp
A->B
```

- [ ] `*(A.B)`
- [ ] `B=A`
- [x] `(*A).B`
- [ ] `&A.B`

Nota: una variante más simple de la pregunta a continuación.

#### Q56. ¿A qué es equivalente esta expresión?

```cpp
A->B->C->D
```

- [ ] `A.B.C.D`
- [ ] `*A.*B.*C.*D`
- [ ] `&A.&B.&C.&D`
- [x] `*(*((*A).B).C).D`

**Nota:** una variante más compleja de la pregunta anterior.

#### Q57. ¿Qué hace esta función?

```cpp
auto buff = new char[50];
std::memset(buff,20,50);
```

- [ ] Declara un buffer de memoria llamado buff que comienza en la dirección 20 y termina en la dirección 70.
- [ ] Establece todos los bits en el array llamado buffer desde su elemento en el índice 20 hasta su elemento en el índice 50.
- [x] Escribe el valor 20 en cada dirección de memoria desde buff hasta buff+49.
- [ ] Declara un buffer de memoria llamado buff que comienza en la dirección 20 y termina en la dirección 50.

[Reference](https://en.cppreference.com/w/cpp/string/byte/memset)

#### Q58. Considere una clase llamada `CustomData`. ¿Cuál opción es una sintaxis de declaración correcta para sobrecargar el operador postfix `++` como miembro de clase?

- [ ] `CustomData& operator++();`
- [ ] `void operator++(CustomData);`
- [ ] `CustomData operator++(CustomData);`
- [x] `CustomData operator++(int);`

[Reference](https://en.cppreference.com/w/cpp/language/operators)

#### Q59. Desea ordenar my_array, declarado a continuación. ¿Cuál opción es la llamada correcta a std::sort, usando una expresión lambda como función de comparación?

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

[Reference](https://docs.microsoft.com/en-us/cpp/cpp/lambda-expressions-in-cpp?view=msvc-160)

#### Q60. ¿Cuál opción es la implementación más razonable de la función std::mutex::lock() usando std::mutex::try_lock()?

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

Nota: variante de la pregunta a continuación.

#### Q61. ¿Cuál es la diferencia principal entre estas dos funciones?

```cpp
std::mutex::lock()
std::mutex::try_lock()
```

- [ ] `lock()` tiene mayor privilegio sobre `try_lock()`. Esto significa que tienes una mejor oportunidad de adquirir un mutex con `lock()`.
- [x] Ambos intentan adquirir un lock, pero `lock()` bloquea si el mutex no está disponible, mientras que `try_lock()` devuelve si el mutex está disponible o no.
- [ ] `lock()` impone la preempción, mientras que `try_lock()` sugiere la preempción.
- [ ] Si el mutex no está disponible, `try_lock()` devuelve con un código correspondiente, mientras que `lock()` arrebata el mutex del thread que actualmente lo tiene.

Nota: variante de la pregunta anterior.

[Reference](https://en.cppreference.com/w/cpp/thread/mutex/try_lock)

#### Q62. ¿Cuál es el propósito de un destructor?

- [x] Permite al programador escribir el código necesario para liberar los recursos adquiridos por el objeto antes de eliminar el objeto mismo.
- [ ] Elimina un objeto. Un ejemplo de un destructor es la función `delete()`.
- [ ] Termina un programa. Esto puede lograrse como una llamada de función regular o como una excepción.
- [ ] No hay destructores en C++.

#### Q63. ¿Cuál es un beneficio de declarar el parámetro como una referencia `const` en lugar de declararlo como un objeto regular?

```cpp
int calculateMedian(const my_array& a)
```

- [ ] En realidad, los objetos no pueden pasarse como variables regulares, porque requieren una llamada al constructor. Por lo tanto, una referencia `const` es la única forma de pasar instancias de clases a las funciones.
- [ ] No hay beneficios porque una referencia y un objeto se tratan de la misma manera.
- [x] El calificador `const` prohíbe que el código modifique el argumento, por lo que el programador puede estar seguro de que el objeto fuente permanecerá sin cambios. / Alt.: El argumento se pasa como referencia, por lo que si el objeto my_array pasado es grande, el programa requerirá menos tiempo y memoria.
- [ ] El argumento se pasa como referencia, por lo que la función recibe una copia que puede modificarse sin afectar la variable original.

[Reference](https://stackoverflow.com/a/2627179/10773894)

#### Q64. ¿Qué es un include guard?

- [ ] una directiva del preprocesador que previene comportamientos inconsistentes en líneas que contienen las directivas #ifdef, #ifndef, o #elif
- [ ] una opción del compilador que previene que el código del usuario incluya bibliotecas adicionales
- [x] una declaración del preprocesador que previene que un archivo fuente sea incluido más de una vez en un proyecto
- [ ] una biblioteca que agrega características de seguridad como mutexes, watchdog timers, y assertions al proyecto

#### Q65. ¿Cuál sería la declaración correcta de un constructor por defecto para una clase llamada Sprite?

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

#### Q66. ¿Cuál es el propósito de esta línea en un archivo header?

```cpp
#pragma once
```

- [ ] restringir el uso de su contenido a solo un archivo fuente
- [ ] decirle al compilador que solo una variable puede ser instanciada de las clases o tipos contenidos en este archivo header
- [ ] ayudar al compilador a terminar más rápido asegurando que solo se necesita una pasada del compilador para el código incluido en este archivo header
- [x] hacer que el compilador analice ese archivo header solo una vez, incluso si se incluye múltiples veces en el fuente

[reference here](https://en.cppreference.com/w/cpp/preprocessor/impl)

#### Q67. ¿Qué es una variable de tipo double?

- [ ] una 2-tupla
- [ ] un número entero
- [x] un número de punto flotante
- [ ] una cadena con más de 255 caracteres

[Reference](https://www.educba.com/c-plus-plus-double/)

#### Q68. Aparte de desplazar bits a la izquierda, ¿para qué se usa el operador <<?

- [ ] desplazar caracteres a la izquierda en una cadena.
- [x] insertar caracteres en un stream de salida como std::cout.
- [ ] comparar números de punto flotante como menor que.
- [ ] asignar una variable a una referencia.

#### Q69. ¿Cuál opción es una razón para especificar el tipo de un pointer en lugar de usar `void *`, que funciona como un pointer a cualquier tipo?

- [ ] El compilador necesita el tipo de datos para asegurarse de que el pointer no se usará en tipos ilegales no apuntables como funciones, etiquetas, pointers y referencias.
- [ ] `void *` no funciona para cualquier tipo. El lenguaje no permite asignar nada más que `void` a un pointer a `void *`.
- [x] El compilador necesita el tipo de datos para saber cuánta memoria asignar para el pointer porque diferentes tipos de datos requieren diferentes longitudes de pointer.
- [ ] Sí, causa un error del compilador porque un campo está definido con un tamaño de 0.

[Reference](https://stackoverflow.com/questions/9802585/why-is-the-data-type-needed-in-pointer-declarations)

#### Q70. ¿Qué está mal con este fragmento de código?

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

- [ ] La función main debe tener un tipo de retorno void.
- [ ] `std::cin` y `std::cout` son inválidos. Los nombres correctos para los streams de entrada y salida de caracteres son `cin` y `cout`.
- [ ] Se supone que debe usarse la dirección de `str`. Es decir, `&str` en lugar de `str`.
- [x] El flujo del operador de entrada está invertido. Debe comenzar desde `std::cin` y luego fluir (>>) hacia `str`.

#### Q71. Cuando se coloca en un contexto de ejecución válido, ¿qué declaración asignará dinámicamente memoria del heap para un entero de valor 11?

- [ ] `int anInt = new int(11);`
- [ ] `int* anInt = new int[11];`
- [ ] `int anInt = new int[11];`
- [x] `int* anInt = new int(11);`

#### Q72. ¿Qué opción describe mejor el tipo `long`?

- [x] un número entero de al menos 32 bits
- [ ] una cadena con más de 255 caracteres
- [ ] un pointer
- [ ] un número de punto flotante de 64 bits

#### Q73. ¿Cuál de los siguientes tipos tiene la funcionalidad más cercana a una class?

- [x] `struct`
- [ ] `union`
- [ ] `enum`
- [ ] `namespace`

[Reference](https://en.cppreference.com/w/c/language/struct)

#### Q74. Dados estos registros en un map, ¿cómo actualizará el valor para la clave "Sinead" a 22?

![image](images/Q79.png?raw=png)

- [x] `marks["Sinead"] = 22`
- [ ] `marks["Sinead"].22`
- [ ] `marks["Sinead"] -> 22`
- [ ] `marks["Sinead"].value = 22`

#### Q75. ¿Por qué std::sort puede recibir un objeto de función como uno de sus parámetros?

- [x] `La función std::sort es un template. El programador es libre de ingresar el algoritmo de ordenamiento en un objeto de función como argumento.`
- [ ] `En realidad, std::sort toma solo un argumento, que es el contenedor a ordenar.`
- [ ] `std::sort opera en un contenedor template. El compilador no sabe cómo comparar relacionalmente los valores que contiene, por lo que se debe proporcionar una función para hacer la comparación.`
- [ ] `std::sort usará la función del parámetro como manejador de errores. La función será llamada si ocurre un error.`

#### Q76. ¿Qué sucederá cuando ejecutes este fragmento de código?

```
#include <iostream>

int main() {
float a = 5.51;
int b = static_cast<int>(a);
std::cout << b;
}
```

- [ ] `Se imprimirá 6 en la salida estándar, sin generar advertencias de compilación.`
- [x] `Se imprimirá 5 en la salida estándar, sin generar advertencias de compilación.`
- [ ] `Se imprimirá 6 en la salida estándar, con advertencias de compilación generadas.`
- [ ] `Se imprimirá 5 en la salida estándar, con advertencias de compilación generadas.`

#### Q77. ¿Qué especificador de acceso no permite que los miembros de la clase sean accedidos desde fuera de la clase, pero permite que sean accedidos por clases derivadas?

- [ ] guarded
- [x] protected
- [ ] public
- [ ] private

#### Q78. La generación ejecutable por defecto en UNIX para un programa C++ es \_

- [ ] a.exe
- [ ] a
- [x] a.out
- [ ] out.a

#### Q79. ¿Cuál será la salida del siguiente programa?

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

#### Q80. ¿Qué significa "c" en cout y cin?

- [ ] compiler
- [ ] console
- [x] character
- [ ] standard namespace

#### Q81. ¿Cuál es el uso de tellp()?

- [ ] Posición actual del Input Pointer
- [x] Posición actual del Output Pointer
- [ ] Última posición del Input Pointer
- [ ] Última posición del Output Pointer

#### Q82. ¿Qué es una función callback?

- [ ] Pointer para un pointer
- [x] Pointer para una función
- [ ] función para un pointer
- [ ] función para una clase

#### Q83. ¿Cuál es la sintaxis correcta para imprimir "Hello World" en C++?

- [x] `cout << "Hello World";`
- [ ] `System.out.println("Hello World");`
- [ ] `print("Hello World");`
- [ ] Console.WriteLine("Hello World");```

#### Q84. ¿Cuántas categorías de iterators hay en C++?

- [ ] 4
- [ ] 3
- [ ] 7
- [x] 5

#### Q85. ¿Cuál es el significado de base class en C++?

- [ ] Hereda de otra clase
- [ ] Tiene una variable pointer
- [ ] Es la primera clase declarada
- [x] Otra clase heredó de esta clase

#### Q86. El tamaño de objetos C++ se expresa en términos de múltiplos del tamaño de un ** y el tamaño de un char es **.

- [ ] char, 4
- [ ] float, 8
- [ ] int, 1
- [x] char, 1

#### Q87. Los aspectos dependientes de la implementación sobre una implementación se pueden encontrar en

- [ ] `<numeric>`
- [ ] `<limit>`
- [x] `<limits>`
- [ ] `<implementation>`

#### Q88. ¿Qué es un constructor por defecto?

- [x] un constructor que puede usarse sin argumentos
- [ ] un constructor que no tiene valor de retorno
- [ ] un constructor que es usado por múltiples clases
- [ ] un constructor que inicializa todos los miembros de una clase

#### Q89. Al proteger un archivo header, ¿por qué usarías '#pragma once' en lugar de 'include' guard?

- [ ] No hay razón para elegir porque sirven propósitos diferentes
- [x] Un include guard usa un macro para lograr una sola inclusión, pero el compilador no puede prevenir que el programador defina ese macro en otro lugar, lo que resultaría en ninguna inclusión
- [ ] '#pragma once' garantiza que el código del header nunca cambiará porque es impuesto por el compilador
- [ ] Los include guards se refieren al archivo header en el sistema de archivos, no al código, por lo que no son útiles si el archivo header existe más de una vez en un proyecto. Esto no es un problema con '#pragma once'

#### Q90. ¿Cuál de las siguientes afirmaciones es válida?

- [ ] Podemos crear un nuevo operador de C++.
- [ ] Podemos cambiar la precedencia del operador de C++.
- [x] No podemos cambiar los templates del operador.
- [ ] Podemos cambiar la asociatividad de los operadores de C++.

#### Q91. ¿Cuál de los siguientes es/son agregados automáticamente a cada clase, si no escribimos los nuestros?

- [ ] Copy Constructor
- [ ] Assignment Operator
- [ ] Un constructor sin ningún parámetro
- [x] Todos los anteriores

#### Q92. ¿Por cuál operador puede ser reemplazada la declaración if-else?

- [ ] estructura certain
- [ ] estructura choosing
- [x] estructura selective
- [ ] Ninguna de las anteriores

#### Q93. ¿Cuál opción sería una solución recursiva al problema del factorial n!?

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

#### Q94. Un destructor de clase puede ser llamado cuando ocurren varias situaciones. ¿Cuál opción no es una de esas situaciones?

- [ ] El programa se termina. Esto llama al destructor de objetos de duración estática.
- [ ] Se llama a la función delete() para un pointer de objeto asignado con el operador new.
- [x] El garbage collector detecta que un objeto ya no va a ser usado.
- [ ] Un objeto de duración de almacenamiento automático sale del scope.

#### Q95. Estás diseñando un sistema de pagos de divisas en C++. Necesitas modelar una transacción de una moneda que tiene un entero como su cantidad y un float como su precio. Luego quieres declarar un objeto real de este tipo. ¿Cómo lo lograrás?

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

#### Q96. ¿Qué sucederá si intentas llamar esta función con checkConcatThreshold("a");?

```cpp
int checkConcatThreshold(string a, string b) {
    return (a + b).length () > 120;
}
```

- [ ] Ocurrirá una advertencia de compilación y el segundo argumento recibirá un valor por defecto de b.
- [ ] Ocurrirá una advertencia de compilación y el segundo argumento recibirá un valor por defecto de la cadena vacía.
- [x] Ocurrirá un error de compilación.
- [ ] No ocurrirán errores de compilación ni advertencias de compilación.

#### Q97. Necesitas definir una función lambda de C++. Quieres que la función tenga acceso solo a las variables que son locales a ella. La función debe recibir un solo parámetro, un nombre, y construir un saludo simple. ¿Cómo lo lograrás?

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

[Reference](https://docs.microsoft.com/en-us/cpp/cpp/lambda-expressions-in-cpp?view=msvc-160)

#### Q98. ¿Cuál es el valor de X después de ejecutar este código?

```cpp
int x=10, a=-3;
X+=a;
```

- [ ] -3
- [x] 7
- [ ] 13
- [ ] 3

**Explicación:** `+=` significa aumentar el valor. Así que `x += a` es equivalente a `x = x + a`

#### Q99. Una vez que termines de escribir en un archivo, ¿qué método llamarás en el `ofstream` para notificar al sistema operativo?

- [ ] printout()
- [x] close()
- [ ] destroy()
- [ ] flush()

#### Q100. ¿Cuál opción no es una palabra clave de C++?

- [ ] static_assert
- [ ] reinterpret_cast
- [x] comPl
- [ ] alignas

#### Q101. La función size_in_bits parece tomar cualquier tipo de parámetro. Esto se puede hacer sobrecargando la función, o dejando que el compilador se encargue escribiendo un template. ¿Cuál opción es una implementación de ese template?

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

#### Q102. Para usar el teclado como entrada se incluye la biblioteca iostream. Para leer entrada desde archivos como entrada, ¿qué biblioteca se necesita?

- [x] fstream
- [ ] cstdlib
- [ ] filestream
- [ ] iostream

#### Q103. ¿Qué imprimirá este programa orientado a objetos?

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

#### Q104. El programa siguiente maneja un contenedor stack. ¿Cuál es la salida de ejecutar el programa?

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

#Explicación detallada:

Aquí se supone que implementamos una estructura de datos stack que sigue el principio **FILO** (First IN Last Out),
_stack.push()_ -> inserta un elemento en el array desde el final.
_stack.pop()_ -> elimina un elemento del final del array.
_stack.top()_ -> simplemente nos da el elemento superior del array.
Siguiendo las secuencias de push y pop: **[1,2,3]** luego se usa la función pop,
El array recién formado es: **[1,2,4]** luego se usa top para recuperar el elemento superior '4', luego se usa nuevamente la función pop que elimina 4.
por lo tanto, el array resultante es: 1,2.
Luego imprime el elemento superior (es decir: 2).

#### Q105. ¿Cuál opción es una forma válida de sobrecargar el operador condicional ternario?

- [ ] `void& operator ?:(const bool cond, const void& iftrue, const void& iffalse);`
- [x] `El operador ternario no es sobrecargable.`
- [ ] `void& operator conditional(const bool cond, const void& iftrue, const void& iffalse);`
- [ ] `void* operator ?:(const bool cond, const void* iftrue, const void* iffalse);`

[Reference](https://en.cppreference.com/w/cpp/language/operators)

#### Q106. ¿Qué jerarquía de clases representa un ejemplo de herencia multinivel?

- [ ] En el mismo programa, en diferentes puntos, una clase dada deriva individualmente de más de una clase diferente.
- [ ] Una primera clase deriva directamente, al mismo tiempo, de una segunda y tercera clase.
- [x] En el mismo programa, en diferentes puntos, una clase dada deriva individualmente de más de dos clases diferentes.
- [ ] Una primera clase deriva de una segunda clase, y esa segunda clase ya deriva de una tercera clase

#### Q107. ¿Cuál de las siguientes es la sintaxis correcta para imprimir el mensaje en el lenguaje C++?

- [ ] Out <<"Hello world!
- [ ] Cout << Hello world! ;
- [x] cout <<"Hello world!";
- [ ] Ninguna de las anteriores

[Reference](https://en.cppreference.com/w/cpp/io/cout)

#### Q108. Considere el siguiente programa. ¿Cuál será la salida/error?

```cpp
#include<iostream>
#include<algorithm>
#include<string.h>
using namespace std;
bool compare(char c1, char c2){
return tolower(c1) > tolower(c2);    //LINE-1
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
- [ ] Error de compilación: la función no está definida

[Reference](https://www.geeksforgeeks.org/tolower-function-in-cpp/)

#### Q109. Considere el siguiente segmento de código. Complete el espacio en blanco en LINE-1 para que el programa imprima "not found"?

```cpp
#include <iostream>
#include <algorithm>
using namespace std;
int main() {
int data[] = {1,2,3,4,5};
int key = 5;
if(binary_search(__________))    //LINE-1
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

[Reference](https://www.geeksforgeeks.org/binary-search-algorithms-the-c-standard-template-library-stl/)

#### Q110. Considere el siguiente segmento de código. ¿Cuál será la salida?

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

[Reference](https://cplusplus.com/reference/algorithm/sort/)

#### Q111. Considere el siguiente segmento de código. ¿Cuál será la salida?

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

[Reference](https://en.cppreference.com/w/cpp/algorithm/rotate)

#### Q112. Considere el siguiente segmento de código. ¿Cuál será la salida?

```cpp
#include <iostream>
#include <vector>
using namespace std;
int main() {
const int size = 3, c = 65;
vector<char> vc(size, ’A’);
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

[Reference](https://en.cppreference.com/w/cpp/container/vector)

#### Q113. Considere el siguiente segmento de código. Elija la opción apropiada para completar el espacio en blanco en LINE-1, de modo que la salida del código sea: a C++ Program.

```cpp
#include <iostream>
#include <string>
using namespace std;
int main(void) {
string s1 = "C++ ";
string s2 = "Program";
__________________;    //LINE-1
cout << s1;
return 0;
}
```

- [x] s1 += s2
- [ ] strcat(s1, s2)
- [x] s1.append(s2)
- [ ] s1.insert(s2)

[Reference](https://www.geeksforgeeks.org/stdstringappend-in-c/)

#### Q114. Considere el siguiente segmento de código. Complete el espacio en blanco en LINE-1 de manera que la salida sea 5 2 3 4 5

```cpp
#include <iostream>
#include <algorithm>
using namespace std;
int main() {
int data[] = { 1, 2, 3, 4, 5 };
for (int i = 0; i < 1; i++) {
int j = data[i];
replace(data, data + 5, j, *(_________________));    //LINE-1
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

[Reference](https://www.geeksforgeeks.org/stdstringreplace-stdstringreplace_if-c/)

#### Q115. Considere el siguiente segmento de código. ¿Cuál será la salida?

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

[Reference](https://en.cppreference.com/w/cpp/container/stack)

#### Q116. Considere el siguiente segmento de código. ¿Qué declaración/declaraciones es/son correctas?

```cpp
int i = 5;
const int *p = &i;
int * const q = &i;
int const *r = &i;
int const * const s = &i;
*p = 10; //STMT-1
*q = 10; //STMT-2
*r = 10; //STMT-3
*s = 10; //STMT-4
```

- [ ] STMT-1
- [x] STMT-2
- [ ] STMT-3
- [ ] STMT-4

[Reference](https://www.geeksforgeeks.org/const-keyword-in-cpp/)

#### Q117. Considere el siguiente programa. ¿Cuál será la salida/error(es)?

```cpp
#include <iostream>
using namespace std;
char add(char c1 = ’a’) { return c1; }
char add(char c1 = ’a’, char c2 = ’b’) { return c1 + c2 - ’a’;}
char add(char c1 = ’a’, int d1 = 100){ return c1 + d1 - ’a’; }
char add(char c1 = ’a’, char c2 = ’b’, char c3) { return c1 + c2 + c3 - ’a’; }
int main() {
char c = add(’o’, ’k’);
cout << c << endl;
return 0;
}
```

- [ ] y
- [ ] z
- [x] Error de compilación: argumento por defecto faltante para "char add(char, char, char)"
- [x] Error de compilación: llamada de sobrecarga "add(char, char)" es ambigua

[Reference](https://learn.microsoft.com/en-us/cpp/cpp/function-overloading?view=msvc-170)

#### Q118. Considere el siguiente segmento de código. ¿Cuál será la salida?

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

[Reference](https://www.geeksforgeeks.org/output-of-the-program-use-macros-carefully/)

#### Q119. Considere el siguiente segmento de código. ¿Qué línea/s le darán un error?

```cpp
#include<iostream>
#define X 1
using namespace std;
int main(){
int i;
const int i1 = 2;
const int i2 = i1; //LINE-1
i2 = X;
i = i1;
i1 = i;
return 0;
//LINE-2
//LINE-3
//LINE-4
}
```

- [ ] LINE-1
- [x] LINE-2
- [ ] LINE-3
- [x] LINE-4

#### Q120. Considere el siguiente segmento de código. ¿Cuál será la salida/error?

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
- [x] Error de compilación: inicialización inválida de referencia no-const

#Explicación detallada:
El error ocurre porque se está intentando crear una referencia a un valor temporal. En la línea int &b = a+1; estamos intentando crear una referencia b al resultado de la expresión a + 1, que es un valor temporal. Las referencias deben estar vinculadas a un objeto real, no a un valor temporal o una expresión que no tiene una ubicación en memoria.

#### Q121. Considere el siguiente segmento de código. ¿Cuál será la salida?

```cpp
#include <iostream>
using namespace std;
int& func(int& i) {     //LINE-1
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

[Reference](https://www.ibm.com/docs/en/zos/2.4.0?topic=calls-pass-by-reference-c-only)

#### Q122. Considere el siguiente segmento de código. Elija la opción apropiada para llenar los espacios en blanco en LINE-1, de modo que la salida del código sea: 300 20000.

```cpp
#include <iostream>
using namespace std;
void compute(int n1, int n2, ________, ________){ //LINE-1
n3 = n1 + n2;
*n4 = n1 * n2;
}
int main(){
int a = 100, b = 200, c = 0, d = 0;
compute(a, b, c, &d); //LINE-2
cout << c << ", ";
cout << d;
return 0;
}
```

- [ ] int n3, int\* n4
- [x] int& n3, int \*n4
- [ ] int* n3, int* n4
- [ ] int& n3, int& n4

#### Q123. Considere el siguiente segmento de código. ¿Cuál será la salida/error?

```cpp
#include <iostream>
using namespace std;
int main() {
int a = 2, *b;
*b = 5;
int * const ptr;    // LINE-1
// LINE-2
ptr = b;
cout << *ptr;
return 0;
}
```

- [ ] `<garbage value>`
- [ ] 5
- [x] Error de compilación en LINE-1: const 'ptr' no inicializado
- [x] Error de compilación en LINE-2: asignación de variable de solo lectura 'ptr'

#### Q124. Considere el siguiente segmento de código. ¿Cuál será la salida/error?

```cpp
#include <iostream>
using namespace std;
void fun(int a = 5) { cout << a << endl; }
//LINE-1
int fun(int x = 10) { cout << x << endl; return 0; }    //LINE-2
int main() {
fun();
return 0;
}
```

- [ ] 5
- [ ] 10
- [ ] 5
- [x] Error de compilación en LINE-2: ambiguando nueva declaración de 'int fun(int)'

#### Q125. Considere el siguiente segmento de código. Complete el espacio en blanco en LINE-1 de manera que el programa imprima 5 + i3

```cpp
#include<iostream>
using namespace std;
struct complex{
int re, im;
void show(){ cout << re << " + i" << im; }
};
______________________________________{ //Line-1
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

[Reference](https://www.w3schools.com/cpp/cpp_structs.asp)

#### Q126. Considere el siguiente programa. ¿Qué línea/s generarán un error?

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
a = m.pra; //LINE-1
b = m.pub; //LINE-2
m.set_pr(100); //LINE-3
m.set_pu(200); //LINE-4
return 0;
}
```

- [x] LINE-1
- [ ] LINE-2
- [ ] LINE-3
- [ ] LINE-4

[Reference](https://stackoverflow.com/questions/4855422/c-classes-public-private-and-protected)

#### Q127. Considere la siguiente clase. Complete los espacios en blanco con especificadores de acceso apropiados para que el miembro y pueda ser accedido desde fuera de la clase pero el miembro x no pueda ser accedido.

```cpp
class Test{
________:
int x;
________:
int y;
/* Some more code */
};
```

- [ ] public, public
- [ ] public, private
- [ ] private, public
- [x] private, private

#### Q128. ¿Qué estándar de C++ agregó inicializadores de miembros por defecto en la clase?

- [ ] C++98
- [x] C++11
- [ ] C++14
- [ ] C++17.

#### Q129. ¿Puedes usar deducción de tipo auto para miembros de datos no estáticos?

- [ ] Sí, desde C++11
- [x] No
- [ ] Sí, desde C++20

#### Q130. ¿Necesitas definir un miembro de datos static inline en un archivo cpp?

- [x] No, la definición ocurre en el mismo lugar donde se declara un miembro static inline.
- [ ] Sí, el compilador necesita la definición en un archivo cpp.
- [ ] Sí, el compilador necesita una definición en todas las unidades de traducción que usan esta variable.

[Reference](https://en.cppreference.com/w/cpp/language/bit_field)

#### Q131. ¿Cuál es la salida del siguiente código:

```cpp
struct S {
    int a { 10 };
    int b { 42 };
};
S s { 1 };
std::cout << s.a << ", " << s.b;
```

- [ ] La salida es: 1, 0
- [ ] La salida es: 10, 42
- [x] La salida es: 1, 42

#### Q132. ¿Puede una variable static inline ser no constante?

- [x] Sí, es solo una variable regular.
- [ ] No, las variables inline deben ser constantes.

#### Q133. Considere el siguiente código:

```cpp
struct C {
    C(int x) : a(x) { }
    int a { 10 };
    int b { 42 };
};
C c(0);

```

- [ ] C::a se inicializa dos veces. La primera vez, se inicializa con 10, y luego la segunda vez con 0 en el constructor.
- [x] C::a se inicializa solo una vez con 0 en el constructor.
- [ ] El código no compila porque el compilador no puede decidir cómo inicializar el miembro C::a.
- [ ] 2 bytes

#### Q134. ¿Qué sucede cuando lanzas una excepción desde un constructor?

- [ ] El objeto se considera "creado" por lo que seguirá el tiempo de vida regular de un objeto.
- [x] El objeto se considera "parcialmente creado", y por lo tanto, el compilador no llamará a su destructor.
- [ ] El compilador llama a std::terminate ya que no puedes lanzar excepciones desde constructores.

#### Q135. ¿Qué sucede cuando compilas este código?

```cpp
struct Point { int x; int y; };
Point pt {.y = 10, .x = 11 };
std::cout << pt.x << ", " << pt.y;
```

- [x] El código no compila. Los designadores tienen que estar en el mismo orden que los miembros de datos en la clase Point.
- [ ] El código compila e imprime 11, 10.
- [ ] El código compila e imprime 10, 11.

#### Q136. ¿Funcionará este código en C++11?

```cpp
struct User { std::string name = "unknown"; unsigned age { 0 }; };
User u { "John", 101 };
```

- [ ] Sí, el código compila en modo C++11.
- [x] El código compila a partir del modo C++14.
- [ ] El código no compila ni siquiera en C++20.

#### Q137. Asuma que tiene un std::map<string, int> m;. Seleccione la única afirmación verdadera sobre el siguiente bucle:

```cpp
for (const pair<string, int>& elem : m)
```

- [x] A El bucle itera correctamente sobre el map, sin crear copias extra.

- [ ] B El bucle creará una copia de cada elemento en el map ya que el tipo de elem no coincide.

- [ ] C El código no compilará ya que un pair const no puede vincularse a un map.

#### Q138. Identifique la extensión correcta del archivo header definido por el usuario en C++.

- [ ] .cpp
- [ ] .hg
- [x] .h
- [ ] .hf

#### Q139. Identifique el tipo de constructor incorrecto.

```cpp
auto x = 4000.22;
```

- [x] Constructor Friend
- [ ] Constructor por defecto
- [ ] Constructor parametrizado
- [ ] Constructor de copia

#### Q140. ¿Cuál de los siguientes tipos de datos es soportado en C++ pero no en C?

- [x] bool
- [ ] int
- [ ] double
- [ ] float

[Reference]: https://stackoverflow.com/questions/1608318/is-bool-a-native-c-type

#### Q141. Identifique la sintaxis correcta para declarar arrays en C++.

- [x] int arr[10]
- [ ] array arr[10]
- [ ] array{10}
- [ ] int arr

[Reference]: (https://en.cppreference.com/w/cpp/language/array)

#### Q142. El tamaño de wchar_t es.

- [ ] 2
- [ ] 4
- [ ] 2 o 4
- [x] Depende del número de bits en el sistema

#### Q143. ¿Cuál de los siguientes bucles es mejor cuando conocemos el número de iteraciones?

- [ ] while
- [x] for
- [ ] do
- [ ] All of the above

#### Q144. ¿Qué palabra clave se usa para definir macros en C++?

- [ ] #macro
- [x] #define
- [ ] macro
- [ ] keyword

#### Q145. ¿Cuál de los siguientes operadores se debe preferir sobrecargar como una función global en lugar de un método miembro?

- [ ] Postfix ++
- [x] Operador de comparación
- [ ] Operador de inserción <<
- [ ] Prefix++

#### Q146. ¿Cómo podemos restringir la asignación dinámica de objetos de una clase usando new?

- [ ] Sobrecargando el operador new
- [ ] Haciendo un operador new privado vacío.
- [x] Haciendo operadores new y new[] privados vacíos
- [ ] Sobrecargando los operadores new y new[]

#### Q147. ¿Cuál es la complejidad temporal del código siguiente?

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

[Reference](<https://medium.com/enjoy-algorithm/analysis-of-loop-in-programming-cc9a644ef8cd#:~:text=At%20each%20step%20of%20the%20iteration%2C%20the%20nested%20loop%20is,%20%3D%20O(n%C2%B2)>)

#### Q148. ¿Cuál es la salida del código dado a continuación?

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

Tanto **++a** como **a++** incrementan el valor de a en 1 (es decir: 11) y por lo tanto k+m se convierte en 22.

#### Q149. ¿Qué construcción de C++ se usa para el manejo de excepciones?

- [x] try-catch
- [ ] if-else
- [ ] for loop
- [ ] switch-case

#### Q150. ¿Cuál es el propósito de la declaración `break` en un bucle en C++?

- [ ] Salir del programa
- [ ] Omitir la iteración actual y continuar con la siguiente
- [x] Terminar el bucle
- [ ] Retornar un valor

[Reference]: (https://www.tutorialspoint.com/cprogramming/c_break_statement.htm)

#### Q151. En C++, ¿cuál es el propósito de la palabra clave `const` cuando se usa con una variable?

- [x] Hace que la variable sea inmutable
- [ ] Cambia el tipo de datos
- [ ] Define una función constante
- [ ] Hace que la variable sea un pointer

#### Q152. ¿Qué es más efectivo al llamar funciones de C++?

- [x] Llamada por referencia
- [ ] Llamada por valor
- [ ] Llamada por pointer
- [ ] Llamada por objeto

[Reference]: (https://www.algbly.com/More/MCQs/Cpp-mcq/Cpp-functions.html)

#### Q153. ¿Cuál será la salida del siguiente programa de C++?

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

- [ ] Segmentation fault
- [x] “Constructor llamado” cinco veces y luego “Destructor llamado” cinco veces
- [ ] “Constructor llamado” cinco veces y luego “Destructor llamado” una vez
- [ ] Error

#### Q154. ¿Cuál opción _no_ está relacionada con declarar la variable miembro count como static en my_class?

```cpp
class my_class{
    public: static int count;
}
```

- [ ] Todos los objetos que intentan acceder a su variable miembro count realmente se refieren a la única variable static count vinculada a la clase.
- [ ] La variable existe incluso cuando no se han definido objetos de la clase, por lo que puede modificarse en cualquier punto del código fuente.
- [x] La variable no puede ser modificada por ninguna parte del código en la misma aplicación o thread. Sin embargo, otros threads pueden modificarla.
- [ ] La variable se asigna solo una vez, independientemente de cuántos objetos se instancien, porque está vinculada a la clase misma, no a sus instancias.

#### Q155. ¿Cuál es el propósito de la palabra clave `constexpr` en C++?

- [ ] Se usa para definir constantes en C++.
- [ ] `constexpr` se usa para especificar que una variable es un constant pointer.
- [x] `constexpr` se usa para indicar que una expresión puede ser evaluada en tiempo de compilación, haciéndola adecuada para usar en expresiones constantes.
- [ ] Es una palabra clave usada para crear funciones asíncronas.

[Ref](https://learn.microsoft.com/en-us/cpp/cpp/constexpr-cpp?view=msvc-170#:~:text=constexpr%20indicates%20that%20the%20value,template%20arguments%20and%20array%20declarations.)

#### Q156. ¿Qué es un template metaprogram en C++?

- Ref(https://www.geeksforgeeks.org/template-metaprogramming-in-c/)

- [ ] Un template metaprogram es un lenguaje de programación de alto nivel.
- [ ] Se refiere a metaprogramación que usa templates en C++.
- [ ] Es un tipo de patrón de diseño de interfaz de usuario.
- [x] Un template metaprogram es una computación en tiempo de compilación, donde los templates y la especialización de templates se usan para realizar cálculos en tiempo de compilación.

#### Q157. Identifique el ejemplo correcto de un operador de pre-incremento.

- [x] ++i
- [ ] i++
- [ ] --i
- [ ] +i

#### Q158. ¿Cuál será la salida del siguiente código?

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

- [ ] Transpuesta de la matriz
- [x] La misma matriz
- [ ] Imagen espejo de la matriz
- [ ] Matriz invertida

#### Q159. ¿Qué es una condición de carrera (race condition) en C++?

- [ ] Una condición donde el programa ejecuta más rápido de lo esperado
- [x] Una condición donde múltiples threads acceden a datos compartidos concurrentemente, y el resultado depende del tiempo de su ejecución
- [ ] Una condición donde dos threads compiten por tiempo de CPU
- [ ] Una condición donde un bucle se ejecuta demasiado rápido y necesita ser ralentizado

[Reference](https://en.cppreference.com/w/cpp/language/memory_model)

#### Q160. Considere el siguiente código que tiene una condición de carrera. ¿Cuál es la forma correcta de arreglarla?

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

- [ ] Agregar la palabra clave `volatile`: `volatile int counter = 0;`
- [x] Usar `std::mutex` para lock/unlock alrededor de `counter++` en la sección crítica
- [ ] Usar `std::this_thread::sleep_for()` para retrasar cada incremento
- [ ] Cambiar `counter++` a `++counter` para operación atómica

[Reference](https://en.cppreference.com/w/cpp/thread/mutex)
