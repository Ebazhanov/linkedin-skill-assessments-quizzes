## Bash

#### D1. Quale dei tre metodi copierà la directory denominata "photo dir" in modo ricorsivo dalla home directory dell'utente a /backups?

```bash
cp -R "~/photo dir" /backups #method1
cp -R ~"/photo dir" /backups #method2
cp -R ~/"photo dir" /backups #method3
```

- \[ ] Nessuno dei tre metodi si espanderà nella home directory dell'utente. Solo utilizzando `"$HOME/photo dir"`avrà successo.
- \[ ] Solo il metodo 1 si espanderà `"~/"` alla home directory dell'utente e quindi aggiungere il nome della directory tra virgolette che include uno spazio.
- \[ ] Solo il metodo 2 si espanderà `"~/"` alla home directory dell'utente e quindi aggiungere il nome della directory tra virgolette che include uno spazio.
- \[x] Solo il metodo 3 si espanderà `"~/"` alla home directory dell'utente e quindi aggiungere il nome della directory tra virgolette che include uno spazio.

#### D2. Se script.sh viene eseguito nella directory corrente, avrà esito negativo. Perché?

```bash
$ ls -1
Beach photo1.jpg
Photo1.jpg
Photo2.jpg
Script.sh

$ cat script.sh
for i in $(ls *.jpg); do
	mv $i ${i}.bak
done
```

- \[ ] ls: impossibile accedere a inesistentfile: Nessun file o directory di questo tipo
- \[x] Il ciclo for si dividerà sui confini delle parole e Beach photo1.jpg ha uno spazio al suo interno.
- \[ ] Il comando mv avrà esito negativo perché la parentesi graffa è un carattere speciale in Bash e non può essere utilizzata nei nomi dei file.
- \[ ] L'esecuzione di script.sh avrà esito positivo poiché il comando ls crea un elenco di file nella directory corrente e per i cicli attraverso tale elenco rinominando i file con un'estensione .bak.

#### D3. Per eseguire un comando copy in una subshell, quale sintassi useresti?

- \[x] `( command )`
- \[ ] `sh command`
- \[ ] `{ command; }`
- \[ ] `(( command ))`

#### D4. Usando "awk", quale sarebbe l'output di questa stringa di comando?

```bash
echo "1 2 3" | awk '{for (i=1; i<=NF; i++) s=s+$i};END {print s}'
```

- \[x] 6
- \[ ] 123
- \[ ] 3
- \[ ] 600

#### D5. Il comando seguente cercherà nel filesystem root i file denominati "finance.db". In questo contesto, quali informazioni vengono inviate a /dev/null?

```bash
find / -name "finance.db" 1>results.txt 2>/dev/null
```

- \[ ] i nomi dei file che non corrispondono alla finanza.db
- \[x] informazioni inviate all'errore standard, ad esempio errori visualizzati dal comando find durante l'esecuzione
- \[ ] i nomi dei file che corrispondono alla finanza.db
- \[ ] informazioni inviate all'output standard, ovvero il percorso dei file individuati dal comando find

#### D6. Per rimuovere definitivamente le righe vuote da un file chiamato file di testo, quale comando è possibile utilizzare?

- \[x] `sed -i '/^$/d' textfile`
- \[ ] `sed '/^$/d' textfile`
- \[ ] `cat textfile | sed '/^$/d`
- \[ ] `sed -i 's/^$//' textfile`

#### D7. Supponendo che user1 esista, quale sarebbe il risultato di questa stringa di comando?

```bash
awk -F: '/user1/{print $1 "-" $3 "-" $6}' /etc/passwd
```

- \[ ] Mostrerebbe il nome utente, l'UID e la home directory di user1 separati da due punti.
- \[ ] Stamperebbe l'UID, il GID e la home directory di user1 separati da trattini.
- \[ ] Stamperebbe l'UID, il commento e la home directory di user1 separati da trattini.
- \[x] Mostrerebbe il nome utente, l'UID e la home directory di user1 separati da trattini.

#### D8. Cosa succede se si utilizza il comando `"set -e"` in uno script Bash?

- \[ ] Causerà l'uscita di Bash se una funzione o una subshell restituisce un codice di stato diverso da zero.
- \[ ] Causerà l'uscita di Bash se un condizionale restituisce un codice di stato diverso da zero.
- \[ ] Causerà l'uscita di Bash se le assegnazioni locali, dichiarate o typeset restituiscono un codice di stato diverso da zero.
- \[x] Causerà l'uscita di Bash se un comando, un elenco di comandi, un comando composto o potenzialmente una pipeline restituisce un codice di stato diverso da zero.

