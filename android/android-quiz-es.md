## Androide

#### P1. Para agregar características, componentes y permisos a tu aplicación de Android, ¿qué archivo debe editarse?

- \[x] AndroidManifest.xml
- \[ ] Componentes.xml
- \[ ] AppManifest.xml
- \[ ] ComponentManifest.xml

#### P2. ¿Qué atributo XML se debe utilizar para que una vista de imagen sea accesible?

- \[ ] android:talkBack
- \[ ] androide:labelFor
- \[ ] androide:sugerencia
- \[x] android:contentDescription

#### P3. Inicias tu aplicación y cuando navegas a una nueva pantalla se bloquea, ¿qué acción NO te ayudará a diagnosticar el problema?

- \[ ] Establezca puntos de interrupción y, a continuación, recorra el código línea por línea
- \[ ] Utilice las herramientas de generador de perfiles en Android Studio para detectar anomalías en la CPU y el uso de la red.
- \[x] Agregue una llamada Thread.sleep() antes de iniciar la nueva actividad.
- \[ ] inspeccionar los registros en Logcat.

#### P4. ¿Por qué las notificaciones push podrían dejar de funcionar?

- \[x] todas estas respuestas
- \[ ] El token del dispositivo no se está enviando correctamente al proveedor de inserción.
- \[ ] Google Play Services no está instalado en el deivce/emulador.
- \[ ] La optimización de la batería está activada en el dispositivo.

#### P5. ¿Cuál es el conjunto correcto de clases de componentes necesarias para implementar una RecyclerView de elementos que muestra una lista de widgets verticalmente?

- \[ ]

```java
  RecycleView
  RecyclerView.Adapter<T extends BaseAdapter>
  RecyclerView.ViewHolder<T extends BaseViewHolder>
  LinearLayoutManager
```

- \[ ]

```java
  RecycleView
  RecyclerView.Adapter
  RecyclerView.ViewHolder<T extends BaseViewHolder>
  LinearLayoutManager
```

- \[ ]

```java
  RecycleView
  RecyclerView.Adapter
  RecyclerView.ViewHolder
  LinearLayoutManager
```

- \[x]

```java
  RecycleView
  RecyclerView.Adapter<VH extends ViewHolder>
  RecyclerView.ViewHolder
  LinearLayoutManager
```

#### P6. El sistema Android mata el proceso cuando necesita liberar memoria. La probabilidad de que el sistema mate un proceso dado depende del estado del proceso y de la actividad en ese momento. ¿Con la combinación de proceso y estado de actividad es más probable que sea asesinado?

- \[x] Proceso: En segundo plano; Actividad:Está detenida
- \[ ] Proceso:En segundo plano; Actividad:Está en pausa
- \[ ] Proceso:En primer plano; Actividad:Se ha iniciado
- \[ ] Proceso:En primer plano; Actividad:Está en pausa

#### P7. Ha creado una clase NextActivity que se basa en una cadena que contiene algunos datos que pasan dentro de la intención ¿Qué fragmento de código le permite iniciar su actividad?

- \[ ]

```java
  Intent(this, NextActivity::class.java).also { intent ->
      startActivity(intent)
  }
```

- \[ ]

```java
  Intent(this, NextActivity::class.java).apply {
      put(EXTRA_NEXT, "some data")
  }.also { intent ->
      activityStart(intent)
  }
```

- \[x]

```java
  Intent(this, NextActivity::class.java).apply {
      putExtra(EXTRA_NEXT, "some data")
  }.also { intent ->
      startActivity(intent)
  }
```

- \[ ]

```java
  Intent(this, NextActivity::class.java).apply {
      put(EXTRA_NEXT, "some data")
  }.also { intent ->
      activityStart(intent)
  }
```

#### P8. Desea incluir módulos acerca de y de configuración en el proyecto. ¿Qué archivos reflejan con precisión su inclusión?

- \[ ] en build.gradle:include ':app',':about' ':settings'
- \[x] en settings.gradle:include ':app',':about' ':settings'
- \[ ] en settings.gradle:include ':about',':settings'
- \[ ] en gradle.properties:include ':app',':about' ':settings'

#### P9. ¿Cuál es el beneficio de usar @VisibleForTesting anotación?

- \[x] para denotar que una clase, metos o campo tiene su visibilidad relajada para que el código sea comprobable
- \[ ] para indicar que una clase, método o campo sólo es visible en el código de prueba
- \[ ] para denotar que una clase, método o campo tiene su visibilidad aumentada para que el código sea menos comprobable
- \[ ] para generar un error en tiempo de ejecución si se accede incorrectamente a una clase, metos o campo con esta anotación

#### P10. ¿Cómo especificaría en el archivo build.gradle que la aplicación requería al menos el nivel de API 21 para ejecutarse, pero que se puede probar en el nivel de API 28?

- \[ ]

```
  defaultConfig {
    ...
    minApiVersion 21
    targetApiVersion 28
  }
```

- \[ ]

