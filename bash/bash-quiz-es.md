## Juerga

#### P1. ¿Cuál de los tres métodos copiará el directorio llamado "photo dir" recursivamente desde el directorio de inicio del usuario a /backups?

```bash
cp -R "~/photo dir" /backups #method1
cp -R ~"/photo dir" /backups #method2
cp -R ~/"photo dir" /backups #method3
```

- \[ ] Ninguno de los tres métodos se expandirá al directorio de inicio del usuario. Solo usando `"$HOME/photo dir"`tendrá éxito.
- \[ ] Sólo el método 1 se expandirá `"~/"` al directorio principal del usuario y, a continuación, agregue el nombre del directorio citado que incluye un espacio.
- \[ ] Sólo el método 2 se expandirá `"~/"` al directorio principal del usuario y, a continuación, agregue el nombre del directorio citado que incluye un espacio.
- \[x] Sólo el método 3 se expandirá `"~/"` al directorio principal del usuario y, a continuación, agregue el nombre del directorio citado que incluye un espacio.

#### P2. Si se ejecuta script.sh en el directorio actual, se producirá un error. ¿Por qué?

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

- \[ ] ls: no se puede acceder a un archivo inexistentearchivo: No existe tal archivo o directorio
- \[x] El bucle for se dividirá en los límites de las palabras y beach photo1.jpg tiene un espacio en él.
- \[ ] El comando mv fallará porque el corchete rizado es un carácter especial en Bash y no se puede usar en los nombres de los archivos.
- \[ ] La ejecución de script.sh se realizará correctamente ya que el comando ls crea una lista de archivos en el directorio actual y para bucles a través de esa lista, cambie el nombre de los archivos con una extensión .bak.

#### P3. Para ejecutar un comando copy en un subshell, ¿qué sintaxis usaría?

- \[x] `( command )`
- \[ ] `sh command`
- \[ ] `{ command; }`
- \[ ] `(( command ))`

#### P4. Usando "awk", ¿cuál sería la salida de esta cadena de comandos?

```bash
echo "1 2 3" | awk '{for (i=1; i<=NF; i++) s=s+$i};END {print s}'
```

- \[x] 6
- \[ ] 123
- \[ ] 3
- \[ ] 600

#### P5. El siguiente comando buscará en el sistema de archivos raíz los archivos llamados "finance.db". En este contexto, ¿qué información se envía a /dev/null?

```bash
find / -name "finance.db" 1>results.txt 2>/dev/null
```

- \[ ] los nombres de los archivos que no coinciden con las finanzas.db
- \[x] información enviada al error estándar, por ejemplo, errores que el comando find muestra a medida que se ejecuta
- \[ ] los nombres de los archivos que coinciden con las finanzas.db
- \[ ] información enviada a la salida estándar, es decir, la ruta de acceso a los archivos que ha localizado el comando find

#### P6. Para eliminar permanentemente las líneas vacías de un archivo llamado textfile, ¿qué comando podría usar?

- \[x] `sed -i '/^$/d' textfile`
- \[ ] `sed '/^$/d' textfile`
- \[ ] `cat textfile | sed '/^$/d`
- \[ ] `sed -i 's/^$//' textfile`

#### P7. Suponiendo que el usuario1 existiera, ¿cuál sería el resultado de esta cadena de comandos?

```bash
awk -F: '/user1/{print $1 "-" $3 "-" $6}' /etc/passwd
```

- \[ ] Mostraría el nombre de usuario, el UID y el directorio de inicio del usuario1 separados por dos puntos.
- \[ ] Imprimiría el UID, GID y el directorio de inicio del usuario1 separados por guiones.
- \[ ] Imprimiría el UID, el comentario y el directorio de inicio del usuario1 separados por guiones.
- \[x] Mostraría el nombre de usuario, el UID y el directorio de inicio del usuario1 separados por guiones.

#### P8. ¿Qué sucede si utiliza el `"set -e"` en un script Bash?

