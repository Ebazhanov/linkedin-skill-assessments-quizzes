## Android

#### F1. Um Features, Komponenten und Berechtigungen zu Ihrer Android-App hinzuzufügen, welche Datei muss bearbeitet werden?

- [x] AndroidManifest.xml
- [ ] Components.xml
- [ ] AppManifest.xml
- [ ] ComponentManifest.xml

#### F2. Welches XML-Attribut sollte verwendet werden, um ein ImageView barrierefrei zu machen?

- [ ] android:talkBack
- [ ] android:labelFor
- [ ] android:hint
- [x] android:contentDescription

#### F3. Sie starten Ihre App und wenn Sie zu einem neuen Bildschirm navigieren, stürzt sie ab. Welche Aktion wird NICHT helfen, das Problem zu diagnostizieren?

- [ ] Setzen Sie Breakpoints und gehen Sie dann den Code Zeile für Zeile durch
- [ ] Verwenden Sie die Profiler-Tools in Android Studio, um Anomalien in CPU- und Netzwerknutzung zu erkennen.
- [x] Fügen Sie einen Thread.sleep()-Aufruf hinzu, bevor Sie die neue Activity starten.
- [ ] Überprüfen Sie die Logs in Logcat.

#### F4. Warum könnten Push-Benachrichtigungen aufhören zu funktionieren?

- [x] alle diese Antworten
- [ ] Das Geräte-Token wird nicht korrekt an den Push-Provider gesendet.
- [ ] Google Play Services ist nicht auf dem Gerät/Emulator installiert.
- [ ] Die Akku-Optimierung ist auf dem Gerät aktiviert.

#### F5. Was ist der korrekte Satz von Komponentenklassen, der benötigt wird, um eine RecyclerView von Elementen zu implementieren, die eine Liste von Widgets vertikal anzeigt?

- [ ] A

```java
    RecycleView
    RecyclerView.Adapter<T extends BaseAdapter>
    RecyclerView.ViewHolder<T extends BaseViewHolder>
    LinearLayoutManager
```

- [ ] B

```java
    RecycleView
    RecyclerView.Adapter
    RecyclerView.ViewHolder<T extends BaseViewHolder>
    LinearLayoutManager
```

- [ ] C

```java
    RecycleView
    RecyclerView.Adapter
    RecyclerView.ViewHolder
    LinearLayoutManager
```

- [x] D

```java
    RecycleView
    RecyclerView.Adapter<VH extends ViewHolder>
    RecyclerView.ViewHolder
    LinearLayoutManager
```

#### F6. Das Android-System beendet den Prozess, wenn es Speicher freigeben muss. Die Wahrscheinlichkeit, dass das System einen bestimmten Prozess beendet, hängt vom Zustand des Prozesses und der Activity zu diesem Zeitpunkt ab. Mit welcher Kombination aus Prozess- und Activity-Zustand wird am ehesten beendet?

- [x] Prozess: Im Hintergrund; Activity: Ist gestoppt
- [ ] Prozess: Im Hintergrund; Activity: Ist pausiert
- [ ] Prozess: Im Vordergrund; Activity: Ist gestartet
- [ ] Prozess: Im Vordergrund; Activity: Ist pausiert

#### F7. Sie haben eine NextActivity-Klasse erstellt, die von einem String abhängt, der einige Daten enthält, die innerhalb des Intents übergeben werden. Welcher Code-Ausschnitt ermöglicht es Ihnen, Ihre Activity zu starten?

- [ ] A

```java
    Intent(this, NextActivity::class.java).also { intent ->
        startActivity(intent)
    }
```

- [ ] B

```java
    Intent(this, NextActivity::class.java).apply {
        put(EXTRA_NEXT, "some data")
    }.also { intent ->
        activityStart(intent)
    }
```

- [x] C

```java
    Intent(this, NextActivity::class.java).apply {
        putExtra(EXTRA_NEXT, "some data")
    }.also { intent ->
        startActivity(intent)
    }
```

- [ ] D

```java
    Intent(this, NextActivity::class.java).apply {
        put(EXTRA_NEXT, "some data")
    }.also { intent ->
        activityStart(intent)
    }
```

#### F8. Sie möchten About- und Settings-Module in Ihr Projekt einbinden. Welche Dateien spiegeln ihre Einbindung korrekt wider?

- [ ] `in build.gradle:include ':app',':about' ':settings'`
- [x] `in settings.gradle:include ':app',':about' ':settings'`
- [ ] `in settings.gradle:include ':about',':settings'`
- [ ] `in gradle.properties:include ':app',':about' ':settings'`

#### F9. Was ist der Vorteil der Verwendung der @VisibleForTesting-Annotation?

- [x] um zu kennzeichnen, dass eine Klasse, Methode oder ein Feld ihre Sichtbarkeit gelockert hat, um Code testbar zu machen
- [ ] um zu kennzeichnen, dass eine Klasse, Methode oder ein Feld nur im Testcode sichtbar ist
- [ ] um zu kennzeichnen, dass eine Klasse, Methode oder ein Feld ihre Sichtbarkeit erhöht hat, um Code weniger testbar zu machen
- [ ] um einen Laufzeitfehler auszulösen, wenn eine Klasse, Methode oder ein Feld mit dieser Annotation unsachgemäß aufgerufen wird

#### F10. Wie würden Sie in Ihrer build.gradle-Datei angeben, dass Ihre App mindestens API-Level 21 zum Ausführen benötigt, aber auf API-Level 28 getestet werden kann?

- [ ] A

```
      defaultConfig {
        ...
        minApiVersion 21
        targetApiVersion 28
      }
```

- [ ] B

