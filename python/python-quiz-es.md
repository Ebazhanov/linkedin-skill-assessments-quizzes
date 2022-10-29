## Python (lenguaje de programación)

#### P1. Que es una clase abstracta?

- [ ] Una clase abstracta es el nombre de cualquier clase desde la que puede instanciar un objeto.
- [ ] Las clases abstractas deben redefinirse cada vez que se crea una instancia de un objeto a partir de ellas.
- [ ] Las clases abstractas deben heredar de las clases concretas.
- [x] Una clase abstracta existe solo para que otras clases "concretas" puedan heredar de la clase abstracta.

[referencia](https://www.geeksforgeeks.org/abstract-classes-in-python/)

#### P2. ¿Qué sucede cuando usa la función incorporada `any()` en una lista?

- [ ] La función `any()` devolverá aleatoriamente cualquier elemento de la lista.
- [x] La función `any()` devuelve True si algún elemento de la lista se evalúa como True. De lo contrario, devuelve False.
- [ ] La función `any()` toma como argumentos la lista a verificar dentro y el elemento a verificar. Si "cualquiera" de los elementos de la lista coincide con el elemento a comprobar, la función devuelve True.
- [ ] La función `any()` devuelve un valor booleano que responde a la pregunta "¿Hay algún elemento en esta lista?"

**ejemplo**

```python
if any([True, False, False, False]) == True:
    print('Yes, there is True')
>>> 'Yes, there is True'
```

#### P3. ¿A qué estructura de datos degenera un árbol binario si no está equilibrado correctamente?

- [x] lista enlazada
- [ ] cola
- [ ] establecer
- [ ] dictado ordenado

[referencia](https://www.scaler.com/topics/linked-list/)

#### P4. ¿Qué afirmación sobre los métodos estáticos es verdadera?

- [ ] Los métodos estáticos se llaman estáticos porque siempre devuelven `None`.
- [ ] Los métodos estáticos pueden vincularse a una clase oa una instancia de una clase.
- [x] Los métodos estáticos sirven principalmente como métodos de utilidad o métodos auxiliares, ya que no pueden acceder ni modificar el estado de una clase.
- [ ] Los métodos estáticos pueden acceder y modificar el estado de una clase o una instancia de una clase.

[referencia](https://www.geeksforgeeks.org/class-method-vs-static-method-python)

#### P5. ¿Qué son los atributos?

- [ ] Los atributos son una versión larga de una declaración `if/else`, que se usa cuando se prueba la igualdad entre objetos.
- [x] Los atributos son una forma de contener datos o describir un estado para una clase o una instancia de una clase.
- [ ] Los atributos son cadenas que describen las características de una clase.
- [ ] Los argumentos de función se denominan "atributos" en el contexto de métodos de clase y métodos de instancia.

**Explicación** `Atributos definidos bajo la clase, los argumentos van bajo las funciones. los argumentos generalmente se refieren como parámetros, mientras que los atributos son el constructor de la clase o una instancia de una clase.

#### P6. ¿Cuál es el término para describir este código?

`recuento, fruta, precio = (2, 'manzana', 3,5)`

- [ ] `asignación de tupla`
- [x] `desempaquetado de tuplas`
- [ ] `coincidencia de tuplas`
- [ ] `duplicación de tuplas`

#### P7. ¿Qué método de lista integrado usaría para eliminar elementos de una lista?

- [ ] Método `.delete()`
- [ ] `pop(mi_lista)`
- [ ] `del(mi_lista)`
- [x] método `.pop()`

**ejemplo**

```python
my_list = [1,2,3]
my_list.pop(0)
my_list
>>>[2,3]
```

#### P8. ¿Cuál es uno de los usos más comunes de la biblioteca sys de Python?

- [x] para capturar los argumentos de la línea de comandos proporcionados en el tiempo de ejecución de un archivo
- [ ] para conectar varios sistemas, como conectar una interfaz web, un servicio API, una base de datos y una aplicación móvil
- [ ] para tomar una instantánea de todos los paquetes y bibliotecas en su entorno virtual
- [ ] para escanear la salud de su ecosistema de Python mientras está dentro de un entorno virtual

#### P9. ¿Cuál es el tiempo de ejecución para acceder a un valor en un diccionario usando su clave?

- [ ] O(n), también llamado tiempo lineal.
- [ ] O(log n), también llamado tiempo logarítmico.
- [ ] O(n^2), también llamado tiempo cuadrático.
- [x] O(1), también llamado tiempo constante.

#### P10. ¿Cuál es la sintaxis correcta para definir una clase llamada Game, si hereda de una clase padre llamada LogicGame?

- [x] `class Game(LogicGame): pass`
- [ ] `def Game(LogicGame): pass`
- [ ] `def Game.LogicGame(): pass`
- [ ] `class Game.LogicGame(): pass`

**Explicación:** `La clase principal que se hereda se pasa como argumento a la clase secundaria. Por lo tanto, aquí la primera opción es la respuesta correcta.`

#### P11. ¿Cuál es la forma correcta de escribir un doctest?

- [ ] A

```python
def sum(a, b):
    """
    sum(4, 3)
    7

    sum(-4, 5)
    1
    """
    return a + b
```

- [x] B

```python
def sum(a, b):
    """
    >>> sum(4, 3)
    7

    >>> sum(-4, 5)
    1
    """
    return a + b
```

- [ ] C

```python
def sum(a, b):
    """
    # >>> sum(4, 3)
    # 7

    # >>> sum(-4, 5)
    # 1
    """
    return a + b
```

- [ ] D

```python
def sum(a, b):
    ###
    >>> sum(4, 3)
    7

    >>> sum(-4, 5)
    1
    ###
    return a + b
```

**Explicación**: use `'''` para iniciar el documento y agregue la salida de la celda después de `>>>`

#### P12. ¿Qué tipo de datos integrado de Python se usa comúnmente para representar una pila (stack en Inglés [Referencia](https://docs.python.org/es/3/tutorial/datastructures.html?highlight=list%20stack#using-lists-as-stacks))?

- [ ] `set`
- [x] `list`
- [ ] `None`
- [ ] `dictionary`
- [ ] `Solo puedes construir una pila desde cero.`

#### P13. ¿Qué devolvería esta expresión?

```python
college_years = ['Freshman', 'Sophomore', 'Junior', 'Senior']
return list(enumerate(college_years, 2019))
```

- [ ] `[('Freshman', 2019), ('Sophomore', 2020), ('Junior', 2021), ('Senior', 2022)]`
- [ ] `[(2019, 2020, 2021, 2022), ('Freshman', 'Sophomore', 'Junior', 'Senior')]`
- [ ] `[('Freshman', 'Sophomore', 'Junior', 'Senior'), (2019, 2020, 2021, 2022)]`
- [x] `[(2019, 'Freshman'), (2020, 'Sophomore'), (2021, 'Junior'), (2022, 'Senior')]`

#### P14. ¿Cuál es el propósito de la palabra clave "self" al definir o llamar a métodos de instancia?

- [ ] `self` significa que no es necesario pasar ningún otro argumento al método.
- [ ] No hay un propósito real para el método `self`; es solo una jerga informática histórica que Python mantiene para mantenerse consistente con otros lenguajes de programación.
- [x] `self` se refiere a la instancia cuyo método fue llamado.
- [ ] `self` se refiere a la clase de la que se heredó para crear el objeto usando `self`.

**Ejemplo sencillo**

```python
class my_secrets:
    def __init__(self, password):
        self.password = password
        pass
instance = my_secrets('1234')
instance.password
>>>'1234'
```

#### P15. ¿Cuál de estas NO es una característica de las tuplas nombradas?

- [ ] Puede asignar un nombre a cada uno de los miembros de `namedtuple` y referirse a ellos de esa manera, de manera similar a como accedería a las claves en el `dictionary`.
- [ ] Cada miembro de un objeto de tupla con nombre se puede indexar directamente, como en una `tuple` normal.
- [ ] Las `namedtuples` son tan eficientes en memoria como las `tuple` regulares.
- [x] No se necesita importar para usar `namedtuples` porque están disponibles en la biblioteca estándar.

**Necesitamos importarlo usando**:`from collections import namedtuple`

#### P16. ¿Qué es un método de instancia?

- [x] Los métodos de instancia pueden modificar el estado de una instancia o el estado de su clase principal.
- [ ] Los métodos de instancia contienen datos relacionados con la instancia.
- [ ] Un método de instancia es cualquier método de clase que no acepta ningún argumento.
- [ ] Un método de instancia es una función normal que pertenece a una clase, pero debe devolver `Ninguno`.

#### P17. ¿Qué afirmación NO describe el concepto de encapsulación de la programación orientada a objetos?

- [ ] Protege los datos de interferencias externas.
- [ ] Se encapsula una clase principal y ningún dato de la clase principal pasa a la clase secundaria.
- [ ] Mantiene los datos y los métodos que pueden manipular esos datos en un solo lugar.
- [x] Solo permite cambiar los datos por métodos.

[Referencia](https://www.scaler.com/topics/python/encapsulation-in-python/)

#### P18. ¿Cuál es el propósito de una declaración if/else?

- [ ] Le dice a la computadora qué fragmento de código ejecutar si las instrucciones que codificaste son incorrectas.
- [ ] Ejecuta un fragmento de código si todas las importaciones fueron exitosas y otro fragmento de código si las importaciones no fueron exitosas.
- [x] Ejecuta un trozo de código si una condición es verdadera, pero un trozo de código diferente si la condición es falsa.
- [ ] Le dice a la computadora qué fragmento de código ejecutar si hay suficiente memoria para manejarlo, y qué fragmento de código ejecutar si no hay suficiente memoria para manejarlo.

[Referencia](https://www.scaler.com/topics/python/python-if-else-statement/)

#### P19. ¿Qué tipo de datos integrado de Python es el más adecuado para implementar una cola?

- [ ] diccionario
- [ ] conjuntos (`set` en Inglés [Referencia](https://docs.python.org/es/3/library/stdtypes.html#set)
- [ ] Ninguna. Solo puede crear una cola desde cero.
- [x] lista

#### P20. ¿Cuál es la sintaxis correcta para instanciar un nuevo objeto del tipo Juego?

- [ ] `mi_juego = class.Juego()`
- [ ] `mi_juego = class(Juego)`
- [x] `mi_juego = Juego()`
- [ ] `mi_juego = Juego.create()`

#### P21. ¿Qué hace la función integrada `map()`?

- [ ] Crea una ruta desde múltiples valores en un iterable a un solo valor.
- [x] Aplica una función a cada elemento en un iterable y devuelve el valor de esa función.
- [ ] Convierte un tipo de valor complejo en tipos de valor más simples.
- [ ] Crea un mapeo entre dos elementos diferentes de diferentes iterables.

**Explicación:** - La sinaxis para la función `map()` es `list(map(function,iterable))`. El buscador de área simple usando el mapa sería así

```python
import math
radius = [1,2,3]
area = list(map(lambda x: round(math.pi*(x**2), 2), radius))
area
>>> [3.14, 12.57, 28.27]
```

#### P22. Si no devuelve explícitamente un valor de una función, ¿qué sucede?

- [ ] La función devolverá un RuntimeError si no devuelve un valor.
- [x] Si la palabra clave de retorno está ausente, la función devolverá `None`.
- [ ] Si la palabra clave de retorno está ausente, la función devolverá `True`.
- [ ] La función entrará en un bucle infinito porque no sabrá cuándo dejar de ejecutar su código.

#### P23. ¿Cuál es el propósito de la instrucción `pass` en Python?

- [ ] Se utiliza para omitir la declaración `yield` de un generador y devolver un valor de Ninguno.
- [x] Es una operación nula utilizada principalmente como marcador de posición en funciones, clases, etc.
- [ ] Se utiliza para pasar el control de un bloque de instrucciones a otro.
- [ ] Se utiliza para omitir el resto de un ciclo `while` o `for` y volver al inicio del ciclo.

#### P24. ¿Cuál es el término que se usa para describir los elementos que se pueden pasar a una función?

- [x] argumentos
- [ ] paradigmas
- [ ] atributos
- [ ] decoradores

#### P25. ¿Qué tipo de colección se utiliza para asociar valores con claves únicas?

- [ ] `slot`
- [x] `dictionary`
- [ ] `queue`
- [ ] `sorted list`

#### P26. ¿Cuándo deja de iterar un bucle for?

- [ ] cuando encuentra un bucle infinito
- [ ] cuando encuentra una declaración if/else que contiene una palabra clave break
- [x] cuando ha evaluado cada elemento en el iterable en el que está trabajando o se encuentra una palabra clave de interrupción
- [ ] cuando el tiempo de ejecución del ciclo excede O(n^2)

#### P27. Suponiendo que el nodo está en una lista de enlaces únicos, ¿cuál es la complejidad del tiempo de ejecución de buscar un nodo específico dentro de una lista de enlaces únicos?

- [x] El tiempo de ejecución es O(n) porque, en el peor de los casos, el nodo que está buscando es el último nodo y se deben visitar todos los nodos de la lista enlazada.
- [ ] El tiempo de ejecución es O(nk), donde n representa el número de nodos yk representa la cantidad de tiempo que lleva acceder a cada nodo en la memoria.
- [ ] El tiempo de ejecución no se puede determinar a menos que sepa cuántos nodos hay en la lista de enlaces individuales.
- [ ] El tiempo de ejecución es O(1) porque puede indexar directamente a un nodo en una lista enlazada individualmente.

#### P28. Dada la siguiente lista de tres, ¿cómo crearía una nueva lista que coincida con el resultado deseado impreso a continuación?

```python
fruits = ['Apples', 'Oranges', 'Bananas']
quantities = [5, 3, 4]
prices = [1.50, 2.25, 0.89]

#Desired output
[('Apples', 5, 1.50),
('Oranges', 3, 2.25),
('Bananas', 4, 0.89)]
```

- [ ] A

```python
output = []

fruit_tuple_0 = (first[0], quantities[0], price[0])
output.append(fruit_tuple)

fruit_tuple_1 = (first[1], quantities[1], price[1])
output.append(fruit_tuple)

fruit_tuple_2 = (first[2], quantities[2], price[2])
output.append(fruit_tuple)

return output
```

- [x] B

```python
i = 0
output = []
for fruit in fruits:
    temp_qty = quantities[i]
    temp_price = prices[i]
    output.append((fruit, temp_qty, temp_price))
    i += 1
return output
```

- [ ] C

```python
groceries = zip(fruits, quantities, prices)
return groceries

>>> [
('Apples', 5, 1.50),
('Oranges', 3, 2.25),
('Bananas', 4, 0.89)
]
```

- [ ] D

```python
i = 0
output = []
for fruit in fruits:
    for qty in quantities:
        for price in prices:
            output.append((fruit, qty, price))
    i += 1
return output
```

#### P29. ¿Qué sucede cuando usa la función integrada all() en una lista?

- [ ] La función `all()` devuelve un valor booleano que responde a la pregunta "¿Son iguales todos los elementos de esta lista?
- [ ] La función `all()` devuelve True si todos los elementos de la lista se pueden convertir en cadenas. De lo contrario, devuelve False.
- [ ] La función `all()` devolverá todos los valores de la lista.
- [x] La función `all()` devuelve True si todos los elementos de la lista se evalúan como True. De lo contrario, devuelve False.

**Explicación** - `all()` devuelve verdadero si todo en la lista es Verdadero, vea el ejemplo a continuación

```python
test = [True,False,False,False]
if all(test) is True:
    print('Yeah all are True')
else:
    print('There is an imposter')
>>> 'There is an imposter'
```

#### P30. ¿Cuál es la sintaxis correcta para llamar a un método de instancia en una clase llamada Juego?

_(El formato de respuesta puede variar. Game and roll (o dice_roll) deben llamarse sin parámetros)._

- [x] A

```python
>>> dice = Game()
>>> dice.roll()
```

- [ ] B

```python
>>> dice = Game(self)
>>> dice.roll(self)
```

- [ ] C

```python
>>> dice = Game()
>>> dice.roll(self)
```

- [ ] D

```python
>>> dice = Game(self)
>>> dice.roll()
```

#### P31. ¿Qué es el paradigma algorítmico de clasificación rápida?

- [ ] retroceso
- [ ] programación dinámica
- [ ] disminuir y conquistar
- [x] divide y vencerás

#### P32. ¿Cuál es la complejidad del tiempo de ejecución del método integrado `.append()` de la lista?

- [x] O(1), también llamado tiempo constante
- [ ] O(log n), también llamado tiempo logarítmico
- [ ] O(n^2), también llamado tiempo cuadrático
- [ ] O(n), también llamado tiempo lineal

#### P33. ¿Cuál es la diferencia clave entre un 'conjunto' (`set` en Inglés) y una 'lista'?

- [ ] Un conjunto es una colección ordenada de elementos únicos. Una lista es una colección desordenada de elementos no únicos.
- [ ] Los elementos se pueden recuperar de una lista pero no se pueden recuperar de un conjunto.
- [ ] Un conjunto es una colección ordenada de elementos no únicos. Una lista es una colección desordenada de elementos únicos.
- [x] Un conjunto es una colección desordenada de elementos únicos. Una lista es una colección ordenada de elementos no únicos.

#### P34. ¿Cuál es la definición de abstracción aplicada a Python orientado a objetos?

- [ ] Abstracción significa que se puede usar un estilo de código diferente, ya que el programa ya conoce muchos detalles entre bastidores.
- [x] Abstracción significa que la implementación está oculta para el usuario y solo se muestran los datos o la información relevante.
- [ ] Abstracción significa que los datos y la funcionalidad de una clase se combinan en una sola entidad.
- [ ] Abstracción significa que una clase puede heredar de más de una clase padre.

#### P35. ¿Qué imprime esta función?

```python
def print_alpha_nums(abc_list, num_list):
    for char in abc_list:
        for num in num_list:
            print(char, num)
    return

print_alpha_nums(['a', 'b', 'c'], [1, 2, 3])
```

- [x] A

```python
a 1
a 2
a 3
b 1
b 2
b 3
c 1
c 2
c 3
```

- [ ] B

```python
['a', 'b', 'c'], [1, 2, 3]
```

- [ ] C

```python
aaa
bbb
ccc
111
222
333
```

- [ ] D

```python
a 1 2 3
b 1 2 3
c 1 2 3
```

#### P36. Elija la representación correcta de doctest para la función en Python.

- [ ] :

```python
def sum(a, b):
    # a = 1
    # b = 2
    # sum(a, b) = 3

    return a + b
```

- [ ] :

```python
def sum(a, b):
    """
    a = 1
    b = 2
    sum(a, b) = 3
    """

    return a + b
```

- [x] :

```python
def sum(a, b):
    """
    >>> a = 1
    >>> b = 2
    >>> sum(a, b)
    3
    """

    return a + b
```

- [ ] :

```python
def sum(a, b):
    '''
    a = 1
    b = 2
    sum(a, b) = 3
    '''
    return a + b
```

**Explicación:** Use `"""` para iniciar y finalizar la cadena de documentación y use `>>>` para representar la salida. Si escribe esto correctamente, también puede ejecutar la prueba de documentación usando el módulo de prueba de documentación incorporado

#### P37. Supongamos que una clase Game hereda de dos clases principales: BoardGame y LogicGame. ¿Qué afirmación es verdadera sobre los métodos de un objeto instanciado desde la clase Game?

- [ ] Al instanciar un objeto, el objeto no hereda ninguno de los métodos de la clase principal.
- [ ] Al crear una instancia de un objeto, el objeto heredará los métodos de la clase principal que tenga más métodos.
- [ ] Al crear una instancia de un objeto, el programador debe especificar de qué clase principal heredará los métodos.
- [x] Una instancia de la clase Game heredará los métodos que tengan las clases BoardGame y LogicGame.

#### P38. ¿Qué devuelve llamar a namedtuple en un tipo de colección?

- [ ] una clase de objeto genérico con campos de parámetros iterables
- [ ] una clase de objeto genérico con campos con nombre no iterables
- [ ] una subclase de tupla con campos de parámetros no iterables
- [x] una subclase de tupla con campos iterables con nombre

**Ejemplo**

```python
# la función namedtuple acepta los siguientes argumentos para generar una clase
desde colecciones importar namedtuple
>>> Point = namedtuple('Point',['x','y'])
>>> point = Point(100, 200)
>>> point
    Point(x=100, y=200)

# Lo que le permite usar tanto el desempaquetado como la iteración para acceder
>>> x, y = point
>>> print(f'({x}, {y})')
    (100, 200)
>>> for coordinate in point:
        print(coordinate)
    100
    200
```

[Referencia](https://www.geeksforgeeks.org/namedtuple-in-python/?ref=lbp)

#### P39. ¿Qué símbolo(s) usas para evaluar la igualdad entre dos elementos?

- [ ] `&&`
- [ ] `=`
- [x] `==`
- [ ] `||`

#### P40. Revise el código a continuación. ¿Cuál es la sintaxis correcta para cambiar el precio a 1,5?

```python
fruit_info = {
  'fruit': 'apple',
  'count': 2,
  'price': 3.5
}
```

- [x] `fruit_info ['price'] = 1.5`
- [ ] `my_list [3.5] = 1.5`
- [ ] `1.5 = fruit_info ['price]`
- [ ] `my_list['price'] == 1.5`

#### P41. ¿Qué valor devolvería esta comprobación de igualdad?

`5 != 6`

- [ ] `yes`
- [ ] `False`
- [x] `True`
- [ ] `None`

**Explicación** - `!=` es equivalente a **no igual a** en python

#### P42. ¿Qué hace el método `__init__()` de una clase?

- [ ] Hace que las clases se reconozcan entre sí si se define más de una clase en un solo archivo de código.
- [ ] Se incluye para preservar la compatibilidad con versiones anteriores de Python 3 a Python 2, pero ya no necesita usarse en Python 3.
- [x] Es un método que actúa como constructor y se llama automáticamente cada vez que se crea un nuevo objeto a partir de una clase. Determina el estado inicial de un objeto nuevo.
- [ ] Inicializa cualquier importación que haya incluido en la parte superior de su archivo.

**Ejemplo:**

```python
class test:
    def __init__(self):
        print('I came here without your permission lol')
        pass
t1 = test()
>>> 'I came here without your permission lol'
```

#### P43. ¿Qué significa la frase "complejidad del espacio"?

- [ ] `Cuántos microprocesadores se necesitarían para ejecutar su código en menos de un segundo`
- [ ] `Cuántas líneas de código hay en su archivo de código`
- [x] `La cantidad de espacio ocupado en la memoria en función del tamaño de entrada`
- [ ] `¿Cuántas copias del archivo de código caben en 1 GB de memoria`

#### P44. ¿Cuál es la sintaxis correcta para crear una variable vinculada a un diccionario?

- [x] `info_fruta = {'fruta': 'manzana', 'recuento': 2, 'precio': 3.5}`
- [ ] `info_fruta =('fruta': 'manzana', 'recuento': 2,'precio': 3.5 ).dict()`
- [ ] `info_fruta = ['fruta': 'manzana', 'recuento': 2, 'precio': 3.5 ].dict()`
- [ ] `info_fruta = to_dict('fruta': 'manzana', 'recuento': 2, 'precio': 3.5)`

#### P45. ¿Cuál es la forma correcta de escribir una lista de comprensión que represente todas las claves de este diccionario?

`frutas = {'Manzanas': 5, 'Naranjas': 3, 'Plátanos': 4}`

- [ ] `nombres_de_frutas = [x en fruit.keys() for x]`
- [ ] `nombres_de_frutas = para x en fruit.keys() *`
- [x] `nombres_de_frutas = [x por x en fruit.keys()]`
- [ ] `nombres_de_frutas = x para x en fruit.keys()`

#### P46. ¿Cuál es el propósito de la palabra clave `self` al definir o llamar a métodos en una instancia de un objeto?

- [ ] `self` se refiere a la clase de la que se heredó para crear el objeto usando `self`.
- [ ] No hay un propósito real para el método `self`. Es solo una jerga informática heredada que Python mantiene para mantenerse consistente con otros lenguajes de programación.
- [ ] `self` significa que no es necesario pasar ningún otro argumento al método.
- [x] `self` se refiere a la instancia cuyo método fue llamado.

**Explicación:** - Intente ejecutar el ejemplo de Q42 sin pasar el argumento `self` dentro de `__init__`, comprenderá el motivo. Obtendrá un error como este `__init__() toma 0 argumentos posicionales pero se le dio 1`, esto significa que algo va adentro incluso si no se ha especificado, que es la instancia misma.

#### P47. ¿Qué afirmación sobre los métodos de clase es verdadera?

- [ ] Un método de clase es una función regular que pertenece a una clase, pero debe devolver Ninguno.
- [x] Un método de clase puede modificar el estado de la clase, pero no puede modificar directamente el estado de una instancia que hereda de esa clase.
- [ ] Un método de clase es similar a una función regular, pero un método de clase no toma ningún argumento.
- [ ] Un método de clase contiene todos los datos de una clase en particular.

#### P48. ¿Qué significa que una función tenga un tiempo de ejecución lineal?

- [ ] No usaste muchos conceptos avanzados de programación de computadoras en tu código.
- [ ] El nivel de dificultad en el que está escrito su código no es tan alto.
- [ ] Tu programa tardará menos de medio segundo en ejecutarse.
- [x] La cantidad de tiempo que tarda la función en completarse crece linealmente a medida que aumenta el tamaño de entrada.

#### P49. ¿Cuál es la forma correcta de definir una función?

- [ ] `def getMaxNum(list_of_nums): # el cuerpo de la función va aquí`
- [ ] `func get_max_num(list_of_nums): # el cuerpo de la función va aquí`
- [ ] `func getMaxNum(list_of_nums): # el cuerpo de la función va aquí`
- [x] `def get_max_num(list_of_nums): # el cuerpo de la función va aquí`

[explicación para 52 y 53](https://www.python.org/dev/peps/pep-0008/)

#### P50. De acuerdo con las pautas de estilo de codificación de PEP 8, ¿cómo se deben nombrar los valores constantes en Python?

- [ ] en mayúsculas y minúsculas sin usar guiones bajos para separar palabras -- p. `valor máximo = 255`
- [ ] en minúsculas con guiones bajos para separar palabras -- p. `valor_máximo = 255`
- [x] en mayúsculas con guiones bajos que separan las palabras, p. `VALOR_MAXIMO = 255`
- [ ] en mayúsculas y minúsculas sin utilizar guiones bajos para separar palabras -- p. `Valor máximo = 255`

#### P51. Describe la funcionalidad de un deque.

- [ ] Un deque agrega elementos a un lado y elimina elementos del otro lado.
- [ ] Un deque agrega elementos a uno o ambos lados, pero solo elimina elementos de la parte superior.
- [x] Un deque agrega elementos en uno o ambos extremos y elimina elementos en uno o ambos extremos.
- [ ] Un deque agrega elementos solo en la parte superior, pero los elimina de uno o ambos lados.

**Explicación** - `deque` se usa para crear un canal de bloque y en eso hay un enfoque de _primero en entrar, primero en salir_, lo que significa que el último elemento en entrar será el primero en salir.

#### P52. ¿Cuál es la sintaxis correcta para crear una variable vinculada a un conjunto?

- [x] `mi_conjunto = {0, 'manzana', 3.5}`
- [ ] `mi_conjunto = to_set(0, 'manzana', 3.5)`
- [ ] `mi_conjunto = (0, 'manzana', 3.5).to_set()`
- [ ] `mi_conjunto = (0, 'manzana', 3.5).conjunto()`

#### P53. ¿Cuál es la sintaxis correcta para definir un método `__init__()` que no toma parámetros?

- [ ] :

```python
class __init__(self):
    pass
```

- [ ] :

```python
def __init__():
    pass
```

- [ ] :

```python
class __init__():
    pass
```

- [x] :

```python
def __init__(self):
    pass
```

#### P54. ¿Cuál de las siguientes es VERDADERA acerca de cómo se organizarían los datos numéricos en un árbol de búsqueda binaria?

- [x] Para cualquier nodo dado en un árbol de búsqueda binaria, el valor del nodo es mayor que todos los valores en el subárbol izquierdo del nodo y menor que los de su subárbol derecho.
- [ ] Árbol de búsqueda binaria no se puede utilizar para organizar y buscar a través de datos numéricos, dada la complicación que se presenta con árboles muy profundos.
- [ ] El nodo superior del árbol de búsqueda binaria sería un número arbitrario. Todos los nodos a la izquierda del nodo superior deben ser menores que el número del nodo superior, pero no es necesario que estén ordenados de ninguna manera en particular.
- [ ] El valor numérico más pequeño iría en el nodo superior. El siguiente número más alto iría en su nodo secundario izquierdo, el siguiente número más alto iría en su nodo secundario derecho. Este patrón continuaría hasta que todos los valores numéricos estuvieran en su propio nodo.

#### P55. ¿Por qué usarías un decorador?

- [ ] Un decorador es similar a una clase y debe usarse si está haciendo programación funcional en lugar de programación orientada a objetos.
- [ ] Un decorador es un indicador visual para alguien que lee su código de que una parte de su código es crítica y no debe cambiarse.
- [x] Usas el decorador para alterar la funcionalidad de una función sin tener que modificar el código de funciones.
- [ ] Una declaración de importación está precedida por un decorador, python sabe importar la versión más reciente de cualquier paquete o biblioteca que se esté importando.

#### P56. ¿Cuándo usarías un bucle for?

- [ ] Solo en algunas situaciones, ya que los bucles se usan solo para cierto tipo de programación.
- [x] Cuando necesita verificar cada elemento en un iterable de longitud conocida.
- [ ] Cuando desee minimizar el uso de cadenas en su código.
- [ ] Cuando desee ejecutar código en un archivo para una función en otro archivo.

#### P57. ¿Cuál es la forma más autodescriptiva de definir una función que calcula el impuesto sobre las ventas en una compra?

- [ ] :

```python
def tax(my_float):
    '''Calculates the sales tax of a purchase. Takes in a float representing the subtotal as an argument and returns a float representing the sales tax.'''
    pass
```

- [ ] :

```python
def tx(amt):
    '''Gets the tax on an amount.'''
```

- [ ] :

```python
def sales_tax(amount):
    '''Calculates the sales tax of a purchase. Takes in a float representing the subtotal as an argument and returns a float representing the sales tax.'''
```

- [x] :

```python
def calculate_sales_tax(subtotal):
    pass
```

#### P58. ¿Qué pasaría si no alterara el estado del elemento en el que está operando un algoritmo recursivamente?

- [ ] No tiene que alterar el estado del elemento en el que recurre el algoritmo.
- [ ] Eventualmente obtendría un KeyError cuando la parte recursiva del código se quedara sin elementos para recurrir.
- [x] Obtendría un RuntimeError: se excedió la profundidad máxima de recursión.
- [ ] La función que utiliza la recursividad devolvería Ninguno.

[explicación](https://www.python-course.eu/python3_recursive_functions.php#Definition-of-Recursion)

#### P59. ¿Cuál es la complejidad del tiempo de ejecución de buscar un elemento en un árbol de búsqueda binaria?

- [ ] El tiempo de ejecución para buscar en un árbol de búsqueda binario es O(1) porque cada nodo actúa como una clave, similar a un diccionario.
- [ ] El tiempo de ejecución para buscar en un árbol de búsqueda binario es O(n!) porque cada nodo debe compararse con todos los demás nodos.
- [x] El tiempo de ejecución para buscar en un árbol de búsqueda binaria es generalmente O(h), donde h es la altura del árbol.
- [ ] El tiempo de ejecución para buscar en un árbol de búsqueda binaria es O(n) porque se deben visitar todos los nodos del árbol.

[explicación](https://www.geeksforgeeks.org/binary-search-tree-data-structure/)

#### P60. ¿Por qué usarías `mixin`?

- [ ] Usas un `mixin` para obligar a una función a aceptar un argumento en tiempo de ejecución incluso si el argumento no estaba incluido en la definición de la función.
- [ ] Usas un `mixin` para permitir que un decorador acepte argumentos de palabras clave.
- [ ] Usas un `mixin` para asegurarte de que los atributos y métodos de una clase no interfieran con variables y funciones globales.
- [x] Si tiene muchas clases que necesitan tener la misma funcionalidad, usaría un `mixin` para definir esa funcionalidad.

[explicación](https://www.youtube.com/watch?v=zVFLBfqV-q0)
