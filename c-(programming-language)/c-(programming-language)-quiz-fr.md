## C (Langage de programmation)

#### Q1. Quel exemple de code finira par épuiser la mémoire de l'ordinateur?

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

#### Q2. Quelle sera la sortie du code ci-dessous?

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

- [ ] Rien n'est affiché à l'écran

#### Q3. Quel est le nom pour appeler une fonction à l'intérieur de la même fonction?

- [x] récursion
- [ ] sous-fonction
- [ ] appel interne
- [ ] boucle infinie

[Référence](https://www.cprogramming.com/tutorial/c/lesson16.html)

#### Q4. Que démontre la déclaration de la variable c2?

```c
main(){
    char c1 ='a';
    char c2 = c1+10;
}
```

- [x] arithmétique de caractères
- [ ] affectation non définie
- [ ] conversion de type
- [ ] déclaration invalide

[Référence](https://tutorialspoint.dev/language/c/character-arithmetic-c-c)

#### Q5. De quoi cette déclaration est-elle un exemple?

```c
struct s {
    int i;
    struct s *s1;
    struct s *s2;
};
```

- [x] un nœud
- [ ] une liste chaînée
- [ ] une pile
- [ ] un arbre binaire

#### Q6. Les fichiers d'en-tête sont listés en utilisant la directive de prétraitement #include, et peuvent avoir l'un des formats suivants : #include &lt;fichierA&gt; ou #include "fichierB". Quelle est la différence entre ces deux formats?

- [ ] Le préprocesseur essaiera de localiser fichierA dans le même répertoire que le fichier source, et fichierB dans un chemin de répertoire prédéterminé.
- [ ] Le préprocesseur essaiera de localiser fichierA dans le répertoire système fixe. Il essaiera de localiser fichierB dans le chemin de répertoire désigné par l'option -I ajoutée à la ligne de commande lors de la compilation du code source.
- [ ] Le fichier utilisant la syntaxe fichierA doit être un fichier système, en nombre illimité; fichierB doit être un fichier utilisateur au maximum d'un par fichier source.
- [x] Le préprocesseur essaiera de localiser fichierA dans un chemin de répertoire prédéterminé. Il essaiera de localiser fichierB dans le même répertoire que le fichier source ainsi qu'un chemin de répertoire personnalisé.

[Référence](https://www.geeksforgeeks.org/difference-between-include-and-include-in-c-c-with-examples/#:~:text=The%20difference%20between%20the%20two,be%20included%20in%20the%20code.&text=%23include%20is%20for%20pre%2Ddefined%20header%20files.)

#### Q7. En utilisant une boucle for, comment pourriez-vous écrire un code C pour compter de 10 à 1 et afficher chaque nombre sur sa propre ligne?

- [ ] :

```c
for (int i = 0; i>=0, i--){
    printf("%d\n", i);
}//fin de la boucle
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
}// fin de la boucle
```

#### Q8. Lequel n'est pas un mot réservé en C standard?

- [ ] volatile
- [x] typeof
- [ ] register
- [ ] typedef

[Référence](https://www.ibm.com/docs/en/adfz/developer-for-zos/14.2.0?topic=programs-c-reserved-keywords)

#### Q9. Que retourne le programme ci-dessous?

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

#### Q10. En utilisant la déclaration Union ci-dessous, combien d'octets d'espace mémoire les données de ce type occuperont-elles?

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

#### Q11. Dans cet exemple de code, qu'est-ce qui n'est pas un problème pour le compilateur C?

```c
main(){
    constant int PI = 3.14;
    printf("%f\n", pi);
}
```

- [x] La valeur de PI doit être définie à 3.141593, et non 3.14
- [ ] La déclaration de PI doit dire const, et non constant.
- [ ] Le type de données de PI doit être float, et non int.
- [ ] L'instruction printf doit utiliser PI, et non pi.

#### Q12. Quel est le plus petit programme à compiler et exécuter sans erreurs?

- [ ] main()
- [x] int main() {return 0;}
- [ ] main() { }
- [ ] main() { ; }

[Référence](https://www.beningo.com/150-the-wolrds-shortest-c-program/)

#### Q13. Qu'est-ce qui est optionnel dans une déclaration de fonction?

- [ ] type de données des paramètres
- [ ] type de retour de la fonction
- [x] noms des paramètres
- [ ] nombre de paramètres

> **Explication:**  
> Dans toutes les normes C modernes, les noms de paramètres dans une déclaration de fonction sont optionnels.  
> Cependant, la signification d'une liste de paramètres vide (`int f();`) diffère selon la norme:
>
> - **Avant C23:** Déclare une fonction avec un nombre non spécifié de paramètres (pas un prototype).
> - **En C23:** Équivalent à `int f(void);` — déclare une fonction qui ne prend aucun paramètre.
>
> [Référence](https://en.cppreference.com/w/c/language/function_declaration)

#### Q14. C traite tous les périphériques, tels que l'écran et le clavier, comme des fichiers. Quel fichier s'ouvre automatiquement lorsqu'un programme s'exécute?

- [x] stdout
- [ ] stdio.h
- [ ] default.h
- [ ] string.h

#### Q15. Dans quel segment l'allocation de mémoire dynamique a-t-elle lieu?

- [ ] Segment BSS
- [ ] pile
- [x] tas
- [ ] segment de données

[Référence](http://www.it.uc3m.es/pbasanta/asng/course_notes/dynamic_memory_heap_en.html#:~:text=The%20dynamic%20memory%20that%20is,reads%20a%20set%20of%20words.)

#### Q16. Quelle fonction utilisez-vous pour désallouer de la mémoire?

- [ ] dalloc()
- [ ] dealloc()
- [ ] release()
- [x] free()

[Référence](https://devdocs.io/c/memory/free)

[Référence](https://www.tutorialspoint.com/c_standard_library/c_function_free.htm)

#### Q17. En langage C, quels sont les blocs de construction de base qui sont construits ensemble pour écrire un programme?

- [ ] mots-clés
- [ ] identificateurs
- [x] jetons
- [ ] fonctions

[Référence](https://fresh2refresh.com/c-programming/c-tokens-identifiers-keywords/#:~:text=C%20tokens%20are%20the%20basic,are%20known%20as%20C%20tokens.)

#### Q18. Quand la mémoire pour une variable est-elle allouée?

- [ ] lors de l'affectation de la variable
- [ ] lors de l'initialisation de la variable
- [x] lors de la déclaration de la variable
- [ ] lors de la définition de la variable

[Référence](https://www.codingame.com/playgrounds/14589/how-to-play-with-pointers-in-c/dynamic-memory-allocation#:~:text=When%20a%20variable%20is%20declared,allocation%20or%20dynamic%20memory%20allocation.)

#### Q19. C utilise la méthode d'appel par valeur pour passer des arguments aux fonctions. Comment pouvez-vous invoquer la méthode d'appel par référence?

- [x] en utilisant des pointeurs
- [ ] en déclarant les fonctions séparément de leur définition
- [ ] en utilisant des fonctions récursives
- [ ] en utilisant des variables globales

[Référence](https://www.javatpoint.com/call-by-value-and-call-by-reference-in-c)

#### Q20. Une union vous permet de stocker différents `___` dans le même `___`.

- [ ] Objets; Structure
- [ ] Variables; Déclaration
- [x] Types de données; Espace mémoire
- [ ] Tableaux; Fichier d'en-tête

#### Q21. Quelle est la sortie de ce programme?

```c
main() {
    char c1='a' , c2='A';
    int i=c2-c1;
    printf("%d", i);
}
```

- [ ] 32
- [ ] Erreur d'exécution
- [x] -32
- [ ] 0

#### Q22. Quelle est la différence entre les fonctions scanf() et sscanf()?

- [ ] La fonction scanf() lit des données formatées sous forme de chaîne; La fonction sscanf() lit une entrée de chaîne depuis l'écran.
- [x] La fonction scanf() lit des données formatées depuis le clavier; La fonction sscanf() lit une entrée formatée depuis une chaîne.
- [ ] La fonction scanf() lit des données de chaîne depuis le clavier; La fonction sscanf() lit des données de chaîne depuis une chaîne.
- [ ] La fonction scanf() lit des données formatées depuis un fichier; La fonction sscanf() lit une entrée depuis une chaîne sélectionnée

#### Q23. Quelle n'est pas une commande valide avec cette déclaration?

```c
char *string[20] = { "one", "two", "three"};
```

- [ ] `printf("%c", string[1][2]);`
- [x] `printf("%s", string[1][2]);`
- [ ] `printf("%s", string[1]);`
- [ ] `printf(string[1]);`

#### Q24. À quoi l'expression player->name est-elle équivalente?

- [ ] `player.name`
- [x] `(*player).name`
- [ ] `*player.name`
- [ ] `player.*name`

#### Q25. Quel programme se compilera et s'exécutera sans erreurs?

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

#### Q26. Que retourne cet appel de fonction?

```c
1 main() { float x = f1(10, 5); }
2 float f1(int a, int b) { return (a/b); }
```

- [ ] 2
- [ ] 2.000000
- [ ] une erreur d'exécution
- [x] une erreur de compilation

#### Q27. Que crée ce programme?

```c
#include <stdio.h>
int main() {
    int *p = NULL;
    return 0;
}
```

- [ ] une erreur d'exécution
- [x] un pointeur NULL
- [ ] une erreur de compilation
- [ ] un pointeur void

#### Q28. Quelle est une manière alternative d'écrire l'expression (\*x).y?

- [ ] Il n'y a pas d'équivalent.
- [x] x->y
- [ ] \*x->y
- [ ] y->x

#### Q29. Les erreurs de compilation sont des erreurs statiques qui peuvent être trouvées dans le code.

- [x] dans les déclarations et les définitions
- [ ] dans les fonctions et les expressions
- [ ] dans la syntaxe et la sémantique
- [ ] dans les objets et les instructions

#### Q30. L'entrée et la sortie de fichiers (E/S) en C sont fortement basées sur la façon dont cela est fait `___`?

- [x] sous Unix
- [ ] en C++
- [ ] en C#
- [ ] sous DOS

#### Q31. Que retourne la fonction strcmp(str1, str2);?

- [x] 0 si str1 et str2 sont identiques, un nombre négatif si str1 est inférieur à str2, un nombre positif si str1 est supérieur à str2
- [ ] vrai (1) si str1 et str2 sont identiques, faux (0) si str1 et str2 ne sont pas identiques
- [ ] vrai (1) si str1 et str2 sont identiques, NULL si str1 et str2 ne sont pas identiques
- [ ] 0 si str1 et str2 sont identiques, un nombre négatif si str2 est inférieur à str1, un nombre positif si str2 est supérieur à str1

#### Q32. Quelle est la sortie de ce programme?

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

#### Q33. Quelle n'est _pas_ une manière correcte de déclarer une variable de chaîne?

- [ ] `char *string = "Hello World";`
- [x] `char string = "Hello World";`
- [ ] `char string[20] = {'H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd'};`
- [ ] `char string[] = "Hello World";`

#### Q34. Quel choix est un garde d'inclusion pour le fichier d'en-tête mylib.h?

- [ ] :

```c
#ifdef MYLIB_H
#undef MYLIB_H

// contenu de mylib.h

#endif /* MYLIB_H */
```

- [x] :

```c
#ifndef MYLIB_H
#define MYLIB_H

// contenu de mylib.h

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

// contenu de mylib.h

#endif /* MYLIB_H */
```

#### Q35. Combien de fois le code à l'intérieur de la boucle while est-il exécuté dans ce programme?

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

#### Q36. L'entrée et la sortie de fichiers (E/S) en C se font à travers quoi?

- [ ] composants basés sur la syntaxe
- [ ] interfaces natives
- [ ] objets système
- [x] appels de fonction

#### Q37. Les directives sont traduites par le?

- [x] Préprocesseur
- [ ] Compilateur
- [ ] Éditeur de liens
- [ ] Éditeur

#### Q38. Les principales structures de boucle en programmation C sont la boucle for, la boucle while, et quelle autre boucle?

- [x] do...while
- [ ] for...in
- [ ] repeat...until
- [ ] do...until

#### Q39. Par défaut, les fonctions C sont de quel type de fonctions?

- [x] globales
- [ ] statiques
- [ ] bibliothèque
- [ ] système

#### Q40. Vous avez écrit une fonction que vous souhaitez inclure en tant que membre de la structure 'a'. Comment un tel membre de structure est-il défini?

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

#### Q41. Une structure de données de pile permet toutes les opérations de données à une seule extrémité, ce qui en fait quel type d'implémentation?

- [ ] FIFO
- [x] LIFO
- [ ] LILO
- [ ] LOLI

#### Q42. Qu'affiche ce programme?

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

#### Q43. Décrivez la relation entre lvalue et rvalue.

- [ ] Une lvalue peut apparaître uniquement du côté gauche d'une affectation; une rvalue peut apparaître uniquement du côté droit.
- [ ] Une lvalue peut apparaître uniquement du côté gauche d'une affectation; une rvalue peut apparaître du côté gauche ou droit.
- [ ] Une lvalue et une rvalue peuvent apparaître du côté gauche ou droit d'une affectation.
- [x] Une lvalue peut apparaître du côté gauche ou droit d'une affectation; une rvalue peut apparaître uniquement du côté droit.

#### Q44. Quel opérateur est utilisé pour accéder à l'adresse d'une variable?

- [ ] `%`
- [ ] `**`
- [ ] `*`
- [x] `&`

#### Q45. Quelle fonction add retourne correctement la valeur mise à jour du résultat?

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

#### Q46. Considérez les nombres de la série de Fibonacci inférieurs à 100 : 0,1,1,2,3,5,8,13,21,34,55,89. Quel morceau de code affiche la séquence?

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

#### Q47. Lequel n'est _pas_ un spécificateur de classe de stockage?

- [x] `intern`
- [ ] `extern`
- [ ] `register`
- [ ] `static`

[Référence](https://en.cppreference.com/w/cpp/language/storage_duration)

#### Q48. Quelle ligne de code, après exécution, donne à `i` la valeur de 1?

- [ ] `for(i=1; i<=1; i++);`
- [ ] `for(i=1; i=10; i++);`
- [x] `for(i=1; i==10; i++);`
- [ ] `for(i=10; i>=1; i--);`

#### Q49. Quelle est la valeur de la variable c à la fin de ce programme?

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

#### Q50. Lequel n'est _pas_ l'un des types de données de base en C?

- [ ] long double
- [ ] unsigned char
- [x] array (tableau)
- [ ] float

#### Q51. Quel est l'opérateur d'accès aux membres pour une structure?

- [ ] ,
- [ ] []
- [x] .
- [ ] :

#### Q52. Quel type de données standard fournit la plus petite taille de stockage et peut être utilisé dans les calculs?

- [x] char
- [ ] float
- [ ] int
- [ ] short

#### Q53. Que fait la fonction ctype tolower()?

- [ ] Elle retourne TRUE pour les lettres minuscules de l'alphabet.
- [ ] Elle garantit que la sortie de texte utilise uniquement des valeurs ASCII (0 à 127).
- [ ] Elle retourne FALSE pour les lettres minuscules de l'alphabet.
- [x] Elle convertit une lettre majuscule de l'alphabet en minuscule.

#### Q54. Le pointeur void _vptr_ est affecté à l'adresse de la variable float _g_. Quelle est une manière valide de déréférencer _vptr_ pour affecter sa valeur pointée à une variable float nommée _f_ plus tard dans le programme?

```c
float g;
void *vptr=&g;
```

- [ ] `f=(float *)vptr;`
- [x] `f=*(float *)vptr;`
- [ ] `f=*(float)vptr;`
- [ ] `f=(float)*vptr;`

#### Q55. Les fonctions d'allocation de mémoire dynamique sont définies dans quel fichier d'en-tête système?

- [ ] stdio.h
- [x] stdlib.h
- [ ] limits.h
- [ ] stddef.h

#### Q56. Une fonction est un ensemble d'**\_**.

- [ ] déclarations
- [x] instructions
- [ ] variables
- [ ] objets

#### Q57. En quoi les fonctions statiques diffèrent-elles des fonctions globales?

- [ ] Les fonctions statiques doivent être déclarées à l'avance avant d'être définies.
- [ ] Les fonctions statiques doivent être déclarées dans un fichier d'en-tête séparé.
- [ ] Les fonctions statiques retournent toujours la même valeur.
- [x] Les fonctions statiques ne peuvent être accessibles que dans le fichier où elles sont déclarées.

#### Q58. Quel exemple de code crée la chaîne "Hello Mars" dans le tampon de stockage `hello`?

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

#### Q59. Si vous utilisez la fonction fopen() avec le mode "a", que se passe-t-il si le fichier nommé n'existe pas?

- [ ] Le fichier est créé et ouvert en lecture.
- [x] Le fichier est créé et ouvert en écriture.
- [ ] La fonction fopen() retourne NULL indiquant que l'opération a échoué.
- [ ] Le fichier est créé et ouvert en écriture et en lecture

[Référence](https://www.tutorialspoint.com/c_standard_library/c_function_fopen.htm)

#### Q60. Que retourne cette fonction?

```c
int fl(int a, int b) { return(a>b?a:b); }
```

- [ ] erreur de compilateur
- [ ] la plus petite valeur des deux paramètres passés
- [ ] erreur d'exécution
- [x] la plus grande valeur des deux paramètres passés

#### Q61. Quelle option est un nom de fonction valide?

- [x] draw_star()
- [ ] 5times()
- [ ] upper-limit()
- [ ] auto()

#### Q62. Quelle n'est pas une définition de type valide d'une structure qui contient des coordonnées x et y sous forme d'entiers, et qui peut être utilisée comme indiqué pour la variable nommée point?

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

#### Q63. Quelle est la sortie du programme ci-dessous?

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
- [ ] 3 ou 5 selon l'entrée
- [ ] Erreur de compilation

#### Q64. Qu'allouent les fonctions malloc() et calloc()?

- [ ] mémoire réallouée
- [ ] mémoire statique
- [x] mémoire dynamique
- [ ] mémoire fragmentée

[Calloc](https://devdocs.io/c/memory/calloc)
[Malloc](https://devdocs.io/c/memory/malloc)

#### Q65. Vous devez déterminer si une variable de chaîne est une sous-chaîne d'une autre chaîne. Quelle fonction de bibliothèque C standard utilisez-vous?

- [ ] substr(str1, str2);
- [x] strstr(str1, str2);
- [ ] substring(str1, str2);
- [ ] strspn(str1, str2);

[Référence](https://devdocs.io/c/string/byte/strstr)

#### Q66. Trouvez la sortie du programme.

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

[Référence](https://www.geeksforgeeks.org/left-shift-right-shift-operators-c-cpp/)

#### Q67. Prédisez la sortie du code suivant lorsque les variables **entières** x est initialisée à 10, y à 2, et z à 0.

```c
z = x + y * x + 10 / 2 * x;
printf("value is =%d",z);
```

- [x] 80
- [ ] 170
- [ ] 31.5
- [ ] 6

[Référence](https://www.informit.com/articles/article.aspx?p=2062174&seqNum=4)

#### Q68. Quelle sera la sortie de l'extrait de code suivant?

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

#### Q69. Quelle est la sortie de ce programme?

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

#### Q70. Qu'est-ce que le caractère \0?

- [ ] Chaîne
- [x] Caractère NULL
- [ ] ZÉRO
- [ ] Variable

[Référence](<https://www.youth4work.com/Talent/C-Language/Forum/117150-what-is-the-use-of-a-0-character-in-c-language#:~:text=by%20using%20of%20null%20character(%27%5C0%27)%20it%20terminates%20the%20string%20untill%20the%20null%20character%20hit...%20which%20means%20comes%20out%20of%20the%20loop...%20In%20strings%20by%20default%20takes%20the%20null%20charater>)

#### Q71. Quelle est la sortie correcte pour le code suivant?

```c
#include<stdio.h>
#include<conio.h>
main()
{
     int a=10, b=20;
     clrscr();
     printf("Avant l'échange a=%d b=%d",a,b);
     a=a+b;
     b=a-b;
     a=a-b;
     printf("\nAprès l'échange a=%d b=%d",a,b);
     getch();
}
```

- [ ] Avant a=10 b=20 , Après a=10 b=10
- [ ] Avant a=10 b=10 , Après a=20 b=10
- [ ] Avant a=10 b=20 , Après a=20 b=20
- [x] Avant a=10 b=20 , Après a=20 b=10

#### Q72. Quelle est l'option incorrecte qui explique la directive #pragma?

- [ ] #pragma exit nous permet de spécifier des fonctions appelées à la sortie du programme.
- [ ] Il s'agit d'une directive de préprocesseur qui peut être utilisée pour activer ou désactiver certaines fonctionnalités.
- [x] #pragma startup ne permet pas de spécifier des fonctions appelées au démarrage du programme.
- [ ] Elle est de deux types : #pragma startup, #pragma exit et pragma warn.

#### Q73. Quelle sera la sortie de l'extrait de code suivant?

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

#### Q74. Quelle sera la sortie de l'extrait de code suivant?

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
- [ ] Erreur de compilation
- [ ] 82 19
- [ ] Aucune de ces réponses

#### Q75. Quelle est la sortie de l'extrait de code suivant?

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

#### Q76. Que signifie la déclaration suivante?

```
int (*ptr)[10];
```

- [ ] ptr est un tableau de pointeurs vers 10 entiers
- [x] ptr est un pointeur vers un tableau de 10 entiers
- [ ] ptr est un tableau de 10 entiers
- [ ] ptr est un pointeur vers un tableau

#### Q77. Quelle sera la sortie de l'extrait de code suivant?

```c
#include <stdio.h>
void change(int,int);
int main()
{
   int a=10,b=20;
   change(a,b); //appel d'une fonction en passant les valeurs des variables.
   printf("Valeur de a est: %d",a);
   printf("\n");
   printf("Valeur de b est: %d",b);
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

**Explication:** La fonction "change" changera la valeur de x et y uniquement dans sa propre portée, donc a et b ne sont pas affectés.

#### Q78. Choisissez vrai ou faux. Lorsqu'une variable est créée en C, une adresse mémoire est attribuée à la variable.

- [x] Vrai
- [ ] Faux

#### Q79. Qu'affiche le fragment de programme C suivant?

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

**Explication:** char c[ ] = "GATE2011"; puisque char \*p =c cela signifie que p représente l'adresse de base de la chaîne "GATE2011" DONC p[3] est 'E' et p[1] est 'A'. La valeur de la sous-expression p[3] – p[1] = valeur ASCII de 'E' – valeur ASCII de 'A' = 4. Donc l'expression p + p[3] – p[1] devient (p + 4) Et (p+4) représente l'adresse de base de la chaîne "2011" printf("%s", p + p[3] – p[1]) ; Donc cela affichera 2011

#### Q80. Quelle est la sortie de l'extrait de code suivant?

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

#### Q81. Quelle sera la sortie du segment de programme C suivant?

```c
char inchar = 'A';
switch (inchar)
{
case 'A' :
	printf ("choix A \n") ;
case 'B' :
	printf ("choix B ") ;
case 'C' :
case 'D' :
case 'E' :
default:
	printf ("Pas de choix") ;
}

```

- [ ] Pas de choix
- [ ] Choix A
- [x] Choix A
      Choix B Pas de choix
- [ ] Le programme ne donne aucune sortie car il est erroné

#### Q82. La variable de chaîne str1 a la valeur "abc", et la variable de chaîne str2 a la valeur "xyz". Quelles sont les valeurs de str1 et str2 après l'exécution de cette instruction?

```c
strcpy(str1, str2);
```

- [x] str1: "xyz" ; str2: "xyz"
- [ ] str1: "abc" ; str2: "xyz"
- [ ] str1: "xyz" ; str2: "abc"
- [ ] str1: "abc" ; str2: "abc"

#### Q88. Quelle n'est pas une commande valide avec cette déclaration?

```c
char *string[20] = { "one", "two", "three"};
```

- [ ] `printf("%c", string[1][2]);`
- [x] `printf("%s", string[1][2]);`
- [ ] `printf("%s", string[1]);`
- [ ] `printf(string[1]);`

#### Q89. Quelle est la sortie de ce code?

```c
int x = 5;
int y = ++x + x++;
printf("%d %d", x, y);
```

- [ ] 6 11
- [x] 7 12
- [ ] 7 11
- [ ] 6 12

**Explication:**
D'abord, ++x incrémente x à 6 et utilise 6 dans l'expression. Ensuite x++ utilise 6 et incrémente x à 7 après. Donc y = 6 + 6 = 12, et x devient 7.

[Référence](https://en.cppreference.com/w/c/language/operator_precedence)

#### Q90. Qu'indique le mot-clé `volatile` en C?

- [ ] La variable ne peut pas être modifiée
- [x] La variable peut être modifiée par des facteurs externes
- [ ] La variable est stockée en ROM
- [ ] La variable est une constante

**Explication:**
Le mot-clé `volatile` indique au compilateur que la valeur d'une variable peut être modifiée par des facteurs externes (matériel, interruptions, autres threads), donc le compilateur ne doit pas optimiser les lectures/écritures.

[Référence](https://en.cppreference.com/w/c/language/volatile)

#### Q91. Quel est le but du mot-clé `restrict` en C99?

- [x] Indiquer qu'un pointeur est le seul moyen d'accéder à un objet
- [ ] Restreindre la portée d'une variable
- [ ] Empêcher la modification d'une variable
- [ ] Restreindre l'accès aux fonctions

**Explication:**
Le mot-clé `restrict` est un qualificateur de type qui peut être appliqué aux pointeurs. Il indique au compilateur que pendant la durée de vie du pointeur, seul lui ou une valeur directement dérivée de lui sera utilisé pour accéder à l'objet vers lequel il pointe. Cela permet certaines optimisations du compilateur.

[Référence](https://en.cppreference.com/w/c/language/restrict)

#### Q92. Quelle est la différence entre `malloc()` et `calloc()`?

- [ ] malloc est plus rapide que calloc
- [x] calloc initialise la mémoire allouée à zéro, malloc ne le fait pas
- [ ] malloc peut allouer plus de mémoire que calloc
- [ ] Il n'y a pas de différence

**Explication:**
`calloc()` alloue de la mémoire et initialise tous les octets à zéro, tandis que `malloc()` alloue de la mémoire mais la laisse non initialisée. `calloc()` prend également deux arguments (nombre d'éléments et taille de chaque élément) tandis que `malloc()` en prend un (taille totale en octets).

[Référence](https://en.cppreference.com/w/c/memory/calloc)

#### Q93. Qu'est-ce qu'un pointeur pendant?

- [ ] Un pointeur qui pointe vers NULL
- [x] Un pointeur qui pointe vers de la mémoire libérée ou supprimée
- [ ] Un pointeur qui n'a pas été initialisé
- [ ] Un pointeur qui pointe vers une constante

**Explication:**
Un pointeur pendant est un pointeur qui pointe vers de la mémoire qui a été libérée ou supprimée. L'accès à un tel pointeur conduit à un comportement indéfini.

[Référence](https://en.wikipedia.org/wiki/Dangling_pointer)

#### Q94. Quelle est la sortie de ce code?

```c
int arr[] = {1, 2, 3, 4, 5};
printf("%d", *(arr + 3));
```

- [ ] 1
- [ ] 2
- [ ] 3
- [x] 4

**Explication:**
`arr` est un pointeur vers le premier élément. `arr + 3` pointe vers le 4ème élément (indice 3). L'opérateur `*` le déréférence pour obtenir la valeur 4.

[Référence](https://en.cppreference.com/w/c/language/operator_member_access)

#### Q95. Que fait le mot-clé `static` lorsqu'il est appliqué à une fonction?

- [x] Limite la portée de la fonction au fichier actuel
- [ ] Rend la fonction plus rapide
- [ ] Empêche la fonction d'être appelée
- [ ] Rend la fonction en ligne

**Explication:**
Lorsque `static` est appliqué à une fonction, il limite la liaison de la fonction à une liaison interne, ce qui signifie qu'elle ne peut être appelée que depuis la même unité de traduction (fichier source).

[Référence](https://en.cppreference.com/w/c/language/storage_duration)

#### Q96. Quelle est la taille d'un pointeur dans un système 64 bits?

- [ ] 4 octets
- [x] 8 octets
- [ ] 16 octets
- [ ] Dépend de ce vers quoi il pointe

**Explication:**
Sur un système 64 bits, les pointeurs font généralement 8 octets (64 bits) quelle que soit la cible vers laquelle ils pointent. La taille est déterminée par l'architecture du système, pas par le type pointé.

[Référence](https://en.cppreference.com/w/c/language/pointer)

#### Q97. Quel est le but de `typedef`?

- [ ] Définir un nouveau type de données
- [x] Créer un alias pour un type de données existant
- [ ] Déclarer une variable
- [ ] Définir une macro

**Explication:**
`typedef` crée un alias (nom alternatif) pour un type de données existant. Il ne crée pas un nouveau type, juste un nouveau nom pour un type existant.

[Référence](https://en.cppreference.com/w/c/language/typedef)

#### Q98. Qu'est-ce qu'une fuite mémoire?

- [ ] Lorsqu'un pointeur pointe vers une mémoire invalide
- [x] Lorsque la mémoire allouée n'est pas libérée
- [ ] Lorsqu'une variable sort de la portée
- [ ] Lorsqu'un débordement de pile se produit

**Explication:**
Une fuite mémoire se produit lorsque de la mémoire allouée dynamiquement (via `malloc`, `calloc`, etc.) n'est pas libérée en utilisant `free()`, ce qui fait que le programme consomme de plus en plus de mémoire au fil du temps.

[Référence](https://en.wikipedia.org/wiki/Memory_leak)

#### Q99. Quelle est la sortie de ce code?

```c
int x = 10;
int *p = &x;
*p = 20;
printf("%d", x);
```

- [ ] 10
- [x] 20
- [ ] Adresse de x
- [ ] Indéfini

**Explication:**
`p` pointe vers `x`. `*p = 20` modifie la valeur à l'adresse vers laquelle p pointe, qui est `x`. Donc `x` devient 20.

[Référence](https://en.cppreference.com/w/c/language/pointer)

#### Q100. Que retourne toujours `sizeof(char)` en C?

- [x] 1
- [ ] 2
- [ ] 4
- [ ] Dépend du système

**Explication:**
Par définition dans la norme C, `sizeof(char)` vaut toujours 1. C'est l'unité fondamentale de taille en C, et toutes les autres tailles en sont des multiples.

[Référence](https://en.cppreference.com/w/c/language/sizeof)

#### Q101. Quelle est la différence entre `++i` et `i++`?

- [x] ++i incrémente avant utilisation, i++ incrémente après utilisation
- [ ] ++i est plus rapide que i++
- [ ] i++ ne peut être utilisé que dans les boucles
- [ ] Il n'y a pas de différence

**Explication:**
`++i` (pré-incrémentation) incrémente la variable et retourne la nouvelle valeur. `i++` (post-incrémentation) retourne la valeur actuelle puis incrémente la variable.

[Référence](https://en.cppreference.com/w/c/language/operator_incdec)

#### Q102. Qu'est-ce qu'une erreur de segmentation?

- [ ] Une erreur de syntaxe
- [x] Une erreur causée par l'accès à une mémoire invalide
- [ ] Une erreur de compilation
- [ ] Un avertissement

**Explication:**
Une erreur de segmentation (segfault) se produit lorsqu'un programme tente d'accéder à une mémoire qu'il n'est pas autorisé à accéder, comme déréférencer un pointeur NULL ou accéder à de la mémoire libérée.

[Référence](https://en.wikipedia.org/wiki/Segmentation_fault)

#### Q103. Quel est le but du mot-clé `const` avec les pointeurs?

```c
const int *p;
```

- [x] La valeur pointée ne peut pas être modifiée via p
- [ ] Le pointeur p ne peut pas être modifié
- [ ] Le pointeur et la valeur sont tous deux constants
- [ ] Cela n'a aucun effet

**Explication:**
`const int *p` signifie que p pointe vers un entier constant - vous ne pouvez pas modifier la valeur via p, mais vous pouvez changer l'endroit où p pointe. Pour `int * const p`, le pointeur lui-même est constant.

[Référence](https://en.cppreference.com/w/c/language/const)

#### Q104. Quelle est la sortie de ce code?

```c
int arr[5] = {1, 2, 3};
printf("%d", arr[4]);
```

- [x] 0
- [ ] 3
- [ ] Valeur aléatoire
- [ ] Erreur de compilation

**Explication:**
Lorsqu'un tableau est partiellement initialisé, les éléments restants sont automatiquement initialisés à 0. Donc arr[3] et arr[4] sont tous deux 0.

[Référence](https://en.cppreference.com/w/c/language/array_initialization)

#### Q105. Que fait le mot-clé `extern`?

- [ ] Rend une variable externe au programme
- [x] Déclare une variable définie ailleurs
- [ ] Exporte une variable vers d'autres programmes
- [ ] Crée une variable globale

**Explication:**
`extern` déclare une variable ou une fonction définie dans un autre fichier source ou plus tard dans le même fichier. Il indique au compilateur que la définition existe ailleurs.

[Référence](https://en.cppreference.com/w/c/language/extern)

#### Q106. Quelle est la différence entre `struct` et `union`?

- [x] Les membres de struct ont une mémoire séparée, les membres de union partagent la mémoire
- [ ] struct est plus rapide que union
- [ ] union peut avoir plus de membres que struct
- [ ] Il n'y a pas de différence

**Explication:**
Dans une `struct`, chaque membre a son propre emplacement mémoire. Dans une `union`, tous les membres partagent le même emplacement mémoire, et un seul membre peut contenir une valeur à la fois. La taille d'une union est la taille de son plus grand membre.

[Référence](https://en.cppreference.com/w/c/language/union)

#### Q107. Quelle est la sortie de ce code?

```c
int x = 5;
printf("%d", x << 2);
```

- [ ] 5
- [ ] 7
- [x] 20
- [ ] 10

**Explication:**
L'opérateur `<<` est un décalage de bits vers la gauche. `x << 2` décale les bits de x vers la gauche de 2 positions, ce qui équivaut à multiplier par 2^2 = 4. Donc 5 \* 4 = 20.

[Référence](https://en.cppreference.com/w/c/language/operator_arithmetic)

#### Q108. Qu'est-ce qu'un pointeur de fonction?

- [ ] Un pointeur vers la valeur de retour d'une fonction
- [x] Un pointeur qui stocke l'adresse d'une fonction
- [ ] Une fonction qui retourne un pointeur
- [ ] Un pointeur à l'intérieur d'une fonction

**Explication:**
Un pointeur de fonction est une variable qui stocke l'adresse d'une fonction. Il peut être utilisé pour appeler la fonction indirectement ou passer des fonctions comme arguments à d'autres fonctions.

[Référence](https://en.cppreference.com/w/c/language/pointer#Pointers_to_functions)

#### Q109. Que représente `NULL` en C?

- [ ] Le nombre zéro
- [x] Une constante de pointeur nul
- [ ] Une chaîne vide
- [ ] Une valeur indéfinie

**Explication:**
`NULL` est une macro qui représente une constante de pointeur nul. Elle est généralement définie comme `((void*)0)` ou simplement `0`. Elle indique qu'un pointeur ne pointe vers aucun emplacement mémoire valide.

[Référence](https://en.cppreference.com/w/c/types/NULL)

#### Q110. Quelle est la sortie de ce code?

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

**Explication:**
`*p1 = *p2` copie la valeur pointée par p2 (qui est 20) vers l'emplacement pointé par p1 (qui est x). Donc x devient 20, y reste 20.

[Référence](https://en.cppreference.com/w/c/language/pointer)

#### Q111. Quel est le but de la directive `#pragma`?

- [ ] Inclure des fichiers d'en-tête
- [ ] Définir des macros
- [x] Fournir des instructions spécifiques au compilateur
- [ ] Déclarer des variables

**Explication:**
`#pragma` est une directive de préprocesseur qui fournit des informations supplémentaires au compilateur. Elle est définie par l'implémentation et utilisée pour des fonctionnalités spécifiques au compilateur.

[Référence](https://en.cppreference.com/w/c/preprocessor/impl)

#### Q112. Quelle est la différence entre `break` et `continue`?

- [x] break sort de la boucle, continue passe à l'itération suivante
- [ ] break est plus rapide que continue
- [ ] continue sort de la boucle, break saute l'itération
- [ ] Il n'y a pas de différence

**Explication:**
`break` termine complètement la boucle et continue l'exécution après la boucle. `continue` saute le reste de l'itération actuelle et passe à l'itération suivante de la boucle.

[Référence](https://en.cppreference.com/w/c/language/break)

#### Q113. Quelle est la sortie de ce code?

```c
int arr[] = {1, 2, 3, 4, 5};
printf("%d", sizeof(arr) / sizeof(arr[0]));
```

- [ ] 4
- [x] 5
- [ ] 20
- [ ] 1

**Explication:**
`sizeof(arr)` donne la taille totale du tableau en octets. `sizeof(arr[0])` donne la taille d'un élément. Les diviser donne le nombre d'éléments : 5.

[Référence](https://en.cppreference.com/w/c/language/sizeof)

#### Q114. Qu'est-ce qu'un pointeur void?

- [ ] Un pointeur qui ne pointe vers rien
- [x] Un pointeur générique qui peut pointer vers n'importe quel type de données
- [ ] Un pointeur vers des fonctions void
- [ ] Un pointeur invalide

**Explication:**
Un pointeur `void*` est un pointeur générique qui peut pointer vers n'importe quel type de données. Il doit être converti vers le type approprié avant le déréférencement.

[Référence](https://en.cppreference.com/w/c/language/pointer)

#### Q115. Que suggère le mot-clé `register` au compilateur?

- [ ] Rendre une variable globale
- [x] Stocker une variable dans un registre CPU pour un accès plus rapide
- [ ] Protéger une variable contre la modification
- [ ] Allouer de la mémoire sur le tas

**Explication:**
Le mot-clé `register` suggère (mais ne garantit pas) que le compilateur devrait stocker la variable dans un registre CPU pour un accès plus rapide. Les compilateurs modernes ignorent souvent cet indice et prennent leurs propres décisions d'optimisation.

[Référence](https://en.cppreference.com/w/c/language/storage_duration)

#### Q116. Quelle est la sortie de ce code?

```c
int x = 5;
int y = (x > 3) ? 10 : 20;
printf("%d", y);
```

- [x] 10
- [ ] 20
- [ ] 5
- [ ] 3

**Explication:**
C'est l'opérateur ternaire. Puisque x > 3 est vrai, y reçoit la valeur 10.

[Référence](https://en.cppreference.com/w/c/language/operator_other)

#### Q117. Quelle est la différence entre `malloc()` et `realloc()`?

- [ ] malloc est plus rapide que realloc
- [x] realloc redimensionne la mémoire précédemment allouée
- [ ] malloc initialise la mémoire, realloc ne le fait pas
- [ ] Il n'y a pas de différence

**Explication:**
`malloc()` alloue une nouvelle mémoire. `realloc()` modifie la taille d'un bloc de mémoire précédemment alloué, le déplaçant potentiellement vers un nouvel emplacement si nécessaire.

[Référence](https://en.cppreference.com/w/c/memory/realloc)

#### Q118. Qu'est-ce qu'une énumération en C?

- [ ] Une construction de boucle
- [x] Un type défini par l'utilisateur consistant en constantes entières nommées
- [ ] Une fonction qui compte les éléments
- [ ] Un tableau de constantes

**Explication:**
Une énumération (`enum`) est un type défini par l'utilisateur qui consiste en un ensemble de constantes entières nommées. Elle rend le code plus lisible en donnant des noms significatifs aux valeurs entières.

[Référence](https://en.cppreference.com/w/c/language/enum)

#### Q119. Quelle est la sortie de ce code?

```c
int x = 10;
int y = x++ + ++x;
printf("%d %d", x, y);
```

- [ ] 11 21
- [x] 12 22
- [ ] 12 21
- [ ] 11 22

**Explication:**
D'abord, x++ utilise 10 et incrémente x à 11. Ensuite ++x incrémente x à 12 et utilise 12. Donc y = 10 + 12 = 22, et x vaut 12.

[Référence](https://en.cppreference.com/w/c/language/operator_incdec)

#### Q120. Quel est le but de la macro `assert()`?

- [ ] Affecter des valeurs aux variables
- [x] Vérifier les hypothèses et terminer si faux
- [ ] Affirmer la dominance sur d'autres fonctions
- [ ] Créer des assertions dans la documentation

**Explication:**
`assert()` est une macro utilisée pour le débogage. Elle vérifie si une condition est vraie. Si elle est fausse, elle affiche un message d'erreur et termine le programme. Elle est généralement désactivée dans les versions de production.

[Référence](https://en.cppreference.com/w/c/error/assert)

#### Q121. Quelle est la différence entre `fgets()` et `gets()`?

- [ ] fgets est plus rapide que gets
- [x] fgets est plus sûr car il limite la taille de l'entrée
- [ ] gets peut lire depuis n'importe quel fichier
- [ ] Il n'y a pas de différence

**Explication:**
`gets()` n'est pas sûr car il ne vérifie pas la taille du tampon, ce qui entraîne des vulnérabilités de débordement de tampon. `fgets()` vous permet de spécifier le nombre maximum de caractères à lire, ce qui le rend plus sûr. `gets()` a été supprimé de la norme C11.

[Référence](https://en.cppreference.com/w/c/io/fgets)

#### Q122. Quelle est la sortie de ce code?

```c
int x = 5;
int *p = &x;
printf("%p %p", (void*)&x, (void*)p);
```

- [x] La même adresse affichée deux fois
- [ ] Deux adresses différentes
- [ ] Erreur de compilation
- [ ] 5 5

**Explication:**
`&x` donne l'adresse de x, et p stocke l'adresse de x. Les deux affichent la même adresse (en format hexadécimal en raison de %p).

[Référence](https://en.cppreference.com/w/c/io/fprintf)

#### Q123. Qu'est-ce qu'une directive de préprocesseur?

- [ ] Une fonction qui traite les données
- [x] Une instruction au préprocesseur avant la compilation
- [ ] Une directive du processeur
- [ ] Un type de boucle

**Explication:**
Les directives de préprocesseur (comme #include, #define, #ifdef) sont des instructions traitées avant la compilation réelle. Elles commencent par # et sont gérées par le préprocesseur.

[Référence](https://en.cppreference.com/w/c/preprocessor)

#### Q124. Quelle est la sortie de ce code?

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

**Explication:**
`arr[1][2]` accède à la ligne 1 (deuxième ligne: {4,5,6}), colonne 2 (troisième élément: 6).

[Référence](https://en.cppreference.com/w/c/language/array)

#### Q125. Quel est le but de la fonction `memset()`?

- [ ] Allouer de la mémoire
- [x] Remplir un bloc de mémoire avec une valeur spécifique
- [ ] Copier de la mémoire
- [ ] Libérer de la mémoire

**Explication:**
`memset()` remplit un bloc de mémoire avec une valeur d'octet spécifiée. Elle est couramment utilisée pour initialiser des tableaux ou des structures à zéro.

[Référence](https://en.cppreference.com/w/c/string/byte/memset)

#### Q126. Quelle est la différence entre `strcpy()` et `strncpy()`?

- [ ] strcpy est plus rapide
- [x] strncpy limite le nombre de caractères copiés
- [ ] strcpy peut copier n'importe quel type de données
- [ ] Il n'y a pas de différence

**Explication:**
`strcpy()` copie toute la chaîne y compris le terminateur nul. `strncpy()` copie au maximum n caractères, offrant une protection contre le débordement de tampon.

[Référence](https://en.cppreference.com/w/c/string/byte/strncpy)

#### Q127. Quelle est la sortie de ce code?

```c
int x = 10;
int y = 3;
printf("%d", x % y);
```

- [x] 1
- [ ] 3
- [ ] 0
- [ ] 10

**Explication:**
L'opérateur `%` est l'opérateur modulo. 10 % 3 donne le reste de 10 divisé par 3, qui est 1.

[Référence](https://en.cppreference.com/w/c/language/operator_arithmetic)

#### Q128. Qu'est-ce qu'une macro en C?

- [ ] Une grande fonction
- [x] Une directive de préprocesseur qui définit un fragment de code
- [ ] Un type de variable
- [ ] Une construction de boucle

**Explication:**
Une macro est définie en utilisant #define et représente un fragment de code qui est remplacé par le préprocesseur avant la compilation. Elle peut être une constante ou une construction de type fonction.

[Référence](https://en.cppreference.com/w/c/preprocessor/replace)

#### Q129. Quelle est la sortie de ce code?

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

**Explication:**
L'opérateur ternaire vérifie si x > y. Comme c'est faux (5 n'est pas supérieur à 10), z reçoit la valeur de y, qui est 10.

[Référence](https://en.cppreference.com/w/c/language/operator_other)

#### Q130. Quel est le but de la fonction `free()`?

- [ ] Libérer des ressources CPU
- [x] Désallouer de la mémoire allouée dynamiquement
- [ ] Libérer des variables de leur portée
- [ ] Effacer l'écran

**Explication:**
`free()` désalloue la mémoire qui a été précédemment allouée par `malloc()`, `calloc()` ou `realloc()`. C'est essentiel pour éviter les fuites mémoire.

[Référence](https://en.cppreference.com/w/c/memory/free)

#### Q131. Quelle est la sortie de ce code?

```c
char str[] = "Hello";
printf("%d", strlen(str));
```

- [ ] 6
- [x] 5
- [ ] 4
- [ ] Indéfini

**Explication:**
`strlen()` retourne la longueur de la chaîne en excluant le terminateur nul. "Hello" a 5 caractères.

[Référence](https://en.cppreference.com/w/c/string/byte/strlen)

#### Q132. Qu'est-ce qu'une variable statique à l'intérieur d'une fonction?

- [ ] Une variable qui ne peut pas changer
- [x] Une variable qui conserve sa valeur entre les appels de fonction
- [ ] Une variable stockée en ROM
- [ ] Une variable globale

**Explication:**
Une variable statique à l'intérieur d'une fonction conserve sa valeur entre les appels de fonction. Elle n'est initialisée qu'une seule fois et existe pendant toute la durée de vie du programme.

[Référence](https://en.cppreference.com/w/c/language/storage_duration)

#### Q133. Quelle est la sortie de ce code?

```c
int arr[] = {1, 2, 3, 4, 5};
int *p = arr + 2;
printf("%d", *p);
```

- [ ] 1
- [ ] 2
- [x] 3
- [ ] 4

**Explication:**
`arr + 2` pointe vers le troisième élément (indice 2). Le déréférencer avec `*p` donne la valeur 3.

[Référence](https://en.cppreference.com/w/c/language/operator_member_access)

#### Q134. Quelle est la différence entre `printf()` et `sprintf()`?

- [ ] printf est plus rapide
- [x] sprintf écrit dans une chaîne, printf écrit sur stdout
- [ ] sprintf ne peut imprimer que des chaînes
- [ ] Il n'y a pas de différence

**Explication:**
`printf()` écrit une sortie formatée sur stdout (console). `sprintf()` écrit une sortie formatée dans un tampon de chaîne de caractères.

[Référence](https://en.cppreference.com/w/c/io/fprintf)

#### Q135. Quelle est la sortie de ce code?

```c
int x = 5;
printf("%d", x & 3);
```

- [ ] 5
- [ ] 3
- [x] 1
- [ ] 8

**Explication:**
L'opérateur `&` est un ET bit à bit. 5 en binaire est 101, 3 est 011. 101 & 011 = 001 = 1.

[Référence](https://en.cppreference.com/w/c/language/operator_arithmetic)

#### Q136. Qu'est-ce qu'un garde d'en-tête?

- [ ] Une fonctionnalité de sécurité
- [x] Une construction de préprocesseur pour empêcher l'inclusion multiple
- [ ] Une fonction qui protège les en-têtes
- [ ] Un type de commentaire

**Explication:**
Les gardes d'en-tête (utilisant #ifndef, #define, #endif) empêchent un fichier d'en-tête d'être inclus plusieurs fois dans la même unité de compilation, ce qui causerait des erreurs de redéfinition.

[Référence](https://en.cppreference.com/w/c/preprocessor/conditional)

#### Q137. Quelle est la sortie de ce code?

```c
int x = 10;
int y = 20;
int *p = &x;
p = &y;
printf("%d", *p);
```

- [ ] 10
- [x] 20
- [ ] Adresse de x
- [ ] Adresse de y

**Explication:**
Initialement p pointe vers x. Ensuite `p = &y` fait pointer p vers y. `*p` déréférence p pour obtenir la valeur de y, qui est 20.

[Référence](https://en.cppreference.com/w/c/language/pointer)

#### Q138. Quel est le but de la fonction `memcpy()`?

- [ ] Allouer de la mémoire
- [x] Copier un bloc de mémoire de la source vers la destination
- [ ] Comparer des blocs de mémoire
- [ ] Libérer de la mémoire

**Explication:**
`memcpy()` copie n octets de la mémoire source vers la mémoire de destination. Elle est plus rapide que de copier élément par élément mais ne gère pas les régions de mémoire qui se chevauchent (utilisez `memmove()` pour cela).

[Référence](https://en.cppreference.com/w/c/string/byte/memcpy)

#### Q139. Quelle est la sortie de ce code?

```c
int x = 5;
printf("%d", x | 3);
```

- [ ] 3
- [ ] 5
- [x] 7
- [ ] 8

**Explication:**
L'opérateur `|` est un OU bit à bit. 5 en binaire est 101, 3 est 011. 101 | 011 = 111 = 7.

[Référence](https://en.cppreference.com/w/c/language/operator_arithmetic)

#### Q140. Quelle est la différence entre `strcmp()` et `strncmp()`?

- [ ] strcmp est sensible à la casse, strncmp ne l'est pas
- [x] strncmp compare uniquement les n premiers caractères
- [ ] strcmp est plus rapide
- [ ] Il n'y a pas de différence

**Explication:**
`strcmp()` compare des chaînes entières. `strncmp()` compare au maximum n caractères, ce qui est utile pour comparer des préfixes de chaînes ou limiter la longueur de comparaison.

[Référence](https://en.cppreference.com/w/c/string/byte/strncmp)