```
      defaultConfig {
        ...
        targetSdkVersion 21
        testSdkVersion 28
      }
```

- [ ] C

```
      defaultConfig {
        ...
        minSdkVersion 21
        testApiVersion 28
      }
```

- [x] D

```
      defaultConfig {
        ...
      minSdkVersion 21
        targetSdkVersion 28
      }
```

#### F11. Wann wird die onActivityResult() einer Activity aufgerufen?

- [ ] beim Aufrufen von finish() in der übergeordneten Activity
- [ ] beim Platzieren einer App in den Hintergrund durch Wechseln zu einer anderen App
- [ ] Wenn onStop() in der Ziel-Activity aufgerufen wird
- [x] beim Aufrufen von finish() in der Ziel-Activity

[Referenz](https://developer.android.com/reference/android/app/Activity)

#### F12. Sie müssen ein Event basierend auf seiner ID von Ihrer API entfernen. Welcher Code-Ausschnitt definiert diese Anfrage in Retrofit?

- [ ] @DELETE("events)
      fun deleteEvent(@Path("id") id: Long): Call<Unit>
- [x] @DELETE("events/{id}")
      fun deleteEvent(@Path("id") id: Long): Call<Unit>
- [ ] @REMOVE("events/{id}")
      fun deleteEvent(@Path("id") id: Long): Call<Unit>
- [x] @DELETE("events/{id}")
      fun deleteEvent(@Path("id") id: Long): Call<Unit>

#### F13. Wann würden Sie einen Product Flavor in Ihrer Build-Konfiguration verwenden?

- [ ] wenn Sie die Strings der App in mehreren Sprachen bereitstellen müssen
- [ ] wenn Sie verschiedene Versionen Ihrer App basierend auf der physischen Gerätegröße bereitstellen müssen
- [ ] wenn Sie verschiedene Versionen Ihrer App basierend auf der Bildschirmdichte des Geräts bereitstellen möchten
- [x] Wenn Sie eine andere Version Ihrer App mit benutzerdefinierter Konfiguration und Ressourcen bereitstellen möchten

#### F14. Gegeben das Fragment unten, wie würden Sie Zugriff auf ein TextView mit der ID text_home erhalten, das in der Layout-Datei einer Fragment-Klasse enthalten ist?

```java
    private lateinit var textView: TextView
    override fun onCreateView(...): View? {
        val root = inflator.inflator(R>layout.fragment_home, container, false)
        textView = ??
        return root
    }
```

- [ ] root.getById(R.id.text_home)
- [ ] findViewByID(R.id.text_home)
- [x] root.findViewById(R.id.text_home)
- [ ] root.find(R.id.text_home)

#### F15. Warum verwenden Sie den AndroidJUnitRunner beim Ausführen von UI-Tests?

Hinweis: AndroidJUnitRunner ermöglicht es uns, JUnit3/4-Stil-Tests auf Android-Geräten auszuführen

- [x] Der Test-Runner erleichtert das Laden Ihres Testpakets und der zu testenden App auf ein Gerät oder einen Emulator, führt den Test aus und meldet die Ergebnisse.
- [ ] Der Test-Runner erstellt Screenshots von jedem Bildschirm, der während der Testausführung angezeigt wird.
- [ ] Der Test-Runner erleichtert die Parallelisierung von Testklassen, indem er für jede Testklasse bereitstellt.
- [ ] Der Test-Runner erleichtert die Interaktion mit sichtbaren Elementen auf einem Gerät, unabhängig von der Activity oder dem Fragment, das den Fokus hat.

#### F16. Was ermöglicht es Ihnen, den Zustand eines Benutzers ordnungsgemäß wiederherzustellen, wenn eine Activity neu gestartet wird?

- [ ] die onSaveInstance()-Methode
- [x] alle diese Antworten
- [ ] persistenter Speicher
- [ ] ViewModel-Objekte

[Referenz](https://developer.android.com/topic/libraries/architecture/saving-states)

#### F17. Wenn der Haupt-Thread zu lange blockiert ist, zeigt das System den _-Dialog an.

- [ ] Thread reagiert nicht
- [ ] Anwendung pausiert
- [x] Anwendung reagiert nicht
- [ ] Anwendung blockiert

#### F18. Wie würden Sie den Wert der E-Mail eines Benutzers aus SharedPreferences abrufen und dabei sicherstellen, dass der zurückgegebene Wert nicht null ist?

- [ ] getPreferances(this).getString(Email,"")
- [ ] getDefaultSharedPrefarances(this).getString(EMAIL,null)
- [x] getDefaultSharedPreferances(this).getString(EMAIL,"")
- [ ] getPreferances(this).getString(EMAIL,null)

**Erklärung:** `In der Methode "getDefaultSharedPrefarances(this).getString()" wird der zweite Parameter übergeben, damit er zurückgegeben werden kann, falls der Schlüssel nicht existiert. Wir müssen also einen leeren String übergeben, der zurückgegeben wird, falls der Schlüssel nicht existiert.`

#### F19. Warum ist es problematisch, Größen mit Pixeln auf Android zu definieren?

- [ ] Obwohl die Bildschirmpixeldichte variiert, wirkt sich dies nicht auf die Verwendung von Pixeln zur Definition von Größen aus.
- [ ] Große Geräte haben immer mehr Pixel, sodass Ihre UI-Elemente betroffen sind, wenn Sie sie mit Pixeln definieren.
- [x] Die gleiche Anzahl von Pixeln kann unterschiedlichen physischen Größen entsprechen, was das Aussehen Ihrer UI-Elemente beeinflusst.
- [ ] Verschiedene Geräte haben unterschiedliche Verständnisse davon, was ein Pixel ist, was das Aussehen Ihrer UI-Elemente beeinflusst

[Referenz](https://developer.android.com/training/multiscreen/screendensities#:~:text=The%20first%20pitfall%20you%20must,physical%20sizes%20on%20different%20devices.)

#### F20. Sie müssen eine Liste der Geräte abrufen, die mit aktiviertem USB-Debugging an Ihren Computer angeschlossen sind. Welchen Befehl würden Sie mit der Android Debug Bridge ausführen?

- [ ] list devices
- [x] adb devices
- [ ] list avd
- [ ] dir devices

#### F21. Welche Drawable-Definition ermöglicht es Ihnen, die folgende Form zu erreichen?

![img](image/shape.png?raw=png)

- [ ] A

```xml
    <shape xmlns:android="http://schemas.android.com/apk/res/android"
        android:shape="oval">
        <stroke
            android:width="4dp"
	    android:color="@android:color/white" />
	<solid android:color="@android:color/black" />
    </shape>
```

- [ ] B

```xml
    <oval xmlns:android="http://schemas.android.com/apk/res/android">
        <stroke android:width="4dp" android:color="@android:color/black"/>
        <solid android:color="@android:color/white"/>
    </oval>
```

- [x] C

```xml
    <shape xmlns:android="http://schemas.android.com/apk/res/android"
        android:shape="oval">
        <stroke
            android:width="4dp"
            android:color="@android:color/black" />
        <solid android:color="@android:color/white" />
    </shape>
```

- [ ] D

```xml
    <shape xmlns:android="http://schemas.android.com/apk/res/android"
        android:shape="oval">
        <stroke
            android:width="4dp"
            android:color="@android:color/white" />
        <solid android:color="@android:color/white" />
    </shape>
```

#### F22. Um eine kleine Sammlung von Schlüssel-Wert-Daten zu speichern, was sollten Sie verwenden?

- [ ] externe Dateispeicherung
- [x] SharedPreferences
- [ ] SQLite
- [ ] interne Dateispeicherung

#### F23. Sie müssen eine Liste von Fotos von einer API abrufen. Welcher Code-Ausschnitt definiert eine HTML-GET-Anfrage in Retrofit?

- [ ] @GET("photo/{id}"}
      fun listPhotos(@Path("id") id:Long?) : Call<Photo>
- [ ] @LIST("photo")
      fun listPhotos() : Call<List<Photo>>
- [ ] @GET("photo")
      fun listPhotos() : Call<Photo>
- [x] @GET("photo")
      fun listPhotos() : Call<List<Photo>>

#### F24. Gegeben die Testklasse unten, welcher Code-Ausschnitt wäre eine korrekte Assertion?

- [ ] assertThat(resultAdd).is(2.0)
- [x] assertNotNull(resultAdd)
- [ ] assertThat(resultAdd).isWqualTo(2.0)
- [ ] assertThat(resultAdd)

#### F25. Welches Tag sollten Sie verwenden, um eine wiederverwendbare View-Komponente zu einer Layout-Datei hinzuzufügen?

- [ ] `<merge/>`
- [x] `<include/>`
- [ ] `<layout/>`
- [ ] `<add/>`

#### F26. Sie möchten ein anderes Drawable für Geräte bereitstellen, die im Querformat sind und deren Sprache auf Französisch eingestellt ist. Welches Verzeichnis ist korrekt benannt?

- [ ] fr-land-drawable
- [x] drawable-fr-land
- [ ] drawable-french-land
- [ ] french-land-drawable

#### F27. Warum müssen Sie möglicherweise die folgende Berechtigung in Ihre App aufnehmen?

`android.permission.ACCESS_NETWORK_STATE`

- [ ] um die Position der Geräte zu überwachen, damit Sie keine Netzwerkaufrufe versuchen, wenn der Benutzer stationär ist
- [ ] um die Möglichkeit anzufordern, Netzwerkaufrufe von Ihrer App aus zu tätigen
- [ ] um den Netzwerkstatus des Geräts zu überwachen, damit Sie dem Benutzer ein In-App-Banner anzeigen können
- [x] um den Netzwerkstatus der Geräte zu überwachen, damit Sie keine Netzwerkaufrufe versuchen, wenn das Netzwerk nicht verfügbar ist

#### F28. Welches Bild entspricht am besten dem folgenden `LinearLayout`?

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

- [ ] A
      ![img](image/00.jpeg)
- [x] B
      ![img](image/01.jpeg)
- [ ] C
      ![img](image/02.jpeg)
- [ ] D
      ![img](image/03.jpeg)

#### F29. Sie möchten die Standard-Dialer-App auf einem Gerät öffnen. Was ist falsch an diesem Code?

```
val dialerIntent = Intent()
val et = findViewById(R.id.some_edit_text)
dialerIntent.action = Intent.ACTION_DIAL
dialerIntent.data = Uri.parse("tel:" + et.getText()?.toString())
startActivity(dialerIntent)
```

- [x] `startActivityWithResult()` sollte anstelle von `startActivity()` verwendet werden, wenn `Intent.ACTION_DIAL` verwendet wird.
- [ ] Für `Intent.ACTION_DIAL` muss die `Intent`-Option `Intent.FLAG_ACTIVITY_NEW_TASK` hinzugefügt werden, wenn dieser `dialerIntent` verwendet wird.
- [ ] Der `dialerIntent` wird eine ActivityNotFoundException auf Geräten auslösen, die `Intent.ACTION_DIAL` nicht unterstützen.
- [ ] Die Berechtigung `android.permission.CALL_PHONE` muss zuerst angefordert werden, bevor `Intent.ACTION_DIAL` verwendet werden kann.

#### F30. Wann sollten Sie Dateien im `/assets`-Verzeichnis speichern?

- [x] wenn Sie Zugriff auf die ursprünglichen Dateinamen und die Dateihierarchie benötigen
- [ ] wenn Sie Zugriff auf die Datei mit ihrer `Ressourcen-ID` benötigen, wie `R.assets.filename`
- [ ] wenn Sie XML-Dateien haben, die Tween-Animationen definieren
- [ ] wenn Sie auf die Datei in ihrer Rohform zugreifen müssen mit `Resources.openRawResource()`

[Referenz](https://medium.com/mobile-app-development-publication/assets-or-resource-raw-folder-of-android-5bdc042570e0)

#### F31. Sie möchten Benutzern erlauben, in Ihrer App Bilder aufzunehmen. Was ist _kein_ Vorteil der Erstellung eines geeigneten `Intent`, anstatt die Kamera-Berechtigung direkt anzufordern?

- [ ] Benutzer können ihre Lieblingsfoto-Apps zum Aufnehmen von Bildern auswählen.
- [ ] Sie müssen keine Berechtigungsanfrage in Ihrer App stellen, um ein Bild aufzunehmen.
- [x] Sie haben die volle Kontrolle über die Benutzererfahrung. Die App, die den Kamera-`Intent` verarbeitet, wird Ihre Designentscheidungen respektieren.
- [ ] Sie müssen die Benutzeroberfläche nicht entwerfen. Die App, die den Kamera-`Intent` verarbeitet, stellt die Benutzeroberfläche bereit.

#### F32. Wann würden Sie die Funktion `ActivityCompat.shouldShowRequestPermissionRationale()` verwenden?

- [ ] wenn ein Benutzer Ihre App zum ersten Mal öffnet und Sie die Verwendung einer bestimmten Berechtigung erklären möchten
- [ ] wenn ein Benutzer die Anfrage für eine bestimmte Berechtigung zuvor abgelehnt hat und "Mehr erfahren" auswählt
- [ ] wenn ein Benutzer die Anfrage für eine bestimmte Berechtigung zuvor abgelehnt hat und Sie deren Verwendung erklären möchten
- [x] wenn ein Benutzer die Anfrage für eine bestimmte Berechtigung zuvor abgelehnt und "Nicht mehr fragen" ausgewählt hat, Sie aber die Berechtigung für die Funktion Ihrer App benötigen

#### F33. Sie möchten Analytics-Tracking nur in `release`-Builds aktivieren. Wie können Sie ein neues Feld in der generierten `BuildConfig`-Klasse erstellen, um diesen Wert zu speichern?

- [ ] A

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

- [ ] B

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

- [x] C

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

- [ ] D

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

#### F34. Um Ihre APK-Größe zu optimieren, welchen Bild-Codec sollten Sie verwenden?

- [ ] JPG
- [ ] PNG gut geformt
- [ ] MPEG
- [x] WebP

[Referenz](https://developer.android.com/topic/performance/reduce-apk-size#:~:text=packJPG%20and%20guetzli.-,Use%20WebP%20file%20format,than%20either%20JPEG%20or%20PNG.)

#### F35. Sie haben Code erstellt, um einen Netzwerkaufruf durchzuführen, und getestet, dass er in Ihrer Entwicklungsumgebung funktioniert. Wenn Sie ihn jedoch in der Play-Konsole veröffentlichen, funktioniert der Netzwerkaufruf nicht. Was wird Ihnen _nicht_ helfen, dieses Problem zu beheben?

- [ ] Überprüfen, ob `ProGuard` -keepclassmembers zu den betreffenden Netzwerkdatenübertragungsobjekten (DTOs) hinzugefügt wurden
- [x] Verwenden der Profiler-Tools in Android Studio, um Anomalien in CPU-, Speicher- und Netzwerknutzung zu erkennen
- [ ] Überprüfen auf Ausnahmen in den Serverprotokollen oder der Serverkonsole
- [ ] Überprüfen, dass das Netzwerkdatenübertragungsobjekt `@SerializedName` auf seine Member-Eigenschaften angewendet hat

#### F36. Welcher Code-Ausschnitt würde das unten angezeigte Layout erreichen?

![img](image/04.jpeg)

- [ ] A

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

- [x] B

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

- [ ] C

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

- [ ] D

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

#### F37. Welches Source-Set ist standardmäßig _nicht_ verfügbar, wenn Android Studio ein neues Projekt erstellt?

- [ ] test
- [ ] androidTest
- [ ] app
- [x] main

#### F38. Welche Definition verhindert, dass andere Apps über einen `Intent` auf Ihre `Activity`-Klasse zugreifen?

- [x] A

```xml
	<activity android:name=".ExampleActivity" />
```

- [ ] B

```xml
	<activity android:name=".ExampleActivity">
		<intent-filter>
			<action android:name="android.intent.action.SEND" />
		</intent-filter>
	</activity>
```

- [ ] C

```xml
	<activity android:name=".ExampleActivity">
		<intent-filter>
			<action android:name="android.intent.action.MAIN" />
			<category android:name="android.intent.category.LAUNCHER" />
		</intent-filter>
	</activity>
```

- [ ] D

```xml
	<activity android:name=".ExampleActivity">
		<intent-filter>
			<action android:name="android.intent.action.VIEW" />
		</intent-filter>
	</activity>
```

**Erklärung:** `Intent-Filter werden verwendet, um Activities für andere Apps über Intents zugänglich zu machen. Wir müssen also die Option ohne Intent-Filter wählen, um sicherzustellen, dass sie nicht per Intent zugänglich ist`

#### F39. Um Gerätespeicher zu schonen, wie könnten Sie feststellen, dass das Gerät des Benutzers begrenzte Speicherkapazitäten hat?

- [x] Verwenden Sie die Methode `ActivityManager.isLowRamDevice()`, um herauszufinden, ob ein Gerät sich selbst als "Low RAM" definiert.
- [ ] Verwenden Sie die Methode `Activity.islowRam()`, um herauszufinden, ob ein Gerät sich selbst als "Low RAM" definiert.
- [ ] Verwenden Sie die Methode `ConnectivityManager.hasLowMemory()`, um herauszufinden, ob ein Gerät sich selbst als "Low RAM" definiert.
- [ ] Führen Sie eine Bild-Download-Anfrage durch und überprüfen Sie die verbleibende Gerätespeichernutzung.

#### F40. Was ist _kein_ guter Weg, um Android-Code wiederzuverwenden?

- [ ] Verwenden Sie ein gemeinsames Gradle-Modul, das von verschiedenen Android-Projekten gemeinsam genutzt wird.
- [ ] Bevorzugen Sie es, benutzerdefinierte Views oder Fragments anstelle von Activities zu erstellen.
- [x] Bevorzugen Sie es, Activities anstelle von Fragments zu erstellen.
- [ ] Zerlegen Sie UI-Layouts in gemeinsame Elemente und verwenden Sie `<include/>`, um sie in andere Layout-XML-Dateien einzubinden.

#### F41. Welches Layout ist am besten für große, komplexe Hierarchien?

- [ ] LinearLayout
- [x] ConstraintLayout
- [ ] FrameLayout
- [ ] RelativeLayout

#### F42. Sie müssen auf die neueste Version des Android Gradle Plugins upgraden. Welche Datei sollten Sie ändern?

- [ ] root_project_dir/app/build.gradle.
- [ ] root_project_dir/settings.gradle.
- [x] root_project_dir/build.gradle.
- [ ] root_project_dir/app/gradle.properties.

[Referenz](https://developer.android.com/studio/releases/gradle-plugin#updating-plugin)

#### F43. Warum platzieren Entwickler oft App-Initialisierungscode in der Application-Klasse?

- [x] Die Application-Klasse wird instanziiert, bevor eine andere Klasse instanziiert wird, wenn der Prozess für die Anwendung erstellt wird.
- [ ] Die Application-Klasse wird nach allen Berechtigungsanfragen instanziiert, wenn der Prozess für die Anwendung erstellt wird.
- [ ] Die Application-Klasse wird jedes Mal erstellt, wenn eine neue Activity gestartet wird, was sie ideal für Initialisierungscode macht.
- [ ] Die Application-Klasse wird jedes Mal erstellt, wenn ein Hintergrunddienst aufgerufen wird, was sie ideal für Initialisierungscode macht.

[Referenz](https://developer.android.com/reference/android/app/Application)

#### F44. Welchen Ordner sollten Sie für die Launcher-Icons Ihrer App verwenden?

- [ ] /drawable
- [ ] /icon
- [x] /mipmap
- [ ] /launcher

#### F45. Welche Drawable-Definition ermöglicht es Ihnen, die folgende Form zu erreichen?

![img](image/43.jpeg)

- [ ] A

```xml
	<shape xmlns:android-"http://schemas.android.com/apk/res/android"
	    android:shape-"oval">
	    <gradient
               android:startColor-"@android:color/white"
               android:endColor-"@android:color/black"
               android:angle-"45"/>
	</shape>
```

- [ ] B

```xml
	<rectangle xmlns:android-"http://schemas.android.com/apk/res/android">
	   <gradient
	      android:startColor-"@android:color/white"
	      android:endColor-"android:color/black"
	      android:angle-"135"/>
	</rectangle>
```

- [x] C

```xml
	<shape xmlns:android-"http://schemas.android.com/apk/res/android"
	   android:shape-"rectangle">
	   <gradient
	      android:startColor-"@android:color/white"
	      android:endColor-"@android:color/black"
	      android:angle-"135"/>
	</shape>
```

- [ ] D

```xml
	<shape xmlns:android-"http://schemas.android.com/apk/res/android"
	   android:shape-"rectangle">
	   <gradient
	      android:startColor-"@android:color/white"
	      android:endColor-"@android:color/black"
	      android:angle-"98"/>
	</shape>
```

#### F46. Gegeben das ConstraintLayout unten, welche Aussage ist wahr?

![img](image/44.jpeg)

- [ ] View B ist nicht horizontal beschränkt.
- [ ] View C hat zu viele Beschränkungen.
- [x] View B ist nicht vertikal beschränkt.
- [ ] View C ist auf das übergeordnete Element beschränkt.

#### F47. Gegeben dieser Code-Ausschnitt aus einer build.gradle-Datei, welche Wahl ist keine mögliche Build-Variante?

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

- [ ] productionDebug.
- [x] developmentDebug.
- [ ] stagingDebug.
- [ ] stagingRelease.

[Referenz](https://developer.android.com/studio/build/build-variants#flavor-dimensions)

#### F48. Wann sollten Sie das androidTest-Verzeichnis verwenden, um Ihre Testklassen zu speichern?

- [ ] wenn die Tests nur aus Unit-Tests bestehen.
- [ ] wenn die Anzahl der auszuführenden Tests groß ist (500+).
- [ ] wenn die Tests auf Ihrer lokalen Maschine ausgeführt werden müssen.
- [x] wenn die Tests auf echten oder virtuellen Geräten ausgeführt werden müssen.

[Referenz](https://developer.android.com/studio/test#test_types_and_location)

#### F49. Gegeben eine APK namens app-internal-debug.apk, die aus dem Build-Prozess erstellt wurde, welche Aussage ist wahrscheinlich wahr?

- [ ] Diese APK wird auf einem Entwicklercomputer aus dem Debug-Product-Flavor erstellt.
- [ ] Diese APK wird aus dem internalDebug-Product-Flavor erstellt.
- [ ] Diese APK wird aus dem Debug-Product-Flavor und dem internen Build-Typ erstellt.
- [x] Diese APK wird aus dem Debug-Build-Typ und dem internen Product-Flavor erstellt.

#### F50. Was könnte der folgende Fehler beim Versuch, Ihr Projekt zu erstellen, anzeigen?

`Conversion to Dalvik format filed: Unable to execute dex: method ID not in [0, 0xffff]: 65536`

- [ ] Sie haben falsche Formatinformationen in Ihrer build.gradle-Datei eingefügt.
- [ ] Sie haben mehr als 20 Abhängigkeiten zu Ihrer build.gradle hinzugefügt.
- [x] Sie haben die Gesamtzahl der Methoden überschritten, die innerhalb einer einzelnen DEX-Datei referenziert werden können.
- [ ] Sie haben eine NullPointerException in Ihrem Code.

#### F51. Welche Anweisung in der build.gradle-Datei gibt korrekt an, dass das entsprechende Modul ein Android-Bibliotheksmodul ist?

- [ ] apply plugin: 'com.module.library'
- [x] apply plugin: 'com.android.library'
- [ ] apply plugin: 'com.module.library'
- [ ] include plugin: 'com.module.library'

#### F52. Gegeben die folgende dimens.xml-Datei, wie würden Sie ein ImageView mit mittlerem Abstand am unteren Rand definieren?

```xml
<?xml version=1.0 encoding="utf-8"?>
<resources>
    <dimen name="spacing_medium">8dp</dimen>
    <dimen name="spacing_large">12dp</dimen>
</resources>
```

- [ ] A

```xml
<ImageView
   android:id=@+id/image_map_pin"
   android:layout_width="wrap_content"
   android:layout_heignt="wrap_content"
   android:src=@drawable/map_pin />
```

- [ ] B

```xml
<ImageView
   android:id=@+id/image_map_pin"
   android:layout_width="wrap_content"
   android:layout_heignt="wrap_content"
   androi:layout_botttom="@dimen/spacing_medium"
   android:src=@drawable/map_pin />
```

- [ ] C

```xml
<ImageView
   android:id=@+id/image_map_pin"
   android:layout_width="wrap_content"
   android:layout_heignt="wrap_content"
   android:layout_marginBottom="@resources/spacing_medium"
   android:src=@drawable/map_pin />
```

- [x] D

```xml
<ImageView
   android:id=@+id/image_map_pin"
   android:layout_width="wrap_content"
   android:layout_heignt="wrap_content"
   android:layout_marginBottom="@dimen/spacing_medium"
   android:src=@drawable/map_pin />
```

#### F53. Was ist kein Vorteil der Externalisierung von App-Ressourcen wie Bildern und Strings aus dem Code?

- [ ] Es ermöglicht Android, die entsprechende Ressource basierend auf der aktuellen Konfiguration während der Laufzeit auszuwählen.
- [x] Es ermöglicht Ihnen, performantere Anwendungen zu haben, da Code und Ressourcen getrennt sind.
- [ ] Es ermöglicht Ihnen, eine andere Benutzererfahrung basierend auf den Spracheinstellungen des Benutzers bereitzustellen.
- [ ] Es ermöglicht Ihnen, eine andere Benutzererfahrung basierend auf der Gerätegröße des Benutzers bereitzustellen.

#### F54. Was ist der Hauptzweck von Zeile fünf in diesem Code-Ausschnitt?

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

- [ ] sicherzustellen, dass die Activity beendet wird, wenn savedInstanceState nicht null ist
- [x] sicherzustellen, dass die Activity jedes Mal ein neues Fragment erstellt, wenn sie aus einem vorherigen Zustand wiederhergestellt wird
- [ ] die Anzeige von zwei Fragmenten nebeneinander in Fällen zu verhindern, in denen die Activity aus einem vorherigen Zustand wiederhergestellt wird
- [ ] die Erstellung überlappender Fragmente in Fällen zu verhindern, in denen die Activity aus einem vorherigen Zustand wiederhergestellt wird

#### F55. Welche Komponente ist kein Einstiegspunkt, durch den das System oder ein Benutzer in Ihre App eintreten kann?

- [ ] Activity
- [ ] Content Provider
- [x] Fragment
- [ ] Service

#### F56. Was sollten Sie verwenden, um eine große, scrollende Liste von Elementen anzuzeigen?

- [ ] ListView
- [x] RecyclerView
- [ ] LinearLayout
- [ ] ScrollView

#### F57. Sie haben eine AboutActivity-Klasse erstellt, die Details über Ihre App anzeigt. Welcher Code-Ausschnitt ermöglicht es Ihnen, Ihre Activity zu starten?

- [ ] `Intent(this, AboutActivity::class).also { intent -> startService(intent)}`
- [x] `Intent(this, AboutActivity::class.java).also { intent -> startActivity(intent)}`
- [ ] `Intent(this, AboutActivity::class).also { intent -> activity(intent)}`
- [ ] `Intent(this, AboutActivity::class).also { intent -> startActivity(intent)}`

**Erklärung**: `Intent(Context packageContext, Class<?> cls) Hinweis: Class nicht KClass`

#### F58. Was ist die Verwendung der AndroidManifest.xml-Datei?

- [x] Sie beschreibt die Komponente der Anwendung
- [ ] Sie deklariert das Mindest-API-Level, das die Anwendung benötigt
- [ ] Sie erleichtert die Bereitstellung eines eindeutigen Namens für die Anwendung durch Angabe des Paketnamens
- [ ] Alle oben genannten

#### F59. Welches Attribut des Elements <uses-sdk> wird verwendet, um das minimale API-Level anzugeben, das für die Ausführung der Anwendung erforderlich ist?

- [ ] android:targetSdkVersion
- [x] android:minSdkVersion
- [ ] android:maxSdkVersion
- [ ] Keine der oben genannten

#### F60. Um Ihren Code in Release-Builds zu verkleinern, welches Tool verwendet Android Studio?

- [x] R8
- [ ] ProGuard
- [ ] Shrinker
- [ ] D8

**Erklärung**: `Wenn Sie Ihr Projekt mit Android Gradle Plugin 3.4.0 oder höher erstellen, verwendet das Plugin nicht mehr ProGuard zur Durchführung der Code-Optimierung zur Kompilierzeit. Stattdessen arbeitet das Plugin mit dem R8-Compiler`

[Referenz](https://developer.android.com/studio/build/shrink-code)

#### F61. Welche Layout-Hierarchie wird wahrscheinlich am schnellsten gezeichnet?

- [x] A
      ![img](https://i.imgur.com/mT08jag.png?raw=png)

- [ ] B
      ![img](https://i.imgur.com/rz9eKYc.png?raw=png)

- [ ] C
      ![img](https://i.imgur.com/ETaHhaS.png?raw=png)

- [ ] D
      ![img](https://i.imgur.com/1QBrTwR.png?raw=png)

#### F62. Was ist die derzeit empfohlene Methode zur Handhabung von lang laufenden Hintergrundaufgaben?

- [x] WorkManager
- [ ] AsyncTask
- [ ] IntentService
- [ ] Thread

[Referenz](https://developer.android.com/guide/background)

#### F63. Sie müssen Ihren Benutzern bestimmte Funktionen Ihrer App auf Abruf oder als Sofort-Erlebnisse über Google Play bereitstellen. Welche Art von Modul sollten Sie erstellen?

- [ ] Bibliotheksmodul
- [x] Dynamisches Feature-Modul
- [ ] Android-App-Modul
- [ ] Google Cloud-Modul

1. [Referenz](https://youtu.be/QdfStuj-MuA?t=86)
2. [Referenz](https://developer.android.com/guidgite/playcore/feature-delivery/on-demand)

#### F64. Welcher Ansatz wird nicht empfohlen, um einen nützlichen Offline-Zustand in Ihrer App bereitzustellen?

- [ ] Daten cachen
- [ ] Daten lokal speichern
- [ ] Ausgehende Anfragen in die Warteschlange stellen, die bei Verbindungsverlust ausgeführt werden sollen
- [x] Benutzer immer benachrichtigen, dass die Verbindung verloren gegangen ist

[Referenz](https://developer.android.com/docs/quality-guidelines/build-for-billions/connectivity#network-offline)

#### F65. Wenn Ihr App-Code Informationen über den aktuellen Build überprüfen muss, welche Klasse sollten Sie verwenden?

- [x] `BuildConfig`
- [ ] `BuildInfo`
- [ ] `ConfigParams`
- [ ] `ConfigInfo`

#### F66. Im ConstraintLayout unten, warum würde sich der Button nicht erweitern, um die Breite des übergeordneten Elements zu füllen?

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

- [ ] `Der Button hat keine Größe`
- [x] `Der Button ist nicht am Ende des übergeordneten Containers beschränkt`
- [ ] `Buttons können nicht über ihre Standardgröße hinaus erweitert werden`
- [ ] `Der Button sollte seine Höhe ebenfalls auf 0dp setzen`

#### F67. Was ist kein Anwendungsfall für Idling-Ressourcen in Ihren Espresso-Tests?

- [ ] `Verwaltung von Systemdiensten`
- [x] `Verarbeitung von Benutzereingabeereignissen`
- [ ] `Laden von Daten aus dem Internet oder einer lokalen Datenquelle`
- [ ] `Durchführung von Bitmap-Transformationen`

#### F68. Was ist kein Typ von Ressource zur Bereitstellung von Strings für Ihre App?

- [ ] `String`
- [x] `Text`
- [ ] `String-array`
- [ ] `Plurals`

#### F69. Was ist nicht im Activity-Lebenszyklus?

- [ ] `onPause()`
- [ ] `onResume()`
- [x] `onOpen()`
- [ ] `onStart()`

#### F70. Sie möchten Benutzern erlauben, ein Bild in Ihrer App aufzunehmen. Welcher Code-Ausschnitt ist der richtige Ansatz?

- [ ] A

```java
  fun showCamera(view: View) {
      Log.i(TAG, "Show camera button pressed.")
      if (ContextCompat.shouldShowRequestPermissionRationale(thisActivity,
      Manifest.permission.CAMERA) {
        showCameraPreview()
      }
       else {
         requestPermissionLauncher.launch(Manifest.permission.CAMERA)
       }
   }
```

- [x] B

```java
  fun showCamera(view: View) {
      Log.i(TAG, "Show camera button pressed.")
      if (ContextCompat.checkSelfPermission(thisActivity,
      Manifest.permission.CAMERA)
      == PackageManager.PERMISSION_GRANTED) {
        showCameraPreview()
      }
      else {
         requestPermissionLauncher.launch(Manifest.permission.CAMERA)
      }
  }
```

- [ ] C

```java
  fun showCamera(view: View) {
      Log.i(TAG, "Show camera button pressed.")
      showCameraPreview()
  }
```

- [ ] D

```java
  fun showCamera(view: View) {
      Log.i(TAG, "Show camera button pressed.")
      if (ContextCompat.checkSelfPermission(thisActivity,
      Manifest.permission.CAMERA)
      != PackageManager.PERMISSION_GRANTED) {
         showCameraPreview()
       }
       else {
          requestPermissionLauncher.launch(Manifest.permission.CAMERA)
       }
  }
```

#### F71. Gegeben die String-Ressource unten, welcher Code-Ausschnitt ist gültig?

```
<string name="upload_photo_notification">%1$d von %2$d Fotos hochgeladen</string>
```

- [ ] A

```
val string: String = getString(
   R.string.upload_photo_notification,
   "2",
   "5"
)
```

- [ ] B

```
val string: String = getString(
   R.id.upload_photo_notification,
   2,
   5
)
```

- [x] C

```
val string: String = getString(
   R.string.upload_photo_notification,
   2,
   5
)
```

- [ ] D

```
val string: String = getString(
   R.id.upload_photo_notification,
   "2",
   "5"
)
```

[Referenz](https://developer.android.com/guide/topics/resources/string-resource#formatting-strings)

#### F72. Verschiedene Sprachen haben unterschiedliche Regeln für grammatikalische Übereinstimmung mit der Menge. Um die folgenden zwei Strings in mehreren Sprachen in Ihrer App zu unterstützen, was ist die ideale Ressourcendefinition?

```
"Sie haben 1 Tag verbleibend"
"Sie haben 2 Tage verbleibend"
```

- [ ] A

```
<string name="trial_days_left_one"> Sie haben %1$d Tag verbleibend</string>
<string name="trial_days_left_other">Sie haben %1$d Tage verbleibend</string>
```

- [ ] B

```
<plurals name="trial days left">
    <plural quantity="one">Sie haben %1$d Tag verbleibend</plural>
    <plural quantity="other">Sie haben %1$d Tage verbleibend</plural>
</plurals>
```

- [x] C

```
<plurals name="trial_days_left">
    <item quantity="one">Sie haben %1$d Tag verbleibend</item>
    <item quantity="other">Sie haben %1$d Tage verbleibend</item>
</plurals>
```

- [ ] D

```
<string name="trial_days_left">
    <plural quantity="one">Sie haben %1$d Tag verbleibend</plural>
    <plural quantity="other">Sie haben &1$d Tage verbleibend</plural>
</string>
```

#### F73. Wann würde das Betriebssystem die Methode onTrimMemory() verwenden?

- [ ] `wenn die App deinstalliert wird`
- [x] `wenn die App in den Hintergrund gelegt wird`
- [ ] `wenn das Gerät im Akku-Optimierungsmodus ist`
- [ ] `wenn Netzwerkanfragen im Haupt-Thread durchgeführt werden`

[Referenz](https://developer.android.com/guide/topics/resources/string-resource#Plurals)

#### F74. In Ihrer App haben Sie eine RecyclerView mit Elementen. Sie möchten eine unterschiedliche Konfiguration für Hochformat- und Querformat-Modi haben. Welcher Code-Ausschnitt würde es Ihnen ermöglichen, das Layout unten am besten zu unterstützen?

![img](image/Q75.png)

- [ ] A

```
recyclerView.setLayoutManager(GridLayoutManager(this, 3))
```

- [x] B

```
val coulumnCount = resources.getInteger(R.integer.column_count)
recyclerView.setLayoutManager(GridLayoutManager(this, columnCount))
```

- [ ] C

```
recyclerView.setLayoutManager(LinearLayoutManager(this))
```

- [ ] D

```
val coulumnCount = resources.getInteger(R.integer.column_count)
recyclerView.setLayoutManager(LinearLayoutManager(this, columnCount))
```

#### F75. Sie müssen ein Event basierend auf seiner ID von Ihrer API entfernen. Welcher Code-Ausschnitt definiert diese Anfrage in Retrofit?

- [ ] @DELETE("events)
      fun deleteEvent(@Path("id") id: Long): Call<Unit>
- [x] @DELETE("events/{id}")
      fun deleteEvent(@Path("id") id: Long): Call<Unit>
- [ ] @REMOVE("events/{id}")
      fun deleteEvent(@Path("id") id: Long): Call<Unit>
- [x] @DELETE("events/{id}")
      fun deleteEvent(@Path("id") id: Long): Call<Unit>

#### F76. Sie möchten Benutzern erlauben, Bilder in Ihrer App aufzunehmen. Was ist _kein_ Vorteil der Erstellung eines geeigneten `Intent`, anstatt die Kamera-Berechtigung direkt anzufordern?

- [ ] Benutzer können ihre Lieblingsfoto-Apps zum Aufnehmen von Bildern auswählen.
- [ ] Sie müssen keine Berechtigungsanfrage in Ihrer App stellen, um ein Bild aufzunehmen.
- [x] Sie haben die volle Kontrolle über die Benutzererfahrung. Die App, die den Kamera-`Intent` verarbeitet, wird Ihre Designentscheidungen respektieren.
- [ ] Sie müssen die Benutzeroberfläche nicht entwerfen. Die App, die den Kamera-`Intent` verarbeitet, stellt die Benutzeroberfläche bereit.

#### F77. Was ist die derzeit empfohlene Methode zur Handhabung von lang laufenden Hintergrundaufgaben?

- [x] WorkManager
- [ ] AsyncTask
- [ ] IntentService
- [ ] Thread