- \[ ] Hará que Bash salga si una función o subshell devuelve un código de estado distinto de cero.
- \[ ] Hará que Bash salga si un condicional devuelve un código de estado distinto de cero.
- \[ ] Hará que Bash se cierre si las asignaciones locales, declaradas o tipográficas devuelven un código de estado distinto de cero.
- \[x] Hará que Bash salga si un comando, una lista de comandos, un comando compuesto o potencialmente una canalización devuelve un código de estado distinto de cero.

#### P9. El **\_** keyword pausa el script para obtener entrada de la entrada estándar.

- \[ ] obtener
- \[ ] argumento
- \[x] leer
- \[ ] entrada

#### P10. Si file.sql contiene instrucciones SQL para ser ejecutadas, ¿qué habrá en file.txt?

```bash
mysql < file.sql > file.txt
```

- \[ ] una copia del contenido del archivo.sql
- \[ ] un error que indica que esta es una sintaxis no válida
- \[ ] el resultado de error del comando MySQL
- \[x] la salida sin error del comando MySQL

**Nota:** consulte la siguiente pregunta para obtener una variante.

#### P11. ¿Cuál será la diferencia entre la salida en pantalla y el contenido de out.txt

```bash
mysql < file.sql > out.txt
```

- \[ ] La salida en la pantalla será idéntica a la salida.txt
- \[x] No habrá salida en la pantalla ya que se está redirigiendo a out.txt.
- \[ ] La salida en la pantalla será idéntica a out.txt más números de línea.
- \[ ] El archivo out.txt contendrá STDERR y STDOUT irá a la pantalla.

**Nota:** consulte la pregunta anterior para ver si hay una variante.

#### P12. ¿Cómo afecta el SUID o setuid a los comandos ejecutables?

- \[ ] Cuando el comando crea archivos, estos serán propiedad del propietario del grupo del comando.
- \[ ] El bit SUID permite a cualquiera ejecutar el comando sin importar qué otros permisos se establezcan.
- \[x] Cuando se ejecuta el comando, sus privilegios de ejecución se elevan al usuario propietario del comando.
- \[ ] Cuando se ejecuta el comando, sus privilegios de ejecución se elevan al propietario del grupo del comando.

#### P13. Para extraer texto de la primera columna del archivo llamada textfile, ¿qué comando usaría?

- \[ ] `cat {$1,textfile}`
- \[ ] `cat textfile | awk [print $1]`
- \[x] `cat textfile | awk '{print $1}'`
- \[ ] `awk textfile {print $1}`

#### P14. ¿Cuál es el método abreviado de teclado para llamar a la búsqueda del historial de Bash como se muestra a continuación?

```bash
(reverse-i-search)`':
```

- \[ ] Esc + R
- \[ ] Ctrl + H
- \[x] Ctrl + R
- \[ ] Alt + R

#### P15. ¿Qué expresión aritmética dará la respuesta más precisa?

- \[ ] `var=$( expr 10 / 8 )`
- \[ ] `(( var= 10 /8 ))`
- \[ ] `var=$(( 10 / 8 ))`
- \[x] `var=$(echo 'scale=2; 10 / 8' | bc)`

#### P16. ¿Cuál es el resultado de este script?

```bash
txt=Penguins
[[ $txt =~ [a-z]{8} ]]; echo $?
```

- \[ ] 0, que representa 'true', porque la variable "txt" contiene ocho letras
- \[ ] 0, que representa 'verdadero', ¡porque todo el mundo ama a los pingüinos!
- \[ ] 1, que representa 'false', porque la variable "txt" es más larga que ocho caracteres
- \[x] 1, que representa 'false', porque la variable "txt" no contiene ocho letras minúsculas entre a y z

#### P17. ¿Cómo cambiaría su mensaje de shell bash a lo siguiente?

```bash
HAL>
```

- \[ ] `SHELL="HAL\>"`
- \[ ] `SHELL="HAL>"`
- \[x] `export PS1="HAL>"`
- \[ ] `PS1="HAL\>"`

#### P18. ¿Cuál es la salida de este código?

```bash
VAR="/var/www/html/website.com/html/"
echo "${VAR#*/html}"
```

- \[x] `/website.com/html/`
- \[ ] `/html/website.com/html/`
- \[ ] `/var/www/html/website.com/`
- \[ ] Nada se hará eco en la pantalla.

#### P19. Si se le solicita texto en la entrada estándar, puede decirle al comando que ha terminado de ingresar texto con qué combinación de teclas.

- \[ ] Ctrl + A (Windows) o Comando + A (Mac)
- \[ ] Ctrl + E (Windows) o Comando + E (Mac)
- \[x] Ctrl + D (Windows) o Comando + D (Mac)
- \[ ] Ctrl + Z (Windows) o Comando + Z (Mac)

#### P20. Para que un script Bash se ejecute como un comando del sistema operativo, debe comenzar con una línea shebang. ¿Cómo es esto?

- \[x] `#!/usr/bin/env bash`
- \[ ] `~/usr/bin/env bash`
- \[ ] `'$!/usr/bin/env bash`
- \[ ] `#/usr/bin/env bash`

