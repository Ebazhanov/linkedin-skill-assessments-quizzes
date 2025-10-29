## C++

#### P1. ¿Cuál es la salida de este código?

```cpp
vector<int> v(22);
bool b = (v[6]);
printf("%d", !b);
```

- [ ] Falso
- [ ] 0
- [x] 1
- [ ] Este código tiene un error.

#### P2. ¿Cuál de las siguientes es una razón por la que usar esta línea se considera una mala práctica? (_Alternativa_: ¿Por qué usar esta línea se considera una mala práctica?)

```cpp
using namespace std;
```

- [ ] El código compilado siempre es más grande debido a todos los símbolos importados.
- [x] Si el código utiliza una función definida en dos bibliotecas diferentes con el mismo prototipo pero posiblemente con diferentes implementaciones, habrá un error de compilación debido a la ambigüedad.
- [ ] Incluye automáticamente todos los archivos de encabezado en la biblioteca estándar (cstdint, cstdlib, cstdio, iostream, etc).
- [ ] Hace que el compilador aplique la inclusión exclusiva de archivos de encabezado pertenecientes a la biblioteca estándar, generando un error de compilación cuando se incluye un archivo de encabezado diferente.

[Referencia](https://www.geeksforgeeks.org/using-namespace-std-considered-bad-practice/)

#### P3. ¿Cuál es el tamaño más pequeño que una variable de tipo child_t puede ocupar en memoria?

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

[Referencia](https://en.cppreference.com/w/cpp/language/bit_field)

#### P4. ¿Cuáles son los vectores v1 y v2 después de ejecutar el código?

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

#### P5. ¿Cuál de las siguientes es una afirmación verdadera sobre la diferencia entre punteros e iteradores?

- [ ] Mientras que los punteros son variables que contienen direcciones de memoria, los iteradores son funciones genéricas utilizadas para recorrer contenedores. Esta función permite al programador implementar código de lectura y escritura mientras se recorre el contenedor.
- [x] Incrementar un iterador siempre significa acceder al siguiente elemento en el contenedor (si existe), sin importar el contenedor. Incrementar el puntero significa apuntar al siguiente elemento en memoria, no siempre el siguiente elemento.
- [ ] Los punteros son variables que contienen direcciones de memoria, mientras que el iterador son enteros sin signo que se refieren a desplazamientos en arreglos.
- [ ] Todos los iteradores se implementan con punteros, por lo que todos los iteradores son punteros, pero no todos los punteros son iteradores.

[Referencia](https://stackoverflow.com/a/31128162)

#### P6. ¿Cuál es el almacenamiento ocupado por u1?

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

[Referencia](https://en.cppreference.com/w/cpp/language/union)

#### P7. ¿Cuál de los siguientes operadores puede ser sobrecargado?

- [ ] `?:`
- [x] `new`
- [ ] `::`
- [ ] `.`

[Referencia](https://www.tutorialspoint.com/operators-that-cannot-be-overloaded-in-cplusplus)

#### P8. ¿Cuál de las siguientes muestra el contenido del vector apuntado por v1 y v2 después de ejecutar este código?

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

#### P9. ¿Cuál de las siguientes NO es una diferencia entre una clase y una estructura?

- [ ] Debido a que las estructuras son parte del lenguaje de programación C, hay cierta complejidad entre las estructuras de C y C++. Este no es el caso con las clases.
- [ ] Las clases pueden tener funciones miembro; las estructuras son privadas.
- [ ] El especificador de acceso predeterminado para miembros de una estructura es público, mientras que para miembros de la clase es privado.
- [x] Los parámetros de tipo de plantilla se pueden declarar con clases, pero no con la palabra clave struct.

Las plantillas se pueden usar tanto con clases como con estructuras  
[Referencia](https://docs.microsoft.com/en-us/cpp/cpp/struct-cpp?view=msvc-170)  
[Referencia](https://www.fluentcpp.com/2017/06/13/the-real-difference-between-struct-class/)

#### P10. Suponga que necesita mantener una estructura de datos con permiso para acceder a algún recurso basado en los días de la semana, pero no puede usar una variable bool para cada día. Necesita usar un bit por día de la semana. ¿Cuál de las siguientes es una implementación correcta de una estructura con campos de bits para esta aplicación?

- [x] A

```cpp
typedef struct {
    int sunday:1;
    int monday:1;
    // más días
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
    // más días
    bit friday:1;
    bit saturday:1;
} weekdays;

```

- [ ] D

```cpp
typedef struct {
    bit sunday;
    bit monday;
    // más días
    bit friday;
    bit saturday;
} weekdays;
```

[Referencia](https://en.cppreference.com/w/cpp/language/bit_field) _NOTA_: La sintaxis correcta es que cada variable tiene un tamaño de 1 bit. `bit` no es un tipo en C++.

#### P11. ¿Qué es un lvalue?

- [ ] Es una expresión constante, es decir, una expresión compuesta de constantes y operaciones.
- [ ] Es una expresión que representa un objeto con una dirección.
- [ ] Es una expresión adecuada para el operando del lado izquierdo en una operación binaria.
- [x] Es un valor de ubicación, es decir, una dirección de memoria adecuada para asignar a un puntero o referencia.

#### P12. ¿Qué hace el especificador de tipo auto en esta línea de código (desde C++11)?

```cpp
auto x = 4000.22;
```

- [x] Especifica que el tipo de x se deducirá del inicializador - en este caso, double.
- [ ] Especifica que el tipo de x es automático, lo que significa que puede ser asignado a diferentes tipos de datos a lo largo del programa.
- [ ] Especifica que x es una variable con duración de almacenamiento automático.
- [ ] Especifica que se asignará más memoria para x en caso de que necesite más espacio, evitando la pérdida de datos debido al desbordamiento.

#### P13. Una plantilla de clase es ¿qué?

- [x] Una clase escrita con el paradigma de programación genérica, especificando comportamiento en términos de parámetro de tipo en lugar de tipo específico.
- [ ] Una superclase en blanco destinada a la herencia y el polimorfismo.
- [ ] Una clase que solo consiste en una variable miembro, sin constructor, destructor o funciones miembro.
- [ ] Código fuente esqueleto para una clase donde el programador debe completar partes específicas para definir los tipos de datos y algoritmos utilizados.

[Referencia](https://www.mygreatlearning.com/blog/templates-in-cpp/)

#### P14. ¿Cuál es el operador ternario equivalente a este fragmento de código?

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

[Referencia](https://www.w3schools.com/cpp/cpp_conditions_shorthand.asp)

#### P15. ¿Cuál es la salida del código dado a continuación?

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

#### P16. ¿Cuál es el significado de las dos partes especificadas entre paréntesis en un bucle for basado en rango, separadas por dos puntos?

- [x] La primera es una declaración de variable que contendrá un elemento en una secuencia. La segunda es la secuencia a recorrer.
- [ ] La primera es un iterador, y la segunda es el valor de incremento que se agregará al iterador.
- [ ] La primera es la variable iteradora. La segunda es un `std::pair` que especifica el rango (inicio y fin) en el que la variable iterará.
- [ ] La primera es un objeto contenedor. La segunda es un `std::pair` que especifica el rango (inicio y fin) en el que se accederá a los elementos dentro del bucle.

#### P17. ¿Cuál es la salida del código dado a continuación?

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

#### P18. ¿Cuál es la salida de este bloque de código?

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

Nota: Conversión implícita de 'int' a 'int8_t' (también conocido como 'signed char') cambia el valor de 200 a -56

#### P19. ¿Cuál es la salida después de ejecutar este fragmento de código?

```cpp
int x=5, y=2;
if(x & y) {
    /*_parte A_*/
}
else {
    /*_parte B_*/
}
```

- [ ] La parte A se ejecuta porque x==5 (verdadero) e y==2 (verdadero), por lo tanto la operación AND se evalúa como verdadero.
- [x] La parte B se ejecuta porque (x & y) resulta en 0, o falso.
- [ ] La parte A se ejecuta porque (x & y) resulta en un valor distinto de cero, o verdadero.
- [ ] La parte B se ejecuta porque la declaración (x & y) no es válida, por lo tanto falso.

[Referencia](https://stackoverflow.com/questions/63867765/dont-understand-why-if-5-2-is-false)

#### P20. ¿Cuál es una definición válida para la función `get_length`, que devuelve la longitud de una cadena terminada en nulo?

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

#### P21. ¿Qué clase STL es la más adecuada para implementar una colección de datos que siempre está ordenada de modo que la operación pop siempre obtenga el mayor de los elementos? Suponga que solo está interesado en las operaciones push y pop.

- [ ] `std::list`
- [ ] `std::vector`
- [x] `std::priority_queue`
- [ ] `std::map`

#### P22. ¿Cuál es el significado de las tres secciones especificadas entre paréntesis en un bucle for separadas por punto y coma?

- [ ] La primera es el nombre de la variable iteradora, la segunda es el número de veces a iterar, y la tercera es el incremento o decremento deseado (especificado con un entero con signo).
- [x] La primera es el bloque de inicialización, la segunda es la condición para iterar, y la tercera es el bloque de incremento.
- [ ] La primera es la variable iteradora, la segunda es el contenedor en el que debe operar, y la tercera es una condición de salida para abortar en cualquier momento.
- [ ] La primera es el nombre de la variable iteradora, la segunda es el valor inicial para la variable iteradora, y la tercera es el valor de parada (el último valor más uno).

#### P23. ¿Qué imprime este código?

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

[Referencia](https://www.geeksforgeeks.org/pre-increment-and-post-increment-in-c/)

#### P24. ¿Qué es verdad sobre la variable llamada `ptr`?

```cpp
void *ptr;
```

- [ ] Es un puntero inicializado en NULL.
- [ ] Es un puntero a una función void.
- [ ] Esa declaración causa un error del compilador, ya que los punteros deben especificar un tipo.
- [x] Es un puntero a un valor sin tipo específico, por lo que puede ser convertido para apuntar a cualquier tipo.

[Referencia](https://en.cppreference.com/w/cpp/language/pointer)

#### P25. ¿Cuál es la salida del código dado a continuación?

```cpp
int c=3; char d='A';
std::printf("c is %d and d is %c",c,d);
```

- [ ] c is d and d is c
- [ ] c is A and d is 3
- [x] c is 3 and d is A
- [ ] c is c and d is d

#### P26. ¿Cuál es la salida de este código?

```cpp
printf("1/2 = %f",(float)(1/2));
```

- [ ] 1/2 = 0.499999
- [ ] 1/2 = 0
- [x] 1/2 = 0.000000
- [ ] 1/2 = 0.5

#### P27. ¿Cuál es la diferencia entre un miembro de clase público y uno privado?

- [ ] Los miembros públicos son iguales a las variables globales, por lo que cada parte del código tiene acceso a ellos. Los miembros privados son iguales a las variables automáticas, por lo que solo su clase tiene acceso a ellos.
- [ ] Los miembros públicos son accesibles a cualquier aplicación en ejecución. Los miembros privados son accesibles solo a la aplicación donde se instancia el objeto.
- [ ] Los miembros públicos se compilarán como variables compartidas en un entorno multihilo. Los miembros privados se compilarán como variables locales de hilo.
- [x] Los miembros públicos pueden ser accedidos por cualquier función. Los miembros privados solo pueden ser accedidos por las funciones miembro de la misma clase y los amigos de la clase.

[Referencia](https://www.geeksforgeeks.org/difference-between-public-and-private-in-c-with-example/)

#### P28. ¿Cuál es el valor de `x` después de ejecutar este código?

```cpp
int x=10, a=-3;
x+=a;
```

- [ ] 3
- [x] 7
- [ ] -3
- [ ] 13

#### P29. ¿Cuál afirmación es verdadera?

- [ ] Solo las clases pueden tener variables miembro y métodos.
- [x] C++ soporta herencia múltiple.
- [ ] C++ soporta solo herencia simple.
- [ ] Solo las estructuras pueden heredar.

#### P30. Considere un puntero a void, llamado `ptr`, que ha sido configurado para apuntar a una variable de punto flotante `g`. ¿Cuál opción es una forma válida de desreferenciar `ptr` para asignar su valor apuntado a una variable float `f` más adelante en el programa?

```cpp
float g;
void *ptr=&g;
```

- [ ] `float f=*(float)ptr;`
- [ ] `float f=(float *)ptr;`
- [ ] `float f=(float)*ptr;`
- [x] `float f=*(float *)ptr;`

#### P31. ¿Qué es el operador `.*` y qué hace?

- [ ] Es lo mismo que el operador de acceso a miembro de clase, o operador de flecha `(->)`, que permite acceder a un miembro de un objeto a través de un puntero al objeto.
- [x] Es el operador de puntero a miembro, y permite acceder a un miembro de un objeto a través de un puntero a ese miembro de clase específico.
- [ ] Es el operador de acceso a miembro con dirección del operador, que devuelve la dirección de un miembro de clase o estructura.
- [ ] Es una combinación del operador de acceso a miembro `(.)` y el operador de desreferencia `(*)`, por lo que permite acceder al objeto al que apunta un puntero de miembro.

[Referencia](https://en.cppreference.com/w/cpp/language/operator_member_access)

#### P32. Para estas declaraciones, ¿cuál opción muestra cuatro formas equivalentes de asignar el carácter "y" en la cadena a una variable char c?

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

#### P33. ¿Cuál opción es la declaración correcta para la clase llamada Dog, derivada de la clase Animal?

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

#### P34. ¿Cuál es la salida de este código dado a continuación?

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

Técnicamente, si un `char` es `signed` o `unsigned` depende de la implementación;
en el último caso, la segunda respuesta sería correcta.
[Referencia](https://en.cppreference.com/w/cpp/language/types)

#### P35. ¿Cómo puede el código C++ llamar a una función C?

- [ ] simplemente llamando al código C
- [ ] No hay forma de que C++ llame a una función C
- [x] usando extern "C"
- [ ] importando el código fuente C

#### P36. ¿Cuál opción NO es una definición de tipo válida de una estructura que contiene coordenadas x e y como enteros, y que puede usarse exactamente como se muestra para la variable llamada `center`?

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

#### P37. ¿Cuál opción NO produce la misma salida que este fragmento de código? Suponga que la variable `i` no se usará en ningún otro lugar del código.

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

#### P38. ¿Qué hace esta parte de un archivo main.cpp?

```cpp
#include "library.h"
```

- [ ] Hace que la cadena de herramientas compile todo el contenido de library.h para que su código ejecutable esté disponible cuando sea necesario por la aplicación final.
- [ ] Selecciona cuidadosamente library.h para las declaraciones y definiciones de todos los datos y funciones utilizadas en el resto del archivo fuente main.cpp, finalmente reemplazando la directiva `#include` con esas declaraciones y definiciones.
- [ ] Informa al enlazador que algunas funciones o datos utilizados en el archivo fuente main.cpp están contenidos en library.h, para que puedan ser llamados en tiempo de ejecución. Esto también se conoce como enlace dinámico.
- [x] Causa el reemplazo de la directiva `#include` por todo el contenido del archivo fuente library.h. Esto es similar a la operación de Copiar-Pegar de library.h en main.cpp.

#### P39. Considere esta declaración de función de `is_even`, que toma un entero y devuelve true si el argumento es un número par y false en caso contrario. ¿Cuáles declaraciones son correctas para versiones sobrecargadas de esa función para soportar números de punto flotante y representaciones de cadena de números?

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

#### P40. ¿Cuál opción es un guardia de inclusión para el archivo de encabezado `my_library.h`?

- [ ] A

```cpp
#ifdef MY_LIBRARY_H
#define MY_LIBRARY_H

// contenido de my_library.h

#endif /* MY_LIBRARY_H */
```

- [x] B

```cpp
#ifndef MY_LIBRARY_H
#define MY_LIBRARY_H

// contenido de my_library.h

#endif /* MY_LIBRARY_H */
```

- [ ] C

```cpp
#ifdef MY_LIBRARY_H
#undef MY_LIBRARY_H

// contenido de my_library.h

#endif /* MY_LIBRARY_H */
```

- [ ] D

```cpp
#define MY_LIBRARY_H
#include MY_LIBRARY_H

// contenido de my_library.h

#undef MY_LIBRARY_H
```

#### P41. ¿Qué está mal con esta definición cuando se usa un compilador pre-C++11?

```cpp
std::vector<std::vector<int>> thematrix;
```

- [ ] No hay nada malo con ella.
- [ ] Un `std::vector` no puede contener más contenedores `std::vector` como sus elementos.
- [ ] La sintaxis correcta debería ser: `std::vector[std::vector[int]] thematrix;`
- [x] `>>` se analiza como el operador de desplazamiento a la derecha, y por lo tanto resulta en un error de compilación.

#### P42. ¿A qué es equivalente la declaración a continuación?

#### P42.b. ¿A qué es equivalente la declaración?

```cpp
sprite->x
```

- [ ] `sprite.x`
- [ ] `sprite.*x`
- [x] `(*sprite).x`
- [ ] `*sprite.x`

#### P43. Considere una clase llamada `complexNumber`. ¿Qué código resultará en un objeto equivalente?

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

#### P44. ¿Cuál es el resultado de ejecutar este fragmento de código?

```cpp
bool x=true, y=false;

if (~x || y) {
    /*parte A*/
} else {
    /*parte B*/
}
```

- [ ] La parte A se ejecuta porque la expresión `(~x || y)` siempre resulta en verdadero si `y==false`.
- [ ] La parte B se ejecuta porque la declaración `(~x || y)` no es válida, por lo tanto falso.
- [x] La parte A se ejecuta porque `~x` no es cero, lo que significa verdadero.
- [ ] La parte B se ejecuta porque `~x` es falso e `y` es falso, por lo tanto la operación OR se evalúa como falso.

#### P45. ¿Cuál sería la salida de este código?

```cpp
int32_t nums[3]={2,4,3};
std::cout << ( nums[0] << nums[1] << nums[2] );
```

- [ ] La salida son las direcciones de `nums[0]`, `nums[1]`, y `nums[2]`, en ese orden, sin espacios.
- [x] 256
- [ ] `0`
- [ ] `243`

#### P46. ¿Cuál es la salida de este código?

```cpp
float values[5]={0.54f, 2.71828f, 3.14159f, 5.499999f, 10.0f};
for(auto f:values)
    printf("%i ",(int)(f+0.5f));
```

- [ ] `0.54 2.71828 3.14159 5.499999 10.0`
- [ ] `1 3 4 6 11`
- [ ] `0 2 3 5 10`
- [x] `1 3 3 5 10`

#### P47. ¿Cuál de las siguientes clases STL es la más adecuada para implementar una guía telefónica? Suponga que cada entrada contiene un nombre y un número de teléfono, sin duplicados, y desea tener una búsqueda por nombre.

- [ ] `std::priority_queue`
- [ ] `std::list`
- [ ] `std::vector`
- [x] `std::map`

[Referencia](https://en.cppreference.com/w/cpp/container/map)

#### P48. ¿Qué hace este programa?

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
- [ ] Añade el contenido de text1.txt en text2.txt - es decir, reemplaza el contenido de text2.txt por la concatenación de text2.txt y text1.txt.

[Referencia](https://en.cppreference.com/w/cpp/header/fstream)

#### P49. ¿Cuál de las siguientes NO es una consecuencia de declarar la variable miembro `count` de my_class como static? / Alt.: ¿Cuál afirmación es verdadera al declarar la variable miembro `count` como static?

```cpp
class my_class {
    public: static int count;
}
```

- [x] La variable no puede ser modificada por ninguna parte del código en la misma aplicación o hilo. Sin embargo, otros hilos pueden modificarla.
- [ ] La variable existe incluso cuando no se han definido objetos de la clase, por lo que puede ser modificada en cualquier punto del código fuente.
- [ ] La variable se asigna solo una vez, independientemente de cuántos objetos se instancien, porque está vinculada a la clase misma, no a sus instancias.
- [ ] Todos los objetos que intentan acceder a su variable miembro count realmente se refieren a la única variable count vinculada a la clase static.

[Referencia](https://en.cppreference.com/w/cpp/language/static)

#### P50. ¿Cuál es el tipo asumido de una constante representada en el código fuente como `0.44`?

- [x] double
- [ ] long float
- [ ] long double
- [ ] float

#### P51. ¿Cuál es una forma apropiada de eliminar `my_object` como se muestra a continuación?

```cpp
my_class *my_object = new my_class();
```

- [x] `delete(my_object);`
- [ ] `free(my_object);`
- [ ] El recolector de basura destruirá el objeto eventualmente.
- [ ] Salir del alcance destruirá el objeto.

#### P52. ¿Cuál es la forma correcta de llamar a la función miembro `count` para el puntero de objeto llamado `grades`?

```cpp
class my_array{
    public:
        int count();
};  // ... más miembros arriba

int main(){
    my_array *grades = new my_array();
};  // ... más código arriba
```

- [ ] `grades.count();`
- [ ] `my_array->count();`
- [x] `grades->count();`
- [ ] `my_array.count();`

[Referencia](https://en.cppreference.com/w/c/language/operator_member_access)

#### P53. ¿Cuál sería la salida de este código?

```cpp
int i0=4, i1=6, i2=8;
int& nums[3]={i2,i0,i1};
std::cout<<nums[0]<<nums[1]<<nums[2];
```

- [x] No hay salida. El código causa un error del compilador porque `nums` es un arreglo de referencias, lo cual es ilegal.
- [ ] 846
- [ ] La salida son las direcciones de `i2`, `i0`, e `i1`, en ese orden, sin espacios.
- [ ] 468

[Referencia](https://en.cppreference.com/w/cpp/language/array)

#### P54. ¿Este código causa un error del compilador? Si es así, ¿por qué, y si no, ¿qué es `child_t`?

```cpp
typedef struct{
    unsigned int  age    : 4;
    unsigned char gender : 1;
    char                 : 0;
    unsigned int  size   : 2;
}child_t;
```

- [ ] Sí, causa un error del compilador porque el carácter de dos puntos no está permitido en definiciones de estructura.
- [x] No, y `child_t` es un tipo definido como una estructura con campos de bits. Tiene 4 bits para age y 1 bit para gender en el primer byte, y 2 bits para size en el segundo byte.
- [ ] Sí, causa un error del compilador porque hay un campo sin nombre.
- [ ] Sí, causa un error del compilador porque un campo está definido como teniendo un tamaño de 0.

[Referencia](https://en.cppreference.com/w/cpp/language/bit_field)

#### P55. ¿A qué es equivalente esta expresión?

```cpp
A->B
```

- [ ] `*(A.B)`
- [ ] `B=A`
- [x] `(*A).B`
- [ ] `&A.B`

Nota: una variante más simple de la pregunta a continuación.

#### P56. ¿A qué es equivalente esta expresión?

```cpp
A->B->C->D
```

- [ ] `A.B.C.D`
- [ ] `*A.*B.*C.*D`
- [ ] `&A.&B.&C.&D`
- [x] `*(*((*A).B).C).D`

**Nota:** una variante más compleja de la pregunta anterior.

#### P57. ¿Qué hace esta función?

```cpp
auto buff = new char[50];
std::memset(buff,20,50);
```

- [ ] Declara un buffer de memoria llamado buff que comienza en la dirección 20 y termina en la dirección 70.
- [ ] Establece todos los bits en el arreglo llamado buffer desde su elemento en el índice 20 hasta su elemento en el índice 50.
- [x] Escribe el valor 20 en cada dirección de memoria desde buff hasta buff+49.
- [ ] Declara un buffer de memoria llamado buff que comienza en la dirección 20 y termina en la dirección 50.

[Referencia](https://en.cppreference.com/w/cpp/string/byte/memset)

#### P58. Considere una clase llamada `CustomData`. ¿Cuál opción es una sintaxis de declaración correcta para sobrecargar el operador posfijo `++` como un miembro de clase?

- [ ] `CustomData& operator++();`
- [ ] `void operator++(CustomData);`
- [ ] `CustomData operator++(CustomData);`
- [x] `CustomData operator++(int);`

[Referencia](https://en.cppreference.com/w/cpp/language/operators)

#### P59. Desea ordenar my_array, declarado a continuación. ¿Cuál opción es la llamada correcta a std::sort, usando una expresión lambda como función de comparación?

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

[Referencia](https://docs.microsoft.com/en-us/cpp/cpp/lambda-expressions-in-cpp?view=msvc-160)

#### P60. ¿Cuál opción es la implementación más razonable de la función std::mutex::lock() usando std::mutex::try_lock()?

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

#### P61. ¿Cuál es la diferencia principal entre estas dos Funciones?

```cpp
std::mutex::lock()
std::mutex::try_lock()
```

- [ ] `lock()` tiene un privilegio mayor sobre `try_lock()`. Esto significa que tiene una mejor oportunidad de adquirir un mutex `con lock()`.
- [x] Ambos intentan adquirir un bloqueo, pero `lock()` bloquea si el mutex no está disponible, mientras que `try_lock()` devuelve si el mutex está disponible o no.
- [ ] `lock()` fuerza la preferencia, mientras que `try_lock()` sugiere la preferencia.
- [ ] Si el mutex no está disponible, `try_lock()` devuelve con un código correspondiente, mientras que `lock()` arrebata el mutex del hilo que actualmente lo tiene.

Nota: variante de la pregunta anterior.

[Referencia](https://en.cppreference.com/w/cpp/thread/mutex/try_lock)

#### P62. ¿Cuál es el propósito de un destructor?

- [x] Permite al programador escribir el código necesario para liberar los recursos adquiridos por el objeto antes de eliminar el objeto mismo.
- [ ] Elimina un objeto. Un ejemplo de un destructor es la función `delete()`.
- [ ] Termina un programa. Esto puede lograrse como una llamada de función regular o como una excepción.
- [ ] No hay destructores en C++.

#### P63. ¿Cuál es un beneficio de declarar el parámetro como una referencia `const` en lugar de declararlo como un objeto regular?

```cpp
int calculateMedian(const my_array& a)
```

- [ ] En realidad, los objetos no se pueden pasar como variables regulares, porque requieren una llamada al constructor. Por lo tanto, una referencia `const` es la única forma de pasar instancias de clase a funciones.
- [ ] No hay beneficios porque una referencia y un objeto se tratan como la misma cosa.
- [x] El calificador `const` prohíbe que el código modifique el argumento, por lo que el programador puede estar seguro de que el objeto fuente permanecerá sin cambios. / Alt.: El argumento se pasa como una referencia, por lo que si el objeto my_array pasado es grande, el programa requerirá menos tiempo y memoria.
- [ ] El argumento se pasa como una referencia, por lo que la función recibe una copia que puede ser modificada sin afectar la variable original.

[Referencia](https://stackoverflow.com/a/2627179/10773894)

#### P64. ¿Qué es un guardia de inclusión?

- [ ] una directiva de preprocesador que previene comportamientos inconsistentes en líneas que contienen las directivas #ifdef, #ifndef, o #elif
- [ ] una opción del compilador que previene que el código del usuario incluya bibliotecas adicionales
- [x] una declaración de preprocesador que previene que un archivo fuente sea incluido más de una vez en un proyecto
- [ ] una biblioteca que agrega características de seguridad como mutexes, temporizadores de vigilancia y aserciones al proyecto

#### P65. ¿Cuál sería la declaración correcta de un constructor predeterminado para una clase llamada Sprite?

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

#### P66. ¿Cuál es el propósito de esta línea en un archivo de encabezado?

```cpp
#pragma once
```

- [ ] restringir el uso de su contenido a solo un archivo fuente
- [ ] decirle al compilador que solo una variable puede ser instanciada de las clases o tipos contenidos en este archivo de encabezado
- [ ] ayudar al compilador a terminar más rápido asegurando que solo una pasada del compilador es necesaria para el código incluido en este archivo de encabezado
- [x] hacer que el compilador analice ese archivo de encabezado solo una vez, incluso si está incluido varias veces en el fuente

[referencia aquí](https://en.cppreference.com/w/cpp/preprocessor/impl)

#### P67. ¿Qué es una variable de tipo double?

- [ ] una tupla de 2 elementos
- [ ] un número entero
- [x] un número de punto flotante
- [ ] una cadena con más de 255 caracteres

[Referencia](https://www.educba.com/c-plus-plus-double/)

#### P68. Además de desplazar bits a la izquierda, ¿para qué se usa el operador << ?

- [ ] desplazar caracteres a la izquierda en una cadena.
- [x] insertar caracteres en un flujo de salida como std::cout.
- [ ] comparar números de punto flotante como menor que.
- [ ] asignar una variable a una referencia.

#### P69. ¿Cuál opción es una razón para especificar el tipo de un puntero en lugar de usar `void *`, que funciona como un puntero a cualquier tipo?

- [ ] El compilador necesita el tipo de datos para asegurarse de que el puntero no se va a usar en tipos ilegales no apuntables como funciones, etiquetas, punteros y referencias.
- [ ] `void *` no funciona para ningún tipo. El lenguaje no permite asignar nada más que `void` a un puntero a `void *`.
- [x] El compilador necesita el tipo de datos para saber cuánta memoria asignar para el puntero porque diferentes tipos de datos requieren diferentes longitudes de puntero.
- [ ] Sí, causa un error del compilador porque un campo está definido como teniendo un tamaño de 0.

[Referencia](https://stackoverflow.com/questions/9802585/why-is-the-data-type-needed-in-pointer-declarations)

#### P70. ¿Qué está mal con este fragmento de código?

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

- [ ] Se supone que la función main debe tener un tipo de retorno void.
- [ ] `std::cin` y `std::cout` no son válidos. Los nombres correctos para los flujos de entrada y salida de caracteres son `cin` y `cout`.
- [ ] Se supone que se debe usar la dirección de `str`. Es decir `&str` en lugar de `str`.
- [x] El flujo del operador de entrada está invertido. debería comenzar desde `std::cin` y luego fluir (>>) hacia `str`.

#### P71. Cuando se coloca en un contexto de ejecución válido, ¿cuál declaración asignará dinámicamente memoria del heap para un entero de valor 11?

- [ ] `int anInt = new int(11);`
- [ ] `int* anInt = new int[11];`
- [ ] `int anInt = new int[11];`
- [x] `int* anInt = new int(11);`

#### P72. ¿Cuál opción describe mejor el tipo `long`?

- [x] un número entero de al menos 32 bits
- [ ] una cadena con más de 255 caracteres
- [ ] un puntero
- [ ] un número de punto flotante de 64 bits

#### P73. ¿Cuál de los siguientes tipos tiene la funcionalidad más cercana a una clase?

- [x] `struct`
- [ ] `union`
- [ ] `enum`
- [ ] `namespace`

[Referencia](https://en.cppreference.com/w/c/language/struct)

#### P74. Dados estos registros en un mapa, ¿cómo actualizará el valor de la clave "Sinead" a 22?

![image](images/Q79.png?raw=png)

- [x] `marks["Sinead"] = 22`
- [ ] `marks["Sinead"].22`
- [ ] `marks["Sinead"] -> 22`
- [ ] `marks["Sinead"].value = 22`

#### P75. ¿Por qué puede std::sort recibir un objeto función como uno de sus parámetros?

- [x] `La función std::sort es una plantilla. El programador es libre de ingresar el algoritmo de ordenamiento en un objeto función como argumento.`
- [ ] `En realidad, std::sort toma solo un argumento, que es el contenedor a ordenar.`
- [ ] `std::sort opera en un contenedor de plantilla. El compilador no sabe cómo comparar relacionalmente los valores que contiene, por lo que se debe proporcionar una función para hacer la comparación.`
- [ ] `std::sort usará la función de parámetro como un manejador de errores. La función será llamada si ocurre un error.`

#### P76. ¿Qué sucederá cuando ejecute este fragmento de código?

```
#include <iostream>

int main() {
float a = 5.51;
int b = static_cast<int>(a);
std::cout << b;
}
```

- [ ] `6 se imprimirá en la salida estándar, sin advertencias de compilación generadas.`
- [x] `5 se imprimirá en la salida estándar, sin advertencias de compilación generadas.`
- [ ] `6 se imprimirá en la salida estándar, con advertencias de compilación generadas.`
- [ ] `5 se imprimirá en la salida estándar, con advertencias de compilación generadas.`

#### P77. ¿Qué especificador de acceso no permite que los miembros de la clase sean accedidos desde fuera de la clase, pero permite que sean accedidos por clases derivadas?

- [ ] guarded
- [x] protected
- [ ] public
- [ ] private

#### P78. La generación de ejecutables predeterminada en UNIX para un programa C++ es _

- [ ] a.exe
- [ ] a
- [x] a.out
- [ ] out.a

#### P79. ¿Cuál será la salida del siguiente programa?

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

#### P80. ¿Qué significa "c" en cout y cin?

- [ ] compiler (compilador)
- [ ] console (consola)
- [x] character (carácter)
- [ ] standard namespace (espacio de nombres estándar)

#### P81. ¿Cuál es el uso de tellp()?

- [ ] Posición del puntero de entrada actual
- [x] Posición del puntero de salida actual
- [ ] Última posición del puntero de entrada
- [ ] Última posición del puntero de salida

#### P82. ¿Qué es una función callback?

- [ ] Puntero a un puntero
- [x] Puntero a una función
- [ ] función para un puntero
- [ ] función para una clase

#### P83. ¿Cuál es la sintaxis correcta para imprimir "Hello World" en C++?

- [x] `cout << "Hello World";`
- [ ] `System.out.println("Hello World");`
- [ ] `print("Hello World");`
- [ ] `Console.WriteLine("Hello World");`

#### P84. ¿Cuántas categorías de iteradores hay en C++?

- [ ] 4
- [ ] 3
- [ ] 7
- [x] 5

#### P85. ¿Cuál es el significado de clase base en C++?

- [ ] Hereda otra clase
- [ ] Tiene una variable puntero
- [ ] Es la primera clase declarada
- [x] Otra clase heredó de esta clase

#### P86. El tamaño de los objetos C++ se expresa en términos de múltiplos del tamaño de un ** y el tamaño de un char es **.

- [ ] char, 4
- [ ] float, 8
- [ ] int, 1
- [x] char, 1

#### P87. Los aspectos dependientes de la implementación sobre una implementación se pueden encontrar en

- [ ] `<numeric>`
- [ ] `<limit>`
- [x] `<limits>`
- [ ] `<implementation>`

#### P88. ¿Qué es un constructor predeterminado?

- [x] un constructor que se puede usar sin argumentos
- [ ] un constructor que no tiene un valor de retorno
- [ ] un constructor que es usado por múltiples clases
- [ ] un constructor que inicializa todos los miembros de una clase

#### P89. Al proteger un archivo de encabezado, ¿por qué usaría '#pragma once' en lugar de 'include' guard?

- [ ] No hay razón para elegir porque sirven propósitos diferentes
- [x] Un include guard usa una macro para lograr una sola inclusión, pero el compilador no puede evitar que el programador defina esa macro en otro lugar, lo que resultaría en ninguna inclusión en absoluto
- [ ] '#pragma once' garantiza que el código del encabezado nunca se cambiará porque está aplicado por el compilador
- [ ] Los include guards se refieren al archivo de encabezado en el sistema de archivos, no al código, por lo que no son útiles si el archivo de encabezado existe más de una vez en un proyecto. Esto no es un problema con '#pragma once'

#### P90. ¿Cuál de las siguientes declaraciones es válida?

- [ ] Podemos crear un nuevo operador de C++.
- [ ] Podemos cambiar la precedencia del operador de C++.
- [x] No podemos cambiar las plantillas de operadores.
- [ ] Podemos cambiar la asociatividad de los operadores de C++.

#### P91. ¿Cuál de las siguientes se agrega/n automáticamente a cada clase, si no escribimos la nuestra?

- [ ] Constructor de copia
- [ ] Operador de asignación
- [ ] Un constructor sin ningún parámetro
- [x] Todas las anteriores

#### P92. La declaración if-else puede ser reemplazada por ¿qué operador?

- [ ] estructura cierta
- [ ] estructura de elección
- [x] estructura selectiva
- [ ] Ninguna de las anteriores

#### P93. ¿Cuál opción sería una solución recursiva al problema del factorial n!?

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

#### P94. Se puede llamar al destructor de una clase cuando ocurren diversas situaciones. ¿Cuál opción NO es una de esas situaciones?

- [ ] El programa se termina. Esto llama al destructor de objetos de duración estática.
- [ ] Se llama a la función delete() para un puntero de objeto asignado con el operador new.
- [x] El recolector de basura detecta que un objeto ya no se va a usar.
- [ ] Un objeto de duración de almacenamiento automático sale del alcance.

#### P95. Está diseñando un sistema de pagos de cambio de divisas en C++. Necesita modelar una transacción de una moneda que tiene un entero como su cantidad y un float como su precio. Luego desea declarar un objeto real de este tipo. ¿Cómo logrará esto?

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

#### P96. ¿Qué sucederá si intenta llamar a esta función con checkConcatThreshold("a");?

```cpp
int checkConcatThreshold(string a, string b) {
    return (a + b).length () > 120;
}
```

- [ ] Ocurrirá una advertencia de compilación y al segundo argumento se le dará un valor predeterminado de b.
- [ ] Ocurrirá una advertencia de compilación y al segundo argumento se le dará un valor predeterminado de la cadena vacía.
- [x] Ocurrirá un error de compilación.
- [ ] No ocurrirán errores de compilación y no ocurrirán advertencias de compilación.

#### P97. Necesita definir una función lambda de C++. Desea que la función tenga acceso solo a las variables que son locales a ella. La función debe recibir un solo parámetro, y un nombre, y construir un saludo simple. ¿Cómo logrará esto?

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

[Referencia](https://docs.microsoft.com/en-us/cpp/cpp/lambda-expressions-in-cpp?view=msvc-160)

#### P98. ¿Cuál es el valor de X después de ejecutar este código?

```cpp
int x=10, a=-3;
X+=a;
```

- [ ] -3
- [x] 7
- [ ] 13
- [ ] 3

**Explicación:** `+=` significa aumentar el valor. Por lo tanto `x += a` es equivalente a `x = x + a`

#### P99. Una vez que haya terminado de escribir en un archivo, ¿qué método llamará en el `ofstream` para notificar al sistema operativo?

- [ ] printout()
- [x] close()
- [ ] destroy()
- [ ] flush()

#### P100. ¿Cuál opción NO es una palabra clave de C++?

- [ ] static_assert
- [ ] reinterpret_cast
- [x] comPl
- [ ] alignas

#### P101. La función size_in_bits parece tomar cualquier tipo de parámetro. Esto se puede hacer sobrecargando la función, o dejando que el compilador se encargue de ello escribiendo una plantilla. ¿Cuál opción es una implementación de esa plantilla?

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

#### P102. Para usar el teclado como entrada se incluye la biblioteca iostream. Para leer entrada de archivos como entrada, ¿qué biblioteca se necesita?

- [x] fstream
- [ ] cstdlib
- [ ] filestream
- [ ] iostream

#### P103. ¿Qué imprimirá este programa orientado a objetos?

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

#### P104. El programa a continuación está manejando un contenedor de pila. ¿Cuál es la salida de ejecutar el programa?

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

Aquí se supone que implementamos una estructura de datos de pila que sigue el principio **FILO** o (First IN Last Out - Primero en Entrar Último en Salir),
_stack.push()_ -> empuja un elemento al final del arreglo.
_stack.pop()_ -> elimina un elemento del final del arreglo.
_stack.top()_ -> Solo nos da el elemento superior del arreglo.
Ahora siguiendo las secuencias de push y pop: **[1,2,3]** luego se usa la función pop,
El arreglo recién formado es: **[1,2,4]** luego se usa top para recuperar el elemento superior '4' y luego se usa nuevamente la función pop que elimina 4.
así, el arreglo resultante es: 1,2.
Luego imprime el elemento superior (ie: 2).

#### P105. ¿Cuál opción es una forma válida de sobrecargar el operador condicional ternario?

- [ ] `void& operator ?:(const bool cond, const void& iftrue, const void& iffalse);`
- [x] `El operador ternario no es sobrecargable.`
- [ ] `void& operator conditional(const bool cond, const void& iftrue, const void& iffalse);`
- [ ] `void* operator ?:(const bool cond, const void* iftrue, const void* iffalse);`

[Referencia](https://en.cppreference.com/w/cpp/language/operators)

#### P106. ¿Qué jerarquía de clases representa un ejemplo de herencia multinivel?

- [ ] En el mismo programa, en diferentes puntos, una clase dada deriva individualmente de más de una clase diferente.
- [ ] Una primera clase deriva directamente, al mismo tiempo, de una segunda y tercera clase.
- [x] En el mismo programa, en diferentes puntos, una clase dada deriva individualmente de más de dos clases diferentes.
- [ ] Una primera clase deriva de una segunda clase, y esa segunda clase ya está derivada de una tercera clase

#### P107. ¿Cuál de las siguientes es la sintaxis correcta para imprimir el mensaje en lenguaje C++?

- [ ] Out <<"Hello world!
- [ ] Cout << Hello world! ;
- [x] cout <<"Hello world!";
- [ ] Ninguna de las anteriores

[Referencia](https://en.cppreference.com/w/cpp/io/cout)

#### P108. Considere el siguiente programa. ¿Cuál será la salida/error?

```cpp
#include<iostream>
#include<algorithm>
#include<string.h>
using namespace std;
bool compare(char c1, char c2){
return tolower(c1) > tolower(c2);    //LÍNEA-1
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

[Referencia](https://www.geeksforgeeks.org/tolower-function-in-cpp/)

#### P109. Considere el siguiente segmento de código. Complete el espacio en blanco en LÍNEA-1 para que el programa imprima "not found"?

```cpp
#include <iostream>
#include <algorithm>
using namespace std;
int main() {
int data[] = {1,2,3,4,5};
int key = 5;
if(binary_search(__________))    //LÍNEA-1
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

[Referencia](https://www.geeksforgeeks.org/binary-search-algorithms-the-c-standard-template-library-stl/)

#### P110. Considere el siguiente segmento de código. ¿Cuál será la salida?

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

[Referencia](https://cplusplus.com/reference/algorithm/sort/)

#### P111. Considere el siguiente segmento de código. ¿Cuál será la salida?

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

[Referencia](https://en.cppreference.com/w/cpp/algorithm/rotate)

#### P112. Considere el siguiente segmento de código. ¿Cuál será la salida?

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

[Referencia](https://en.cppreference.com/w/cpp/container/vector)

#### P113. Considere el siguiente segmento de código. Elija la opción apropiada para completar el espacio en blanco en LÍNEA-1, de modo que la salida del código sea: a C++ Program.

```cpp
#include <iostream>
#include <string>
using namespace std;
int main(void) {
string s1 = "C++ ";
string s2 = "Program";
__________________;    //LÍNEA-1
cout << s1;
return 0;
}
```

- [x] s1 += s2
- [ ] strcat(s1, s2)
- [x] s1.append(s2)
- [ ] s1.insert(s2)

[Referencia](https://www.geeksforgeeks.org/stdstringappend-in-c/)

#### P114. Considere el siguiente segmento de código. Complete el espacio en blanco en LÍNEA-1 de modo que la salida sea 5 2 3 4 5

```cpp
#include <iostream>
#include <algorithm>
using namespace std;
int main() {
int data[] = { 1, 2, 3, 4, 5 };
for (int i = 0; i < 1; i++) {
int j = data[i];
replace(data, data + 5, j, *(_________________));    //LÍNEA-1
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

[Referencia](https://www.geeksforgeeks.org/stdstringreplace-stdstringreplace_if-c/)

#### P115. Considere el siguiente segmento de código. ¿Cuál será la salida?

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

[Referencia](https://en.cppreference.com/w/cpp/container/stack)

#### P116. Considere el siguiente segmento de código. ¿Qué declaración/declaraciones es/son correcta(s)?

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

[Referencia](https://www.geeksforgeeks.org/const-keyword-in-cpp/)

#### P117. Considere el siguiente programa. ¿Cuál será la salida/error(es)?

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
- [x] Error de compilación: falta argumento predeterminado para "char add(char, char, char)"
- [x] Error de compilación: llamada de sobrecarga "add(char, char)" es ambigua

[Referencia](https://learn.microsoft.com/en-us/cpp/cpp/function-overloading?view=msvc-170)

#### P118. Considere el siguiente segmento de código. ¿Cuál será la salida?

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

[Referencia](https://www.geeksforgeeks.org/output-of-the-program-use-macros-carefully/)

#### P119. Considere el siguiente segmento de código. ¿Qué línea/s le darán un error?

```cpp
#include<iostream>
#define X 1
using namespace std;
int main(){
int i;
const int i1 = 2;
const int i2 = i1; //LÍNEA-1
i2 = X;
i = i1;
i1 = i;
return 0;
//LÍNEA-2
//LÍNEA-3
//LÍNEA-4
}
```

- [ ] LÍNEA-1
- [x] LÍNEA-2
- [ ] LÍNEA-3
- [x] LÍNEA-4

#### P120. Considere el siguiente segmento de código. ¿Cuál será la salida/error?

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
- [x] Error de compilación: inicialización no válida de referencia no constante

#Explicación detallada:
El error está ocurriendo porque está tratando de crear una referencia a un valor temporal. En la línea int &b = a+1; estamos intentando crear una referencia b al resultado de la expresión a + 1, que es un valor temporal. Las referencias deben estar vinculadas a un objeto real, no a un valor temporal o una expresión que no tenga una ubicación de memoria.

#### P121. Considere el siguiente segmento de código. ¿Cuál será la salida?

```cpp
#include <iostream>
using namespace std;
int& func(int& i) {     //LÍNEA-1
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

[Referencia](https://www.ibm.com/docs/en/zos/2.4.0?topic=calls-pass-by-reference-c-only)

#### P122. Considere el siguiente segmento de código. Elija la opción apropiada para completar los espacios en blanco en LÍNEA-1, de modo que la salida del código sea: 300 20000.

```cpp
#include <iostream>
using namespace std;
void compute(int n1, int n2, ________, ________){ //LÍNEA-1
n3 = n1 + n2;
*n4 = n1 * n2;
}
int main(){
int a = 100, b = 200, c = 0, d = 0;
compute(a, b, c, &d); //LÍNEA-2
cout << c << ", ";
cout << d;
return 0;
}
```

- [ ] int n3, int\* n4
- [x] int& n3, int \*n4
- [ ] int* n3, int* n4
- [ ] int& n3, int& n4

#### P123. Considere el siguiente segmento de código. ¿Cuál será la salida/error?

```cpp
#include <iostream>
using namespace std;
int main() {
int a = 2, *b;
*b = 5;
int * const ptr;    // LÍNEA-1
// LÍNEA-2
ptr = b;
cout << *ptr;
return 0;
}
```

- [ ] `<valor basura>`
- [ ] 5
- [x] Error de compilación en LÍNEA-1: 'ptr' const no inicializado
- [x] Error de compilación en LÍNEA-2: asignación de variable de solo lectura 'ptr'

#### P124. Considere el siguiente segmento de código. ¿Cuál será la salida/error?

```cpp
#include <iostream>
using namespace std;
void fun(int a = 5) { cout << a << endl; }
//LÍNEA-1
int fun(int x = 10) { cout << x << endl; return 0; }    //LÍNEA-2
int main() {
fun();
return 0;
}
```

- [ ] 5
- [ ] 10
- [ ] 5
- [x] Error de compilación en LÍNEA-2: nueva declaración ambigua de 'int fun(int)'

#### P125. Considere el siguiente segmento de código. Complete el espacio en blanco en LÍNEA-1 de modo que el programa imprima 5 + i3

```cpp
#include<iostream>
using namespace std;
struct complex{
int re, im;
void show(){ cout << re << " + i" << im; }
};
______________________________________{ //Línea-1
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

[Referencia](https://www.w3schools.com/cpp/cpp_structs.asp)

#### P126. Considere el siguiente programa. ¿Qué línea/s generará(n) un error?

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
a = m.pra; //LÍNEA-1
b = m.pub; //LÍNEA-2
m.set_pr(100); //LÍNEA-3
m.set_pu(200); //LÍNEA-4
return 0;
}
```

- [x] LÍNEA-1
- [ ] LÍNEA-2
- [ ] LÍNEA-3
- [ ] LÍNEA-4

[Referencia](https://stackoverflow.com/questions/4855422/c-classes-public-private-and-protected)

#### P127. Considere la siguiente clase. Complete los espacios en blanco con especificadores de acceso apropiados para que el miembro y pueda ser accedido desde fuera de la clase pero el miembro x no pueda ser accedido.

```cpp
class Test{
________:
int x;
________:
int y;
/* Más código */
};
```

- [ ] public, public
- [ ] public, private
- [ ] private, public
- [x] private, private

#### P128. ¿Qué estándar de C++ agregó inicializadores de miembros predeterminados en clase?

- [ ] C++98
- [x] C++11
- [ ] C++14
- [ ] C++17.

#### P129. ¿Puede usar la deducción de tipo auto para miembros de datos no estáticos?

- [ ] Sí, desde C++11
- [x] No
- [ ] Sí, desde C++20

#### P130. ¿Necesita definir un miembro de datos inline static en un archivo cpp?

- [x] No, la definición ocurre en el mismo lugar donde se declara un miembro inline static.
- [ ] Sí, el compilador necesita la definición en un archivo cpp.
- [ ] Sí, el compilador necesita una definición en todas las unidades de traducción que usen esta variable.

[Referencia](https://en.cppreference.com/w/cpp/language/bit_field)

#### P131. ¿Cuál es la salida del siguiente código:

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

#### P132. ¿Puede una variable inline static ser no constante?

- [x] Sí, es solo una variable regular.
- [ ] No, las variables inline deben ser constantes.

#### P133. Considere el siguiente código:

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

#### P134. ¿Qué sucede cuando lanzas una excepción desde un constructor?

- [ ] El objeto se considera "creado", por lo que seguirá el ciclo de vida regular de un objeto.
- [x] El objeto se considera "parcialmente creado", y por lo tanto, el compilador no llamará a su destructor.
- [ ] El compilador llama a std::terminate ya que no se pueden lanzar excepciones desde constructores.

#### P135. ¿Qué sucede cuando compilas este código?

```cpp
struct Point { int x; int y; };
Point pt {.y = 10, .x = 11 };
std::cout << pt.x << ", " << pt.y;
```

- [x] El código no compila. Los designadores deben estar en el mismo orden que los miembros de datos en la clase Point.
- [ ] El código compila e imprime 11, 10.
- [ ] El código compila e imprime 10, 11.

#### P136. ¿Funcionará este código en C++11?

```cpp
struct User { std::string name = "unknown"; unsigned age { 0 }; };
User u { "John", 101 };
```

- [ ] Sí, el código compila en modo C++11.
- [x] El código compila a partir del modo C++14.
- [ ] El código no compila incluso en C++20.

#### P137. Suponga que tiene un std::map<string, int> m;. Seleccione la única afirmación verdadera sobre el siguiente bucle:

```cpp
for (const pair<string, int>& elem : m)
```

- [x] A El bucle itera correctamente sobre el mapa, sin crear copias adicionales.

- [ ] B El bucle creará una copia de cada elemento en el mapa ya que el tipo de elem no coincide.

- [ ] C El código no compilará porque un par const no puede vincularse a un mapa.

#### P138. Identifique la extensión correcta del archivo de encabezado definido por el usuario en C++.

- [ ] .cpp
- [ ] .hg
- [x] .h
- [ ] .hf

#### P139. Identifique el tipo de constructor incorrecto.

```cpp
auto x = 4000.22;
```

- [x] Constructor Amigo
- [ ] Constructor Predeterminado
- [ ] Constructor Parametrizado
- [ ] Constructor de Copia

#### P140. ¿Cuál de los siguientes tipos de datos es compatible con C++ pero no con C?

- [x] bool
- [ ] int
- [ ] double
- [ ] float

[Referencia]: https://stackoverflow.com/questions/1608318/is-bool-a-native-c-type

#### P141. Identifique la sintaxis correcta para declarar arreglos en C++.

- [x] int arr[10]
- [ ] array arr[10]
- [ ] array{10}
- [ ] int arr

[Referencia]: (https://en.cppreference.com/w/cpp/language/array)

#### P142. El tamaño de wchat_t es.

- [ ] 2
- [ ] 4
- [ ] 2 o 4
- [x] Depende del número de bits en el sistema

#### P143. ¿Cuál de los siguientes bucles es mejor cuando conocemos el número de iteraciones?

- [ ] while
- [x] for
- [ ] do
- [ ] Todos los anteriores

#### P144. ¿Qué palabra clave se usa para definir las macros en C++?

- [ ] #macro
- [x] #define
- [ ] macro
- [ ] keyword

#### P145. ¿Cuál de los siguientes operadores debería preferirse para sobrecargarse como una función global en lugar de un método miembro?

- [ ] Postfijo ++
- [x] Operador de Comparación
- [ ] Operador de Inserción <<
- [ ] Prefijo++

#### P146. ¿Cómo podemos restringir la asignación dinámica de objetos de una clase usando new?

- [ ] Sobrecargando el operador new
- [ ] Haciendo un operador new privado vacío.
- [x] Haciendo operadores new y new[] privados vacíos
- [ ] Sobrecargando operadores new y operadores new[]

#### P147. ¿Cuál es la complejidad temporal del código a continuación?

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

[Referencia](<https://medium.com/enjoy-algorithm/analysis-of-loop-in-programming-cc9a644ef8cd#:~:text=At%20each%20step%20of%20the%20iteration%2C%20the%20nested%20loop%20is,%20%3D%20O(n%C2%B2)>)

#### P148. ¿Cuál es la salida del código dado a continuación?

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

Tanto **++a** como **a++** aumentan el valor de a en 1 (es decir: 11) y por lo tanto k+m se convierte en 22.

#### P149. ¿Qué construcción de C++ se usa para el manejo de excepciones?

- [x] try-catch
- [ ] if-else
- [ ] for loop
- [ ] switch-case

#### P150. ¿Cuál es el propósito de la declaración `break` en un bucle en C++?

- [ ] Salir del programa
- [ ] Saltar la iteración actual y continuar con la siguiente
- [x] Terminar el bucle
- [ ] Devolver un valor

[Referencia]: (https://www.tutorialspoint.com/cprogramming/c_break_statement.htm)

#### P151. En C++, ¿cuál es el propósito de la palabra clave `const` cuando se usa con una variable?

- [x] Hace que la variable sea inmutable
- [ ] Cambia el tipo de datos
- [ ] Define una función constante
- [ ] Hace que la variable sea un puntero

#### P152. ¿Cuál es más efectivo al llamar a las funciones de C++?

- [x] Llamada por referencia
- [ ] Llamada por valor
- [ ] Llamada por puntero
- [ ] Llamada por objeto

[Referencia]: (https://www.algbly.com/More/MCQs/Cpp-mcq/Cpp-functions.html)

#### P153. ¿Cuál será la salida del siguiente programa de C++?

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

- [ ] Fallo de segmentación
- [x] "Constructor called" cinco veces y luego "Destructor called" cinco veces
- [ ] "Constructor called" cinco veces y luego "Destructor called" una vez
- [ ] Error

#### P154. ¿Cuál opción NO está relacionada con declarar la variable miembro count como static en my_class?

```cpp
class my_class{
    public: static int count;
}
```

- [ ] Todos los objetos que intentan acceder a su variable miembro count realmente se refieren a la única variable count vinculada a la clase static.
- [ ] La variable existe incluso cuando no se han definido objetos de la clase, por lo que puede ser modificada en cualquier punto del código fuente.
- [x] La variable no puede ser modificada por ninguna parte del código en la misma aplicación o hilo. Sin embargo, otros hilos pueden modificarla.
- [ ] La variable se asigna solo una vez, independientemente de cuántos objetos se instancien, porque está vinculada a la clase misma, no a sus instancias.

#### P155. ¿Cuál es el propósito de la palabra clave `constexpr` en C++?

- [ ] Se usa para definir constantes en C++.
- [ ] `constexpr` se usa para especificar que una variable es un puntero constante.
- [x] `constexpr` se usa para indicar que una expresión puede ser evaluada en tiempo de compilación, haciéndola adecuada para su uso en expresiones constantes.
- [ ] Es una palabra clave usada para crear funciones asíncronas.

[Ref](https://learn.microsoft.com/en-us/cpp/cpp/constexpr-cpp?view=msvc-170#:~:text=constexpr%20indica%20que%20el%20valor,argumentos%20de%20plantilla%20y%20declaraciones%20de%20arreglos.)

#### P156. ¿Qué es un metaprograma de plantilla en C++?

- Ref(https://www.geeksforgeeks.org/template-metaprogramming-in-c/)

- [ ] Un metaprograma de plantilla es un lenguaje de programación de alto nivel.
- [ ] Se refiere a la metaprogramación que usa plantillas en C++.
- [ ] Es un tipo de patrón de diseño de interfaz de usuario.
- [x] Un metaprograma de plantilla es una computación en tiempo de compilación, donde las plantillas y la especialización de plantillas se usan para realizar cálculos en tiempo de compilación.

#### P157. Identifique el ejemplo correcto para un operador de pre-incremento.

- [x] ++i
- [ ] i++
- [ ] --i
- [ ] +i

#### P158. ¿Cuál será la salida del siguiente código?

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

- [ ] Transpuesta de matriz
- [x] Misma matriz
- [ ] Imagen especular de la matriz
- [ ] Matriz invertida

#### P159. ¿Qué es una condición de carrera en C++?

- [ ] Una condición donde el programa se ejecuta más rápido de lo esperado
- [x] Una condición donde múltiples hilos acceden a datos compartidos concurrentemente, y el resultado depende del momento de su ejecución
- [ ] Una condición donde dos hilos compiten por tiempo de CPU
- [ ] Una condición donde un bucle se ejecuta demasiado rápido y necesita ser ralentizado

[Referencia](https://en.cppreference.com/w/cpp/language/memory_model)

#### P160. Considere el siguiente código que tiene una condición de carrera. ¿Cuál es la forma correcta de arreglarlo?

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
- [x] Usar `std::mutex` para bloquear/desbloquear alrededor de `counter++` en la sección crítica
- [ ] Usar `std::this_thread::sleep_for()` para retrasar cada incremento
- [ ] Cambiar `counter++` a `++counter` para operación atómica

[Referencia](https://en.cppreference.com/w/cpp/thread/mutex)