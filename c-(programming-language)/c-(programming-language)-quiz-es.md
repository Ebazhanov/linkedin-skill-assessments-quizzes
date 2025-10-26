## C (Lenguaje de Programación)

#### Q1. ¿Qué ejemplo de código eventualmente provocará que la computadora se quede sin memoria?

- [x] :

```c
while(1)
{
    char *smallString = (char *) malloc(10);
}
```

- [ ] :

```c
long long number = 1;
    while(1)
    number *= 2;
```

- [ ] :

```c
while(1)
{
    char hugeString[1000000L];
    memset(hugeString, 0, 1000000L);
}
```

- [ ] :

```c
while(1)
{
    long *bigArray = (long *) malloc(sizeof(long) * 1000);
    memset(bigArray, 1000000, 1000);

    (bigArray);
}
```

#### Q2. ¿Cuál será el resultado del código siguiente?

```c
int f1 (int a, int b)
{
    if (a > b)
    {
        printf("A is greater than B\n");
        return 1;
    }
    else
    {
        printf("B is greater than A");
        return 0;
    }
}

main()
{
    if (f1(20,10) || f1(10,20))
        printf("C is fun!\n");
}
```

- [x] :

```
A is greater than B
C is fun!
```

- [ ] :

```
A is greater than B
B is greater than A
C is fun!
```

- [ ] :

```
A is greater than B
B is greater than A
```

- [ ] Nothing is printed on Screen

#### Q3. ¿Cómo se llama una función dentro de la misma función?

- [x] recursividad
- [ ] subfunción
- [ ] llamada interna
- [ ] bucle infinito

