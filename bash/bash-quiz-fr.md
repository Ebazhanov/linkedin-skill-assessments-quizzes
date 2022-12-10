## Cogner

#### Q1. Laquelle des trois méthodes copiera le répertoire nommé « photo dir » de manière récursive du répertoire de base de l’utilisateur vers /backups ?

```bash
cp -R "~/photo dir" /backups #method1
cp -R ~"/photo dir" /backups #method2
cp -R ~/"photo dir" /backups #method3
```

- \[ ] Aucune des trois méthodes ne s’étendra au répertoire de base de l’utilisateur. Utilisation uniquement `"$HOME/photo dir"`sera couronné de succès.
- \[ ] Seule la méthode 1 se développera `"~/"` au répertoire de base de l’utilisateur, puis ajoutez le nom du répertoire entre guillemets qui inclut un espace.
- \[ ] Seule la méthode 2 se développera `"~/"` au répertoire de base de l’utilisateur, puis ajoutez le nom du répertoire entre guillemets qui inclut un espace.
- \[x] Seule la méthode 3 se développera `"~/"` au répertoire de base de l’utilisateur, puis ajoutez le nom du répertoire entre guillemets qui inclut un espace.

#### Q2. Si script.sh est exécuté dans le répertoire actif, il échouera. Pourquoi?

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

- \[ ] ls: impossible d’accéder au fichier inexistant: Aucun fichier ou répertoire de ce type
- \[x] La boucle for se divisera sur les limites des mots et Beach photo1.jpg a un espace dedans.
- \[ ] La commande mv échouera car le crochet bouclé est un caractère spécial dans Bash et ne peut pas être utilisé dans les noms de fichiers.
- \[ ] L’exécution de script.sh réussira car la commande ls crée une liste de fichiers dans le répertoire actif et pour les boucles à travers cette liste en renommant les fichiers avec une extension .bak.

#### Q3. Pour exécuter une commande de copie dans un sous-shell, quelle syntaxe utiliseriez-vous ?

- \[x] `( command )`
- \[ ] `sh command`
- \[ ] `{ command; }`
- \[ ] `(( command ))`

#### Q4. En utilisant « awk », quelle serait la sortie de cette chaîne de commande ?

```bash
echo "1 2 3" | awk '{for (i=1; i<=NF; i++) s=s+$i};END {print s}'
```

- \[x] 6
- \[ ] 123
- \[ ] 3
- \[ ] 600

#### Q5. La commande ci-dessous recherchera dans le système de fichiers racine les fichiers nommés « finance.db ». Dans ce contexte, quelles informations sont envoyées à /dev/null ?

```bash
find / -name "finance.db" 1>results.txt 2>/dev/null
```

- \[ ] les noms des fichiers qui ne correspondent pas au financement.db
- \[x] informations envoyées à l’erreur standard - par exemple, les erreurs que la commande find affiche lors de son exécution
- \[ ] les noms des fichiers qui correspondent au financement.db
- \[ ] informations envoyées à la sortie standard, c’est-à-dire le chemin d’accès aux fichiers que la commande find a localisés

#### Q6. Pour supprimer définitivement les lignes vides d’un fichier appelé textfile, quelle commande pourriez-vous utiliser ?

- \[x] `sed -i '/^$/d' textfile`
- \[ ] `sed '/^$/d' textfile`
- \[ ] `cat textfile | sed '/^$/d`
- \[ ] `sed -i 's/^$//' textfile`

#### Q7. En supposant que user1 existe, quel serait le résultat de cette chaîne de commande ?

```bash
awk -F: '/user1/{print $1 "-" $3 "-" $6}' /etc/passwd
```

- \[ ] Il afficherait le nom d’utilisateur, l’UID et le répertoire de base de user1 séparés par deux-points.
- \[ ] Il imprimerait l’UID, le GID et le répertoire de base de user1 séparés par des traits d’union.
- \[ ] Il imprimerait l’UID, le commentaire et le répertoire de base de user1 séparés par des tirets.
- \[x] Il afficherait le nom d’utilisateur, l’UID et le répertoire de base de user1 séparés par des traits d’union.

#### Q8. Que se passe-t-il si vous utilisez le `"set -e"` dans un script Bash ?

