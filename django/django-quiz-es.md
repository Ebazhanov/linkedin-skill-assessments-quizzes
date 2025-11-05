## Django

#### P1. Para almacenar en caché todo tu sitio para una aplicación en Django, agregas todas las configuraciones excepto ¿cuál de estas?

- [ ] django.middleware.common.CommonMiddleware
- [ ] django.middleware.cache.UpdateCacheMiddleware
- [ ] django.middleware.cache.FetchFromCacheMiddleware
- [x] django.middleware.cache.AcceleratedCacheMiddleware

**Referencia:**
Django viene con un sistema de caché robusto que te permite guardar páginas dinámicas, por lo que no tienen que ser calculadas para cada solicitud. Por conveniencia, Django ofrece caché con diferentes granularidades: desde el sitio web completo hasta páginas, partes de páginas, resultados de consultas de BD hasta cualquier objeto en memoria. Middleware de caché. Si está habilitado, cada página impulsada por Django se almacenará en caché según la URL.

#### P2. ¿En qué lenguaje de programación está escrito Django?

- [ ] C++
- [ ] Java
- [x] Python
- [ ] Ruby

#### P3. Para proporcionar automáticamente un valor para un campo, o para hacer validación que requiera acceso a más de un solo campo, debes sobrescribir el método `___` en la clase `___`.

- [ ] validate(); Model
- [ ] group(); Model
- [ ] validate(); Form
- [x] clean(); Model

#### P4. Un cliente quiere que su sitio pueda cargar episodios de "Rick & Morty" por número o por título, por ejemplo, shows/3/3 o shows/picklerick. ¿Qué patrón de URL recomiendas?

- [ ] A

```python
url(r'shows/<int:season>/<int:episode>/', views.episode_number),
url(r'shows/<slug:episode_name>/', views.episode_name)
```

- [x] B

```python
path('shows/<int:season>/<int:episode>/', views.episode_number),
path('shows/<slug:episode_name>/', views.episode_name)
```

- [ ] C

```python
path('shows/<int:season>/<int:episode>', views.episode_number),
path('shows/<slug:episode_name>/', views.episode_number)
```

- [ ] D

```python
url(r'^show/(?P<season>[0-9]+)/(?P<episode>[0-9]+)/$', views.episode_number),
url(r'^show/(?P<episode_name>[\w-]+)/', views.episode_name
```

#### P5. ¿Cómo determinas en el momento de inicio si se debe usar un middleware?