#### P21. ¿Qué línea del script Bash probablemente produjo el resultado que se muestra a continuación?

```bash
The date is: Sun Mar 24 12:30:06 CST 2019!
```

- \[ ] `echo "The date is: !"`
- \[ ] `echo "The date is: date!"`
- \[ ] `echo "The date is: (date)!"`
- \[x] `echo "The date is: $(date)!"`

#### P22. Supongamos que su directorio de trabajo actual es su directorio de inicio. ¿Cómo podría ejecutar el script demo.sh que se encuentra en su directorio principal? Encuentra tres respuestas correctas.

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

#### P23. ¿Cómo podría obtener una lista de todos los archivos .html en su árbol?

- \[ ] `find . -type html`
- \[ ] `find . -name *.html`
- \[ ] `find *.html`
- \[x] `find . -name \*.html -print`

El segundo parece estar bien, pero expandirá el \* si hay algún archivo de .html en su directorio de trabajo.

#### P24. ¿Qué habría fuera.txt?

```bash
cat < in.txt > out.txt
```

- \[ ] La salida de la línea de comandos. Por defecto, STDIN proviene del teclado.
- \[ ] Nada porque no puede redirigir desde el archivo (in.txt) a otro archivo (out.txt). Solo puede redirigir desde un comando a un archivo.
- \[x] Sería el contenido de in.txt.
- \[ ] Nada. La redirección creará un nuevo archivo vacío, pero no habrá ninguna salida del comando cat para redirigir.

#### P25. ¿Qué hace esta declaración bash?

```bash
(( $a == $b ))
echo $?
```

- \[ ] Se repite entre los valores de `$a` y `$b`.
- \[x] Prueba si los valores de las variables `$a` y `$b` son iguales.
- \[ ] Vuelve `$b` si es mayor que `$a`.
- \[ ] Vuelve `$a` si es mayor que `$b`.

#### P26. ¿Qué usas en una declaración de caso para decirle a Bash que has terminado con una prueba específica?

- \[x] `; ;`
- \[ ] `: :`
- \[ ] `done`
- \[ ] `$$`

#### P27. ¿Qué representa el asterisco en esta declaración?

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

- \[x] un caso que coincide con cualquier valor, proporcionando una opción predeterminada si nada más captura ese valor
- \[ ] un caso solo para lo que sucede cuando el carácter del asterisco se pasa al guión
- \[ ] la acción de todos los demás asuntos combinados
- \[ ] una acción que se realiza para cualquier entrada, incluso si coincide con una condición especificada

#### P28. ¿Qué script Bash creará correctamente estos archivos?

- \[ ] `touch file{1+10}.txt`
- \[ ] `touch file{1-10}.txt`
- \[x] `touch file{1..10}.txt`
- \[ ] `touch file(1..10).txt`

