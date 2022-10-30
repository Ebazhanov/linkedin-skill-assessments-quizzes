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

#### P61. ¿Cuál es la complejidad del tiempo de ejecución de agregar un elemento a una pila y eliminar un elemento de una pila?

- [ ] Agregue elementos a una pila en tiempo O (1) y elimine elementos de una pila en tiempo O (n).
- [x] Agregue elementos a una pila en tiempo O (1) y elimine elementos de una pila en tiempo O (1).
- [ ] Agregue elementos a una pila en tiempo O (n) y elimine elementos de una pila en tiempo O (1).
- [ ] Agregue elementos a una pila en tiempo O (n) y elimine elementos de una pila en tiempo O (n).

#### P62. ¿Qué afirmación describe con precisión cómo se agregan y eliminan elementos de una pila?

- [ ] una pila agrega elementos a un lado y elimina elementos del otro lado.
- [x] una pila agrega elementos a la parte superior y elimina elementos de la parte superior.
- [ ] una pila agrega elementos a la parte superior y elimina elementos de cualquier parte de la pila.
- [ ] una pila agrega elementos a cualquier extremo y elimina elementos de cualquier extremo.

**Explicación** La pila usa el enfoque _último en entrar, primero en salir_

#### P63. ¿Qué es un caso base en una función recursiva?

- [x] Un caso base es la condición que permite que el algoritmo deje de repetirse. Por lo general, es un problema que es lo suficientemente pequeño como para resolverlo directamente.
- [ ] El caso base es un resumen del problema general que debe resolverse.
- [ ] El caso base se pasa como argumento a una función cuyo cuerpo hace uso de la recursividad.
- [ ] El caso base es similar a una clase base, ya que puede ser heredado por otro objeto.

#### P64. ¿Por qué se considera una buena práctica abrir un archivo desde un script de Python utilizando la palabra clave `with`?

- [ ] La palabra clave `with` le permite elegir en qué aplicación abrir el archivo.
- [ ] La palabra clave `with` actúa como un bucle `for` y te permite acceder a cada línea del archivo una por una.
- [ ] No hay ningún beneficio en usar la palabra clave `with` para abrir un archivo en Python.
- [x] Cuando abre un archivo usando la palabra clave `with` en Python, Python se asegurará de que el archivo se cierre, incluso si se produce una excepción o un error.