```
  defaultConfig {
    ...
    targetSdkVersion 21
    testSdkVersion 28
  }
```

- \[ ]

```
  defaultConfig {
    ...
    minSdkVersion 21
    testApiVersion 28
  }
```

- \[x]

```
  defaultConfig {
    ...
  minSdkVersion 21
    targetSdkVersion 28
  }
```

#### P11. ¿Cuándo se llamará a onActivityResult() de una actividad?

- \[ ] al llamar a finish()en la actividad principal
- \[ ] al colocar una aplicación en segundo plano al vincularla a otra aplicación
- \[ ] Cuando se llama a onStop() en la actividad objetivo
- \[x] al llamar a finish() en la actividad de destino

[Para más información](https://developer.android.com/reference/android/app/Activity)

#### P12. Debe eliminar un evento basado en su identificador de su API, ¿Qué fragmento de código define esa solicitud en Retrofit?

- \[ ] @DELETE("eventos))
  fun deleteEvent(@Path("id") id: Long): Llamar<Unit>
- \[x] @DELETE("events/{id}")
  fun deleteEvent(@Path("id") id: Long): Llamar<Unit>
- \[ ] @REMOVE("events/{id}")
  fun deleteEvent(@Path("id") id: Long): Llamar<Unit>
- \[x] @DELETE("events/{id}")
  fun deleteEvent(@Path("id") id: Long): Llamar<Unit>

#### P13. ¿Cuándo usaría un sabor de producto en su configuración de construcción?

- \[ ] cuando necesite tener las cadenas de la aplicación presentes en varios lanuages
- \[ ] cuando tiene que proporcionar diferentes versiones de la aplicación en función del tamaño del dispositivo físico
- \[ ] cuando desee proporcionar diferentes versiones de la aplicación en función de la densidad de la pantalla del dispositivo
- \[x] cuando desee proporcionar una versión diferente de la aplicación con configuración y recursos personalizados

#### P14. Dado el fragmento siguiente, ¿cómo obtendría acceso a un TextView con un ID de text_home contenido en el archivo de diseño de una clase Fragment?

```java
  private lateinit var textView: TextView
  override fun onCreateView(...): View? {
      val root = inflator.inflator(R>layout.fragment_home, container, false)
      textView = ??
      return root
  }
```

- \[ ] root.getById(R.id.text_home)
- \[ ] findViewByID(R.id.text_home)
- \[x] root.findViewById(R.id.text_home)
- \[ ] root.find(R.id.text_home)

#### P15. ¿Por qué usas AndroidJUnitRunner cuando ejecutas pruebas de interfaz de usuario?

Aviso: AndroidJUnitRunner nos permite ejecutar pruebas de estilo JUnit3/4 en dispositivos Android

- \[x] El ejecutor de pruebas facilita la carga del paquete de prueba y la aplicación en prueba en un dispositivo o emulador, ejecuta la prueba e informa de los resultados.
- \[ ] El ejecutor de pruebas crea capturas de pantalla de cada pantalla que se muestra mientras se ejecutan las pruebas.
- \[ ] El ejecutor de la prueba facilita la paralelización de las clases de prueba al proporcionar para cada clase de prueba.
- \[ ] El ejecutor de la prueba facilita la interacción con elementos visibles en un dispositivo, independientemente de la actividad o fragmento que tenga foco.

#### P16. ¿Qué le permite restaurar correctamente el estado de un usuario cuando se reinicia una actividad?

- \[ ] el método onSaveInstance()
- \[x] todas estas respuestas
- \[ ] almacenamiento persistente
- \[ ] Objetos ViewModel

[Refrencia](https://developer.android.com/topic/libraries/architecture/saving-states)

#### P17. Dada la definición a continuación. ¿Cómo se obtendría acceso a un TextView con un ID de text_home contenido en el archivo de diseño thr de una clase Fragment?

- \[ ] root.find(R.id.text_home)
- \[ ] findViewById(R.id.text_home)
- \[ ] root.getById(R.id.text_home)
- \[x] root.findViewById(R.id.text_home)

#### P18. SI el subproceso principal está bloqueado durante demasiado tiempo, ¿el sistema muestra el cuadro de diálogo \_?

- \[ ] El hilo no responde
- \[ ] Aplicación en pausa
- \[x] La aplicación no responde
- \[ ] Aplicación bloqueada

#### P19. ¿Cómo recuperaría el valor del correo electrónico de un usuario de SharedPreferences mientras se asegura de que el valor devuelto no sea nulo?

- \[ ] getPreferances(this).getString(Email,"")
- \[ ] getDefaultSharedPrefarances(this).getString(EMAIL,null)
- \[x] getDefaultSharedPreferances(this).getString(EMAIL,"")
- \[ ] getPreferances(this).getString(EMAIL,null)

**Explicación:** En el método "getDefaultSharedPrefarances(this).getString()" se pasa el segundo parámetro para que se pueda devolver, en caso de que la clave no exista. Por lo tanto, debemos pasar una cadena vacía para devolverla en caso de que la clave no exista.

#### P20. ¿Por qué es problemático definir tamaños usando píxeles en Android?

- \[ ] Aunque la densidad de píxeles de la pantalla varía, esto no afecta el uso de píxeles para definir tamaños.
- \[ ] Los dispositivos grandes siempre tienen más píxeles, por lo que los elementos de la interfaz de usuario se verán afectados si los define con píxeles.
- \[x] El mismo número de píxeles puede corresponder a diferentes tamaños físicos, lo que afecta a la apariencia de los elementos de la interfaz de usuario.
- \[ ] Los diferentes dispositivos tienen una comprensión diferente de lo que es un píxel, lo que afecta la apariencia de los elementos de la interfaz de usuario

[Referencia](https://developer.android.com/training/multiscreen/screendensities#:~:text=The%20first%20pitfall%20you%20must,physical%20sizes%20on%20different%20devices.)

#### P21. Debe obtener una lista de los dispositivos que están conectados a su computadora con la depuración USB habilitada. ¿Qué comando se ejecutaría usando Android Debug Bridge?

- \[ ] enumerar dispositivos
- \[x] dispositivos adb
- \[ ] lista avd
- \[ ] dispositivos dir

#### P22. ¿Qué definición dibujable le permite lograr la forma a continuación?

![img](image/shape.png?raw=png)

- \[ ]

```xml
  <shape xmlns:android="http://schemas.android.com/apk/res/android"
      android:shape="oval">
      <stroke
          android:width="4dp"
    android:color="@android:color/white" />
    <solid android:color="@android:color/black" />
  </shape>
```

- \[ ]

```xml
  <oval xmlns:android="http://schemas.android.com/apk/res/android">
      <stroke android:width="4dp" android:color="@android:color/black"/>
      <solid android:color="@android:color/white"/>
  </oval>
```

- \[x]

```xml
  <shape xmlns:android="http://schemas.android.com/apk/res/android"
      android:shape="oval">
      <stroke
          android:width="4dp"
          android:color="@android:color/black" />
      <solid android:color="@android:color/white" />
  </shape>
```

- \[ ]

```xml
  <shape xmlns:android="http://schemas.android.com/apk/res/android"
      android:shape="oval">
      <stroke
          android:width="4dp"
          android:color="@android:color/white" />
      <solid android:color="@android:color/white" />
  </shape>
```

#### P23. Para conservar una pequeña colección de datos clave-valor, ¿qué debe usar?

- \[ ] almacenamiento externo de archivos
- \[x] SharedPereferences
- \[ ] SQLite
- \[ ] almacenamiento interno de archivos

#### P24. Debe recuperar una lista de fotos de una API. ¿Qué fragmento de código define una solicitud HTML GET en Retrofit?

- \[ ] @GET("foto/{id}"}
  fun listPhotos(@Path("id") id:Long?) : Llamar<Photo>
- \[ ] @LIST("foto")
  lista divertidaFotos() : Call\<List<Photo>>
- \[ ] @GET("foto")
  fun listPhotos() : Llamar<Photo>
- \[x] @GET("foto")
  lista divertidaFotos() : Call\<List<Photo>>

#### P25. Dada la clase de prueba a continuación, ¿qué fragmento de código sería una afirmación correcta?

- \[ ] assertThat(resultAdd).is(2.0)
- \[x] assertNotNull(resultAdd)
- \[ ] assertThat(resultAdd).isWqualTo(2.0)
- \[ ] assertThat(resultAdd)

#### P26. ¿Qué etiqueta debe usar para agregar un componente de vista reutilizable a un archivo de diseño?

- \[ ] `<merge/>`
- \[x] `<include/>`
- \[ ] `<layout/>`
- \[ ] `<add/>`

#### P27. Desea proporcionar un dibujo diferente para los dispositivos que están en modo horizontal y cuyo idioma está establecido en francés. ¿Qué directorio tiene el nombre correcto?

- \[ ] fr-land-drawable
- \[x] drawable-fr-land
- \[ ] drawable-french-land
- \[ ] french-land-drawable

#### P28. ¿Por qué es posible que debas incluir el siguiente permiso en tu aplicación?

`android.permission.ACCESS_NETWORK_STATE`

- \[ ] para supervisar la ubicación de los dispositivos de modo que no intente realizar llamadas de red cuando el usuario está parado
- \[ ] para solicitar la capacidad de realizar llamadas de red desde la aplicación
- \[ ] para supervisar el estado de red del dispositivo de modo que pueda mostrar un banner en la aplicación al usuario
- \[x] para supervisar el estado de red de los dispositivos para que no intente realizar llamadas de red cuando la red no esté disponible

#### P29. Qué imagen corresponde mejor a la siguiente `LinearLayout`?

```xml
  <LinearLayout
      android:layout_width="match_parent"
      android:layout_height="match_parent"
      android:orientation="horizontal"
      android:gravity="center">
      <Button
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="Button" />
      <Button
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="Button" />
  </LinearLayout>
```

- \[ ] A
  ![img](image/00.jpeg)
- \[x] B
  ![img](image/01.jpeg)
- \[ ] C
  ![img](image/02.jpeg)
- \[ ] D
  ![img](image/03.jpeg)

#### P30. Desea abrir la aplicación Marcador predeterminada en un dispositivo. ¿Qué tiene de malo este código?

```java
  val dialerIntent = Intent()
  val et = findViewById(R.id.some_edit_text)
  dialerIntent.action = Intent.ACTION_DIAL
  dialerIntent.data = Uri.parse("tel:" + et.getText()?.toString())
  startActivity(dialerIntent)
```

- \[x] `startActivityWithResult()` debe usarse en lugar de `startActivity()` cuando se utiliza `Intent.ACTION_DIAL`.
- \[ ] Para `Intent.ACTION_DIAL`el `Intent` opción `Intent.FLAG_ACTIVITY_NEW_TASK` Debe agregarse al utilizar esto `dialerIntent`.
- \[ ] El `dialerIntent` provocará que se lance una excepción ActivityNotFoundException en dispositivos que no admiten `Intent.ACTION_DIAL`.
- \[ ] El permiso `android.permission.CALL_PHONE` debe solicitarse primero antes `Intent.ACTION_DIAL` se puede utilizar.

#### P31. ¿Cuándo debe almacenar archivos en el `/assets` ¿directorio?

- \[x] cuando necesite acceso a los nombres de archivo originales y a la jerarquía de archivos [(Referencia)](https://medium.com/mobile-app-development-publication/assets-or-resource-raw-folder-of-android-5bdc042570e0)
- \[ ] cuando necesite acceder al archivo con su `resource ID`gustar `R.assets.filename`
- \[ ] cuando tiene archivos XML que definen animaciones de interpolación
- \[ ] cuando necesite acceder al archivo en su forma sin formato utilizando `Resources.openRawResource()`

#### P32. Quieres permitir que los usuarios tomen fotografías en tu aplicación. Que es _no_ una ventaja de crear un `intent`, en lugar de solicitar el permiso de la cámara directamente?

- \[ ] Los usuarios pueden seleccionar sus aplicaciones de fotos favoritas para tomar fotos.
- \[ ] No tienes que hacer una solicitud de permiso en tu aplicación para tomar una foto.
- \[x] Usted tiene control total sobre la experiencia del usuario. La aplicación que controla la cámara `intent` respetará sus elecciones de diseño.
- \[ ] No es necesario diseñar la interfaz de usuario. La aplicación que controla la cámara `intent` proporcionará la interfaz de usuario.

#### P33. ¿Cuándo usaría el `ActivityCompat.shouldShowRequestPermissionRationale()` ¿función?

- \[ ] cuando un usuario abre la aplicación por primera vez y desea proporcionar una explicación para el uso de un permiso determinado
- \[ ] cuando un usuario ha denegado previamente la solicitud de un permiso determinado y selecciona "Cuéntame más"
- \[ ] cuando un usuario ha denegado previamente la solicitud de un permiso determinado y desea proporcionar una explicación de su uso
- \[x] cuando un usuario ha denegado previamente la solicitud de un permiso determinado y ha seleccionado "No volver a preguntar", pero necesita el permiso para que su aplicación funcione

#### P34. Desea habilitar el seguimiento analítico solo en `release` Construye. ¿Cómo se puede crear un nuevo campo en el generado? `BuildConfig` para almacenar ese valor?

- \[ ]

```
  buildTypes {
    debug {
      buildConfig 'boolean', 'ENABLE_ANALYTICS', 'false'
    }
    release {
      buildConfig 'boolean', 'ENABLE_ANALYTICS', 'true'
    }
  }
```

- \[ ]

```
  buildTypes {
    debug {
      buildConfig 'String', 'ENABLE_ANALYTICS', 'false'
    }
    release {
      buildConfig 'String', 'ENABLE_ANALYTICS', 'true'
    }
  }
```

- \[x]

```
  buildTypes {
    debug {
      buildConfigField 'boolean', 'ENABLE_ANALYTICS', 'false'
    }
    release {
      buildConfigField 'boolean', 'ENABLE_ANALYTICS', 'true'
    }
  }
```

- \[ ]

```
  buildTypes {
    debug {
      buildConfigField 'boolean', 'ENABLE_ANALYTICS', 'true'
    }
    release {
      buildConfigField 'boolean', 'ENABLE_ANALYTICS', 'false'
    }
  }
```

#### P35. Para optimizar el tamaño de tu APK, ¿qué códec de imagen debes usar?

- \[ ] JPG
- \[ ] PNG
- \[ ] MPEG
- \[x] WebP [(Referencia)](https://developer.android.com/topic/performance/reduce-apk-size#:~:text=packJPG%20and%20guetzli.-,Use%20WebP%20file%20format,than%20either%20JPEG%20or%20PNG.)

#### P36. Ha creado código para realizar una llamada de red y ha probado que funciona en su entorno de desarrollo. Sin embargo, cuando lo publicas en Play Console, la llamada de red no funciona. ¿Qué será? _no_ ayudarle a solucionar este problema?

- \[ ] comprobar si `ProGuard` -KeepClassmembers se han añadido a los objetos de transferencia de datos de red (DTO) en cuestión
- \[x] uso de las herramientas de generador de perfiles en Android Studio para detectar anomalías en el uso de la CPU, la memoria y la red
- \[ ] comprobación de excepciones en los registros del servidor o en la consola del servidor
- \[ ] comprobación de que el objeto de transferencia de datos de red tiene `@SerizlizedName` aplicado a sus propiedades miembro

#### P37. ¿Qué fragmento de código lograría el diseño que se muestra a continuación?

![img](image/04.jpeg)

- \[ ]

```xml
  <androidx.constraintlayout.widget.ConstraintLayout
  ...>

    <TextView
      android:id="@+id/text_dashboard"
      android:layout_width="match_parent"
      android:layout_height="wrap_content"
      android:layout_marginTop="16dp"
      android:padding="8dp"
      android:textAlignment="center"
      android:text="Dashboard"
      app:layout_constraintEnd_toEndOf="parent"
      app:layout_constraintStart_toStartOf="parent"
      app:layout_constraintTop_toTopOf="parent" />

  </androidx.constraintlayout.widget.ConstraintLayout>
```

- \[x]

```xml
  <androidx.constraintlayout.widget.ConstraintLayout
    	...>
    	<TextView
    		android:id="@+id/text_dashboard"
    		android:layout_width="match_parent"
    		android:layout_height="wrap_content"
    		android:layout_marginStart="8dp"
    		android:layout_marginEnd="8dp"
    		android:textAlignment="center"
    		android:text="Dashboard"
    		app:layout_constraintEnd_toEndOf="parent"
    		app:layout_constraintStart_toStartOf="parent"
    		app:layout_constraintTop_toTopOf="parent" />

  </androidx.constraintlayout.widget.ConstraintLayout>
```

- \[ ]

```xml
  <androidx.constraintlayout.widget.ConstraintLayout
    	...>

    	<TextView
    		android:id="@+id/text_dashboard"
    		android:layout_width="match_parent"
    		android:layout_height="wrap_content"
    		android:layout_marginStart="8dp"
    		android:layout_marginTop="16dp"
    		android:layout_marginEnd="8dp"
    		android:padding="8dp"
    		android:textAlignment="center"
    		android:text="Dashboard"
    		app:layout_constraintEnd_toEndOf="parent"
    		app:layout_constraintStart_toStartOf="parent"
    		app:layout_constraintTop_toTopOf="parent" />

  </androidx.constraintlayout.widget.ConstraintLayout>
```

- \[ ]

```xml
  <androidx.constraintlayout.widget.ConstraintLayout
    	...>
    	<TextView
    		android:id="@+id/text_dashboard"
    		android:layout_width="match_parent"
    		android:layout_height="wrap_content"
    		android:layout_marginStart="8dp"
    		android:layout_marginTop="16dp"
    		android:layout_marginEnd="8dp"
    		android:padding="8dp"
    		android:text="Dashboard"
    		app:layout_constraintEnd_toEndOf="parent"
    		app:layout_constraintStart_toStartOf="parent"
    	/>

  </androidx.constraintlayout.widget.ConstraintLayout>
```

#### P38. Qué conjunto de fuentes es `_not_` disponible para usted de forma predeterminada cuando Android Studio crea un nuevo proyecto?

- \[ ] prueba
- \[ ] androidTest
- \[ ] aplicación
- \[x] principal

#### P39. ¿Qué definición impedirá que otras aplicaciones accedan a su `Activity` clase a través de un `intent`?

- \[x]

```xml
  <activity android:name=".ExampleActivity" />
```

- \[ ]

```xml
  <activity android:name=".ExampleActivity">
    <intent-filter>
      <action android:name="android.intent.action.SEND" />
    </intent-filter>
  </activity>
```

- \[ ]

```xml
  <activity android:name=".ExampleActivity">
    <intent-filter>
      <action android:name="android.intent.action.MAIN" />
      <category android:name="android.intent.category.LAUNCHER" />
    </intent-filter>
  </activity>
```

- \[ ]

```xml
  <activity android:name=".ExampleActivity">
    <intent-filter>
      <action android:name="android.intent.action.VIEW" />
    </intent-filter>
  </activity>
```

**Explicación:** Los filtros de intención se usan para hacer que las actividades sean accesibles para otras aplicaciones mediante intenciones. Por lo tanto, tenemos que elegir opciones que no tengan filtro de intención para asegurarnos de que no sea accesible por intención.

#### P40. Para preservar la memoria en el dispositivo, ¿cómo podría determinar que el dispositivo del usuario tiene capacidades de almacenamiento limitadas?

- \[x] Utilice el botón `ActivityManager.isLowRamDevice()` método para averiguar si un dispositivo se define a sí mismo como "baja RAM".
- \[ ] Utilice el botón `Activity.islowRam()` método para averiguar si un dispositivo se define a sí mismo como "baja RAM".
- \[ ] Utilice el botón `ConnectivityManager.hasLowMemory()` método para averiguar si un dispositivo se define a sí mismo como "baja RAM".
- \[ ] Realice una solicitud de descarga de imágenes y compruebe el uso de almacenamiento del dispositivo restante.

#### P41. Qué es `_not_` una buena manera de reutilizar el código de Android?

- \[ ] Utilice un módulo Gradle común compartido por diferentes proyectos de Android.
- \[ ] Prefiere crear vistas o fragmentos personalizados sobre las actividades.
- \[x] Prefiere construir actividades en lugar de fragmentos.
- \[ ] Desglose los diseños de la interfaz de usuario en elementos comunes y use `<include/>` para incluirlos en otros archivos XML de diseño.

#### P42. ¿Qué diseño es mejor para jerarquías grandes y complejas?

- \[ ] LinearLayout
- \[x] ConstraintLayout
- \[ ] FrameLayout
- \[ ] RelativeLayout

#### P43. Debe actualizar a la última versión del complemento Android Gradle. ¿Qué archivo debe modificar?

- \[ ] root_project_dir/app/build.gradle.
- \[ ] root_project_dir/settings.gradle.
- \[x] root_project_dir/build.gradle.
- \[ ] root_project_dir/app/gradle.properties.

[referencia](https://developer.android.com/studio/releases/gradle-plugin#updating-plugin)

#### P44. ¿Por qué los desarrolladores suelen poner código de inicialización de aplicaciones en la clase Application?

- \[x] Se crea una instancia de la clase Application antes que cualquier otra clase cuando se crea el proceso para la aplicación.
- \[ ] La clase Application se crea una instancia después de cualquier solicitud de permisos cuando se crea el proceso para la aplicación.
- \[ ] La clase Application se crea cada vez que se inicia una nueva actividad, lo que la hace ideal para el código de inicialización.
- \[ ] La clase Application se crea cada vez que se llama a un servicio en segundo plano, lo que la hace ideal para el código de inicialización.

[referencia](https://developer.android.com/reference/android/app/Application)

#### P45. ¿Qué carpeta debes usar para los iconos del iniciador de tu aplicación?

- \[ ] /dibujable
- \[ ] /icon
- \[x] /mipmap
- \[ ] /lanzador

#### P46. ¿Qué definición dibujable le permite lograr la forma a continuación?

![img](image/43.jpeg)

- \[ ]

```xml
  <shape xmlns:android-"http://schemas.android.com/apk/res/android"
      android:shape-"oval">
      <gradient
                android:startColor-"@android:color/white"
                android:endColor-"@android:color/black"
                android:angle-"45"/>
  </shape>
```

- \[ ]

```xml
  <rectangle xmlns:android-"http://schemas.android.com/apk/res/android">
      <gradient
        android:startColor-"@android:color/white"
        android:endColor-"android:color/black"
        android:angle-"135"/>
  </rectangle>
```

- \[x]

```xml
  <shape xmlns:android-"http://schemas.android.com/apk/res/android"
      android:shape-"rectangle">
      <gradient
        android:startColor-"@android:color/white"
        android:endColor-"@android:color/black"
        android:angle-"135"/>
  </shape>
```

- \[ ]

```xml
  <shape xmlns:android-"http://schemas.android.com/apk/res/android"
      android:shape-"rectangle">
      <gradient
        android:startColor-"@android:color/white"
        android:endColor-"@android:color/black"
        android:angle-"98"/>
  </shape>
```

#### P47. Dado el ConstraintLayout a continuación, ¿qué afirmación es verdadera?

![img](image/44.jpeg)

- \[ ] La vista B no está restringida horizontalmente.
- \[ ] La vista C tiene demasiadas restricciones.
- \[x] La vista B no está restringida verticalmente.
- \[ ] La vista C está restringida al padre.

#### P48. Dado este código snippey de un archivo build.gradle, ¿qué opción no es una posible variante de compilación?

```
  android {
      ...
      defaultConfig{...}

      buildTypes{
      debug{...}
      releasae{...}
  }

    flavorDimensions "environment"
    productFlavors {
        producation {...}
        staging {...}
    }
  }
```

- \[ ] productionDebug.
- \[x] developmentDebug.
- \[ ] stagingDebug.
- \[ ] puesta en escenaRelease.

[Referencia](https://developer.android.com/studio/build/build-variants#flavor-dimensions)

#### Pregunta 49. ¿Cuándo debe usar el directorio androidTest para almacenar sus clases de prueba?

- \[ ] cuando las pruebas consistan únicamente en pruebas unitarias.
- \[ ] cuando el número de pruebas a ejecutar es grande(500+).
- \[ ] cuando las pruebas deben ejecutarse en su máquina local.
- \[x] cuando las pruebas necesitan ejecutarse en dispositivos reales o virtuales.

[Referencia](https://developer.android.com/studio/test#test_types_and_location)

#### Pregunta 50. Dado un APK llamado app-internal-debug.apk producido a partir del proceso de compilación, ¿qué afirmación es probable que sea cierta?

- \[ ] Este APK se crea en una máquina desarrolladora a partir del sabor del producto de depuración.
- \[ ] Este APK se crea a partir del sabor del producto internalDebug.
- \[ ] Este APK creado a partir del sabor del producto de depuración y el tipo de compilación interna.
- \[x] Este APK se crea a partir del tipo de compilación de depuración y el sabor interno del producto.

#### Pregunta 51. Al intentar compilar el proyecto, ¿qué podría indicar el siguiente error?

`Conversion to Dalvik format filed: Unable to execute dex: method ID not in [0, 0xffff]: 65536`

- \[ ] Ha incluido información de formato incorect en el archivo build.gradle.
- \[ ] Ha agregado más de 20 dependencias a su build.gradle.
- \[x] Ha superado el número total de métodos a los que se puede hacer referencia en un único archivo DEX.
- \[ ] Tiene una excepción NullPointerException en el código.

#### P52. ¿Qué declaración, en el archivo build.gradle, denota correctamente que el módulo correspondiente es un módulo de biblioteca de Android?

- \[ ] aplicar plugin: 'com.module.library'
- \[x] aplicar plugin: 'com.android.library'
- \[ ] aplicar plugin: 'com.module.library'
- \[ ] incluye plugin: 'com.module.library'

#### Pregunta 53. Teniendo en cuenta los siguientes dimens.xml archivo, ¿cómo definiría un ImageView con espaciado medio en la parte inferior?

```xml
<?xml version=1.0 encoding="utf-8"?>
<resources>
    <dimen name="spacing_medium">8dp</dimen>
    <dimen name="spacing_large">12dp</dimen>
</resources>
```

- \[ ]

```xml
  <ImageView
      android:id="@+id/image_map_pin"
      android:layout_width="wrap_content"
      android:layout_heignt="wrap_content"
      android:src=@drawable/map_pin />
```

- \[ ]

```xml
  <ImageView
    android:id="@+id/image_map_pin"
    android:layout_width="wrap_content"
    android:layout_heignt="wrap_content"
    androi:layout_botttom="@dimen/spacing_medium"
    android:src=@drawable/map_pin />
```

- \[ ]

```xml
  <ImageView
      android:id="@+id/image_map_pin"
      android:layout_width="wrap_content"
      android:layout_heignt="wrap_content"
      android:layout_marginBottom="@resources/spacing_medium"
      android:src=@drawable/map_pin />

- \[x]

```xml
    <ImageView
      android:id="@+id/image_map_pin"
      android:layout_width="wrap_content"
      android:layout_heignt="wrap_content"
      android:layout_marginBottom="@dimen/spacing_medium"
      android:src=@drawable/map_pin />
```

#### Pregunta 54. ¿Qué no es beneficioso de externalizar los recursos de la aplicación, como la imagen y la cadena, a partir de un código?

- \[ ] Permite a Android elegir el recurso apropiado en función de la configuración actual durante el tiempo de ejecución.
- \[x] Le permite tener aplicaciones de mayor rendimiento porque el código y los recursos están separados.
- \[ ] Le permite proporcionar una experiencia Ul diferente basada en la configuración de idioma del usuario.
- \[ ] Le permite proporcionar una experiencia Ul diferente basada en el tamaño del dispositivo del usuario.

#### Pregunta 55. ¿Cuál es el propósito principal de la línea cinco en este fragmento de código?

```java
  override fun onCreate(savedInstanceState: Bundle?) { super.onCreate(savedInstanceState) setContentView(R.layout.activity_post_create)

    if (savedInstanceState != null) return

    val fragment = CreatePostFragment()
      supportFragmentManager
      .beginTransaction()
      .add(R.id. fragment_container, fragment)
      .commit()

  }
```

- \[ ] para asegurarse de que la actividad finaliza cuando savedInstanceState no es null
- \[x] para asegurarse de que la actividad crea un nuevo fragmento cada vez que se restaura desde un estado anterior
- \[ ] para evitar la visualización de dos fragmentos uno al lado del otro en los casos en que la actividad se restaura desde un estado anterior
- \[ ] para evitar la creación de fragmentos superpuestos en los casos en que la actividad se restablezca de un estado anterior

#### Pregunta 56. ¿Qué componente no es un punto de entrada a través del cual el sistema o un usuario pueden ingresar a su aplicación?

- \[ ] actividad
- \[ ] proveedor de contenido
- \[x] fragmento
- \[ ] servicio

#### Pregunta 57. ¿Qué debe usar para mostrar una gran lista de elementos de desplazamiento?

- \[ ] ListView
- \[x] Vista del reciclador
- \[ ] LinearLayout
- \[ ] Scrollview

#### Pregunta 58. Ha creado una clase AboutActivity que muestra detalles sobre la aplicación. ¿Qué fragmento de código te permite iniciar tu actividad?

- \[ ] Intent(this, AboutActivity::class).also { intent ->
  startService(intención)
  }

- \[x] Intent(this, AboutActivity::class.java).also { intent ->
  startActivity(intención)
  }

- \[ ] Intent(this, AboutActivity::class).also { intent ->
  actividad(intención)
  }

- \[ ] Intent(this, AboutActivity::class).also { intent ->
  startActivity(intención)
  }
  Explicación: Intención(Context packageContext, Class\<?> cls)
  Aviso: Clase no KClass

#### Pregunta 59. ¿Cuál es el uso del archivo AndroidManifest.xml?

- \[x] Describe el componente de la aplicación
- \[ ] Declara el nivel mínimo de la API de Android que requiere la aplicación
- \[ ] Facilita proporcionar un nombre uinque para la aplicación especificando el nombre del paquete
- \[ ] Todo lo anterior

#### P60. Qué atributo del elemento <uses-sdk> se utiliza para especificar el nivel mínimo de API necesario para que la aplicación se ejecute?

- \[ ] android:targetSdkVersion
- \[x] android:minSdkVersion
- \[ ] android:maxSdkVersion
- \[ ] Nada de lo anterior

#### P61. Para reducir el código en las compilaciones de lanzamiento, ¿qué herramienta utiliza Android Studio?

- \[x] R8
- \[ ] ProGuard
- \[ ] Encogedor
- \[ ] D8
  Explicación: Cuando crea su proyecto utilizando el complemento Android Gradle 3.4.0 o superior, el complemento ya no utiliza ProGuard para realizar la optimización del código en tiempo de compilación. En cambio, el complemento funciona con el compilador R8 para manejar

[Referencia](https://developer.android.com/studio/build/shrink-code)

#### P62. ¿Qué jerarquía de diseño es probable que se dibuje más rápidamente?

- \[x] A
  ![img](https://i.imgur.com/mT08jag.png?raw=png)

- \[ ] B
  ![img](https://i.imgur.com/rz9eKYc.png?raw=png)

- \[ ] C
  ![img](https://i.imgur.com/ETaHhaS.png?raw=png)

- \[ ] D
  ![img](https://i.imgur.com/1QBrTwR.png?raw=png)

#### P63. ¿Cuál es la forma recomendada actual de manejar tareas en segundo plano de larga duración?

- \[x] WorkManager
- \[ ] AsyncTask
- \[ ] IntentService
- \[ ] Hilo

[Referencia](https://developer.android.com/guide/background)

#### Pregunta 64. Debe proporcionar a sus usuarios ciertas funciones de su aplicación bajo demanda o como experiencias instantáneas a través de Google Play. ¿Qué tipo de módulo debe crear?

- \[ ] módulo de biblioteca
- \[x] módulo de características dinámicas
- \[ ] Módulo de aplicación android
- \[ ] Módulo de Google Cloud

1.  [Referencia](https://youtu.be/QdfStuj-MuA?t=86)
2.  [Referencia](https://developer.android.com/guide/playcore/feature-delivery/on-demand)

#### Pregunta 65. ¿Qué enfoque no se recomienda para proporcionar un estado sin conexión útil en la aplicación?

- \[ ] datos de almacenamiento en caché
- \[ ] almacenar datos localmente
- \[ ] poner en cola las solicitudes salientes a la acción cuando se ha perdido la conectividad
- \[ ] siempre notificando a los usuarios que se ha perdido la conectividad

#### Pregunta 66. Si necesitas el código de la aplicación para inspeccionar la información sobre la compilación actual, ¿qué clase debes usar?

- \[x] `BuildConfig`
- \[ ] `BuildInfo`
- \[ ] `ConfigParams`
- \[ ] `ConfigInfo`

#### Pregunta 67. En el ConstraintLayout a continuación, ¿por qué no se expandiría el botón para llenar el ancho del padre?

```xml
  <androidx.constraintlayout.widget.ConstrantLayout
      ...>
    <Button
          android:layout_width="0dp"
          android:layout_height="wrap_content"
          android:text="Button"
          app:layout_constraintStart_toStartOf="parent"
          app:layout_constraintTop_toTopOf="parent"/>

  </androidx.constraintlayout.widget.ConstrantLayout>
```

- \[ ] `The button does not have a size`
- \[x] `The button is not constrained to the end of the parent container`
- \[ ] `Buttons cannot expand beyond their default size`
- \[ ] `The button should have its height set to 0dp as well`

#### Pregunta 68. ¿Qué no es un caso de uso para los recursos al ralentí en sus pruebas de Espresso?

- \[ ] `managing system services`
- \[x] `processing user input events`
- \[ ] `loading data from the internet or a local data source`
- \[ ] `perfoming bitmap transformatinos`

#### Pregunta 69. ¿Qué no es un tipo de recurso para proporcionar cadenas a la aplicación?

- \[ ] `String`
- \[x] `Text`
- \[ ] `String-array`
- \[ ] `Plurals`