#### P29. ¿Qué variable comprobaría para comprobar que el último comando se ejecutó correctamente?

- \[ ] `$$`
- \[x] `$?`
- \[ ] `$!`
- \[ ] `$@`

#### P30. ¿Cuál es el resultado de este script?

```bash
#!/bin/bash
fname=john
john=thomas
echo ${!fname}
```

- \[ ] juan
- \[x] tomás
- \[ ] Error de sintaxis
- \[ ] en blanco

[referencia](https://unix.stackexchange.com/questions/41292/variable-substitution-with-an-exclamation-mark-in-bash)

#### P31. ¿Cuál será el resultado de este script?

![question](images/Q30/question.png?raw=png)

- \[ ] `A` ![A](images/Q30/A.png?raw=png)
- \[ ] `B` ![B](images/Q30/B.png?raw=png)
- \[x] `C` ![C](images/Q30/C.png?raw=png)
- \[ ] `D` ![D](images/Q30/D.png?raw=png)

Aquí hay una versión basada en texto de Q.30:

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

#### P32. ¿Qué tiene de malo este script?

```bash
#!/bin/bash
read -p "Enter your pet type." PET
if [ $PET = dog ] ;then
    echo "You have a dog"
fi
```

- \[ ] Si el valor de PET no coincide con dog, el script devolverá un código de estado distinto de cero.
- \[ ] No hay nada de malo en ello. La condición comprueba perfectamente el valor del PET.
- \[x] Fallará si el usuario presiona la tecla Enter (Return) sin ingresar un nombre de mascota cuando se le solicite.
- \[ ] La declaración de entonces debe estar en una línea separada.

#### P33. ¿Cómo se puede reunir la historia de varios terminales?

- \[ ] Simplemente funciona por defecto.
- \[ ] `history --shared`
- \[ ] `history --combined`
- \[x] `shopt -s histappend`

#### P34. ¿Cuál es la diferencia entre las variables $@ y $\*?

- \[x] `$@` trata cada argumento citado como una entidad separada. `$*` trata toda la cadena de argumentos como una entidad.
- \[ ] `$*` trata cada argumento citado como una entidad separada. `$@` trata toda la cadena de argumentos como una entidad.
- \[ ] `$*` se utiliza para contar los argumentos pasados a un script, `$@` proporciona todos los argumentos en una cadena.
- \[ ] `$*` es el comodín que incluye todos los argumentos con división de palabras, `$@` contiene los mismos datos pero en una matriz.

#### P35. ¿Qué comando se está ejecutando en este script para comprobar si existe file.txt?

```bash
if [ -f file.txt ]; then
    echo "file.txt exists"
fi
```

- \[ ] `/usr/bin/test`
- \[ ] `/usr/bin/[`
- \[x] `the built-in [ command`
- \[ ] `/usr/bin/[[`

#### P36. ¿Cuál será el resultado de este script?

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

#### P37. ¿Qué archivo le permite guardar modificaciones en el entorno de shell en todas las sesiones?

- \[ ] `/etc/bash.conf`
- \[x] `~/.profile`
- \[ ] `/etc/bashprofile`
- \[ ] `~/profile`

#### P38. Dados los permisos enumerados en los datos.txt ¿es posible que el usuario2 pueda tener permisos de lectura, escritura y ejecución en los datos.txt?

```bash
$ ls -l
total 0
-rwx------+ 1 user1 user1 0 Oct 27 10:54 data.txt
```

- \[ ] No, está claro que user2 no tiene permisos de lectura, escritura y ejecución.
- \[x] Sí, el `+` al final de la cadena de permisos de 10 dígitos significa que hay una lista de control de acceso. Esto podría dar a user2 permisos no visibles por `ls -l`.
- \[ ] Es posible que SELinux proporcione permisos de lectura, escritura y ejecución para el usuario2 que no son visibles con `ls -l`.
- \[ ] Sí, el `+` al final de la cadena de permisos de 10 dígitos significa que hay un conjunto de atributos extendido. Esto podría otorgar a user2 permisos para leer, escribir y ejecutar datos.txt.

#### P39. ¿Qué logra este script?

```bash
#!/bin/bash
declare -A ARRAY=([user1]=bob [user2]=ted [user3]=sally)
KEYS=(${!ARRAY[@]})

for (( i=0; $i < ${#ARRAY[@]}; i+=1 ));do
        echo ${KEYS[$i]} - ${ARRAY[${KEYS[$i]}]}
done
```

- \[ ] Ordena la matriz asociativa denominada ARRAY y almacena los resultados en una matriz indexada denominada KEYS. A continuación, utiliza esta matriz ordenada para recorrer la matriz asociativa ARRAY.
- \[x] Usando un estilo C para el bucle, recorre la matriz asociativa denominada ARRAY utilizando las claves de la matriz asociativa y genera tanto la clave como los valores de cada elemento.
- \[ ] Crea una matriz indexada de la matriz asociativa denominada ARRAY. A continuación, utiliza un estilo C para el bucle y la matriz indexada para recorrer todos los elementos de la matriz asociativa, emitiendo la clave y el valor de cada elemento de la matriz utilizando el número de índice.
- \[ ] Crea una matriz asociativa llamada ARRAY, que recorre utilizando un estilo C para bucle y los números de índice de cada elemento en las claves de la matriz asociativa, emitiendo el valor de cada elemento.

#### P40. ¿Qué archivo coincidiría con el código a continuación?

```bash
ls Hello[[.vertical-line.]]World
```

- \[ ] Nada, este es un archivo glob no válido.
- \[ ] `Hello.vertical-line.World`
- \[ ] `Hello[[.vertical-line.]]World`
- \[x] `Hello|World`

#### P41. ¿Qué habrá fuera.txt?

```bash
ls nonexistentfile | grep "No such file" > out.txt
```

- \[ ] No existe tal archivo
- \[ ] ls: no se puede acceder a un archivo inexistentearchivo: No existe tal archivo o directorio
- \[x] Nada, fuera.txt estará vacío.
- \[ ] Será el contenido del archivo inexistente.

#### P42. Para que el script imprima "Es numérico" en la pantalla, ¿qué tendría que ingresar el usuario cuando se le solicite?

```bash
#!/bin/bash
read -p "Enter text " var
if [[ "$var" =~ "^[0-9]+$" ]];then
    echo "Is numeric"
else
    echo "Is not numeric"
fi
```

- \[ ] Cualquier secuencia de caracteres que incluya un entero
- \[ ] El usuario tendría que introducir la secuencia de caracteres de `^[0-9]]+$` Solo esto demostrará ser cierto y "Es numérico" se imprimirá en la pantalla debido a una sintaxis incorrecta. Al encapsular la expresión regular entre comillas dobles, todas las coincidencias fallarán, excepto la cadena de texto `^[0-9]+$`
- \[ ] Uno o más caracteres que solo incluyen enteros
- \[x] Debido a un error de sintaxis es imposible conseguir que el script imprima "Es numérico"

El regex no debe ser cotizado para funcionar correctamente.

#### P43. ¿Cómo encontraría el último comando de copia ejecutado en su historial?

- \[ ] historia | encontrar cp
- \[x] | de historia grep cp
- \[ ] historia de grep cp
- \[ ] historia de cp

#### P44. Para escribir un script que itera a través de los archivos en un directorio, ¿cuál de los siguientes podría usar?

- \[x] `bash for i in $(ls); do ... done`
- \[ ] `bash for $(ls); do ... done`
- \[ ] `bash for i in $ls; do ... done`
- \[ ] `bash for $ls; do ... done`

#### P45. Al ejecutar un comando y pasar la salida de ese comando a otro comando, ¿qué carácter le permite encadenar estos comandos?

- \[x] |
- \[ ] ->
- \[ ] #
- \[ ] @

#### P46. En el script que se muestra a continuación, ¿qué es **saludo**?

```bash
#!/usr/bin/env bash
greeting="Hello"
echo $greeting, everybody!
```

- \[ ] un comando
- \[ ] un bucle
- \[ ] un parámetro
- \[x] una variable

#### P47. ¿Qué instrucción comprueba si la variable num es mayor que cinco?

- \[ ] `(( num -gt 5 ))`
- \[ ] `[[$num -lt 5]]`
- \[x] `(( num > 5 ))`
- \[ ] `num > 5`

[referencia](https://tldp.org/LDP/abs/html/dblparens.html)

#### P48. Usando Bash extended globbing, ¿cuál será la salida de este comando?

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

[referencia](https://www.linuxjournal.com/content/bash-extended-globbing)

#### Pregunta 49. Cuando se usa desde dentro de un script, ¿qué variable contiene el nombre del script?

- \[x] $0
- \[ ] $# // número de parámetros posicionales
- \[ ] $$ // pid de la cáscara actual
- \[ ] $@ // Construcción tipo matriz de todos los parámetros posicionales

#### Pregunta 50. ¿Qué significa el + al final de los permisos de archivo de 10 dígitos en los datos.txt?

```bash
ls -l
-rwx------+ 1 user1 u1 0 Oct 1 10:00 data.txt
```

- \[ ] Existe un contexto de seguridad selinux
- \[ ] El bit pegajoso está configurado y el archivo permanecerá en la RAM para mayor velocidad
- \[x] Hay una lista de control de acceso
- \[ ] Hay un atributo extendido como conjunto inmutable

#### Pregunta 51. En Bash, ¿qué hace el comentario a continuación?

```bash
cd -
```

- \[x] Te mueve al directorio en el que estabas anteriormente.
- \[ ] Lo mueve a su carpeta de inicio (sea cual sea su directorio de trabajo actual).
- \[ ] Elimina el directorio actual
- \[ ] Te mueve un directorio por encima de tu directorio de trabajo actual.

#### P52. ¿Qué hace este comando?

```bash
cat > notes -
```

- \[x] Acepta texto de entrada estándar y lo coloca en "notas"
- \[ ] Crea "notas" y sale
- \[ ] Genera el contenido de las notas y lo elimina
- \[ ] Añade texto a las "notas" existentes

#### Pregunta 53. ¿Cuál es el resultado de:

```bash
VAR="This old man came rolling"
echo "\${VAR//man/rolling}"
```

- \[x] Este viejo rollo vino rodando
- \[ ] Este anciano vino hombre
- \[ ] Este anciano vino rodando
- \[ ] Este viejo vino

#### Pregunta 54. El shell examina el contenido de una variable en particular para identificar qué programas puede ejecutar. ¿Cuál es el nombre de esta variable?

- \[ ] $INCLUDE
- \[x] $PATH
- \[ ] $PROGRAM
- \[ ] $PATHS

#### Pregunta 55. ¿Qué instrucción usarías para imprimir esto en la consola?

`Shall we play a game? yes\no`

- \[ ] `echo "Shall we play a game? yes/\no"`
- \[ ] `echo "Shall we play a game\? yes\\no"`
- \[x] `echo "Shall we play a game? yes\\no"`
- \[ ] `echo "Shall we play a game? yes\no"`

#### Pregunta 56. Dado un directorio con estos siete archivos, ¿qué quedaría después de ejecutar estos comandos?

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

Todos estos archivos serán eliminados

- \[x] d:

```bash
image1.gif
image1.jpg
image2.gif
image2.jpg
```

#### Pregunta 57. El código a continuación parece funcionar y genera "8 es mayor que 5". Sin embargo, ¿qué resultado inesperado le dirá que no está funcionando correctamente?

```bash
#!/bin/bash
var="8"
if [ $var > 5 ]; then
    echo "$var is greater than 5"
fi
```

- \[ ] No habrá resultados inesperados. Este script funciona tal cual y la salida será "8 es mayor que 5".
- \[ ] La comparación no podrá manejar números de coma flotante, ya que Bash solo maneja enteros. Por lo tanto, este ejemplo generará un mensaje de error si el valor de $var se cambia a "8.8".
- \[x] Habrá un archivo en el directorio actual denominado 5.
- \[ ] La variable $var no se cita, lo que conducirá a la división de palabras. Este script fallará con un mensaje de "operador unario esperado" si cambia el valor de

#### Pregunta 58. ¿Cuál es el resultado de este script?

![question](images/Q60/question.png?raw=png)

- \[ ] Elimina el directorio 'foo' y los archivos contenidos en él.
- \[ ] Elimina todos los archivos excepto los del directorio actual.
- \[x] Elimina todos los archivos del directorio actual.
- \[ ] Elimina todos los archivos excepto los del directorio 'foo'.

#### Pregunta 59. ¿Cuál es la verdadera?

- \[x] Las reglas de la política de SELinux se comprueban después de las reglas de DAC.
- \[ ] Las reglas de la política de SELinux se comprueban antes de las reglas de DAC
- \[ ] Las reglas de la política de SELinux nunca se comprueban después de las reglas de DAC.
- \[ ] Ninguno de estos

[referencia](https://unix.stackexchange.com/questions/16828/what-roles-do-dac-file-permissions-acl-and-mac-selinux-play-in-linux-file-s)

#### P60. ¿Qué hace el siguiente comando?

```bash
w
```

- \[ ] No muestra información sobre los usuarios actualmente en la máquina.
- \[x] Muestra información sobre los usuarios actualmente en la máquina.
- \[ ] Muestra información sobre los usuarios actualmente en la otra máquina.
- \[ ] Ninguno de estos

#### P61. ¿Qué opciones de sed debe usar para cambiar la penúltima instancia de la variable a rock para que diga:

Una constante es una variable que es una roca que no es variable

```bash
var="A constant is a variable that is a variable that isn't variable"
echo "$var" | sed _____
```

- \[x] s/(.\*)variable(.\*variable)/\1rock\2/'
- \[ ] s/variable/roca/'
- \[ ] s/variable/roca/g'
- \[ ] s/(.\*)variable(.\*variable)/\1rock\2/'

#### P62. Para hacer que un script Bash llamado script.sh ejecutable, ¿qué debe ejecutar?

- \[ ] script.sh ejecutiva
- \[x] chmod +x script.sh
- \[ ] bash script.sh
- \[ ] fuente script.sh

#### P63. ¿Cómo se puede crear un terminal compartido en un shell Bash?

- Pantalla \[x]
- \[ ] pantalla -X
- \[ ] pantalla --compartida
- \[ ] terminal -compartido

#### Pregunta 64. ¿Qué operador envía la salida de ls a un archivo para su uso posterior?

- \[ ] ls < lista de archivos.txt
- \[ ] ls ¦ lista de archivos.txt
- \[x] lista de archivos de > ls.txt
- \[ ] ls - lista de archivos.txt

#### Pregunta 65. Al comparar los ítems con el caso, ¿qué afirmación indica el fin del bloque de evaluación?

- \[ ] parada
- \[x] esac
- \[ ] hecho
- \[ ] salida

#### Pregunta 66. Para ejecutar un grupo de comandos sin generar un subshell, ¿qué sintaxis usaría?

- \[ ] comando sh1; comando2
- \[ ] { comando1; comando2; }
- \[ ] (( comando1; comando2 ))
- \[x] comando1; comando2

#### Pregunta 67. ¿Cuáles son los resultados del comando con un usuario llamado jon?

```bash
echo 'Hello, $(whoami)!'
```

- \[ ] ¡Hola, $(jon)!
- \[ ] ¡Hola, jon!
- \[x] ¡Hola, $(whoami)!
- \[ ] ¡Hola, whoami!

#### Pregunta 68. ¿Cómo se puede copiar un directorio a otro sistema con compresión?

- \[ ] tar -ssh user@192.158.1.1 /bin/newfile
- \[x] tar cvzf - /wwwdata | ssh root@192.168.1.201 "dd of=/backup/wwwdata.tar.gz"
- \[ ] No se puede comprimir la secuencia
- \[ ] Directorio scp -r user@192.168.1.1:/tmp

#### Pregunta 69. Para asignar el comando `ls -lah` al comando de acceso directo `lh`, ¿qué comando debe usar?

- \[x] alias lh='ls -lah'
- \[ ] enlace lh='ls -lah'
- \[ ] alias 'ls -lah'=lh
- \[ ] lh | ls -lah

#### Pregunta 70. ¿Qué instrucción imprimirá todos los archivos .cvs completos en el directorio principal o subdirectorios sin mostrar ningún error?

- \[ ] buscar $USER_DIR -name "\*.csv" 2>/dev/null
- \[ ] buscar $HOME -name "\*.csv" 1>/dev/null
- \[x] buscar $HOME -name "\*.csv" 2>/dev/null
- \[ ] encontrar HOME -name "\*.csv" 1>/dev/null

#### P71. En Bash, ¿qué indica un # al final de la cadena de solicitud predeterminada?

- \[x] que el usuario está actuando como root
- \[ ] que el directorio de trabajo actual es la raíz del sistema de archivos
- \[ ] que hay actualizaciones disponibles para el sistema
- \[ ] que el usuario no tiene privilegios

#### P72. ¿Cuál será el resultado de este comando?

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

El caret (`^`) aquí niega las coincidencias dentro del corchete. [Referencia](https://tldp.org/LDP/abs/html/globbingref.html)

#### Pregunta 73. ¿Cuál es la salida de esta secuencia de comandos?

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

#### Pregunta 74. ¿Qué habría fuera.txt?

```bash
#!/bin/bash

echo 123446789 > out.txt
exec 3<> out.txt
read -n 4 <&3
echo -n 5 >&3
exec 3>&-
```

- \[ ] 123446789
- \[ ] el símbolo de guión (-)
- \[x] 123456789
- \[ ] el número 5, que se escribe en el archivo usando echo

Ver [Redirección de E/S](https://tldp.org/LDP/abs/html/io-redirection.html)

Ver también: [¿Cuál es la diferencia entre "eco" y "eco -n"?](https://stackoverflow.com/questions/30761986/what-is-the-difference-between-echo-and-echo-n)

#### Pregunta 75. ¿Qué variable contiene el ID de proceso (PID) del script mientras se está ejecutando?

- \[ ] $ID
- \[ ] $ #
- \[ ] $ @
- \[x] $$

#### Pregunta 76. Al combinar el globbing extendido y la expansión de parámetros, ¿cuál sería el valor del VAR?

    #!/bin/bash
    shopt -s extglob
    VAR='     This is...     a string of characters     '
    VAR=${VAR##+([[:space:]])}; VAR=${VAR%%+([[:space:]])};
    echo "$VAR"

- \[ ] `<pre> This is... a string of characters</pre>`
- \[ ] `<pre> This is...a string of characters</pre>`
- \[ ] `<pre>This is... a string of characters</pre>`
- \[ ] `<pre>This is...a string of characters</pre>`

Referencias:

1.  [¿Cuál es el significado de la sintaxis ${0##...} con variable, llaves y carácter hash en bash?](https://stackoverflow.com/questions/2059794/what-is-the-meaning-of-the-0-syntax-with-variable-braces-and-hash-chara)
2.  [¿Qué significa expandir una variable como "${var%%r\*}" en bash?](https://stackoverflow.com/questions/41859601/what-does-expanding-a-variable-as-varr-mean-in-bash)

#### Pregunta 77. ¿Qué operador le dice al shell que ejecute un comando determinado en segundo plano?

- \[ ] !
- \[ ] &&
- \[x] y
- \[ ] $