#### D9. Le **\_** parola chiave mette in pausa lo script per ottenere input dall'input standard.

- \[ ] ottieni
- \[ ] argomento
- \[x] leggi
- \[ ] ingresso

#### D10. Se file.sql contiene istruzioni SQL da eseguire, cosa ci sarà in file.txt?

```bash
mysql < file.sql > file.txt
```

- \[ ] una copia del contenuto del file.sql
- \[ ] un errore che indica che si tratta di una sintassi non valida
- \[ ] l'output di errore del comando MySQL
- \[x] l'output non di errore del comando MySQL

**Nota:** controlla la domanda qui sotto per una variante.

#### D11. Quale sarà la differenza tra l'output sullo schermo e il contenuto di out.txt

```bash
mysql < file.sql > out.txt
```

- \[ ] L'output sullo schermo sarà identico a out.txt
- \[x] Non ci sarà alcun output sullo schermo mentre viene reindirizzato a out.txt.
- \[ ] L'output sullo schermo sarà identico a out.txt più numeri di riga.
- \[ ] Il file out.txt conterrà STDERR e STDOUT andrà allo schermo.

**Nota:** controlla la domanda sopra per una variante.

#### D12. In che modo SUID o setuid influisce sui comandi eseguibili?

- \[ ] Quando il comando crea file, questi saranno di proprietà del proprietario del gruppo del comando.
- \[ ] Il bit SUID consente a chiunque di eseguire il comando indipendentemente dalle altre autorizzazioni impostate.
- \[x] Quando il comando viene eseguito, i suoi privilegi in esecuzione passano al proprietario utente del comando.
- \[ ] Quando il comando viene eseguito, i suoi privilegi in esecuzione vengono elevati al proprietario del gruppo del comando.

#### D13. Per estrarre il testo dalla prima colonna di file chiamata textfile, quale comando useresti?

- \[ ] `cat {$1,textfile}`
- \[ ] `cat textfile | awk [print $1]`
- \[x] `cat textfile | awk '{print $1}'`
- \[ ] `awk textfile {print $1}`

#### D14. Qual è la scorciatoia da tastiera per richiamare la ricerca della cronologia bash come mostrato di seguito?

```bash
(reverse-i-search)`':
```

- \[ ] Esc + R
- \[ ] Ctrl + H
- \[x] Ctrl + R
- \[ ] Alt + R

#### D15. Quale espressione aritmetica darà la risposta più precisa?

- \[ ] `var=$( expr 10 / 8 )`
- \[ ] `(( var= 10 /8 ))`
- \[ ] `var=$(( 10 / 8 ))`
- \[x] `var=$(echo 'scale=2; 10 / 8' | bc)`

#### D16. Qual è il risultato di questo script?

```bash
txt=Penguins
[[ $txt =~ [a-z]{8} ]]; echo $?
```

- \[ ] 0, che rappresenta 'true', perché la variabile "txt" contiene otto lettere
- \[ ] 0, che rappresenta 'vero', perché tutti amano i pinguini!
- \[ ] 1, che rappresenta 'false', perché la variabile "txt" è più lunga di otto caratteri
- \[x] 1, che rappresenta 'false', perché la variabile "txt" non contiene otto lettere minuscole tra a e z

#### D17. Come cambieresti il prompt della shell Bash come segue?

```bash
HAL>
```

- \[ ] `SHELL="HAL\>"`
- \[ ] `SHELL="HAL>"`
- \[x] `export PS1="HAL>"`
- \[ ] `PS1="HAL\>"`

#### D18. Qual è l'output di questo codice?

```bash
VAR="/var/www/html/website.com/html/"
echo "${VAR#*/html}"
```

- \[x] `/website.com/html/`
- \[ ] `/html/website.com/html/`
- \[ ] `/var/www/html/website.com/`
- \[ ] Nulla sarà riecheggiato sullo schermo.

#### D19. Se viene richiesto il testo all'input standard, è possibile dire al comando che hai finito di inserire il testo con quale combinazione di tasti?

- \[ ] Ctrl + A (Windows) o Comando + A (Mac)
- \[ ] Ctrl + E (Windows) o Comando + E (Mac)
- \[x] Ctrl + D (Windows) o Comando + D (Mac)
- \[ ] Ctrl + Z (Windows) o Comando + Z (Mac)

#### D20. Affinché uno script Bash possa essere eseguito come un comando del sistema operativo, dovrebbe iniziare con una linea shebang. Che aspetto ha?

- \[x] `#!/usr/bin/env bash`
- \[ ] `~/usr/bin/env bash`
- \[ ] `'$!/usr/bin/env bash`
- \[ ] `#/usr/bin/env bash`