- [x] Lanzar MiddlewareNotUsed en la función **init** de tu middleware.
- [ ] Implementar el método not_used en tu clase de middleware.
- [ ] Listar el middleware debajo de una entrada de django.middleware.IgnoredMiddleware.
- [ ] Escribir código para eliminar el middleware de la configuración en [app]/**init**.py.

#### P6. ¿Cómo desactivas el escape automático de HTML de Django para parte de una página web?

- [ ] Coloca esa sección entre etiquetas de párrafo que contengan el interruptor autoescape=off.
- [x] Envuelve esa sección entre { percentage mark autoescape off percentage mark} y {percentage mark endautoescape percentage mark} tags.
- [ ] Envuelve esa sección entre {percentage mark autoescapeoff percentage mark} y {percentage mark endautoescapeoff percentage mark} tags.
- [ ] No necesitas hacer nada, el autoescape está desactivado por defecto.

#### P7. ¿Qué paso NO te ayudaría a solucionar el error "django-admin: command not found"?

- [ ] Verifica que la carpeta bin dentro de tu directorio Django esté en la ruta del sistema.
- [ ] Asegúrate de haber activado el entorno virtual que has configurado con Django.
- [ ] Verifica que hayas instalado Django.
- [x] Asegúrate de haber creado un proyecto Django.

#### P8. Cada vez que se guarda un usuario, su quiz_score necesita ser recalculado. ¿Dónde podría ser un lugar ideal para agregar esta lógica?

- [ ] plantilla
- [x] modelo
- [ ] base de datos
- [ ] vista

#### P9. ¿Cuál es la forma correcta de comenzar una clase llamada "Rainbow" en Python?

- [ ] Rainbow {}
- [ ] export Rainbow:
- [x] class Rainbow:
- [ ] def Rainbow:

#### P10. Has heredado un proyecto Django y necesitas ejecutarlo localmente. Viene con un archivo requirements.txt que contiene todas sus dependencias. ¿Qué comando debes usar?

- [ ] django-admin startproject requirements.txt
- [ ] python install -r requirements.txt
- [x] pip install -r requirements.txt
- [ ] pip install Django

#### P11. ¿Qué mejor práctica NO es relevante para las migraciones?

- [x] Para asegurarte de que tus migraciones estén actualizadas, debes ejecutar updatemigrations antes de ejecutar tus pruebas.
- [ ] Debes hacer una copia de seguridad de tu base de datos de producción antes de ejecutar una migración.
- [ ] Tu código de migración debe estar bajo control de versiones.
- [ ] Si un proyecto tiene muchos datos, debes probar contra una copia de staging antes de ejecutar la migración en producción.

#### P12. ¿Qué coincidirá con este patrón de URL? url(r'^\$', views.hello)

- [ ] una cadena que comienza con la letra R
- [x] una cadena vacía en la raíz del servidor
- [ ] una cadena que contiene ^ y $
- [ ] una cadena vacía en cualquier lugar de la URL

#### P13. ¿Cuál es el orden típico de un ciclo de solicitud/respuesta HTTP en Django?

- [x] URL > vista > plantilla
- [ ] formulario > modelo > vista
- [ ] plantilla > vista > modelo
- [ ] URL > plantilla > vista > modelo

#### P14. Las vistas genéricas basadas en clases de Django proporcionan ¿qué clases que implementan tareas comunes de desarrollo web?

- [ ] concretas
- [ ] seguras para hilos
- [x] abstractas
- [ ] dinámicas

#### P15. ¿Qué habilidades necesitas para mantener un conjunto de plantillas de Django?

- [ ] sintaxis de plantillas
- [x] HTML y sintaxis de plantillas
- [ ] Python, HTML y sintaxis de plantillas
- [ ] Python y sintaxis de plantillas

#### P16. ¿Cómo definirías la relación entre una estrella y una constelación en un modelo Django?

- [x] A

```python
class Star(models.Model):
    name = models.CharField(max_length=100)
class Constellation(models.Model):
    stars = models.ManyToManyField(Star)
```

- [ ] B

```python
class Star(models.Model):
    constellation = models.ForeignKey(Constellation, on_delete=models.CASCADE)
class Constellation(models.Model):
    stars = models.ForeignKey(Star, on_delete=models.CASCADE)
```

- [ ] C

```python
class Star(models.Model):
    name = models.CharField(max_length=100)
class Constellation(models.Model):
    stars = models.OneToManyField(Star)
```

- [ ] D

```python
class Star(models.Model):
    constellation = models.ManyToManyField(Constellation)
class Constellation(models.Model):
    name = models.CharField(max_length=100)
```

#### P17. ¿Cuál NO es un paso válido para configurar tu instancia de Django 2.x para servir archivos estáticos como imágenes o CSS?

- [x] En tu archivo urls, agrega un patrón que incluya el nombre de tu directorio estático.
- [ ] Crea un directorio llamado static dentro del directorio de tu aplicación.
- [ ] Crea un directorio con el nombre de la aplicación bajo el directorio static y coloca archivos estáticos dentro.
- [ ] Usa la etiqueta de plantilla {percentage mark load static percentage mark}.

#### P18. ¿Cuál es la forma correcta de hacer que una variable esté disponible para todas tus plantillas?

- [ ] Establecer una variable de sesión.
- [ ] Usar una variable global.
- [x] Agregar un diccionario al contexto de la plantilla.
- [ ] Usar RequestContext.

#### P19. ¿Deberías crear un modelo de usuario personalizado para nuevos proyectos?

- [ ] No. Usar un modelo de usuario personalizado podría romper la interfaz de administración y algunas aplicaciones de terceros.
- [x] Sí. Es más fácil hacer cambios una vez que entra en producción.
- [ ] No. La clase models.User incorporada de Django ha sido probada, no tiene sentido reinventar la rueda.
- [ ] Sí, ya que no hay otra opción.

#### P20. Quieres crear una página que permita editar dos clases conectadas por una clave foránea (por ejemplo, una pregunta y respuesta que residen en tablas separadas). ¿Qué característica de Django puedes usar?

- [ ] acciones
- [ ] admin
- [ ] mezcal
- [x] inlines

#### P21. ¿Por qué se consideran "perezosos" los QuerySets?

- [ ] Los resultados de un QuerySet no están ordenados.
- [x] Los QuerySets no crean ninguna actividad de base de datos hasta que son evaluados.
- [ ] Los QuerySets no cargan objetos en memoria hasta que son necesarios.
- [ ] Usando QuerySets, no puedes ejecutar consultas más complejas.

#### P22. Recibes un `MultiValueDictKeyError` al intentar acceder a un parámetro de solicitud con el siguiente código: request.GET['search_term']. ¿Qué solución NO te ayudará en este escenario?

- [x] Cambiar a usar POST en lugar de GET como método de solicitud.
- [ ] Asegurarte de que el campo de entrada en tu formulario también se llame "search_term".
- [ ] Usar el método GET de MultiValueDict en lugar de acceder al diccionario directamente así: request.GET.get('search_term', '').
- [ ] Verificar si el parámetro search_term está presente en la solicitud antes de intentar acceder a él.

#### P23. ¿Qué función de la clase Form de Django renderizará los campos de un formulario como una serie de etiquetas <p>?

- [ ] show_fields()
- [x] as_p()
- [ ] as_table()
- [ ] fields()

#### P24. Has encontrado un error en Django y quieres enviar un parche. ¿Cuál es el procedimiento correcto?

- [ ] Hacer fork del repositorio de Django en GitHub.
- [ ] Enviar un pull request.
- [x] todas estas respuestas.
- [ ] Ejecutar la suite de pruebas de Django.

#### P25. Django proporciona valores predeterminados sensatos para la configuración. ¿En qué módulo de Python puedes encontrar estas configuraciones?

- [ ] `django.utils.default_settings.py`
- [ ] `django.utils.global_settings.py`
- [ ] `django.conf.default_settings.py`
- [x] `django.conf.global_settings.py`

#### P26. ¿Qué nombre de variable es mejor según las directrices PEP 8?

- [ ] numFingers
- [ ] number-of-Fingers
- [x] number_of_fingers
- [ ] finger_num

#### P27. Un proyecto ha acumulado 500 migraciones. ¿Qué curso de acción seguirías?

- [ ] Fusionar manualmente tus archivos de migración para reducir el número
- [ ] No preocuparse por el número
- [ ] Intentar minimizar el número de migraciones
- [x] Usar squashmigrations para reducir el número

#### P28. ¿Qué te permite hacer un objeto F() al trabajar con modelos?

- [x] realizar operaciones de BD sin recuperar un objeto modelo
- [ ] definir niveles de aislamiento de transacciones de BD
- [ ] usar funciones agregadas más fácilmente
- [ ] construir QuerySets reutilizables

#### P29. ¿Cuál no es un tipo de campo Django para contener enteros?

- [ ] SmallIntegerField
- [x] NegativeIntegerField
- [ ] BigAutoField
- [ ] PositiveIntegerField

#### P30. ¿Cuál mostrará la versión actualmente instalada?

- [ ] print (django.version)
- [ ] import django django.getVersion()
- [x] import django django.get_version()
- [ ] python -c django --version

#### P31. Debes usar el método http `___` para leer datos y `___` para actualizar o crear datos

- [ ] READ; WRITE
- [x] GET; POST
- [ ] POST; GET
- [ ] GET; PATCH

#### P32. ¿Cuándo debes emplear el método POST sobre GET para enviar datos?

- [ ] cuando la eficiencia es importante
- [ ] cuando quieres que los datos se almacenen en caché
- [ ] cuando quieres usar tu navegador para ayudar con la depuración
- [x] cuando los datos en el formulario pueden ser sensibles

#### P33. ¿Cuándo usar el framework de sitios de Django?

- [x] si tu instalación única alimenta más de un sitio
- [ ] si necesitas servir contenido estático y dinámico
- [ ] si quieres que tu aplicación tenga un nombre de dominio completamente calificado
- [ ] si esperas más de 10,000 usuarios

#### P34. ¿Qué infraestructura necesitas:

`title=models.charfield(max_length=100, validators=[validate_spelling])`

- [ ] array inicializado llamado validators
- [x] un archivo validators que contiene una función llamada validate_spelling importada en la parte superior del modelo
- [ ] un archivo validators que contiene una función llamada validate importada en la parte superior del modelo
- [ ] paquete spelling importado en la parte superior del modelo

#### P35. ¿Qué decorador se usa para requerir que una vista acepte solo los métodos get y head?

- [x] require_safe()
- [ ] require_put()
- [ ] require_post()
- [ ] require_get()

#### P36. ¿Cómo definirías la relación entre un libro y un autor - el libro tiene solo un autor?

```python
class Author (models.model):
    book=models.foreignkey(Book,on_delete=models.cascade)
class Book(models.model):
    name=models.charfield(max_length=100)
```

- [x] A

```python
class Author (models.model):
    name=models.charfield(max_length=100)
class Book(models.model):
    author=models.foreignkey(Author,on_delete=models.cascade)
```

- [ ] B

```python
class Author (models.model):
    name=models.charfield(max_length=100)
class Book(models.model):
    author=models.foreignkey(Author)
```

- [ ] C

```python
class Author (models.model):
    name=models.charfield(max_length=100)
class Book(models.model):
    author=models.foreignkey(Author,on_delete=models.cascade)
```

- [ ] D

```python
class Author (models.model):
    name=models.charfield(max_length=100)
class Book(models.model):
    author=Author.name
```

#### P37. ¿Qué es un callable que toma un valor y genera un error si el valor falla?

- [x] validador
- [ ] desodorante
- [ ] mediador
- [ ] expresión regular

#### P38. Para proteger un endpoint de API, haciéndolo accesible solo para usuarios registrados, puedes reemplazar el valor rest_framework.permissions.allowAny en la sección default_permissions de tu settings.py por

- [ ] rest_framework.permissions.IsAdminUser
- [x] rest_framework.permissions.IsAuthenticated
- [ ] rest_framework.permissions.IsAuthorized
- [ ] rest_framework.permissions.IsRegistered

#### P39. ¿Qué comando usarías para aplicar una migración?

- [ ] makemigration
- [ ] update_db
- [ ] applymigration
- [x] migrate

#### P40. ¿Qué tipo de clase permite que QuerySets e instancias de modelo se conviertan en tipos de datos nativos de Python para usar en APIs?

- [ ] objectwriters
- [x] serializers
- [ ] picklers
- [ ] viewsets

#### P41. ¿Cómo debe terminar el código?

```python
{ percentage if spark >= 50 percentage }
Mucho chispa
{percentage elif spark == 42 percentage}
```

- [ ] { percentage else percentage}
- [x] {percentage endif percentage}
- [ ] No se necesita nada
- [ ] {percentage end percentage}

#### P42. ¿Qué bloque de código creará un serializador?

```python
from rest_framework import serializers
from .models import Planet
```

- [x] A

```python
class PlanetSerializer(serializers.ModelSerializer):
    class Meta:
        model=Planet
        fields=('name','position', 'mass', 'rings')
```

- [ ] B

```python
from rest_framework import serializers
from .models import Planet
class PlanetSerializer():
    class Meta:
        fields=('name','position', 'mass', 'rings')
        model=Planet
```

- [ ] C

```python
from django.db import serializers
from .models import Planet
class PlanetSerializer(serializers.ModelSerializer):
    fields=('name','position', 'mass', 'rings')
    model=Sandwich
```

- [ ] D

```python
from django.db import serializers
from .models import Planet
class PlanetSerializer(serializers.ModelSerializer):
    class Meta:
        fields=('name')
        model=Planet
```

#### P43. ¿Qué clase te permite crear automáticamente una clase Serializer con campos y validadores que corresponden a los campos de tu modelo?

- [x] ModelSerializer
- [ ] Model
- [ ] DataSerializer
- [ ] ModelToSerializer

#### P44. ¿Qué comando para acceder a la herramienta de administración integrada por primera vez?

- [ ] django-admin setup
- [ ] django-admin runserver
- [ ] python manage.py createuser
- [x] python manage.py createsuperuser

#### P45. Los entornos virtuales son para gestionar dependencias. ¿Qué granularidad funciona mejor?

- [x] debes configurar un nuevo virtualenv para cada proyecto Django
- [ ] No deben usarse
- [ ] Usa el mismo venv para todo tu trabajo de Django
- [ ] Usa un nuevo venv para cada aplicación Django

#### P46. ¿Qué ejecuta varios comandos de Django como ejecutar un servidor web o crear una aplicación?

- [ ] migrate.py
- [ ] wsgi.py
- [x] manage.py
- [ ] runserver

#### P47. ¿Qué sugieren las mejores prácticas de Django que debería ser "gordo"?

- [x] modelos
- [ ] controladores
- [ ] programadores
- [ ] clientes

#### P48. ¿Cuál no es parte de la filosofía de diseño de Django?

- [ ] Acoplamiento débil
- [ ] Menos código
- [ ] Desarrollo rápido
- [x] Implícito sobre explícito

#### P49. ¿Cuál es el resultado de este código de plantilla?

{% raw %}{{"live long and prosper"|truncatewords:3}}{% endraw %}

- [x] live long and ...
- [ ] live long and
- [ ] un error de compilación
- [ ] liv

#### P50. ¿Cuándo carga este código datos en memoria?

```
1 sandwiches = Sandwich.objects.filter(is_vegan=True)
2 for sandwich in sandwiches:
3   print(sandwich.name + " - " + sandwich.spice_level)
```

- [ ] línea 1
- [ ] Depende de cuántos resultados devuelva la consulta.
- [ ] Depende del caché.
- [x] línea 2

#### P51. Estás construyendo una aplicación web usando un frontend React y un backend Django. ¿Para qué necesitarás provisionar?

- [ ] un servidor web NGINX
- [ ] una base de datos NoSQL
- [ ] un disco duro más grande
- [x] middleware CORS

#### P52. Para exponer un modelo existente a través de un endpoint de API, ¿qué necesitas implementar?

- [ ] una solicitud HTTP
- [ ] un objeto JSON
- [ ] una consulta
- [x] un serializador

#### P53. ¿Cómo evitarías que Django realice operaciones de creación o eliminación de tablas de base de datos a través de migraciones para un modelo en particular?

- [ ] Ejecutar el comando `migrate` con `--exclude=[model_name]`.
- [ ] Mover la definición del modelo de `models.py` a su propio archivo.
- [x] Establecer `managed=False` dentro del modelo.
- [ ] No ejecutar el comando `migrate`.

#### P54. ¿Qué método puedes usar para verificar si los datos del formulario han cambiado al usar una instancia de formulario?

- [x] has_changed()
- [ ] its_changed()
- [ ] has_updated()
- [ ] Ninguna de estas

#### P55. ¿Qué es WSGI?

- [ ] un servidor
- [x] una especificación de interfaz
- [ ] un módulo de Python
- [ ] un framework

Enlace de referencia: https://wsgi.tutorial.codepoint.net/intro

#### P56. ¿Qué vista genérica debe usarse para mostrar los títulos de todas las canciones de Django Reinhardt?

- [ ] DetailView
- [ ] TittleView
- [ ] SongView
- [x] ListView

#### P57. ¿Qué declaración es más precisa respecto a usar la base de datos SQLite predeterminada en tu máquina local/desarrollo pero Postgres en producción?

- [ ] Hay menos posibilidades de introducir errores ya que SQLite ya funciona desde el principio
- [ ] Está bien, solo necesitas mantener ambas instancias sincronizadas
- [x] Es una mala idea y podría llevar a problemas más adelante
- [ ] Es la forma más eficiente de construir un proyecto

#### P58. ¿Por qué querrías escribir un Manager de modelo personalizado?

- [ ] para realizar consultas de base de datos
- [ ] para configurar una base de datos para pruebas
- [x] para modificar el QuerySet inicial que devuelve el Manager
- [ ] para filtrar los resultados que devuelve una consulta de base de datos

#### P59. En Django, ¿qué se usa para personalizar los datos que se envían a las plantillas?

- [ ] modelos
- [x] vistas
- [ ] formularios
- [ ] serializadores

#### P60. Para completar el condicional, ¿con qué debe terminar este bloque de código?

```shell
% if sparles >= 50 %
  ¡Muchos brillos!
% elif sparkles == 42 %
  ¡La respuesta a la vida, el universo y todo!
```

- [x] `% endif %`
- [ ] No se necesita nada más.
- [ ] `% end%`
- [ ] `% else %`

#### P61. ¿Cuándo debes emplear el método POST sobre el método GET para enviar datos de un formulario?

- [x] cuando los datos en el formulario pueden ser sensibles
- [ ] cuando quieres que los datos se almacenen en caché
- [ ] cuando quieres usar tu navegador para ayudar con la depuración
- [ ] cuando la eficiencia es importante

#### P62. ¿Qué es un callable que toma un valor y genera un error si el valor no cumple con algunos criterios?

- [ ] mediador
- [x] validador
- [ ] expresión regular
- [ ] desodorante

#### P63. Estás subiendo un archivo a Django desde un formulario y quieres guardar el archivo recibido como un campo en un objeto modelo. Simplemente puedes asignar el objeto archivo de ****_ a un campo de tipo _**** en el modelo.

- [ ] request.META; FileField
- [ ] request.FILES; BLOBField
- [x] request.FILES; FileField
- [ ] request.META.Files; CLOBField

#### P64. ¿Qué módulo de Python se podría usar para almacenar el estado actual de un modelo Django en un archivo?

- [x] pickle
- [ ] struct
- [ ] marshal
- [ ] serialize

#### P65. Para agregar una nueva aplicación a un proyecto Django existente, debes editar la sección **_\_\_ del archivo _**.

- [ ] ALLOWED_HOSTS; settings.py
- [ ] APPS; manage.py
- [x] INSTALLED_APPS; settings.py
- [ ] TEMPLATES; urls.py

#### P66. ¿Cuál no es un paquete de terceros comúnmente usado para autenticación?

- [ ] django-guardian
- [ ] django-rest-auth
- [ ] authtoken
- [x] django-rest-framework-jwt

#### P67. ¿Qué función en el paquete django.urls puede ayudarte a evitar codificar URLs generando una URL dado el nombre de una vista?

- [ ] get_script_prefix()
- [ ] redirect()
- [x] reverse()
- [ ] resolve()

#### P68. ¿Cuál es un método de solicitud HTTP ficticio?

- [ ] POST
- [ ] PUT
- [x] PAUSE
- [ ] PATCH

#### P69. ¿Qué función auxiliar NO se proporciona como parte del paquete django.shortcuts?

- [x] render_to_request()
- [ ] render()
- [ ] redirect()
- [ ] get_object_or_404()

[Referencia](https://docs.djangoproject.com/en/4.0/topics/http/shortcuts/#:~:text=The%20package%20django.,controlled%20coupling%20for%20convenience's%20sake)

#### P70. ¿Cuál es un lugar no estándar para almacenar plantillas?

- [x] en el nivel raíz de un proyecto
- [ ] dentro de la aplicación
- [ ] en la base de datos
- [ ] en Github

#### P71. Si omites el 8080 del comando python manage.py runserver 8080, ¿qué puerto usaría Django por defecto?

- [ ] 8080
- [ ] 80
- [x] 8000
- [ ] Fallaría al iniciar

#### P72. ¿Qué declaración sobre las aplicaciones Django es falsa?

- [x] Una aplicación Django es el contenedor de nivel superior para una aplicación web impulsada por Django.
- [ ] Las aplicaciones Django son pequeñas bibliotecas diseñadas para representar un solo aspecto de un proyecto.
- [ ] Cada aplicación Django debe hacer una cosa, y solo una cosa.
- [ ] Un proyecto Django está compuesto por muchas aplicaciones.

#### P73. ¿Qué caracteres son ilegales en los nombres de variables de plantilla?

- [ ] guiones bajos.
- [ ] letras mayúsculas.
- [x] signos de puntuación.
- [ ] números.

[Referencia](https://docs.djangoproject.com/en/4.1/ref/templates/language/#:~:text=Variable%20names%20consist%20of%20any,may%20not%20be%20a%20number.)

#### P74. ¿Cuál no es una etiqueta de cierre de plantilla válida?

- [ ] `% endautoescape %`
- [x] `% endifempty %`
- [ ] `% endcomment %`
- [ ] `% endfilter %`

#### P75. ¿Cuándo necesitarías usar la función de utilidad reverse_lazy en lugar de reverse?

- [ ] cuando quieres proporcionar una URL inversa como valor predeterminado para un parámetro en la firma de una función
- [x] todas estas respuestas
- [ ] cuando quieres proporcionar una URL inversa como el atributo url de una vista genérica basada en clases
- [ ] cuando quieres proporcionar una URL a un decorador, como el argumento login_url para el decorador permission_required()

#### P76. ¿Cuál es el propósito del archivo \_\_init\_\_.py?

- [ ] extender el conjunto de módulos encontrados en un paquete
- [ ] permitir que módulos compilados de diferentes versiones de Python coexistan
- [ ] inicializar la configuración del proyecto
- [x] declarar el contenido del directorio como un módulo de Python

[Referencia](<https://docs.djangoproject.com/en/4.1/ref/urlresolvers/#:~:text=reverse_lazy()&text=It%20is%20useful%20for%20when,a%20generic%20class%2Dbased%20view>)

#### P77. ¿Qué paquete de Python se puede usar para editar números en forma más legible como "1200000" a "1.2 millones"?

- [ ] black
- [ ] puffer
- [ ] pitch
- [x] humanize

#### P78. ¿Dónde encontrarías el archivo settings.py?

- [x] \[projectname\]/settings.py
- [ ] \[projectname\]/\[projectname\]/settings.py
- [ ] \[PYTHON_ROOT\]/settings.py
- [ ] \[DJANGO_ROOT]/settings.py

#### P79. ¿Qué escribirías para definir la relación entre un libro y un autor, asumiendo que un libro tiene solo un autor, en un modelo Django?

- [x] A

```python
class Author (models.Model):
  name = models.CharField(max_length=100)
class Book(models.Model):
  author = models.ForeignKey(Author, on_delete=models.CASCADE)
```

- [ ] B

```python
class Author (models.Model):
  name = models.CharField(max length=100)
class Book(models.Model):
  author = models.ForeignKey(Author)
```

- [ ] C

```python
class Author (models.Model):
  name = models.CharField(max_length=100)
class Book(models.Author):
  author = Author.name
```

- [ ] D

```python
class Author (models.Model):
  book = models.ForeignKey(Book, on_delete=models.CASCADE)
class Book(models.Model):
  name = models.CharField(max length=100)
```

#### P80. ¿Qué método puedes usar para verificar si los datos del formulario han cambiado al usar una instancia de Form?

- [ ] changed_data()
- [x] has_changed()
- [ ] has_updated()
- [ ] is_modified()

#### P81. ¿Qué declaración es más precisa respecto a usar la base de datos SQLite predeterminada en tu máquina local/desarrollo pero Postgres en producción?

- [ ] Es la forma más eficiente de construir un proyecto
- [ ] Hay menos posibilidades de introducir errores ya que SQLite ya funciona desde el principio
- [x] Es una mala idea y podría llevar a problemas más adelante
- [ ] Está bien, solo necesitas mantener ambas instancias sincronizadas

#### P82. ¿Cómo maneja Django el enrutamiento de URL?

- [ ] usando clases
- [ ] usando funciones
- [x] usando expresiones regulares
- [ ] usando ruta fija

#### P83. ¿Cuál es el propósito del middleware de Django?

- [ ] Para definir el esquema de la base de datos
- [ ] Para gestionar el enrutamiento de URL
- [x] Para manejar solicitudes y respuestas HTTP globalmente
- [ ] Para crear interfaces de usuario

[Referencia](https://medium.com/scalereal/everything-you-need-to-know-about-middleware-in-django-2a3bd3853cd6)

#### P84. ¿Cuál de las siguientes es verdadera sobre el ORM (Mapeo Objeto-Relacional) de Django?

- [ ] Se usa para definir el enrutamiento de URL en una aplicación Django.
- [x] Te permite consultar la base de datos usando código Python.
- [ ] Se usa para definir la estructura de las plantillas HTML.
- [ ] Es responsable de gestionar la autenticación de usuarios.

#### P85. ¿Cuál de las siguientes es verdadera sobre el campo "many-to-many" de Django en un modelo?

- [ ] Se usa para definir una relación uno a uno entre dos modelos.
- [ ] Crea una relación de clave foránea entre dos modelos.
- [x] Permite que múltiples objetos estén asociados entre sí.
- [ ] Aplica restricciones únicas en un campo.

#### P86. Las vistas genéricas basadas en clases de Django proporcionan ¿qué clases que implementan tareas comunes de desarrollo web?

- [ ] concretas
- [ ] seguras para hilos
- [x] abstractas
- [ ] dinámicas

#### P87. ¿Qué habilidades necesitas para mantener un conjunto de plantillas de Django?

- [ ] sintaxis de plantillas
- [x] HTML y sintaxis de plantillas
- [ ] Python, HTML y sintaxis de plantillas
- [ ] Python y sintaxis de plantillas

#### P88. ¿Cuál es un lugar no estándar para almacenar plantillas?

- [x] en el nivel raíz de un proyecto
- [ ] dentro de la aplicación
- [ ] en la base de datos
- [ ] en Github

#### P89. Si omites el 8080 del comando python manage.py runserver 8080, ¿qué puerto usaría Django por defecto?

- [ ] 8080
- [ ] 80
- [x] 8000
- [ ] Fallaría al iniciar

#### P90. ¿Cuál es el propósito del ORM (Mapeo Objeto-Relacional) de Django?

- [ ] Para definir el enrutamiento de URL en una aplicación Django.
- [ ] Para manejar solicitudes y respuestas HTTP globalmente.
- [x] Para mapear objetos Python a tablas de base de datos y simplificar las operaciones de base de datos.
- [ ] Para crear interfaces de usuario.

#### P91. En Django, ¿a qué se refiere el término "migración"?

- [ ] Un cambio en la configuración de enrutamiento de URL.
- [x] El proceso de propagar los cambios que haces a tus modelos (agregar un campo, eliminar un modelo, etc.) en el esquema de tu base de datos.
- [ ] Una forma de definir middleware personalizado.
- [ ] El proceso de crear plantillas HTML para tu aplicación.

#### P92. ¿Cuál es el propósito del "contexto" de Django en el contexto de renderizar plantillas?

- [x] Para pasar datos de tus vistas a tus plantillas para que los datos puedan renderizarse dinámicamente.
- [ ] Para definir patrones de URL para tu aplicación.
- [ ] Para gestionar solicitudes y respuestas HTTP.
- [ ] Para crear interfaces de usuario.

#### P93. ¿Qué representa la clase `QuerySet` de Django?

- [ ] Una clase de Python usada para definir el enrutamiento de URL en Django.
- [ ] Una clase para gestionar solicitudes y respuestas HTTP.
- [x] Una consulta de base de datos hecha por Django, representada en Python.
- [ ] Una clase para definir plantillas HTML.

#### P94. En Django, ¿cuál es el propósito del comando de gestión "collectstatic"?

- [ ] Para recopilar datos de usuario para análisis.
- [ ] Para recopilar registros de base de datos de múltiples fuentes.
- [x] Para recopilar todos los archivos estáticos (CSS, JavaScript, imágenes) de cada una de tus aplicaciones en una sola ubicación.
- [ ] Para recopilar registros para propósitos de depuración.

#### P95. ¿Para qué se usa el sitio de administración de Django?

- [ ] Para gestionar la autenticación de usuarios.
- [ ] Para definir el enrutamiento de URL para aplicaciones Django.
- [x] Para proporcionar una interfaz de administración generada automáticamente para tus modelos.
- [ ] Para escribir y ejecutar consultas de base de datos.

#### P96. ¿A qué se refiere el "middleware" de Django?

- [ ] Una forma de crear interfaces de usuario.
- [ ] Una consulta de base de datos en Django.
- [x] Una forma de procesar solicitudes y respuestas HTTP globalmente antes de que lleguen a la vista o después de que salgan de la vista.
- [ ] Una forma de configurar el enrutamiento de URL en Django.

#### P97. ¿Cuál es el propósito principal de los "archivos de migración" de Django?

- [x] Para definir y almacenar cambios en el esquema de la base de datos a lo largo del tiempo.
- [ ] Para gestionar archivos estáticos como CSS y JavaScript.
- [ ] Para configurar patrones de URL.
- [ ] Para crear plantillas HTML.

#### P98. ¿Qué sistema de autenticación proporciona Django de forma predeterminada?

- [ ] OAuth 2.0
- [x] Autenticación de usuario con modelos de usuario y vistas integrados.
- [ ] JWT (JSON Web Tokens)
- [ ] SAML (Security Assertion Markup Language)

#### P99. En Django, ¿a qué se refiere el patrón arquitectónico "Model-View-Controller" (MVC)?

- [ ] Un patrón para definir el enrutamiento de URL.
- [ ] Un patrón para crear plantillas HTML.
- [x] Un patrón que divide la aplicación en tres componentes interconectados: Modelo, Vista y Controlador (Django a menudo se refiere a él como MTV, Model-View-Template).
- [ ] Un patrón para la autenticación de usuarios.

#### P100. ¿Cuál es el propósito de las "plantillas" de Django?

- [ ] Para definir el esquema de la base de datos y las relaciones del modelo.
- [x] Para definir la estructura y el diseño de las páginas HTML que se servirán al usuario.
- [ ] Para configurar patrones de URL para tu aplicación.
- [ ] Para almacenar y servir archivos estáticos como imágenes y JavaScript.

#### P101. ¿Qué método del ORM de Django se usa para recuperar un solo objeto que coincida con los parámetros de búsqueda dados?

- [ ] `get_object_or_404()`
- [x] `get()`
- [ ] `filter()`
- [ ] `values()`

#### P102. ¿Cuál es el propósito del método `__str__()` en un modelo Django?

- [ ] Para definir el ordenamiento predeterminado para instancias del modelo
- [x] Para proporcionar una representación de cadena legible para humanos de la instancia del modelo
- [ ] Para definir el campo predeterminado a usar para búsquedas
- [ ] Para definir el campo de visualización predeterminado en la interfaz de administración de Django

#### P103. ¿Qué método del ORM de Django se usa para recuperar una lista de objetos que coincidan con los parámetros de búsqueda dados?

- [ ] `get()`
- [ ] `get_object_or_404()`
- [x] `filter()`
- [ ] `values()`

#### P104. ¿Cuál es el propósito del parámetro `related_name` en el campo `ForeignKey` de un modelo Django?

- [ ] Para definir el nombre de la relación inversa en el modelo relacionado
- [ ] Para definir el ordenamiento predeterminado para los objetos relacionados
- [x] Para definir el nombre del atributo en el modelo relacionado que accede al conjunto de objetos relacionados
- [ ] Para definir el nombre del atributo en el modelo actual que accede al objeto relacionado

#### P105. ¿Qué método del ORM de Django se usa para recuperar una lista de valores distintos para los campos especificados?

- [ ] `get()`
- [ ] `get_object_or_404()`
- [ ] `filter()`
- [x] `values()`

#### P106. ¿Cuál es el propósito del parámetro `unique` en un campo de modelo Django?

- [ ] Para definir el ordenamiento predeterminado para el campo
- [ ] Para definir el valor predeterminado para el campo
- [x] Para asegurar que el valor del campo sea único en todas las instancias del modelo
- [ ] Para definir la longitud máxima del campo

#### P107. ¿Qué método del ORM de Django se usa para recuperar un solo objeto que coincida con los parámetros de búsqueda dados o generar una excepción `Http404` si no se encuentra ningún objeto?

- [x] `get_object_or_404()`
- [ ] `get()`
- [ ] `filter()`
- [ ] `values()`

#### P108. ¿Cuál es el propósito del parámetro `on_delete` en el campo `ForeignKey` de un modelo Django?

- [ ] Para definir el valor predeterminado para el campo
- [ ] Para definir la longitud máxima del campo
- [x] Para especificar el comportamiento cuando se elimina el objeto referenciado
- [ ] Para definir el nombre de la relación inversa en el modelo relacionado

#### P109. ¿Qué método del ORM de Django se usa para realizar operaciones de agregación (por ejemplo, `sum()`, `avg()`, `count()`) en un QuerySet?

- [ ] `get()`
- [ ] `get_object_or_404()`
- [ ] `filter()`
- [x] `aggregate()`

#### P110. ¿Cuál es el propósito del parámetro `related_query_name` en el campo `ForeignKey` de un modelo Django?

- [ ] Para definir el nombre de la relación inversa en el modelo relacionado
- [x] Para definir el nombre del atributo en el modelo relacionado que accede al conjunto de objetos relacionados
- [ ] Para definir el ordenamiento predeterminado para los objetos relacionados
- [ ] Para definir el nombre del atributo en el modelo actual que accede al objeto relacionado

#### P111. ¿Qué método del ORM de Django se usa para crear un nuevo objeto y guardarlo en la base de datos?

- [ ] `get()`
- [ ] `get_object_or_404()`
- [x] `save()`
- [ ] `create()`

#### P112. ¿Cuál es el propósito del parámetro `default` en un campo de modelo Django?

- [ ] Para definir la longitud máxima del campo
- [x] Para especificar el valor predeterminado para el campo
- [ ] Para definir el nombre de la relación inversa en el modelo relacionado
- [ ] Para asegurar que el valor del campo sea único en todas las instancias del modelo

#### P113. ¿Qué método del ORM de Django se usa para recuperar una lista de objetos que coincidan con los parámetros de búsqueda dados y devolverlos como una lista de diccionarios?

- [ ] `get()`
- [ ] `get_object_or_404()`
- [ ] `filter()`
- [x] `values()`

#### P114. ¿Cuál es el propósito del parámetro `null` en un campo de modelo Django?

- [ ] Para definir la longitud máxima del campo
- [ ] Para asegurar que el valor del campo sea único en todas las instancias del modelo
- [x] Para especificar si el campo puede tener un valor nulo
- [ ] Para definir el valor predeterminado para el campo

#### P115. ¿Qué método del ORM de Django se usa para recuperar una lista de objetos que coincidan con los parámetros de búsqueda dados y ordenarlos por uno o más campos?

- [ ] `get()`
- [ ] `get_object_or_404()`
- [x] `order_by()`
- [ ] `values()`

#### P116. ¿Cuál es el propósito del parámetro `verbose_name` en un campo de modelo Django?

- [ ] Para definir el ordenamiento predeterminado para el campo
- [ ] Para definir la longitud máxima del campo
- [x] Para proporcionar un nombre legible para humanos para el campo
- [ ] Para asegurar que el valor del campo sea único en todas las instancias del modelo

#### P117. ¿Qué método del ORM de Django se usa para recuperar una lista de objetos que coincidan con los parámetros de búsqueda dados y excluir ciertos objetos?

- [ ] `get()`
- [ ] `get_object_or_404()`
- [x] `exclude()`
- [ ] `values()`

#### P118. ¿Cuál es el propósito del parámetro `on_delete` en el `OneToOneField` de un modelo Django?

- [ ] Para definir el ordenamiento predeterminado para los objetos relacionados
- [ ] Para definir el nombre de la relación inversa en el modelo relacionado
- [x] Para especificar el comportamiento cuando se elimina el objeto referenciado
- [ ] Para definir el nombre del atributo en el modelo relacionado que accede al conjunto de objetos relacionados

#### P119. ¿Qué método del ORM de Django se usa para recuperar una lista de objetos que coincidan con los parámetros de búsqueda dados y devolverlos como una lista de tuplas?

- [ ] `get()`
- [ ] `get_object_or_404()`
- [ ] `filter()`
- [x] `values_list()`

#### P120. ¿Cuál es el propósito del parámetro `unique_together` en una clase Meta de modelo Django?

- [ ] Para definir el ordenamiento predeterminado para el modelo
- [ ] Para definir la longitud máxima de los campos
- [x] Para asegurar que la combinación de los campos especificados sea única en todas las instancias del modelo
- [ ] Para definir el nombre de la relación inversa en el modelo relacionado

#### P121. ¿Qué método del ORM de Django se usa para recuperar una lista de objetos que coincidan con los parámetros de búsqueda dados y devolverlos como una lista de instancias de modelo?

- [x] `all()`
- [ ] `get()`
- [ ] `get_object_or_404()`
- [ ] `values()`

#### P122. ¿Cuál es el propósito del parámetro `blank` en un campo de modelo Django?

- [ ] Para definir el valor predeterminado para el campo
- [x] Para especificar si el campo puede dejarse en blanco
- [ ] Para asegurar que el valor del campo sea único en todas las instancias del modelo
- [ ] Para definir la longitud máxima del campo

#### P123. ¿Qué método del ORM de Django se usa para recuperar una lista de objetos que coincidan con los parámetros de búsqueda dados y devolverlos como una lista de diccionarios con los campos especificados?

- [ ] `get()`
- [ ] `get_object_or_404()`
- [ ] `filter()`
- [x] `values()`

#### P124. ¿Cuál es el propósito del parámetro `default` en el campo `ForeignKey` de un modelo Django?

- [ ] Para definir el nombre de la relación inversa en el modelo relacionado
- [x] Para especificar el valor predeterminado para el campo
- [ ] Para asegurar que el valor del campo sea único en todas las instancias del modelo
- [ ] Para definir la longitud máxima del campo

#### P125. ¿Qué método del ORM de Django se usa para recuperar una lista de objetos que coincidan con los parámetros de búsqueda dados y devolverlos como una lista de tuplas con los campos especificados?

- [ ] `get()`
- [ ] `get_object_or_404()`
- [ ] `filter()`
- [x] `values_list()`

#### P126. ¿Cuál es el propósito del parámetro `editable` en un campo de modelo Django?

- [ ] Para definir el ordenamiento predeterminado para el campo
- [ ] Para asegurar que el valor del campo sea único en todas las instancias del modelo
- [x] Para especificar si el campo debe mostrarse en interfaces de administración para edición
- [ ] Para definir la longitud máxima del campo

#### P127. ¿Qué método del ORM de Django se usa para recuperar una lista de objetos que coincidan con los parámetros de búsqueda dados y devolverlos como una lista de instancias de modelo con los campos especificados?

- [ ] `get()`
- [ ] `get_object_or_404()`
- [x] `values()`
- [ ] `values_list()`

#### P128. ¿Cuál es el propósito del parámetro `choices` en un campo de modelo Django?

- [ ] Para definir el ordenamiento predeterminado para el campo
- [x] Para especificar un conjunto de opciones para el campo
- [ ] Para asegurar que el valor del campo sea único en todas las instancias del modelo
- [ ] Para definir la longitud máxima del campo

#### P129. ¿Qué método del ORM de Django se usa para recuperar una lista de objetos que coincidan con los parámetros de búsqueda dados y devolverlos como una lista de tuplas con los campos especificados en un orden específico?

- [ ] `get()`
- [ ] `get_object_or_404()`
- [ ] `values()`
- [x] `values_list()`

#### P130. ¿Cuál es el propósito del parámetro `db_index` en un campo de modelo Django?

- [ ] Para definir el ordenamiento predeterminado para el campo
- [x] Para crear un índice de base de datos para el campo
- [ ] Para asegurar que el valor del campo sea único en todas las instancias del modelo
- [ ] Para definir la longitud máxima del campo

#### P131. ¿Qué método del ORM de Django se usa para recuperar una lista de objetos que coincidan con los parámetros de búsqueda dados y devolverlos como una lista de instancias de modelo con los campos especificados?

- [ ] `get()`
- [ ] `get_object_or_404()`
- [x] `values()`
- [ ] `values_list()`

#### P132. ¿Cuál es el propósito de los parámetros `unique_for_date`, `unique_for_month` y `unique_for_year` en un campo de modelo Django?

- [ ] Para definir el ordenamiento predeterminado para el campo
- [x] Para asegurar que el valor del campo sea único para la fecha, mes o año especificado
- [ ] Para crear un índice de base de datos para el campo
- [ ] Para definir la longitud máxima del campo

#### P133. ¿Qué método del ORM de Django se usa para recuperar una lista de objetos que coincidan con los parámetros de búsqueda dados y devolverlos como una lista de tuplas con los campos especificados en un orden específico?

- [ ] `get()`
- [ ] `get_object_or_404()`
- [ ] `values()`
- [x] `values_list()`

#### P134. ¿Cuál es el propósito del parámetro `help_text` en un campo de modelo Django?

- [ ] Para definir el ordenamiento predeterminado para el campo
- [x] Para proporcionar información adicional sobre el campo, que se muestra en las interfaces de administración
- [ ] Para asegurar que el valor del campo sea único en todas las instancias del modelo
- [ ] Para definir la longitud máxima del campo

#### P135. ¿Qué método del ORM de Django se usa para recuperar una lista de objetos que coincidan con los parámetros de búsqueda dados y devolverlos como una lista de instancias de modelo con los campos especificados?

- [ ] `get()`
- [ ] `get_object_or_404()`
- [x] `values()`
- [ ] `values_list()`

#### P136. ¿Cuál es el propósito del parámetro `verbose_name_plural` en una clase Meta de modelo Django?

- [ ] Para definir el ordenamiento predeterminado para el modelo
- [ ] Para crear un índice de base de datos para el modelo
- [x] Para proporcionar un nombre plural legible para humanos para el modelo
- [ ] Para asegurar que la combinación de los campos especificados sea única en todas las instancias del modelo

#### P137. ¿Qué método del ORM de Django se usa para recuperar una lista de objetos que coincidan con los parámetros de búsqueda dados y devolverlos como una lista de tuplas con los campos especificados en un orden específico?

- [ ] `get()`
- [ ] `get_object_or_404()`
- [ ] `values()`
- [x] `values_list()`

#### P138. ¿Cuál es el propósito de los parámetros `auto_now` y `auto_now_add` en un `DateField` o `DateTimeField` de modelo Django?

- [ ] Para definir el ordenamiento predeterminado para el campo
- [x] Para establecer automáticamente el campo a la fecha/hora actual cuando se guarda o crea el objeto
- [ ] Para asegurar que el valor del campo sea único en todas las instancias del modelo
- [ ] Para definir la longitud máxima del campo

#### P139. ¿Qué método del ORM de Django se usa para recuperar una lista de objetos que coincidan con los parámetros de búsqueda dados y devolverlos como una lista de instancias de modelo con los campos especificados?

- [ ] `get()`
- [ ] `get_object_or_404()`
- [x] `values()`
- [ ] `values_list()`

#### P140. ¿Cuál es el propósito del parámetro `related_name` en el `ManyToManyField` de un modelo Django?

- [ ] Para definir el ordenamiento predeterminado para los objetos relacionados
- [x] Para definir el nombre del atributo en el modelo relacionado que accede al conjunto de objetos relacionados
- [ ] Para asegurar que la combinación de los campos especificados sea única en todas las instancias del modelo
- [ ] Para definir la longitud máxima del campo

#### P141. ¿Qué método del ORM de Django se usa para recuperar una lista de objetos que coincidan con los parámetros de búsqueda dados y devolverlos como una lista de tuplas con los campos especificados en un orden específico?

- [ ] `get()`
- [ ] `get_object_or_404()`
- [ ] `values()`
- [x] `values_list()`

#### P142. ¿Cuál es el propósito del parámetro `on_delete` en el `ManyToManyField` de un modelo Django?

- [ ] Para definir el ordenamiento predeterminado para los objetos relacionados
- [ ] Para definir el nombre del atributo en el modelo relacionado que accede al conjunto de objetos relacionados
- [x] Para especificar el comportamiento cuando se elimina el objeto referenciado
- [ ] Para definir la longitud máxima del campo

#### P143. ¿Qué método del ORM de Django se usa para recuperar una lista de objetos que coincidan con los parámetros de búsqueda dados y devolverlos como una lista de instancias de modelo con los campos especificados?

- [ ] `get()`
- [ ] `get_object_or_404()`
- [x] `values()`
- [ ] `values_list()`

#### P144. ¿Cuál es el propósito del parámetro `default` en el `ManyToManyField` de un modelo Django?

- [ ] Para definir el ordenamiento predeterminado para los objetos relacionados
- [x] Para especificar el valor predeterminado para el campo
- [ ] Para asegurar que la combinación de los campos especificados sea única en todas las instancias del modelo
- [ ] Para definir la longitud máxima del campo

#### P145. ¿Qué método del ORM de Django se usa para recuperar una lista de objetos que coincidan con los parámetros de búsqueda dados y devolverlos como una lista de tuplas con los campos especificados en un orden específico?

- [ ] `get()`
- [ ] `get_object_or_404()`
- [ ] `values()`
- [x] `values_list()`

#### P146. ¿Cuál es el propósito del parámetro `null` en el campo `ForeignKey` de un modelo Django?

- [ ] Para definir el ordenamiento predeterminado para los objetos relacionados
- [x] Para especificar si el campo puede tener un valor nulo
- [ ] Para asegurar que la combinación de los campos especificados sea única en todas las instancias del modelo
- [ ] Para definir la longitud máxima del campo

#### P147. ¿Qué método del ORM de Django se usa para recuperar una lista de objetos que coincidan con los parámetros de búsqueda dados y devolverlos como una lista de instancias de modelo con los campos especificados?

- [ ] `get()`
- [ ] `get_object_or_404()`
- [x] `values()`
- [ ] `values_list()`

#### P148. ¿Cuál es el propósito del parámetro `db_column` en un campo de modelo Django?

- [ ] Para definir el ordenamiento predeterminado para el campo
- [x] Para especificar el nombre de la columna de base de datos para el campo
- [ ] Para asegurar que el valor del campo sea único en todas las instancias del modelo
- [ ] Para definir la longitud máxima del campo

#### P149. ¿Qué método del ORM de Django se usa para recuperar una lista de objetos que coincidan con los parámetros de búsqueda dados y devolverlos como una lista de tuplas con los campos especificados en un orden específico?

- [ ] `get()`
- [ ] `get_object_or_404()`
- [ ] `values()`
- [x] `values_list()`

#### P150. ¿Cuál es el propósito del parámetro `db_table` en una clase Meta de modelo Django?

- [ ] Para definir el ordenamiento predeterminado para el modelo
- [x] Para especificar el nombre de la tabla de base de datos para el modelo

#### P151. ¿Qué campo de formulario Django se usa para validar que la entrada de un usuario es una dirección de correo electrónico válida?

- [ ] EmailField
- [x] EmailField
- [ ] CharField(validators=[validate_email])
- [ ] EmailInput

#### P152. ¿Cuál es el propósito de usar el método `is_valid()` en un formulario Django?

- [ ] Para verificar si el formulario ha sido enviado
- [ ] Para guardar los datos del formulario en la base de datos
- [x] Para validar los datos del formulario y verificar si son correctos
- [ ] Para renderizar el HTML del formulario

#### P153. ¿Cuándo usarías un `ModelForm` en lugar de un `Form` regular de Django?

- [ ] Cuando quieres crear un formulario que no esté vinculado a un modelo de base de datos
- [ ] Cuando quieres agregar reglas de validación personalizadas a tu formulario
- [ ] Cuando quieres renderizar el formulario usando una plantilla personalizada
- [x] Cuando quieres crear un formulario que esté directamente vinculado a un modelo de base de datos

#### P154. ¿Cómo puedes personalizar el renderizado de un campo de formulario Django?

- [ ] Sobrescribiendo el método `as_p()` del formulario
- [ ] Creando una clase de campo de formulario personalizada
- [x] Usando el parámetro `widgets` al definir el campo del formulario
- [ ] Modificando la plantilla que renderiza el formulario

#### P155. ¿Cuál es el propósito del diccionario `cleaned_data` en un formulario Django?

- [ ] Contiene los datos sin procesar y sin validar enviados por el usuario
- [ ] Contiene los datos del formulario escapados en HTML
- [x] Contiene los datos validados y limpiados del formulario
- [ ] Contiene los valores predeterminados para los campos del formulario

#### P156. ¿Cómo puedes agregar reglas de validación personalizadas a un campo de formulario Django?

- [ ] Sobrescribiendo el método `clean()` del formulario
- [ ] Agregando un parámetro `validators` a la definición del campo del formulario
- [x] Tanto sobrescribiendo el método `clean()` como agregando un parámetro `validators`
- [ ] Creando una clase de campo de formulario personalizada y agregando la lógica de validación allí

#### P157. ¿Cuál es el propósito del atributo `form.is_bound` en un formulario Django?

- [ ] Indica si el formulario ha sido enviado
- [x] Indica si el formulario ha sido enviado con datos
- [ ] Indica si el formulario ha sido guardado en la base de datos
- [ ] Indica si el formulario ha sido renderizado en la página

#### P158. ¿Cómo puedes personalizar la salida HTML de un campo de formulario Django?

- [ ] Sobrescribiendo los métodos `as_p()`, `as_ul()` o `as_table()` del formulario
- [ ] Creando una clase de widget personalizada y usándola en la definición del campo del formulario
- [x] Tanto sobrescribiendo los métodos de renderizado del campo del formulario como usando widgets personalizados
- [ ] Modificando la plantilla que renderiza el formulario

#### P159. ¿Cuál es el propósito del parámetro `required` al definir un campo de formulario Django?

- [ ] Establece el valor predeterminado del campo
- [ ] Agrega lógica de validación personalizada al campo
- [x] Hace que el campo sea obligatorio para que el formulario sea válido
- [ ] Cambia el renderizado HTML del campo

#### P160. ¿Cómo puedes agregar mensajes de error personalizados a un campo de formulario Django?

- [ ] Estableciendo el parámetro `error_messages` al definir el campo del formulario
- [ ] Sobrescribiendo el método `clean()` del formulario y generando un `ValidationError`
- [x] Usando tanto el parámetro `error_messages` como sobrescribiendo el método `clean()`
- [ ] Modificando la plantilla que renderiza el formulario

#### P161. ¿Cuál es el propósito del parámetro `label` al definir un campo de formulario Django?

- [ ] Establece el valor predeterminado del campo
- [x] Establece el texto de la etiqueta que se muestra para el campo
- [ ] Agrega lógica de validación personalizada al campo
- [ ] Cambia el renderizado HTML del campo

#### P162. ¿Cómo puedes pre-poblar los datos iniciales en un formulario Django?

- [ ] Estableciendo el parámetro `initial` al definir los campos del formulario
- [ ] Pasando los datos iniciales como parte de los datos `request.POST`
- [x] Pasando los datos iniciales como un parámetro `data` al crear la instancia del formulario
- [ ] Sobrescribiendo el método `get_initial()` de la clase del formulario

#### P163. ¿Cuál es el propósito del parámetro `widget` al definir un campo de formulario Django?

- [ ] Establece el valor predeterminado del campo
- [ ] Agrega lógica de validación personalizada al campo
- [x] Especifica el widget HTML a usar para renderizar el campo
- [ ] Cambia el texto de la etiqueta que se muestra para el campo

#### P164. ¿Cómo puedes personalizar los atributos HTML de un campo de formulario Django?

- [ ] Estableciendo el parámetro `attrs` al definir el campo del formulario
- [ ] Sobrescribiendo el método `as_widget()` del campo del formulario
- [x] Usando tanto el parámetro `attrs` como sobrescribiendo `as_widget()`
- [ ] Modificando la plantilla que renderiza el formulario

#### P165. ¿Cuál es el propósito del parámetro `help_text` al definir un campo de formulario Django?

- [ ] Establece el valor predeterminado del campo
- [x] Proporciona texto explicativo adicional para el campo
- [ ] Agrega lógica de validación personalizada al campo
- [ ] Cambia el renderizado HTML del campo

#### P166. ¿Cómo puedes agregar lógica de validación personalizada a un campo de formulario Django?

- [ ] Estableciendo el parámetro `validators` al definir el campo del formulario
- [ ] Sobrescribiendo el método `clean()` del campo del formulario
- [x] Usando tanto el parámetro `validators` como sobrescribiendo `clean()`
- [ ] Modificando la plantilla que renderiza el formulario

#### P167. ¿Cuál es el propósito del parámetro `required` al definir un campo de formulario Django?

- [ ] Establece el valor predeterminado del campo
- [ ] Agrega lógica de validación personalizada al campo
- [x] Hace que el campo sea obligatorio para que el formulario sea válido
- [ ] Cambia el renderizado HTML del campo

#### P168. ¿Cómo puedes personalizar los mensajes de error mostrados para un campo de formulario Django?

- [ ] Estableciendo el parámetro `error_messages` al definir el campo del formulario
- [ ] Sobrescribiendo el método `clean()` del campo del formulario y generando un `ValidationError`
- [x] Usando tanto el parámetro `error_messages` como sobrescribiendo `clean()`
- [ ] Modificando la plantilla que renderiza el formulario

#### P169. ¿Cuál es el propósito del parámetro `label` al definir un campo de formulario Django?

- [ ] Establece el valor predeterminado del campo
- [x] Establece el texto de la etiqueta que se muestra para el campo
- [ ] Agrega lógica de validación personalizada al campo
- [ ] Cambia el renderizado HTML del campo

#### P170. ¿Cómo puedes pre-poblar los datos iniciales en un formulario Django?

- [ ] Estableciendo el parámetro `initial` al definir los campos del formulario
- [ ] Pasando los datos iniciales como parte de los datos `request.POST`
- [x] Pasando los datos iniciales como un parámetro `data` al crear la instancia del formulario
- [ ] Sobrescribiendo el método `get_initial()` de la clase del formulario

#### P171. ¿Cuál es el propósito del parámetro `widget` al definir un campo de formulario Django?

- [ ] Establece el valor predeterminado del campo
- [ ] Agrega lógica de validación personalizada al campo
- [x] Especifica el widget HTML a usar para renderizar el campo
- [ ] Cambia el texto de la etiqueta que se muestra para el campo

#### P172. ¿Cómo puedes personalizar los atributos HTML de un campo de formulario Django?

- [ ] Estableciendo el parámetro `attrs` al definir el campo del formulario
- [ ] Sobrescribiendo el método `as_widget()` del campo del formulario
- [x] Usando tanto el parámetro `attrs` como sobrescribiendo `as_widget()`
- [ ] Modificando la plantilla que renderiza el formulario

#### P173. ¿Cuál es el propósito del parámetro `help_text` al definir un campo de formulario Django?

- [ ] Establece el valor predeterminado del campo
- [x] Proporciona texto explicativo adicional para el campo
- [ ] Agrega lógica de validación personalizada al campo
- [ ] Cambia el renderizado HTML del campo

#### P174. ¿Cómo puedes agregar lógica de validación personalizada a un campo de formulario Django?

- [ ] Estableciendo el parámetro `validators` al definir el campo del formulario
- [ ] Sobrescribiendo el método `clean()` del campo del formulario
- [x] Usando tanto el parámetro `validators` como sobrescribiendo `clean()`
- [ ] Modificando la plantilla que renderiza el formulario

#### P175. ¿Cuál es el propósito del parámetro `max_length` al definir un campo CharField de formulario Django?

- [ ] Establece el valor predeterminado del campo
- [ ] Agrega lógica de validación personalizada al campo
- [x] Limita la longitud máxima de la entrada del usuario
- [ ] Cambia el renderizado HTML del campo

#### P176. ¿Cómo puedes personalizar los mensajes de error mostrados para un campo de formulario Django?

- [ ] Estableciendo el parámetro `error_messages` al definir el campo del formulario
- [ ] Sobrescribiendo el método `clean()` del campo del formulario y generando un `ValidationError`
- [x] Usando tanto el parámetro `error_messages` como sobrescribiendo `clean()`
- [ ] Modificando la plantilla que renderiza el formulario

#### P177. ¿Cuál es el propósito del parámetro `required` al definir un campo de formulario Django?

- [ ] Establece el valor predeterminado del campo
- [ ] Agrega lógica de validación personalizada al campo
- [x] Hace que el campo sea obligatorio para que el formulario sea válido
- [ ] Cambia el renderizado HTML del campo

#### P178. ¿Cómo puedes pre-poblar los datos iniciales en un formulario Django?

- [ ] Estableciendo el parámetro `initial` al definir los campos del formulario
- [ ] Pasando los datos iniciales como parte de los datos `request.POST`
- [x] Pasando los datos iniciales como un parámetro `data` al crear la instancia del formulario
- [ ] Sobrescribiendo el método `get_initial()` de la clase del formulario

#### P179. ¿Cuál es el propósito del parámetro `widget` al definir un campo de formulario Django?

- [ ] Establece el valor predeterminado del campo
- [ ] Agrega lógica de validación personalizada al campo
- [x] Especifica el widget HTML a usar para renderizar el campo
- [ ] Cambia el texto de la etiqueta que se muestra para el campo

#### P180. ¿Cómo puedes personalizar los atributos HTML de un campo de formulario Django?

- [ ] Estableciendo el parámetro `attrs` al definir el campo del formulario
- [ ] Sobrescribiendo el método `as_widget()` del campo del formulario
- [x] Usando tanto el parámetro `attrs` como sobrescribiendo `as_widget()`
- [ ] Modificando la plantilla que renderiza el formulario

#### P181. ¿Cuál es el propósito del parámetro `help_text` al definir un campo de formulario Django?

- [ ] Establece el valor predeterminado del campo
- [x] Proporciona texto explicativo adicional para el campo
- [ ] Agrega lógica de validación personalizada al campo
- [ ] Cambia el renderizado HTML del campo

#### P182. ¿Cómo puedes agregar lógica de validación personalizada a un campo de formulario Django?

- [ ] Estableciendo el parámetro `validators` al definir el campo del formulario
- [ ] Sobrescribiendo el método `clean()` del campo del formulario
- [x] Usando tanto el parámetro `validators` como sobrescribiendo `clean()`
- [ ] Modificando la plantilla que renderiza el formulario

#### P183. ¿Cuál es el propósito del parámetro `max_length` al definir un campo CharField de formulario Django?

- [ ] Establece el valor predeterminado del campo
- [ ] Agrega lógica de validación personalizada al campo
- [x] Limita la longitud máxima de la entrada del usuario
- [ ] Cambia el renderizado HTML del campo

#### P184. ¿Cómo puedes personalizar los mensajes de error mostrados para un campo de formulario Django?

- [ ] Estableciendo el parámetro `error_messages` al definir el campo del formulario
- [ ] Sobrescribiendo el método `clean()` del campo del formulario y generando un `ValidationError`
- [x] Usando tanto el parámetro `error_messages` como sobrescribiendo `clean()`
- [ ] Modificando la plantilla que renderiza el formulario

#### P185. ¿Cuál es el propósito del parámetro `required` al definir un campo de formulario Django?

- [ ] Establece el valor predeterminado del campo
- [ ] Agrega lógica de validación personalizada al campo
- [x] Hace que el campo sea obligatorio para que el formulario sea válido
- [ ] Cambia el renderizado HTML del campo

#### P186. ¿Cómo puedes pre-poblar los datos iniciales en un formulario Django?

- [ ] Estableciendo el parámetro `initial` al definir los campos del formulario
- [ ] Pasando los datos iniciales como parte de los datos `request.POST`
- [x] Pasando los datos iniciales como un parámetro `data` al crear la instancia del formulario
- [ ] Sobrescribiendo el método `get_initial()` de la clase del formulario

#### P187. ¿Cuál es el propósito del parámetro `widget` al definir un campo de formulario Django?

- [ ] Establece el valor predeterminado del campo
- [ ] Agrega lógica de validación personalizada al campo
- [x] Especifica el widget HTML a usar para renderizar el campo
- [ ] Cambia el texto de la etiqueta que se muestra para el campo

#### P188. ¿Cómo puedes personalizar los atributos HTML de un campo de formulario Django?

- [ ] Estableciendo el parámetro `attrs` al definir el campo del formulario
- [ ] Sobrescribiendo el método `as_widget()` del campo del formulario
- [x] Usando tanto el parámetro `attrs` como sobrescribiendo `as_widget()`
- [ ] Modificando la plantilla que renderiza el formulario

#### P189. ¿Cuál es el propósito del parámetro `help_text` al definir un campo de formulario Django?

- [ ] Establece el valor predeterminado del campo
- [x] Proporciona texto explicativo adicional para el campo
- [ ] Agrega lógica de validación personalizada al campo
- [ ] Cambia el renderizado HTML del campo

#### P190. ¿Cómo puedes agregar lógica de validación personalizada a un campo de formulario Django?

- [ ] Estableciendo el parámetro `validators` al definir el campo del formulario
- [ ] Sobrescribiendo el método `clean()` del campo del formulario
- [x] Usando tanto el parámetro `validators` como sobrescribiendo `clean()`
- [ ] Modificando la plantilla que renderiza el formulario

#### P191. ¿Cuál es el propósito del parámetro `max_length` al definir un campo CharField de formulario Django?

- [ ] Establece el valor predeterminado del campo
- [ ] Agrega lógica de validación personalizada al campo
- [x] Limita la longitud máxima de la entrada del usuario
- [ ] Cambia el renderizado HTML del campo

#### P192. ¿Cómo puedes personalizar los mensajes de error mostrados para un campo de formulario Django?

- [ ] Estableciendo el parámetro `error_messages` al definir el campo del formulario
- [ ] Sobrescribiendo el método `clean()` del campo del formulario y generando un `ValidationError`
- [x] Usando tanto el parámetro `error_messages` como sobrescribiendo `clean()`
- [ ] Modificando la plantilla que renderiza el formulario

#### P193. ¿Cuál es el propósito del parámetro `required` al definir un campo de formulario Django?

- [ ] Establece el valor predeterminado del campo
- [ ] Agrega lógica de validación personalizada al campo
- [x] Hace que el campo sea obligatorio para que el formulario sea válido
- [ ] Cambia el renderizado HTML del campo

#### P194. ¿Cómo puedes pre-poblar los datos iniciales en un formulario Django?

- [ ] Estableciendo el parámetro `initial` al definir los campos del formulario
- [ ] Pasando los datos iniciales como parte de los datos `request.POST`
- [x] Pasando los datos iniciales como un parámetro `data` al crear la instancia del formulario
- [ ] Sobrescribiendo el método `get_initial()` de la clase del formulario

#### P195. ¿Cuál es el propósito del parámetro `widget` al definir un campo de formulario Django?

- [ ] Establece el valor predeterminado del campo
- [ ] Agrega lógica de validación personalizada al campo
- [x] Especifica el widget HTML a usar para renderizar el campo
- [ ] Cambia el texto de la etiqueta que se muestra para el campo

#### P196. ¿Cómo puedes personalizar los atributos HTML de un campo de formulario Django?

- [ ] Estableciendo el parámetro `attrs` al definir el campo del formulario
- [ ] Sobrescribiendo el método `as_widget()` del campo del formulario
- [x] Usando tanto el parámetro `attrs` como sobrescribiendo `as_widget()`
- [ ] Modificando la plantilla que renderiza el formulario

#### P197. ¿Cuál es el propósito del parámetro `help_text` al definir un campo de formulario Django?

- [ ] Establece el valor predeterminado del campo
- [x] Proporciona texto explicativo adicional para el campo
- [ ] Agrega lógica de validación personalizada al campo
- [ ] Cambia el renderizado HTML del campo

#### P198. ¿Cómo puedes agregar lógica de validación personalizada a un campo de formulario Django?

- [ ] Estableciendo el parámetro `validators` al definir el campo del formulario
- [ ] Sobrescribiendo el método `clean()` del campo del formulario
- [x] Usando tanto el parámetro `validators` como sobrescribiendo `clean()`
- [ ] Modificando la plantilla que renderiza el formulario

#### P199. ¿Cuál es el propósito del parámetro `max_length` al definir un campo CharField de formulario Django?

- [ ] Establece el valor predeterminado del campo
- [ ] Agrega lógica de validación personalizada al campo
- [x] Limita la longitud máxima de la entrada del usuario
- [ ] Cambia el renderizado HTML del campo

#### P200. ¿Cómo puedes personalizar los mensajes de error mostrados para un formulario Django?

#### P201. ¿Cuál es el propósito principal del método `get_context_data()` en una vista basada en clases de Django?

- [ ] Para definir el patrón de URL para la vista
- [x] Para proporcionar datos adicionales a la plantilla
- [ ] Para manejar métodos de solicitud HTTP
- [ ] Para definir la plantilla de la vista

#### P202. ¿Qué vista basada en clases de Django usarías para crear una interfaz simple de crear, leer, actualizar y eliminar (CRUD) para un modelo?

- [ ] `TemplateView`
- [ ] `FormView`
- [x] `ModelFormView`
- [ ] `DetailView`

#### P203. ¿Cuál es el propósito del método `get_queryset()` en una vista basada en clases de Django?

- [ ] Para definir el patrón de URL para la vista
- [ ] Para manejar métodos de solicitud HTTP
- [x] Para personalizar el queryset utilizado por la vista
- [ ] Para proporcionar datos adicionales a la plantilla

#### P204. ¿Cuál es el caso de uso principal del decorador `@login_required` de Django?

- [ ] Para requerir HTTPS para una vista
- [x] Para requerir autenticación de usuario para una vista
- [ ] Para limitar el número de solicitudes a una vista
- [ ] Para manejar la validación de formularios en una vista

#### P205. ¿Qué vista basada en clases de Django usarías para mostrar una lista de objetos de un modelo?

- [ ] `DetailView`
- [ ] `CreateView`
- [x] `ListView`
- [ ] `UpdateView`

#### P206. ¿Cuál es el propósito del método `get_absolute_url()` en un modelo Django?

- [ ] Para definir el patrón de URL para la vista de detalle del modelo
- [ ] Para manejar métodos de solicitud HTTP para el modelo
- [x] Para proporcionar una URL canónica para una instancia del modelo
- [ ] Para personalizar el queryset utilizado por una vista para el modelo

#### P207. ¿Qué vista basada en clases de Django usarías para mostrar un solo objeto de un modelo?

- [ ] `ListView`
- [x] `DetailView`
- [ ] `CreateView`
- [ ] `UpdateView`

#### P208. ¿Cuál es el propósito del método `form_valid()` en una vista basada en clases de Django?

- [ ] Para definir el patrón de URL para la vista
- [x] Para manejar envíos de formularios exitosos
- [ ] Para personalizar el queryset utilizado por la vista
- [ ] Para proporcionar datos adicionales a la plantilla

#### P209. ¿Qué vista basada en clases de Django usarías para manejar envíos de formularios?

- [ ] `ListView`
- [ ] `DetailView`
- [x] `FormView`
- [ ] `TemplateView`

#### P210. ¿Cuál es el propósito del método `get_success_url()` en una vista basada en clases de Django?

- [ ] Para definir el patrón de URL para la vista
- [ ] Para personalizar el queryset utilizado por la vista
- [x] Para especificar la URL a la que redirigir después de un envío de formulario exitoso
- [ ] Para proporcionar datos adicionales a la plantilla

#### P211. ¿Qué vista basada en clases de Django usarías para crear un nuevo objeto de un modelo?

- [ ] `ListView`
- [ ] `DetailView`
- [x] `CreateView`
- [ ] `UpdateView`

#### P212. ¿Cuál es el propósito del método `dispatch()` en una vista basada en clases de Django?

- [ ] Para definir el patrón de URL para la vista
- [x] Para manejar la solicitud HTTP entrante y determinar el manejador de método HTTP apropiado
- [ ] Para personalizar el queryset utilizado por la vista
- [ ] Para proporcionar datos adicionales a la plantilla

#### P213. ¿Qué vista basada en clases de Django usarías para actualizar un objeto existente de un modelo?

- [ ] `ListView`
- [ ] `CreateView`
- [ ] `DetailView`
- [x] `UpdateView`

#### P214. ¿Cuál es el propósito del método `get_object()` en una vista basada en clases de Django?

- [ ] Para definir el patrón de URL para la vista
- [x] Para recuperar el objeto sobre el que debe operar la vista
- [ ] Para manejar la solicitud HTTP entrante y determinar el manejador de método HTTP apropiado
- [ ] Para proporcionar datos adicionales a la plantilla

#### P215. ¿Qué vista basada en clases de Django usarías para eliminar un objeto existente de un modelo?

- [ ] `ListView`
- [ ] `CreateView`
- [ ] `UpdateView`
- [x] `DeleteView`

#### P216. ¿Cuál es el propósito del método `get_form_class()` en una vista basada en clases de Django?

- [ ] Para definir el patrón de URL para la vista
- [ ] Para manejar la solicitud HTTP entrante y determinar el manejador de método HTTP apropiado
- [x] Para personalizar el formulario utilizado por la vista
- [ ] Para proporcionar datos adicionales a la plantilla

#### P217. ¿Qué vista basada en clases de Django usarías para mostrar una plantilla sin ninguna funcionalidad específica del modelo?

- [x] `TemplateView`
- [ ] `ListView`
- [ ] `CreateView`
- [ ] `UpdateView`

#### P218. ¿Cuál es el propósito del método `get_form_kwargs()` en una vista basada en clases de Django?

- [ ] Para definir el patrón de URL para la vista
- [ ] Para manejar la solicitud HTTP entrante y determinar el manejador de método HTTP apropiado
- [x] Para personalizar los argumentos pasados al formulario utilizado por la vista
- [ ] Para proporcionar datos adicionales a la plantilla

#### P219. ¿Qué vista basada en clases de Django usarías para manejar subidas de archivos?

- [ ] `TemplateView`
- [x] `FormView`
- [ ] `ListView`
- [ ] `CreateView`

#### P220. ¿Cuál es el propósito del método de clase `as_view()` en una vista basada en clases de Django?

- [ ] Para definir el patrón de URL para la vista
- [x] Para crear una vista basada en funciones a partir de una vista basada en clases
- [ ] Para manejar la solicitud HTTP entrante y determinar el manejador de método HTTP apropiado
- [ ] Para proporcionar datos adicionales a la plantilla

#### P221. ¿Qué vista basada en clases de Django usarías para implementar un asistente de formularios múltiples?

- [ ] `TemplateView`
- [x] `FormView`
- [ ] `ListView`
- [ ] `CreateView`

#### P222. ¿Cuál es el propósito del método `get_success_message()` en una vista basada en clases de Django?

- [ ] Para definir el patrón de URL para la vista
- [ ] Para manejar la solicitud HTTP entrante y determinar el manejador de método HTTP apropiado
- [x] Para personalizar el mensaje de éxito mostrado después de un envío de formulario exitoso
- [ ] Para proporcionar datos adicionales a la plantilla

#### P223. ¿Qué vista basada en clases de Django usarías para implementar una funcionalidad de búsqueda?

- [x] `ListView`
- [ ] `FormView`
- [ ] `TemplateView`
- [ ] `CreateView`

#### P224. ¿Cuál es el propósito del método `get_form_kwargs()` en una vista basada en clases de Django?

- [ ] Para definir el patrón de URL para la vista
- [ ] Para manejar la solicitud HTTP entrante y determinar el manejador de método HTTP apropiado
- [x] Para personalizar los argumentos pasados al formulario utilizado por la vista
- [ ] Para proporcionar datos adicionales a la plantilla

#### P225. ¿Qué vista basada en clases de Django usarías para implementar una vista que requiere autenticación?

- [ ] `TemplateView`
- [x] `LoginRequiredMixin`
- [ ] `ListView`
- [ ] `CreateView`

#### P226. ¿Cuál es el propósito del método `get_queryset()` en una vista basada en clases de Django?

- [ ] Para definir el patrón de URL para la vista
- [ ] Para manejar la solicitud HTTP entrante y determinar el manejador de método HTTP apropiado
- [x] Para personalizar el queryset utilizado por la vista
- [ ] Para proporcionar datos adicionales a la plantilla

#### P227. ¿Qué vista basada en clases de Django usarías para implementar una vista que requiere autorización de usuario basada en permisos?

- [ ] `TemplateView`
- [x] `PermissionRequiredMixin`
- [ ] `ListView`
- [ ] `CreateView`

#### P228. ¿Cuál es el propósito del método `get_context_object_name()` en una vista basada en clases de Django?

- [ ] Para definir el patrón de URL para la vista
- [ ] Para manejar la solicitud HTTP entrante y determinar el manejador de método HTTP apropiado
- [x] Para personalizar el nombre del objeto(s) pasado a la plantilla
- [ ] Para proporcionar datos adicionales a la plantilla

#### P229. ¿Qué vista basada en clases de Django usarías para implementar una vista que requiere protección CSRF?

- [ ] `TemplateView`
- [x] `CsrfExemptMixin`
- [ ] `ListView`
- [ ] `CreateView`

#### P230. ¿Cuál es el propósito del método `get_template_names()` en una vista basada en clases de Django?

- [ ] Para definir el patrón de URL para la vista
- [ ] Para manejar la solicitud HTTP entrante y determinar el manejador de método HTTP apropiado
- [x] Para personalizar la(s) plantilla(s) utilizada(s) por la vista
- [ ] Para proporcionar datos adicionales a la plantilla

#### P231. ¿Qué vista basada en clases de Django usarías para implementar una vista que requiere autenticación HTTP Basic?

- [ ] `TemplateView`
- [x] `HttpBasicAuthMixin`
- [ ] `ListView`
- [ ] `CreateView`

#### P232. ¿Cuál es el propósito del método `get_initial()` en una vista basada en clases de Django?

- [ ] Para definir el patrón de URL para la vista
- [ ] Para manejar la solicitud HTTP entrante y determinar el manejador de método HTTP apropiado
- [x] Para personalizar los datos iniciales para el formulario utilizado por la vista
- [ ] Para proporcionar datos adicionales a la plantilla

#### P233. ¿Qué vista basada en clases de Django usarías para implementar una vista que requiere autenticación HTTP Digest?

- [ ] `TemplateView`
- [x] `HttpDigestAuthMixin`
- [ ] `ListView`
- [ ] `CreateView`

#### P234. ¿Cuál es el propósito del método `get_success_url()` en una vista basada en clases de Django?

- [ ] Para definir el patrón de URL para la vista
- [ ] Para manejar la solicitud HTTP entrante y determinar el manejador de método HTTP apropiado
- [x] Para especificar la URL a la que redirigir después de un envío de formulario exitoso
- [ ] Para proporcionar datos adicionales a la plantilla

#### P235. ¿Qué vista basada en clases de Django usarías para implementar una vista que requiere control de acceso basado en dirección IP?

- [ ] `TemplateView`
- [x] `IPAddressRequiredMixin`
- [ ] `ListView`
- [ ] `CreateView`

#### P236. ¿Cuál es el propósito del método `form_invalid()` en una vista basada en clases de Django?

- [ ] Para definir el patrón de URL para la vista
- [x] Para manejar envíos de formularios no exitosos
- [ ] Para personalizar el queryset utilizado por la vista
- [ ] Para proporcionar datos adicionales a la plantilla

#### P237. ¿Qué vista basada en clases de Django usarías para implementar una vista que requiere autenticación de dos factores?

- [ ] `TemplateView`
- [x] `TwoFactorAuthMixin`
- [ ] `ListView`
- [ ] `CreateView`

#### P238. ¿Cuál es el propósito del método `get_form()` en una vista basada en clases de Django?

- [ ] Para definir el patrón de URL para la vista
- [ ] Para manejar la solicitud HTTP entrante y determinar el manejador de método HTTP apropiado
- [x] Para personalizar el formulario utilizado por la vista
- [ ] Para proporcionar datos adicionales a la plantilla

#### P239. ¿Qué vista basada en clases de Django usarías para implementar una vista que requiere activación de usuario?

- [ ] `TemplateView`
- [x] `UserActivationRequiredMixin`
- [ ] `ListView`
- [ ] `CreateView`

#### P240. ¿Cuál es el propósito del método `get_object()` en una vista basada en clases de Django?

- [ ] Para definir el patrón de URL para la vista
- [x] Para recuperar el objeto sobre el que debe operar la vista
- [ ] Para manejar la solicitud HTTP entrante y determinar el manejador de método HTTP apropiado
- [ ] Para proporcionar datos adicionales a la plantilla

#### P241. ¿Qué vista basada en clases de Django usarías para implementar una vista que requiere HTTPS?

- [ ] `TemplateView`
- [x] `SSLRequiredMixin`
- [ ] `ListView`
- [ ] `CreateView`

#### P242. ¿Cuál es el propósito del método `get_context_data()` en una vista basada en clases de Django?

- [ ] Para definir el patrón de URL para la vista
- [ ] Para manejar la solicitud HTTP entrante y determinar el manejador de método HTTP apropiado
- [x] Para proporcionar datos adicionales a la plantilla
- [ ] Para personalizar el queryset utilizado por la vista

#### P243. ¿Qué vista basada en clases de Django usarías para implementar una vista que requiere verificación de usuario?

- [ ] `TemplateView`
- [x] `UserVerificationRequiredMixin`
- [ ] `ListView`
- [ ] `CreateView`

#### P244. ¿Cuál es el propósito del método `dispatch()` en una vista basada en clases de Django?

- [ ] Para definir el patrón de URL para la vista
- [x] Para manejar la solicitud HTTP entrante y determinar el manejador de método HTTP apropiado
- [ ] Para personalizar el queryset utilizado por la vista
- [ ] Para proporcionar datos adicionales a la plantilla

#### P245. ¿Qué vista basada en clases de Django usarías para implementar una vista que requiere acceso de usuario staff?

- [ ] `TemplateView`
- [x] `StaffuserRequiredMixin`
- [ ] `ListView`
- [ ] `CreateView`

#### P246. ¿Cuál es el propósito del método `get_form_kwargs()` en una vista basada en clases de Django?

- [ ] Para definir el patrón de URL para la vista
- [ ] Para manejar la solicitud HTTP entrante y determinar el manejador de método HTTP apropiado
- [x] Para personalizar los argumentos pasados al formulario utilizado por la vista
- [ ] Para proporcionar datos adicionales a la plantilla

#### P247. ¿Qué vista basada en clases de Django usarías para implementar una vista que requiere acceso de superusuario?

- [ ] `TemplateView`
- [x] `SuperuserRequiredMixin`
- [ ] `ListView`
- [ ] `CreateView`

#### P248. ¿Cuál es el propósito del método `get_form_class()` en una vista basada en clases de Django?

- [ ] Para definir el patrón de URL para la vista
- [ ] Para manejar la solicitud HTTP entrante y determinar el manejador de método HTTP apropiado
- [x] Para personalizar el formulario utilizado por la vista
- [ ] Para proporcionar datos adicionales a la plantilla

#### P249. ¿Qué vista basada en clases de Django usarías para implementar una vista que requiere verificación de correo electrónico del usuario?

- [ ] `TemplateView`
- [x] `EmailVerificationRequiredMixin`
- [ ] `ListView`
- [ ] `CreateView`

#### P250. ¿Cuál es el propósito del decorador `@method_decorator()` en una vista basada en clases de Django?

- [ ] Para definir el patrón de URL para la vista
- [x] Para aplicar un decorador de vista basada en funciones a un método de vista basada en clases
- [ ] Para personalizar el queryset utilizado por la vista
- [ ] Para proporcionar datos adicionales a la plantilla

#### P251. ¿Qué método de serializador de Django REST Framework te permite validar y limpiar datos antes de que se guarden en la base de datos?

- [ ] update()
- [x] validate()
- [ ] save()
- [ ] create()

#### P252. ¿Cuál es el propósito del atributo `lookup_field` en un ViewSet de Django REST Framework?

- [ ] Especifica el campo utilizado para buscar el objeto en la base de datos.
- [ ] Establece el ordenamiento predeterminado del queryset.
- [x] Determina el parámetro de URL utilizado para recuperar el objeto.
- [ ] Filtra el queryset basado en el campo de búsqueda.

#### P253. ¿Cómo puedes aplicar autenticación para todas las vistas en una API de Django REST Framework?

- [ ] Establecer el atributo `authentication_classes` en la clase `DefaultRouter`.
- [x] Establecer la configuración `DEFAULT_AUTHENTICATION_CLASSES` en el archivo settings.py de tu proyecto Django.
- [ ] Sobrescribir el método `get_authenticators()` en tu clase de vista base.
- [ ] Usar el decorador `@authentication_required` en cada función de vista.

#### P254. ¿Cuál es el propósito de la clase `ModelSerializer` en Django REST Framework?

- [ ] Genera automáticamente una clase serializadora basada en un modelo Django.
- [ ] Proporciona una forma de serializar y deserializar estructuras de datos complejas.
- [ ] Te permite definir lógica de serialización personalizada para tus modelos.
- [x] Todas las anteriores

#### P255. ¿Cómo puedes agregar lógica de validación personalizada a un serializador de Django REST Framework?

- [ ] Sobrescribir el método `validate()` en la clase serializadora.
- [ ] Usar el argumento `validators` al definir los campos del serializador.
- [ ] Crear una función validadora personalizada y aplicarla a los campos del serializador.
- [x] Todas las anteriores

#### P256. ¿Cuál es el propósito del atributo `permission_classes` en un ViewSet de Django REST Framework?

- [ ] Especifica las clases de autenticación a usar para el ViewSet.
- [ ] Establece el ordenamiento predeterminado del queryset.
- [x] Determina las clases de permisos que se aplicarán al ViewSet.
- [ ] Filtra el queryset basado en los permisos especificados.

#### P257. ¿Cómo puedes usar Django REST Framework para implementar autenticación basada en tokens?

- [ ] Usar la clase `TokenAuthentication` e incluir la aplicación `rest_framework.authtoken` en tu proyecto.
- [ ] Implementar un backend de autenticación personalizado que genere y verifique tokens.
- [ ] Usar la clase `JSONWebTokenAuthentication` e incluir el paquete `rest_framework_jwt`.
- [x] Todas las anteriores

#### P258. ¿Cuál es el propósito del atributo `serializer_class` en un ViewSet de Django REST Framework?

- [ ] Especifica el serializador a usar para las operaciones de lectura del ViewSet.
- [ ] Determina las clases de autenticación a usar para el ViewSet.
- [x] Especifica el serializador a usar para las operaciones de crear, actualizar y eliminar del ViewSet.
- [ ] Establece el ordenamiento predeterminado del queryset.

#### P259. ¿Cómo puedes agregar capacidades de filtrado a una API de Django REST Framework?

- [ ] Usar la clase `FilterSet` e incluir el paquete `django-filter` en tu proyecto.
- [ ] Implementar un backend de filtro personalizado y aplicarlo al ViewSet.
- [ ] Usar las clases `SearchFilter` y `OrderingFilter` proporcionadas por Django REST Framework.
- [x] Todas las anteriores

#### P260. ¿Cuál es el propósito del decorador `@action` en un ViewSet de Django REST Framework?

- [ ] Te permite definir acciones personalizadas que no son parte de las operaciones CRUD estándar.
- [ ] Especifica los métodos HTTP que deben permitirse para la acción.
- [ ] Establece la ruta de URL para la acción personalizada.
- [x] Todas las anteriores

#### P261. ¿Cómo puedes usar Django REST Framework para implementar control de acceso basado en roles (RBAC) en tu API?

- [ ] Usar la clase de permisos `IsAdminUser` para restringir el acceso a usuarios administradores.
- [ ] Crear clases de permisos personalizadas que verifiquen el rol o la membresía de grupo del usuario.
- [ ] Implementar un backend de autenticación personalizado que recupere el rol del usuario de una fuente externa.
- [x] Todas las anteriores

#### P262. ¿Cuál es el propósito del atributo `serializer_class` en un `GenericAPIView` de Django REST Framework?

- [ ] Especifica el serializador a usar para las operaciones de lectura de la vista.
- [x] Especifica el serializador a usar para las operaciones de crear, actualizar y eliminar de la vista.
- [ ] Establece el ordenamiento predeterminado del queryset.
- [ ] Determina las clases de autenticación a usar para la vista.

#### P263. ¿Cómo puedes usar Django REST Framework para implementar paginación en tu API?

- [ ] Usar las clases `LimitOffsetPagination` o `PageNumberPagination` proporcionadas por Django REST Framework.
- [ ] Implementar una clase de paginación personalizada y aplicarla al ViewSet.
- [ ] Establecer el atributo `pagination_class` en el ViewSet o vista.
- [x] Todas las anteriores

#### P264. ¿Cuál es el propósito del atributo `throttle_classes` en un ViewSet de Django REST Framework?

- [ ] Especifica las clases de throttling a aplicar al ViewSet.
- [ ] Determina las clases de autenticación a usar para el ViewSet.
- [ ] Establece el ordenamiento predeterminado del queryset.
- [x] Limita la tasa a la que los clientes pueden hacer solicitudes al ViewSet.

#### P265. ¿Cómo puedes usar Django REST Framework para implementar caché en tu API?

- [ ] Usar las clases `CacheResponseMixin` o `BrowsableAPIRenderer` proporcionadas por Django REST Framework.
- [ ] Implementar un backend de caché personalizado y aplicarlo al ViewSet.
- [ ] Establecer el encabezado `cache_control` en la respuesta.
- [x] Todas las anteriores

#### P266. ¿Cuál es el propósito del atributo `renderer_classes` en un ViewSet de Django REST Framework?

- [ ] Especifica el serializador a usar para las operaciones de crear, actualizar y eliminar del ViewSet.
- [ ] Determina las clases de autenticación a usar para el ViewSet.
- [x] Especifica los renderizadores a usar para las respuestas del ViewSet.
- [ ] Establece el ordenamiento predeterminado del queryset.

#### P267. ¿Cómo puedes usar Django REST Framework para implementar versionado en tu API?

- [ ] Usar las clases `NamespaceVersioning` o `URLPathVersioning` proporcionadas por Django REST Framework.
- [ ] Implementar un esquema de versionado personalizado y aplicarlo al ViewSet.
- [ ] Establecer el atributo `version` en el ViewSet o vista.
- [x] Todas las anteriores

#### P268. ¿Cuál es el propósito del atributo `lookup_url_kwarg` en un ViewSet de Django REST Framework?

- [ ] Especifica el parámetro de URL utilizado para recuperar el objeto.
- [ ] Establece el ordenamiento predeterminado del queryset.
- [x] Determina el nombre del parámetro de URL utilizado para buscar el objeto.
- [ ] Filtra el queryset basado en el campo de búsqueda.

#### P269. ¿Cómo puedes usar Django REST Framework para implementar relaciones con hiperenlaces en tu API?

- [ ] Usar los campos de serializador `HyperlinkedIdentityField` o `HyperlinkedRelatedField`.
- [ ] Establecer los atributos `lookup_field` y `lookup_url_kwarg` en el ViewSet.
- [ ] Usar la clase `HyperlinkedModelSerializer`.
- [x] Todas las anteriores

#### P270. ¿Cuál es el propósito del atributo `throttle_scope` en un ViewSet de Django REST Framework?

- [ ] Especifica el nombre del ámbito de throttling a aplicar al ViewSet.
- [ ] Determina las clases de autenticación a usar para el ViewSet.
- [x] Establece el ordenamiento predeterminado del queryset.
- [ ] Filtra el queryset basado en el ámbito de throttling especificado.

#### P271. ¿Cómo puedes usar Django REST Framework para implementar lógica de paginación personalizada en tu API?

- [ ] Crear una clase de paginación personalizada que herede de la clase `BasePagination`.
- [ ] Sobrescribir los métodos `paginate_queryset()` y `get_paginated_response()` en la clase de paginación personalizada.
- [ ] Aplicar la clase de paginación personalizada al ViewSet o vista.
- [x] Todas las anteriores

#### P272. ¿Cuál es el propósito del atributo `filter_backends` en un ViewSet de Django REST Framework?

- [ ] Especifica el serializador a usar para las operaciones de crear, actualizar y eliminar del ViewSet.
- [ ] Determina las clases de autenticación a usar para el ViewSet.
- [x] Especifica los backends de filtro a usar para el queryset del ViewSet.
- [ ] Establece el ordenamiento predeterminado del queryset.

#### P273. ¿Cómo puedes usar Django REST Framework para implementar autenticación basada en tokens con JWT (JSON Web Tokens)?

- [ ] Usar la clase `JSONWebTokenAuthentication` proporcionada por el paquete `rest_framework_jwt`.
- [ ] Implementar un backend de autenticación personalizado que genere y verifique tokens JWT.
- [ ] Configurar las configuraciones `JWT_AUTH` en el archivo settings.py de tu proyecto Django.
- [x] Todas las anteriores

#### P274. ¿Cuál es el propósito del atributo `throttle_scope` en un `GenericAPIView` de Django REST Framework?

- [ ] Especifica el nombre del ámbito de throttling a aplicar a la vista.
- [ ] Determina las clases de autenticación a usar para la vista.
- [x] Establece el ordenamiento predeterminado del queryset.
- [ ] Filtra el queryset basado en el ámbito de throttling especificado.

#### P275. ¿Cómo puedes usar Django REST Framework para implementar autenticación OAuth2 en tu API?

- [ ] Usar la clase `OAuth2Authentication` proporcionada por el paquete `django-oauth-toolkit`.
- [ ] Configurar las configuraciones OAuth2 en el archivo settings.py de tu proyecto Django.
- [ ] Implementar un proveedor OAuth2 personalizado que se integre con tu aplicación.
- [x] Todas las anteriores

#### P276. ¿Cuál es el propósito del atributo `permission_classes` en un `GenericAPIView` de Django REST Framework?

- [ ] Especifica las clases de autenticación a usar para la vista.
- [ ] Establece el ordenamiento predeterminado del queryset.
- [x] Determina las clases de permisos que se aplicarán a la vista.
- [ ] Filtra el queryset basado en los permisos especificados.

#### P277. ¿Cómo puedes usar Django REST Framework para implementar CORS (Cross-Origin Resource Sharing) en tu API?

- [ ] Usar el paquete `django-cors-headers` y configurar las configuraciones CORS en el archivo settings.py de tu proyecto Django.
- [ ] Implementar un middleware CORS personalizado que verifique y modifique los encabezados de respuesta.
- [ ] Usar la clase `CorsMiddleware` proporcionada por el paquete `django-cors-headers`.
- [x] Todas las anteriores

#### P278. ¿Cuál es el propósito del atributo `renderer_classes` en un `GenericAPIView` de Django REST Framework?

- [ ] Especifica el serializador a usar para las operaciones de crear, actualizar y eliminar de la vista.
- [ ] Determina las clases de autenticación a usar para la vista.
- [x] Especifica los renderizadores a usar para las respuestas de la vista.
- [ ] Establece el ordenamiento predeterminado del queryset.

#### P279. ¿Cómo puedes usar Django REST Framework para implementar subidas de archivos en tu API?

- [ ] Usar los campos de serializador `FileField` o `ImageField`.
- [ ] Manejar las subidas de archivos en los métodos `create()` o `update()` de la vista.
- [ ] Configurar las configuraciones de almacenamiento de archivos multimedia en el archivo settings.py de tu proyecto Django.
- [x] Todas las anteriores

#### P280. ¿Cuál es el propósito del atributo `lookup_field` en un `GenericAPIView` de Django REST Framework?

- [x] Especifica el campo utilizado para buscar el objeto en la base de datos.
- [ ] Establece el ordenamiento predeterminado del queryset.
- [ ] Determina el parámetro de URL utilizado para recuperar el objeto.
- [ ] Filtra el queryset basado en el campo de búsqueda.

#### P281. ¿Cómo puedes usar Django REST Framework para implementar capacidades de búsqueda y filtrado en tu API?

- [ ] Usar las clases `SearchFilter` y `FilterBackend` proporcionadas por Django REST Framework.
- [ ] Implementar backends de filtro y búsqueda personalizados y aplicarlos al ViewSet o vista.
- [ ] Usar el paquete `django-filter` para definir campos filtrables y clases FilterSet.
- [x] Todas las anteriores

#### P282. ¿Cuál es el propósito del atributo `throttle_scope` en un ViewSet de Django REST Framework?

- [x] Especifica el nombre del ámbito de throttling a aplicar al ViewSet.
- [ ] Determina las clases de autenticación a usar para el ViewSet.
- [ ] Establece el ordenamiento predeterminado del queryset.
- [ ] Filtra el queryset basado en el ámbito de throttling especificado.

#### P283. ¿Cómo puedes usar Django REST Framework para implementar serializadores anidados en tu API?

- [ ] Usar los campos de serializador `PrimaryKeyRelatedField` o `SlugRelatedField`.
- [ ] Definir clases serializadoras para los modelos anidados y usarlas como campos en el serializador padre.
- [ ] Establecer el parámetro `depth` en la clase `Meta` del serializador.
- [x] Todas las anteriores

#### P284. ¿Cuál es el propósito del atributo `authentication_classes` en un ViewSet de Django REST Framework?

- [x] Especifica las clases de autenticación a usar para el ViewSet.
- [ ] Determina las clases de permisos que se aplicarán al ViewSet.
- [ ] Establece el ordenamiento predeterminado del queryset.
- [ ] Filtra el queryset basado en las clases de autenticación especificadas.

#### P285. ¿Cómo puedes usar Django REST Framework para implementar throttling personalizado en tu API?

- [ ] Crear una clase de throttling personalizada que herede de la clase `BaseThrottle`.
- [ ] Sobrescribir los métodos `allow_request()` y `wait()` en la clase de throttling personalizada.
- [ ] Aplicar la clase de throttling personalizada al ViewSet o vista.
- [x] Todas las anteriores

#### P286. ¿Cuál es el propósito del atributo `filter_backends` en un `GenericAPIView` de Django REST Framework?

- [ ] Especifica el serializador a usar para las operaciones de crear, actualizar y eliminar de la vista.
- [ ] Determina las clases de autenticación a usar para la vista.
- [x] Especifica los backends de filtro a usar para el queryset de la vista.
- [ ] Establece el ordenamiento predeterminado del queryset.

#### P287. ¿Cómo puedes usar Django REST Framework para implementar caché en las respuestas de tu API?

- [ ] Usar la clase `CacheResponseMixin` proporcionada por Django REST Framework.
- [ ] Establecer el encabezado `Cache-Control` en la respuesta.
- [ ] Implementar un backend de caché personalizado y aplicarlo al ViewSet o vista.
- [x] Todas las anteriores

#### P288. ¿Cuál es el propósito del atributo `authentication_classes` en un `GenericAPIView` de Django REST Framework?

- [x] Especifica las clases de autenticación a usar para la vista.
- [ ] Determina las clases de permisos que se aplicarán a la vista.
- [ ] Establece el ordenamiento predeterminado del queryset.
- [ ] Filtra el queryset basado en las clases de autenticación especificadas.

#### P289. ¿Cómo puedes usar Django REST Framework para implementar versionado en tu API?

- [ ] Usar las clases `NamespaceVersioning`, `URLPathVersioning` o `AcceptHeaderVersioning`.
- [ ] Implementar un esquema de versionado personalizado y aplicarlo al ViewSet o vista.
- [ ] Establecer el atributo `versioning_class` en el ViewSet o vista.
- [x] Todas las anteriores

#### P290. ¿Cuál es el propósito del atributo `lookup_url_kwarg` en un `GenericAPIView` de Django REST Framework?

- [x] Determina el nombre del parámetro de URL utilizado para buscar el objeto.
- [ ] Establece el ordenamiento predeterminado del queryset.
- [ ] Especifica el parámetro de URL utilizado para recuperar el objeto.
- [ ] Filtra el queryset basado en el campo de búsqueda.

#### P291. ¿Cómo puedes usar Django REST Framework para implementar paginación en las respuestas de tu API?

- [ ] Usar las clases `LimitOffsetPagination` o `PageNumberPagination`.
- [ ] Implementar una clase de paginación personalizada y aplicarla al ViewSet o vista.
- [ ] Establecer el atributo `pagination_class` en el ViewSet o vista.
- [x] Todas las anteriores

#### P292. ¿Cuál es el propósito del atributo `throttle_classes` en un `GenericAPIView` de Django REST Framework?

- [x] Especifica las clases de throttling a aplicar a la vista.
- [ ] Determina las clases de autenticación a usar para la vista.
- [ ] Establece el ordenamiento predeterminado del queryset.
- [ ] Limita la tasa a la que los clientes pueden hacer solicitudes a la vista.

#### P293. ¿Cómo puedes usar Django REST Framework para implementar control de acceso basado en roles (RBAC) en tu API?

- [ ] Crear clases de permisos personalizadas que verifiquen el rol o la membresía de grupo del usuario.
- [ ] Usar la clase de permisos `IsAdminUser` para restringir el acceso a usuarios administradores.
- [ ] Implementar un backend de autenticación personalizado que recupere el rol del usuario de una fuente externa.
- [x] Todas las anteriores

#### P294. (Pregunta incompleta en el original)

#### P301. ¿Qué característica del Admin de Django te permite personalizar la visualización de lista de un modelo?

- [ ] Acciones de admin
- [x] Visualización de lista
- [ ] Fieldsets
- [ ] Modelos en línea

#### P302. ¿Cuál es el propósito de usar acciones de admin en Django?

- [ ] Para personalizar la interfaz de administración
- [ ] Para agregar funcionalidad personalizada al admin
- [x] Para realizar operaciones masivas en objetos seleccionados
- [ ] Para filtrar la vista de lista del admin

#### P303. ¿Cómo puedes agregar un filtro personalizado a la interfaz del Admin de Django?

- [ ] Sobrescribiendo el método `get_queryset()`
- [ ] Creando una clase `FieldListFilter` personalizada
- [x] Definiendo un atributo `list_filter` en la clase admin
- [ ] Agregando un campo `filter_horizontal` a la clase admin

#### P304. ¿Cuál es el propósito de usar modelos en línea en el Admin de Django?

- [ ] Para agregar funcionalidad personalizada al admin
- [ ] Para filtrar la vista de lista del admin
- [x] Para mostrar objetos relacionados en línea en la página del admin
- [ ] Para realizar operaciones masivas en objetos seleccionados

#### P305. ¿Cómo puedes personalizar el diseño del formulario de cambio del Admin de Django?

- [ ] Usando el atributo `list_display`
- [ ] Creando una clase `FieldListFilter` personalizada
- [ ] Definiendo un atributo `list_filter` en la clase admin
- [x] Usando el atributo `fieldsets` en la clase admin

#### P306. ¿Qué característica del Admin de Django te permite agregar acciones personalizadas a la vista de lista del admin?

- [ ] Visualización de lista
- [x] Acciones de admin
- [ ] Modelos en línea
- [ ] Fieldsets

#### P307. ¿Cómo puedes agregar un campo de búsqueda personalizado a la interfaz del Admin de Django?

- [ ] Usando el atributo `list_display`
- [x] Definiendo un atributo `search_fields` en la clase admin
- [ ] Creando una clase `FieldListFilter` personalizada
- [ ] Usando el atributo `fieldsets` en la clase admin

#### P308. ¿Cuál es el propósito de usar una clase `ModelAdmin` en el Admin de Django?

- [ ] Para personalizar la interfaz de administración
- [ ] Para agregar funcionalidad personalizada al admin
- [ ] Para realizar operaciones masivas en objetos seleccionados
- [x] Para configurar el comportamiento de un modelo en el admin

#### P309. ¿Cómo puedes agregar un formulario personalizado al formulario de cambio del Admin de Django?

- [ ] Usando el atributo `list_display`
- [ ] Definiendo un atributo `search_fields` en la clase admin
- [x] Sobrescribiendo el método `get_form()` en la clase admin
- [ ] Usando el atributo `fieldsets` en la clase admin

#### P310. ¿Cuál es el propósito de usar clases `InlineModelAdmin` en el Admin de Django?

- [ ] Para agregar funcionalidad personalizada al admin
- [ ] Para filtrar la vista de lista del admin
- [x] Para mostrar objetos relacionados en línea en la página del admin
- [ ] Para realizar operaciones masivas en objetos seleccionados

#### P311. ¿Cómo puedes personalizar las acciones disponibles en el Admin de Django?

- [ ] Usando el atributo `list_display`
- [ ] Definiendo un atributo `search_fields` en la clase admin
- [x] Sobrescribiendo el método `get_actions()` en la clase admin
- [ ] Usando el atributo `fieldsets` en la clase admin

#### P312. ¿Cuál es el propósito de usar un `FieldListFilter` en el Admin de Django?

- [ ] Para personalizar la interfaz de administración
- [x] Para agregar opciones de filtrado personalizadas a la vista de lista del admin
- [ ] Para mostrar objetos relacionados en línea en la página del admin
- [ ] Para realizar operaciones masivas en objetos seleccionados

#### P313. ¿Cómo puedes agregar una vista de admin personalizada en el Admin de Django?

- [ ] Usando el atributo `list_display`
- [ ] Definiendo un atributo `search_fields` en la clase admin
- [x] Creando una vista de admin personalizada y registrándola con el sitio admin
- [ ] Usando el atributo `fieldsets` en la clase admin

#### P314. ¿Cuál es el propósito de usar un `ModelChoiceField` en un formulario del Admin de Django?

- [ ] Para agregar funcionalidad personalizada al admin
- [ ] Para filtrar la vista de lista del admin
- [x] Para permitir al usuario elegir de una lista de instancias de modelo relacionadas
- [ ] Para realizar operaciones masivas en objetos seleccionados

#### P315. ¿Cómo puedes agregar una plantilla personalizada al formulario de cambio del Admin de Django?

- [ ] Usando el atributo `list_display`
- [ ] Definiendo un atributo `search_fields` en la clase admin
- [ ] Sobrescribiendo el método `get_actions()` en la clase admin
- [x] Sobrescribiendo el atributo `change_form_template` en la clase admin

#### P316. ¿Cuál es el propósito de usar el método `get_queryset()` en una clase Admin de Django?

- [ ] Para personalizar la interfaz de administración
- [ ] Para agregar funcionalidad personalizada al admin
- [x] Para modificar el queryset utilizado para mostrar objetos en la vista de lista del admin
- [ ] Para realizar operaciones masivas en objetos seleccionados

#### P317. ¿Cómo puedes agregar funcionalidad personalizada a la vista de eliminación del Admin de Django?

- [ ] Usando el atributo `list_display`
- [ ] Definiendo un atributo `search_fields` en la clase admin
- [x] Sobrescribiendo el método `delete_view()` en la clase admin
- [ ] Usando el atributo `fieldsets` en la clase admin

#### P318. ¿Cuál es el propósito de usar el método `get_form()` en una clase Admin de Django?

- [ ] Para personalizar la interfaz de administración
- [x] Para modificar el formulario utilizado en el formulario de cambio del admin
- [ ] Para filtrar la vista de lista del admin
- [ ] Para realizar operaciones masivas en objetos seleccionados

#### P319. ¿Cómo puedes agregar validación personalizada al formulario de cambio del Admin de Django?

- [ ] Usando el atributo `list_display`
- [ ] Definiendo un atributo `search_fields` en la clase admin
- [x] Sobrescribiendo el método `clean()` en el formulario del admin
- [ ] Usando el atributo `fieldsets` en la clase admin

#### P320. ¿Cuál es el propósito de usar el método `get_urls()` en una clase Admin de Django?

- [ ] Para personalizar la interfaz de administración
- [x] Para agregar vistas y URLs de admin personalizadas
- [ ] Para filtrar la vista de lista del admin
- [ ] Para realizar operaciones masivas en objetos seleccionados

#### P321. ¿Cómo puedes agregar un botón personalizado al formulario de cambio del Admin de Django?

- [ ] Usando el atributo `list_display`
- [ ] Definiendo un atributo `search_fields` en la clase admin
- [x] Agregando una plantilla personalizada y sobrescribiendo el atributo `change_form_template`
- [ ] Usando el atributo `fieldsets` en la clase admin

#### P322. ¿Cuál es el propósito de usar el método `save_model()` en una clase Admin de Django?

- [ ] Para personalizar la interfaz de administración
- [x] Para realizar lógica personalizada cuando se guarda un modelo en el admin
- [ ] Para filtrar la vista de lista del admin
- [ ] Para realizar operaciones masivas en objetos seleccionados

#### P323. ¿Cómo puedes agregar una barra lateral personalizada al formulario de cambio del Admin de Django?

- [ ] Usando el atributo `list_display`
- [ ] Definiendo un atributo `search_fields` en la clase admin
- [x] Agregando una plantilla personalizada y sobrescribiendo el atributo `change_form_template`
- [ ] Usando el atributo `fieldsets` en la clase admin

#### P324. ¿Cuál es el propósito de usar el método `get_changeform_initial_data()` en una clase Admin de Django?

- [ ] Para personalizar la interfaz de administración
- [x] Para proporcionar datos iniciales para el formulario de cambio del admin
- [ ] Para filtrar la vista de lista del admin
- [ ] Para realizar operaciones masivas en objetos seleccionados

#### P325. ¿Cómo puedes agregar un filtro personalizado a la vista de lista del Admin de Django?

- [ ] Usando el atributo `list_display`
- [x] Creando una clase `FieldListFilter` personalizada y registrándola
- [ ] Sobrescribiendo el método `get_actions()` en la clase admin
- [ ] Usando el atributo `fieldsets` en la clase admin

#### P326. ¿Cuál es el propósito de usar el método `get_object()` en una clase Admin de Django?

- [ ] Para personalizar la interfaz de administración
- [x] Para recuperar el objeto que se está editando en el formulario de cambio del admin
- [ ] Para filtrar la vista de lista del admin
- [ ] Para realizar operaciones masivas en objetos seleccionados

#### P327. ¿Cómo puedes agregar un campo de búsqueda personalizado al formulario de cambio del Admin de Django?

- [ ] Usando el atributo `list_display`
- [ ] Definiendo un atributo `search_fields` en la clase admin
- [x] Sobrescribiendo el método `get_search_fields()` en la clase admin
- [ ] Usando el atributo `fieldsets` en la clase admin

#### P328. ¿Cuál es el propósito de usar el método `has_add_permission()` en una clase Admin de Django?

- [ ] Para personalizar la interfaz de administración
- [x] Para controlar si los usuarios pueden agregar nuevos objetos en el admin
- [ ] Para filtrar la vista de lista del admin
- [ ] Para realizar operaciones masivas en objetos seleccionados

#### P329. ¿Cómo puedes agregar una breadcrumb personalizada al formulario de cambio del Admin de Django?

- [ ] Usando el atributo `list_display`
- [ ] Definiendo un atributo `search_fields` en la clase admin
- [x] Sobrescribiendo el `change_form_template` y agregando lógica de plantilla personalizada
- [ ] Usando el atributo `fieldsets` en la clase admin

#### P330. ¿Cuál es el propósito de usar el método `has_delete_permission()` en una clase Admin de Django?

- [ ] Para personalizar la interfaz de administración
- [x] Para controlar si los usuarios pueden eliminar objetos en el admin
- [ ] Para filtrar la vista de lista del admin
- [ ] Para realizar operaciones masivas en objetos seleccionados

#### P331. ¿Cómo puedes agregar un botón de guardar personalizado al formulario de cambio del Admin de Django?

- [ ] Usando el atributo `list_display`
- [ ] Definiendo un atributo `search_fields` en la clase admin
- [x] Sobrescribiendo el `change_form_template` y agregando lógica de plantilla personalizada
- [ ] Usando el atributo `fieldsets` en la clase admin

#### P332. ¿Cuál es el propósito de usar el método `has_view_permission()` en una clase Admin de Django?

- [ ] Para personalizar la interfaz de administración
- [x] Para controlar si los usuarios pueden ver objetos en el admin
- [ ] Para filtrar la vista de lista del admin
- [ ] Para realizar operaciones masivas en objetos seleccionados

#### P333. ¿Cómo puedes agregar una barra lateral personalizada al panel del Admin de Django?

- [ ] Usando el atributo `list_display`
- [ ] Definiendo un atributo `search_fields` en la clase admin
- [x] Sobrescribiendo el `app_index_template` y agregando lógica de plantilla personalizada
- [ ] Usando el atributo `fieldsets` en la clase admin

#### P334. ¿Cuál es el propósito de usar el método `has_change_permission()` en una clase Admin de Django?

- [ ] Para personalizar la interfaz de administración
- [x] Para controlar si los usuarios pueden cambiar objetos en el admin
- [ ] Para filtrar la vista de lista del admin
- [ ] Para realizar operaciones masivas en objetos seleccionados

#### P335. ¿Cómo puedes agregar un widget de panel personalizado al Admin de Django?

- [ ] Usando el atributo `list_display`
- [ ] Definiendo un atributo `search_fields` en la clase admin
- [x] Creando una vista de admin personalizada y registrándola con el sitio admin
- [ ] Usando el atributo `fieldsets` en la clase admin

#### P336. ¿Cuál es el propósito de usar el método `has_module_permission()` en una clase Admin de Django?

- [ ] Para personalizar la interfaz de administración
- [x] Para controlar si los usuarios pueden acceder al admin para un modelo específico
- [ ] Para filtrar la vista de lista del admin
- [ ] Para realizar operaciones masivas en objetos seleccionados

#### P337. ¿Cómo puedes agregar un menú de admin personalizado al Admin de Django?

- [ ] Usando el atributo `list_display`
- [ ] Definiendo un atributo `search_fields` en la clase admin
- [x] Sobrescribiendo el método `get_urls()` y agregando vistas de admin personalizadas
- [ ] Usando el atributo `fieldsets` en la clase admin

#### P338. ¿Cuál es el propósito de usar el método `get_fieldsets()` en una clase Admin de Django?

- [ ] Para personalizar la interfaz de administración
- [x] Para modificar los fieldsets utilizados en el formulario de cambio del admin
- [ ] Para filtrar la vista de lista del admin
- [ ] Para realizar operaciones masivas en objetos seleccionados

#### P339. ¿Cómo puedes agregar una plantilla de admin personalizada al Admin de Django?

- [ ] Usando el atributo `list_display`
- [ ] Definiendo un atributo `search_fields` en la clase admin
- [x] Sobrescribiendo el `change_form_template` u otros atributos de plantilla relevantes
- [ ] Usando el atributo `fieldsets` en la clase admin

#### P340. ¿Cuál es el propósito de usar el método `get_exclude()` en una clase Admin de Django?

- [ ] Para personalizar la interfaz de administración
- [x] Para excluir ciertos campos del formulario de cambio del admin
- [ ] Para filtrar la vista de lista del admin
- [ ] Para realizar operaciones masivas en objetos seleccionados

#### P341. ¿Cómo puedes agregar una acción personalizada a la vista de lista del Admin de Django?

- [ ] Usando el atributo `list_display`
- [ ] Definiendo un atributo `search_fields` en la clase admin
- [x] Agregando un método personalizado y registrándolo como una acción de admin
- [ ] Usando el atributo `fieldsets` en la clase admin

#### P342. ¿Cuál es el propósito de usar el método `get_readonly_fields()` en una clase Admin de Django?

- [ ] Para personalizar la interfaz de administración
- [x] Para marcar ciertos campos como de solo lectura en el formulario de cambio del admin
- [ ] Para filtrar la vista de lista del admin
- [ ] Para realizar operaciones masivas en objetos seleccionados

#### P343. ¿Cómo puedes agregar un enlace personalizado al formulario de cambio del Admin de Django?

- [ ] Usando el atributo `list_display`
- [ ] Definiendo un atributo `search_fields` en la clase admin
- [x] Sobrescribiendo el `change_form_template` y agregando lógica de plantilla personalizada
- [ ] Usando el atributo `fieldsets` en la clase admin

#### P344. ¿Cuál es el propósito de usar el método `get_list_display()` en una clase Admin de Django?

- [ ] Para personalizar la interfaz de administración
- [x] Para modificar los campos de visualización de lista en la vista de lista del admin
- [ ] Para filtrar la vista de lista del admin
- [ ] Para realizar operaciones masivas en objetos seleccionados

#### P345. ¿Cómo puedes agregar un botón personalizado a la vista de lista del Admin de Django?

- [ ] Usando el atributo `list_display`
- [ ] Definiendo un atributo `search_fields` en la clase admin
- [x] Sobrescribiendo el `change_list_template` y agregando lógica de plantilla personalizada
- [ ] Usando el atributo `fieldsets` en la clase admin

#### P346. ¿Cuál es el propósito de usar el método `get_list_filter()` en una clase Admin de Django?

- [ ] Para personalizar la interfaz de administración
- [x] Para modificar las opciones de filtro de lista en la vista de lista del admin
- [ ] Para agregar funcionalidad personalizada al admin
- [ ] Para realizar operaciones masivas en objetos seleccionados

#### P347. ¿Cómo puedes agregar una vista de admin personalizada con una plantilla personalizada?

- [ ] Usando el atributo `list_display`
- [ ] Definiendo un atributo `search_fields` en la clase admin
- [x] Creando una vista de admin personalizada y sobrescribiendo el `change_form_template`
- [ ] Usando el atributo `fieldsets` en la clase admin

#### P348. ¿Cuál es el propósito de usar el método `get_search_fields()` en una clase Admin de Django?

- [ ] Para personalizar la interfaz de administración
- [x] Para modificar los campos de búsqueda en la vista de lista del admin
- [ ] Para agregar funcionalidad personalizada al admin
- [ ] Para realizar operaciones masivas en objetos seleccionados

#### P349. ¿Cómo puedes agregar un inline personalizado al formulario de cambio del Admin de Django?

- [ ] Usando el atributo `list_display`
- [ ] Definiendo un atributo `search_fields` en la clase admin
- [x] Creando una clase `InlineModelAdmin` personalizada y registrándola con el admin
- [ ] Usando el atributo `fieldsets` en la clase admin

#### P350. ¿Cuál es el propósito de usar el método `get_queryset()` en una clase Admin de Django?

- [ ] Para personalizar la interfaz de administración
- [x] Para modificar el queryset utilizado para mostrar objetos en la vista de lista del admin
- [ ] Para agregar funcionalidad personalizada al admin
- [ ] Para realizar operaciones masivas en objetos seleccionados

#### P351. ¿Qué clase de middleware de Django es responsable de manejar la protección CSRF?

- [ ] CsrfViewMiddleware
- [x] CsrfViewMiddleware
- [ ] CSRFProtectionMiddleware
- [ ] DjangoCSRFMiddleware

#### P352. ¿Cuál es el propósito de la configuración `settings.CACHES` en Django?

- [ ] Para configurar la base de datos predeterminada utilizada por la aplicación
- [ ] Para configurar el backend de correo electrónico utilizado por la aplicación
- [x] Para configurar el backend de caché utilizado por la aplicación
- [ ] Para configurar el backend de autenticación utilizado por la aplicación

#### P353. ¿Qué tipo de campo de modelo Django debes usar para almacenar una gran cantidad de datos de texto?

- [ ] CharField
- [ ] TextField
- [x] TextField
- [ ] LargeTextField

#### P354. ¿Cómo puedes ejecutar un comando de gestión de Django desde dentro de tu código Python?

- [ ] Usando la función `os.system()`
- [ ] Usando la función `subprocess.call()`
- [x] Usando la función `call_command()`
- [ ] Usando la función `django.core.management.execute_from_command_line()`

#### P355. ¿Cuál es el propósito del método `signal.dispatch()` en Django?

- [ ] Para activar manualmente una señal
- [x] Para enviar una señal a todos los receptores registrados
- [ ] Para registrar un receptor de señales
- [ ] Para cancelar el registro de un receptor de señales

#### P356. ¿Qué decorador de función de vista de Django se usa para habilitar la protección CSRF para una vista?

- [ ] `@login_required`
- [ ] `@require_http_methods`
- [x] `@csrf_protect`
- [ ] `@ensure_csrf_cookie`

#### P357. ¿Cuál es el propósito del parámetro `content_type` en la clase `django.http.HttpResponse`?

- [ ] Para establecer la codificación de caracteres de la respuesta
- [x] Para establecer el tipo MIME de la respuesta
- [ ] Para establecer el código de estado HTTP de la respuesta
- [ ] Para establecer el encabezado content-length de la respuesta

#### P358. ¿Cuál es el propósito del decorador `@transaction.atomic()` en Django?

- [ ] Para asegurar que una función de vista se ejecute de forma asíncrona
- [x] Para asegurar que un conjunto de operaciones de base de datos se ejecute como una sola transacción
- [ ] Para asegurar que una función de vista solo sea ejecutada por un solo usuario a la vez
- [ ] Para asegurar que una función de vista solo sea ejecutada por un usuario con los permisos requeridos

#### P359. ¿Cuál es el propósito de la configuración `settings.ALLOWED_HOSTS` en Django?

- [ ] Para configurar los métodos HTTP permitidos para la aplicación
- [ ] Para configurar los tipos de archivo permitidos para subidas de archivos
- [x] Para configurar los nombres de host permitidos para la aplicación
- [ ] Para configurar las direcciones IP permitidas para la aplicación

#### P360. ¿Cómo puedes crear un comando de gestión personalizado de Django?

- [ ] Creando un módulo de Python con una función `main()`
- [ ] Creando un módulo de Python con una función `handle()`
- [x] Creando una clase de Python que herede de `django.core.management.BaseCommand`
- [ ] Creando una función de Python con el decorador `@django.core.management.command`

#### P361. ¿Cuál es el propósito de la configuración `settings.CACHES` en Django?

- [ ] Para configurar la base de datos predeterminada utilizada por la aplicación
- [ ] Para configurar el backend de correo electrónico utilizado por la aplicación
- [x] Para configurar el backend de caché utilizado por la aplicación
- [ ] Para configurar el backend de autenticación utilizado por la aplicación

#### P362. ¿Cómo puedes usar el framework de caché de Django para cachear una función de vista?

- [ ] Decorando la función de vista con el decorador `@cache_page()`
- [x] Decorando la función de vista con el decorador `@cache_page()`
- [ ] Llamando al método `cache.set()` en la función de vista
- [ ] Configurando la configuración `settings.CACHES` y llamando a `cache.get()` en la función de vista

#### P363. ¿Cuál es el propósito del método `signal.disconnect()` en Django?

- [ ] Para activar manualmente una señal
- [ ] Para enviar una señal a todos los receptores registrados
- [ ] Para registrar un receptor de señales
- [x] Para cancelar el registro de un receptor de señales

#### P364. ¿Cuál es el propósito de la configuración `settings.DEBUG` en Django?

- [ ] Para habilitar o deshabilitar la protección CSRF para la aplicación
- [x] Para habilitar o deshabilitar el modo de depuración para la aplicación
- [ ] Para habilitar o deshabilitar el caché para la aplicación
- [ ] Para habilitar o deshabilitar el registro para la aplicación

#### P365. ¿Cómo puedes usar el cliente de prueba de Django para simular un inicio de sesión de usuario?

- [ ] Llamando al método `client.login()` con las credenciales del usuario
- [ ] Estableciendo la configuración `settings.AUTH_USER_MODEL`
- [x] Llamando al método `client.force_login()` con el objeto usuario
- [ ] Estableciendo el atributo `request.user` en el caso de prueba

#### P366. ¿Cuál es el propósito de la configuración `settings.MIDDLEWARE` en Django?

- [ ] Para configurar la base de datos predeterminada utilizada por la aplicación
- [x] Para configurar las clases de middleware utilizadas por la aplicación
- [ ] Para configurar el backend de caché utilizado por la aplicación
- [ ] Para configurar el backend de autenticación utilizado por la aplicación

#### P367. ¿Cómo puedes usar el framework de caché de Django para cachear la respuesta de una función de vista?

- [ ] Decorando la función de vista con el decorador `@cache_page()`
- [x] Decorando la función de vista con el decorador `@cache_page()`
- [ ] Llamando al método `cache.set()` en la función de vista
- [ ] Configurando la configuración `settings.CACHES` y llamando a `cache.get()` en la función de vista

#### P368. ¿Cuál es el propósito de la configuración `settings.CSRF_TRUSTED_ORIGINS` en Django?

- [ ] Para configurar los nombres de host permitidos para la aplicación
- [x] Para configurar los dominios de origen confiables para la protección CSRF
- [ ] Para configurar los tipos de archivo permitidos para subidas de archivos
- [ ] Para configurar las direcciones IP permitidas para la aplicación

#### P369. ¿Cómo puedes usar el cliente de prueba de Django para simular una solicitud POST con datos de formulario?

- [ ] Llamando al método `client.post()` con los datos del formulario como un diccionario
- [ ] Estableciendo el atributo `request.POST` en el caso de prueba
- [x] Llamando al método `client.post()` con los datos del formulario como un diccionario
- [ ] Llamando al método `client.request()` con los datos del formulario como un diccionario

#### P370. ¿Cuál es el propósito de la función `django.core.mail.send_mail()`?

- [ ] Para enviar un archivo adjunto
- [ ] Para enviar un correo electrónico HTML
- [x] Para enviar un correo electrónico de texto plano
- [ ] Para enviar un correo electrónico de múltiples partes

#### P371. ¿Cómo puedes usar el decorador `@login_required` de Django para restringir el acceso a una función de vista?

- [ ] Decorando la función de vista con el decorador `@login_required`
- [x] Decorando la función de vista con el decorador `@login_required`
- [ ] Llamando al método `request.user.is_authenticated` en la función de vista
- [ ] Estableciendo la configuración `settings.LOGIN_URL`

#### P372. ¿Cuál es el propósito de la configuración `settings.STATIC_ROOT` en Django?

- [ ] Para configurar el directorio desde el que se sirven los archivos estáticos
- [x] Para configurar el directorio donde se recopilan los archivos estáticos para el despliegue
- [ ] Para configurar el directorio donde se almacenan los archivos multimedia subidos
- [ ] Para configurar el directorio donde se encuentra el código de la aplicación Django

#### P373. ¿Cómo puedes usar el cliente de prueba de Django para simular un cierre de sesión de usuario?

- [ ] Llamando al método `client.logout()`
- [x] Llamando al método `client.session.flush()`
- [ ] Estableciendo el atributo `request.user` en `AnonymousUser`
- [ ] Estableciendo la configuración `settings.LOGOUT_URL`

#### P374. ¿Cuál es el propósito de la configuración `settings.EMAIL_BACKEND` en Django?

- [ ] Para configurar la base de datos predeterminada utilizada por la aplicación
- [ ] Para configurar el backend de caché utilizado por la aplicación
- [x] Para configurar el backend de correo electrónico utilizado por la aplicación
- [ ] Para configurar el backend de autenticación utilizado por la aplicación

#### P375. ¿Cómo puedes usar el cliente de prueba de Django para simular un inicio de sesión de usuario con un objeto de usuario específico?

- [ ] Llamando al método `client.login()` con las credenciales del usuario
- [ ] Estableciendo la configuración `settings.AUTH_USER_MODEL`
- [x] Llamando al método `client.force_login()` con el objeto usuario
- [ ] Estableciendo el atributo `request.user` en el caso de prueba

#### P376. ¿Cuál es el propósito de la configuración `settings.MEDIA_ROOT` en Django?

- [ ] Para configurar el directorio desde el que se sirven los archivos estáticos
- [ ] Para configurar el directorio donde se recopilan los archivos estáticos para el despliegue
- [x] Para configurar el directorio donde se almacenan los archivos multimedia subidos
- [ ] Para configurar el directorio donde se encuentra el código de la aplicación Django

#### P377. ¿Cómo puedes usar el cliente de prueba de Django para simular una solicitud GET con parámetros de consulta?

- [ ] Llamando al método `client.post()` con los parámetros de consulta como un diccionario
- [ ] Estableciendo el atributo `request.GET` en el caso de prueba
- [x] Llamando al método `client.get()` con los parámetros de consulta como un diccionario
- [ ] Llamando al método `client.request()` con los parámetros de consulta como un diccionario

#### P378. ¿Cuál es el propósito de la configuración `settings.SECRET_KEY` en Django?

- [ ] Para configurar la base de datos predeterminada utilizada por la aplicación
- [ ] Para configurar el backend de caché utilizado por la aplicación
- [ ] Para configurar el backend de correo electrónico utilizado por la aplicación
- [x] Para configurar la clave secreta utilizada para la firma criptográfica

#### P379. ¿Cómo puedes usar el cliente de prueba de Django para simular un inicio de sesión de usuario con un objeto de usuario específico?

- [ ] Llamando al método `client.login()` con las credenciales del usuario
- [ ] Estableciendo la configuración `settings.AUTH_USER_MODEL`
- [x] Llamando al método `client.force_login()` con el objeto usuario
- [ ] Estableciendo el atributo `request.user` en el caso de prueba

#### P380. ¿Cuál es el propósito de la configuración `settings.LOGGING` en Django?

- [ ] Para configurar la base de datos predeterminada utilizada por la aplicación
- [ ] Para configurar el backend de caché utilizado por la aplicación
- [x] Para configurar las configuraciones de registro para la aplicación
- [ ] Para configurar el backend de correo electrónico utilizado por la aplicación

#### P381. ¿Cómo puedes usar el cliente de prueba de Django para simular una solicitud POST con datos de archivo?

- [ ] Llamando al método `client.post()` con los datos del archivo como un diccionario
- [ ] Estableciendo el atributo `request.FILES` en el caso de prueba
- [x] Llamando al método `client.post()` con los datos del archivo como un diccionario
- [ ] Llamando al método `client.request()` con los datos del archivo como un diccionario

#### P382. ¿Cuál es el propósito de la configuración `settings.SECURE_BROWSER_XSS_FILTER` en Django?

- [ ] Para configurar los nombres de host permitidos para la aplicación
- [ ] Para configurar los dominios de origen confiables para la protección CSRF
- [x] Para habilitar el encabezado HTTP X-XSS-Protection para protección contra cross-site scripting
- [ ] Para configurar los tipos de archivo permitidos para subidas de archivos

#### P383. ¿Cómo puedes usar el cliente de prueba de Django para simular un cierre de sesión de usuario?

- [ ] Llamando al método `client.logout()`
- [x] Llamando al método `client.session.flush()`
- [ ] Estableciendo el atributo `request.user` en `AnonymousUser`
- [ ] Estableciendo la configuración `settings.LOGOUT_URL`

#### P384. ¿Cuál es el propósito de la configuración `settings.SECURE_SSL_REDIRECT` en Django?

- [ ] Para configurar los nombres de host permitidos para la aplicación
- [x] Para habilitar la redirección HTTPS para la aplicación
- [ ] Para configurar los dominios de origen confiables para la protección CSRF
- [ ] Para configurar los tipos de archivo permitidos para subidas de archivos

#### P385. ¿Cómo puedes usar el cliente de prueba de Django para simular una solicitud GET con parámetros de consulta?

- [ ] Llamando al método `client.post()` con los parámetros de consulta como un diccionario
- [ ] Estableciendo el atributo `request.GET` en el caso de prueba
- [x] Llamando al método `client.get()` con los parámetros de consulta como un diccionario
- [ ] Llamando al método `client.request()` con los parámetros de consulta como un diccionario

#### P386. ¿Cuál es el propósito de la configuración `settings.SECURE_HSTS_SECONDS` en Django?

- [ ] Para configurar los nombres de host permitidos para la aplicación
- [x] Para habilitar el encabezado HTTP Strict Transport Security (HSTS)
- [ ] Para configurar los dominios de origen confiables para la protección CSRF
- [ ] Para configurar los tipos de archivo permitidos para subidas de archivos

#### P387. ¿Cómo puedes usar el cliente de prueba de Django para simular una solicitud POST con datos de archivo?

- [ ] Llamando al método `client.post()` con los datos del archivo como un diccionario
- [ ] Estableciendo el atributo `request.FILES` en el caso de prueba
- [x] Llamando al método `client.post()` con los datos del archivo como un diccionario
- [ ] Llamando al método `client.request()` con los datos del archivo como un diccionario

#### P388. ¿Cuál es el propósito de la configuración `settings.SECURE_REFERRER_POLICY` en Django?

- [ ] Para configurar los nombres de host permitidos para la aplicación
- [ ] Para habilitar el encabezado HTTP Strict Transport Security (HSTS)
- [x] Para configurar el encabezado HTTP Referrer-Policy para la aplicación de política de referente
- [ ] Para configurar los tipos de archivo permitidos para subidas de archivos

#### P389. ¿Cómo puedes usar el cliente de prueba de Django para simular una solicitud POST con datos de formulario?

- [ ] Llamando al método `client.post()` con los datos del formulario como un diccionario
- [ ] Estableciendo el atributo `request.POST` en el caso de prueba
- [x] Llamando al método `client.post()` con los datos del formulario como un diccionario
- [ ] Llamando al método `client.request()` con los datos del formulario como un diccionario

#### P390. ¿Cuál es el propósito de la configuración `settings.STATIC_URL` en Django?

- [ ] Para configurar el directorio desde el que se sirven los archivos estáticos
- [ ] Para configurar el directorio donde se recopilan los archivos estáticos para el despliegue
- [x] Para configurar el prefijo de URL para servir archivos estáticos
- [ ] Para configurar el directorio donde se almacenan los archivos multimedia subidos

#### P391. ¿Cómo puedes usar el cliente de prueba de Django para simular un inicio de sesión de usuario con un objeto de usuario específico?

- [ ] Llamando al método `client.login()` con las credenciales del usuario
- [ ] Estableciendo la configuración `settings.AUTH_USER_MODEL`
- [x] Llamando al método `client.force_login()` con el objeto usuario
- [ ] Estableciendo el atributo `request.user` en el caso de prueba

#### P392. ¿Cuál es el propósito de la configuración `settings.MEDIA_URL` en Django?

- [ ] Para configurar el directorio desde el que se sirven los archivos estáticos
- [ ] Para configurar el directorio donde se recopilan los archivos estáticos para el despliegue
- [x] Para configurar el prefijo de URL para servir archivos multimedia
- [ ] Para configurar el directorio donde se almacenan los archivos multimedia subidos

#### P393. ¿Cómo puedes usar el cliente de prueba de Django para simular un cierre de sesión de usuario?

- [ ] Llamando al método `client.logout()`
- [x] Llamando al método `client.session.flush()`
- [ ] Estableciendo el atributo `request.user` en `AnonymousUser`
- [ ] Estableciendo la configuración `settings.LOGOUT_URL`

#### P394. ¿Cuál es el propósito de la configuración `settings.CSRF_COOKIE_SECURE` en Django?

- [ ] Para configurar los nombres de host permitidos para la aplicación
- [x] Para habilitar la bandera secure para la cookie CSRF
- [ ] Para configurar los dominios de origen confiables para la protección CSRF
- [ ] Para configurar los tipos de archivo permitidos para subidas de archivos

#### P395. ¿Cómo puedes usar el cliente de prueba de Django para simular una solicitud GET con parámetros de consulta?

- [ ] Llamando al método `client.post()` con los parámetros de consulta como un diccionario
- [ ] Estableciendo el atributo `request.GET` en el caso de prueba
- [x] Llamando al método `client.get()` con los parámetros de consulta como un diccionario
- [ ] Llamando al método `client.request()` con los parámetros de consulta como un diccionario

#### P396. ¿Cuál es el propósito de la configuración `settings.CSRF_COOKIE_HTTPONLY` en Django?

- [ ] Para configurar los nombres de host permitidos para la aplicación
- [ ] Para habilitar la bandera secure para la cookie CSRF
- [x] Para habilitar la bandera HttpOnly para la cookie CSRF
- [ ] Para configurar los dominios de origen confiables para la protección CSRF

#### P397. ¿Cómo puedes usar el cliente de prueba de Django para simular una solicitud POST con datos de archivo?

- [ ] Llamando al método `client.post()` con los datos del archivo como un diccionario
- [ ] Estableciendo el atributo `request.FILES` en el caso de prueba
- [x] Llamando al método `client.post()` con los datos del archivo como un diccionario
- [ ] Llamando al método `client.request()` con los datos del archivo como un diccionario

#### P398. ¿Cuál es el propósito de la configuración `settings.SECURE_CONTENT_TYPE_NOSNIFF` en Django?

- [ ] Para configurar los nombres de host permitidos para la aplicación
- [ ] Para habilitar la bandera secure para la cookie CSRF
- [x] Para habilitar el encabezado HTTP X-Content-Type-Options para prevenir el olfateo de tipo MIME
- [ ] Para configurar los tipos de archivo permitidos para subidas de archivos
