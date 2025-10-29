## C (Linguaggio di Programmazione)

#### Q1. Quale esempio di codice causerà eventualmente l'esaurimento della memoria del computer?

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

#### Q2. Quale sarà l'output del codice seguente?

```c
int f1 (int a, int b)
{
    if (a > b)
    {
        printf("A è maggiore di B\n");
        return 1;
    }
    else
    {
        printf("B è maggiore di A");
        return 0;
    }
}

main()
{
    if (f1(20,10) || f1(10,20))
        printf("C è divertente!\n");
}
```

- [x] :

```
A è maggiore di B
C è divertente!
```

- [ ] :

```
A è maggiore di B
B è maggiore di A
C è divertente!
```

- [ ] :

```
A è maggiore di B
B è maggiore di A
```

- [ ] Nulla viene stampato sullo schermo

#### Q3. Come si chiama la chiamata di una funzione all'interno della stessa funzione?

- [x] ricorsione
- [ ] sottofunzione
- [ ] chiamata interna
- [ ] ciclo infinito

[Riferimento](https://www.cprogramming.com/tutorial/c/lesson16.html)

#### Q4. Cosa dimostra la dichiarazione della variabile c2?

```c
main(){
    char c1 ='a';
    char c2 = c1+10;
}
```

- [x] aritmetica dei caratteri
- [ ] assegnazione non definita
- [ ] conversione di tipo
- [ ] dichiarazione non valida

[Riferimento](https://tutorialspoint.dev/language/c/character-arithmetic-c-c)

#### Q5. Di cosa è un esempio questa dichiarazione?

```c
struct s {
    int i;
    struct s *s1;
    struct s *s2;
};
```

- [x] un nodo
- [ ] una lista collegata
- [ ] uno stack
- [ ] un albero binario

#### Q6. I file di intestazione sono elencati utilizzando la direttiva di preelaborazione #include e possono avere uno dei seguenti formati: #include &lt;fileA&gt; o #include "fileB". Qual è la differenza tra questi due formati?

- [ ] Il preprocessore cercherà di localizzare fileA nella stessa directory del file sorgente e fileB in un percorso di directory predeterminato.
- [ ] Il preprocessore cercherà di localizzare fileA nella directory di sistema fissa. Cercherà di localizzare fileB nel percorso di directory designato dall'opzione -I aggiunta alla riga di comando durante la compilazione del codice sorgente.
- [ ] Il file che utilizza la sintassi fileA deve essere un file di sistema, in numero illimitato; fileB deve essere un file utente con un massimo di uno per file sorgente.
- [x] Il preprocessore cercherà di localizzare fileA in un percorso di directory predeterminato. Cercherà di localizzare fileB nella stessa directory del file sorgente insieme a un percorso di directory personalizzato.

[Riferimento](https://www.geeksforgeeks.org/difference-between-include-and-include-in-c-c-with-examples/#:~:text=The%20difference%20between%20the%20two,be%20included%20in%20the%20code.&text=%23include%20is%20for%20pre%2Ddefined%20header%20files.)

#### Q7. Utilizzando un ciclo for, come potresti scrivere un codice C per contare da 10 a 1 e visualizzare ogni numero sulla propria riga?

- [ ] :

```c
for (int i = 0; i>=0, i--){
    printf("%d\n", i);
}//fine del ciclo
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
}// fine del ciclo
```

#### Q8. Quale non è una delle parole riservate in C standard?

- [ ] volatile
- [x] typeof
- [ ] register
- [ ] typedef

[Riferimento](https://www.ibm.com/docs/en/adfz/developer-for-zos/14.2.0?topic=programs-c-reserved-keywords)

#### Q9. Cosa restituisce il programma mostrato di seguito?

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

#### Q10. Utilizzando la dichiarazione Union di seguito, quanti byte di spazio di memoria occuperanno i dati di questo tipo?

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

#### Q11. In questo esempio di codice, cosa non è un problema per il compilatore C?

```c
main(){
    constant int PI = 3.14;
    printf("%f\n", pi);
}
```

- [x] Il valore di PI deve essere impostato su 3.141593, non 3.14
- [ ] La dichiarazione di PI deve dire const, non constant.
- [ ] Il tipo di dato di PI deve essere float, non int.
- [ ] L'istruzione printf deve usare PI, non pi.

#### Q12. Qual è il programma più piccolo da compilare ed eseguire senza errori?

- [ ] main()
- [x] int main() {return 0;}
- [ ] main() { }
- [ ] main() { ; }

[Riferimento](https://www.beningo.com/150-the-wolrds-shortest-c-program/)

#### Q13. Cosa è facoltativo in una dichiarazione di funzione?

- [ ] tipo di dato dei parametri
- [ ] tipo di ritorno della funzione
- [x] nomi dei parametri
- [ ] numero di parametri

> **Spiegazione:**  
> In tutti gli standard C moderni, i nomi dei parametri in una dichiarazione di funzione sono facoltativi.  
> Tuttavia, il significato di un elenco di parametri vuoto (`int f();`) differisce per standard:
>
> - **Prima di C23:** Dichiara una funzione con un numero non specificato di parametri (non un prototipo).
> - **In C23:** Equivalente a `int f(void);` — dichiara una funzione che non accetta parametri.
>
> [Riferimento](https://en.cppreference.com/w/c/language/function_declaration)

#### Q14. C tratta tutti i dispositivi, come il display e la tastiera, come file. Quale file si apre automaticamente quando un programma viene eseguito?

- [x] stdout
- [ ] stdio.h
- [ ] default.h
- [ ] string.h

#### Q15. In quale segmento avviene l'allocazione dinamica della memoria?

- [ ] Segmento BSS
- [ ] stack
- [x] heap
- [ ] segmento dati

[Riferimento](http://www.it.uc3m.es/pbasanta/asng/course_notes/dynamic_memory_heap_en.html#:~:text=The%20dynamic%20memory%20that%20is,reads%20a%20set%20of%20words.)

#### Q16. Quale funzione utilizzi per deallocare la memoria?

- [ ] dalloc()
- [ ] dealloc()
- [ ] release()
- [x] free()

[Riferimento](https://devdocs.io/c/memory/free)

[Riferimento](https://www.tutorialspoint.com/c_standard_library/c_function_free.htm)

#### Q17. Nel linguaggio C quali sono i blocchi di base che vengono costruiti insieme per scrivere un programma?

- [ ] parole chiave
- [ ] identificatori
- [x] token
- [ ] funzioni

[Riferimento](https://fresh2refresh.com/c-programming/c-tokens-identifiers-keywords/#:~:text=C%20tokens%20are%20the%20basic,are%20known%20as%20C%20tokens.)

#### Q18. Quando viene allocata la memoria per una variabile?

- [ ] durante l'assegnazione della variabile
- [ ] durante l'inizializzazione della variabile
- [x] durante la dichiarazione della variabile
- [ ] durante la definizione della variabile

[Riferimento](https://www.codingame.com/playgrounds/14589/how-to-play-with-pointers-in-c/dynamic-memory-allocation#:~:text=When%20a%20variable%20is%20declared,allocation%20or%20dynamic%20memory%20allocation.)

#### Q19. C utilizza il metodo di chiamata per valore per passare argomenti alle funzioni. Come puoi invocare il metodo di chiamata per riferimento?

- [x] utilizzando i puntatori
- [ ] dichiarando le funzioni separatamente dalla loro definizione
- [ ] utilizzando funzioni ricorsive
- [ ] utilizzando variabili globali

[Riferimento](https://www.javatpoint.com/call-by-value-and-call-by-reference-in-c)

#### Q20. Un'unione ti permette di memorizzare diversi `___` nello stesso `___`.

- [ ] Oggetti; Struttura
- [ ] Variabili; Dichiarazione
- [x] Tipi di dati; Spazio di memoria
- [ ] Array; File di intestazione

#### Q21. Qual è l'output di questo programma?

```c
main() {
    char c1='a' , c2='A';
    int i=c2-c1;
    printf("%d", i);
}
```

- [ ] 32
- [ ] Errore di runtime
- [x] -32
- [ ] 0

#### Q22. Qual è la differenza tra le funzioni scanf() e sscanf()?

- [ ] La funzione scanf() legge dati formattati come stringa; La funzione sscanf() legge input di stringa dallo schermo.
- [x] La funzione scanf() legge dati formattati dalla tastiera; La funzione sscanf() legge input formattato da una stringa.
- [ ] La funzione scanf() legge dati di stringa dalla tastiera; La funzione sscanf() legge dati di stringa da una stringa.
- [ ] La funzione scanf() legge dati formattati da un file; La funzione sscanf() legge input da una stringa selezionata

#### Q23. Quale non è un comando valido con questa dichiarazione?

```c
char *string[20] = { "one", "two", "three"};
```

- [ ] `printf("%c", string[1][2]);`
- [x] `printf("%s", string[1][2]);`
- [ ] `printf("%s", string[1]);`
- [ ] `printf(string[1]);`

#### Q24. A cosa è equivalente l'espressione player->name?

- [ ] `player.name`
- [x] `(*player).name`
- [ ] `*player.name`
- [ ] `player.*name`

#### Q25. Quale programma compilerà ed eseguirà senza errori?

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

#### Q26. Cosa restituisce questa chiamata di funzione?

```c
1 main() { float x = f1(10, 5); }
2 float f1(int a, int b) { return (a/b); }
```

- [ ] 2
- [ ] 2.000000
- [ ] un errore di runtime
- [x] un errore del compilatore

#### Q27. Cosa crea questo programma?

```c
#include <stdio.h>
int main() {
    int *p = NULL;
    return 0;
}
```

- [ ] un errore di runtime
- [x] un puntatore NULL
- [ ] un errore di compilazione
- [ ] un puntatore void

#### Q28. Qual è un modo alternativo per scrivere l'espressione (\*x).y?

- [ ] Non esiste un equivalente.
- [x] x->y
- [ ] \*x->y
- [ ] y->x

#### Q29. Gli errori di compilazione sono errori statici che possono essere trovati nel codice.

- [x] nelle dichiarazioni e definizioni
- [ ] nelle funzioni e espressioni
- [ ] nella sintassi e semantica
- [ ] negli oggetti e istruzioni

#### Q30. L'input e output (I/O) di file in C si basa pesantemente sul modo in cui viene fatto `___`?

- [x] in Unix
- [ ] in C++
- [ ] in C#
- [ ] in DOS

#### Q31. Cosa restituisce la funzione strcmp(str1, str2);?

- [x] 0 se str1 e str2 sono uguali, un numero negativo se str1 è minore di str2, un numero positivo se str1 è maggiore di str2
- [ ] true (1) se str1 e str2 sono uguali, false (0) se str1 e str2 non sono uguali
- [ ] true (1) se str1 e str2 sono uguali, NULL se str1 e str2 non sono uguali
- [ ] 0 se str1 e str2 sono uguali, un numero negativo se str2 è minore di str1, un numero positivo se str2 è maggiore di str1

#### Q32. Qual è l'output di questo programma?

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

#### Q33. Quale _non_ è un modo corretto per dichiarare una variabile stringa?

- [ ] `char *string = "Hello World";`
- [x] `char string = "Hello World";`
- [ ] `char string[20] = {'H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd'};`
- [ ] `char string[] = "Hello World";`

#### Q34. Quale scelta è una guardia di inclusione per il file di intestazione mylib.h?

- [ ] :

```c
#ifdef MYLIB_H
#undef MYLIB_H

// contenuto di mylib.h

#endif /* MYLIB_H */
```

- [x] :

```c
#ifndef MYLIB_H
#define MYLIB_H

// contenuto di mylib.h

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

// contenuto di mylib.h

#endif /* MYLIB_H */
```

#### Q35. Quante volte viene eseguito il codice all'interno del ciclo while in questo programma?

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

#### Q36. L'input e output (I/O) di file in C viene effettuato tramite cosa?

- [ ] componenti guidati dalla sintassi
- [ ] interfacce native
- [ ] oggetti di sistema
- [x] chiamate di funzione

#### Q37. Le direttive sono tradotte dal?

- [x] Pre-processore
- [ ] Compilatore
- [ ] Linker
- [ ] Editor

#### Q38. Le principali strutture di ciclo nella programmazione C sono il ciclo for, il ciclo while e quale altro ciclo?

- [x] do...while
- [ ] for...in
- [ ] repeat...until
- [ ] do...until

#### Q39. Per impostazione predefinita, le funzioni C sono di che tipo di funzioni?

- [x] globali
- [ ] statiche
- [ ] di libreria
- [ ] di sistema

#### Q40. Hai scritto una funzione che vuoi includere come membro della struttura 'a'. Come viene definito tale membro di struttura?

- [ ] A

```c
struct a {
    void *f1;
};
```

- [x] B

```c
struct a {
    void (*f1)();
};
```

- [ ] C

```c
struct a {
    *(void *f1)();
};
```

- [ ] D

```c
struct a {
    void *f1();
};
```

#### Q41. Una struttura dati Stack consente tutte le operazioni sui dati in una sola estremità, rendendola che tipo di implementazione?

- [ ] FIFO
- [x] LIFO
- [ ] LILO
- [ ] LOLI

#### Q42. Cosa visualizza questo programma?

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

#### Q43. Descrivi la relazione tra lvalue e rvalue.

- [ ] Un lvalue può apparire solo sul lato sinistro di un'assegnazione; un rvalue può apparire solo sul lato destro.
- [ ] Un lvalue può apparire solo sul lato sinistro di un'assegnazione; un rvalue può apparire sia sul lato sinistro che destro.
- [ ] Un lvalue e un rvalue possono apparire sia sul lato sinistro che destro di un'assegnazione.
- [x] Un lvalue può apparire sul lato sinistro o destro di un'assegnazione; un rvalue può apparire solo sul lato destro.

#### Q44. Quale operatore viene utilizzato per accedere all'indirizzo di una variabile?

- [ ] `%`
- [ ] `**`
- [ ] `*`
- [x] `&`

#### Q45. Quale funzione add restituisce correttamente il valore aggiornato del risultato?

- [x] A

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

- [ ] B

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

- [ ] C

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

- [ ] D

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

#### Q46. Considera i numeri della serie di Fibonacci inferiori a 100: 0,1,1,2,3,5,8,13,21,34,55,89. Quale pezzo di codice produce la sequenza?

- [ ] A

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

- [ ] B

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

- [x] C

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

- [ ] D

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

#### Q47. Quale _non_ è uno specificatore di classe di memorizzazione?

- [x] `intern`
- [ ] `extern`
- [ ] `register`
- [ ] `static`

[Riferimento](https://en.cppreference.com/w/cpp/language/storage_duration)

#### Q48. Quale riga di codice, dopo l'esecuzione, risulta in `i` con il valore di 1?

- [ ] `for(i=1; i<=1; i++);`
- [ ] `for(i=1; i=10; i++);`
- [x] `for(i=1; i==10; i++);`
- [ ] `for(i=10; i>=1; i--);`

#### Q49. Qual è il valore della variabile c alla fine di questo programma?

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

#### Q50. Quale _non_ è uno dei tipi di dati di base in C?

- [ ] long double
- [ ] unsigned char
- [x] array
- [ ] float

#### Q51. Qual è l'operatore di accesso ai membri per una struttura?

- [ ] ,
- [ ] []
- [x] .
- [ ] :

#### Q52. Quale tipo di dato standard fornisce la dimensione di memorizzazione più piccola e può essere utilizzato nei calcoli?

- [x] char
- [ ] float
- [ ] int
- [ ] short

#### Q53. Cosa fa la funzione ctype tolower()?

- [ ] Restituisce TRUE per le lettere minuscole dell'alfabeto.
- [ ] Assicura che l'output di testo utilizzi solo valori ASCII (da 0 a 127).
- [ ] Restituisce FALSE per le lettere minuscole dell'alfabeto.
- [x] Converte una lettera maiuscola dell'alfabeto in minuscola.

#### Q54. Il puntatore void _vptr_ è assegnato all'indirizzo della variabile float _g_. Qual è un modo valido per dereferenziare _vptr_ per assegnare il suo valore puntato a una variabile float chiamata _f_ più avanti nel programma?

```c
float g;
void *vptr=&g;
```

- [ ] `f=(float *)vptr;`
- [x] `f=*(float *)vptr;`
- [ ] `f=*(float)vptr;`
- [ ] `f=(float)*vptr;`

#### Q55. Le funzioni di allocazione dinamica della memoria sono definite in quale file di intestazione di sistema?

- [ ] stdio.h
- [x] stdlib.h
- [ ] limits.h
- [ ] stddef.h

#### Q56. Una funzione è un insieme di **\_**.

- [ ] dichiarazioni
- [x] istruzioni
- [ ] variabili
- [ ] oggetti

#### Q57. In che modo le funzioni statiche differiscono dalle funzioni globali?

- [ ] Le funzioni statiche devono essere dichiarate prima di essere definite.
- [ ] Le funzioni statiche devono essere dichiarate in un file di intestazione separato.
- [ ] Le funzioni statiche restituiscono sempre lo stesso valore.
- [x] Le funzioni statiche possono essere accessibili solo nel file in cui sono dichiarate.

#### Q58. Quale esempio di codice crea la stringa "Hello Mars" nel buffer di memorizzazione `hello`.

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

#### Q59. Se utilizzi la funzione fopen() con la modalità "a", cosa succede se il file nominato non esiste?

- [ ] Il file viene creato e aperto per la lettura.
- [x] Il file viene creato e aperto per la scrittura.
- [ ] La funzione fopen() restituisce un NULL indicando che l'operazione è fallita.
- [ ] Il file viene creato e aperto sia per la scrittura che per la lettura

[Riferimento](https://www.tutorialspoint.com/c_standard_library/c_function_fopen.htm)

#### Q60. Cosa restituisce questa funzione?

```c
int fl(int a, int b) { return(a>b?a:b); }
```

- [ ] errore del compilatore
- [ ] il valore più piccolo dei due parametri passati
- [ ] errore di runtime
- [x] il valore più grande dei due parametri passati

#### Q61. Quale opzione è un nome di funzione valido?

- [x] draw_star()
- [ ] 5times()
- [ ] upper-limit()
- [ ] auto()

#### Q62. Quale non è una definizione di tipo valida di una struttura che contiene coordinate x e y come interi e che può essere utilizzata come mostrato per la variabile denominata point?

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

#### Q63. Qual è l'output del programma seguente?

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
- [ ] 3 o 5 a seconda dell'input
- [ ] Errore di compilazione

#### Q64. Cosa allocano le funzioni malloc() e calloc()?

- [ ] memoria riallocata
- [ ] memoria statica
- [x] memoria dinamica
- [ ] memoria frammentata

[Calloc](https://devdocs.io/c/memory/calloc)
[Malloc](https://devdocs.io/c/memory/malloc)

#### Q65. Devi determinare se una variabile stringa è una sottostringa di un'altra stringa. Quale funzione della libreria standard C utilizzi?

- [ ] substr(str1, str2);
- [x] strstr(str1, str2);
- [ ] substring(str1, str2);
- [ ] strspn(str1, str2);

[Riferimento](https://devdocs.io/c/string/byte/strstr)

#### Q66. Trova l'output del programma.

```c
#include <stdio.h>

#define L 10
int main(){
    int a =10;
    switch (a,a<<2){
        case L:printf("a==L");     break;
        case L*2 : printf("a = L* 2\n");     break;
        case L*4 : printf("a = L* 4\n");    break;
        default: printf("Errore\n");
    }
}
```

- [ ] `a=L*2`
- [ ] `a=L`
- [ ] `Errore`
- [x] `a=L*4`

[Riferimento](https://www.geeksforgeeks.org/left-shift-right-shift-operators-c-cpp/)

#### Q67. Prevedi l'output del seguente codice quando le variabili **intere** x è inizializzata a 10, y a 2 e z a 0.

```c
z = x + y * x + 10 / 2 * x;
printf("il valore è =%d",z);
```

- [x] 80
- [ ] 170
- [ ] 31.5
- [ ] 6

[Riferimento](https://www.informit.com/articles/article.aspx?p=2062174&seqNum=4)

#### Q68. Qual sarà l'output del seguente frammento di codice?

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

#### Q69. Qual è l'output di questo programma?

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

#### Q70. Cos'è il carattere /0?

- [ ] Stringa
- [x] Carattere NULL
- [ ] ZERO
- [ ] Variabile

[Riferimento](<https://www.youth4work.com/Talent/C-Language/Forum/117150-what-is-the-use-of-a-0-character-in-c-language#:~:text=by%20using%20of%20null%20character(%27%5C0%27)%20it%20terminates%20the%20string%20untill%20the%20null%20character%20hit...%20which%20means%20comes%20out%20of%20the%20loop...%20In%20strings%20by%20default%20takes%20the%20null%20charater>)

#### Q71. Qual è l'output corretto per il seguente codice?

```c
#include&lt;stdio.h&gt;
#include&lt;conio.h&gt;
main()
{
     int a=10, b=20;
     clrscr();
     printf("Prima dello scambio a=%d b=%d",a,b);
     a=a+b;
     b=a-b;
     a=a-b;
     printf("nDopo lo scambio a=%d b=%d",a,b);
     getch();
}
```

- [ ] Prima a=10 b=20 , Dopo a=10 b=10
- [ ] Prima a=10 b=10 , Dopo a=20 b=10
- [ ] Prima a=10 b=20 , Dopo a=20 b=20
- [x] Prima a=10 b=20 , Dopo a=20 b=10

#### Q72. Quale è l'opzione errata che spiega la direttiva # pragma?

- [ ] #pragma exit ci permette di specificare le funzioni chiamate all'uscita del programma.
- [ ] Questa è una direttiva del preprocessore che può essere utilizzata per attivare o disattivare determinate funzionalità.
- [x] #pragma startup non ci permette di specificare le funzioni chiamate all'avvio del programma.
- [ ] È di due tipi #pragma startup, #pragma exit e pragma warn.

#### Q73. Qual sarà l'output del seguente frammento di codice?

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

#### Q74. Qual sarà l'output del seguente frammento di codice?

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
- [ ] Errore di compilazione
- [ ] 82 19
- [ ] Nessuna di queste

#### Q75. Qual è l'output del seguente frammento di codice?

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

#### Q76. Cosa significa la seguente dichiarazione?

```
int (*ptr)[10];
```

- [ ] ptr è un array di puntatori a 10 interi
- [x] ptr è un puntatore a un array di 10 interi
- [ ] ptr è un array di 10 interi
- [ ] ptr è un puntatore a un array

#### Q77. Qual sarà l'output del seguente frammento di codice?

```c
#include <stdio.h>
void change(int,int);
int main()
{
   int a=10,b=20;
   change(a,b); //chiamata di una funzione passando i valori delle variabili.
   printf("Valore di a è: %d",a);
   printf("\n");
   printf("Valore di b è: %d",b);
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

**Spiegazione:** La funzione "change" cambierà il valore di x e y solo all'interno del proprio ambito, quindi a e b non sono influenzati.

#### Q78. Scegli vero o falso. Quando viene creata una variabile in C, viene assegnato un indirizzo di memoria alla variabile.

- [x] Vero
- [ ] Falso

#### Q79. Cosa stampa il seguente frammento di programma C?

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

**Spiegazione:** char c[ ] = "GATE2011"; poiché char \*p =c significa che p rappresenta l'indirizzo base della stringa "GATE2011" QUINDI p[3] è 'E' e p[1] è 'A'. Valore della sottoespressione p[3] – p[1] = valore ASCII di 'E' – valore ASCII di 'A' = 4. Quindi l'espressione p + p[3] – p[1] diventa ( p + 4) E (p+4) rappresenta l'indirizzo base della stringa "2011" printf("%s", p + p[3] – p[1]) ; Quindi stamperà 2011

#### Q80. Qual è l'output del seguente frammento di codice?

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

#### Q81. Qual sarà l'output del seguente segmento di programma C?

```c
char inchar = 'A';
switch (inchar)
{
case 'A' :
	printf ("scelta A \n") ;
case 'B' :
	printf ("scelta B ") ;
case 'C' :
case 'D' :
case 'E' :
default:
	printf ("Nessuna scelta") ;
}

```

- [ ] Nessuna scelta
- [ ] Scelta A
- [x] Scelta A
      Scelta B Nessuna scelta
- [ ] Il programma non produce output perché è errato

#### Q82. La variabile stringa str1 ha il valore di "abc" e la variabile stringa str2 ha il valore "xyz". Quali sono i valori di str1 e str2 dopo che questa istruzione è stata eseguita?

```c
strcpy(str1, str2);
```

- [x] str1: "xyz" ; str2: "xyz"
- [ ] str1: "abc" ; str2: "xyz"
- [ ] str1: "xyz" ; str2: "abc"
- [ ] str1: "abc" ; str2: "abc"

#### Q88. Quale non è un comando valido con questa dichiarazione?

```c
char *string[20] = { "one", "two", "three"};
```

- [ ] `printf("%c", string[1][2]);`
- [x] `printf("%s", string[1][2]);`
- [ ] `printf("%s", string[1]);`
- [ ] `printf(string[1]);`

#### Q89. Qual è l'output di questo codice?

```c
int x = 5;
int y = ++x + x++;
printf("%d %d", x, y);
```

- [ ] 6 11
- [x] 7 12
- [ ] 7 11
- [ ] 6 12

**Spiegazione:**
Prima, ++x incrementa x a 6 e usa 6 nell'espressione. Poi x++ usa 6 e incrementa x a 7 dopo. Quindi y = 6 + 6 = 12, e x diventa 7.

[Riferimento](https://en.cppreference.com/w/c/language/operator_precedence)

#### Q90. Cosa indica la parola chiave `volatile` in C?

- [ ] La variabile non può essere modificata
- [x] La variabile può essere modificata da fattori esterni
- [ ] La variabile è memorizzata in ROM
- [ ] La variabile è una costante

**Spiegazione:**
La parola chiave `volatile` dice al compilatore che il valore di una variabile può essere modificato da fattori esterni (hardware, interrupt, altri thread), quindi il compilatore non dovrebbe ottimizzare via le letture/scritture su di essa.

[Riferimento](https://en.cppreference.com/w/c/language/volatile)

#### Q91. Qual è lo scopo della parola chiave `restrict` in C99?

- [x] Per indicare che un puntatore è l'unico modo per accedere a un oggetto
- [ ] Per limitare l'ambito di una variabile
- [ ] Per impedire la modifica di una variabile
- [ ] Per limitare l'accesso alla funzione

**Spiegazione:**
La parola chiave `restrict` è un qualificatore di tipo che può essere applicato ai puntatori. Dice al compilatore che per la durata del puntatore, solo esso o un valore derivato direttamente da esso sarà utilizzato per accedere all'oggetto a cui punta. Ciò consente determinate ottimizzazioni del compilatore.

[Riferimento](https://en.cppreference.com/w/c/language/restrict)

#### Q92. Qual è la differenza tra `malloc()` e `calloc()`?

- [ ] malloc è più veloce di calloc
- [x] calloc inizializza la memoria allocata a zero, malloc no
- [ ] malloc può allocare più memoria di calloc
- [ ] Non c'è differenza

**Spiegazione:**
`calloc()` alloca memoria e inizializza tutti i byte a zero, mentre `malloc()` alloca memoria ma la lascia non inizializzata. `calloc()` accetta anche due argomenti (numero di elementi e dimensione di ciascun elemento) mentre `malloc()` ne accetta uno (dimensione totale in byte).

[Riferimento](https://en.cppreference.com/w/c/memory/calloc)

#### Q93. Cos'è un puntatore pendente?

- [ ] Un puntatore che punta a NULL
- [x] Un puntatore che punta a memoria liberata o eliminata
- [ ] Un puntatore che non è stato inizializzato
- [ ] Un puntatore che punta a una costante

**Spiegazione:**
Un puntatore pendente è un puntatore che punta a memoria che è stata liberata o eliminata. L'accesso a tale puntatore porta a un comportamento indefinito.

[Riferimento](https://en.wikipedia.org/wiki/Dangling_pointer)

#### Q94. Qual è l'output di questo codice?

```c
int arr[] = {1, 2, 3, 4, 5};
printf("%d", *(arr + 3));
```

- [ ] 1
- [ ] 2
- [ ] 3
- [x] 4

**Spiegazione:**
`arr` è un puntatore al primo elemento. `arr + 3` punta al 4° elemento (indice 3). L'operatore `*` lo dereferenzia per ottenere il valore 4.

[Riferimento](https://en.cppreference.com/w/c/language/operator_member_access)

#### Q95. Cosa fa la parola chiave `static` quando applicata a una funzione?

- [x] Limita l'ambito della funzione al file corrente
- [ ] Rende la funzione più veloce
- [ ] Impedisce la chiamata della funzione
- [ ] Rende la funzione inline

**Spiegazione:**
Quando `static` è applicato a una funzione, limita il collegamento della funzione a collegamento interno, il che significa che può essere chiamata solo dall'interno della stessa unità di traduzione (file sorgente).

[Riferimento](https://en.cppreference.com/w/c/language/storage_duration)

#### Q96. Qual è la dimensione di un puntatore in un sistema a 64 bit?

- [ ] 4 byte
- [x] 8 byte
- [ ] 16 byte
- [ ] Dipende da cosa punta

**Spiegazione:**
Su un sistema a 64 bit, i puntatori sono tipicamente 8 byte (64 bit) indipendentemente da cosa puntano. La dimensione è determinata dall'architettura del sistema, non dal tipo puntato.

[Riferimento](https://en.cppreference.com/w/c/language/pointer)

#### Q97. Qual è lo scopo di `typedef`?

- [ ] Per definire un nuovo tipo di dato
- [x] Per creare un alias per un tipo di dato esistente
- [ ] Per dichiarare una variabile
- [ ] Per definire una macro

**Spiegazione:**
`typedef` crea un alias (nome alternativo) per un tipo di dato esistente. Non crea un nuovo tipo, solo un nuovo nome per uno esistente.

[Riferimento](https://en.cppreference.com/w/c/language/typedef)

#### Q98. Cos'è una perdita di memoria?

- [ ] Quando un puntatore punta a memoria non valida
- [x] Quando la memoria allocata non viene liberata
- [ ] Quando una variabile esce dall'ambito
- [ ] Quando si verifica uno stack overflow

**Spiegazione:**
Una perdita di memoria si verifica quando la memoria allocata dinamicamente (tramite `malloc`, `calloc`, ecc.) non viene liberata utilizzando `free()`, causando al programma di consumare sempre più memoria nel tempo.

[Riferimento](https://en.wikipedia.org/wiki/Memory_leak)

#### Q99. Qual è l'output di questo codice?

```c
int x = 10;
int *p = &x;
*p = 20;
printf("%d", x);
```

- [ ] 10
- [x] 20
- [ ] Indirizzo di x
- [ ] Indefinito

**Spiegazione:**
`p` punta a `x`. `*p = 20` modifica il valore all'indirizzo a cui p punta, che è `x`. Quindi `x` diventa 20.

[Riferimento](https://en.cppreference.com/w/c/language/pointer)

#### Q100. Cosa restituisce sempre `sizeof(char)` in C?

- [x] 1
- [ ] 2
- [ ] 4
- [ ] Dipende dal sistema

**Spiegazione:**
Per definizione nello standard C, `sizeof(char)` è sempre 1. Questa è l'unità fondamentale di dimensione in C, e tutte le altre dimensioni sono multipli di essa.

[Riferimento](https://en.cppreference.com/w/c/language/sizeof)

#### Q101. Qual è la differenza tra `++i` e `i++`?

- [x] ++i incrementa prima dell'uso, i++ incrementa dopo l'uso
- [ ] ++i è più veloce di i++
- [ ] i++ può essere usato solo nei cicli
- [ ] Non c'è differenza

**Spiegazione:**
`++i` (pre-incremento) incrementa la variabile e restituisce il nuovo valore. `i++` (post-incremento) restituisce il valore corrente e poi incrementa la variabile.

[Riferimento](https://en.cppreference.com/w/c/language/operator_incdec)

#### Q102. Cos'è un segmentation fault?

- [ ] Un errore di sintassi
- [x] Un errore causato dall'accesso a memoria non valida
- [ ] Un errore di compilazione
- [ ] Un avviso

**Spiegazione:**
Un segmentation fault (segfault) si verifica quando un programma cerca di accedere a memoria a cui non è autorizzato ad accedere, come dereferenziare un puntatore NULL o accedere a memoria liberata.

[Riferimento](https://en.wikipedia.org/wiki/Segmentation_fault)

#### Q103. Qual è lo scopo della parola chiave `const` con i puntatori?

```c
const int *p;
```

- [x] Il valore puntato non può essere modificato tramite p
- [ ] Il puntatore p non può essere modificato
- [ ] Sia il puntatore che il valore sono costanti
- [ ] Non ha effetto

**Spiegazione:**
`const int *p` significa che p punta a un intero costante - non puoi modificare il valore tramite p, ma puoi cambiare dove punta p. Per `int * const p`, il puntatore stesso è costante.

[Riferimento](https://en.cppreference.com/w/c/language/const)

#### Q104. Qual è l'output di questo codice?

```c
int arr[5] = {1, 2, 3};
printf("%d", arr[4]);
```

- [x] 0
- [ ] 3
- [ ] Valore spazzatura
- [ ] Errore di compilazione

**Spiegazione:**
Quando un array è parzialmente inizializzato, gli elementi rimanenti sono automaticamente inizializzati a 0. Quindi arr[3] e arr[4] sono entrambi 0.

[Riferimento](https://en.cppreference.com/w/c/language/array_initialization)

#### Q105. Cosa fa la parola chiave `extern`?

- [ ] Rende una variabile esterna al programma
- [x] Dichiara una variabile che è definita altrove
- [ ] Esporta una variabile ad altri programmi
- [ ] Crea una variabile globale

**Spiegazione:**
`extern` dichiara una variabile o funzione che è definita in un altro file sorgente o più avanti nello stesso file. Dice al compilatore che la definizione esiste altrove.

[Riferimento](https://en.cppreference.com/w/c/language/extern)

#### Q106. Qual è la differenza tra `struct` e `union`?

- [x] i membri struct hanno memoria separata, i membri union condividono la memoria
- [ ] struct è più veloce di union
- [ ] union può avere più membri di struct
- [ ] Non c'è differenza

**Spiegazione:**
In una `struct`, ogni membro ha la propria posizione di memoria. In un'`union`, tutti i membri condividono la stessa posizione di memoria e solo un membro può contenere un valore alla volta. La dimensione di un'unione è la dimensione del suo membro più grande.

[Riferimento](https://en.cppreference.com/w/c/language/union)

#### Q107. Qual è l'output di questo codice?

```c
int x = 5;
printf("%d", x << 2);
```

- [ ] 5
- [ ] 7
- [x] 20
- [ ] 10

**Spiegazione:**
L'operatore `<<` è uno spostamento bit a sinistra. `x << 2` sposta i bit di x a sinistra di 2 posizioni, che è equivalente a moltiplicare per 2^2 = 4. Quindi 5 \* 4 = 20.

[Riferimento](https://en.cppreference.com/w/c/language/operator_arithmetic)

#### Q108. Cos'è un puntatore a funzione?

- [ ] Un puntatore al valore di ritorno di una funzione
- [x] Un puntatore che memorizza l'indirizzo di una funzione
- [ ] Una funzione che restituisce un puntatore
- [ ] Un puntatore all'interno di una funzione

**Spiegazione:**
Un puntatore a funzione è una variabile che memorizza l'indirizzo di una funzione. Può essere utilizzato per chiamare la funzione indirettamente o passare funzioni come argomenti ad altre funzioni.

[Riferimento](https://en.cppreference.com/w/c/language/pointer#Pointers_to_functions)

#### Q109. Cosa rappresenta `NULL` in C?

- [ ] Il numero zero
- [x] Una costante puntatore null
- [ ] Una stringa vuota
- [ ] Un valore indefinito

**Spiegazione:**
`NULL` è una macro che rappresenta una costante puntatore null. È tipicamente definito come `((void*)0)` o semplicemente `0`. Indica che un puntatore non punta a nessuna posizione di memoria valida.

[Riferimento](https://en.cppreference.com/w/c/types/NULL)

#### Q110. Qual è l'output di questo codice?

```c
int x = 10, y = 20;
int *p1 = &x, *p2 = &y;
*p1 = *p2;
printf("%d %d", x, y);
```

- [ ] 10 20
- [x] 20 20
- [ ] 10 10
- [ ] 20 10

**Spiegazione:**
`*p1 = *p2` copia il valore puntato da p2 (che è 20) nella posizione puntata da p1 (che è x). Quindi x diventa 20, y rimane 20.

[Riferimento](https://en.cppreference.com/w/c/language/pointer)

#### Q111. Qual è lo scopo della direttiva `#pragma`?

- [ ] Per includere file di intestazione
- [ ] Per definire macro
- [x] Per fornire istruzioni specifiche del compilatore
- [ ] Per dichiarare variabili

**Spiegazione:**
`#pragma` è una direttiva del preprocessore che fornisce informazioni aggiuntive al compilatore. È definito dall'implementazione e utilizzato per funzionalità specifiche del compilatore.

[Riferimento](https://en.cppreference.com/w/c/preprocessor/impl)

#### Q112. Qual è la differenza tra `break` e `continue`?

- [x] break esce dal ciclo, continue salta alla prossima iterazione
- [ ] break è più veloce di continue
- [ ] continue esce dal ciclo, break salta l'iterazione
- [ ] Non c'è differenza

**Spiegazione:**
`break` termina completamente il ciclo e continua l'esecuzione dopo il ciclo. `continue` salta il resto dell'iterazione corrente e passa alla prossima iterazione del ciclo.

[Riferimento](https://en.cppreference.com/w/c/language/break)

#### Q113. Qual è l'output di questo codice?

```c
int arr[] = {1, 2, 3, 4, 5};
printf("%d", sizeof(arr) / sizeof(arr[0]));
```

- [ ] 4
- [x] 5
- [ ] 20
- [ ] 1

**Spiegazione:**
`sizeof(arr)` dà la dimensione totale dell'array in byte. `sizeof(arr[0])` dà la dimensione di un elemento. Dividendoli si ottiene il numero di elementi: 5.

[Riferimento](https://en.cppreference.com/w/c/language/sizeof)

#### Q114. Cos'è un puntatore void?

- [ ] Un puntatore che punta a nulla
- [x] Un puntatore generico che può puntare a qualsiasi tipo di dato
- [ ] Un puntatore a funzioni void
- [ ] Un puntatore non valido

**Spiegazione:**
Un puntatore `void*` è un puntatore generico che può puntare a qualsiasi tipo di dato. Deve essere convertito al tipo appropriato prima di essere dereferenziato.

[Riferimento](https://en.cppreference.com/w/c/language/pointer)

#### Q115. Cosa suggerisce la parola chiave `register` al compilatore?

- [ ] Di rendere una variabile globale
- [x] Di memorizzare una variabile in un registro CPU per un accesso più veloce
- [ ] Di proteggere una variabile dalla modifica
- [ ] Di allocare memoria sull'heap

**Spiegazione:**
La parola chiave `register` suggerisce (ma non garantisce) che il compilatore dovrebbe memorizzare la variabile in un registro CPU per un accesso più veloce. I compilatori moderni spesso ignorano questo suggerimento e prendono le proprie decisioni di ottimizzazione.

[Riferimento](https://en.cppreference.com/w/c/language/storage_duration)

#### Q116. Qual è l'output di questo codice?

```c
int x = 5;
int y = (x > 3) ? 10 : 20;
printf("%d", y);
```

- [x] 10
- [ ] 20
- [ ] 5
- [ ] 3

**Spiegazione:**
Questo è l'operatore ternario. Poiché x > 3 è vero, y viene assegnato 10.

[Riferimento](https://en.cppreference.com/w/c/language/operator_other)

#### Q117. Qual è la differenza tra `malloc()` e `realloc()`?

- [ ] malloc è più veloce di realloc
- [x] realloc ridimensiona la memoria precedentemente allocata
- [ ] malloc inizializza la memoria, realloc no
- [ ] Non c'è differenza

**Spiegazione:**
`malloc()` alloca nuova memoria. `realloc()` cambia la dimensione di un blocco di memoria precedentemente allocato, potenzialmente spostandolo in una nuova posizione se necessario.

[Riferimento](https://en.cppreference.com/w/c/memory/realloc)

#### Q118. Cos'è un'enumerazione in C?

- [ ] Un costrutto di ciclo
- [x] Un tipo definito dall'utente costituito da costanti intere nominate
- [ ] Una funzione che conta gli elementi
- [ ] Un array di costanti

**Spiegazione:**
Un'enumerazione (`enum`) è un tipo definito dall'utente che consiste in un insieme di costanti intere nominate. Rende il codice più leggibile dando nomi significativi ai valori interi.

[Riferimento](https://en.cppreference.com/w/c/language/enum)

#### Q119. Qual è l'output di questo codice?

```c
int x = 10;
int y = x++ + ++x;
printf("%d %d", x, y);
```

- [ ] 11 21
- [x] 12 22
- [ ] 12 21
- [ ] 11 22

**Spiegazione:**
Prima, x++ usa 10 e incrementa x a 11. Poi ++x incrementa x a 12 e usa 12. Quindi y = 10 + 12 = 22, e x è 12.

[Riferimento](https://en.cppreference.com/w/c/language/operator_incdec)

#### Q120. Qual è lo scopo della macro `assert()`?

- [ ] Per assegnare valori alle variabili
- [x] Per verificare le assunzioni e terminare se false
- [ ] Per affermare la dominanza su altre funzioni
- [ ] Per creare asserzioni nella documentazione

**Spiegazione:**
`assert()` è una macro utilizzata per il debug. Verifica se una condizione è vera. Se falsa, stampa un messaggio di errore e termina il programma. È tipicamente disabilitata nelle build di rilascio.

[Riferimento](https://en.cppreference.com/w/c/error/assert)

#### Q121. Qual è la differenza tra `fgets()` e `gets()`?

- [ ] fgets è più veloce di gets
- [x] fgets è più sicura perché limita la dimensione dell'input
- [ ] gets può leggere da qualsiasi file
- [ ] Non c'è differenza

**Spiegazione:**
`gets()` non è sicura perché non controlla la dimensione del buffer, portando a vulnerabilità di buffer overflow. `fgets()` ti permette di specificare il numero massimo di caratteri da leggere, rendendola più sicura. `gets()` è stata rimossa dallo standard C11.

[Riferimento](https://en.cppreference.com/w/c/io/fgets)

#### Q122. Qual è l'output di questo codice?

```c
int x = 5;
int *p = &x;
printf("%p %p", (void*)&x, (void*)p);
```

- [x] Stesso indirizzo stampato due volte
- [ ] Due indirizzi diversi
- [ ] Errore di compilazione
- [ ] 5 5

**Spiegazione:**
`&x` dà l'indirizzo di x, e p memorizza l'indirizzo di x. Entrambi stampano lo stesso indirizzo (in formato esadecimale a causa di %p).

[Riferimento](https://en.cppreference.com/w/c/io/fprintf)

#### Q123. Cos'è una direttiva del preprocessore?

- [ ] Una funzione che elabora dati
- [x] Un'istruzione al preprocessore prima della compilazione
- [ ] Una direttiva dal processore
- [ ] Un tipo di ciclo

**Spiegazione:**
Le direttive del preprocessore (come #include, #define, #ifdef) sono istruzioni elaborate prima della compilazione vera e propria. Iniziano con # e sono gestite dal preprocessore.

[Riferimento](https://en.cppreference.com/w/c/preprocessor)

#### Q124. Qual è l'output di questo codice?

{% raw %}

```c
int arr[3][3] = {{1,2,3},{4,5,6},{7,8,9}};
printf("%d", arr[1][2]);
```

{% endraw %}

- [ ] 5
- [x] 6
- [ ] 8
- [ ] 9

**Spiegazione:**
`arr[1][2]` accede alla riga 1 (seconda riga: {4,5,6}), colonna 2 (terzo elemento: 6).

[Riferimento](https://en.cppreference.com/w/c/language/array)

#### Q125. Qual è lo scopo della funzione `memset()`?

- [ ] Per allocare memoria
- [x] Per riempire un blocco di memoria con un valore specifico
- [ ] Per copiare memoria
- [ ] Per liberare memoria

**Spiegazione:**
`memset()` riempie un blocco di memoria con un valore byte specificato. È comunemente usato per inizializzare array o strutture a zero.

[Riferimento](https://en.cppreference.com/w/c/string/byte/memset)

#### Q126. Qual è la differenza tra `strcpy()` e `strncpy()`?

- [ ] strcpy è più veloce
- [x] strncpy limita il numero di caratteri copiati
- [ ] strcpy può copiare qualsiasi tipo di dato
- [ ] Non c'è differenza

**Spiegazione:**
`strcpy()` copia l'intera stringa incluso il terminatore null. `strncpy()` copia al massimo n caratteri, fornendo protezione contro il buffer overflow.

[Riferimento](https://en.cppreference.com/w/c/string/byte/strncpy)

#### Q127. Qual è l'output di questo codice?

```c
int x = 10;
int y = 3;
printf("%d", x % y);
```

- [x] 1
- [ ] 3
- [ ] 0
- [ ] 10

**Spiegazione:**
L'operatore `%` è l'operatore modulo. 10 % 3 dà il resto di 10 diviso per 3, che è 1.

[Riferimento](https://en.cppreference.com/w/c/language/operator_arithmetic)

#### Q128. Cos'è una macro in C?

- [ ] Una funzione grande
- [x] Una direttiva del preprocessore che definisce un frammento di codice
- [ ] Un tipo di variabile
- [ ] Un costrutto di ciclo

**Spiegazione:**
Una macro è definita usando #define e rappresenta un frammento di codice che viene sostituito dal preprocessore prima della compilazione. Può essere una costante o un costrutto simile a una funzione.

[Riferimento](https://en.cppreference.com/w/c/preprocessor/replace)

#### Q129. Qual è l'output di questo codice?

```c
int x = 5;
int y = 10;
int z = (x > y) ? x : y;
printf("%d", z);
```

- [ ] 5
- [x] 10
- [ ] 1
- [ ] 0

**Spiegazione:**
L'operatore ternario verifica se x > y. Poiché è falso (5 non è maggiore di 10), a z viene assegnato il valore di y, che è 10.

[Riferimento](https://en.cppreference.com/w/c/language/operator_other)

#### Q130. Qual è lo scopo della funzione `free()`?

- [ ] Per liberare risorse CPU
- [x] Per deallocare memoria allocata dinamicamente
- [ ] Per liberare variabili dall'ambito
- [ ] Per cancellare lo schermo

**Spiegazione:**
`free()` dealloca la memoria che era stata precedentemente allocata da `malloc()`, `calloc()` o `realloc()`. È essenziale per prevenire perdite di memoria.

[Riferimento](https://en.cppreference.com/w/c/memory/free)

#### Q131. Qual è l'output di questo codice?

```c
char str[] = "Hello";
printf("%d", strlen(str));
```

- [ ] 6
- [x] 5
- [ ] 4
- [ ] Indefinito

**Spiegazione:**
`strlen()` restituisce la lunghezza della stringa escludendo il terminatore null. "Hello" ha 5 caratteri.

[Riferimento](https://en.cppreference.com/w/c/string/byte/strlen)

#### Q132. Cos'è una variabile statica all'interno di una funzione?

- [ ] Una variabile che non può cambiare
- [x] Una variabile che mantiene il suo valore tra le chiamate di funzione
- [ ] Una variabile memorizzata in ROM
- [ ] Una variabile globale

**Spiegazione:**
Una variabile statica all'interno di una funzione mantiene il suo valore tra le chiamate di funzione. È inizializzata solo una volta ed esiste per la durata del programma.

[Riferimento](https://en.cppreference.com/w/c/language/storage_duration)

#### Q133. Qual è l'output di questo codice?

```c
int arr[] = {1, 2, 3, 4, 5};
int *p = arr + 2;
printf("%d", *p);
```

- [ ] 1
- [ ] 2
- [x] 3
- [ ] 4

**Spiegazione:**
`arr + 2` punta al terzo elemento (indice 2). Dereferenziandolo con `*p` si ottiene il valore 3.

[Riferimento](https://en.cppreference.com/w/c/language/operator_member_access)

#### Q134. Qual è la differenza tra `printf()` e `sprintf()`?

- [ ] printf è più veloce
- [x] sprintf scrive su una stringa, printf scrive su stdout
- [ ] sprintf può stampare solo stringhe
- [ ] Non c'è differenza

**Spiegazione:**
`printf()` scrive output formattato su stdout (console). `sprintf()` scrive output formattato su un buffer di stringa di caratteri.

[Riferimento](https://en.cppreference.com/w/c/io/fprintf)

#### Q135. Qual è l'output di questo codice?

```c
int x = 5;
printf("%d", x & 3);
```

- [ ] 5
- [ ] 3
- [x] 1
- [ ] 8

**Spiegazione:**
L'operatore `&` è AND bit a bit. 5 in binario è 101, 3 è 011. 101 & 011 = 001 = 1.

[Riferimento](https://en.cppreference.com/w/c/language/operator_arithmetic)

#### Q136. Cos'è una guardia di intestazione?

- [ ] Una funzionalità di sicurezza
- [x] Un costrutto del preprocessore per prevenire l'inclusione multipla
- [ ] Una funzione che protegge le intestazioni
- [ ] Un tipo di commento

**Spiegazione:**
Le guardie di intestazione (usando #ifndef, #define, #endif) impediscono che un file di intestazione venga incluso più volte nella stessa unità di compilazione, il che causerebbe errori di ridefinizione.

[Riferimento](https://en.cppreference.com/w/c/preprocessor/conditional)

#### Q137. Qual è l'output di questo codice?

```c
int x = 10;
int y = 20;
int *p = &x;
p = &y;
printf("%d", *p);
```

- [ ] 10
- [x] 20
- [ ] Indirizzo di x
- [ ] Indirizzo di y

**Spiegazione:**
Inizialmente p punta a x. Poi `p = &y` fa puntare p a y. `*p` dereferenzia p per ottenere il valore di y, che è 20.

[Riferimento](https://en.cppreference.com/w/c/language/pointer)

#### Q138. Qual è lo scopo della funzione `memcpy()`?

- [ ] Per allocare memoria
- [x] Per copiare un blocco di memoria dalla sorgente alla destinazione
- [ ] Per confrontare blocchi di memoria
- [ ] Per liberare memoria

**Spiegazione:**
`memcpy()` copia n byte dalla memoria sorgente alla memoria di destinazione. È più veloce della copia elemento per elemento ma non gestisce regioni di memoria sovrapposte (usa `memmove()` per quello).

[Riferimento](https://en.cppreference.com/w/c/string/byte/memcpy)

#### Q139. Qual è l'output di questo codice?

```c
int x = 5;
printf("%d", x | 3);
```

- [ ] 3
- [ ] 5
- [x] 7
- [ ] 8

**Spiegazione:**
L'operatore `|` è OR bit a bit. 5 in binario è 101, 3 è 011. 101 | 011 = 111 = 7.

[Riferimento](https://en.cppreference.com/w/c/language/operator_arithmetic)

#### Q140. Qual è la differenza tra `strcmp()` e `strncmp()`?

- [ ] strcmp distingue maiuscole/minuscole, strncmp no
- [x] strncmp confronta solo i primi n caratteri
- [ ] strcmp è più veloce
- [ ] Non c'è differenza

**Spiegazione:**
`strcmp()` confronta stringhe intere. `strncmp()` confronta al massimo n caratteri, il che è utile per confrontare prefissi di stringhe o limitare la lunghezza del confronto.

[Riferimento](https://en.cppreference.com/w/c/string/byte/strncmp)