- \[ ] La fermeture de Bash se produit si une fonction ou un sous-shell renvoie un code d’état différent de zéro.
- \[ ] Cela entraînera la fermeture de Bash si un conditionnel renvoie un code d’état différent de zéro.
- \[ ] Cela entraînera la fermeture de Bash si les affectations locales, déclaratives ou typographiques renvoient un code d’état différent de zéro.
- \[x] Bash se ferme si une commande, une liste de commandes, une commande composée ou potentiellement un pipeline renvoie un code d’état différent de zéro.

#### Q9. Le **\_** le mot-clé met le script en pause pour obtenir l’entrée à partir de l’entrée standard.

- \[ ] obtenir
- \[ ] argument
- \[x] lire
- \[ ] entrée

#### Q10. Si file.sql contient des instructions SQL à exécuter, qu’y aura-t-il dans file.txt ?

```bash
mysql < file.sql > file.txt
```

- \[ ] une copie du contenu du fichier.sql
- \[ ] une erreur indiquant qu’il s’agit d’une syntaxe non valide
- \[ ] la sortie d’erreur de la commande MySQL
- \[x] la sortie sans erreur de la commande MySQL

**Remarque:** vérifiez la question ci-dessous pour une variante.

#### Q11. Quelle sera la différence entre la sortie à l’écran et le contenu de la sortie.txt

```bash
mysql < file.sql > out.txt
```

- \[ ] La sortie à l’écran sera identique à la sortie.txt
- \[x] Il n’y aura pas de sortie à l’écran car il est redirigé vers out.txt.
- \[ ] La sortie à l’écran sera identique à out.txt plus les numéros de ligne.
- \[ ] Le fichier out.txt contiendra STDERR et STDOUT ira à l’écran.

**Remarque:** vérifiez la question ci-dessus pour une variante.

#### Q12. Comment le SUID ou le setuid affecte-t-il les commandes exécutables ?

- \[ ] Lorsque la commande crée des fichiers, ils appartiennent au propriétaire du groupe de la commande.
- \[ ] Le bit SUID permet à quiconque d’exécuter la commande, quelles que soient les autres autorisations définies.
- \[x] Lorsque la commande est exécutée, ses privilèges d’exécution s’élèvent au rang d’utilisateur propriétaire de la commande.
- \[ ] Lorsque la commande est exécutée, ses privilèges d’exécution s’élèvent au rang de propriétaire du groupe de la commande.

#### Q13. Pour extraire du texte de la première colonne du fichier appelé textfile, quelle commande utiliseriez-vous ?

- \[ ] `cat {$1,textfile}`
- \[ ] `cat textfile | awk [print $1]`
- \[x] `cat textfile | awk '{print $1}'`
- \[ ] `awk textfile {print $1}`

#### Q14. Quel est le raccourci clavier pour appeler la recherche dans l’historique Bash comme indiqué ci-dessous?

```bash
(reverse-i-search)`':
```

- \[ ] Échap + R
- \[ ] Ctrl + H
- \[x] Ctrl + R
- \[ ] Alt + R

#### Q15. Quelle expression arithmétique donnera la réponse la plus précise ?

- \[ ] `var=$( expr 10 / 8 )`
- \[ ] `(( var= 10 /8 ))`
- \[ ] `var=$(( 10 / 8 ))`
- \[x] `var=$(echo 'scale=2; 10 / 8' | bc)`

#### Q16. Quel est le résultat de ce script ?

```bash
txt=Penguins
[[ $txt =~ [a-z]{8} ]]; echo $?
```

- \[ ] 0, représentant 'true', car la variable « txt » contient huit lettres
- \[ ] 0, représentant « vrai », parce que tout le monde aime les pingouins !
- \[ ] 1, représentant 'false', car la variable « txt » est plus longue que huit caractères
- \[x] 1, représentant 'false', car la variable « txt » ne contient pas huit lettres minuscules entre a et z

#### Q17. Comment modifieriez-vous votre invite de shell Bash comme suit ?

```bash
HAL>
```

- \[ ] `SHELL="HAL\>"`
- \[ ] `SHELL="HAL>"`
- \[x] `export PS1="HAL>"`
- \[ ] `PS1="HAL\>"`

#### Q18. Quelle est la sortie de ce code ?

```bash
VAR="/var/www/html/website.com/html/"
echo "${VAR#*/html}"
```

- \[x] `/website.com/html/`
- \[ ] `/html/website.com/html/`
- \[ ] `/var/www/html/website.com/`
- \[ ] Rien ne sera repris à l’écran.

#### Q19. Si vous êtes invité à entrer du texte à l’entrée standard, vous pouvez indiquer à la commande que vous avez terminé de saisir du texte avec quelle combinaison de touches?

- \[ ] Ctrl + A (Windows) ou Commande + A (Mac)
- \[ ] Ctrl + E (Windows) ou Commande + E (Mac)
- \[x] Ctrl + D (Windows) ou Commande + D (Mac)
- \[ ] Ctrl + Z (Windows) ou Commande + Z (Mac)

#### Q20. Pour qu’un script Bash soit exécuté comme une commande du système d’exploitation, il doit commencer par une ligne shebang. À quoi cela ressemble-t-il?

- \[x] `#!/usr/bin/env bash`
- \[ ] `~/usr/bin/env bash`
- \[ ] `'$!/usr/bin/env bash`
- \[ ] `#/usr/bin/env bash`