#### D21. Quale linea di script Bash probabilmente ha prodotto l'output mostrato di seguito?

```bash
The date is: Sun Mar 24 12:30:06 CST 2019!
```

- \[ ] `echo "The date is: !"`
- \[ ] `echo "The date is: date!"`
- \[ ] `echo "The date is: (date)!"`
- \[x] `echo "The date is: $(date)!"`

#### D22. Supponiamo che la tua attuale directory di lavoro sia la tua home directory. Come è possibile eseguire lo script demo.sh che si trova nella home directory? Trova tre risposte corrette.

```bash
A. /home/demo.sh
B. ./demo.sh
C. ~/demo.sh
D. bash /home/demo.sh
E. bash demo.sh
```

- \[x] B, C, E
- \[ ] A, B, C
- \[ ] C, D, E
- \[ ] B, D, E

#### D23. Come potresti ottenere un elenco di tutti i file .html nel tuo albero?

- \[ ] `find . -type html`
- \[ ] `find . -name *.html`
- \[ ] `find *.html`
- \[x] `find . -name \*.html -print`

Il secondo sembra buono, ma espanderà il \* se c'è qualche file .html nella directory di lavoro.

#### D24. Cosa ci sarebbe dentro.txt?

```bash
cat < in.txt > out.txt
```

- \[ ] Output dalla riga di comando. Per impostazione predefinita, STDIN proviene dalla tastiera.
- \[ ] Niente perché non è possibile reindirizzare dal file (in.txt) a un altro file (out.txt). È possibile reindirizzare solo da un comando a un file.
- \[x] Sarebbe il contenuto di in.txt.
- \[ ] Niente. Il reindirizzamento creerà un nuovo file vuoto ma non ci sarà alcun output dal comando cat per reindirizzare.

#### D25. Cosa fa questa dichiarazione bash?

```bash
(( $a == $b ))
echo $?
```

- \[ ] Si alterna tra i valori di `$a` e `$b`.
- \[x] Verifica se i valori delle variabili `$a` e `$b` sono uguali.
- \[ ] Ritorna `$b` se è più grande di `$a`.
- \[ ] Ritorna `$a` se è più grande di `$b`.

#### D26. Cosa usi in una case statement per dire a Bash che hai finito con un test specifico?

- \[x] `; ;`
- \[ ] `: :`
- \[ ] `done`
- \[ ] `$$`

#### D27. Cosa rappresenta l'asterisco in questa dichiarazione?

```bash
#!/usr/bin/env bash
case $num in
	1)
	echo "one"
	;;
	2)
	echo "two"
	;;
	*)
	echo "a mystery"
	;;
esac
```

- \[x] un caso che corrisponde a qualsiasi valore, fornendo un'opzione predefinita se nient'altro rileva quel valore
- \[ ] un caso solo per ciò che accade quando il carattere asterisco viene passato nello script
- \[ ] l'azione di tutti gli altri casi combinati insieme
- \[ ] un'azione eseguita per qualsiasi input, anche se corrisponde a una condizione specificata

#### D28. Quale script Bash creerà correttamente questi file?

- \[ ] `touch file{1+10}.txt`
- \[ ] `touch file{1-10}.txt`
- \[x] `touch file{1..10}.txt`
- \[ ] `touch file(1..10).txt`

#### D29. Quale variabile controlleresti per verificare che l'ultimo comando sia stato eseguito correttamente?

- \[ ] `$$`
- \[x] `$?`
- \[ ] `$!`
- \[ ] `$@`

#### D30. Qual è l'output di questo script?

```bash
#!/bin/bash
fname=john
john=thomas
echo ${!fname}
```

- \[ ] giovanni
- \[x] thomas
- \[ ] Errore di sintassi
- \[ ] vuoto