[Reference](https://www.cprogramming.com/tutorial/c/lesson16.html)

#### Q4. ¿Qué demuestra la declaración de la variable c2?

```c
main(){
    char c1 ='a';
    char c2 = c1+10;
}
```

- [x] aritmética de caracteres
- [ ] asignación indefinida
- [ ] conversión de tipo
- [ ] declaración inválida

[Reference](https://tutorialspoint.dev/language/c/character-arithmetic-c-c)

#### Q5. ¿De qué es un ejemplo esta declaración?

```c
struct s {
    int i;
    struct s *s1;
    struct s *s2;
};
```

- [x] un nodo
- [ ] una linked list
- [ ] una stack
- [ ] un binary tree

#### Q6. Los archivos header se listan usando la directiva de preprocesamiento #include, y pueden tener uno de los siguientes formatos: #include &lt;fileA&gt; o #include "fileB". ¿Cuál es la diferencia entre estos dos formatos?

- [ ] El preprocesador intentará localizar fileA en el mismo directorio que el archivo fuente, y fileB en una ruta de directorio predeterminada.
- [ ] El preprocesador intentará localizar fileA en el directorio del sistema fijo. Intentará localizar fileB en la ruta del directorio designada por la opción -I agregada a la línea de comandos al compilar el código fuente.
- [ ] El archivo que usa la sintaxis fileA debe ser archivos del sistema, de número ilimitado; fileB debe ser un archivo de usuario con un máximo de uno por archivo fuente.
- [x] El preprocesador intentará localizar fileA en una ruta de directorio predeterminada. Intentará localizar fileB en el mismo directorio que el archivo fuente junto con una ruta de directorio personalizada.

[Reference](https://www.geeksforgeeks.org/difference-between-include-and-include-in-c-c-with-examples/#:~:text=The%20difference%20between%20the%20two,be%20included%20in%20the%20code.&text=%23include%20is%20for%20pre%2Ddefined%20header%20files.)

#### Q7. Usando un for loop, ¿cómo podrías escribir código en C para contar hacia atrás desde 10 hasta 1 y mostrar cada número en su propia línea?

- [ ] :

```c
for (int i = 0; i>=0, i--){
    printf("%d\n", i);
}//end of loop
```

- [ ] :

```c
int i;
for (i=1; i<=10; i++){
    printf("%d", i);
}
```

- [ ] :

```c
int i = 10;
while (i>0){
    printf("%d\n", i);
    i--;
}
```

- [x] :

```c
int i;
for (i= 10; i>0; i--){
    printf("%d\n", i);
}// end of loop
```

#### Q8. ¿Cuál no es una de las palabras reservadas en C estándar?

- [ ] volatile
- [x] typeof
- [ ] register
- [ ] typedef

[Reference](https://www.ibm.com/docs/en/adfz/developer-for-zos/14.2.0?topic=programs-c-reserved-keywords)

#### Q9. ¿Qué devuelve el programa mostrado a continuación?

```c
int main(){
    int a=1, b=2, c=3, d=4;
    int x = a;
    if (a>b)
    if (b<c) x=b;
    else x=c;
    return(x);
}
```

- [x] 1
- [ ] 3
- [ ] 2
- [ ] 0

#### Q10. Usando la declaración Union a continuación, ¿cuántos bytes de espacio de memoria ocuparán los datos de este tipo?

```c
union Cars {
    char make[20];
    char model[30];
    short year;
} car;
```

- [ ] 32
- [ ] 54
- [x] 30
- [ ] 52

#### Q11. En esta muestra de código, ¿qué no es un problema para el compilador de C?

```c
main(){
    constant int PI = 3.14;
    printf("%f\n", pi);
}
```

- [x] El valor de PI debe establecerse en 3.141593, no 3.14
- [ ] La declaración de PI debe decir const, no constant.
- [ ] El tipo de datos de PI debe ser float, no int.
- [ ] La declaración printf debe usar PI, no pi.

#### Q12. ¿Cuál es el programa más pequeño para compilar y ejecutar sin errores?

- [ ] main()
- [x] int main() {return 0;}
- [ ] main() { }
- [ ] main() { ; }

[Reference](https://www.beningo.com/150-the-wolrds-shortest-c-program/)

#### Q13. ¿Qué es opcional en una declaración de función?

- [ ] tipo de datos de los parámetros
- [ ] tipo de retorno de la función
- [x] nombres de los parámetros
- [ ] número de parámetros

> **Explicación:**  
> En todos los estándares modernos de C, los nombres de los parámetros en una declaración de función son opcionales.  
> Sin embargo, el significado de una lista de parámetros vacía (`int f();`) difiere según el estándar:
>
> - **Antes de C23:** Declara una función con un número no especificado de parámetros (no es un prototipo).
> - **En C23:** Equivalente a `int f(void);` — declara una función que no toma parámetros.
>
> [Reference](https://en.cppreference.com/w/c/language/function_declaration)

#### Q14. C trata todos los dispositivos, como la pantalla y el teclado, como archivos. ¿Qué archivo se abre automáticamente cuando se ejecuta un programa?

- [x] stdout
- [ ] stdio.h
- [ ] default.h
- [ ] string.h

#### Q15. ¿En qué segmento ocurre la asignación dinámica de memoria?

- [ ] BSS Segment
- [ ] stack
- [x] heap
- [ ] data segment

[Reference](http://www.it.uc3m.es/pbasanta/asng/course_notes/dynamic_memory_heap_en.html#:~:text=The%20dynamic%20memory%20that%20is,reads%20a%20set%20of%20words.)

#### Q16. ¿Qué función usas para desasignar memoria?

- [ ] dalloc()
- [ ] dealloc()
- [ ] release()
- [x] free()

[Reference](https://devdocs.io/c/memory/free)

[Reference](https://www.tutorialspoint.com/c_standard_library/c_function_free.htm)

#### Q17. En el lenguaje C, ¿cuáles son los bloques de construcción básicos que se construyen juntos para escribir un programa?

- [ ] keywords
- [ ] identificadores
- [x] tokens
- [ ] funciones

[Reference](https://fresh2refresh.com/c-programming/c-tokens-identifiers-keywords/#:~:text=C%20tokens%20are%20the%20basic,are%20known%20as%20C%20tokens.)

#### Q18. ¿Cuándo se asigna memoria para una variable?

- [ ] durante la asignación de la variable
- [ ] durante la inicialización de la variable
- [x] durante la declaración de la variable
- [ ] durante la definición de la variable

[Reference](https://www.codingame.com/playgrounds/14589/how-to-play-with-pointers-in-c/dynamic-memory-allocation#:~:text=When%20a%20variable%20is%20declared,allocation%20or%20dynamic%20memory%20allocation.)

#### Q19. C usa el método call by value para pasar argumentos a las funciones. ¿Cómo puedes invocar el método call by reference?

- [x] usando pointers
- [ ] declarando funciones separadamente de definirlas
- [ ] usando funciones recursivas
- [ ] usando variables globales

[Reference](https://www.javatpoint.com/call-by-value-and-call-by-reference-in-c)

#### Q20. Un union te permite almacenar diferentes `___` en el mismo `___`.

- [ ] Objetos; Structure
- [ ] Variables; Declaración
- [x] Tipos de datos; Espacio de memoria
- [ ] Arrays; Archivo header

#### Q21. ¿Cuál es la salida de este programa?

```c
main() {
    char c1='a' , c2='A';
    int i=c2-c1;
    printf("%d", i);
}
```

- [ ] 32
- [ ] Error en tiempo de ejecución
- [x] -32
- [ ] 0

#### Q22. ¿Cuál es la diferencia entre las funciones scanf() y sscanf()?

- [ ] La función scanf() lee datos formateados como una cadena; La función sscanf() lee entrada de cadena de la pantalla.
- [x] La función scanf() lee datos formateados del teclado; La función sscanf() lee entrada formateada de una cadena.
- [ ] La función scanf() lee datos de cadena del teclado; La función sscanf() lee datos de cadena de una cadena.
- [ ] La función scanf() lee datos formateados de un archivo; La función sscanf() lee entrada de una cadena seleccionada

#### Q23. ¿Cuál no es un comando válido con esta declaración?

```c
char *string[20] = { "one", "two", "three"};
```

- [ ] `printf("%c", string[1][2]);`
- [x] `printf("%s", string[1][2]);`
- [ ] `printf("%s", string[1]);`
- [ ] `printf(string[1]);`

#### Q24. ¿A qué es equivalente la expresión player->name?

- [ ] `player.name`
- [x] `(*player).name`
- [ ] `*player.name`
- [ ] `player.*name`

#### Q25. ¿Qué programa compilará y ejecutará sin errores?

- [ ] :

```c
main() {
    for(i=0; i<10; i++) ;
}
```

- [x] :

```c
main() {
int i=0;
    for(; i<10; i++) ;
}
```

- [ ] :

```c
main() {
    int i;
    for(i=0; i<j; i++) ;
}
```

- [ ] :

```c
main() {
int i;
    for (i= 10; i<10; i++)
}
```

#### Q26. ¿Qué devuelve esta llamada de función?

```c
1 main() { float x = f1(10, 5); }
2 float f1(int a, int b) { return (a/b); }
```

- [ ] 2
- [ ] 2.000000
- [ ] un error en tiempo de ejecución
- [x] un error del compilador

#### Q27. ¿Qué crea este programa?

```c
#include <stdio.h>
int main() {
    int *p = NULL;
    return 0;
}
```

- [ ] un error en tiempo de ejecución
- [x] un NULL pointer
- [ ] un error de compilación
- [ ] un void pointer

#### Q28. ¿Cuál es una forma alternativa de escribir la expresión (\*x).y?

- [ ] No hay equivalente.
- [x] x->y
- [ ] \*x->y
- [ ] y->x

#### Q29. Los errores en tiempo de compilación son errores estáticos que se pueden encontrar en el código.

- [x] en declaraciones y definiciones
- [ ] en funciones y expresiones
- [ ] en sintaxis y semántica
- [ ] en objetos y declaraciones

#### Q30. La entrada y salida de archivos (I/O) en C está fuertemente basada en la forma en que se hace `___`?

- [x] in Unix
- [ ] in C++
- [ ] in C#
- [ ] in DOS

#### Q31. ¿Qué devuelve la función strcmp(str1, str2)?

- [x] 0 si str1 y str2 son iguales, un número negativo si str1 es menor que str2, un número positivo si str1 es mayor que str2
- [ ] true (1) si str1 y str2 son iguales, false (0) si str1 y str2 no son iguales
- [ ] true (1) si str1 y str2 son iguales, NULL si str1 y str2 no son iguales
- [ ] 0 si str1 y str2 son iguales, un número negativo si str2 es menor que str1, un número positivo si str2 es mayor que str1

#### Q32. ¿Cuál es la salida de este programa?

```c
int a=10, b=20;
int f1(a) { return(a*b); }
main() {
printf("%d", f1(5));
}
```

- [x] 100
- [ ] 200
- [ ] 5
- [ ] 50

#### Q33. ¿Cuál _no_ es una forma correcta de declarar una variable string?

- [ ] `char *string = "Hello World";`
- [x] `char string = "Hello World";`
- [ ] `char string[20] = {'H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd'};`
- [ ] `char string[] = "Hello World";`

#### Q34. ¿Cuál opción es un include guard para el archivo header mylib.h?

- [ ] :

```c
#ifdef MYLIB_H
#undef MYLIB_H

// mylib.h content

#endif /* MYLIB_H */
```

- [x] :

```c
#ifndef MYLIB_H
#define MYLIB_H

// mylib.h content

#endif /* MYLIB_H */
```

- [ ] :

```c
#define MYLIB_H
#include "mylib.h"

#undef MYLIB_H
```

- [ ] :

```c
#ifdef MYLIB_H
#define MYLIB_H

// mylib.h content

#endif /* MYLIB_H */
```

#### Q35. ¿Cuántas veces se ejecuta el código dentro del while loop en este programa?

```c
main(){
 int x=1;
 while(x++<100){
    x*=x;
    if(x<10) continue;
    if(x>50) break;
 }
}
```

- [ ] 100
- [x] 3
- [ ] 5
- [ ] 50

#### Q36. ¿A través de qué se hace la entrada y salida de archivos (I/O) en C?

- [ ] componentes controlados por sintaxis
- [ ] interfaces nativas
- [ ] objetos del sistema
- [x] llamadas de función

#### Q37. ¿Las directivas son traducidas por el?

- [x] Pre-procesador
- [ ] Compilador
- [ ] Enlazador
- [ ] Editor

#### Q38. Las estructuras de loop principales en la programación en C son el for loop, el while loop, ¿y cuál otro loop?

- [x] do...while
- [ ] for...in
- [ ] repeat...until
- [ ] do...until

#### Q39. Por defecto, ¿las funciones en C son qué tipo de funciones?

- [ ] global
- [x] static
- [ ] library
- [ ] system

#### Q40. Has escrito una función que quieres incluir como miembro de la estructura 'a'. ¿Cómo se define tal miembro de estructura?

- [ ] :

```c
struct a {
    void *f1;
};
```

- [x] :

```c
struct a {
    void (*f1)();
};
```

- [ ] :

```c
struct a {
    *(void *f1)();
};
```

- [ ] :

```c
struct a {
    void *f1();
};
```

#### Q41. Una estructura de datos Stack permite todas las operaciones de datos en un extremo solamente, haciéndola qué tipo de implementación?

- [ ] FIFO
- [x] LIFO
- [ ] LILO
- [ ] LOLI

#### Q42. ¿Qué muestra este programa?

```c
main(){
    char *p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    int i;
    for (i=0;i<5;i++) *p++; *p++;
    printf("%c",*p++);
}
```

#### Q43. Describe la relación entre lvalue y rvalue.

- [ ] Un lvalue puede aparecer solo en el lado izquierdo de una asignación; un rvalue puede aparecer solo en el lado derecho.
- [ ] Un lvalue puede aparecer solo en el lado izquierdo de una asignación; un rvalue puede aparecer en el lado izquierdo o derecho.
- [ ] Un lvalue y un rvalue pueden aparecer en el lado izquierdo o derecho de una asignación.
- [x] Un lvalue puede aparecer en el lado izquierdo o derecho de una asignación; un rvalue puede aparecer solo en el lado derecho.

#### Q44. ¿Qué operador se usa para acceder a la dirección de una variable?

- [ ] `%`
- [ ] `**`
- [ ] `*`
- [x] `&`

#### Q45. ¿Qué función add devuelve correctamente el valor actualizado del resultado?

- [x] :

```c
void add (int a, int b, int *result)
{
    *result = a+b;
}

main()
{
    int a = 10;
    int b = 20;
    int result = 0;

    add(a,b,&result);
}
```

- [ ] :

```c
void add (int a, int b, int result)
{
    result = a+b;
}

main()
{
    int a = 10;
    int b = 20;
    int result = 0;

    add(a,b,result);
}
```

- [ ] :

```c
void add (int a, int b, int *result)
{
    result = a+b;
}

main()
{
    int a = 10;
    int b = 20;
    int result = 0;

    add(a,b,result);
}
```

- [ ] :

```c
void add (int *a, int *b, int *result)
{
    result = a+b;
}

main()
{
    int a = 10;
    int b = 20;
    int result = 0;

    add(*a,*b,*result);
}
```

#### Q46. Considera los números de la serie Fibonacci menores a 100: 0,1,1,2,3,5,8,13,21,34,55,89. ¿Qué fragmento de código genera la secuencia?

- [ ] :

```c
void fibonacci(int a, int b)
{
    int c = a+b;

    if(a>100)
       return;

    printf("%d", a);

    fibonacci(a,b);
}

int main()
{
    fibonacci(0,1);
}
```

- [ ] :

```c
void fibonacci(int a, int b)
{
    int c = a+b;

    if(a>100)
       return;

    printf("%d", b);

    fibonacci(a,c);
}

int main()
{
    fibonacci(0,1);
}
```

- [x] :

```c
void fibonacci(int a, int b)
{
    int c = a+b;

    if(a>100)
       return;

    printf("%d", a);

    fibonacci(b,c);
}

int main()
{
    fibonacci(0,1);
}
```

- [ ] :

```c
void fibonacci(int a, int b)
{
    int c = a+b;

    if(a>100)
       return;

    printf("%d", c);

    fibonacci(b,c);
}

int main()
{
    fibonacci(0,1);
}
```

#### Q47. ¿Cuál _no_ es un especificador de storage class?

- [x] `intern`
- [ ] `extern`
- [ ] `register`
- [ ] `static`

[Reference](https://en.cppreference.com/w/cpp/language/storage_duration)

#### Q48. ¿Qué línea de código, después de la ejecución, resulta en que `i` tenga el valor de 1?

- [ ] `for(i=1; i<=1; i++);`
- [ ] `for(i=1; i=10; i++);`
- [x] `for(i=1; i==10; i++);`
- [ ] `for(i=10; i>=1; i--);`

#### Q49. ¿Cuál es el valor de la variable c al final de este programa?

```
1 main() {
2   int a, b, c;
3   a=10; b=50;
4   c=a * b % a;
5 }
```

- [ ] 50
- [ ] 5
- [x] 0
- [ ] 500

#### Q50. ¿Cuál _no_ es uno de los tipos de datos básicos en C?

- [ ] long double
- [ ] unsigned char
- [x] array
- [ ] float

#### Q51. ¿Cuál es el operador de acceso a miembros para una estructura?

- [ ] ,
- [ ] []
- [x] .
- [ ] :

#### Q52. ¿Qué tipo de datos estándar proporciona el tamaño de almacenamiento más pequeño y se puede usar en cálculos?

- [x] char
- [ ] float
- [ ] int
- [ ] short

#### Q53. ¿Qué hace la función ctype tolower()?

- [ ] It returns TRUE for lowercase letters of the alphabet.
- [ ] It ensures that text output uses only ASCII values (0 through 127).
- [ ] It returns FALSE for lowercase letters of the alphabet.
- [x] It converts an uppercase letter of the alphabet to lowercase.

#### Q54. El void pointer _vptr_ se asigna a la dirección de la variable float _g_. ¿Cuál es una forma válida de desreferenciar _vptr_ para asignar su valor apuntado a una variable float llamada _f_ más adelante en el programa?

```c
float g;
void *vptr=&g;
```

- [ ] `f=(float *)vptr;`
- [x] `f=*(float *)vptr;`
- [ ] `f=*(float)vptr;`
- [ ] `f=(float)*vptr;`

#### Q55. ¿Las funciones de asignación dinámica de memoria están definidas en qué archivo header del sistema?

- [ ] stdio.h
- [x] stdlib.h
- [ ] limits.h
- [ ] stddef.h

#### Q56. Una función es un conjunto de **\_**.

- [ ] declaraciones
- [x] sentencias
- [ ] variables
- [ ] objetos

#### Q57. ¿Cómo son diferentes las funciones static de las funciones globales?

- [ ] Las funciones static deben declararse antes de ser definidas.
- [ ] Las funciones static deben declararse en un archivo header separado.
- [ ] Las funciones static siempre devuelven el mismo valor.
- [x] Las funciones static solo pueden ser accedidas en el archivo donde se declaran.

#### Q58. ¿Qué ejemplo de código crea la cadena "Hello Mars" en el buffer de almacenamiento `hello`?

- [ ] :

```c
    char hello[25];
    strcpy(hello, "Hello ");
    strcpy(hello, "Mars");
```

- [x] :

```c
    char hello[25];
    char *p;
    strcpy(hello, "Hello World");
    p = hello;
    p +=6;
    strcpy(p, "Mars");
```

- [ ] :

```c
    char *hello;
    strcpy(hello, "Hello World");
    hello+=6;
    strcpy(hello, "Mars");
```

- [ ] :

```c
    char hello[25];
    strcpy(hello, "Hello World");
    strcpy(*hello[6], "Mars");
```

#### Q59. Si usas la función fopen() con el modo "a", ¿qué sucede si el archivo nombrado no existe?

- [ ] El archivo se crea y se abre para lectura.
- [x] El archivo se crea y se abre para escritura.
- [ ] La función fopen() devuelve NULL indicando que la operación ha fallado.
- [ ] El archivo se crea y se abre tanto para escritura como para lectura

[Reference](https://www.tutorialspoint.com/c_standard_library/c_function_fopen.htm)

#### Q60. ¿Qué devuelve esta función?

```c
int fl(int a, int b) { return(a>b?a:b); }
```

- [ ] error del compilador
- [ ] el valor menor de los dos parámetros pasados
- [ ] error en tiempo de ejecución
- [x] el valor mayor de los dos parámetros pasados

#### Q61. ¿Cuál opción es un nombre de función válido?

- [x] draw_star()
- [ ] 5times()
- [ ] upper-limit()
- [ ] auto()

#### Q62. ¿Cuál no es una definición de tipo válida de una estructura que contiene coordenadas x e y como enteros, y que puede usarse como se muestra para la variable llamada point?

```c
coord point;
point.x = 9;
point.y = 3;
```

- [ ] :

```c
struct coord{
    int x;
    int y;
};
typedef struct coord coord;
```

- [x] :

```c
typedef struct coord{
    int x;
    int y;
};
```

- [ ] :

```c
typedef struct coord{
    int x;
    int y;
} coord;
```

- [ ] :

```c
typedef struct{
    int x;
    int y;
} coord;
```

#### Q63. ¿Cuál es la salida del programa siguiente?

```c
#include <stdio.h>
#if X == 3
    #define Y 3
#else
    #define Y 5
#endif

int main()
{
    printf("%d", Y);
    return 0;
}
```

- [ ] 3
- [x] 5
- [ ] 3 o 5 dependiendo de la entrada
- [ ] Error en tiempo de compilación

#### Q64. ¿Qué asignan las funciones malloc() y calloc()?

- [ ] memoria reasignada
- [ ] memoria estática
- [x] memoria dinámica
- [ ] memoria fragmentada

[Calloc](https://devdocs.io/c/memory/calloc)
[Malloc](https://devdocs.io/c/memory/malloc)

#### Q65. Necesitas determinar si una variable string es una subcadena de otra cadena. ¿Qué función de la biblioteca estándar de C usas?

- [ ] substr(str1, str2);
- [x] strstr(str1, str2);
- [ ] substring(str1, str2);
- [ ] strspn(str1, str2);

[Reference](https://devdocs.io/c/string/byte/strstr)

#### Q66. Encuentra la salida del programa.

```c
#include <stdio.h>

#define L 10
int main(){
    int a =10;
    switch (a,a<<2){
        case L:printf("a==L");     break;
        case L*2 : printf("a = L* 2\n");     break;
        case L*4 : printf("a = L* 4\n");    break;
        default: printf("Error\n");
    }
}
```

- [ ] `a=L*2`
- [ ] `a=L`
- [ ] `Error`
- [x] `a=L*4`

[Reference](https://www.geeksforgeeks.org/left-shift-right-shift-operators-c-cpp/)

#### Q67. Predice la salida del siguiente código cuando las variables **enteras** x se inicializa a 10, y a 2, y z a 0.

```c
z = x + y * x + 10 / 2 * x;
printf("value is =%d",z);
```

- [x] 80
- [ ] 170
- [ ] 31.5
- [ ] 6

[Reference](https://www.informit.com/articles/article.aspx?p=2062174&seqNum=4)

#### Q68. ¿Cuál será la salida del siguiente fragmento de código?

```c
#include <stdio.h>
void solve() {
    int x = 2;
    printf("%d", (x << 1) + (x >> 1));
}
int main() {
    solve();
	return 0;
}
```

- [x] 5
- [ ] 4
- [ ] 2
- [ ] 1

#### Q69. ¿Cuál es la salida de este programa?

```c
int a=20, b=10;
int f1(a) {
    return(a*b);
}
main() {
    printf("%d", f1(5));
}
```

- [ ] 100
- [ ] 200
- [ ] 5
- [x] 50

#### Q70. ¿Qué es el carácter \0?

- [ ] Cadena
- [x] Carácter NULL
- [ ] CERO
- [ ] Variable

[Reference](<https://www.youth4work.com/Talent/C-Language/Forum/117150-what-is-the-use-of-a-0-character-in-c-language#:~:text=by%20using%20of%20null%20character(%27%5C0%27)%20it%20terminates%20the%20string%20untill%20the%20null%20character%20hit...%20which%20means%20comes%20out%20of%20the%20loop...%20In%20strings%20by%20default%20takes%20the%20null%20charater>)

#### Q71. ¿Cuál es la salida correcta para el siguiente código?

```c
#include&lt;stdio.h&gt;
#include&lt;conio.h&gt;
main()
{
     int a=10, b=20;
     clrscr();
     printf("Before swapping a=%d b=%d",a,b);
     a=a+b;
     b=a-b;
     a=a-b;
     printf("nAfter swapping a=%d b=%d",a,b);
     getch();
}
```

- [ ] Before a=10 b=20 , After a=10 b=10
- [ ] Before a=10 b=10 , After a=20 b=10
- [ ] Before a=10 b=20 , After a=20 b=20
- [x] Before a=10 b=20 , After a=20 b=10

#### Q72. ¿Cuál es la opción incorrecta que explica la directiva #pragma?

- [ ] #pragma exit nos permite especificar funciones llamadas al salir del programa.
- [ ] Esta es una directiva del preprocesador que se puede usar para activar o desactivar ciertas características.
- [x] #pragma startup no nos permite especificar funciones llamadas al iniciar el programa.
- [ ] Es de dos tipos #pragma startup, #pragma exit y pragma warn.

#### Q73. ¿Cuál será la salida del siguiente fragmento de código?

```c
#include <stdio.h>
union School {
    int age, rollNo;
    double marks;
};
void solve() {
    union School sc;
    sc.age = 19;
    sc.rollNo = 82;
    sc.marks = 19.04;
    printf("%d", (int)sizeof(sc));
}
int main() {
    solve();
	return 0;
}
```

- [ ] 2
- [ ] 4
- [x] 8
- [ ] 10

#### Q74. ¿Cuál será la salida del siguiente fragmento de código?

```c
#include <stdio.h>
struct School {
    int age, rollNo;
};
void solve() {
    struct School sc;
    sc.age = 19;
    sc.rollNo = 82;
    printf("%d %d", sc.age, sc.rollNo);
}
int main() {
    solve();
	return 0;
}
```

- [x] 19 82
- [ ] Error de compilación
- [ ] 82 19
- [ ] Ninguna de estas

#### Q75. ¿Cuál es la salida del siguiente fragmento de código?

```c
int main() {
	int sum = 2 + 4 / 2 + 6 * 2;
	printf("%d", sum);
	return 0;
}
```

- [ ] 2
- [ ] 15
- [x] 16
- [ ] 18

#### Q76. ¿Qué significa la siguiente declaración?

```
int (*ptr)[10];
```

- [ ] ptr es un array de pointers a 10 enteros
- [x] ptr es un pointer a un array de 10 enteros
- [ ] ptr es un array de 10 enteros
- [ ] ptr es un pointer a un array

#### Q77. ¿Cuál será la salida del siguiente fragmento de código?

```c
#include <stdio.h>
void change(int,int);
int main()
{
   int a=10,b=20;
   change(a,b); //calling a function by passing the values of variables.
   printf("Value of a is: %d",a);
   printf("\n");
   printf("Value of b is: %d",b);
   return 0;
}
void change(int x,int y)
{
   x=13;
   y=17;
}
```

- [x] 10,20
- [ ] 10,10
- [ ] 20,20
- [ ] 20,10

**Explicación:** La función "change" cambiará el valor de x e y solo dentro de su propio alcance, por lo que a y b no se ven afectados.

#### Q78. Elige verdadero o falso. Cuando se crea una variable en C, se asigna una dirección de memoria a la variable.

- [x] Verdadero
- [ ] Falso

#### Q79. ¿Qué imprime el siguiente fragmento de programa en C?

```c
#include <stdio.h>

int main()
{
    char c[] = "GATE2011";

    char *p = c;

    printf("%s", p + p[3] -p[1]);

    return 0;
}
```

- [ ] GATE 2011
- [ ] E2011
- [x] 2011
- [ ] 01

**Explicación:** char c[ ] = "GATE2011"; dado que char \*p =c significa que p representa la dirección base de la cadena "GATE2011", entonces p[3] es 'E' y p[1] es 'A'. El valor de la subexpresión p[3] – p[1] = valor ASCII de 'E' – valor ASCII de 'A' = 4. Por lo tanto, la expresión p + p[3] – p[1] se convierte en ( p + 4) y (p+4) representa la dirección base de la cadena "2011" printf("%s", p + p[3] – p[1]); Por lo tanto, imprimirá 2011

#### Q80. ¿Cuál es la salida del siguiente fragmento de código?

```c
int main() {
	int a = 5, b = 6, c;
	c = a++ + ++b;
	printf("%d %d %d", a, b, c);
	return 0;
}
```

- [ ] 5 6 11
- [x] 6 7 12
- [ ] 5 6 12
- [ ] 6 6 12

#### Q81. ¿Cuál será la salida del siguiente segmento de programa en C?

```c
char inchar = 'A';
switch (inchar)
{
case 'A' :
	printf ("choice A \n") ;
case 'B' :
	printf ("choice B ") ;
case 'C' :
case 'D' :
case 'E' :
default:
	printf ("No Choice") ;
}
```

- [ ] No choice
- [ ] Choice A
- [x] Choice A
      Choice B No choice
- [ ] El programa no da salida ya que es erróneo

#### Q82. La variable string str1 tiene el valor de "abc", y la variable string str2 tiene el valor "xyz". ¿Cuáles son los valores de str1 y str2 después de que se ejecute esta declaración?

```c
strcpy(str1, str2);
```

- [x] str1: "xyz" ; str2: "xyz"
- [ ] str1: "abc" ; str2: "xyz"
- [ ] str1: "xyz" ; str2: "abc"
- [ ] str1: "abc" ; str2: "abc"

#### Q83. ¿Cuál no es uno de los tipos de datos básicos en C?

- [x] array
- [ ] float
- [ ] long double
- [ ] unsigned char

#### Q84. Has escrito una función que quieres incluir como miembro de la estructura a. ¿Cómo se define tal miembro de estructura?

- [ ] :

```c
struct a {
    void *f1;
};
```

- [x] :

```c
struct a {
    void (*f1)();
};
```

- [ ] :

```c
struct a {
    *(void *f1)();
};
```

- [ ] :

```c
struct a {
    void *f1();
};
```

#### Q85. Necesitas determinar si una variable string es una subcadena de otra cadena. ¿Qué función de la biblioteca estándar de C usas?

- [ ] substr(str1, str2);
- [x] strstr(str1, str2);
- [ ] substring(str1, str2);
- [ ] strspn(str1, str2);

#### Q86. ¿Cómo son diferentes las funciones static de las funciones globales?

- [ ] Las funciones static deben declararse antes de ser definidas.
- [ ] Las funciones static deben declararse en un archivo header separado.
- [ ] Las funciones static siempre devuelven el mismo valor.
- [x] Las funciones static solo pueden ser accedidas en el archivo donde se declaran.

#### Q87. ¿Qué muestra este programa?

```c
main(){
    char *p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    int i;
    for (i=0;i<5;i++) *p++; *p++;
    printf("%c",*p++);
}
```

- [ ] K
- [ ] M
- [ ] H
- [x] G

#### Q88. ¿Cuál no es un comando válido con esta declaración?

```c
char *string[20] = { "one", "two", "three"};
```

- [ ] `printf("%c", string[1][2]);`
- [x] `printf("%s", string[1][2]);`
- [ ] `printf("%s", string[1]);`
- [ ] `printf(string[1]);`
