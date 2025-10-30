## Python (Lenguaje de Programación)

**Nota:** Esta es una traducción al español del quiz de evaluación de habilidades Python de LinkedIn. Para la versión original en inglés, consulte `python-quiz.md`.

---

#### Q1. ¿Qué es una clase abstracta?

- [ ] Una clase abstracta es el nombre de cualquier clase de la cual puedes instanciar un objeto.
- [ ] Las clases abstractas deben redefinirse cada vez que se instancia un objeto de ellas.
- [ ] Las clases abstractas deben heredar de clases concretas.
- [x] Una clase abstracta existe únicamente para que otras clases "concretas" puedan heredar de ella.

[referencia](https://www.geeksforgeeks.org/abstract-classes-in-python/)

#### Q2. ¿Qué sucede cuando usas la función incorporada `any()` en una lista?

- [ ] La función `any()` siempre devuelve un elemento aleatorio de la lista.
- [x] La función `any()` devuelve True si cualquier elemento de la lista se evalúa como True. De lo contrario, devuelve False.
- [ ] La función `any()` toma como argumentos la lista a verificar y el elemento a verificar. Si "cualquiera" de los elementos de la lista coincide con el elemento a verificar, la función devuelve True.
- [ ] La función `any()` devuelve un valor booleano que responde a la pregunta "¿Hay algún elemento en esta lista?"

**ejemplo**

```python
if any([True, False, False, False]) == True:
    print('Yes, there is True')
>>> 'Yes, there is True'
```

#### Q3. ¿A qué estructura de datos degenera un árbol binario si no está balanceado correctamente?

- [x] lista enlazada
- [ ] cola
- [ ] conjunto

[referencia](https://www.scaler.com/topics/linked-list/)

#### Q4. ¿Qué afirmación sobre los métodos estáticos es verdadera?

- [ ] Los métodos estáticos se llaman estáticos porque siempre devuelven `None`.
- [ ] Los métodos estáticos pueden vincularse a una clase o a una instancia de una clase.
- [x] Los métodos estáticos sirven principalmente como métodos de utilidad o ayuda, ya que no pueden acceder ni modificar el estado de una clase.
- [ ] Los métodos estáticos pueden acceder y modificar el estado de una clase o una instancia de una clase.

[referencia](https://www.geeksforgeeks.org/class-method-vs-static-method-python)

#### Q5. ¿Qué son los atributos?

- [ ] Los atributos son versiones largas de una declaración `if/else`, utilizadas al probar la igualdad entre objetos.
- [x] Los atributos son una forma de almacenar datos o describir un estado para una clase o una instancia de una clase.
- [ ] Los atributos son cadenas que describen las características de una clase.
- [ ] Los argumentos de función se llaman "atributos" en el contexto de métodos de clase y métodos de instancia.

**Explicación:** Los atributos se definen bajo la clase, y los argumentos van bajo las funciones. Los argumentos generalmente se refieren a parámetros, mientras que los atributos son los constructores de la clase o una instancia de la clase.

#### Q6. ¿Cuál es el término para describir este código?

`count, fruit, price = (2, 'apple', 3.5)`

- [ ] Asignación de tupla.
- [x] Desempaquetado de tupla.
- [ ] Coincidencia de tupla.
- [ ] Duplicación de tupla.

[Referencia](https://www.w3schools.com/python/python_tuples_unpack.asp)

#### Q7. ¿Qué método incorporado de lista usarías para eliminar elementos de una lista?

- [ ] método `.delete()`
- [ ] `pop(my_list)`
- [ ] `del(my_list)`
- [x] método `.pop()`

[Referencia](https://www.w3schools.com/python/ref_list_pop.asp)

**ejemplo**

```python
my_list = [1,2,3]
my_list.pop(0)
my_list
>>>[2,3]
```

#### Q8. ¿Cuál es uno de los usos más comunes de la librería `sys` de Python?

- [x] Para capturar argumentos de línea de comandos dados en tiempo de ejecución de un archivo.
- [ ] Para conectar diferentes sistemas, como conectar un front-end web, un servicio API, una base de datos y una aplicación móvil.
- [ ] Para tomar una instantánea de todos los paquetes y librerías en tu entorno virtual.
- [ ] Para analizar la salud de tu ecosistema Python mientras estás en un entorno virtual.

[referencia](https://docs.python.org/3/library/sys.html)

#### Q9. ¿Cuál es la complejidad temporal de acceder a un valor en un diccionario usando su clave?

- [ ] O(n), también llamado tiempo lineal.
- [ ] O(log n), también llamado tiempo logarítmico.
- [ ] O(n^2), también llamado tiempo cuadrático.
- [x] O(1), también llamado tiempo constante.

#### Q10. ¿Cuál es la sintaxis correcta para definir una clase llamada Game, si hereda de una clase padre llamada LogicGame?

- [x] `class Game(LogicGame): pass`
- [ ] `def Game(LogicGame): pass`
- [ ] `def Game.LogicGame(): pass`
- [ ] `class Game.LogicGame(): pass`

**Explicación:** La clase padre de la cual se hereda se pasa como argumento a la clase hija. Por lo tanto, la primera opción es la respuesta correcta.

#### Q11. ¿Cuál es el formato apropiado para escribir un doctest?

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

**Explicación:** Usa `'''` para comenzar el doc y agrega la salida de la celda después de `>>>`

#### Q12. ¿Qué tipo de datos incorporado de Python se usa comúnmente para representar una pila?

- [ ] `set`
- [x] `list`
- [ ] `None`
- [ ] `dictionary`
- [ ] `Solo puedes construir una pila desde cero.`

#### Q13. ¿Qué devolvería esta expresión?

```python
college_years = ['Freshman', 'Sophomore', 'Junior', 'Senior']
return list(enumerate(college_years, 2019))
```

- [ ] `[('Freshman', 2019), ('Sophomore', 2020), ('Junior', 2021), ('Senior', 2022)]`
- [ ] `[(2019, 2020, 2021, 2022), ('Freshman', 'Sophomore', 'Junior', 'Senior')]`
- [ ] `[('Freshman', 'Sophomore', 'Junior', 'Senior'), (2019, 2020, 2021, 2022)]`
- [x] `[(2019, 'Freshman'), (2020, 'Sophomore'), (2021, 'Junior'), (2022, 'Senior')]`

#### Q14. ¿Cuál es el propósito de la palabra clave "self" al definir o llamar métodos de instancia?

- [ ] `self` significa que no se requiere que se pasen otros argumentos al método.
- [ ] No hay un propósito real para el método `self`; es solo jerga histórica de la informática que Python mantiene para ser consistente con otros lenguajes de programación.
- [x] `self` se refiere a la instancia cuyo método fue llamado.
- [ ] `self` se refiere a la clase de la cual se heredó para crear el objeto usando `self`.

[Referencia](https://www.geeksforgeeks.org/self-in-python-class/)

**Ejemplo simple**

```python
class my_secrets:
    def __init__(self, password):
        self.password = password
        pass
instance = my_secrets('1234')
instance.password
>>>'1234'
```

#### Q15. ¿Cuál de estas características NO es una característica de los namedtuples?

- [ ] Puedes asignar un nombre a cada uno de los miembros del `namedtuple` y hacer referencia a él de esa manera, de la misma forma que accederías a las claves en un `dictionary`.
- [ ] Cada miembro de un objeto namedtuple puede ser indexado directamente, igual que en un `tuple` regular.
- [ ] Los `namedtuples` son tan eficientes en memoria como los `tuples` regulares.
- [x] No se necesita importación para usar `namedtuples` porque están disponibles en la biblioteca estándar.

**Debemos importarlo usando**: `from collections import namedtuple`

#### Q16. ¿Qué es un método de instancia?

- [x] Los métodos de instancia pueden modificar el estado de una instancia o el estado de su clase padre.
- [ ] Los métodos de instancia contienen datos relacionados con la instancia.
- [ ] Un método de instancia es cualquier método de clase que no toma argumentos.
- [ ] Un método de instancia es una función regular que pertenece a una clase, pero debe devolver `None`.

#### Q17. ¿Qué declaración NO describe el concepto de encapsulación en programación orientada a objetos?

- [ ] Protege los datos de interferencias externas.
- [x] Una clase padre está encapsulada y ningún dato de la clase padre pasa a la clase hija.
- [ ] Mantiene los datos y los métodos que pueden manipular esos datos en el mismo lugar.
- [ ] Solo permite que los métodos modifiquen los datos.

[Referencia](https://www.scaler.com/topics/python/encapsulation-in-python/)

#### Q18. ¿Cuál es el propósito de una declaración if/else?

- [ ] Le dice a la computadora qué pieza de código ejecutar si las instrucciones que has codificado son incorrectas.
- [ ] Ejecuta una pieza de código si todas las importaciones tuvieron éxito, y una pieza diferente de código si las importaciones no tuvieron éxito.
- [x] Ejecuta una pieza de código si una condición es verdadera, pero una pieza diferente de código si la condición es falsa.
- [ ] Le dice a la computadora qué pieza de código ejecutar si hay suficiente memoria para manejarlo, y qué pieza de código ejecutar si no hay suficiente memoria para manejarlo.

[Referencia](https://www.scaler.com/topics/python/python-if-else-statement/)

#### Q19. ¿Qué tipo de datos incorporado de Python es más adecuado para implementar una cola?

- [ ] dictionary
- [ ] set
- [ ] None. Solo puedes construir una cola desde cero.
- [x] list

#### Q20. ¿Cuál es la sintaxis correcta para instanciar un nuevo objeto del tipo Game?

- [ ] `my_game = class.Game()`
- [ ] `my_game = class(Game)`
- [x] `my_game = Game()`
- [ ] `my_game = Game.create()`

[Referencia](https://www.w3schools.com/python/python_classes.asp)

#### Q21. ¿Qué hace la función incorporada `map()`?

- [ ] Crea un camino de múltiples valores en un iterable hacia un solo valor.
- [x] Aplica una función a cada elemento de un iterable y devuelve el valor de esa función.
- [ ] Convierte un tipo de valor complejo en tipos de valores más simples.
- [ ] Crea un mapeo entre dos elementos diferentes de iterables diferentes.

[Referencia](https://www.geeksforgeeks.org/python-map-function/)

**Explicación:** - La sintaxis de la función `map()` es `list(map(function,iterable))`. Una calculadora simple de área usando map sería así

```python
import math
radius = [1,2,3]
area = list(map(lambda x: round(math.pi*(x**2), 2), radius))
area
>>> [3.14, 12.57, 28.27]
```

#### Q22. Si no devuelves explícitamente un valor de una función, ¿qué sucede?

- [ ] La función devolverá un RuntimeError si no devuelves un valor.
- [x] Si la palabra clave return está ausente, la función devolverá `None`.
- [ ] Si la palabra clave return está ausente, la función devolverá `True`.
- [ ] La función entrará en un bucle infinito porque no sabrá cuándo dejar de ejecutar su código.

[referencia](https://www.askpython.com/python/python-return-statement#). Cuando la declaración return es `None` o no tiene valor o no hay declaración return, la función devuelve `None`.

#### Q23. ¿Cuál es el propósito de la declaración `pass` en Python?

- [ ] Se usa para saltar la declaración `yield` de un generador y devolver un valor None.
- [x] Es una operación nula usada principalmente como marcador de posición en funciones, clases, etc.
- [ ] Se usa para pasar el control de un bloque de declaraciones a otro.
- [ ] Se usa para saltar el resto de un bucle `while` o `for` y volver al inicio del bucle.

La declaración pass se usa como marcador de posición para código futuro. Cuando se ejecuta la declaración pass, no pasa nada, pero evitas obtener un error cuando no se permite código vacío.
[referencia](https://realpython.com/python-pass/)

#### Q24. ¿Cuál es el término usado para describir los elementos que pueden pasarse a una función?

- [x] argumentos
- [ ] paradigmas
- [ ] atributos
- [ ] decoradores

#### Q25. ¿Qué tipo de colección se usa para asociar valores con claves únicas?

- [ ] `slot`
- [x] `dictionary`
- [ ] `queue`
- [ ] `sorted list`

[Referencia](https://www.w3schools.com/python/python_dictionaries.asp)

#### Q26. ¿Cuándo deja de iterar un bucle For?

- [ ] cuando encuentra un bucle infinito
- [ ] cuando encuentra una declaración if/else que contiene una palabra clave break
- [x] cuando ha evaluado cada elemento del iterable en el que está trabajando o se encuentra una palabra clave break
- [ ] cuando el tiempo de ejecución del bucle excede O(n^2)

[Referencia](https://www.w3schools.com/python/python_for_loops.asp)

#### Q27. Asumiendo que el nodo está en una lista enlazada simple, ¿cuál es la complejidad temporal de buscar un nodo específico en una lista enlazada simple?

- [x] El tiempo de ejecución es O(n) porque en el peor caso, el nodo que buscas es el último nodo, y cada nodo en la lista enlazada debe ser visitado.
- [ ] El tiempo de ejecución es O(nk), con n representando el número de nodos y k representando el tiempo requerido para acceder a cada nodo en memoria.
- [ ] El tiempo de ejecución no puede determinarse a menos que sepas cuántos nodos están en la lista enlazada simple.
- [ ] El tiempo de ejecución es O(1) porque puedes indexar directamente un nodo en una lista enlazada simple.

#### Q28. Dadas las siguientes tres listas, ¿cómo crearías una nueva lista que coincida con la salida deseada impresa abajo?

```python
fruits = ['Apples', 'Oranges', 'Bananas']
quantities = [5, 3, 4]
prices = [1.50, 2.25, 0.89]

#Salida deseada
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

#### Q29. ¿Qué sucede cuando usas la función incorporada all() en una lista?

- [ ] La función `all()` devuelve un valor booleano que responde a la pregunta "¿Todos los elementos en esta lista son iguales?"
- [ ] La función `all()` devuelve True si todos los elementos en la lista pueden convertirse a cadenas. De lo contrario, devuelve False.
- [ ] La función `all()` devolverá todos los valores en la lista.
- [x] La función `all()` devuelve True si todos los elementos en la lista se evalúan como True. De lo contrario, devuelve False.

[Referencia](https://www.geeksforgeeks.org/python-all-function/)

**Explicación:** `all()` devuelve `True` si todos los elementos en la lista son `True`. Ver el ejemplo abajo:

```python
test = [True, False, False, False]
if all(test) is True:
    print('Yeah, all of them are true.')
else:
    print('There is an imposter.')

>>> 'There is an imposter'
```

#### Q30. ¿Cuál es la sintaxis correcta para llamar un método de instancia en una clase llamada Game?

_(El formato de respuesta puede variar. Game y roll (o dice_roll) deben ser llamados sin parámetros.)_

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

#### Q31. ¿Cuál es el paradigma algorítmico del ordenamiento rápido (quick sort)?

- [ ] Retroceso (Backtracking)
- [ ] Programación dinámica
- [ ] Disminuir y conquistar
- [x] Dividir y conquistar

El ordenamiento por mezcla y el ordenamiento rápido emplean un paradigma algorítmico común basado en la recursión. Este paradigma, dividir y conquistar, descompone un problema en subproblemas similares al problema original, resuelve recursivamente los subproblemas, y finalmente combina las soluciones de los subproblemas para resolver el problema original.
[referencia](https://www.khanacademy.org/computing/computer-science/algorithms/merge-sort/a/divide-and-conquer-algorithms#:~:text=Both%20merge%20sort%20and%20quicksort,to%20solve%20the%20original%20problem.)

#### Q32. ¿Cuál es la complejidad temporal del método incorporado `.append()` de la lista?

- [x] O(1), también llamado tiempo constante.
- [ ] O(log n), también llamado tiempo logarítmico.
- [ ] O(n^2), también llamado tiempo cuadrático.
- [ ] O(n), también llamado tiempo lineal.

Esta función tiene una complejidad temporal constante, es decir, O(1), porque las listas son accesibles aleatoriamente, por lo que el último elemento puede alcanzarse en O(1), por eso el tiempo requerido para agregar el nuevo elemento al final de la lista es O(1).

#### Q33. ¿Cuál es la diferencia clave entre un `set` y una `list`?

- [ ] Un conjunto es una colección ordenada de elementos únicos. Una lista es una colección no ordenada de elementos no únicos.
- [ ] Los elementos pueden recuperarse de una lista pero no pueden recuperarse de un conjunto.
- [ ] Un conjunto es una colección ordenada de elementos no únicos. Una lista es una colección no ordenada de elementos únicos.
- [x] Un conjunto es una colección no ordenada de elementos únicos. Una lista es una colección ordenada de elementos no únicos.

#### Q34. ¿Cuál es la definición de abstracción aplicada a Python orientado a objetos?

- [ ] La abstracción significa que se puede usar un estilo de código diferente porque muchos detalles ya son conocidos por el programa en segundo plano.
- [x] La abstracción significa que la implementación está oculta al usuario, y solo se muestran los datos o información relevante.
- [ ] La abstracción significa que los datos y la funcionalidad de una clase se combinan en una sola entidad.
- [ ] La abstracción significa que una clase puede heredar de más de una clase padre.

La abstracción en Python se define como un proceso de manejar la complejidad ocultando información innecesaria al usuario.
[referencia](<https://www.mygreatlearning.com/blog/abstraction-in-python/#:~:text=What%20is%20Abstraction%20in%20Python,oriented%20programming%20(OOP)%20languages.>)

#### Q35. ¿Qué imprime esta función?

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

#### Q36. Elige la representación correcta del doctest para una función en Python.

- [ ] A

```python
def sum(a, b):
    # a = 1
    # b = 2
    # sum(a, b) = 3

    return a + b
```

- [ ] B

```python
def sum(a, b):
    """
    a = 1
    b = 2
    sum(a, b) = 3
    """

    return a + b
```

- [x] C

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

- [ ] D

```python
def sum(a, b):
    '''
    a = 1
    b = 2
    sum(a, b) = 3
    '''
    return a + b
```

**Explicación:** Usa `"""` para comenzar y terminar el docstring y usa `>>>` para representar la salida. Si escribes esto correctamente, también puedes ejecutar el doctest usando el módulo doctest incorporado

#### Q37. Supongamos que una clase Game hereda de dos clases padre: BoardGame y LogicGame. ¿Qué afirmación es verdadera respecto a los métodos de un objeto instanciado de la clase Game?

- [ ] Al instanciar un objeto, el objeto no hereda ninguno de los métodos de la clase padre.
- [ ] Al instanciar un objeto, el objeto heredará los métodos de la clase padre que tenga más métodos.
- [ ] Al instanciar un objeto, el programador debe especificar de qué clase padre heredar los métodos.
- [x] Una instancia de la clase Game heredará todos los métodos que las clases BoardGame y LogicGame poseen.

#### Q38. ¿Qué devuelve la llamada de namedtuple en un tipo de colección?

- [ ] una clase de objeto genérica con campos de parámetros iterables
- [ ] una clase de objeto genérica con campos nombrados no iterables
- [ ] una subclase de tuple con campos de parámetros no iterables
- [x] una subclase de tuple con campos nombrados iterables

**Ejemplo**

```python
# la función namedtuple acepta los siguientes argumentos para generar una clase
from collections import namedtuple
>>> Point = namedtuple('Point',['x','y'])
>>> point = Point(100, 200)
>>> point
    Point(x=100, y=200)

# Lo que te permite usar tanto desempaquetado como iteración para acceder
>>> x, y = point
>>> print(f'({x}, {y})')
    (100, 200)
>>> for coordinate in point:
        print(coordinate)
    100
    200
```

[Referencia](https://www.geeksforgeeks.org/namedtuple-in-python/?ref=lbp)

#### Q39. ¿Qué símbolo(s) usas para evaluar la igualdad entre dos elementos?

- [ ] `&&`
- [ ] `=`
- [x] `==`
- [ ] `||`

#### Q40. Examina el código abajo. ¿Cuál es la sintaxis correcta para cambiar el precio a 1.5?

```python
fruit_info = {
  'fruit': 'apple',
  'count': 2,
  'price': 3.5
}
```

- [x] `fruit_info['price'] = 1.5`
- [ ] `my_list[3.5] = 1.5`
- [ ] `1.5 = fruit_info['price]`
- [ ] `my_list['price'] == 1.5`

#### Q41. ¿Qué valor sería devuelto por esta verificación de igualdad?

`5 != 6`

- [ ] `yes`
- [ ] `False`
- [x] `True`
- [ ] `None`

**Explicación:** En Python, `!=` es equivalente a _no igual a_.

#### Q42. ¿Qué hace el método `__init__()` de una clase?

- [ ] Permite que las clases se conozcan entre sí si se define más de una clase en un solo archivo de código.
- [ ] Se incluye para preservar la compatibilidad hacia atrás de Python 3 a Python 2, pero ya no necesita usarse en Python 3.
- [x] Es un método que actúa como constructor y se llama automáticamente cada vez que se crea un nuevo objeto de una clase. Define el estado inicial de un nuevo objeto.
- [ ] Inicializa todas las importaciones que puedas haber incluido en la parte superior de tu archivo.

[Referencia](https://www.geeksforgeeks.org/__init__-in-python/)

**Ejemplo:**

```python
class test:
    def __init__(self):
        print('I came here without your permission lol')
        pass
t1 = test()
>>> 'I came here without your permission lol'
```

#### Q43. ¿Qué significa el término "complejidad espacial"?

- [ ] `Cuántos microprocesadores se necesitarían para ejecutar tu código en menos de un segundo`
- [ ] `Cuántas líneas de código hay en tu archivo de código`
- [x] `La cantidad de espacio ocupado en memoria en función del tamaño de la entrada`
- [ ] `Cuántas copias del archivo de código podrían caber en 1 GB de memoria`

#### Q44. ¿Cuál es la sintaxis correcta para crear una variable vinculada a un diccionario?

- [x] `fruit_info = {'fruit': 'apple', 'count': 2, 'price': 3.5}`
- [ ] `fruit_info =('fruit': 'apple', 'count': 2,'price': 3.5 ).dict()`
- [ ] `fruit_info = ['fruit': 'apple', 'count': 2,'price': 3.5 ].dict()`
- [ ] `fruit_info = to_dict('fruit': 'apple', 'count': 2, 'price': 3.5)`

#### Q45. ¿Cuál es la forma apropiada de escribir una comprensión de lista que represente todas las claves de este diccionario?

`fruits = {'Apples': 5, 'Oranges': 3, 'Bananas': 4}`

- [ ] `fruit_names = [x in fruits.keys() for x]`
- [ ] `fruit_names = for x in fruits.keys() *`
- [x] `fruit_names = [x for x in fruits.keys()]`
- [ ] `fruit_names = x for x in fruits.keys()`

#### Q46. ¿Cuál es el propósito de la palabra clave `self` al definir o llamar métodos en una instancia de un objeto?

- [ ] `self` se refiere a la clase de la cual se heredó para crear el objeto usando `self`.
- [ ] No hay un propósito real para el método `self`. Es solo jerga informática heredada que Python mantiene para ser consistente con otros lenguajes de programación.
- [ ] `self` significa que no se requiere que se pasen otros argumentos al método.
- [x] `self` se refiere a la instancia cuyo método fue llamado.

**Explicación:** - Intenta ejecutar el ejemplo de Q42 sin pasar el argumento `self` en el `__init__`, entenderás la razón. Obtendrás el error como este `__init__() takes 0 positional arguments but 1 was given`, esto significa que algo entra aunque no se haya especificado, que es la instancia misma.

#### Q47. ¿Qué afirmación sobre los métodos de clase es verdadera?

- [ ] Un método de clase es una función regular que pertenece a una clase, pero debe devolver None.
- [x] Un método de clase puede modificar el estado de la clase, pero no puede modificar directamente el estado de una instancia que hereda de esa clase.
- [ ] Un método de clase es similar a una función regular, pero un método de clase no toma argumentos.
- [ ] Un método de clase contiene todos los datos de una clase particular.

[Referencia](https://pynative.com/python-class-method/)  
Los métodos de clase son métodos que se llaman en la clase misma, no en una instancia de objeto específica. Por lo tanto, pertenece a un nivel de clase, y todas las instancias de clase comparten un método de clase.

#### Q48. ¿Qué significa que una función tenga un tiempo de ejecución lineal?

- [ ] No has usado muchos conceptos avanzados de programación informática en tu código.
- [ ] El nivel de dificultad al que está escrito tu código no es tan alto.
- [ ] Tomará menos de medio segundo para que tu programa se ejecute.
- [x] El tiempo requerido para que la función termine aumenta linealmente a medida que aumenta el tamaño de la entrada.

#### Q49. ¿Cuál es la forma apropiada de definir una función?

- [ ] `def getMaxNum(list_of_nums): # cuerpo de la función aquí`
- [ ] `func get_max_num(list_of_nums): # cuerpo de la función aquí`
- [ ] `func getMaxNum(list_of_nums): # cuerpo de la función aquí`
- [x] `def get_max_num(list_of_nums): # cuerpo de la función aquí`

El uso de guiones bajos como separadores de palabras se remonta a finales de los años 1960. Está particularmente asociado con C, se encuentra en The C Programming Language (1978), y contrasta con Pascal case (un tipo de camel case). Sin embargo, la convención tradicionalmente no tenía un nombre específico: la guía de estilo del lenguaje de programación Python simplemente se refiere a él como "lower_case_with_underscores".
En Usenet, el término snake_case se vio por primera vez en la comunidad Ruby en 2004, usado por Gavin Kistner, escribiendo:
Por cierto... ¿cómo llamas a este estilo de nomenclatura? ¿snake_case? Así es como lo llamaré hasta que alguien me corrija.

[referencia](https://en.wikipedia.org/wiki/Snake_case)

#### Q50. Según las pautas de estilo de codificación PEP 8, ¿cómo deben nombrarse los valores constantes en Python?

- [ ] en camel case sin usar guiones bajos para separar palabras -- ej. `maxValue = 255`
- [ ] en minúsculas con guiones bajos para separar palabras -- ej. `max_value = 255`
- [x] en mayúsculas con guiones bajos separando las palabras -- ej. `MAX_VALUE = 255`
- [ ] en case mixto sin usar guiones bajos para separar palabras -- ej. `MaxValue = 255`

Usa una letra mayúscula única, una palabra o palabras. Separa las palabras con guiones bajos para mejorar la legibilidad.
[Referencia](https://realpython.com/python-pep8/)

#### Q51. Describe la funcionalidad de una deque.

- [ ] Una deque agrega elementos de un lado y elimina elementos del otro lado.
- [ ] Una deque agrega elementos de un lado o ambos lados pero elimina únicamente elementos de la parte superior.
- [x] Una deque agrega elementos a uno o ambos extremos y elimina elementos de uno o ambos extremos.
- [ ] Una deque agrega elementos únicamente en la parte superior pero los elimina de un lado o ambos lados.

Deque o Double Ended Queue es una versión generalizada de la estructura de datos Queue que permite inserción y eliminación en ambos extremos.
[referencia](https://www.geeksforgeeks.org/deque-set-1-introduction-applications/?ref=gcse)

#### Q52. ¿Cuál es la sintaxis correcta para crear una variable vinculada a un conjunto?

- [x] `my_set = {0, 'apple', 3.5}`
- [ ] `my_set = to_set(0, 'apple', 3.5)`
- [ ] `my_set = (0, 'apple', 3.5).to_set()`
- [ ] `my_set = (0, 'apple', 3.5).set()`

#### Q53. ¿Cuál es la sintaxis correcta para definir un método `__init__()` que no toma parámetros?

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

#### Q54. ¿Cuál de las siguientes afirmaciones es VERDADERA sobre cómo se organizarían los datos numéricos en un árbol de búsqueda binaria?

- [x] Para cualquier nodo dado en un árbol de búsqueda binaria, el valor del nodo es mayor que todos los valores en el subárbol izquierdo del nodo y menor que los de su subárbol derecho.
- [ ] El árbol de búsqueda binaria no puede usarse para organizar y buscar datos numéricos, dadas las complicaciones que surgen con árboles muy profundos.
- [ ] El nodo superior del árbol de búsqueda binaria sería un número arbitrario. Todos los nodos a la izquierda del nodo superior deben ser menores que el número del nodo superior, pero no necesitan estar ordenados de una manera particular.
- [ ] El valor numérico más pequeño iría en el nodo más alto. El siguiente número más alto iría en su nodo hijo izquierdo, el siguiente número más alto después de eso iría en su nodo hijo derecho. Este patrón continuaría hasta que todos los valores numéricos estén en su nodo.

En ciencias de la computación, un árbol de búsqueda binaria (BST), también llamado árbol binario ordenado o clasificado, es una estructura de datos de árbol binario enraizado con la clave de cada nodo interno siendo mayor que todas las claves en el subárbol izquierdo del nodo respectivo y menor que las de su subárbol derecho.
[referencia](https://en.wikipedia.org/wiki/Binary_search_tree#:~:text=In%20computer%20science%2C%20a%20binary,ones%20in%20its%20right%20subtree.)

#### Q55. ¿Por qué usarías un decorador?

- [ ] Un decorador es similar a una clase y debe usarse si estás haciendo programación funcional en lugar de programación orientada a objetos.
- [ ] Un decorador es un indicador visual para alguien que lee tu código de que una parte de tu código es crítica y no debe modificarse.
- [x] Usas el decorador para modificar la funcionalidad de una función sin tener que modificar el código de la función.
- [ ] Una declaración de importación es precedida por un decorador, Python sabe importar la versión más reciente del paquete o librería importada.

Los decoradores nos permiten envolver otra función para extender el comportamiento de la función envuelta, sin modificarla permanentemente.
[referencia](https://www.geeksforgeeks.org/decorators-in-python/)

#### Q56. ¿Cuándo usarías un bucle for?

- [ ] Solo en ciertas situaciones, porque los bucles solo se usan para ciertos tipos de programación.
- [x] Cuando necesitas verificar cada elemento en un iterable de longitud conocida.
- [ ] Cuando quieres minimizar el uso de cadenas en tu código.
- [ ] Cuando quieres ejecutar código en un archivo para una función en otro archivo.

[Referencia](https://www.interviewbit.com/python-cheat-sheet/)

#### Q57. ¿Cuál es la forma más autodescriptiva de definir una función que calcule el impuesto de ventas en una compra?

- [ ] A:

```python
def tax(my_float):
    ''' Calcula el impuesto de ventas de una compra. Toma un float que representa el subtotal como argumento y devuelve un float que representa el impuesto de ventas.'''
    pass
```

- [ ] B:

```python
def tx(amt):
    ''' Obtiene el impuesto de una cantidad.'''
```

- [ ] C:

```python
def sales_tax(amount):
    ''' Calcula el impuesto de ventas de una compra. Toma un float que representa el subtotal como argumento y devuelve un float que representa el impuesto de ventas.'''
```

- [x] D:

```python
def calculate_sales_tax(subtotal):
    pass
```

#### Q58. ¿Qué pasaría si no modificaras el estado del elemento en el que un algoritmo opera de forma recursiva?

- [ ] No tienes que modificar el estado del elemento en el que el algoritmo hace recursión.
- [ ] Terminarías obteniendo un KeyError cuando la parte recursiva del código se quede sin elementos sobre los cuales hacer recursión.
- [x] Obtendrías un RuntimeError: maximum recursion depth exceeded.
- [ ] La función que usa recursión devolvería None.

[explicación](https://www.python-course.eu/python3_recursive_functions.php#Definition-of-Recursion)

#### Q59. ¿Cuál es la complejidad temporal de buscar un elemento en un árbol de búsqueda binaria?

- [ ] El tiempo de ejecución para buscar en un árbol de búsqueda binaria es O(1) porque cada nodo actúa como una clave, similar a un diccionario.
- [ ] El tiempo de ejecución para buscar en un árbol de búsqueda binaria es O(n!) porque cada nodo debe compararse con todos los otros nodos.
- [x] El tiempo de ejecución para buscar en un árbol de búsqueda binaria es generalmente O(h), donde h es la altura del árbol.
- [ ] El tiempo de ejecución para buscar en un árbol de búsqueda binaria es O(n) porque cada nodo en el árbol debe visitarse.

[explicación](https://www.geeksforgeeks.org/binary-search-tree-data-structure/)

#### Q60. ¿Por qué usarías un `mixin`?

- [ ] Usas un `mixin` para forzar a una función a aceptar un argumento en tiempo de ejecución aunque el argumento no estuviera incluido en la definición de la función.
- [ ] Usas un `mixin` para permitir que un decorador acepte argumentos de palabras clave.
- [ ] Usas un `mixin` para asegurar que los atributos y métodos de una clase no interfieran con las variables y funciones globales.
- [x] Si tienes muchas clases que todas necesitan tener la misma funcionalidad, usarías un `mixin` para definir esa funcionalidad.

Hay dos situaciones principales donde se usan los mixins:
Quieres proporcionar muchas funcionalidades opcionales para una clase.
Quieres usar una funcionalidad particular en muchas clases diferentes.
[referencia](https://stackoverflow.com/questions/533631/what-is-a-mixin-and-why-is-it-useful)
[explicación](https://www.youtube.com/watch?v=zVFLBfqV-q0)

#### Q61. ¿Cuál es la complejidad temporal de agregar un elemento a una pila y eliminar un elemento de una pila?

- [ ] Agregar elementos a una pila en tiempo O(1) y eliminar elementos de una pila en tiempo O(n).
- [x] Agregar elementos a una pila en tiempo O(1) y eliminar elementos de una pila en tiempo O(1).
- [ ] Agregar elementos a una pila en tiempo O(n) y eliminar elementos de una pila en tiempo O(1).
- [ ] Agregar elementos a una pila en tiempo O(n) y eliminar elementos de una pila en tiempo O(n).

#### Q62. ¿Qué declaración describe con precisión cómo se agregan y eliminan elementos de una pila?

- [ ] una pila agrega elementos de un lado y elimina elementos del otro lado.
- [x] una pila agrega elementos en la parte superior y elimina elementos de la parte superior.
- [ ] una pila agrega elementos en la parte superior y elimina elementos de cualquier lugar en la pila.
- [ ] una pila agrega elementos a cualquier extremo y elimina elementos de cualquier extremo.

**Explicación:** La pila usa el enfoque _último en entrar, primero en salir_ (last in first out).

#### Q63. ¿Qué es un caso base en una función recursiva?

- [x] Un caso base es la condición que permite al algoritmo dejar de hacer recursión. Usualmente es un problema lo suficientemente pequeño para resolverse directamente.
- [ ] El caso base es un resumen del problema general que necesita resolverse.
- [ ] El caso base se pasa como argumento a una función cuyo cuerpo hace uso de la recursión.
- [ ] El caso base es similar a una clase base, en que puede ser heredado por otro objeto.

#### Q64. ¿Por qué se considera una buena práctica abrir un archivo desde un script Python usando la palabra clave `with`?

- [ ] La palabra clave `with` te permite elegir en qué aplicación abrir el archivo.
- [ ] La palabra clave `with` actúa como un bucle `for`, y te permite acceder a cada línea en el archivo una por una.
- [ ] No hay beneficio en usar la palabra clave `with` para abrir un archivo en Python.
- [x] Cuando abres un archivo usando la palabra clave `with` en Python, Python se asegurará de que el archivo se cierre, incluso si se lanza una excepción o error.

Es una buena práctica usar la palabra clave 'with' cuando se trata de objetos archivo. La ventaja es que el archivo se cierra correctamente después de que su suite termina, incluso si se lanza una excepción en algún punto. Usar with también es mucho más corto que escribir bloques try-finally equivalentes:

**ejemplo**

```python
>>> f = open('workfile', 'w', encoding="utf-8")
>>> with open('workfile', encoding="utf-8") as f:
    read_data = f.read()
# Podemos verificar que el archivo se ha cerrado automáticamente.
>>> f.closed
True
```

[Referencia](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)

#### Q65. ¿Por qué usarías un entorno virtual?

- [x] Los entornos virtuales crean una "burbuja" alrededor de tu proyecto para que cualquier librería o paquete que instales dentro no afecte toda tu máquina.
- [ ] Los equipos con empleados remotos usan entornos virtuales para poder compartir código, hacer revisiones de código y colaborar remotamente.
- [ ] Los entornos virtuales eran comunes en Python 2 porque aumentaban las características faltantes en el lenguaje. Los entornos virtuales no son necesarios en Python 3 debido a los avances en el lenguaje.
- [ ] Los entornos virtuales están vinculados a tu cuenta de GitHub o Bitbucket, permitiéndote acceder virtualmente a cualquiera de tus repositorios desde cualquier máquina.

#### Q66. ¿Cuál es la forma correcta de ejecutar todos los doctests en un archivo dado desde la línea de comandos?

- [x] `python3 -m doctest <_filename_>`
- [ ] `python3 <_filename_>`
- [ ] `python3 <_filename_> rundoctests`
- [ ] `python3 doctest`

También hay un atajo de línea de comandos para ejecutar testmod(). Puedes instruir al intérprete de Python para ejecutar el módulo doctest directamente desde la biblioteca estándar y pasar el/los nombre(s) de módulo en la línea de comandos:
`python -m doctest -v example.py`
Esto importará example.py como un módulo independiente y ejecutará testmod() en él. Ten en cuenta que esto puede no funcionar correctamente si el archivo es parte de un paquete e importa otros submódulos de ese paquete.  
[referencia](https://docs.python.org/3/library/doctest.html)  
[video tutorial](https://www.youtube.com/watch?v=P8qm0VAbbww&t=180s)

#### Q67. ¿Qué es una función lambda?

- [ ] cualquier función que hace uso de constantes científicas o matemáticas, a menudo representadas por letras griegas en la escritura académica
- [ ] una función que se ejecuta cuando se usan decoradores
- [ ] cualquier función cuya definición está contenida dentro de cinco líneas de código o menos
- [x] una función pequeña y anónima que puede tomar cualquier número de argumentos pero tiene solo una expresión para evaluar

[Referencia](https://www.guru99.com/python-lambda-function.html)

**Explicación:**

> La notación lambda es una función anónima que puede tomar cualquier número de argumentos con solo una expresión (es decir, no puede sobrecargarse). Ha sido introducida en otros lenguajes de programación, como C++ y Java. La notación lambda permite a los programadores "evitar" la declaración de función.

#### Q68. ¿Cuál es la diferencia principal entre listas y tuplas?

- [ ] Puedes acceder a un elemento específico en una lista indexando a su posición, pero no puedes acceder a un elemento específico en una tupla a menos que iteres a través de la tupla
- [x] Las listas son mutables, lo que significa que puedes cambiar los datos que están dentro de ellas en cualquier momento. Las tuplas son inmutables, lo que significa que no puedes cambiar los datos que están dentro de ellas una vez que has creado la tupla.
- [ ] Las listas son inmutables, lo que significa que no puedes cambiar los datos que están dentro de ellas una vez que has creado la lista. Las tuplas son mutables, lo que significa que puedes cambiar los datos que están dentro de ellas en cualquier momento.
- [ ] Las listas pueden contener varios tipos de datos a la vez, pero las tuplas solo pueden contener el mismo tipo de datos si hay múltiples elementos presentes.

[Referencia](https://www.geeksforgeeks.org/python-difference-between-list-and-tuple/)

#### Q69. ¿Qué devuelve un generador?

- [ ] None
- [x] Un objeto iterable
- [ ] Una estructura de datos de lista enlazada de una lista no vacía
- [ ] Todas las claves del diccionario dado

#### Q70. ¿Cuál es la diferencia entre atributos de clase y atributos de instancia?

- [ ] Los atributos de instancia pueden cambiarse, pero los atributos de clase no pueden cambiarse
- [x] Los atributos de clase son compartidos por todas las instancias de la clase. Los atributos de instancia pueden ser únicos solo para esa instancia
- [ ] No hay diferencia entre atributos de clase y atributos de instancia
- [ ] Los atributos de clase pertenecen solo a la clase, no a la instancia de esa clase. Los atributos de instancia se comparten entre todas las instancias de una clase

#### Q71. ¿Cuál es la sintaxis correcta para crear un método de instancia?

- [ ] :

```python
def get_next_card():
  # cuerpo del método aquí
```

- [x] :

```python
def get_next_card(self):
  # cuerpo del método aquí
```

- [ ] :

```python
def self.get_next_card():
  # cuerpo del método aquí
```

- [ ] :

```python
def self.get_next_card(self):
  # cuerpo del método aquí
```

#### Q72. ¿Cuál es la forma correcta de llamar una función?

- [x] `get_max_num([57, 99, 31, 18])`
- [ ] `call.(get_max_num)`
- [ ] `def get_max_num([57, 99, 31, 18])`
- [ ] `call.get_max_num([57, 99, 31, 18])`

#### Q73. ¿Cómo agregas un comentario a un script Python existente?

- [ ] `-- Esto es un comentario`
- [x] `# Esto es un comentario`
- [ ] `/* Esto es un comentario */`
- [ ] `// Esto es un comentario`

[Referencia](https://realpython.com/python-comments-guide/)

#### Q74. ¿Cuál es la sintaxis correcta para reemplazar la cadena `apple` en la lista con la cadena `orange`?

```python
my_list = ['kiwi', 'apple', 'banana']
```

- [ ] `orange = my_list[1]`
- [x] `my_list[1] = 'orange'`
- [ ] `my_list['orange'] = 1`
- [ ] `my_list[1] == orange`

#### Q75. ¿Qué pasará si usas un bucle while y olvidas incluir lógica que eventualmente detenga el bucle while?

- [ ] No pasará nada; tu computadora sabe cuándo dejar de ejecutar el código en el bucle while.
- [ ] Obtendrás un KeyError.
- [x] Tu código se quedará atascado en un bucle infinito.
- [ ] Obtendrás un WhileLoopError.

#### Q76. Describe la funcionalidad de una cola (queue).

- [x] Una cola agrega elementos a cualquier extremo y elimina elementos de cualquier extremo.
- [ ] Una cola agrega elementos en la parte superior y elimina elementos de la parte superior.
- [ ] Una cola agrega elementos en la parte superior y elimina elementos de cualquier lugar en una lista.
- [ ] Una cola agrega elementos en la parte superior y elimina elementos de cualquier lugar en la cola.

#### Q77. ¿Qué opción es el ejemplo sintácticamente más correcto de ramificación condicional?

- [x] A:

```python
num_people = 5

if num_people > 10:
    print("There is a lot of people in the pool.")
elif num_people > 4:
    print("There are some people in the pool.")
else:
    print("There is no one in the pool.")
```

- [ ] B:

```python
num_people = 5

if num_people > 10:
    print("There is a lot of people in the pool.")
if num_people > 4:
    print("There are some people in the pool.")
else:
    print("There is no one in the pool.")
```

- [ ] C:

```python
num_people = 5

if num_people > 10;
    print("There is a lot of people in the pool.")
elif num_people > 4;
    print("There are some people in the pool.")
else;
    print("There is no one in the pool.")
```

- [ ] D:

```python
if num_people > 10;
    print("There is a lot of people in the pool.")
if num_people > 4;
    print("Hay algunas personas en la piscina.")
else;
    print("No hay nadie en la piscina.")
```

#### Q78. ¿Cómo funciona `defaultdict`?

- [ ] `defaultdict` creará automáticamente un diccionario para ti que tiene claves que son los enteros 0-10.
- [ ] `defaultdict` fuerza a un diccionario a aceptar solo claves de los tipos especificados cuando se crea el `defaultdict` (como cadenas o enteros).
- [x] Si intentas leer de un `defaultdict` con una clave inexistente, se creará un nuevo par clave-valor por defecto para ti en lugar de lanzar un `KeyError`.
- [ ] `defaultdict` almacena una copia de un diccionario en memoria al cual puedes volver por defecto si el original se modifica involuntariamente.

`defaultdict` es un diccionario tipo contenedor presente en el módulo collections. La funcionalidad de los diccionarios y de `defaultdict` es casi la misma, excepto que `defaultdict` nunca lanza un `KeyError`. Proporciona un valor por defecto para la clave que no existe.

**ejemplo**

```python
# Función para devolver un valor por defecto
# para claves que no están presentes
def def_value():
    return "Not Present"

# Definiendo el dict
d = defaultdict(def_value)
```

[referencia](https://www.geeksforgeeks.org/defaultdict-in-python/)

#### Q79. ¿Cuál es la sintaxis correcta para agregar una clave llamada `variety` al diccionario `fruit_info` que tiene un valor de `Red Delicious`?

- [ ] `fruit_info['variety'] == 'Red Delicious'`
- [x] `fruit_info['variety'] = 'Red Delicious'`
- [ ] `red_delicious = fruit_info['variety']`
- [ ] `red_delicious == fruit_info['variety']`

#### Q80. ¿Cuándo usarías un bucle `while`?

- [ ] Cuando quieres minimizar el uso de cadenas en tu código.
- [ ] Cuando quieres ejecutar código en un archivo mientras código en otro archivo también se está ejecutando.
- [x] Cuando quieres que un código continúe ejecutándose mientras una cierta condición sea verdadera.
- [ ] Cuando necesitas ejecutar dos o más piezas de código al mismo tiempo en el mismo archivo.

**Ejemplo Simple**

```python
i = 1
while i<6:
    print(f"Countdown: {i}")
    i = i + 1
```

#### Q81. ¿Cuál es la sintaxis correcta para definir un método `__init__()` que establece atributos específicos de instancia al crear una nueva instancia de clase?

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

**Explicación:** Al instanciar un nuevo objeto de una clase dada, el método `__init__()` tomará tanto `attr1` como `attr2`, y establecerá sus valores a su atributo de objeto correspondiente, por eso necesitas usar `self.attr1 = attr1` en lugar de `attr1 = attr1`.

#### Q82. ¿Qué imprimiría esta función recursiva si se llama sin parámetros?

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

#### Q83. En Python, al usar conjuntos, usas **\_** para calcular la intersección entre dos conjuntos y **\_** para calcular la unión.

- [ ] `Intersect`; `union`
- [ ] `|`; `&`
- [x] `&`; `|`
- [ ] `&&`; `||`

#### Q84. ¿Qué devolverá este fragmento de código?

```python
import numpy as np
np.ones([1,2,3,4,5])
```

- [ ] Devuelve una matriz 5x5; cada fila tendrá los valores 1,2,3,4,5.
- [ ] Devuelve un array con los valores 1,2,3,4,5.
- [ ] Devuelve cinco matrices cuadradas diferentes llenas de unos. La primera es 1x1, la segunda 2x2, y así sucesivamente hasta 5x5.
- [x] Devuelve un array de 5 dimensiones de tamaño 1x2x3x4x5 lleno de 1.

[Referencia](https://www.geeksforgeeks.org/numpy-ones-python/)

#### Q85. Te encuentras con una FileNotFoundException al usar solo el nombre del archivo en la función `open`. ¿Cuál podría ser la solución más simple?

- [ ] Asegúrate de que el archivo esté en el `PATH` del sistema.
- [ ] Crea un enlace simbólico para permitir mejor acceso al archivo.
- [x] Copia el archivo al mismo directorio donde se ejecuta el script.
- [ ] Agrega la ruta del archivo a la variable de entorno `PYTHONPATH`.

#### Q86. ¿Qué devolverá este comando?

```python
{x for x in range(100) if x%3 == 0}
```

- [x] Un conjunto de todos los múltiplos de 3 menores que 100.
- [ ] Un conjunto de todos los números de 0 a 100 multiplicados por 3.
- [ ] Una lista de todos los múltiplos de 3 menores que 100.
- [ ] Un conjunto de todos los múltiplos de 3 menores que 100 excluyendo 0.

[referencia](https://www.geeksforgeeks.org/comprehensions-in-python/) Es una `Comprensión de Conjunto` porque está entre '{}', llaves, así que devolverá un 'Conjunto' !

#### Q87. ¿Qué permite hacer el operador // en Python 3?

- [x] Realizar división entera.
- [ ] Realizar operaciones con exponentes.
- [ ] Encontrar el residuo de una operación de división.
- [ ] Realizar división de punto flotante.

#### Q88. ¿Qué archivo se importa para usar fechas en Python?

- [x] `datetime`
- [ ] `dateday`
- [ ] `daytime`
- [ ] `timedate`

#### Q89. ¿Cuál es la sintaxis correcta para definir una clase llamada Game?

- [ ] `def Game(): pass`
- [ ] `def Game: pass`
- [x] `class Game: pass`
- [ ] `class Game(): pass`

[referencia aquí](https://docs.python.org/3/tutorial/classes.html)

#### Q90. ¿Cuál es la sintaxis correcta para llamar un método de instancia en una clase llamada Game?

- [ ] `my_game = Game(self) self.my_game.roll_dice()`
- [ ] `my_game = Game() self.my_game.roll_dice()`
- [x] `my_game = Game() my_game.roll_dice()`
- [ ] `my_game = Game(self) my_game.roll_dice(self)`

#### Q91. ¿Cuál es la salida de este código? (NumPy ha sido importado como np.)

```python
a = np.array([1,2,3,4])
print(a[[False, True, False, False]])
```

- [ ] `{0,2}`
- [x] `[2]`
- [ ] `{2}`
- [ ] `[0,2,0,0]`

#### Q92. Supongamos que tienes una variable de cadena definida como y="stuff;thing;junk;". ¿Cuál sería la salida de este código?

```python
z = y.split(';')
len(z)
```

- [ ] 17
- [x] 4
- [ ] 0
- [ ] 3

**Explicación:**

```python
y="stuff;thing;junk"
    len(z) ==> 3

y="stuff;thing;junk;"
    len(z) ==> 4
```

#### Q93. ¿Cuál es la salida de este código?

```python
num_list = [1,2,3,4,5]
num_list.remove(2)
print(num_list)
```

- [ ] `[1,2,4,5]`
- [x] `[1,3,4,5]`
- [ ] `[3,4,5]`
- [ ] `[1,2,3]`

**Explicación:** `.remove()` está basado en el valor del elemento, no en el índice; aquí, elimina el elemento que coincide con "2". Si quisieras eliminar un elemento basado en su índice, usarías `.pop()`.

```python
num_list = [1,2,3,4,5]

num_list.pop(2)
>>> [1,2,4,5]

num_list.remove(2)
>>> [1,3,4,5]
```

#### Q94. ¿Qué comando creará una lista de 10 a 1? Ejemplo:

`[10,9,8,7,6,5,4,3,2,1]`

- [ ] `reversed(list(range(1,11)))`
- [ ] `list(reversed(range(1,10)))`
- [ ] `list(range(10,1,-1))`
- [x] `list(reversed(range(1,11)))`

[Referencia](https://www.w3schools.com/python/python_tuples.asp)

#### Q95. ¿Qué fragmento de código imprimirá la misma salida que este fragmento?

```Python
import math
print(math.pow(2,10)) # imprime 2 elevado a la potencia 10
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

[Referencia](https://www.digitalocean.com/community/tutorials/how-to-do-math-in-python-3-with-operators#:~:text=The%20**%20operator%20in%20Python,multiplied%20by%20itself%203%20times.)

#### Q96. Los elementos rodeados de `[]` son **\_**, `{}` son **\_**, y `()` son **\_**.

- [ ] solo conjuntos; listas o diccionarios; tuplas
- [ ] listas; solo conjuntos; tuplas
- [ ] tuplas; conjuntos o listas; diccionarios
- [x] listas; diccionarios o conjuntos; tuplas

[Referencia](https://www.geeksforgeeks.org/differences-and-applications-of-list-tuple-set-and-dictionary-in-python/)

#### Q97. ¿Cuál es la salida de este código? (NumPy ha sido importado como np.)

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

#### Q98. ¿Qué imprimirá este código?

```python
number = 3
print(f"The number is {number}")
```

- [x] `The number is 3`
- [ ] `the number is 3`
- [ ] `THE NUMBER IS 3`
- [ ] Lanza una `TypeError` porque el entero debe convertirse a cadena.

[Referencia](https://colab.research.google.com/drive/1PRGf7Wgcr_gQk7snnxxuc5rL9O1ky9Xg?usp=sharing)

#### Q99. ¿Qué sintaxis crea correctamente una variable vinculada a una tupla?

- [ ] `my_tuple tup(2, 'apple', 3.5) %D`
- [ ] `my_tuple [2, 'apple', 3.5].tuple() %D`
- [x] `my_tuple = (2, 'apple', 3.5)`
- [ ] `my_tuple = [2, 'apple', 3.5]`

[Referencia](https://beginnersbook.com/2018/02/python-tuple/)

#### Q100. ¿Qué modo NO es una forma válida de acceder a un archivo desde un script Python?

- [ ] `write('w')`
- [x] `scan('s')`
- [ ] `append('a')`
- [ ] `read('r')`

1. [Referencia](https://docs.python.org/3/library/functions.html#open)
2. [Referencia](https://www.w3schools.com/python/ref_list_append.asp)

#### Q101. NumPy te permite multiplicar dos arrays sin un bucle for. Esto es un ejemplo de \_.

- [x] Vectorización.
- [ ] Atribuciones.
- [ ] Aceleración.
- [ ] Programación funcional.

#### Q102. ¿Qué tipo de datos incorporado de Python puede usarse como tabla hash?

- [ ] `set`
- [ ] `list`
- [ ] `tuple`
- [x] `dictionary`

#### Q103. ¿Qué función Python te permite ejecutar comandos shell de Linux en Python?

- [ ] `sys.exc_info()`
- [x] `os.system()`
- [ ] `os.getcwd()`
- [ ] `sys.executable`

#### Q104. Supongamos que tienes el siguiente fragmento de código y quieres extraer una lista con solo las letras. ¿Qué fragmento de código NO logrará ese objetivo?

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

**Explicación:** El primero (la opción correcta) devuelve la lista de los valores (los números). El resto de las opciones devuelven una lista de las claves.

#### Q105. Cuando un array es grande, NumPy no imprimirá todo el array cuando se le da la función incorporada `print`. ¿Qué función puedes usar dentro de NumPy para forzarlo a imprimir todo el array?

- [ ] `set_printparams`
- [x] `set_printoptions`
- [ ] `set_fullprint`
- [ ] `setp_printwhole`

#### Q106. ¿Cuándo usarías un bloque try/except en el código?

- [x] Usas bloques `try/except` cuando quieres ejecutar algún código, pero necesitas una forma de ejecutar código diferente si se lanza una excepción.
- [ ] Usas bloques `try/except` dentro de pruebas unitarias para que las pruebas unitarias siempre pasen.
- [ ] Usas bloques `try/except` para poder demostrar a tus revisores de código que intentaste un nuevo enfoque, pero si el nuevo enfoque no es lo que estaban buscando, pueden dejar comentarios bajo la palabra clave `except`.
- [ ] Usas bloques `try/except` para que ninguna de tus funciones o métodos devuelva `None`.

[Referencia](https://runestone.academy/ns/books/published/fopp/Exceptions/using-exceptions.html#:~:text=The%20reason%20to%20use%20try,you're%20writing%20the%20code)

#### Q107. En Python, ¿cómo puede el compilador identificar el bloque interno de un bucle for?

- [x] `debido al nivel de indentación después del bucle for`
- [ ] `debido a la palabra clave end al final del bucle for`
- [ ] `porque el bloque está rodeado por llaves ({})`
- [ ] `debido al espacio en blanco al final del cuerpo del bucle for`

#### Q108. ¿Qué mecanismo Python es más adecuado para decirle a un usuario que está usando una función obsoleta?

- [ ] `sys.stdout`
- [ ] Traceback
- [x] Warnings (Advertencias)
- [ ] Exceptions

#### Q109. ¿Cuál será el valor de `x` después de ejecutar este código?

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

#### Q110. ¿Cómo accederías y almacenarías todas las claves de este diccionario de una vez?

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

#### Q111. ¿Qué está mal con esta definición de función?

```python
def be_friendly(greet = "How are you!", name):
    pass
```

- [ ] `name` es una palabra reservada.
- [ ] Los guiones bajos no están permitidos en nombres de funciones.
- [x] Un argumento sin valor por defecto sigue a un argumento con valor por defecto.
- [ ] No hay nada malo con esta definición de función.

#### Q112. Dado que NumPy se importa como `np`, ¿qué opción devolverá `True`?

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

#### Q113. ¿Cómo agregas un comentario a un script Python existente?

- [ ] `// Esto es un comentario`
- [x] `# Esto es un comentario`
- [ ] `-- Esto es un comentario`
- [ ] `/* Esto es un comentario */`

#### Q114. En este fragmento de código, ¿a qué serán equivalentes los valores de c y d?

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

#### Q115. ¿Qué dos funciones dentro de la biblioteca NumPy podrías usar para resolver un sistema de ecuaciones lineales?

- [x] `linalg.eig() and .matmul()`
- [ ] `linalg.inv() and .dot()`
- [ ] `linalg.det() and .dot()`
- [ ] `linalg.inv() and .eye()`

**Explicación:** Entender esta respuesta requiere conocimiento de álgebra lineal. Algunos sistemas de ecuaciones pueden resolverse mediante el método de _diagonalización_, que implica encontrar los **vectores propios y valores propios** de la matriz del sistema y multiplicar matrices relacionadas.

#### Q116. ¿Cuál es la sintaxis correcta para crear una variable vinculada a una lista?

- [ ] `my_list = (2, 'apple', 3.5)`
- [x] `my_list = [2, 'apple', 3.5]`
- [ ] `my_list = [2, 'apple', 3.5].to_list()`
- [ ] `my_list = to_list(2, 'apple', 3.5)`

[Referencia](https://www.tutorialspoint.com/python/python_lists.htm)

#### Q117. Este código proporciona el **\_** de la lista de números.

```python
num_list = [21, 13, 19, 3, 11, 5, 18]
num_list.sort()
num_list[len(num_list) // 2]
```

- [ ] moda
- [ ] promedio
- [ ] media
- [x] mediana

**Explicación:** `//` es el operador de división entera, que es una operación de división normal que devuelve el entero más grande posible, menor o igual al resultado de la división normal. Aquí se usa para encontrar la mediana, que es el valor que separa la mitad superior de la mitad inferior de una muestra de datos, encontrando el índice del elemento de la lista en el medio de la lista. (Esto es suficiente para una lista con un número impar de elementos; si la lista tuviera un número par de elementos, promediarías los valores de los dos elementos del medio para encontrar el valor de la mediana.)

#### Q118. ¿Cuáles son las dos principales estructuras de datos en la biblioteca Pandas?

- [ ] Arrays y DataFrames
- [ ] Series y Matrices
- [ ] Matrices y DataFrames
- [x] Series y DataFrames

[Referencia](https://pandas.pydata.org/docs/user_guide/dsintro.html)

#### Q119. Supongamos que tienes una variable llamada `vector` de tipo np.array con 10,000 elementos. ¿Cómo puedes convertir `vector` en una variable llamada `matrix` con dimensiones 100x100?

- [ ] `matrix = (vector.shape = (100,100))`
- [ ] `matrix = vector.to_matrix(100,100)`
- [ ] `matrix = matrix(vector,100,100)`
- [x] `matrix = vector.reshape(100, 100)`

[Referencia](https://www.w3schools.com/python/numpy/numpy_array_reshape.asp)

#### Q120. ¿Qué opción es un tipo de datos inmutable?

- [ ] Dictionary
- [ ] List
- [ ] Set
- [x] String

[Referencia](https://www.tutorialspoint.com/python_text_processing/python_string_immutability.htm)

#### Q121. ¿Cuál es la salida de este código?

```python
def myFunction(country = "France"):
    print(f"Hello, I am from {country}")

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

#### Q122. Elige la opción abajo para la cual no se puede crear una instancia de la clase.

- [ ] Clase Anónima
- [ ] Clase Padre
- [ ] Clase Anidada
- [x] Clase Abstracta

[Referencia](https://www.scaler.com/topics/python/data-abstraction-in-python/)

#### Q123. Usando Pandas, cargamos un conjunto de datos de Kaggle, estructurado como en la imagen abajo. ¿Qué comando devolverá el número total de sobrevivientes?

![Q129](images/Q129.png?raw=png)

- [x] `sum(titanic['Survived'])`
- [ ] `[x for x in titanic['Survived'] if x == 1]`
- [ ] `len(titanic["Survived"])`
- [ ] `sum(titanic['Survived']==0)`

**Explicación:** El `titanic['Survived']` devuelve un objeto `pandas.Series`, que contiene la columna `Survived` del `DataFrame`.
Sumar los valores de esta columna (es decir, `sum(titanic['Survived'])`) devuelve el número total de sobrevivientes ya que un sobreviviente está representado por un 1 y una pérdida por 0.

#### Q124. ¿Cómo crearías una lista de tuplas que coincida con estas listas de personajes y actores?

```python
characters = ["Iron Man", "Spider Man", "Captain America"]
actors = ["Downey", "Holland", "Evans"]

# salida ejemplo : [("IronMan", "Downey"), ("Spider Man", "Holland"), ("Captain America", "Evans")]
```

- [ ] `[(x,y)] for x in characters for y in actors]`
- [x] `zip(characters, actors)`
- [ ] &shy;

  ```python
  d = {}

  for x in range(1, len(characters)):
      d[x] = actors[x]
  ```

- [ ] `{x:y for x in characters for y in actors}`

#### Q125. ¿Qué devolverá esta declaración?

```python
{x : x*x for x in range(1,100)}
```

- [ ] Un diccionario con `x` como clave, y `x` al cuadrado como su valor; de 1 a 100.
- [x] Un diccionario con `x` como clave, y `x` al cuadrado como su valor; de 1 a 99.
- [ ] Un conjunto de tuplas, consistente en (`x`, `x` al cuadrado); de 1 a 99.
- [ ] Una lista con todos los números al cuadrado de 1 a 99.

#### Q126. La Similaridad de Jaccard es una fórmula que te dice qué tan similares son dos conjuntos. Se define como la cardinalidad de la intersección dividida por la cardinalidad de la unión. ¿Qué opción es una implementación precisa en Python?

![Q132](images/Q132.png?raw=png)

- [ ] `def jaccard(a, b): return len (a | b) / len (a & b)`
- [x] `def jaccard(a, b): return len (a & b) / len (a | b)`
- [ ] `def jaccard(a, b): return len (a && b) / len (a || b)`
- [ ] `def jaccard(a, b): return a.intersection(b) / a.union(b)`

[Referencia](https://docs.python.org/3/tutorial/datastructures.html?highlight=set#sets.)

#### Q127. ¿Qué opción NO es un tipo numérico nativo en Python?

- [ ] Long
- [ ] Int
- [ ] Float
- [x] Double

#### Q128. ¿Cuál será la salida de este código?

```python
[1,2,3] * 3
```

- [ ] `[3,2,3]`
- [x] `[1, 2, 3, 1, 2, 3, 1, 2, 3]`
- [ ] Obtendrás un error de tipo.
- [ ] `[3,6,9]`

#### Q129. Dada una lista definida como numbers = `[1,2,3,4]`, ¿cuál es el valor de `numbers[-2]`?

- [ ] 1
- [x] 3
- [ ] 2
- [ ] Se lanza una excepción IndexError.

#### Q130. ¿Qué afirmación sobre las cadenas en Python es verdadera?

- [x] Las cadenas pueden estar encerradas por comillas dobles (") o comillas simples (').
- [ ] Las cadenas solo pueden estar encerradas en comillas simples (').
- [ ] Las cadenas de un solo carácter deben estar encerradas en comillas simples ('), y el resto debe estar encerrado en comillas dobles (").
- [ ] Las cadenas solo pueden estar encerradas en comillas dobles (").

#### Q131. ¿Cuál es la sintaxis correcta para definir un método `__init__()` que no toma parámetros?

- [ ] `def __init__(self): pass`
- [ ] `class __init__(self): pass`
- [ ] `class __init__(): pass`
- [x] `def __init__(): pass`

`()` - parámetro vacío.
`self` - se refiere a todas las instancias dentro de una clase.
`__init__` - un método reservado, también conocido como constructor.
`__init__()` - siempre se ejecuta cuando se inicia la clase.

#### Q132. Supongamos que necesitas usar la función `sin` de la biblioteca `math`. ¿Cuál es la sintaxis correcta para importar solo esa función?

- [x] `from math import sin`
- [ ] `import sin from math`
- [ ] `import math.sin`
- [ ] `from math.sin import math`

#### Q133. ¿Cuál es la sintaxis correcta para crear una variable vinculada a un conjunto?

- [x] `my_set = {0, 'apple', 3.5}`
- [ ] `my_set = to_set(0, 'apple', 3.5)`
- [ ] `my_set = (0, 'apple', 3.5).to_set()`
- [ ] `my_set = (0, 'apple', 3.5).set()`

#### Q134. ¿Cuál es el resultado de este código?

```python
import numpy as np
a = np.array([1, 2, 3])
print(a[1])
```

- [x] `2`
- [ ] `[1, 2, 3]`
- [ ] `1`
- [ ] `[2]`

#### Q135. ¿Cuál es la sintaxis correcta para crear una variable vinculada a un diccionario?

- [ ] `fruit_info = to_dict("fruit": "apple", "count": 2, "price": 3.5)`
- [x] `fruit_info = {"fruit": "apple", "count": 2, "price": 3.5}`
- [ ] `fruit_info = ("fruit": "apple", "count": 2, "price": 3.5).dict()`
- [ ] `fruit_info = ("fruit": "apple", "count": 2, "price": 3.5)`

#### Q136. A menudo es el caso que la biblioteca pandas se usa para datos **\_** y NumPy para datos **\_**.

- [ ] cadenas; numéricos
- [ ] no estructurados; estructurados
- [ ] numéricos; tabulares
- [x] tabulares; numéricos

**Explicación:** La biblioteca Pandas se usa comúnmente para trabajar con datos tabulares, como datos en forma de tablas o hojas de cálculo. Proporciona estructuras de datos y funciones para manipulación y análisis de datos. Por otro lado, NumPy es una biblioteca poderosa para computación numérica en Python, y a menudo se usa para realizar operaciones matemáticas en datos numéricos, como arrays y matrices.

#### Q137. ¿Qué necesitas hacer para instalar paquetes adicionales en Python?

- [ ] Usar un compilador C como `gcc` o `clang`.
- [x] Usar un gestor de paquetes como `pip` o `conda`.
- [ ] Usar un IDE como Notepad++ o Idle.
- [ ] Usar un gestor de paquetes como NPM o NuGet.

#### Q138. La imagen abajo fue creada usando Matplotlib. Es un gráfico de distribución de una lista de enteros llenos con números usando la función **\_** y graficado con **\_**.

![Q132](images/Q138.png?raw=png)

- [ ] `random.uniform(0,50);plt.hist`
- [x] `random.gauss(50,20);plt.hist`
- [ ] `random();plt.scatter`
- [ ] `random.triangular(0,50);plt.bar`

[Referencia](https://www.geeksforgeeks.org/random-gauss-function-in-python/)

#### Q139. En este fragmento de código, ¿cuáles serán los valores de `a` y `b`?

```python
import numpy as np

a = np.arange(100)
b = a[50:60:2]
```

- [x] `a`: todos los enteros de 0 a 99 (inclusive); `b`: todos los enteros pares de 50 a 58 (inclusive).
- [ ] `a`: todos los enteros de 0 a 100 (inclusive); `b`: todos los enteros pares de 50 a 60 (inclusive).
- [ ] `a`: todos los enteros de 0 a 99 (inclusive); `b`: todos los enteros pares de 50 a 60 (inclusive).
- [ ] `a`: todos los enteros de 0 a 99 (inclusive); `b`: todos los enteros impares de 49 a 59 (inclusive).

#### Q140. Al usar NumPy en Python, ¿cómo verificas la dimensionalidad (número y longitud de dimensiones) de un objeto llamado `my_object`?

- [ ] `my_object.get_shape()`
- [x] `my_object.shape`
- [ ] `my_object.dim()`
- [ ] `len(my_object)`

#### Q141. Asume que tienes una lista no vacía llamada `mylist` y quieres buscar un valor específico. El número mínimo de comparaciones será **\_** y el número máximo de comparaciones será **\_**.

- [ ] `len(mylist); len(mylist)`
- [x] `1; len(mylist)`
- [ ] `2; len(mylist)`
- [ ] `0; len(mylist)`

**Explicación:** Puedes usar una declaración break y el valor que se busca puede ser el primer elemento de la lista, dado que no está vacía.

#### Q142. Si una función no tiene una declaración return, ¿qué devuelve?

- [ ] `0`
- [ ] `True`
- [x] `None`
- [ ] `False`

#### Q143. Supongamos que quieres verificar si dos matrices pueden multiplicarse usando NumPy para propósitos de depuración. ¿Cómo completarías este fragmento de código llenando los espacios en blanco con las variables apropiadas?

```python
import numpy as np

def can_matrices_be_multiplied (matrix1, matrix2):
    rowsMat1, columnsMat1 = matrix1.shape
    rowsMat2, columnsMat2 = matrix2.shape

    if _____ == ______ :
        print("Las matrices pueden multiplicarse!")
        return True
    else:
        return False
```

- [ ] columnsMat1; rowsMat1;
- [x] columnsMat1; rowsMat2;
- [ ] columnsMat1; columnsMat2;
- [ ] columnsMat2; rowsMat1;

[referencia](https://www.khanacademy.org/math/precalculus/x9e81a4f98389efdf:matrices/x9e81a4f98389efdf:multiplying-matrices-by-matrices/a/multiplying-matrices#).
Una matriz puede multiplicarse por cualquier otra matriz que tenga el mismo número de filas que la primera tiene columnas. Es decir, una matriz con 2 columnas puede multiplicarse por cualquier matriz con 2 filas

#### Q144. ¿Cuál es la salida de esta comprensión?

`[(x, x+1) for x in range(1,5)] `

- [ ] [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]
- [ ] [1,2,3,4,5]
- [ ] [(1, 2), (2, 3), (3, 4)]
- [x] [(1, 2), (2, 3), (3, 4), (4, 5)]

#### Q145. En Python, un método de clase debe tener **\_** como decorador de función, y el primer parámetro del método será una referencia a **\_**.

- [x] @classmethod; la clase
- [ ] inline; la clase
- [ ] static; self
- [ ] @static; self

[Referencia](https://docs.python.org/3/library/functions.html#classmethod)

#### Q146. ¿Qué fragmento de código imprimirá _My name is Joffrey, son of Robert_?

- [ ] :

```python
class Father():
    name = 'Robert'

class Person(Father):
    def __init__(self, name):
        self.fathername = super.name
        self.name = name

    def introduce(self):
        print(f"My name is {self.name} son of {self.fathername}")

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
        print(f"My name is {self.name} son of {self.fathername}")


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
        print(f"My name is {self.name} son of {super.name}")

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
        print(f"My name is {self.name} son of {base.name}")

king = Person("Joffrey")
king.introduce()

```

**Explicación:** En el primero, super no tiene `.name` (debería ser `self.name`). El tercero pierde Robert, y `base` no está definido en el cuarto.

#### Q147. ¿Qué salida produce este código en la consola, asumiendo que defaultdict ya ha sido importado?

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
      # se lanzará una excepción
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

**Explicación:** Los diccionarios usualmente resultan en una excepción cuando se usa la sintaxis de corchetes cuadrados. Defaultdict aquí devuelve un valor por defecto dedicado por el primer parámetro, así que en lugar de lanzar una excepción, devuelven el valor por defecto. Nota que esto necesita importarse como sigue: `from collections import defaultdict`

[Referencia](https://www.geeksforgeeks.org/defaultdict-in-python/)

#### Q148. ¿Qué devolverá esta línea de código? (Asume que `n` ya está definido como cualquier valor entero positivo.)

```python
[x*2 for x in range(1,n)]
```

- [x] Una lista con todos los números pares menores que 2\*n.
- [ ] Un diccionario con todos los números pares menores que 2\*n.
- [ ] Una lista con todos los números impares menores que 2\*n.
- [ ] Una lista con todos los números pares menores o iguales a 2\*n.

[Referencia](https://www.w3schools.com/python/ref_func_range.asp)

#### Q149. ¿Qué imprime este código en la consola?

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

- [ ] `C`
- [ ] `B`
- [x] `A`
- [ ] `BC`

#### Q150. ¿Cuál es la longitud máxima de un identificador Python?

- [ ] 32
- [ ] 16
- [ ] 128
- [x] No se especifica una longitud fija.

[referencia](https://peps.python.org/pep-0008/) No se especifica una longitud fija pero Pep-8 especifica bajo "Longitud Máxima de Línea" "Limitar todas las líneas a un máximo de 79 caracteres".

#### Q151. ¿Cuál será el valor de la variable `i` cuando el siguiente bucle termine su ejecución?

```python
for i in range(5): pass
```

- [ ] 5
- [ ] La variable se vuelve no disponible.
- [ ] 6
- [x] 4

#### Q152. Los `f-strings` también se llaman:

- [ ] Expresiones de cadenas formateadas.
- [ ] Cadenas funcionales.
- [ ] Cadenas formateadas modulo.
- [x] Literales de cadenas formateadas.

#### Q153. ¿Cuántos CPUs (o núcleos) aprovechará simultáneamente la biblioteca de threading de Python?

- [x] Uno.
- [ ] Todos los CPUs disponibles.
- [ ] Dos.
- [ ] Tres.

**Explicación:** El threading de Python está restringido a un solo CPU a la vez. La biblioteca multiprocessing te permitirá ejecutar código en diferentes procesadores.

#### Q154. ¿Cuál será el valor de `y` en este código?

```python
x = 5
y = 1 + (20 if x < 5 else 30)
```

- [ ] `False`
- [ ] `21`
- [ ] `2`
- [x] `31`

[Referencia](https://www.w3schools.com/python/python_conditions.asp)

**Explicación:** Si tienes solo una declaración para ejecutar, una para `if` y una para `else`, puedes ponerlo todo en la misma línea.

```python
x = 5
# Esta es la misma declaración expandida a múltiples líneas
y = 1
if (x < 5):
    y += 20
else:
    y += 30
```

#### Q155. ¿El proceso de pickling en Python incluye?

- [x] Conversión de una jerarquía de objetos Python en flujo de bytes.
- [ ] Conversión de una tabla de datos en una lista.
- [ ] Conversión de un flujo de bytes en jerarquía de objetos Python.
- [ ] Conversión de una lista en una tabla de datos.

[referencia](https://docs.python.org/3/library/pickle.html#:~:text="Pickling"%20is%20the%20process%20whereby,back%20into%20an%20object%20hierarchy.)  
"Pickling" es el proceso por el cual una jerarquía de objetos Python se convierte en un flujo de bytes, y "unpickling" es la operación inversa, por la cual un flujo de bytes (de un archivo binario u objeto tipo bytes) se convierte de vuelta en una jerarquía de objetos.

#### Q156. ¿Cuál es la salida del siguiente programa?

```python
print("codescracker".endswith("er"))
```

- [x] `True`
- [ ] `1`
- [ ] `2`
- [ ] `False`

#### Q157. ¿Es la lista mutable en Python?

- [x] Verdadero
- [ ] Falso

#### Q158. ¿Cuál es la salida del siguiente programa?

```python
print("programming".center())
```

- [ ] `cr`
- [ ] `programming`
- [x] Error que dice `TypeError: center expected at least 1 argument, got 0`.
- [ ] Ninguna de las anteriores.

[referencia](https://www.w3schools.com/python/ref_string_center.asp). El método center() alineará al centro la cadena, usando un carácter especificado (el espacio es el predeterminado) como carácter de relleno.  
Sintaxis: `string.center(length, character)` donde `length` es requerido!

#### Q159. ¿Quién creó el lenguaje de programación Python?

- [ ] Tim Berners-Lee
- [ ] Ada Lovelace
- [x] Guido van Rossum
- [ ] Alan Turing

#### Q160. ¿Qué colección está ordenada, es modificable y permite miembros duplicados?

- [ ] Set
- [ ] Tuple
- [ ] Dictionary
- [x] List

#### Q161. ¿Qué se imprimirá en la consola si ejecutas este código?

```python
x = 1j
print(x**2 == -1)
```

- [ ] Un error de tiempo de ejecución diciéndote que la variable `j` no ha sido inicializada.
- [x] `True`
- [ ] `1j`
- [ ] `False`

**Explicación:** La letra `j` actúa como la unidad imaginaria en Python, por lo tanto `x**2` significa `j**2` que es igual a `-1`. La declaración `x**2 == -1` se evalúa como `True`.

#### Q162. ¿Qué se imprimirá en la consola si ejecutas este código?

```python
print(0xA + 0xB + 0xC)
```

- [x] `33`
- [ ] `63`
- [ ] `0xA + 0xB + 0xC`
- [ ] `None`

**Explicación:** `A`, `B` y `C` son enteros hexadecimales con valores `10`, `11` y `12` respectivamente, así que la suma de `A`, `B` y `C` es `33`.

#### Q163. ¿Qué salida produce este código en la pantalla?

```python
for i in range(5):
    print(i)
else:
    print("Done!")
```

- [ ] A

```python
1
2
3
4
5
Done!
```

- [ ] B

```python
0
1
2
3
4
5
Done!
```

- [x] C

```python
0
1
2
3
4
Done!
```

- [ ] D:
      Obtendrás un error de sintaxis.

#### Q164. ¿Qué comparación de listas y tuplas en Python es correcta?

- [ ] Usa listas en lugar de tuplas cuando tienes una colección de objetos relacionados pero diferentes.
- [ ] Usa tuplas en lugar de listas cuando tienes una colección común de objetos similares.
- [x] Usa tuplas en lugar de listas para funciones que necesitan devolver múltiples valores.
- [ ] Usa listas en lugar de tuplas cuando la posición de los elementos es importante.

[Referencia](https://www.scaler.com/topics/python/tuples-in-python/)

#### Q165. Considera el siguiente fragmento de código que usa decoradores para calcular el tiempo de ejecución de la función `execution_fn`:

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

**¿Cuál de las siguientes opciones son los argumentos faltantes?**

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
MISSING_ARG_1 está vacío

MISSING_ARG_2 = rval

MISSING_ARG_3 = wrapper
```

- [ ] :

```
MISSING_ARG_1 está vacío

MISSING_ARG_2 = rval

MISSING_ARG_3 = func
```

#### Q166. ¿Cuál de las siguientes declaraciones define un nuevo tipo de objeto llamado `Dog` en Python?

- [x] `class Dog:`
- [ ] `Dog class:`
- [ ] `Dog:`
- [ ] `class Dog`

#### Q167. Para usar pipelines en `scikit-learn`, importa del submódulo `scikit-learn.\_`.

- [ ] `preprocessing`
- [x] `pipeline`
- [ ] `filters`
- [ ] `pipe_filter`

[referencia](https://scikit-learn.org/stable/modules/compose.html) La sintaxis correcta es en realidad: `from sklearn.pipeline import Pipeline`

#### Q168. Debes pasar un valor de **\_** para el argumento axis al método apply de Pandas para aplicar la función a cada fila.

- [ ] row
- [ ] col
- [x] 1
- [ ] 0

#### Q169. Los puntos de datos en Pyplot se llaman...

- [ ] ... punteros.
- [ ] ... puntos.
- [x] ... marcadores.
- [ ] ... ninguna de estas.

#### Q170. ¿Qué imprime este código?

```python
a = np.array([[1, 2], [3, 4], [5, 6]])
c = a[(a > 3) & (a < 11)]
print(c)
```

- [ ] `[[3, 4], [5, 6]]`
- [ ] `[False, False, False, True, True, True]`
- [ ] `[[0,0], [3, 4], [5, 6]]`
- [x] `[4 5 6]`

#### Q171. Asume que `m`, `n`, y `p` son enteros positivos. En la siguiente comprensión, ¿cuántas veces se llamará la función `randint`?

```python
[ [ [ randint(1,100) for i in range(m) ] for j in range(n) ] for k in range(p) ]
```

- [x] `m * n * p`
- [ ] El mayor valor de `(m,n,p)`.
- [ ] 1 millón.
- [ ] `m + n + p`

#### Q172. Supongamos que tienes una clase llamada `MyClass` que tiene herencia múltiple y métodos con el mismo nombre en sus ancestros. ¿Qué método de clase podrías llamar para ver qué método tendrá prioridad cuando sea invocado?

- [x] `MyClass.__mro__`
- [ ] `MyClass.hierarchy()`
- [ ] `callable(MyClass)`
- [ ] `dir(MyClass)`

**Explicación:** MRO significa Method Resolution Order (Orden de Resolución de Métodos). Devuelve una lista de tipos de los cuales la clase se deriva, en el orden en que se buscan los métodos.

#### Q173. Supongamos que tienes una lista de empleados descrita por el código abajo. Quieres asignar a Alice el mismo salario que Charlie. ¿Qué opción logrará eso?

```python
employees = {
    'alice':{
        'position':'Lead Developer',
        'salary':1000
    },
    'bob':{
        'position': 'Lead Artist',
        'salary':2000
    },
    'charlie':{
        'position':'cfo',
        'salary':3000
    }
}
```

- [x] `employees['alice']['salary'] = employees['charlie']['salary']`
- [ ] `employees.alice.salary = employees.charlie.salary`
- [ ] `employees['alice'][1] = employees['charlie'][1]`
- [ ] `employees['alice'].salary = employees['charlie'].salary`

**Explicación:** Esto es acceder a una clave en un diccionario anidado dentro de otro diccionario. El comando `employees['alice']['salary'] = employees['charlie']['salary']` asigna el valor de la clave `salary` en el diccionario del empleado `charlie` al valor de la clave `salary` en el diccionario del empleado `alice`.

#### Q174. Te dan este fragmento de código. Asume que `m` y `n` ya están definidos como algún valor entero positivo. Cuando se complete, ¿cuántas tuplas contendrá mi lista?

```python
mylist = []

for i in range(m):
    for j in range(n):
        mylist.append((i,j))
```

- [ ] `m`
- [ ] `m + n`
- [ ] `n`
- [x] `m * n`

**Explicación:** Este código se ejecutará `m` x `n` veces, si ejecutas este código, creará `m` x `n` tuplas.

El primer bucle se ejecuta `m` veces y el bucle interno se ejecutará `n` veces. La única iteración del primer bucle solo se completará cuando todas las `n` iteraciones de un bucle interno se hayan completado. Este es el mismo proceso para la 2da, y 3ra, ... `m`-ésima iteraciones para el bucle externo. En general, ambos bucles se ejecutarán `m` x `n` veces.

#### Q175. ¿Qué te proporcionará esta comprensión?

```python
{x : [y for y in range (1, x) if x % y == 0] for x in range (2, 100)}
```

- [x] Un diccionario cuyas claves son los números del 2 al 99 (inclusive), y sus valores respectivos son sus factores.
- [ ] Un diccionario cuyas claves son los números del 2 al 99 (inclusive), y sus valores respectivos son una lista del 1 al valor de la clave misma (inclusive).
- [ ] Un diccionario cuyas claves son los números del 2 al 99 (inclusive), y sus valores respectivos son los números pares del 1 al valor de la clave misma (inclusive).
- [ ] Un diccionario cuyas claves son los números del 2 al 99 (inclusive), y sus valores respectivos son los números impares del 1 al valor de la clave misma (inclusive).

#### Q176. ¿Cuál es un uso común de la biblioteca sys de Python?

- [ ] tomar una instantánea de todos los paquetes y bibliotecas en tu entorno virtual
- [ ] conectar varios sistemas, como conectar un front-end web, un servicio API, una base de datos y una aplicación móvil
- [x] capturar argumentos de línea de comandos dados en tiempo de ejecución de un archivo
- [ ] escanear la salud de tu ecosistema Python mientras estás en un entorno virtual

#### Q177. ¿Cuál es la salida de 17 % 15?

- [ ] 17
- [ ] 15
- [x] 2
- [ ] 16

#### Q178. Sean las listas 'characters' y 'actors' definidas como se da. ¿Cuál de las siguientes líneas de código da la salida deseada?

```python
characters = ["Iron Man", "Spider Man", "Captain America"]
actors = ["Downey", "Holland", "Evans"]

#Salida deseada : [("Iron Man", "Downey"), ("Spider Man", "Holland"), ("Captain America", "Evans")]
```

- [ ] print( zip( characters, actors ) )
- [ ] print( { x: y for x in characters for y in actors } )
- [ ] print( [ ( x, y ) for x in characters for y in actors ] )
- [x] print( list( zip( characters, actors ) ) )

Explicación: zip() es la función correcta para este caso de uso. Sin embargo, zip() hace un objeto tipo zip que es un iterador. Por lo tanto, usar list() es necesario para convertir el objeto zip en una lista de tuplas que puede mostrarse o accederse directamente. Las otras opciones tienen errores lógicos.

#### Q179. ¿Cuándo se ejecuta el bloque `if __name__ == "__main__":` en un script Python?

- [ ] Siempre, ya que es requerido en cada script Python.
- [x] Solo cuando el script se ejecuta directamente desde la línea de comandos o como el programa principal.
- [ ] Solo cuando el script contiene errores de sintaxis.
- [ ] Solo cuando el script se importa como módulo en otro script.

El bloque `if __name__ == "__main__":` se ejecuta cuando el script se ejecuta directamente pero no cuando se importa como módulo en otro script.
[referencia](https://docs.python.org/3/tutorial/modules.html#executing-modules-as-scripts)

#### Q180. ¿Cuál será la salida del siguiente código Python?

```python
def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5]
squared_numbers = map(square, numbers)
result = list(squared_numbers)
print(result)
```

- [x] `[1, 4, 9, 16, 25]`
- [ ] `[1, 2, 3, 4, 5]`
- [ ] `[1, 8, 27, 64, 125]`
- [ ] `[2, 4, 6, 8, 10]`

El código define una función `square` para calcular el cuadrado de un número. Luego usa la función `map` para aplicar esta función a cada elemento en la lista `numbers`, resultando en un nuevo iterable. Finalmente, el constructor `list` se usa para convertir este iterable en una lista. La salida será una lista de números al cuadrado.
[referencia](https://docs.python.org/3/library/functions.html#map)

#### Q181. ¿Cuál de las siguientes NO es una función incorporada válida en Python?

- [ ] int
- [ ] string
- [ ] boolean
- [x] array

[Fuente](https://docs.python.org/3/library/functions.html)

#### Q182. ¿Cuál de los siguientes NO es un tipo de datos válido en Python?

- [ ] int
- [x] char
- [ ] float
- [ ] str

#### Q183. En Python, ¿qué función se usa para leer una línea de la entrada de consola?

- [x] input()
- [ ] read_line()
- [ ] console_input()
- [ ] getline()

[Referencia](https://www.geeksforgeeks.org/taking-input-from-console-in-python/)

#### Q184. ¿Cuál será la salida del siguiente código Python?

`print("Hello {name1} and {name2}".format(name1='foo', name2='bin'))`

- [x] Hello foo and bin
- [ ] Hello {name1} and {name2}
- [ ] Error
- [ ] Hello and

#### Q185. ¿Cuál será la salida del siguiente fragmento de código?

```python
def outer_func(x):
    y = x + 1
    def inner_func():
        return y + x
    return inner_func

x = 10
y = 20
closure_func = outer_func(x)
print(closure_func())
```

- [ ] 30
- [x] 21
- [ ] 11
- [ ] 31

**Explicación**: Cuando se llama `outer_func(10)`, `y` se establece en 11 dentro de `outer_func`. La `inner_func`, que tiene acceso al ámbito de `outer_func`, devuelve `y` + `x`. Cuando se llama `closure_func()`, usa `y` = `11` (de `outer_func`) y `x` = `10` del ámbito global, no del argumento de la función. Por lo tanto, `closure_func()` devuelve 11 + 10 = 21.

#### Q186. ¿Cuál es la salida del siguiente código Python?

```python
x = 5
def func():
    x = 10
    print(x)
func()
print(x)
```

- [x] 10, 5
- [ ] 10, 10
- [ ] 5, 5
- [ ] 5, 10

**Explicación:**
La respuesta correcta es 10, 5.

En el código dado, la variable `x` se define primero en el ámbito global con un valor de 5. Dentro de la función `func()`, se crea una nueva variable local `x` y se le asigna el valor de 10. Cuando se llama `func()`, imprime el valor de la `x` local, que es 10.

Después de la llamada a la función, la declaración print fuera de la función se refiere a la `x` global, que aún tiene el valor de 5.

Por lo tanto, la salida es 10, 5.

#### Q187. ¿Cuál es la salida del siguiente código Python?

```python
def func(a, b=2, c=3):
    print(a, b, c)

func(10)
func(10, 20)
func(10, 20, 30)
```

- [x] 10 2 3, 10 20 3, 10 20 30
- [ ] 10 2 3, 10 2 3, 10 2 3
- [ ] 10 2 3, 10 20 2, 10 20 30
- [ ] 10 2 3, 10 20 3, 10 20 30

**Explicación:**
La respuesta correcta es 10 2 3, 10 20 3, 10 20 30.

En el código dado, la función `func()` tiene tres parámetros: `a`, `b`, y `c`. `b` y `c` tienen valores por defecto de 2 y 3, respectivamente.

Cuando se llama `func(10)`, solo se proporciona el primer parámetro `a`, así que `b` y `c` toman sus valores por defecto de 2 y 3, respectivamente.

Cuando se llama `func(10, 20)`, el primer parámetro `a` es 10, y el segundo parámetro `b` es 20. El tercer parámetro `c` toma su valor por defecto de 3.

Cuando se llama `func(10, 20, 30)`, se proporcionan los tres parámetros, así que `a` es 10, `b` es 20, y `c` es 30.

Por lo tanto, la salida es:
10 2 3
10 20 3
10 20 30

#### Q188. ¿Cuál es la salida del siguiente código Python?

```python
x = [1, 2, 3]
y = x
y.append(4)
print(x)
```

- [ ] [1, 2, 3]
- [x] [1, 2, 3, 4]
- [ ] [4, 1, 2, 3]
- [ ] Error

**Explicación:**
La respuesta correcta es [1, 2, 3, 4].

En Python, asignar y = x no crea una nueva lista; tanto x como y se refieren al mismo objeto en memoria.
Así que cuando llamamos y.append(4), modifica la lista original a la que ambas variables apuntan.
Por lo tanto, imprimir x mostrará la lista actualizada [1, 2, 3, 4].

#### Q189. ¿Cuál es la salida del siguiente código Python?

```python
def add_item(item, item_list=[]):
    item_list.append(item)
    return item_list

print(add_item(1))
print(add_item(2))
print(add_item(3, []))
```

- [ ] [1] [2] [3]
- [x] [1] [1,2] [3]
- [ ] [1,2,3] [1,2,3] [3]
- [ ] [1] [2] [3,1,2]

**Explicación:**
La respuesta correcta es [1] [1, 2] [3].

En Python, los argumentos mutables por defecto (como las listas) se evalúan solo una vez cuando se define la función — no cada vez que se llama.
Eso significa que las primeras dos llamadas a add_item() comparten la misma lista por defecto, así que acumula valores [1] y luego [1, 2].

Sin embargo, en la tercera llamada add_item(3, []), pasamos una nueva lista vacía, así que crea una lista separada [3].

#### Q190. ¿Qué método se usa para implementar la función `len()` para una clase personalizada?

- [ ] `__length__()`
- [x] `__len__()`
- [ ] `__size__()`
- [ ] `__count__()`

[Referencia Métodos Especiales](https://docs.python.org/3/reference/datamodel.html#special-method-names)

#### Q191. ¿Qué producirá este código?

```python
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result
    return wrapper

@decorator
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
```

- [x] `Before function call`, `Hello, Alice!`, `After function call`
- [ ] `Hello, Alice!`
- [ ] `Before function call`, `After function call`
- [ ] `decorator`

#### Q192. ¿Qué afirmación sobre los generadores de Python es correcta?

- [ ] Los generadores almacenan todos los valores en memoria a la vez
- [x] Los generadores producen valores bajo demanda usando la palabra clave `yield`
- [ ] Los generadores solo pueden crearse con comprensiones de lista
- [ ] Los generadores no pueden iterarse múltiples veces

#### Q193. ¿Cuál es la salida de este código?

```python
class Parent:
    def method(self):
        print("Parent method")

class Child(Parent):
    def method(self):
        super().method()
        print("Child method")

obj = Child()
obj.method()
```

- [x] `Parent method`, `Child method`
- [ ] `Child method`, `Parent method`
- [ ] `Child method`
- [ ] `Parent method`

#### Q194. ¿Qué método se usa para implementar la representación de cadena para depuración?

- [ ] `__str__()`
- [x] `__repr__()`
- [ ] `__format__()`
- [ ] `__debug__()`

#### Q195. ¿Qué producirá este código?

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))
print(fibonacci.cache_info())
```

- [x] `55` y estadísticas de caché
- [ ] `55` y `None`
- [ ] `RecursionError`
- [ ] `TypeError`