#### Q21. Quelle ligne de script Bash a probablement produit la sortie montrée ci-dessous?

```bash
The date is: Sun Mar 24 12:30:06 CST 2019!
```

- \[ ] `echo "The date is: !"`
- \[ ] `echo "The date is: date!"`
- \[ ] `echo "The date is: (date)!"`
- \[x] `echo "The date is: $(date)!"`

#### Q22. Supposons que votre répertoire de travail actuel soit votre répertoire personnel. Comment pouvez-vous exécuter le script demo.sh qui se trouve dans votre répertoire personnel ? Trouvez trois bonnes réponses.

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

#### Q23. Comment pourriez-vous obtenir une liste de tous les fichiers .html de votre arbre?

- \[ ] `find . -type html`
- \[ ] `find . -name *.html`
- \[ ] `find *.html`
- \[x] `find . -name \*.html -print`

Le second semble bien, mais développera le \* s’il y a un fichier .html sur votre répertoire de travail.

#### Q24. Qu’y aurait-il dans l’out.txt?

```bash
cat < in.txt > out.txt
```

- \[ ] Sortie de la ligne de commande. Par défaut, STDIN provient du clavier.
- \[ ] Rien car vous ne pouvez pas rediriger du fichier (in.txt) vers un autre fichier (out.txt). Vous pouvez uniquement rediriger d’une commande vers un fichier.
- \[x] Ce serait le contenu de in.txt.
- \[ ] Rien. La redirection créera un nouveau fichier vide mais il n’y aura aucune sortie de la commande cat à rediriger.

#### Q25. Que fait cette déclaration bash ?

```bash
(( $a == $b ))
echo $?
```

- \[ ] Il effectue une boucle entre les valeurs de `$a` et `$b`.
- \[x] Il teste si les valeurs des variables `$a` et `$b` sont égaux.
- \[ ] Il renvoie `$b` s’il est plus grand que `$a`.
- \[ ] Il renvoie `$a` s’il est plus grand que `$b`.

#### Q26. Qu’utilisez-vous dans une déclaration de cas pour dire à Bash que vous avez terminé avec un test spécifique?

- \[x] `; ;`
- \[ ] `: :`
- \[ ] `done`
- \[ ] `$$`

#### Q27. Que représente l’astérisque dans cette déclaration ?

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

- \[x] un cas qui correspond à n’importe quelle valeur, fournissant une option par défaut si rien d’autre n’attrape cette valeur
- \[ ] un cas uniquement pour ce qui se passe lorsque le caractère astérisque est passé dans le script
- \[ ] l’action de toutes les autres affaires combinées ensemble
- \[ ] une action qui est effectuée pour n’importe quelle entrée, même si elle correspond à une condition spécifiée

#### Q28. Quel script Bash créera correctement ces fichiers ?

- \[ ] `touch file{1+10}.txt`
- \[ ] `touch file{1-10}.txt`
- \[x] `touch file{1..10}.txt`
- \[ ] `touch file(1..10).txt`

