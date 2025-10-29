## C++

#### D1. Qual è l'output di questo codice?

```cpp
vector<int> v(22);
bool b = (v[6]);
printf("%d", !b);
```

- [ ] False
- [ ] 0
- [x] 1
- [ ] Questo codice ha un errore.

#### D2. Quale delle seguenti è una ragione per cui l'uso di questa riga è considerato una cattiva pratica? (_Alternativa_: Perché l'uso di questa riga è considerato una cattiva pratica?)

```cpp
using namespace std;
```

- [ ] Il codice compilato è sempre più grande a causa di tutti i simboli importati.
- [x] Se il codice utilizza una funzione definita in due librerie diverse con lo stesso prototipo ma possibilmente con implementazioni diverse, ci sarà un errore di compilazione dovuto all'ambiguità.
- [ ] Include automaticamente tutti i file di intestazione nella libreria standard (cstdint, cstdlib, cstdio, iostream, ecc.).
- [ ] Fa sì che il compilatore imponga l'inclusione esclusiva dei file di intestazione appartenenti alla libreria standard, generando un errore di compilazione quando viene incluso un file di intestazione diverso.

[Riferimento](https://www.geeksforgeeks.org/using-namespace-std-considered-bad-practice/)

#### D3. Qual è la dimensione minima che una variabile di tipo child_t può occupare in memoria?

```cpp
typedef struct{
    unsigned int  age    : 4;
    unsigned char gender : 1;
    unsigned int  size   : 2;
}child_t;
```

- [ ] 7 bit.
- [ ] 25 byte.
- [ ] 1 bit.
- [x] 1 byte.

[Riferimento](https://en.cppreference.com/w/cpp/language/bit_field)

#### D4. Quali sono i vettori v1 e v2 dopo aver eseguito il codice?

```cpp
std::vector<int> v1{1,2,3},v2;
v2=v1;
v1.push_back(4);
v2.push_back(5);
```

- [ ] Errore
- [ ] v1:{1,2,3,4}; v2:{5};
- [ ] v1:{1,2,3,4,5}; v2:{1,2,3,4,5};
- [x] v1:{1,2,3,4}; v2:{1,2,3,5};

#### D5. Quale delle seguenti è un'affermazione vera sulla differenza tra puntatori e iteratori?

- [ ] Mentre i puntatori sono variabili che contengono indirizzi di memoria, gli iteratori sono funzioni generiche utilizzate per attraversare i contenitori. Questa funzione consente al programmatore di implementare codice di lettura e scrittura mentre il contenitore viene attraversato.
- [x] Incrementare un iteratore significa sempre accedere al prossimo elemento nel contenitore (se presente), indipendentemente dal contenitore. Incrementare il puntatore significa puntare al prossimo elemento in memoria, non sempre al prossimo elemento.
- [ ] I puntatori sono variabili che contengono indirizzi di memoria mentre l'iteratore è un intero senza segno che si riferisce agli offset negli array.
- [ ] Tutti gli iteratori sono implementati con puntatori quindi tutti gli iteratori sono puntatori ma non tutti i puntatori sono iteratori.

[Riferimento](https://stackoverflow.com/a/31128162)

#### D6. Qual è la memoria occupata da u1?

```cpp
union {
    uint16_t a;
    uint32_t b;
    int8_t c;
} u1;
```

- [x] 4 byte
- [ ] 7 byte
- [ ] 8 byte
- [ ] 2 byte

[Riferimento](https://en.cppreference.com/w/cpp/language/union)

#### D7. Quale dei seguenti operatori può essere sovraccaricato?

- [ ] `?:`
- [x] `new`
- [ ] `::`
- [ ] `.`

[Riferimento](https://www.tutorialspoint.com/operators-that-cannot-be-overloaded-in-cplusplus)

#### D8. Quale delle seguenti mostra i contenuti del vettore puntato da v1 e v2 dopo aver eseguito questo codice?

```cpp
std:: vector<int> *v1 = new std::vector<int>({1,2,3});
std:: vector<int> *v2;
v2=v1;
v1->push_back(4);
v2->push_back(5);
```

- [ ] `*v1:{1,2,3,4}; *v2:{5};`
- [x] `*v1:{1,2,3,4,5}; *v2:{1,2,3,4,5};`
- [ ] Errore
- [ ] `*v1:{1,2,3,4}; *v2:{1,2,3,5};`

v1 e v2 puntano allo stesso vettore.

#### D9. Quale delle seguenti NON è una differenza tra una classe e una struct?

- [ ] Poiché le struct fanno parte del linguaggio di programmazione C, c'è una certa complessità tra le struct C e C++. Questo non è il caso delle classi.
- [ ] Le classi possono avere funzioni membro; le struct sono private.
- [ ] Lo specificatore di accesso predefinito per i membri di una struct è pubblico, mentre per i membri della classe è privato.
- [x] I parametri di tipo template possono essere dichiarati con le classi, ma non con la parola chiave struct.

I template possono essere utilizzati sia con classi che con struct  
[Riferimento](https://docs.microsoft.com/en-us/cpp/cpp/struct-cpp?view=msvc-170)  
[Riferimento](https://www.fluentcpp.com/2017/06/13/the-real-difference-between-struct-class/)

#### D10. Supponi di dover mantenere una struttura dati con il permesso di accedere a una risorsa in base ai giorni della settimana, ma non puoi usare una variabile bool per ogni giorno. Devi usare un bit per giorno della settimana. Quale delle seguenti è un'implementazione corretta di una struttura con campi di bit per questa applicazione?

- [x] A

```cpp
typedef struct {
    int sunday:1;
    int monday:1;
    // altri giorni
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
    // altri giorni
    bit friday:1;
    bit saturday:1;
} weekdays;

```

- [ ] D

```cpp
typedef struct {
    bit sunday;
    bit monday;
    // altri giorni
    bit friday;
    bit saturday;
} weekdays;
```

[Riferimento](https://en.cppreference.com/w/cpp/language/bit_field) _NOTA_: La sintassi corretta è che ogni variabile ha dimensione di 1 bit. `bit` non è un tipo in C++.

#### D11. Cos'è un lvalue?

- [ ] È un'espressione costante, cioè un'espressione composta da costanti e operazioni.
- [ ] È un'espressione che rappresenta un oggetto con un indirizzo.
- [ ] È un'espressione adatta per l'operando sinistro in un'operazione binaria.
- [x] È un valore di posizione, cioè un indirizzo di memoria adatto per essere assegnato a un puntatore o riferimento.

#### D12. Cosa fa lo specificatore di tipo auto in questa riga di codice (da C++11)?

```cpp
auto x = 4000.22;
```

- [x] Specifica che il tipo di x sarà dedotto dall'inizializzatore - in questo caso, double.
- [ ] Specifica che il tipo di x è automatico, il che significa che può essere assegnato a diversi tipi di dati durante il programma.
- [ ] Specifica che x è una variabile con durata di archiviazione automatica.
- [ ] Specifica che verrà allocata più memoria per x nel caso ne abbia bisogno, evitando la perdita di dati dovuta all'overflow.

#### D13. Un template di classe è un \_?

- [x] classe scritta con il paradigma di programmazione generica, specificando il comportamento in termini di parametro di tipo piuttosto che di tipo specifico.
- [ ] superclasse vuota destinata all'ereditarietà e al polimorfismo.
- [ ] classe che consiste solo di una variabile membro, senza costruttore, distruttore o funzioni membro.
- [ ] codice sorgente scheletro per una classe in cui il programmatore deve compilare parti specifiche per definire i tipi di dati e gli algoritmi utilizzati.

[Riferimento](https://www.mygreatlearning.com/blog/templates-in-cpp/)

#### D14. Qual è l'equivalente dell'operatore ternario per questo frammento di codice?

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

[Riferimento](https://www.w3schools.com/cpp/cpp_conditions_shorthand.asp)

#### D15. Qual è l'output del codice fornito qui sotto?

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

#### D16. Qual è il significato delle due parti specificate tra parentesi in un ciclo for basato su intervallo, separate da due punti?

- [x] La prima è una dichiarazione di variabile che conterrà un elemento in una sequenza. La seconda è la sequenza da attraversare.
- [ ] La prima è un iteratore, e la seconda è il valore di incremento da aggiungere all'iteratore.
- [ ] La prima è la variabile iterante. La seconda è una `std::pair` che specifica l'intervallo (inizio e fine) in cui la variabile itererà.
- [ ] La prima è un oggetto contenitore. La seconda è una `std::pair` che specifica l'intervallo (inizio e fine) in cui gli elementi saranno accessibili all'interno del ciclo.

#### D17. Qual è l'output del codice fornito qui sotto?

```cpp
int8_t a=200;
uint8_t b=100;
if(a>b)
    std::cout<<"greater";
else
    std::cout<<"less";
```

- [ ] Non c'è output perché c'è un'eccezione quando si confronta un int8_t con un uint8_t.
- [ ] greater
- [x] less
- [ ] Non c'è output perché c'è un errore del compilatore.

Nota: una variante della domanda qui sotto.

#### D18. Qual è l'output di questo blocco di codice?

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

Nota: Conversione implicita da 'int' a 'int8_t' (alias 'signed char') cambia il valore da 200 a -56

#### D19. Qual è l'output dopo aver eseguito questo frammento di codice?

```cpp
int x=5, y=2;
if(x & y) {
    /*_parte A_*/
}
else {
    /*_parte B_*/
}
```

- [ ] La parte A viene eseguita perché x==5 (vero) e y==2 (vero), quindi l'operazione AND valuta come vera.
- [x] La parte B viene eseguita perché (x & y) risulta in 0, o falso.
- [ ] La parte A viene eseguita perché (x & y) risulta in un valore diverso da zero, o vero.
- [ ] La parte B viene eseguita perché l'istruzione (x & y) non è valida, quindi falsa.

[Riferimento](https://stackoverflow.com/questions/63867765/dont-understand-why-if-5-2-is-false)

#### D20. Qual è una definizione valida per la funzione `get_length`, che restituisce la lunghezza di una stringa terminata con null?

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

#### D21. Quale classe STL è la più adatta per implementare una collezione di dati che è sempre ordinata in modo che l'operazione pop ottenga sempre il più grande degli elementi? Supponi di essere interessato solo alle operazioni push e pop.

- [ ] `std::list`
- [ ] `std::vector`
- [x] `std::priority_queue`
- [ ] `std::map`

#### D22. Qual è il significato delle tre sezioni specificate tra parentesi in un ciclo for separate da punti e virgola?

- [ ] La prima è il nome della variabile iterante, la seconda è il numero di volte da iterare, e la terza è l'incremento o decremento desiderato (specificato con un intero con segno).
- [x] La prima è il blocco di inizializzazione, la seconda è la condizione per iterare, e la terza è il blocco di incremento.
- [ ] La prima è la variabile iterante, la seconda è il contenitore in cui dovrebbe operare, e la terza è una condizione di uscita per interrompere in qualsiasi momento.
- [ ] La prima è il nome della variabile iterante, la seconda è il valore iniziale per la variabile iterante, e la terza è il valore di stop (l'ultimo valore più uno).

#### D23. Cosa stampa questo codice?

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

[Riferimento](https://www.geeksforgeeks.org/pre-increment-and-post-increment-in-c/)

#### D24. Cosa è vero riguardo alla variabile chiamata `ptr`?

```cpp
void *ptr;
```

- [ ] È un puntatore inizializzato a NULL.
- [ ] È un puntatore a una funzione void.
- [ ] Quella dichiarazione causa un errore del compilatore, poiché i puntatori devono specificare un tipo.
- [x] È un puntatore a un valore senza tipo specifico, quindi può essere convertito per puntare a qualsiasi tipo.

[Riferimento](https://en.cppreference.com/w/cpp/language/pointer)

#### D25. Qual è l'output del codice fornito qui sotto?

```cpp
int c=3; char d='A';
std::printf("c is %d and d is %c",c,d);
```

- [ ] c is d and d is c
- [ ] c is A and d is 3
- [x] c is 3 and d is A
- [ ] c is c and d is d

#### D26. Qual è l'output di questo codice?

```cpp
printf("1/2 = %f",(float)(1/2));
```

- [ ] 1/2 = 0.499999
- [ ] 1/2 = 0
- [x] 1/2 = 0.000000
- [ ] 1/2 = 0.5

#### D27. Qual è la differenza tra un membro di classe pubblico e uno privato?

- [ ] I membri pubblici sono gli stessi delle variabili globali, quindi ogni parte del codice ha accesso ad essi. I membri privati sono gli stessi delle variabili automatiche, quindi solo la loro classe ha accesso ad essi.
- [ ] I membri pubblici sono resi accessibili a qualsiasi applicazione in esecuzione. I membri privati sono resi accessibili solo all'applicazione in cui l'oggetto è istanziato.
- [ ] I membri pubblici saranno compilati come variabili condivise in un ambiente multithread. I membri privati saranno compilati come variabili locali al thread.
- [x] I membri pubblici possono essere accessibili da qualsiasi funzione. I membri privati possono essere accessibili solo dalle funzioni membro della stessa classe e dagli amici della classe.

[Riferimento](https://www.geeksforgeeks.org/difference-between-public-and-private-in-c-with-example/)

#### D28. Qual è il valore di `x` dopo aver eseguito questo codice?

```cpp
int x=10, a=-3;
x+=a;
```

- [ ] 3
- [x] 7
- [ ] -3
- [ ] 13

#### D29. Quale affermazione è vera?

- [ ] Solo le classi possono avere variabili e metodi membro.
- [x] C++ supporta l'ereditarietà multipla.
- [ ] C++ supporta solo l'ereditarietà singola.
- [ ] Solo le struct possono ereditare.

#### D30. Considera un puntatore a void, chiamato `ptr`, che è stato impostato per puntare a una variabile floating point `g`. Quale scelta è un modo valido per dereferenziare `ptr` per assegnare il suo valore puntato a una variabile float `f` successivamente nel programma?

```cpp
float g;
void *ptr=&g;
```

- [ ] `float f=*(float)ptr;`
- [ ] `float f=(float *)ptr;`
- [ ] `float f=(float)*ptr;`
- [x] `float f=*(float *)ptr;`

#### D31. Cos'è l'operatore `.*` e cosa fa?

- [ ] È lo stesso dell'operatore di accesso ai membri della classe, o operatore freccia `(->)`, che consente di accedere a un membro di un oggetto tramite un puntatore all'oggetto.
- [x] È l'operatore puntatore a membro, e consente di accedere a un membro di un oggetto tramite un puntatore a quel membro di classe specifico.
- [ ] È l'operatore di accesso ai membri con indirizzo, che restituisce l'indirizzo di un membro di classe o struct.
- [ ] È una combinazione dell'operatore di accesso ai membri `(.)` e dell'operatore di dereferenziazione `(*)`, quindi consente di accedere all'oggetto a cui punta un puntatore membro.

[Riferimento](https://en.cppreference.com/w/cpp/language/operator_member_access)

#### D32. Per queste dichiarazioni, quale scelta mostra quattro modi equivalenti per assegnare il carattere "y" nella stringa a una variabile char c?

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

#### D33. Quale scelta è la dichiarazione corretta per la classe chiamata Dog, derivata dalla classe Animal?

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

#### D34. Qual è l'output di questo codice qui sotto?

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

Tecnicamente, se un `char` è `signed` o `unsigned` è definito dall'implementazione;
nel secondo caso, la seconda risposta sarebbe corretta.
[Riferimento](https://en.cppreference.com/w/cpp/language/types)

#### D35. Come può il codice C++ chiamare una funzione C?

- [ ] semplicemente chiamando il codice C
- [ ] Non c'è modo per C++ di chiamare una funzione C
- [x] usando extern "C"
- [ ] importando il codice sorgente C

#### D36. Quale scelta NON è una definizione di tipo valida di una struttura che contiene coordinate x e y come interi, e che può essere utilizzata esattamente come mostrato per la variabile chiamata `center`?

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

#### D37. Quale scelta NON produce lo stesso output di questo frammento di codice? Supponi che la variabile `i` non verrà utilizzata altrove nel codice.

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

#### D38. Cosa fa questa parte di un file main.cpp?

```cpp
#include "library.h"
```

- [ ] Fa sì che la toolchain compili tutti i contenuti di library.h in modo che il suo codice eseguibile sia disponibile quando necessario dall'applicazione finale.
- [ ] Seleziona library.h per le dichiarazioni e definizioni di tutti i dati e funzioni utilizzate nel resto del file sorgente main.cpp, sostituendo infine la direttiva `#include` con quelle dichiarazioni e definizioni.
- [ ] Informa il linker che alcune funzioni o dati utilizzati nel file sorgente main.cpp sono contenuti in library.h, in modo che possano essere chiamati in fase di esecuzione. Questo è anche noto come collegamento dinamico.
- [x] Causa la sostituzione della direttiva `#include` con l'intero contenuto del file sorgente library.h. Questo è simile all'operazione Copia-Incolla di library.h in main.cpp.

#### D39. Considera questa dichiarazione di funzione di `is_even`, che prende un intero e restituisce true se l'argomento è un numero pari e false altrimenti. Quali dichiarazioni sono corrette per le versioni sovraccaricate di quella funzione per supportare numeri in virgola mobile e rappresentazioni stringa di numeri?

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

#### D40. Quale scelta è una guardia di inclusione per il file di intestazione `my_library.h`?

- [ ] A

```cpp
#ifdef MY_LIBRARY_H
#define MY_LIBRARY_H

// contenuto my_library.h

#endif /* MY_LIBRARY_H */
```

- [x] B

```cpp
#ifndef MY_LIBRARY_H
#define MY_LIBRARY_H

// contenuto my_library.h

#endif /* MY_LIBRARY_H */
```

- [ ] C

```cpp
#ifdef MY_LIBRARY_H
#undef MY_LIBRARY_H

// contenuto my_library.h

#endif /* MY_LIBRARY_H */
```

- [ ] D

```cpp
#define MY_LIBRARY_H
#include MY_LIBRARY_H

// contenuto my_library.h

#undef MY_LIBRARY_H
```

#### D41. Cosa c'è di sbagliato con questa definizione quando si utilizza un compilatore pre-C++11?

```cpp
std::vector<std::vector<int>> thematrix;
```

- [ ] Non c'è niente di sbagliato.
- [ ] Uno `std::vector` non può contenere altri contenitori `std::vector` come suoi elementi.
- [ ] La sintassi corretta dovrebbe essere: `std::vector[std::vector[int]] thematrix;`
- [x] `>>` è analizzato come operatore di shift a destra, e quindi risulta in un errore di compilazione.

#### D42. A cosa è equivalente l'istruzione qui sotto?

#### D42.b. A cosa è equivalente l'istruzione?

```cpp
sprite->x
```

- [ ] `sprite.x`
- [ ] `sprite.*x`
- [x] `(*sprite).x`
- [ ] `*sprite.x`

#### D43. Considera una classe chiamata `complexNumber`. Quale codice risulterà in un oggetto equivalente?

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

#### D44. Qual è il risultato dell'esecuzione di questo frammento di codice?

```cpp
bool x=true, y=false;

if (~x || y) {
    /*parte A*/
} else {
    /*parte B*/
}
```

- [ ] La parte A viene eseguita perché l'espressione `(~x || y)` risulta sempre vera se `y==false`.
- [ ] La parte B viene eseguita perché l'istruzione `(~x || y)` non è valida, quindi falsa.
- [x] La parte A viene eseguita perché `~x` non è zero, il che significa vero.
- [ ] La parte B viene eseguita perché `~x` è falso e `y` è falso, quindi l'operazione OR valuta come falsa.

#### D45. Quale sarebbe l'output di questo codice?

```cpp
int32_t nums[3]={2,4,3};
std::cout << ( nums[0] << nums[1] << nums[2] );
```

- [ ] L'output sono gli indirizzi di `nums[0]`, `nums[1]`, e `nums[2]`, in quell'ordine, senza spazi.
- [x] 256
- [ ] `0`
- [ ] `243`

#### D46. Qual è l'output di questo codice?

```cpp
float values[5]={0.54f, 2.71828f, 3.14159f, 5.499999f, 10.0f};
for(auto f:values)
    printf("%i ",(int)(f+0.5f));
```

- [ ] `0.54 2.71828 3.14159 5.499999 10.0`
- [ ] `1 3 4 6 11`
- [ ] `0 2 3 5 10`
- [x] `1 3 3 5 10`

#### D47. Quale delle seguenti classi STL è la più adatta per implementare una rubrica telefonica? Supponi che ogni voce contenga un nome e un numero di telefono, senza duplicati, e che si voglia effettuare una ricerca per nome.

- [ ] `std::priority_queue`
- [ ] `std::list`
- [ ] `std::vector`
- [x] `std::map`

[Riferimento](https://en.cppreference.com/w/cpp/container/map)

#### D48. Cosa fa questo programma?

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

- [ ] Rinomina text1.txt in text2.txt.
- [ ] Crea una directory chiamata text2.txt e sposta text1.txt lì.
- [x] Copia il contenuto di text1.txt in text2.txt - cioè, crea una copia di text1.txt, chiamata text2.txt.
- [ ] Aggiunge il contenuto di text1.txt in text2.txt - cioè, sostituisce il contenuto di text2.txt con la concatenazione di text2.txt e text1.txt.

[Riferimento](https://en.cppreference.com/w/cpp/header/fstream)

#### D49. Quale delle seguenti NON è una conseguenza della dichiarazione della variabile membro `count` di my_class come statica? / Alt.: Quale affermazione è vera quando si dichiara la variabile membro `count` come statica?

```cpp
class my_class {
    public: static int count;
}
```

- [x] La variabile non può essere modificata da nessuna parte del codice nella stessa applicazione o thread. Tuttavia, altri thread possono modificarla.
- [ ] La variabile esiste anche quando non sono stati definiti oggetti della classe, quindi può essere modificata in qualsiasi punto del codice sorgente.
- [ ] La variabile viene allocata una sola volta, indipendentemente da quanti oggetti vengono istanziati, perché è legata alla classe stessa, non alle sue istanze.
- [ ] Tutti gli oggetti che tentano di accedere alla loro variabile membro count in realtà fanno riferimento all'unica variabile statica count legata alla classe.

[Riferimento](https://en.cppreference.com/w/cpp/language/static)

#### D50. Qual è il tipo presunto di una costante rappresentata nel codice sorgente come `0.44`?

- [x] double
- [ ] long float
- [ ] long double
- [ ] float

#### D51. Qual è un modo appropriato di rimuovere `my_object` come mostrato qui sotto?

```cpp
my_class *my_object = new my_class();
```

- [x] `delete(my_object);`
- [ ] `free(my_object);`
- [ ] Il garbage collector distruggerà l'oggetto alla fine.
- [ ] Uscire dallo scope distruggerà l'oggetto.

#### D52. Qual è il modo corretto di chiamare la funzione membro `count` per il puntatore all'oggetto chiamato `grades`?

```cpp
class my_array{
    public:
        int count();
};  // ... altri membri sopra

int main(){
    my_array *grades = new my_array();
};  // ... altro codice sopra
```

- [ ] `grades.count();`
- [ ] `my_array->count();`
- [x] `grades->count();`
- [ ] `my_array.count();`

[Riferimento](https://en.cppreference.com/w/c/language/operator_member_access)

#### D53. Quale sarebbe l'output di questo codice?

```cpp
int i0=4, i1=6, i2=8;
int& nums[3]={i2,i0,i1};
std::cout<<nums[0]<<nums[1]<<nums[2];
```

- [x] Non c'è output. Il codice causa un errore del compilatore perché `nums` è un array di riferimenti, che è illegale.
- [ ] 846
- [ ] L'output sono gli indirizzi di `i2`, `i0`, e `i1`, in quell'ordine, senza spazi.
- [ ] 468

[Riferimento](https://en.cppreference.com/w/cpp/language/array)

#### D54. Questo codice causa un errore del compilatore? Se sì, perché, e se no, cos'è `child_t`?

```cpp
typedef struct{
    unsigned int  age    : 4;
    unsigned char gender : 1;
    char                 : 0;
    unsigned int  size   : 2;
}child_t;
```

- [ ] Sì, causa un errore del compilatore perché il carattere due punti non è consentito nelle definizioni di struct.
- [x] No, e `child_t` è un tipo definito come una struttura con campi di bit. Ha 4 bit per l'età e 1 bit per il genere nel primo byte, e 2 bit per la dimensione nel secondo byte.
- [ ] Sì, causa un errore del compilatore perché c'è un campo senza nome.
- [ ] Sì, causa un errore del compilatore perché un campo è definito come avente una dimensione di 0.

[Riferimento](https://en.cppreference.com/w/cpp/language/bit_field)

#### D55. A cosa è equivalente questa espressione?

```cpp
A->B
```

- [ ] `*(A.B)`
- [ ] `B=A`
- [x] `(*A).B`
- [ ] `&A.B`

Nota: una variante più semplice della domanda qui sotto.

#### D56. A cosa è equivalente questa espressione?

```cpp
A->B->C->D
```

- [ ] `A.B.C.D`
- [ ] `*A.*B.*C.*D`
- [ ] `&A.&B.&C.&D`
- [x] `*(*((*A).B).C).D`

**Nota:** una variante più complessa della domanda sopra.

#### D57. Cosa fa questa funzione?

```cpp
auto buff = new char[50];
std::memset(buff,20,50);
```

- [ ] Dichiara un buffer di memoria chiamato buff che inizia all'indirizzo 20 e termina all'indirizzo 70.
- [ ] Imposta tutti i bit nell'array chiamato buffer dal suo elemento all'indice 20 al suo elemento all'indice 50.
- [x] Scrive il valore 20 in ogni indirizzo di memoria da buff a buff+49.
- [ ] Dichiara un buffer di memoria chiamato buff che inizia all'indirizzo 20 e termina all'indirizzo 50.

[Riferimento](https://en.cppreference.com/w/cpp/string/byte/memset)

#### D58. Considera una classe chiamata `CustomData`. Quale scelta è una sintassi di dichiarazione corretta per sovraccaricare l'operatore postfisso `++` come membro di classe?

- [ ] `CustomData& operator++();`
- [ ] `void operator++(CustomData);`
- [ ] `CustomData operator++(CustomData);`
- [x] `CustomData operator++(int);`

[Riferimento](https://en.cppreference.com/w/cpp/language/operators)

#### D59. Vuoi ordinare my_array, dichiarato qui sotto. Quale scelta è la chiamata corretta a std::sort, utilizzando un'espressione lambda come funzione di confronto?

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

[Riferimento](https://docs.microsoft.com/en-us/cpp/cpp/lambda-expressions-in-cpp?view=msvc-160)

#### D60. Quale scelta è l'implementazione più ragionevole della funzione std::mutex::lock() usando std::mutex::try_lock()?

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

Nota: variante della domanda qui sotto.

#### D61. Qual è la differenza principale tra queste due funzioni?

```cpp
std::mutex::lock()
std::mutex::try_lock()
```

- [ ] `lock()` ha un privilegio maggiore su `try_lock()`. Questo significa che hai una migliore possibilità di acquisire un mutex con `lock()`.
- [x] Entrambe tentano di acquisire un lock, ma `lock()` si blocca se il mutex non è disponibile, mentre `try_lock()` restituisce se il mutex è disponibile o meno.
- [ ] `lock()` impone la preemption, mentre `try_lock()` suggerisce la preemption.
- [ ] Se il mutex non è disponibile, `try_lock()` ritorna con un codice corrispondente, mentre `lock()` strappa il mutex dal thread che lo possiede attualmente.

Nota: variante della domanda precedente.

[Riferimento](https://en.cppreference.com/w/cpp/thread/mutex/try_lock)

#### D62. Qual è lo scopo di un distruttore?

- [x] Permette al programmatore di scrivere il codice necessario per liberare le risorse acquisite dall'oggetto prima di eliminare l'oggetto stesso.
- [ ] Elimina un oggetto. Un esempio di distruttore è la funzione `delete()`.
- [ ] Termina un programma. Questo può essere ottenuto come una normale chiamata di funzione o come un'eccezione.
- [ ] Non ci sono distruttori in C++.

#### D63. Qual è un vantaggio di dichiarare il parametro come riferimento `const` invece di dichiararlo come oggetto normale?

```cpp
int calculateMedian(const my_array& a)
```

- [ ] In realtà, gli oggetti non possono essere passati come variabili normali, perché richiedono una chiamata al costruttore. Pertanto, un riferimento `const` è l'unico modo per passare istanze di classe alle funzioni.
- [ ] Non ci sono vantaggi perché un riferimento e un oggetto sono trattati come la stessa cosa.
- [x] Il qualificatore `const` vieta al codice di modificare l'argomento, quindi il programmatore può essere sicuro che l'oggetto sorgente rimarrà invariato. / Alt.: L'argomento è passato come riferimento, quindi se l'oggetto my_array passato è grande, il programma richiederà meno tempo e memoria.
- [ ] L'argomento è passato come riferimento, quindi la funzione riceve una copia che può essere modificata senza influenzare la variabile originale.

[Riferimento](https://stackoverflow.com/a/2627179/10773894)

#### D64. Cos'è una guardia di inclusione?

- [ ] una direttiva del preprocessore che previene comportamenti incoerenti nelle righe che contengono le direttive #ifdef, #ifndef o #elif
- [ ] un'opzione del compilatore che impedisce al codice utente di includere librerie aggiuntive
- [x] un'istruzione del preprocessore che impedisce a un file sorgente di essere incluso più di una volta in un progetto
- [ ] una libreria che aggiunge funzionalità di sicurezza come mutex, watchdog timer e asserzioni al progetto

#### D65. Qual è la dichiarazione corretta di un costruttore predefinito per una classe chiamata Sprite?

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

#### D66. Qual è lo scopo di questa riga in un file di intestazione?

```cpp
#pragma once
```

- [ ] per limitare l'uso dei suoi contenuti a un solo file sorgente
- [ ] per dire al compilatore che può essere istanziata solo una variabile dalle classi o tipi contenuti in questo file di intestazione
- [ ] per aiutare il compilatore a terminare più velocemente assicurando che sia necessario un solo passaggio del compilatore per il codice incluso in questo file di intestazione
- [x] per far sì che il compilatore analizzi quel file di intestazione una sola volta, anche se è incluso più volte nel sorgente

[riferimento qui](https://en.cppreference.com/w/cpp/preprocessor/impl)

#### D67. Cos'è una variabile di tipo double?

- [ ] una 2-tupla
- [ ] un numero intero
- [x] un numero in virgola mobile
- [ ] una stringa con più di 255 caratteri

[Riferimento](https://www.educba.com/c-plus-plus-double/)

#### D68. Oltre allo spostamento di bit a sinistra, per cosa viene utilizzato l'operatore <<?

- [ ] spostare caratteri a sinistra in una stringa.
- [x] inserire caratteri in un flusso di output come std::cout.
- [ ] confrontare numeri in virgola mobile come minore di.
- [ ] assegnare una variabile a un riferimento.

#### D69. Quale scelta è una ragione per specificare il tipo di un puntatore invece di usare `void *`, che funziona come puntatore a qualsiasi tipo?

- [ ] Il compilatore ha bisogno del tipo di dato per assicurarsi che il puntatore non verrà utilizzato su tipi illegali non puntabili come funzioni, etichette, puntatori e riferimenti.
- [ ] `void *` non funziona per nessun tipo. Il linguaggio non consente di assegnare nulla diverso da `void` a un puntatore a `void *`.
- [x] Il compilatore ha bisogno del tipo di dato per sapere quanta memoria allocare per il puntatore perché diversi tipi di dati richiedono diverse lunghezze di puntatore.
- [ ] Sì, causa un errore del compilatore perché un campo è definito come avente una dimensione di 0.

[Riferimento](https://stackoverflow.com/questions/9802585/why-is-the-data-type-needed-in-pointer-declarations)

#### D70. Cosa c'è di sbagliato con questo pezzo di codice?

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

- [ ] La funzione main dovrebbe avere un tipo di ritorno void.
- [ ] `std::cin` e `std::cout` non sono validi. I nomi corretti per i flussi di input e output dei caratteri sono `cin` e `cout`.
- [ ] Dovrebbe essere utilizzato l'indirizzo di `str`. Cioè `&str` invece di `str`.
- [x] Il flusso dell'operatore di input è invertito. dovrebbe iniziare da `std::cin` e poi fluire (>>) in `str`.

#### D71. Quando posto in un contesto di esecuzione valido, quale istruzione allocherà dinamicamente memoria dall'heap per un intero con valore 11?

- [ ] `int anInt = new int(11);`
- [ ] `int* anInt = new int[11];`
- [ ] `int anInt = new int[11];`
- [x] `int* anInt = new int(11);`

#### D72. Quale scelta descrive meglio il tipo `long`?

- [x] un numero intero di almeno 32 bit
- [ ] una stringa con più di 255 caratteri
- [ ] un puntatore
- [ ] un numero in virgola mobile a 64 bit

#### D73. Quale dei seguenti tipi ha la funzionalità più simile a una classe?

- [x] `struct`
- [ ] `union`
- [ ] `enum`
- [ ] `namespace`

[Riferimento](https://en.cppreference.com/w/c/language/struct)

#### D74. Dati questi record in una mappa, come aggiornerai il valore per la chiave "Sinead" a 22?

![image](images/Q79.png?raw=png)

- [x] `marks["Sinead"] = 22`
- [ ] `marks["Sinead"].22`
- [ ] `marks["Sinead"] -> 22`
- [ ] `marks["Sinead"].value = 22`

#### D75. Perché std::sort può ricevere un oggetto funzione come uno dei suoi parametri?

- [x] `La funzione std::sort è un template. Il programmatore è libero di inserire l'algoritmo di ordinamento in un oggetto funzione come argomento.`
- [ ] `In realtà, std::sort accetta un solo argomento, che è il contenitore da ordinare.`
- [ ] `std::sort opera su un contenitore template. Il compilatore non sa come confrontare relazionalmente i valori che contiene, quindi deve essere fornita una funzione per fare il confronto.`
- [ ] `std::sort utilizzerà la funzione parametro come gestore di errori. La funzione verrà chiamata se si verifica un errore.`

#### D76. Cosa succederà quando eseguirai questo frammento di codice?

```
#include <iostream>

int main() {
float a = 5.51;
int b = static_cast<int>(a);
std::cout << b;
}
```

- [ ] `6 verrà stampato sull'output standard, senza avvisi di compilazione generati.`
- [x] `5 verrà stampato sull'output standard, senza avvisi di compilazione generati.`
- [ ] `6 verrà stampato sull'output standard, con avvisi di compilazione generati.`
- [ ] `5 verrà stampato sull'output standard, con avvisi di compilazione generati.`

#### D77. Quale specificatore di accesso non consente ai membri della classe di essere accessibili dall'esterno della classe, ma consente loro di essere accessibili dalle classi derivate?

- [ ] guarded
- [x] protected
- [ ] public
- [ ] private

#### D78. La generazione eseguibile predefinita su UNIX per un programma C++ è \_

- [ ] a.exe
- [ ] a
- [x] a.out
- [ ] out.a

#### D79. Quale sarà l'output del seguente programma?

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

#### D80. Cosa significa "c" in cout e cin?

- [ ] compiler
- [ ] console
- [x] character
- [ ] standard namespace

#### D81. Qual è l'uso di tellp()?

- [ ] Posizione corrente del puntatore di input
- [x] Posizione corrente del puntatore di output
- [ ] Ultima posizione del puntatore di input
- [ ] Ultima posizione del puntatore di output

#### D82. Cos'è una funzione callback?

- [ ] Puntatore per un puntatore
- [x] Puntatore per una funzione
- [ ] funzione per un puntatore
- [ ] funzione per una classe

#### D83. Qual è la sintassi corretta per stampare "Hello World" in C++?

- [x] `cout << "Hello World";`
- [ ] `System.out.println("Hello World");`
- [ ] `print("Hello World");`
- [ ] `Console.WriteLine("Hello World");`

#### D84. Quante categorie di iteratori ci sono in C++?

- [ ] 4
- [ ] 3
- [ ] 7
- [x] 5

#### D85. Qual è il significato di classe base in C++?

- [ ] Eredita altre classi
- [ ] Ha una variabile puntatore
- [ ] È la prima classe dichiarata
- [x] Un'altra classe è stata ereditata da questa classe

#### D86. La dimensione degli oggetti C++ è espressa in termini di multipli della dimensione di un ** e la dimensione di un char è **.

- [ ] char, 4
- [ ] float, 8
- [ ] int, 1
- [x] char, 1

#### D87. Gli aspetti dipendenti dall'implementazione relativi a un'implementazione possono essere trovati in

- [ ] `<numeric>`
- [ ] `<limit>`
- [x] `<limits>`
- [ ] `<implementation>`

#### D88. Cos'è un costruttore predefinito?

- [x] un costruttore che può essere utilizzato senza argomenti
- [ ] un costruttore che non ha un valore di ritorno
- [ ] un costruttore utilizzato da più classi
- [ ] un costruttore che inizializza tutti i membri di una classe

#### D89. Quando si protegge un file di intestazione, perché si userebbe '#pragma once' invece della guardia 'include'?

- [ ] Non c'è motivo di scegliere perché servono scopi diversi
- [x] Una guardia include usa una macro per ottenere l'inclusione singola, ma il compilatore non può impedire al programmatore di definire quella macro altrove, il che risulterebbe in nessuna inclusione
- [ ] '#pragma once' garantisce che il codice dell'intestazione non verrà mai modificato perché è imposto dal compilatore
- [ ] Le guardie include si riferiscono al file di intestazione nel file system, non al codice, quindi non sono utili se il file di intestazione esiste più di una volta in un progetto. Questo non è un problema con '#pragma once'

#### D90. Quale delle seguenti affermazioni è valida?

- [ ] Possiamo creare un nuovo operatore C++.
- [ ] Possiamo cambiare la precedenza dell'operatore C++.
- [x] Non possiamo cambiare i template degli operatori.
- [ ] Possiamo cambiare l'associatività degli operatori C++.

#### D91. Quale dei seguenti viene/vengono automaticamente aggiunto/i a ogni classe, se non scriviamo il nostro?

- [ ] Costruttore di copia
- [ ] Operatore di assegnazione
- [ ] Un costruttore senza parametri
- [x] Tutti i precedenti

#### D92. L'istruzione if-else può essere sostituita da quale operatore?

- [ ] struttura certa
- [ ] struttura di scelta
- [x] struttura selettiva
- [ ] Nessuna delle precedenti

#### D93. Quale scelta sarebbe una soluzione ricorsiva al problema del fattoriale n!?

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

#### D94. Un distruttore di classe può essere chiamato quando si verificano una varietà di situazioni. Quale scelta NON è una di quelle situazioni?

- [ ] Il programma viene terminato. Questo chiama il distruttore degli oggetti di durata statica.
- [ ] La funzione delete() viene chiamata per un puntatore a oggetto assegnato con l'operatore new.
- [x] Il garbage collector rileva che un oggetto non verrà più utilizzato.
- [ ] Un oggetto di durata di archiviazione automatica esce dallo scope.

#### D95. Stai progettando un sistema di pagamenti in valuta estera in C++. Devi modellare una transazione di una valuta che ha un intero come quantità e un float come prezzo. Vuoi quindi dichiarare un oggetto effettivo di questo tipo. Come lo otterrai?

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

#### D96. Cosa succederà se tenterai di chiamare questa funzione con checkConcatThreshold("a");?

```cpp
int checkConcatThreshold(string a, string b) {
    return (a + b).length () > 120;
}
```

- [ ] Si verificherà un avviso di compilazione e il secondo argomento riceverà un valore predefinito di b.
- [ ] Si verificherà un avviso di compilazione e il secondo argomento riceverà un valore predefinito della stringa vuota.
- [x] Si verificherà un errore di compilazione.
- [ ] Non si verificheranno errori di compilazione e nessun avviso di compilazione.

#### D97. Devi definire una funzione lambda C++. Vuoi che la funzione abbia accesso solo alle variabili che le sono locali. La funzione dovrebbe ricevere un singolo parametro, un nome, e costruire un semplice saluto. Come lo otterrai?

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

[Riferimento](https://docs.microsoft.com/en-us/cpp/cpp/lambda-expressions-in-cpp?view=msvc-160)

#### D98. Qual è il valore di X dopo aver eseguito questo codice?

```cpp
int x=10, a=-3;
X+=a;
```

- [ ] -3
- [x] 7
- [ ] 13
- [ ] 3

**Spiegazione:** `+=` significa incremento del valore. Quindi `x += a` è equivalente a `x = x + a`

#### D99. Una volta terminata la scrittura su un file, quale metodo chiamerai su `ofstream` per notificare il sistema operativo?

- [ ] printout()
- [x] close()
- [ ] destroy()
- [ ] flush()

#### D100. Quale scelta NON è una parola chiave C++?

- [ ] static_assert
- [ ] reinterpret_cast
- [x] comPl
- [ ] alignas

#### D101. La funzione size_in_bits sembra accettare qualsiasi tipo di parametro. Questo può essere fatto sovraccaricando la funzione, o lasciando che il compilatore se ne occupi scrivendo un template. Quale scelta è un'implementazione di quel template?

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

#### D102. Per utilizzare la tastiera come input viene inclusa la libreria iostream. Per leggere l'input da file come input quale libreria è necessaria?

- [x] fstream
- [ ] cstdlib
- [ ] filestream
- [ ] iostream

#### D103. Cosa stamperà questo programma orientato agli oggetti?

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

#### D104. Il programma seguente gestisce un contenitore stack. Qual è l'output dell'esecuzione del programma?

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

#Spiegazione dettagliata:

Qui dovremmo implementare una struttura dati stack che segue il principio **FILO** o (First IN Last Out),
_stack.push()_ -> inserisce un elemento dalla fine dell'array.
_stack.pop()_ -> rimuove un elemento dalla fine dell'array.
_stack.top()_ -> Ci dà solo l'elemento in cima all'array.
Ora seguendo le sequenze di push e pop: **[1,2,3]** poi viene usata la funzione pop,
L'array appena formato è: **[1,2,4]** poi il top viene usato per recuperare l'elemento in cima '4' poi di nuovo viene usata la funzione pop che rimuove 4.
quindi, l'array risultante è: 1,2.
Poi stampa l'elemento in cima (cioè: 2).

#### D105. Quale scelta è un modo valido per sovraccaricare l'operatore condizionale ternario?

- [ ] `void& operator ?:(const bool cond, const void& iftrue, const void& iffalse);`
- [x] `L'operatore ternario non è sovraccaricabile.`
- [ ] `void& operator conditional(const bool cond, const void& iftrue, const void& iffalse);`
- [ ] `void* operator ?:(const bool cond, const void* iftrue, const void* iffalse);`

[Riferimento](https://en.cppreference.com/w/cpp/language/operators)

#### D106. Quale gerarchia di classi rappresenta un esempio di ereditarietà multilivello?

- [ ] Nello stesso programma, in punti diversi, una data classe deriva individualmente da più di una classe diversa.
- [ ] Una prima classe deriva direttamente, allo stesso tempo, da una seconda e terza classe.
- [x] Nello stesso programma, in punti diversi, una data classe deriva individualmente da più di due classi diverse.
- [ ] Una prima classe deriva da una seconda classe, e quella seconda classe è già derivata da una terza classe

#### D107. Qual è la sintassi corretta per stampare il messaggio in linguaggio C++?

- [ ] Out <<"Hello world!
- [ ] Cout << Hello world! ;
- [x] cout <<"Hello world!";
- [ ] Nessuna delle precedenti

[Riferimento](https://en.cppreference.com/w/cpp/io/cout)

#### D108. Considera il seguente programma. Quale sarà l'output/errore?

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
- [ ] Errore di compilazione: funzione non definita

[Riferimento](https://www.geeksforgeeks.org/tolower-function-in-cpp/)

#### D109. Considera il seguente segmento di codice. Riempi lo spazio vuoto alla RIGA-1 in modo che il programma stampi "not found"?

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

[Riferimento](https://www.geeksforgeeks.org/binary-search-algorithms-the-c-standard-template-library-stl/)

#### D110. Considera il seguente segmento di codice. Quale sarà l'output?

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

[Riferimento](https://cplusplus.com/reference/algorithm/sort/)

#### D111. Considera il seguente segmento di codice. Quale sarà l'output?

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

[Riferimento](https://en.cppreference.com/w/cpp/algorithm/rotate)

#### D112. Considera il seguente segmento di codice. Quale sarà l'output?

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

[Riferimento](https://en.cppreference.com/w/cpp/container/vector)

#### D113. Considera il seguente segmento di codice. Scegli l'opzione appropriata per riempire lo spazio vuoto alla RIGA-1, in modo che l'output del codice sia: a C++ Program.

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

[Riferimento](https://www.geeksforgeeks.org/stdstringappend-in-c/)

#### D114. Considera il seguente segmento di codice. Riempi lo spazio vuoto alla RIGA-1 in modo che l'output sia 5 2 3 4 5

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

[Riferimento](https://www.geeksforgeeks.org/stdstringreplace-stdstringreplace_if-c/)

#### D115. Considera il seguente segmento di codice. Quale sarà l'output?

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

[Riferimento](https://en.cppreference.com/w/cpp/container/stack)

#### D116. Considera il seguente segmento di codice. Quale/i istruzione/i è/sono corretta/e?

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

[Riferimento](https://www.geeksforgeeks.org/const-keyword-in-cpp/)

#### D117. Considera il seguente programma. Quale sarà l'output/errore(i)?

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
- [x] Errore di compilazione: argomento predefinito mancante per "char add(char, char, char)"
- [x] Errore di compilazione: chiamata di sovraccarico "add(char, char)" è ambigua

[Riferimento](https://learn.microsoft.com/en-us/cpp/cpp/function-overloading?view=msvc-170)

#### D118. Considera il seguente segmento di codice. Quale sarà l'output?

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

[Riferimento](https://www.geeksforgeeks.org/output-of-the-program-use-macros-carefully/)

#### D119. Considera il seguente segmento di codice. Quale/i riga/righe darà/daranno un errore?

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

#### D120. Considera il seguente segmento di codice. Quale sarà l'output/errore?

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
- [x] Errore di compilazione: inizializzazione non valida di riferimento non const

#Spiegazione dettagliata:
L'errore si verifica perché sta cercando di creare un riferimento a un valore temporaneo. Nella riga int &b = a+1; stiamo tentando di creare un riferimento b al risultato dell'espressione a + 1, che è un valore temporaneo. I riferimenti devono essere legati a un oggetto effettivo, non a un valore temporaneo o a un'espressione che non ha una posizione di memoria.

#### D121. Considera il seguente segmento di codice. Quale sarà l'output?

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

[Riferimento](https://www.ibm.com/docs/en/zos/2.4.0?topic=calls-pass-by-reference-c-only)

#### D122. Considera il seguente segmento di codice. Scegli l'opzione appropriata per riempire gli spazi vuoti alla RIGA-1, in modo che l'output del codice sia: 300 20000.

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

#### D123. Considera il seguente segmento di codice. Quale sarà l'output/errore?

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

- [ ] `<valore spazzatura>`
- [ ] 5
- [x] Errore di compilazione alla RIGA-1: 'ptr' const non inizializzato
- [x] Errore di compilazione alla RIGA-2: assegnazione della variabile di sola lettura 'ptr'

#### D124. Considera il seguente segmento di codice. Quale sarà l'output/errore?

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
- [x] Errore di compilazione alla RIGA-2: dichiarazione ambigua di 'int fun(int)'

#### D125. Considera il seguente segmento di codice. Riempi lo spazio vuoto alla RIGA-1 in modo che il programma stampi 5 + i3

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

[Riferimento](https://www.w3schools.com/cpp/cpp_structs.asp)

#### D126. Considera il seguente programma. Quale/i riga/righe genererà/genereranno un errore?

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

[Riferimento](https://stackoverflow.com/questions/4855422/c-classes-public-private-and-protected)

#### D127. Considera la seguente classe. Riempi gli spazi vuoti con gli specificatori di accesso appropriati in modo che il membro y possa essere accessibile dall'esterno della classe ma il membro x non possa essere accessibile.

```cpp
class Test{
________:
int x;
________:
int y;
/* Altro codice */
};
```

- [ ] public, public
- [ ] public, private
- [x] private, public
- [ ] private, private

#### D128. Quale standard C++ ha aggiunto gli inizializzatori di membri predefiniti in-class?

- [ ] C++98
- [x] C++11
- [ ] C++14
- [ ] C++17.

#### D129. Puoi usare la deduzione del tipo auto per i membri dati non statici?

- [ ] Sì, da C++11
- [x] No
- [ ] Sì, da C++20

#### D130. Devi definire un membro dati static inline in un file cpp?

- [x] No, la definizione avviene nello stesso punto in cui viene dichiarato un membro static inline.
- [ ] Sì, il compilatore ha bisogno della definizione in un file cpp.
- [ ] Sì, il compilatore ha bisogno di una definizione in tutte le unità di traduzione che usano questa variabile.

[Riferimento](https://en.cppreference.com/w/cpp/language/bit_field)

#### D131. Qual è l'output del seguente codice:

```cpp
struct S {
    int a { 10 };
    int b { 42 };
};
S s { 1 };
std::cout << s.a << ", " << s.b;
```

- [ ] L'output è: 1, 0
- [ ] L'output è: 10, 42
- [x] L'output è: 1, 42

#### D132. Una variabile static inline può essere non costante?

- [x] Sì, è solo una variabile normale.
- [ ] No, le variabili inline devono essere costanti.

#### D133. Considera il seguente codice:

```cpp
struct C {
    C(int x) : a(x) { }
    int a { 10 };
    int b { 42 };
};
C c(0);

```

- [ ] C::a viene inizializzato due volte. La prima volta, viene inizializzato con 10, e poi la seconda volta con 0 nel costruttore.
- [x] C::a viene inizializzato solo una volta con 0 nel costruttore.
- [ ] Il codice non compila perché il compilatore non può decidere come inizializzare il membro C::a.
- [ ] 2 byte

#### D134. Cosa succede quando lanci un'eccezione da un costruttore?

- [ ] L'oggetto è considerato "creato" quindi seguirà il ciclo di vita regolare di un oggetto.
- [x] L'oggetto è considerato "parzialmente creato", e quindi il compilatore non chiamerà il suo distruttore.
- [ ] Il compilatore chiama std::terminate poiché non puoi lanciare eccezioni dai costruttori.

#### D135. Cosa succede quando compili questo codice?

```cpp
struct Point { int x; int y; };
Point pt {.y = 10, .x = 11 };
std::cout << pt.x << ", " << pt.y;
```

- [x] Il codice non compila. I designatori devono essere nello stesso ordine dei membri dati nella classe Point.
- [ ] Il codice compila e stampa 11, 10.
- [ ] Il codice compila e stampa 10, 11.

#### D136. Questo codice funzionerà in C++11?

```cpp
struct User { std::string name = "unknown"; unsigned age { 0 }; };
User u { "John", 101 };
```

- [ ] Sì, il codice compila in modalità C++11.
- [x] Il codice compila a partire dalla modalità C++14.
- [ ] Il codice non compila nemmeno in C++20.

#### D137. Supponi di avere un std::map<string, int> m;. Seleziona l'unica affermazione vera sul seguente ciclo:

```cpp
for (const pair<string, int>& elem : m)
```

- [x] A Il ciclo itera correttamente sulla mappa, non creando copie extra.

- [ ] B Il ciclo creerà una copia di ogni elemento nella mappa poiché il tipo di elem non corrisponde.

- [ ] C Il codice non compilerà poiché una coppia const non può essere vincolata a una mappa.

#### D138. Identifica l'estensione corretta del file di intestazione definito dall'utente in C++.

- [ ] .cpp
- [ ] .hg
- [x] .h
- [ ] .hf

#### D139. Identifica il tipo di costruttore errato.

```cpp
auto x = 4000.22;
```

- [x] Costruttore Friend
- [ ] Costruttore predefinito
- [ ] Costruttore parametrizzato
- [ ] Costruttore di copia

#### D140. Quale dei seguenti tipi di dati è supportato in C++ ma non in C?

- [x] bool
- [ ] int
- [ ] double
- [ ] float

[Riferimento]: https://stackoverflow.com/questions/1608318/is-bool-a-native-c-type

#### D141. Identifica la sintassi corretta per dichiarare array in C++.

- [x] int arr[10]
- [ ] array arr[10]
- [ ] array{10}
- [ ] int arr

[Riferimento]: (https://en.cppreference.com/w/cpp/language/array)

#### D142. La dimensione di wchat_t è.

- [ ] 2
- [ ] 4
- [ ] 2 o 4
- [x] Dipende dal numero di bit nel sistema

#### D143. Quale dei seguenti cicli è migliore quando conosciamo il numero di iterazioni?

- [ ] while
- [x] for
- [ ] do
- [ ] Tutti i precedenti

#### D144. Quale parola chiave viene utilizzata per definire le macro in C++?

- [ ] #macro
- [x] #define
- [ ] macro
- [ ] keyword

#### D145. Quale dei seguenti operatori dovrebbe essere preferibilmente sovraccaricato come funzione globale piuttosto che come metodo membro?

- [ ] Postfisso ++
- [x] Operatore di confronto
- [ ] Operatore di inserimento <<
- [ ] Prefisso++

#### D146. Come possiamo limitare l'allocazione dinamica di oggetti di una classe usando new?

- [ ] Sovraccaricando l'operatore new
- [ ] Rendendo privato un operatore new vuoto.
- [x] Rendendo privati operatori new e new[] vuoti
- [ ] Sovraccaricando gli operatori new e new[]

#### D147. Qual è la complessità temporale del codice seguente?

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

[Riferimento](<https://medium.com/enjoy-algorithm/analysis-of-loop-in-programming-cc9a644ef8cd#:~:text=At%20each%20step%20of%20the%20iteration%2C%20the%20nested%20loop%20is,%20%3D%20O(n%C2%B2)>)

#### D148. Qual è l'output del codice fornito qui sotto?

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

Sia **++a** che **a++** aumentano il valore di a di 1 (cioè: 11) e quindi k+m diventa 22.

#### D149. Quale costrutto C++ viene utilizzato per la gestione delle eccezioni?

- [x] try-catch
- [ ] if-else
- [ ] ciclo for
- [ ] switch-case

#### D150. Qual è lo scopo dell'istruzione `break` in un ciclo in C++?

- [ ] Uscire dal programma
- [ ] Saltare l'iterazione corrente e continuare con la successiva
- [x] Terminare il ciclo
- [ ] Restituire un valore

[Riferimento]: (https://www.tutorialspoint.com/cprogramming/c_break_statement.htm)

#### D151. In C++, qual è lo scopo della parola chiave `const` quando usata con una variabile?

- [x] Rende la variabile immutabile
- [ ] Cambia il tipo di dato
- [ ] Definisce una funzione costante
- [ ] Rende la variabile un puntatore

#### D152. Quale è più efficace durante la chiamata di funzioni C++?

- [x] Chiamata per riferimento
- [ ] Chiamata per valore
- [ ] Chiamata per puntatore
- [ ] Chiamata per oggetto

[Riferimento]: (https://www.algbly.com/More/MCQs/Cpp-mcq/Cpp-functions.html)

#### D153. Quale sarà l'output del seguente programma C++?

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
- [x] "Constructor called" cinque volte e poi "Destructor called" cinque volte
- [ ] "Constructor called" cinque volte e poi "Destructor called" una volta
- [ ] Errore

#### D154. Quale scelta NON è correlata alla dichiarazione della variabile membro count come statica in my_class?

```cpp
class my_class{
    public: static int count;
}
```

- [ ] Tutti gli oggetti che cercano di accedere alla loro variabile membro count in realtà si riferiscono all'unica variabile statica count legata alla classe.
- [ ] La variabile esiste anche quando non sono stati definiti oggetti della classe, quindi può essere modificata in qualsiasi punto del codice sorgente.
- [x] La variabile non può essere modificata da nessuna parte del codice nella stessa applicazione o thread. Tuttavia, altri thread possono modificarla.
- [ ] La variabile viene allocata una sola volta, indipendentemente da quanti oggetti vengono istanziati, perché è legata alla classe stessa, non alle sue istanze.

#### D155. Qual è lo scopo della parola chiave `constexpr` in C++?

- [ ] Viene utilizzata per definire costanti in C++.
- [ ] `constexpr` viene utilizzata per specificare che una variabile è un puntatore costante.
- [x] `constexpr` viene utilizzata per indicare che un'espressione può essere valutata in fase di compilazione, rendendola adatta per l'uso in espressioni costanti.
- [ ] È una parola chiave utilizzata per creare funzioni asincrone.

[Rif](https://learn.microsoft.com/en-us/cpp/cpp/constexpr-cpp?view=msvc-170#:~:text=constexpr%20indicates%20that%20the%20value,template%20arguments%20and%20array%20declarations.)

#### D156. Cos'è un metaprogramma template in C++?

- Rif(https://www.geeksforgeeks.org/template-metaprogramming-in-c/)

- [ ] Un metaprogramma template è un linguaggio di programmazione di alto livello.
- [ ] Si riferisce alla metaprogrammazione che usa template in C++.
- [ ] È un tipo di pattern di design dell'interfaccia utente.
- [x] Un metaprogramma template è un calcolo in fase di compilazione, dove i template e la specializzazione dei template vengono utilizzati per eseguire calcoli in fase di compilazione.

#### D157. Identifica l'esempio corretto per un operatore di pre-incremento.

- [x] ++i
- [ ] i++
- [ ] --i
- [ ] +i

#### D158. Quale sarà l'output del seguente codice?

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

- [ ] Trasposta della matrice
- [x] Stessa matrice
- [ ] Immagine speculare della matrice
- [ ] Matrice invertita

#### D159. Cos'è una race condition in C++?

- [ ] Una condizione in cui il programma viene eseguito più velocemente del previsto
- [x] Una condizione in cui più thread accedono a dati condivisi contemporaneamente, e il risultato dipende dalla tempistica della loro esecuzione
- [ ] Una condizione in cui due thread competono per il tempo della CPU
- [ ] Una condizione in cui un ciclo viene eseguito troppo rapidamente e deve essere rallentato

[Riferimento](https://en.cppreference.com/w/cpp/language/memory_model)

#### D160. Considera il seguente codice che ha una race condition. Qual è il modo corretto per risolverlo?

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

- [ ] Aggiungere la parola chiave `volatile`: `volatile int counter = 0;`
- [x] Usare `std::mutex` per bloccare/sbloccare intorno a `counter++` nella sezione critica
- [ ] Usare `std::this_thread::sleep_for()` per ritardare ogni incremento
- [ ] Cambiare `counter++` in `++counter` per un'operazione atomica

[Riferimento](https://en.cppreference.com/w/cpp/thread/mutex)