[riferimento](https://unix.stackexchange.com/questions/41292/variable-substitution-with-an-exclamation-mark-in-bash)

#### D31. Quale sarà l'output di questo script?

![question](images/Q30/question.png?raw=png)

- \[ ] `A` ![A](images/Q30/A.png?raw=png)
- \[ ] `B` ![B](images/Q30/B.png?raw=png)
- \[x] `C` ![C](images/Q30/C.png?raw=png)
- \[ ] `D` ![D](images/Q30/D.png?raw=png)

Ecco una versione basata su testo di Q.30:

```bash
ll
-rw-r--r-- 1 frankmolev staff 374   Jun 3 19:30 .
-rw-r--r-- 1 frankmolev staff 1666  Jun 3 19:30 ..
-rw-r--r-- 1 frankmolev staff 0     Jun 3 19:30 file1.txt
-rw-r--r-- 1 frankmolev staff 0     Jun 3 19:30 file2.txt
..

ll | sed -e 's,file,text,g'

```

- \[ ] A

<!---->

      -rw-r--r-- 1 frankmolev staff 374   Jun 3 19:30 .
      -rw-r--r-- 1 frankmolev staff 1666  Jun 3 19:30 ..
      -rw-r--r-- 1 frankmolev staff 0     Jun 3 19:30 file1.file
      -rw-r--r-- 1 frankmolev staff 0     Jun 3 19:30 file2.file
      ..

- \[ ] B

<!---->

      -rw-r--r-- 1 frankmolev staff 374   Jun 3 19:30 .
      -rw-r--r-- 1 frankmolev staff 1666  Jun 3 19:30 ..
      -rw-r--r-- 1 frankmolev staff 0     Jun 3 19:30 file1.txt
      -rw-r--r-- 1 frankmolev staff 0     Jun 3 19:30 file2.txt
      ..

- \[ ] C

<!---->

      -rw-r--r-- 1 frankmolev staff 68    Jun 3 19:30 .
      -rw-r--r-- 1 frankmolev staff 1666  Jun 3 19:30 ..

- \[x] D

<!---->

    -rw-r--r-- 1 frankmolev staff 374     Jun 3 19:30 .
    -rw-r--r-- 1 frankmolev staff 1666    Jun 3 19:30 ..
    -rw-r--r-- 1 frankmolev staff 0       Jun 3 19:30 text1.txt
    -rw-r--r-- 1 frankmolev staff 0       Jun 3 19:30 text.txt
    ..

#### D32. Cosa c'è di sbagliato in questo script?

```bash
#!/bin/bash
read -p "Enter your pet type." PET
if [ $PET = dog ] ;then
    echo "You have a dog"
fi
```

- \[ ] Se il valore di PET non corrisponde a dog, lo script restituirà un codice di stato diverso da zero.
- \[ ] Non c'è niente di sbagliato in questo. La condizione controlla perfettamente il valore del PET.
- \[x] Avrà esito negativo se l'utente preme il tasto Invio (A capo) senza immettere un nome di animale domestico quando richiesto.
- \[ ] L'istruzione then deve trovarsi su una riga separata.

#### D33. Come puoi raccogliere la cronologia per più terminali?

- \[ ] Funziona solo per impostazione predefinita.
- \[ ] `history --shared`
- \[ ] `history --combined`
- \[x] `shopt -s histappend`

#### D34. Qual è la differenza tra le variabili $@ e $\*?

- \[x] `$@` considera ogni argomento citato come un'entità separata. `$*` considera l'intera stringa di argomenti come un'unica entità.
- \[ ] `$*` considera ogni argomento citato come un'entità separata. `$@` considera l'intera stringa di argomenti come un'unica entità.
- \[ ] `$*` viene utilizzato per contare gli argomenti passati a uno script, `$@` fornisce tutti gli argomenti in un'unica stringa.
- \[ ] `$*` è il carattere jolly che include tutti gli argomenti con suddivisione delle parole, `$@` contiene gli stessi dati ma in una matrice.

#### D35. Quale comando viene eseguito in questo script per verificare se esiste .txt file?

```bash
if [ -f file.txt ]; then
    echo "file.txt exists"
fi
```

- \[ ] `/usr/bin/test`
- \[ ] `/usr/bin/[`
- \[x] `the built-in [ command`
- \[ ] `/usr/bin/[[`

#### D36. Quale sarà l'output di questo script?

```bash
#!/bin/bash
Linux=('Debian' 'Redhat' 'Ubuntu' 'Android' 'Fedora' 'Suse')
x=3

Linux=(${Linux[@]:0:$x} ${Linux[@]:$(($x + 1))})
echo "${Linux[@]}"
```

- \[ ] Debian Redhat Ubuntu Android Fedora Suse
- \[ ] Androide
- \[ ] Fedora Suse
- \[x] Debian Redhat Ubuntu Fedora Suse

#### D37. Quale file consente di salvare le modifiche nell'ambiente shell tra le sessioni?

- \[ ] `/etc/bash.conf`
- \[x] `~/.profile`
- \[ ] `/etc/bashprofile`
- \[ ] `~/profile`

#### D38. Date le autorizzazioni elencate sui dati.txt è possibile che l'utente2 abbia le autorizzazioni di lettura, scrittura ed esecuzione sui dati.txt?

```bash
$ ls -l
total 0
-rwx------+ 1 user1 user1 0 Oct 27 10:54 data.txt
```

- \[ ] No, è chiaro che user2 non dispone di autorizzazioni di lettura, scrittura ed esecuzione.
- \[x] Sì, il `+` alla fine della stringa di autorizzazione di 10 cifre indica che è presente un elenco di controllo di accesso. Questo potrebbe eventualmente dare all'utente2 autorizzazioni non visibili da `ls -l`.
- \[ ] È possibile che SELinux fornisca autorizzazioni di lettura, scrittura ed esecuzione per user2 che non sono visibili con `ls -l`.
- \[ ] Sì, il `+` alla fine della stringa di autorizzazione a 10 cifre indica che è presente un set di attributi esteso. Ciò potrebbe concedere all'utente2 le autorizzazioni per leggere, scrivere ed eseguire dati.txt.

#### D39. Che cosa realizza questo script?

```bash
#!/bin/bash
declare -A ARRAY=([user1]=bob [user2]=ted [user3]=sally)
KEYS=(${!ARRAY[@]})

for (( i=0; $i < ${#ARRAY[@]}; i+=1 ));do
        echo ${KEYS[$i]} - ${ARRAY[${KEYS[$i]}]}
done
```

- \[ ] Ordina l'array associativo denominato ARRAY e memorizza i risultati in un array indicizzato denominato KEYS. Utilizza quindi questa matrice ordinata per eseguire il ciclo attraverso l'array associativo ARRAY.
- \[x] Utilizzando uno stile C per il ciclo, esegue il loop attraverso la matrice associativa denominata ARRAY utilizzando le chiavi dell'array associativo e restituisce sia la chiave che i valori per ogni elemento.
- \[ ] Crea una matrice indicizzata della matrice associativa denominata ARRAY. Utilizza quindi uno stile C per il ciclo e l'array indicizzato per eseguire il ciclo tra tutti gli elementi nella matrice associativa, emettendo la chiave e il valore di ciascun elemento della matrice utilizzando il numero di indice.
- \[ ] Crea una matrice associativa denominata ARRAY, che esegue un ciclo in loop utilizzando uno stile C per loop e i numeri di indice di ogni elemento nelle chiavi dell'array associativo, emettendo il valore di ciascun elemento.

#### D40. Quale file corrisponderebbe al codice qui sotto?

```bash
ls Hello[[.vertical-line.]]World
```

- \[ ] Niente, questo è un file glob non valido.
- \[ ] `Hello.vertical-line.World`
- \[ ] `Hello[[.vertical-line.]]World`
- \[x] `Hello|World`

#### D41. Cosa ci sarà in out.txt?

```bash
ls nonexistentfile | grep "No such file" > out.txt
```

- \[ ] Nessun file di questo tipo
- \[ ] ls: impossibile accedere a inesistentfile: Nessun file o directory di questo tipo
- \[x] Niente, fuori.txt sarà vuoto.
- \[ ] Sarà il contenuto di un file inesistente.

#### D42. Affinché lo script stampi "È numerico" sullo schermo, cosa dovrebbe inserire l'utente quando richiesto?

```bash
#!/bin/bash
read -p "Enter text " var
if [[ "$var" =~ "^[0-9]+$" ]];then
    echo "Is numeric"
else
    echo "Is not numeric"
fi
```

- \[ ] Qualsiasi sequenza di caratteri che include un numero intero
- \[ ] L'utente dovrebbe inserire la sequenza di caratteri di `^[0-9]]+$` Solo questo si rivelerà vero e "È numerico" verrà stampato sullo schermo a causa di una sintassi errata. Incapsulando l'espressione regolare tra virgolette doppie, ogni corrispondenza avrà esito negativo tranne la stringa di testo `^[0-9]+$`
- \[ ] Uno o più caratteri che includono solo numeri interi
- \[x] A causa di un errore di sintassi è impossibile ottenere lo script per stampare "È numerico"

La regex non deve essere citata per funzionare correttamente.

#### D43. Come troveresti l'ultimo comando di copia eseguito nella tua cronologia?

- \[ ] storia | trova cp
- \[x] storia | grep cp
- \[ ] grep cp storia
- \[ ] cp storia

#### D44. Per scrivere uno script che scorre i file in una directory, quale dei seguenti elementi è possibile utilizzare?

- \[x] `bash for i in $(ls); do ... done`
- \[ ] `bash for $(ls); do ... done`
- \[ ] `bash for i in $ls; do ... done`
- \[ ] `bash for $ls; do ... done`

#### D45. Quando si esegue un comando e si passa l'output di quel comando a un altro comando, quale carattere consente di concatenare questi comandi insieme?

- \[x] |
- \[ ] ->
- \[ ] #
- \[ ] @

#### D46. Nello script mostrato di seguito, cos'è **saluto**?

```bash
#!/usr/bin/env bash
greeting="Hello"
echo $greeting, everybody!
```

- \[ ] un comando
- \[ ] un ciclo
- \[ ] un parametro
- \[x] una variabile

#### D47. Quale istruzione controlla se la variabile num è maggiore di cinque?

- \[ ] `(( num -gt 5 ))`
- \[ ] `[[$num -lt 5]]`
- \[x] `(( num > 5 ))`
- \[ ] `num > 5`

[riferimento](https://tldp.org/LDP/abs/html/dblparens.html)

#### D48. Usando bash extended globbing, quale sarà l'output di questo comando?

```bash
$ ls -l
apple
banana
bananapple
banapple
pineapple
strawberry
$ shopt -s extglob
$ ls -l @(ba*(na)|a+(p)le)
```

- \[x] a

```bash
apple
banana
```

- \[ ] b

```bash
apple
banana
bananapple
banapple
pineapple
strawberry
```

- \[ ] c

```bash
apple
banana
bananappple
banapple
pineapple
```

- \[ ] d

```bash
apple
banana
bananapple
banapple
pineapple
```

[riferimento](https://www.linuxjournal.com/content/bash-extended-globbing)

#### D49. Se utilizzato dall'interno di uno script, quale variabile contiene il nome dello script?

- \[x] $ 0
- \[ ] $# // numero di parametri posizionali
- \[ ] $$ // pid del guscio corrente
- \[ ] $@ // costrutto array-like di tutti i parametri posizionali

#### D50. Cosa significa il + alla fine delle autorizzazioni di file a 10 cifre su data.txt?

```bash
ls -l
-rwx------+ 1 user1 u1 0 Oct 1 10:00 data.txt
```

- \[ ] Esiste un contesto di sicurezza SELinux
- \[ ] Il bit appiccicoso è impostato e il file rimarrà nella RAM per la velocità
- \[x] Esiste un elenco di controllo di accesso
- \[ ] Esiste un attributo esteso come l'insieme immutabile

#### D51. In Bash, cosa fa il commento qui sotto?

```bash
cd -
```

- \[x] Ti sposta nella directory in cui ti trovavi in precedenza.
- \[ ] Ti sposta nella tua cartella Inizio (qualunque sia la tua attuale directory di lavoro).
- \[ ] Elimina la directory corrente
- \[ ] Ti sposta di una directory sopra la tua attuale directory di lavoro.

#### D52. A cosa serve questo comando?

```bash
cat > notes -
```

- \[x] Accetta il testo dall'input standard e lo inserisce in "note"
- \[ ] Crea "note" ed esce
- \[ ] Restituisce il contenuto delle note e lo elimina
- \[ ] Aggiunge testo alle "note" esistenti

#### D53. Qual è l'output di:

```bash
VAR="This old man came rolling"
echo "\${VAR//man/rolling}"
```

- \[x] Questa vecchia laminazione è arrivata a rotolare
- \[ ] Questo vecchio è venuto uomo
- \[ ] Questo vecchio è venuto rotolando
- \[ ] Questo vecchio è venuto

#### D54. La shell esamina il contenuto di una particolare variabile per identificare quali programmi può eseguire. Qual è il nome di questa variabile?

- \[ ] $INCLUDE
- \[x] $PATH
- \[ ] $PROGRAM
- \[ ] $PATHS

#### D55. Quale dichiarazione useresti per stamparlo nella console?

`Shall we play a game? yes\no`

- \[ ] `echo "Shall we play a game? yes/\no"`
- \[ ] `echo "Shall we play a game\? yes\\no"`
- \[x] `echo "Shall we play a game? yes\\no"`
- \[ ] `echo "Shall we play a game? yes\no"`

#### D56. Data una directory con questi sette file, cosa rimarrebbe dopo l'esecuzione di questi comandi?

```bash
archive.tar
image1.gif
image1.jpg
image2.gif
image2.jpg
textfile1.txt
textfile2.txt

----------

`shopt -s extglob
rm !(*gif|*jpg)`
```

- \[ ] a

```bash
archive.tar
image1.gif
image1.jpg
image2.gif
image2.jpg
textfile1.txt
textfile2.txt
```

- \[ ] b

```bash
archive.tar
textfile1.txt
textfile2.txt
```

- \[ ] c

Tutti questi file verranno eliminati

- \[x] d:

```bash
image1.gif
image1.jpg
image2.gif
image2.jpg
```

#### D57. Il codice sottostante sembra funzionare e restituisce "8 è maggiore di 5". Tuttavia, quale risultato inaspettato ti dirà che non funziona correttamente?

```bash
#!/bin/bash
var="8"
if [ $var > 5 ]; then
    echo "$var is greater than 5"
fi
```

- \[ ] Non ci saranno risultati inaspettati. Questo script funziona così com'è e l'output sarà "8 è maggiore di 5".
- \[ ] Il confronto non sarà in grado di gestire i numeri a virgola mobile, poiché Bash gestisce solo i numeri interi. Quindi questo esempio genererà un messaggio di errore se il valore di $var viene modificato in "8.8".
- \[x] Ci sarà un file nella directory corrente denominato 5.
- \[ ] La variabile $var non è citata, il che porterà alla divisione delle parole. Questo script avrà esito negativo con un messaggio "operatore unario previsto" se si modifica il valore di

#### D58. Qual è il risultato di questo script?

![question](images/Q60/question.png?raw=png)

- \[ ] Rimuove la directory 'pippo' e i file contenuti al suo interno.
- \[ ] Rimuove tutti i file tranne quelli nella directory corrente.
- \[x] Rimuove tutti i file nella directory corrente.
- \[ ] Rimuove tutti i file tranne quelli nella directory 'pippo'.

#### D59. Qual è la verità?

- \[x] Le regole dei criteri SELinux vengono controllate dopo le regole del dac.
- \[ ] Le regole dei criteri SELinux vengono controllate prima delle regole del DAC
- \[ ] Le regole dei criteri SELinux non vengono mai controllate dopo le regole del DAC.
- \[ ] Nessuno di questi

[riferimento](https://unix.stackexchange.com/questions/16828/what-roles-do-dac-file-permissions-acl-and-mac-selinux-play-in-linux-file-s)

#### D60. A cosa serve il comando sottostante?

```bash
w
```

- \[ ] Non visualizza informazioni sugli utenti attualmente sulla macchina.
- \[x] Visualizza informazioni sugli utenti attualmente sulla macchina.
- \[ ] Visualizza informazioni sugli utenti attualmente presenti su un'altra macchina.
- \[ ] Nessuno di questi

#### D61. Quali opzioni sed dovresti usare per cambiare la penultima istanza della variabile in rock in modo che legga:

Una costante è una variabile che è una roccia che non è variabile

```bash
var="A constant is a variable that is a variable that isn't variable"
echo "$var" | sed _____
```

- \[x] s/(.\*)variabile(.\*variabile)/\1rock\2/'
- \[ ] s/variabile/rock/'
- \[ ] s/variabile/roccia/g'
- \[ ] s/(.\*)variable(.\*variable)/\1rock\2/'

#### D62. Per creare uno script Bash denominato script.sh eseguibile, cosa dovresti eseguire?

- \[ ] script.sh esecutivo
- \[x] chmod +x script.sh
- \[ ] bash script.sh
- \[ ] fonte script.sh

#### D63. Come si può creare un terminale condiviso in una shell Bash?

- \[x] schermo
- \[ ] schermo -X
- \[ ] schermata --shared
- \[ ] terminale -condiviso

#### D64. Quale operatore invia l'output di ls a un file per un uso successivo?

- \[ ] ls < filelist.txt
- \[ ] ls ¦ filelist.txt
- \[x] ls > filelist.txt
- \[ ] ls - filelist.txt

#### D65. Quando si confrontano gli elementi con il caso, quale affermazione indica la fine del blocco di valutazione?

- \[ ] fermata
- \[x] esac
- \[ ] fatto
- \[ ] uscita

#### D66. Per eseguire un gruppo di comandi senza generare una subshell, quale sintassi useresti?

- \[ ] sh command1; comando2
- \[ ] { command1; command2; }
- \[ ] (( command1; command2 ))
- \[x] comando1; comando2

#### D67. Quali sono i risultati del comando con un utente di nome jon?

```bash
echo 'Hello, $(whoami)!'
```

- \[ ] Ciao, $(jon)!
- \[ ] Ciao, jon!
- \[x] Ciao, $(whoami)!
- \[ ] Ciao, whoami!

#### D68. Come si può copiare una directory in un altro sistema con compressione?

- \[ ] tar -ssh user@192.158.1.1 /bin/newfile
- \[x] tar cvzf - /wwwdata | ssh root@192.168.1.201 "dd of=/backup/wwwdata.tar.gz"
- \[ ] Non è possibile comprimere il flusso
- \[ ] directory scp -r user@192.168.1.1:/tmp

#### D69. Per assegnare il comando `ls -lah` al comando di scelta rapida `lh`, quale comando dovresti usare?

- \[x] alias lh='ls -lah'
- \[ ] link lh='ls -lah'
- \[ ] alias 'ls -lah'=lh
- \[ ] lh | ls -lah

#### D70. Quale istruzione stamperà tutti i file .cvs completi nella home directory o nelle sottodirectory senza visualizzare errori?

- \[ ] find $USER_DIR -name "\*.csv" 2>/dev/null
- \[ ] trova $HOME -name "\*.csv" 1>/dev/null
- \[x] trova $HOME -name "\*.csv" 2>/dev/null
- \[ ] find HOME -name "\*.csv" 1>/dev/null

#### D71. In Bash, cosa indica un # alla fine della stringa di prompt predefinita?

- \[x] che l'utente agisce come root
- \[ ] che la directory di lavoro corrente è la radice del file system
- \[ ] che ci sono aggiornamenti per il sistema disponibili
- \[ ] che l'utente non è privilegiato

#### D72. Quale sarà l'output di questo comando?

```bash
$ ls -l
file10.txt
file1.txt
fileabc.txt
filea.txt
fileb.txt
filec.txt
$ ls -l file[^abc]*.txt
```

- \[x] A

```bash
file1.txt
file10.txt
```

- \[ ] B

```bash
file10.txt
file1.txt
fileabc.txt
filea.txt
fileb.txt
filec.txt
```

- \[ ] C

```bash
fileabc.txt filea.txt fileb.txt filec.txt
```

- \[ ] D

```bash
filea.txt
fileb.txt
filec.txt
```

Il caret (`^`) qui nega le corrispondenze all'interno della parentesi. [Riferimento](https://tldp.org/LDP/abs/html/globbingref.html)

#### D73. Qual è l'output di questa sequenza di comandi?

```bash
cat <<EOF
------------------------
   This is line 1.
   This is line 2.
   This is line 3.
------------------------
EOF
```

- \[ ] A

```bash
This is line 1.
This is line 2.
This is line 3.
```

- \[ ] B

```bash
------------------------This is line 1.This is line 2.This is line 3.------------------------
```

- \[x] C

```bash
------------------------
   This is line 1.
   This is line 2.
   This is line 3.
------------------------
```

- \[ ] D

```bash
------------------------
This is line 1.
This is line 2.
This is line 3.
------------------------
```

#### D74. Cosa ci sarebbe dentro.txt?

```bash
#!/bin/bash

echo 123446789 > out.txt
exec 3<> out.txt
read -n 4 <&3
echo -n 5 >&3
exec 3>&-
```

- \[ ] 123446789
- \[ ] il simbolo del trattino (-)
- \[x] 123456789
- \[ ] il numero 5, che viene scritto nel file usando echo

Vedere [Reindirizzamento I/O](https://tldp.org/LDP/abs/html/io-redirection.html)

Vedi anche: [Qual è la differenza tra "echo" e "echo -n"?](https://stackoverflow.com/questions/30761986/what-is-the-difference-between-echo-and-echo-n)

#### D75. Quale variabile contiene l'ID processo (PID) dello script mentre è in esecuzione?

- \[ ] $ID
- \[ ] $ #
- \[ ] $ @
- \[x] $$

#### D76. Combinando il globbing esteso e l'espansione dei parametri, quale sarebbe il valore del VAR?

    #!/bin/bash
    shopt -s extglob
    VAR='     This is...     a string of characters     '
    VAR=${VAR##+([[:space:]])}; VAR=${VAR%%+([[:space:]])};
    echo "$VAR"

- \[ ] `<pre> This is... a string of characters</pre>`
- \[ ] `<pre> This is...a string of characters</pre>`
- \[ ] `<pre>This is... a string of characters</pre>`
- \[ ] `<pre>This is...a string of characters</pre>`

Referenze:

1.  [Qual è il significato della sintassi ${0##...} con variabile, parentesi graffe e carattere hash in bash?](https://stackoverflow.com/questions/2059794/what-is-the-meaning-of-the-0-syntax-with-variable-braces-and-hash-chara)
2.  [Cosa significa espandere una variabile come "${var%%r\*}" in bash?](https://stackoverflow.com/questions/41859601/what-does-expanding-a-variable-as-varr-mean-in-bash)

#### D77. Quale operatore indica alla shell di eseguire un determinato comando in background?

- \[ ] !
- \[ ] &&
- \[x] &
- \[ ] $