#### Q29. Quelle variable vérifieriez-vous pour vérifier que la dernière commande a été exécutée avec succès ?

- \[ ] `$$`
- \[x] `$?`
- \[ ] `$!`
- \[ ] `$@`

#### Q30. Quelle est la sortie de ce script ?

```bash
#!/bin/bash
fname=john
john=thomas
echo ${!fname}
```

- \[ ] jean
- \[x] thomas
- \[ ] Erreur de syntaxe
- \[ ] vide

[référence](https://unix.stackexchange.com/questions/41292/variable-substitution-with-an-exclamation-mark-in-bash)

#### Q31. Quelle sera la sortie de ce script ?

![question](images/Q30/question.png?raw=png)

- \[ ] `A` ![A](images/Q30/A.png?raw=png)
- \[ ] `B` ![B](images/Q30/B.png?raw=png)
- \[x] `C` ![C](images/Q30/C.png?raw=png)
- \[ ] `D` ![D](images/Q30/D.png?raw=png)

Voici une version textuelle de Q.30 :

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

#### Q32. Qu’est-ce qui ne va pas avec ce script ?

```bash
#!/bin/bash
read -p "Enter your pet type." PET
if [ $PET = dog ] ;then
    echo "You have a dog"
fi
```

- \[ ] Si la valeur de PET ne correspond pas à dog, le script renvoie un code d’état différent de zéro.
- \[ ] Il n’y a rien de mal à cela. L’état vérifie parfaitement la valeur du PET.
- \[x] Il échouera si l’utilisateur appuie sur la touche Entrée (Retour) sans entrer de nom d’animal de compagnie lorsqu’il y est invité.
- \[ ] L’instruction then doit se trouver sur une ligne distincte.

#### Q33. Comment pouvez-vous rassembler l’histoire pour plusieurs terminaux?

- \[ ] Cela fonctionne simplement par défaut.
- \[ ] `history --shared`
- \[ ] `history --combined`
- \[x] `shopt -s histappend`

#### Q34. Quelle est la différence entre les variables $@ et $\* ?

- \[x] `$@` traite chaque argument cité comme une entité distincte. `$*` traite la chaîne d’arguments entière comme une seule entité.
- \[ ] `$*` traite chaque argument cité comme une entité distincte. `$@` traite la chaîne d’arguments entière comme une seule entité.
- \[ ] `$*` est utilisé pour compter les arguments transmis à un script, `$@` fournit tous les arguments dans une chaîne.
- \[ ] `$*` est le caractère générique qui inclut tous les arguments avec fractionnement de mots, `$@` contient les mêmes données mais dans un tableau.

#### Q35. Quelle commande est exécutée dans ce script pour vérifier si le fichier .txt existe ?

```bash
if [ -f file.txt ]; then
    echo "file.txt exists"
fi
```

- \[ ] `/usr/bin/test`
- \[ ] `/usr/bin/[`
- \[x] `the built-in [ command`
- \[ ] `/usr/bin/[[`

#### Q36. Quelle sera la sortie de ce script ?

```bash
#!/bin/bash
Linux=('Debian' 'Redhat' 'Ubuntu' 'Android' 'Fedora' 'Suse')
x=3

Linux=(${Linux[@]:0:$x} ${Linux[@]:$(($x + 1))})
echo "${Linux[@]}"
```

- \[ ] Debian Redhat Ubuntu Android Fedora Suse
- \[ ] Android
- \[ ] Fedora Suse
- \[x] Debian Redhat Ubuntu Fedora Suse

#### Q37. Quel fichier vous permet d’enregistrer les modifications apportées à l’environnement shell entre les sessions ?

- \[ ] `/etc/bash.conf`
- \[x] `~/.profile`
- \[ ] `/etc/bashprofile`
- \[ ] `~/profile`

#### Q38. Compte tenu des autorisations répertoriées sur les données.txt est-il possible que l’utilisateur2 puisse avoir des autorisations de lecture, d’écriture et d’exécution sur les données.txt ?

```bash
$ ls -l
total 0
-rwx------+ 1 user1 user1 0 Oct 27 10:54 data.txt
```

- \[ ] Non, il est clair que user2 n’a pas d’autorisations de lecture, d’écriture et d’exécution.
- \[x] Oui, le `+` à la fin de la chaîne d’autorisation à 10 chiffres, cela signifie qu’il y a une liste de contrôle d’accès. Cela pourrait éventuellement donner à l’utilisateur2 des autorisations non visibles par `ls -l`.
- \[ ] Il est possible que SELinux fournisse des autorisations de lecture, d’écriture et d’exécution pour user2 qui ne sont pas visibles avec `ls -l`.
- \[ ] Oui, le `+` à la fin de la chaîne d’autorisation à 10 chiffres, cela signifie qu’il existe un jeu d’attributs étendu. Cela pourrait donner à l’utilisateur2 des autorisations pour lire, écrire et exécuter des données.txt.

#### Q39. Qu’est-ce que ce script accomplit ?

```bash
#!/bin/bash
declare -A ARRAY=([user1]=bob [user2]=ted [user3]=sally)
KEYS=(${!ARRAY[@]})

for (( i=0; $i < ${#ARRAY[@]}; i+=1 ));do
        echo ${KEYS[$i]} - ${ARRAY[${KEYS[$i]}]}
done
```

- \[ ] Il trie le tableau associatif nommé ARRAY et stocke les résultats dans un tableau indexé nommé KEYS. Il utilise ensuite ce tableau trié pour parcourir en boucle le tableau associatif ARRAY.
- \[x] À l’aide d’une boucle de style C, il effectue une boucle à travers le tableau associatif nommé ARRAY à l’aide des clés du tableau associatif et génère à la fois la clé et les valeurs de chaque élément.
- \[ ] Il crée un tableau indexé du tableau associatif nommé ARRAY. Il utilise ensuite un style C pour boucle et le tableau indexé pour parcourir en boucle tous les éléments du tableau associatif, en sortant la clé et la valeur de chaque élément de tableau à l’aide du numéro d’index.
- \[ ] Il crée un tableau associatif nommé ARRAY, qu’il effectue en boucle à l’aide d’un style C pour boucle et des numéros d’index de chaque élément dans les clés du tableau associatif, en sortant la valeur de chaque élément.

#### Q40. Quel fichier correspondrait au code ci-dessous?

```bash
ls Hello[[.vertical-line.]]World
```

- \[ ] Rien, il s’agit d’un fichier glob non valide.
- \[ ] `Hello.vertical-line.World`
- \[ ] `Hello[[.vertical-line.]]World`
- \[x] `Hello|World`

#### Q41. Qu’y aura-t-il dedans.txt?

```bash
ls nonexistentfile | grep "No such file" > out.txt
```

- \[ ] Aucun fichier de ce type
- \[ ] ls: impossible d’accéder au fichier inexistant: Aucun fichier ou répertoire de ce type
- \[x] Rien, dehors.txt ne sera vide.
- \[ ] Ce sera le contenu du fichier inexistant.

#### Q42. Pour que le script imprime « Est numérique » à l’écran, que devrait entrer l’utilisateur lorsqu’il y est invité ?

```bash
#!/bin/bash
read -p "Enter text " var
if [[ "$var" =~ "^[0-9]+$" ]];then
    echo "Is numeric"
else
    echo "Is not numeric"
fi
```

- \[ ] Toute séquence de caractères qui inclut un entier
- \[ ] L’utilisateur devrait entrer la séquence de caractères de `^[0-9]]+$` Seulement cela s’avérera vrai et « Est numérique » serait imprimé à l’écran en raison d’une syntaxe incorrecte. En encapsulant l’expression régulière entre guillemets doubles, toutes les correspondances échouent, à l’exception de la chaîne de texte `^[0-9]+$`
- \[ ] Un ou plusieurs caractères qui n’incluent que des entiers
- \[x] En raison d’une erreur de syntaxe, il est impossible d’obtenir le script pour imprimer « Est numérique »

Le regex ne doit pas être cité pour fonctionner correctement.

#### Q43. Comment trouveriez-vous la dernière commande de copie exécutée dans votre historique ?

- \[ ] | d’histoire trouver cp
- \[x] | historique grep cp
- \[ ] historique grep cp
- \[ ] cp historique

#### Q44. Pour écrire un script qui parcourt les fichiers d’un répertoire, lequel des éléments suivants pourriez-vous utiliser ?

- \[x] `bash for i in $(ls); do ... done`
- \[ ] `bash for $(ls); do ... done`
- \[ ] `bash for i in $ls; do ... done`
- \[ ] `bash for $ls; do ... done`

#### Q45. Lors de l’exécution d’une commande et de la transmission de la sortie de cette commande à une autre commande, quel caractère vous permet d’enchaîner ces commandes ?

- \[x] |
- \[ ] ->
- \[ ] #
- \[ ] @

#### Q46. Dans le script ci-dessous, qu’est-ce qui est **salutation**?

```bash
#!/usr/bin/env bash
greeting="Hello"
echo $greeting, everybody!
```

- \[ ] une commande
- \[ ] une boucle
- \[ ] un paramètre
- \[x] une variable

#### Q47. Quelle instruction vérifie si la variable num est supérieure à cinq ?

- \[ ] `(( num -gt 5 ))`
- \[ ] `[[$num -lt 5]]`
- \[x] `(( num > 5 ))`
- \[ ] `num > 5`

[référence](https://tldp.org/LDP/abs/html/dblparens.html)

#### Q48. En utilisant Bash extended globbing, quelle sera la sortie de cette commande?

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

[référence](https://www.linuxjournal.com/content/bash-extended-globbing)

#### Q49. Lorsqu’elle est utilisée à partir d’un script, quelle variable contient le nom du script ?

- \[x] 0 $
- \[ ] $# // nombre de paramètres positionnels
- \[ ] $$ // pid du shell actuel
- \[ ] $@ // construction de type tableau de tous les paramètres positionnels

#### Q50. Que signifie le + à la fin des autorisations de fichier à 10 chiffres sur les données.txt ?

```bash
ls -l
-rwx------+ 1 user1 u1 0 Oct 1 10:00 data.txt
```

- \[ ] Il existe un contexte de sécurité SELinux
- \[ ] Le bit collant est défini et le fichier restera dans la RAM pour la vitesse
- \[x] Il existe une liste de contrôle d’accès
- \[ ] Il existe un attribut étendu tel qu’un ensemble immuable

#### Q51. Dans Bash, que fait le commentaire ci-dessous ?

```bash
cd -
```

- \[x] Il vous déplace vers le répertoire dans lequel vous étiez précédemment.
- \[ ] Il vous déplace vers votre dossier d’accueil (quel que soit votre répertoire de travail actuel).
- \[ ] Il supprime le répertoire actuel
- \[ ] Il vous déplace un répertoire au-dessus de votre répertoire de travail actuel.

#### Q52. Que fait cette commande ?

```bash
cat > notes -
```

- \[x] Accepte le texte de l’entrée standard et le place dans des « notes »
- \[ ] Crée des « notes » et quitte
- \[ ] Génère le contenu des notes et le supprime
- \[ ] Ajoute du texte aux « notes » existantes

#### Q53. Quel est le résultat de:

```bash
VAR="This old man came rolling"
echo "\${VAR//man/rolling}"
```

- \[x] Ce vieux rouleau est venu rouler
- \[ ] Ce vieil homme est venu homme
- \[ ] Ce vieil homme est venu rouler
- \[ ] Ce vieux est venu

#### Q54. Le shell examine le contenu d’une variable particulière pour identifier les programmes qu’il peut exécuter. Quel est le nom de cette variable ?

- \[ ] $INCLUDE
- \[x] $PATH
- \[ ] $PROGRAM
- \[ ] $PATHS

#### Q55. Quelle instruction utiliseriez-vous pour l’imprimer dans la console ?

`Shall we play a game? yes\no`

- \[ ] `echo "Shall we play a game? yes/\no"`
- \[ ] `echo "Shall we play a game\? yes\\no"`
- \[x] `echo "Shall we play a game? yes\\no"`
- \[ ] `echo "Shall we play a game? yes\no"`

#### Q56. Étant donné un répertoire avec ces sept fichiers, que resterait-il après l’exécution de ces commandes?

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

Tous ces fichiers seront supprimés

- \[x] d:

```bash
image1.gif
image1.jpg
image2.gif
image2.jpg
```

#### Q57. Le code ci-dessous semble fonctionner et les sorties « 8 est supérieur à 5 ». Cependant, quel résultat inattendu vous dira qu’il ne fonctionne pas correctement?

```bash
#!/bin/bash
var="8"
if [ $var > 5 ]; then
    echo "$var is greater than 5"
fi
```

- \[ ] Il n’y aura pas de résultats inattendus. Ce script fonctionne tel quel et la sortie sera « 8 est supérieur à 5 ».
- \[ ] La comparaison ne pourra pas gérer les nombres à virgule flottante, car Bash ne gère que les entiers. Cet exemple génère donc un message d’erreur si la valeur de $var est remplacée par « 8.8 ».
- \[x] Il y aura un fichier dans le répertoire actuel nommé 5.
- \[ ] La variable $var n’est pas citée, ce qui entraînera un fractionnement des mots. Ce script échouera avec un message « opérateur unaire attendu » si vous modifiez la valeur de

#### Q58. Quel est le résultat de ce script ?

![question](images/Q60/question.png?raw=png)

- \[ ] Il supprime le répertoire 'foo' et les fichiers qu’il contient.
- \[ ] Il supprime tous les fichiers à l’exception de ceux du répertoire actuel.
- \[x] Il supprime tous les fichiers du répertoire actif.
- \[ ] Il supprime tous les fichiers sauf ceux du répertoire 'foo'.

#### Q59. Lequel est vrai?

- \[x] Les règles de stratégie SELinux sont vérifiées après les règles DAC.
- \[ ] Les règles de stratégie SELinux sont vérifiées avant les règles DAC
- \[ ] Les règles de stratégie SELinux ne sont jamais vérifiées après les règles DAC.
- \[ ] Aucun de ces éléments

[référence](https://unix.stackexchange.com/questions/16828/what-roles-do-dac-file-permissions-acl-and-mac-selinux-play-in-linux-file-s)

#### Q60. Que fait la commande ci-dessous ?

```bash
w
```

- \[ ] Il n’affiche pas d’informations sur les utilisateurs actuellement sur la machine.
- \[x] Il affiche des informations sur les utilisateurs actuellement sur la machine.
- \[ ] Il affiche des informations sur les utilisateurs actuellement sur l’autre machine.
- \[ ] Aucun de ces éléments

#### Q61. Quelles options sed devriez-vous utiliser pour changer l’avant-dernière instance de variable en rock afin qu’elle se lise comme suit:

Une constante est une variable qui est une roche qui n’est pas variable

```bash
var="A constant is a variable that is a variable that isn't variable"
echo "$var" | sed _____
```

- \[x] s/(.\*)variable(.\*variable)/\1rock\2/'
- \[ ] s/variable/roche/'
- \[ ] s/variable/roche/g'
- \[ ] s/(.\*)variable(.\*variable)/\1rock\2/'

#### Q62. Pour créer un script Bash nommé script.sh exécutable, que devez-vous exécuter ?

- \[ ] script.sh exécutif
- \[x] chmod +x script.sh
- \[ ] bash script.sh
- \[ ] script.sh source

#### Q63. Comment créer un terminal partagé dans un shell Bash ?

- \[x] écran
- \[ ] écran -X
- \[ ] écran --partagé
- \[ ] terminal -partagé

#### Q64. Quel opérateur envoie la sortie de ls dans un fichier pour une utilisation ultérieure ?

- \[ ] ls < liste de fichiers.txt
- \[ ] ls ¦ liste de fichiers.txt
- \[x] ls > liste de fichiers.txt
- \[ ] ls - liste de fichiers.txt

#### Q65. Lorsque l’on compare les éléments avec la casse, quel énoncé indique la fin du bloc d’évaluation?

- \[ ] arrêt
- \[x] esac
- \[ ] fait
- \[ ] sortie

#### Q66. Pour exécuter un groupe de commandes sans générer de sous-shell, quelle syntaxe utiliseriez-vous ?

- \[ ] sh, commande1; commande2
- \[ ] { command1; command2; }
- \[ ] (( command1; command2 ))
- \[x] commande1 ; commande2

#### Q67. Quels sont les résultats de la commande avec un utilisateur nommé jon ?

```bash
echo 'Hello, $(whoami)!'
```

- \[ ] Bonjour, $(jon)!
- \[ ] Bonjour, jon!
- \[x] Bonjour, $(whoami)!
- \[ ] Bonjour, whoami!

#### Q68. Comment copier un répertoire sur un autre système avec compression ?

- \[ ] tar -ssh user@192.158.1.1 /bin/newfile
- \[x] tar cvzf - /wwwdata | ssh root@192.168.1.201 « dd of=/backup/wwwdata.tar.gz »
- \[ ] Vous ne pouvez pas compresser le flux
- \[ ] répertoire scp -r user@192.168.1.1:/tmp

#### Q69. Pour affecter la commande `ls -lah` à la commande de raccourci `lh`, quelle commande devez-vous utiliser ?

- \[x] alias lh='ls -lah'
- \[ ] lien lh='ls -lah'
- \[ ] alias 'ls -lah'=lh
- \[ ] lh | ls -lah

#### Q70. Quelle instruction imprimera tous les fichiers .cvs complets dans le répertoire de base ou les sous-répertoires sans afficher d’erreurs ?

- \[ ] trouver $USER_DIR -name « \*.csv » 2>/dev/null
- \[ ] trouver $HOME -name « \*.csv » 1>/dev/null
- \[x] trouver $HOME -name « \*.csv » 2>/dev/null
- \[ ] trouver HOME -name « \*.csv » 1>/dev/null

#### Q71. Dans Bash, qu’est-ce qu’un # à la fin de la chaîne d’invite par défaut indique ?

- \[x] que l’utilisateur agit en tant que root
- \[ ] que le répertoire de travail actuel est la racine du système de fichiers
- \[ ] qu’il existe des mises à jour pour le système disponibles
- \[ ] que l’utilisateur n’est pas privilégié

#### Q72. Quelle sera la sortie de cette commande ?

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

Le caret (`^`) annule ici les correspondances à l’intérieur du crochet. [Référence](https://tldp.org/LDP/abs/html/globbingref.html)

#### Q73. Quelle est la sortie de cette séquence de commandes ?

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

#### Q74. Qu’y aurait-il dans l’out.txt?

```bash
#!/bin/bash

echo 123446789 > out.txt
exec 3<> out.txt
read -n 4 <&3
echo -n 5 >&3
exec 3>&-
```

- \[ ] 123446789
- \[ ] le symbole du trait d’union (-)
- \[x] 123456789
- \[ ] le chiffre 5, qui est écrit dans le fichier à l’aide de l’écho

Voir [Redirection d’E/S](https://tldp.org/LDP/abs/html/io-redirection.html)

Voir aussi : [Quelle est la différence entre « echo » et « echo -n » ?](https://stackoverflow.com/questions/30761986/what-is-the-difference-between-echo-and-echo-n)

#### Q75. Quelle variable contient l’ID de processus (PID) du script pendant son exécution ?

- \[ ] $ID
- \[ ] $ #
- \[ ] $ @
- \[x] $$

#### Q76. En combinant le globbing étendu et l’expansion des paramètres, quelle serait la valeur de la VAR ?

    #!/bin/bash
    shopt -s extglob
    VAR='     This is...     a string of characters     '
    VAR=${VAR##+([[:space:]])}; VAR=${VAR%%+([[:space:]])};
    echo "$VAR"

- \[ ] `<pre> This is... a string of characters</pre>`
- \[ ] `<pre> This is...a string of characters</pre>`
- \[ ] `<pre>This is... a string of characters</pre>`
- \[ ] `<pre>This is...a string of characters</pre>`

Références:

1.  [Quelle est la signification de la syntaxe ${0##...} avec variable, accolades et caractère de hachage en bash ?](https://stackoverflow.com/questions/2059794/what-is-the-meaning-of-the-0-syntax-with-variable-braces-and-hash-chara)
2.  [Que signifie développer une variable comme « ${var%%r\*} » en bash ?](https://stackoverflow.com/questions/41859601/what-does-expanding-a-variable-as-varr-mean-in-bash)

#### Q77. Quel opérateur indique au shell d’exécuter une commande donnée en arrière-plan ?

- \[ ] !
- \[ ] &&
- \[x] &
- \[ ] $