[explicación](https://docs.python.org/3/tutorial/inputoutput.html#lectura-y-escritura-de-archivos)

#### P65. ¿Por qué usarías un entorno virtual?

- [x] Los entornos virtuales crean una "burbuja" alrededor de su proyecto para que las bibliotecas o paquetes que instale dentro de él no afecten a toda su máquina.
- [ ] Los equipos con empleados remotos usan entornos virtuales para poder compartir código, hacer revisiones de código y colaborar de forma remota.
- [ ] Los entornos virtuales eran comunes en Python 2 porque aumentaban las funciones que faltaban en el lenguaje. Los entornos virtuales no son necesarios en Python 3 debido a los avances en el lenguaje.
- [ ] Los entornos virtuales están vinculados a su cuenta de GitHub o Bitbucket, lo que le permite acceder a cualquiera de sus repositorios prácticamente desde cualquier máquina.

#### P66. ¿Cuál es la forma correcta de ejecutar todos los doctests en un archivo dado desde la línea de comando?

- [x] `python3 -m doctest <_nombre_archivo_>`
- [ ] `python3 <_nombre_archivo_>`
- [ ] `python3 <_nombre de archivo_> pruebas de ejecución`
- [ ] `test de documento de python3`

[videotutorial](https://www.youtube.com/watch?v=P8qm0VAbbww&t=180s)

#### P67. ¿Qué es una función lambda?

- [ ] cualquier función que haga uso de constantes científicas o matemáticas, a menudo representadas por letras griegas en la escritura académica
- [ ] una función que se ejecuta cuando se usan decoradores
- [ ] cualquier función cuya definición esté contenida en cinco líneas de código o menos
- [x] una función pequeña y anónima que puede tomar cualquier cantidad de argumentos pero solo tiene una expresión para evaluar

[Referencia](https://www.guru99.com/python-lambda-function.html)

**Explicación:**

> La notación lambda es básicamente una función anónima que puede tomar cualquier cantidad de argumentos con una sola expresión (es decir, no se puede sobrecargar). Se ha introducido en otros lenguajes de programación, como C++ y Java. La notación lambda permite a los programadores "pasar por alto" la declaración de funciones.

#### P68. ¿Cuál es la principal diferencia entre listas y tuplas?

- [ ] Puede acceder a un elemento específico en una lista indexando su posición, pero no puede acceder a un elemento específico en una tupla a menos que itere a través de la tupla
- [x] Las listas son mutables, lo que significa que puede cambiar los datos que están dentro de ellas en cualquier momento. Las tuplas son inmutables, lo que significa que no puede cambiar los datos que están dentro de ellas una vez que haya creado la tupla.
- [ ] Las listas son inmutables, lo que significa que no puede cambiar los datos que contienen una vez que haya creado la lista. Las tuplas son mutables, lo que significa que puede cambiar los datos que contienen en cualquier momento.
- [ ] Las listas pueden contener varios tipos de datos dentro de ellas a la vez, pero las tuplas solo pueden contener el mismo tipo de datos si hay varios elementos presentes.

#### P69. ¿Qué devuelve un generador?

- [ ] Ninguna
- [x] Un objeto iterable
- [ ] Una estructura de datos de lista enlazada de una lista no vacía
- [ ] Todas las claves del diccionario dado

#### P70. ¿Cuál es la diferencia entre atributos de clase y atributos de instancia?

- [ ] Los atributos de instancia se pueden cambiar, pero los atributos de clase no se pueden cambiar
- [x] Los atributos de clase son compartidos por todas las instancias de la clase. Los atributos de instancia pueden serúnico solo para esa instancia
- [ ] No hay diferencia entre atributos de clase y atributos de instancia
- [ ] Los atributos de clase pertenecen solo a la clase, no a la instancia de esa clase. Los atributos de instancia se comparten entre todas las instancias de una clase

#### P71. ¿Cuál es la sintaxis correcta para crear un método de instancia?

- [ ] :

```python
def get_next_card():
  # method body goes here
```

- [x] :

```python
def get_next_card(self):
  # method body goes here
```

- [ ] :

```python
def self.get_next_card():
  # method body goes here
```

- [ ] :

```python
def self.get_next_card(self):
  # method body goes here
```

#### P72. ¿Cuál es la forma correcta de llamar a una función?

- [x] `get_max_num([57, 99, 31, 18])`
- [ ] `call.(get_max_num)`
- [ ] `def get_max_num([57, 99, 31, 18])`
- [ ] `call.get_max_num([57, 99, 31, 18])`

#### P73. ¿Cómo se crea un comentario?

- [ ] `-- Esto es un comentario`
- [x] `# Esto es un comentario`
- [ ] `/_ Esto es un comentario _\`
- [ ] `// Esto es un comentario`

#### P74. ¿Cuál es la sintaxis correcta para reemplazar la cadena manzana en la lista con la cadena naranja?

```python
my_list = ['kiwi', 'apple', 'banana']
```

- [ ] `orange = my_list[1]`
- [x] `my_list[1] = 'orange'`
- [ ] `my_list['orange'] = 1`
- [ ] `my_list[1] == orange`

#### P75. ¿Qué sucederá si usa un ciclo while y olvida incluir la lógica que eventualmente hace que el ciclo while se detenga?

- [ ] Nada pasará; su computadora sabe cuándo dejar de ejecutar el código en el ciclo while.
- [ ] Obtendrá un KeyError.
- [x] Su código se quedará atascado en un bucle infinito.
- [ ] Obtendrá un WhileLoopError.

#### P76. ¿Describa la funcionalidad de una cola?

- [x] Una cola agrega elementos a cualquier extremo y elimina elementos de cualquier extremo.
- [ ] Una cola agrega elementos a la parte superior y elimina elementos de la parte superior.
- [ ] Una cola agrega elementos a la parte superior y elimina elementos de cualquier parte de una lista.
- [ ] Una cola agrega elementos en la parte superior y elimina elementos de cualquier parte de la cola.

#### P77. ¿Qué opción es el ejemplo más sintácticamente correcto de la bifurcación condicional?

- [x] :

```python
num_people = 5

if num_people > 10:
    print("There is a lot of people in the pool.")
elif num_people > 4:
    print("There are some people in the pool.")
else:
    print("There is no one in the pool.")
```

- [ ] :

```python
num_people = 5

if num_people > 10:
    print("There is a lot of people in the pool.")
if num_people > 4:
    print("There are some people in the pool.")
else:
    print("There is no one in the pool.")
```

- [ ] :

```python
num_people = 5

if num_people > 10;
    print("There is a lot of people in the pool.")
elif num_people > 4;
    print("There are some people in the pool.")
else;
    print("There is no one in the pool.")
```

- [ ] :

```python
if num_people > 10;
    print("There is a lot of people in the pool.")
if num_people > 4;
    print("There are some people in the pool.")
else;
    print("There is no one in the pool.")
```

#### P78. ¿Cómo funciona `defaultdict`?

- [ ] `defaultdict` creará automáticamente un diccionario para usted que tiene claves que son los números enteros 0-10.
- [ ] `defaultdict` obliga a un diccionario a aceptar solo claves que sean de los tipos especificados cuando creó el `defaultdict` (como cadenas o números enteros).
- [x] Si intenta leer desde un `defaultdict` con una clave inexistente, se creará un nuevo par clave-valor predeterminado para usted en lugar de generar un `KeyError`.
- [ ] `defaultdict` almacena una copia de un diccionario en la memoria que puede usar de forma predeterminada si el original se modifica involuntariamente.

#### P79. ¿Cuál es la sintaxis correcta para agregar una clave llamada `variedad` al diccionario `fruit_info` que tiene un valor de `Red Delicious`?

- [ ] `info_fruta['variedad'] == 'Red Delicious'`
- [x] `info_fruta['variedad'] = 'Red Delicious'`
- [ ] `rojo_delicioso = fruit_info['variedad']`
- [ ] `rojo_delicioso == fruit_info['variedad']`

#### P80. ¿Cuándo usarías un bucle `while`?

- [ ] cuando desee minimizar el uso de cadenas en su código
- [ ] cuando desea ejecutar código en un archivo mientras también se está ejecutando código en otro archivo
- [x] cuando desea que algún código continúe ejecutándose siempre que alguna condición sea verdadera
- [ ] cuando necesite ejecutar dos o más fragmentos de código a la vez dentro del mismo archivo

**Ejemplo sencillo**

```python
i = 1
while i<6:
    print('Countdown:',i)
    i = i + 1
```

#### P81. ¿Cuál es la sintaxis correcta para definir un método `__init__()` que establece atributos específicos de la instancia al crear una nueva instancia de clase?

- [ ] :

```python
def __init__(self, attr1, attr2):
    attr1 = attr1
    attr2 = attr2
```

- [ ] :

```python
def __init__(attr1, attr2):
    attr1 = attr1
    attr2 = attr2
```

- [x] :

```python
def __init__(self, attr1, attr2):
    self.attr1 = attr1
    self.attr2 = attr2
```

- [ ] :

```python
def __init__(attr1, attr2):
    self.attr1 = attr1
    self.attr2 = attr2
```

**Explicación**: Al instanciar un nuevo objeto de una clase dada, el método `__init__()` tomará `attr1` y `attr2`, y establezca sus valores en su atributo de objeto correspondiente, por eso es necesario usar `self.attr1 = attr1` en lugar de `attr1 = attr1`.

#### P82. ¿Qué imprimiría esta función recursiva si se llama sin parámetros?

```python
def count_recursive(n=1):
    if n > 3:
        return
    print(n)

    count_recursive(n + 1)
```

- [ ] :

```python
1
1
2
2
3
3
```

- [ ] :

```python
3
2
1
```

- [ ] :

```python
3
3
2
2
1
1
```

- [x] :

```python
1
2
3
```

#### P83. En Python, cuando usa conjuntos, usa **\_** para calcular la intersección entre dos conjuntos y **\_** para calcular la unión.

- [ ] `Intersect`; `union`
- [ ] `|`; `&`
- [x] `&`; `|`
- [ ] `&&`; `||`

#### P84. ¿Qué devolverá este fragmento de código?

```python
import numpy as np
np.ones([1,2,3,4,5])
```

- [ ] Devuelve una matriz de 5x5; cada fila tendrá los valores 1,2,3,4,5.
- [ ] Devuelve un array con los valores 1,2,3,4,5
- [ ] Devuelve cinco matrices cuadradas diferentes llenas de unos. El primero es 1x1, el segundo 2x2, y así sucesivamente hasta 5x5
- [x] Devuelve una matriz de 5 dimensiones de tamaño 1x2x3x4x5 llena de 1s.

[Referencia](https://www.geeksforgeeks.org/numpy-ones-python/)

#### P85. Encuentra una excepción FileNotFoundException mientras usa solo el nombre de archivo en la función `open`. ¿Cuál podría ser la solución más fácil?

- [ ] Asegúrese de que el archivo esté en la RUTA del sistema
- [ ] Crear un enlace simbólico para permitir un mejor acceso al archivo
- [x] Copie el archivo en el mismo directorio desde donde se ejecuta el script
- [ ] Agregue la ruta al archivo a la variable de entorno PYTHONPATH

#### P86. ¿Qué devolverá este comando?

```python
{x for x in range(100) if x%3 == 0}
```

- [x] un conjunto de todos los múltiplos de 3 menos de 100
- [ ] un conjunto de todos los números del 0 al 100 multiplicados por 3
- [ ] una lista de todos los múltiplos de 3 menos de 100
- [ ] un conjunto de todos los múltiplos de 3 menos de 100 excluyendo 0

#### P87. ¿Qué te permite hacer el operador // en Python 3?

- [x] Realizar división de enteros
- [ ] Realizar operaciones sobre exponentes
- [ ] Encontrar el resto de una operación de división
- [ ] Realizar división de punto flotante

#### P88. ¿Qué archivo se importa para usar fechas en python?

- [x] fecha y hora
- [ ] dia de cita
- [ ] durante el día
- [ ] hora Fecha

#### P89. ¿Cuál es la sintaxis correcta para definir una clase llamada Juego?

- [ ] `def Juego(): pass`
- [ ] `def Juego: pass`
- [x] `class Juego: pass`
- [ ] `class Juego(): pass`

[referencia aquí](https://docs.python.org/3/tutorial/classes.html)

#### P90. ¿Cuál es la sintaxis correcta para llamar a un método de instancia en una clase llamada Juego?

- [ ] `my_game = Game(self) self.my_game.roll_dice()`
- [ ] `my_game = Game() self.my_game.roll_dice()`
- [x] `my_game = Game() my_game.roll_dice()`
- [ ] `my_game = Game(self) my_game.roll_dice(self)`

#### P91. ¿Cuál es la salida de este código? (NumPy se ha importado como np.)?

```python
a = np.array([1,2,3,4])
print(a[[False, True, False, False]])
```

- [ ] `{0,2}`
- [x] `[2]`
- [ ] `{2}`
- [ ] `[0,2,0,0]`

#### P92. Suponga que tiene una variable de cadena definida como y="cosas;cosa;basura;". ¿Cuál sería la salida de este código?

```python
z = y.split(';')
len(z)
```

- [ ] 17
- [x] 4
- [ ] 0
- [ ] 3

**Explicación**:

```python
y="stuff;thing;junk"
	len(z) ==> 3

y="stuff;thing;junk;"
	len(z) ==> 4
```

#### P93. ¿Cuál es la salida de este código?

```python
num_list = [1,2,3,4,5]
num_list.remove(2)
print(num_list)
```

- [ ] `[1,2,4,5]`
- [x] `[1,3,4,5]`
- [ ] `[3,4,5]`
- [ ] `[1,2,3]`

**Explicación**:

```python
num_list = [1,2,3,4,5]

num_list.pop(3)
>>> [1,2,4,5]

num_list.remove(2)
>>> [1,3,4,5]
```

#### P94. ¿Qué comando creará una lista del 10 al 1? Ejemplo:

`[10,9,8,7,6,5,4,3,2,1]`

- [ ] `reversed(list(range(1,11)))`
- [ ] `list(reversed(range(1,10)))`
- [ ] `list(range(10,1,-1))`
- [x] `list(reversed(range(1,11)))`

[Referencia](https://www.w3schools.com/python/python_tuples.asp)

#### P95. ¿Qué fragmento de código imprimirá exactamente el mismo resultado que este fragmento?

```python
import math
print(math.pow(2,10)) # prints 2 elevated to the 10th power
```

- [ ] :

```python
print(2^10)
```

- [x] :

```python
print(2**10)
```

- [ ] :

```python
y = [x*2 for x in range(1,10)]
print(y)
```

- [ ] :

```python
y = 1
for i in range(1,10):
    y = y * 2
print(y)
```

[Referencia](https://www.digitalocean.com/community/tutorials/how-to-do-math-in-python-3-with-operators#:~:text=The%20**%20operator%20in %20Python,multiplicado%20por%20sí mismo%203%20 veces.)

#### P96. Los elementos rodeados por `[]` son **\_**, `{}` son **\_** y `()` son **\_**.

- [ ] conjuntos solamente; listas o diccionarios; tuplas
- [ ] listas; conjuntos solamente; tuplas
- [ ] tuplas; conjuntos o listas; diccionarios
- [x] listas; diccionarios o juegos; tuplas

[Referencia](https://www.geeksforgeeks.org/differences-and-applications-of-list-tuple-set-and-dictionary-in-python/)

#### P97. ¿Cuál es la salida de este código? (NumPy se ha importado como np.)

```python
table = np.array([
    [1,3],
    [2,4]])
print(table.max(axis=1))
```

- [ ] `[2, 4]`
- [x] `[3, 4]`
- [ ] `[4]`
- [ ] `[1,2]`

[Referencia](https://colab.research.google.com/drive/1PRGf7Wgcr_gQk7snnxxuc5rL9O1ky9Xg?usp=sharing)

#### P98. ¿Qué imprimirá este código?

```python
number = 3
print (f"The number is {number}")
```

- [x] `El número es 3`
- [ ] `el número es 3`
- [ ] `EL NÚMERO ES 3`
- [ ] Lanza un TypeError porque el entero debe convertirse en una cadena.

[Referencia](https://colab.research.google.com/drive/1PRGf7Wgcr_gQk7snnxxuc5rL9O1ky9Xg?usp=sharing)

#### P99. ¿Qué sintaxis crea correctamente una variable que está vinculada a una tupla?

- [ ] `mi_tuple tup(2, 'manzana', 3.5) %D`
- [ ] `mi_tupla [2, 'manzana', 3.5].tuple() %D`
- [x] `mi_tupla = (2, 'manzana', 3.5)`
- [ ] `mi_tupla = [2, 'manzana', 3.5]`

[Referencia](https://beginnersbook.com/2018/02/python-tuple/)

#### Q100. ¿Qué modo no es una forma válida de acceder a un archivo desde un script de Python?

- [ ] `write('w')`
- [x] `scan('s')`
- [ ] `append('a')`
- [ ] `read('r')`

1. [Referencia](https://docs.python.org/3/library/functions.html#open)
2. [Referencia](https://www.w3schools.com/python/ref_list_append.asp)

#### P101. NumPy le permite multiplicar dos matrices sin un bucle for. Esto es un ejemplo de \_.

- [x] vectorización
- [ ] atribuciones
- [ ] aceleración
- [ ] programación funcional

#### P102. ¿Qué tipo de datos integrado de Python se puede usar como una tabla hash?

- [ ] `conjunto`
- [ ] `lista`
- [ ] `tupla`
- [x] `diccionario`

#### P103. ¿Qué función de Python le permite ejecutar comandos de shell de Linux en Python?

- [ ] `sys.exc_info()`
- [x] `os.system()`
- [ ] `os.getcwd()`
- [ ] `sys.executable`

#### P104. Suponga que tiene el siguiente fragmento de código y desea extraer una lista con solo las letras. ¿Qué fragmento de código \_no\_ logrará ese objetivo?

```python
my_dictionary = {
    'A': 1,
    'B': 2,
    'C': 3,
    'D': 4,
    'E': 5
}
```

- [x] <br>

```python
letters = []

for letter in my_dictionary.values():
    letters.append(letter)
```

- [ ] `letters = my_dictionary.keys()`
- [ ] `letters = [letter for (letter, number) in my_dictionary.items()]`
- [ ] `letters4 = list(my_dictionary)`

**Explicación:** La primera (la opción correcta) devuelve la lista de los valores (los números). El resto de las opciones devuelven una lista de las claves.

#### P105. Cuando una matriz es grande, NumPy no imprimirá la matriz completa cuando se le proporcione la función "imprimir" incorporada. ¿Qué función puede usar dentro de NumPy para forzarlo a imprimir toda la matriz?

- [ ] `set_printparams`
- [x] `set_printoptions`
- [ ] `set_fullprint`
- [ ] `setp_printwhole`

#### P106. ¿Cuándo usarías un bloque try/except en el código?

- [x] Utiliza bloques `try/except` cuando desea ejecutar algún código, pero necesita una forma de ejecutar código diferente si se genera una excepción.
- [ ] Usas bloques `try/except` dentro de las pruebas unitarias para que los testículos unitarios siempre pasen.
- [ ] Usa bloques `try/except` para que pueda demostrar a sus revisores de código que probó un nuevo enfoque, pero si el nuevo enfoque no es lo que estaban buscando, pueden dejar comentarios bajo la palabra clave `except` .
- [ ] Utiliza bloques `try/except` para que ninguna de sus funciones o métodos devuelva `Ninguno`.

[Referencia](https://runestone.academy/ns/books/published/fopp/Exceptions/using-exceptions.html#:~:text=The%20reason%20to%20use%20try, you're%20write%20the %20código)

#### P107. En Python, ¿cómo puede el compilador identificar el bloque interno de un bucle for?

- [x] `debido al nivel de sangría después del ciclo for`
- [ ] `debido a la palabra clave end al final del bucle for`
- [ ] `porque el bloque está entre corchetes ({})`
- [ ] `debido al espacio en blanco al final del cuerpo del bucle for`

#### P108. Qué mecanismo de Python es el más adecuado para decirle a un usuario que está usando una función obsoleta

- [ ] salida estándar del sistema
- [ ] rastrear
- [x] advertencias
- [ ] excepciones

#### P109. ¿Cuál será el valor de x después de ejecutar este código?

```python
x = {1,2,3,4,5}
x.add(5)
x.add(6)
```

- [ ] `{1, 2, 3, 4, 5, 5, 6}`
- [ ] `{5, 6, 1, 2, 3, 4, 5, 6}`
- [ ] `{6, 1, 2, 3, 4, 5}`
- [x] `{1, 2, 3, 4, 5, 6}`

**Explicación:** El método `.add()` agrega el elemento al conjunto solo si no existe.

#### P110. ¿Cómo accedería y almacenaría todas las claves en este diccionario a la vez?

```python
fruit_info = {
    'fruit': 'apple',
    'count': 2,
    'price': 3.5
}
```

- [ ] `my_keys = fruit_info.to_keys()`
- [ ] `my_keys = fruit_info.all_keys()`
- [ ] `my_keys = fruit_info.keys`
- [x] `my_keys = fruit_info.keys()`

#### P111. ¿Qué tiene de malo esta definición de función?

```python
def be_friendly(greet = "How are you!", name):
    pass
```

- [ ] `name` es una palabra reservada.
- [ ] No se permiten guiones bajos en los nombres de las funciones.
- [x] Un argumento no predeterminado sigue a un argumento predeterminado.
- [ ] No hay nada malo con esta definición de función.

#### P112. Dado que NumPy se importa como `np`, ¿qué opción devolverá `True`?

- [x] :

```python
a = np.zeros([3,4])
b = a.copy()
np.array_equal(a,b)
```

- [ ] :

```python
a = np.empty([3,4])
b = np.empty([3,4])
np.array_equal(a,b)
```

- [ ] :

```python
a = np.zeros([3,4])
b = np.zeros([4,3])
np.array_equal(a,b)
```

- [ ] :

```python
a = np.array([1, np.nan])
np.array_equal(a,a)
```

#### P113. ¿Cómo se agrega un comentario a un script de Python existente?

- [ ] `// Esto es un comentario`
- [x] `# Esto es un comentario`
- [ ] `-- Esto es un comentario`
- [ ] `/* Esto es un comentario *\`

#### P114. En este fragmento de código, ¿a qué serán equivalentes los valores de c y d?

```python
import numpy as np
a = np.array([1,2,3])
b = np.array([4,5,6])
c = a*b
d = np.dot(a,b)
```

- [ ] A

```python
c = [ a[1] * b[1], a[2] * b[2], a[3] * b[3] ]
d = sum(c)
```

- [ ] B

```python
c = a[0] * b[0], a[1] * b[1], a[2] * b[2]

d = [ a[0] * b[0], a[1] * b[1], a[2] * b[2] ]
```

- [ ] C

```python
c = [ a[0] * b[0], a[1] * b[1], a[2] * b[2] ]

d = sum(a) + sum(b)
```

- [x] D

```python
c = [ a[0] * b[0], a[1] * b[1], a[2] * b[2] ]

d = sum(c)
```

#### P115. ¿Qué dos funciones dentro de la biblioteca NumPy podrías usar para resolver un sistema de ecuaciones lineales?

- [x] `linalg.eig() y .matmul()`
- [ ] `linalg.inv() y .dot()`
- [ ] `linalg.det() y .dot()`
- [ ] `linalg.inv() y .eye()`

#### P116. ¿Cuál es la sintaxis correcta para crear una variable vinculada a una lista?

- [ ] `mi_lista = (2, 'manzana', 3.5)`
- [x] `mi_lista = [2, 'manzana', 3.5]`
- [ ] `mi_lista = [2, 'manzana', 3.5].to_list()`
- [ ] `mi_lista = to_list(2, 'manzana', 3.5)`

[Referencia](https://www.tutorialspoint.com/python/python_lists.htm)

#### P117. Este código proporciona el **\_** de la lista de números.

```python
num_list = [21, 13, 19, 3, 11, 5, 18]
num_list.sort()
num_list[len(num_list) // 2]
```

- [ ] modo
- [ ] promedio
- [ ] media
- [x] mediana

**Explicación:** La mediana es el valor que separa la mitad superior de la mitad inferior de una muestra de datos. Aquí son las 13.

#### P118. ¿Cuáles son las dos estructuras de datos principales en la biblioteca Pandas?

- [ ] Matrices y tramas de datos
- [ ] Series y Matrices
- [ ] Matrices y DataFrames
- [x] Series y DataFrames

[Referencia](https://pandas.pydata.org/docs/user_guide/dsintro.html)

#### P119. Suponga que tiene una variable llamada `vector` de tipo np.array con 10.000 elementos. ¿Cómo puedes convertir `vector` en una variable llamada `matriz` con dimensiones 100x100?

- [ ] `matrix = (vector.shape = (100,100))`
- [ ] `matrix = vector.to_matrix(100,100)`
- [ ] `matrix = matrix(vector,100,100)`
- [x] `matrix = vector.reshape(100, 100)`

[Referencia](https://www.w3schools.com/python/numpy/numpy_array_reshape.asp)

#### P120. ¿Qué opción es un tipo de datos inmutable?

- [ ] diccionario
- [ ] lista
- [ ] conjunto (`set`en Inglés)
- [x] cadena de caracteres (`string` en Inglés)

[Referencia](https://www.tutorialspoint.com/python_text_processing/python_string_immutability.htm)

#### P121. ¿Cuál es la salida de este código?

```python
def myFunction(country = "France"):
    print("Hello, I am from", country)

myFunction("Spain")
myFunction("")
myFunction()
```

- [ ] :

```python
Hello, I am from Spain
Hello, I am from
Hello, I am from
```

- [ ] :

```python
Hello, I am from France
Hello, I am from France
Hello, I am from France
```

- [x] :

```python
Hello, I am from Spain
Hello, I am from
Hello, I am from France
```

- [ ] :

```python
Hello, I am from Spain
Hello, I am from France
Hello, I am from France
```

#### P122. Elija la opción a continuación para la cual no se puede crear una instancia de la clase

- [ ] Clase anónima
- [ ] Clase principal
- [ ] Clase anidada
- [x] Clase abstracta

[Referencia](https://www.scaler.com/topics/python/data-abstraction-in-python/)

#### P123. Usando Pandas, cargamos un conjunto de datos de Kaggle, como se estructura en la imagen a continuación. ¿Qué comando devolverá el número total de supervivientes?

![Q129](images/Q129.png?raw=png)

- [x] `sum(titanic['Survived'])`
- [ ] `[x for x in titanic['Survived'] if x == 1]`
- [ ] `len(titanic["Survived"])`
- [ ] `sum(titanic['Survived']==0)`

**Explicación:** `titanic['Survived']` devuelve un objeto `pandas.Series`, que contiene la columna `Survived` del `DataFrame`.
Sumar los valores de esta columna (es decir, `sum(titanic['Survived'])`) devuelve el número total de supervivientes, ya que un superviviente se representa con un 1 y una pérdida con un 0.

#### P124. ¿Cómo crearía una lista de tuplas que coincidan con estas listas de personajes y actores?

```python
characters = ["Iron Man", "Spider Man", "Captain America"]
actors = ["Downey", "Holland", "Evans"]

# example output : [("IronMan", "Downey"), ("Spider Man", "Holland"), ("Captain America", "Evans")]
```

- [ ] `[(x,y)] for x in characters for y in actors]`
- [x] `zip(characters, actors)`
- [ ]

```python
d = {}

for x in range(1, len(characters)):
    d[x] = actors[x]
```

- [ ] `{x:y for x in characters for y in actors}`

#### P125. ¿Qué devolverá esta declaración?

```python
{x : x*x for x in range(1,100)}
```

- [ ] un diccionario con x como clave y x al cuadrado como su valor; del 1 al 100
- [x] un diccionario con x como clave y x al cuadrado como su valor; del 1 al 99
- [ ] un conjunto de tuplas, compuesto por (x, x al cuadrado); del 1 al 99
- [ ] una lista con todos los números al cuadrado del 1 al 99

#### P126. La similitud de Jaccard es una fórmula que te dice qué tan similares son dos conjuntos. Se define como la cardinalidad de la intersección dividida por la cardinalidad de la unión. ¿Qué opción es una implementación precisa en Python?

![Q132](images/Q132.png?raw=png)

- [ ] `def jaccard(a, b): return len (a | b) / len (a & b)`
- [x] `def jaccard(a, b): return len (a & b) / len (a | b)`
- [ ] `def jaccard(a, b): return len (a && b) / len (a || b)`
- [ ] `def jaccard(a, b): return a.intersection(b) / a.union(b)`

[Referencia](https://docs.python.org/3/tutorial/datastructures.html?highlight=set#sets.)

#### P127. ¿Qué opción no es un tipo numérico nativo en Python?

- [ ] Long
- [ ] Int
- [ ] Float
- [x] Double

#### P128. ¿Cuál será la salida de este código?

```python
[1,2,3] * 3
```

- [ ] `[3,2,3]`
- [x] `[1, 2, 3, 1, 2, 3, 1, 2, 3]`
- [ ] Obtendrá un error de tipo.
- [ ] `[3,6,9]`

#### P129. Dada una lista definida como números = `[1,2,3,4]`, ¿cuál es el valor de `numbers[-2]`?

- [ ] 1
- [x] 3
- [ ] 2
- [ ] Se lanza una excepción IndexError.

#### P130. ¿Qué afirmación sobre las cadenas en Python es verdadera?

- [x] Las cadenas se pueden encerrar entre comillas dobles (") o comillas simples (').
- [ ] Las cadenas solo se pueden escribir entre comillas simples (').
- [ ] Las cadenas de un solo carácter deben estar entre comillas simples ('), y el resto debe estar entre comillas dobles (").
- [ ] Las cadenas solo se pueden escribir entre comillas dobles (").

#### P131. ¿Cuál es la sintaxis correcta para definir un método _init_() que no toma parámetros?

- [ ] def*init*(self): pass
- [ ] class*init*(self): pass
- [ ] class*init*(): pass
- [x] def*init*(): pass

() -parámetro vacío
self -se refiere a todas las instancias dentro de una clase
_init_ -un método reservado, también conocido como constructor
_init_() -siempre se ejecuta cuando se inicia la clase

#### P132. Suponga que necesita usar la función `sin` de la biblioteca `math`. ¿Cuál es la sintaxis correcta para importar solo esa función?

- [ ] `using math.sin`
- [ ] `import math.sin`
- [x] `from math import sin`
- [ ] `import sin from math`

#### P133. ¿Qué obtienes si aplicas numpy.sum() a una lista que contiene solo valores booleanos?

- [ ] `0`
- [x] `el recuento de todos los valores verdaderos`
- [ ] `un error de tipo`
- [ ] `Ninguno`

#### P134. ¿Qué imprimirá este código?

```python
print ("foo" if (256).bit_length() > 8 else "bar")
```

- [ ] Verdadero
- [x] foo
- [ ] Obtendrá un mensaje de error porque los valores enteros constantes no son clases.
- [ ] bar

#### P135. Si no devuelve explícitamente un valor de una función, ¿qué sucede?

- [ ] Si la palabra clave de retorno está ausente, la función devolverá True.
- [ ] La función entrará en un ciclo infinito porque no saber cuándo dejar de ejecutar su código.
- [ ] La función devolverá un RuntimeError si no devuelve un valor.
- [x] Si la palabra clave de retorno está ausente, la función devolverá Ninguno.

#### P136. a menudo ocurre que la biblioteca pandas se usa para datos **_ data y NumPy for _** data.

- [x] string; numerical
- [ ] unstructured; structured
- [ ] numerical; tabular
- [ ] tabular; numerical

#### P137. ¿Qué necesita hacer para instalar paquetes adicionales en Python?

- [ ] Use un compilador de C como gcc o clang.
- [x] Usa un administrador de paquetes como pip o conda.
- [ ] Usa un IDE como Notepad++ o Idle.
- [ ] Use un administrador de paquetes como NPM o NuGet.

#### P138. La imagen de abajo fue creada usando Matplotlib. Es un diagrama de distribución de una lista de enteros llenos de números usando la función **\_** y trazados con **\_**.

![Q132](images/Q138.png?raw=png)

- [ ] `random.uniform(0,50);plt.hist`
- [x] `random.gauss(50,20);plt.hist`
- [ ] `random();plt.scatter`
- [ ] `random.triangular(0,50);plt.bar`

[Referencia](https://www.geeksforgeeks.org/random-gauss-function-in-python/)

#### P139. En este fragmento de código, ¿cuáles serán los valores de a y b?

```python
import numpy as np

a = np.arange(100)
b = a[50:60:2]
```

- [x] a: todos los números enteros del 0 al 99 (inclusive) b: todos los números pares del 50 al 58 (inclusive)
- [ ] a: todos los números enteros del 0 al 100 (inclusive) b: todos los números pares del 50 al 60 (inclusive)
- [ ] a: todos los números enteros del 0 al 99 (inclusive) b: todos los números pares del 50 al 60 (inclusive)
- [ ] a: todos los números enteros del 0 al 99 (inclusive) b: todos los números impares del 49 al 59 (inclusive)

#### P140. Cuando usa NumPy en Python, ¿cómo verifica la dimensionalidad (número y longitud de las dimensiones) de un objeto llamado my_object?

- [ ] `my_object.get_shape()`
- [x] `my_object.shape`
- [ ] `my_object.dim()`
- [ ] `len(my_object)`

#### P141. Suponga que tiene una lista no vacía llamada _mylist_ y desea buscar un valor específico. ¿El número mínimo de comparación será \_**_ y el número máximo de comparación será _**?

- [ ] `len(milista); len(milista)`
- [x] `1; len(milista)`
- [ ] `2; len(milista)`
- [ ] `0; len(milista)`

**Explicación:** Puede usar una declaración de interrupción y el valor que se busca puede ser el primer elemento de la lista, dado que no está vacío.

#### P142. Si una función no tiene declaración de retorno, ¿qué es lo que realmente devuelve?

- [ ] 0
- [ ] True
- [x] None
- [ ] False

#### P143. ¿Cuál es un uso común de la biblioteca sys de Python?

- [x] para capturar los argumentos de la línea de comandos proporcionados en el tiempo de ejecución de un archivo
- [ ] para tomar una instantánea de todos los paquetes y bibliotecas en su entorno virtual
- [ ] para conectar varios sistemas, como conectar una interfaz web, un servicio API, una base de datos y una aplicación móvil
- [ ] para escanear la salud de su ecosistema de Python mientras está dentro de un entorno virtual

[Referencia](https://docs.python.org/3/library/sys.html)

#### P144. Suponga que desea volver a verificar si dos matrices se pueden multiplicar usando NumPy para fines de depuración. ¿Cómo completarías este fragmento de código llenando los espacios en blanco con las variables apropiadas?

```python
import numpy as np

def can_matrices_be_multiplied (matrix1, matrix2):
    rowsMat1, columnsMat1 = matrix1.shape
    rowsMat2, columnsMat2 = matrix2.shape

    if _____ == ______ :
        print('The matrices can be multipled!')
        return True
    else:
        return False
```

- [ ] columnsMat1; rowsMat1;
- [ ] columnsMat1; rowsMat2;
- [ ] columnsMat1; columnsMat2;
- [x] columnsMat2; rowsMat1;

#### P145. ¿Cuál es el resultado de esta comprensión?

`[(x, x+1) for x in range(1,5)] `

- [ ] [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]
- [ ] [1,2,3,4,5]
- [ ] [(1, 2), (2, 3), (3, 4)]
- [x] [(1, 2), (2, 3), (3, 4), (4, 5)]

#### P146. En Python, un método de clase debe tener \_**\_ como decorador de funciones, y el primer parámetro del método será una referencia a \_\_**.

- [x] @classmethod; the class
- [ ] inline; the class
- [ ] static; self
- [ ] @static; self

[Referencia](https://docs.python.org/3/library/functions.html#classmethod)

#### P147. ¿Qué fragmento de código imprimirá Mi nombre es Joffrey, hijo de Robert?

- [ ] :

```python
class Father():
    name = 'Robert'

class Person(Father):
    def __init__(self, name):
        self.fathername = super.name
        self.name = name

    def introduce(self):
        print("My name is", self.name, "son of", self.fathername)

king = Person("Joffrey")
king.introduce()

```

- [x] :

```python
class Father():
    name = 'Robert'


class Person(Father):
    def __init__(self, name):
        self.fathername = self.name
        self.name = name

    def introduce(self):
        print("My name is", self.name, "son of", self.fathername)


king = Person("Joffrey")
king.introduce()

```

- [ ] :

```python
class Father():
    name = 'Robert'


class Person(Father):
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("My name is", self.name, "son of", super.name)

king = Person("Jofrey")
rey.presentar()
```

- [ ] :

```pitón
clase Padre():
    nombre = 'Roberto'

Persona de clase (Padre):
    def __init__(uno mismo, nombre):
        self.nombre = nombre

    def presentar (auto):
        print("Mi nombre es", self.name, "hijo de", base.name)

rey = Persona("Joffrey")
rey.presentar()

```

**Explicación:** En el primero, super no tiene .name (debe ser self.name), el tercero elimina a Robert y la base no está definida en el 4to.

#### P148.

```python
animals = {
    'a': ['ant', 'antelope', 'armadillo'],
    'b': ['beetle', 'bear', 'bat'],
    'c': ['cat', 'cougar', 'camel']
}

animals = defaultdict(list, animals)

print(animals['b'])
print(animals['d'])
```

- [x] A

```python
      ['beetle', 'bear', 'bat']
      []
```

- [ ] B

```python
      ['beetle', 'bear', 'bat']
      # an exception will be thrown
```

- [ ] C

```python
      ['beetle', 'bear', 'bat']
      None
```

- [ ] D

```python
      ['bat', 'bear', 'beetle']
      []
```

**Explicación:** Los diccionarios generalmente generan una excepción cuando se usa la sintaxis de corchetes. Defaultdict aquí devuelve un valor predeterminado dedicado por el primer parámetro, por lo que en lugar de lanzar una excepción, devuelven el valor predeterminado. Tenga en cuenta que esto debe importarse de la siguiente manera: `from collections import defaultdict`

[Referencia](https://www.geeksforgeeks.org/defaultdict-in-python/)

#### P149. ¿Qué devolverá esta línea de código? (Suponga que n ya está definido como cualquier valor entero positivo).

```python
[x*2 for x in range(1,n)]
```

- [x] una lista con todos los números pares menores que 2\*n
- [ ] un diccionario con todos los números pares menores que 2\*n
- [ ] una lista con todos los números impares menores que 2\*n
- [ ] una lista con todos los números pares menores o iguales a 2\*n

[Referencia](https://www.w3schools.com/python/ref_func_range.asp)

#### Q150. ¿Qué imprime este código en la consola?

```python
x = 18

if x > 10:
	if x > 15:
		print('A')
	else:
		print('B')
else:
	print('C')

```

- [ ] C
- [ ] AB
- [ ] B
- [x] A

#### P151. Suponga que tiene una variable llamada vector de tipo np.array con 10.000 elementos. ¿Cómo puede convertir un vector en una matriz variable con dimensiones de 100x100?

- [ ] matrix = matrix(vector,100,100)
- [ ] matrix = vector.to_matrix(100,100)
- [ ] matrix = (vector.shape = (100,100))
- [x] matrix = vector.reshape(100,100) Exa

#### P152. ¿Cuál es la longitud máxima de un identificador de Python?

- [ ] 32
- [ ] dieciséis
- [ ] 128
- [x] No se especifica longitud fija

#### P153. ¿Cuál será el valor de la variable i cuando el siguiente ciclo termine su ejecución?

para i en el rango (5): pasar

- [ ] 5
- [ ] la variable deja de estar disponible
- [ ] 6
- [x] 4

#### P154. Las cuerdas f también se llaman:

- [ ] Expresiones de cadena formateadas
- [ ] Cadenas funcionales
- [ ] Cadenas con formato Modulo
- [x] Literales de cadena con formato

#### P155. ¿Cuántas CPU (o núcleos) aprovechará la biblioteca de subprocesamiento de Python simultáneamente?

- [x] Uno
- [ ] Todas las CPU disponibles
- [ ] Dos
- [ ] Tres

**Explicación**: los subprocesos de Python están restringidos a una sola CPU a la vez. La biblioteca de multiprocesamiento le permitirá ejecutar código en diferentes procesadores.

#### P156 ¿Cuál será el valor de y en este código?

```python
x = 5
y = 1 + (20 if x < 5 else 30)
```

- [ ] Falso
- [ ] 21
- [ ] 2
- [x] 31

**Explicación:**
Si x < 5 ==> y = 1 + 20
De lo contrario y = 1 + 30

#### Q157.¿El proceso de decapado en Python incluye?

- [x] conversión de una jerarquía de objetos de Python en un flujo de bytes
- [ ] conversión de una tabla de datos en una lista
- [ ] conversión de un flujo de bytes en la jerarquía de objetos de Python
- [ ] conversión de una lista en una tabla de datos

Explicación: el decapado es el proceso de esterilización de un objeto de Python, es decir, la conversión de un flujo de bytes en una jerarquía de objetos de Python. El reverso de este proceso se conoce como decapado.

#### P158. ¿Cuál es la salida del siguiente programa?

```
print("codescracker".endswith("er"))
```

- [x] Verdadero
- [ ] 1
- [ ] 2
- [ ] Falso

#### P159. ¿La lista es mutable en Python?

- [x] Verdadero
- [ ] Falso

#### Q160. ¿Cuál es la salida del siguiente programa?

print("programming".center())

- [ ] cr
- [ ] programación
- [x] El error dice TypeError: el centro esperaba al menos 1 argumento, obtuvo 0
- [ ] Ninguna de las anteriores

#### P161. ¿Quién creó el lenguaje de programación Python?

- [ ] Tim Berners-Lee
- [ ] Ada Lovelace
- [x] Guido van Rossum
- [ ] Alan Turing

#### P162. ¿Qué colección es ordenada, cambiable y permite miembros duplicados?

- [ ] ESTABLECER
- [ ] TUPLE
- [ ] DICCIONARIO
- [x] LISTA

#### P163. ¿Qué se imprimirá en la consola si ejecuta este código?

```python
x = 1j
print(x**2 == -1)
```

- [ ] un error en tiempo de ejecución que le indica que la variable `j` no se ha inicializado
- [x] Verdadero
- [ ] 1j
- [ ] Falso

Explicación: La letra `j` actúa como la unidad imaginaria en Python, por lo tanto `x**2` significa `j**2` que es igual a `-1`. La sentencia `x**2 == -1` se evalúa como `True`.

#### P164. ¿Qué se imprimirá en la consola si ejecuta este código?

```python
print(0xA + 0xB + 0xC)
```

- [x] 33
- [ ] 63
- [ ] 0xA + 0xB + 0xC
- [ ] Ninguna

Explicación: A, B y C son números enteros hexadecimales con valores 10, 11 y 12 respectivamente, por lo que la suma
de A, B y C es 33.

#### P165. ¿Qué mostrará este código en la pantalla?

```python
for i in range(5):
    print(i)
else:
    print("Done!")
```

- [ ] 1 2 3 4 5 ¡Listo!
- [ ] 0 1 2 3 4 5 ¡Listo!
- [x] 0 1 2 3 4 ¡Listo!
- [ ] Obtendrá un error de sintaxis.

#### P166. ¿Qué comparación de listas y tuplas en Python es correcta?

- [ ] Use listas en lugar de tuplas cuando tenga una colección de objetos relacionados pero diferentes.
- [ ] Use tuplas en lugar de listas cuando tenga una colección común de objetos similares.
- [x] Use tuplas en lugar de listas para funciones que necesitan devolver múltiples valores.
- [ ] Utilice listas en lugar de tuplas cuando la posición de los elementos sea importante.

#### P167. Considere el siguiente fragmento de código que usa decoradores para calcular el tiempo de ejecución de la función execution_fn:

```python
import functools
import time

def timer(MISSING_ARG_1):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        rval = func(*args, **kwargs)
        end_time = time.perf_counter()
        duration = end_time - start_time
        print(f"Executed in {duration:.4f} seconds")
        return MISSING_ARG_2
    return MISSING_ARG_3

@timer
def execution_fn():
    for i in range(3):
        time.sleep(1)

execution_fn()
```

**¿Cuáles de las siguientes opciones son los argumentos que faltan?**

- [ ] :

```
MISSING_ARG_1 = wrapper

MISSING_ARG_2 = rval

MISSING_ARG_3 = func
```

- [x] :

```
MISSING_ARG_1 = func

MISSING_ARG_2 = rval

MISSING_ARG_3 = wrapper
```

- [ ] :

```
MISSING_ARG_1 is empty

MISSING_ARG_2 = rval

MISSING_ARG_3 = wrapper
```

- [ ] :

```
MISSING_ARG_1 is empty

MISSING_ARG_2 = rval

MISSING_ARG_3 = func
```

#### P168. ¿Cuál de las siguientes declaraciones define un nuevo tipo de objeto llamado "Perro" en Python?

- [x] class Perro:
- [ ] Class de perro:
- [ ] Perro:
- [ ] class Perro

#### P169. Para usar canalizaciones en scikit-learn, importe desde el submódulo scikit-learn.**\_**.

- [ ] preprocesamiento
- [x] tubería (pipeline en Inglés [Referencia](https://es.wikipedia.org/wiki/Tuber%C3%ADa_(inform%C3%A1tica))
- [ ] filtros
- [ ] tubo_filtro

#### P170. Debe pasar un valor de **\_** para el argumento del eje al método de aplicación de Pandas para aplicar la función a cada fila.

- [ ] fila
- [ ] columna
- [x] 1
- [ ] 0

#### P171. Los puntos de datos en pyplot se llaman

- [ ] punteros
- [ ] puntos
- [x] marcadores
- [ ] ninguno de esos

#### P172. ¿Qué imprime este código?

```
a = np.array([[1, 2], [3, 4], [5, 6]])
c = a[(a > 3) & (a < 11)]
print(c)
```

- [ ] `[[3, 4], [5, 6]]`
- [ ] `[False, False, False, True, True, True]`
- [ ] `[[0,0], [3, 4], [5, 6]]`
- [x] `[4 5 6]`

