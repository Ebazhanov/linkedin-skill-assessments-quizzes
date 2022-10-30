## Androide

#### D1. Per aggiungere funzionalità, componenti e autorizzazioni alla tua app Android, quale file deve essere modificato?

- \[x] AndroidManifest.xml
- \[ ] Componenti.xml
- \[ ] AppManifest.xml
- \[ ] ComponentManifest.xml

#### D2. Quale attributo XML deve essere utilizzato per rendere accessibile una visualizzazione immagine?

- \[ ] android:talkBack
- \[ ] android:labelFor
- \[ ] androide:suggerimento
- \[x] android:contentDescription

#### D3. Avvii la tua app e quando passi a una nuova schermata si blocca, quale azione NON ti aiuterà a diagnosticare il problema?

- \[ ] Impostare i punti di interruzione e quindi scorrere il codice riga per riga
- \[ ] Utilizza gli strumenti di profiler in Android Studio per rilevare anomalie della CPU e dell'utilizzo della rete.
- \[x] Aggiungere una chiamata Thread.sleep() prima di iniziare la nuova attività.
- \[ ] ispezionare i registri in Logcat.

#### D4. Perché le notifiche push potrebbero smettere di funzionare?

- \[x] tutte queste risposte
- \[ ] Il token del dispositivo non viene inviato correttamente al provider push.
- \[ ] Google Play Services non è installato sul deivce/emulatore.
- \[ ] L'ottimizzazione della batteria è attivata sul dispositivo.

#### D5. Qual è il set corretto di classi di componenti necessario per implementare un RecyclerView di elementi che visualizza un elenco di widget verticalmente?

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

#### D6. Il sistema Android uccide il processo quando ha bisogno di liberare memoria. La probabilità che il sistema uccida un determinato processo dipende dallo stato del processo e dall'attività in quel momento. Con la combinazione di processo e stato di attività è più probabile che venga ucciso?

- \[x] Processo:In background; Attività:Viene interrotto
- \[ ] Processo:In background; Attività:È in pausa
- \[ ] Processo:In primo piano; Attività:Viene avviato
- \[ ] Processo:In primo piano; Attività:È in pausa

#### D7. È stata creata una classe NextActivity che si basa su una stringa contenente alcuni dati che passano all'interno dell'intento Quale frammento di codice consente di avviare l'attività?

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

#### D8. Si desidera includere i moduli di informazioni e impostazione nel progetto. Quali file riflettono accuratamente la loro inclusione?

- \[ ] in build.gradle:include ':app',':about' ':settings'
- \[x] in settings.gradle:include ':app',':about' ':settings'
- \[ ] in settings.gradle:include ':about',':settings'
- \[ ] in gradle.properties:include ':app',':about' ':settings'

#### D9. Qual è il vantaggio di utilizzare @VisibleForTesting annotazione?

- \[x] per indicare che una classe, un methos o un campo ha la sua visibilità rilassata per rendere il codice testabile
- \[ ] per indicare che una classe, un metodo o un campo è visibile solo nel codice del test
- \[ ] per indicare che una classe, un metodo o un campo ha la sua visibilità aumentata per rendere il codice meno testabile
- \[ ] per generare un errore di runtime se si accede in modo errato a una classe, a un methos o a un campo con questa annotazione

#### D10. Come si specifica nel file build.gradle che l'app richiede almeno il livello API 21 per l'esecuzione, ma che può essere testata al livello API 28?

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

#### D11. Quando verrà chiamata onActivityResult()di un'attività?

- \[ ] quando si chiama finish()nell'attività padre
- \[ ] quando si posiziona un'app in background collegandosi a un'altra app
- \[ ] Quando onStop() viene chiamato nell'attività di destinazione
- \[x] quando si chiama finish() nell'attività di destinazione

[Per maggiori informazioni](https://developer.android.com/reference/android/app/Activity)

#### D12. Devi rimuovere un evento in base al suo ID dalla tua API, Quale snippet di codice definisce quella richiesta in Retrofit?

- \[ ] @DELETE("eventi"
  fun deleteEvent(@Path("id") id: Long): Chiama<Unit>
- \[x] @DELETE("events/{id}")
  fun deleteEvent(@Path("id") id: Long): Chiama<Unit>
- \[ ] @REMOVE("events/{id}")
  fun deleteEvent(@Path("id") id: Long): Chiama<Unit>
- \[x] @DELETE("events/{id}")
  fun deleteEvent(@Path("id") id: Long): Chiama<Unit>

#### D13. Quando useresti un sapore di prodotto nella tua configurazione di costruzione?

- \[ ] quando è necessario avere le stringhe dell'app presenti in più lanuage
- \[ ] quando devi fornire versioni diverse della tua app in base alle dimensioni del dispositivo fisico
- \[ ] quando vuoi fornire versioni diverse della tua app in base alla densità dello schermo del dispositivo
- \[x] quando vuoi fornire una versione diversa della tua app con configurazione e risorse personalizzate

#### D14. Dato il frammento riportato di seguito, come si otterrebbe l'accesso a un oggetto TextView con un ID di text_home contenuto nel file di layout di una classe Fragment?

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

#### D15. Perché usi AndroidJUnitRunner quando esegui i test dell'interfaccia utente?

Avviso: AndroidJUnitRunner ci consente di eseguire test in stile JUnit3 / 4 su dispositivi Android

- \[x] Il test runner facilita il caricamento del pacchetto di test e dell'app sottoposta a test su un dispositivo o un emulatore, esegue il test e segnala i risultati.
- \[ ] Il test runner che crea schermate di ogni schermata visualizzata durante l'esecuzione dei test.
- \[ ] Il test runner facilita la parallelizzazione delle classi di test fornendo per ogni classe di test.
- \[ ] Il test runner facilita l'interazione con gli elementi visibili su un dispositivo, indipendentemente dall'attività o dal frammento che ha lo stato attivo.

#### D16. Cosa consente di ripristinare correttamente lo stato di un utente quando un'attività viene riavviata?

- \[ ] il metodo onSaveInstance()
- \[x] tutte queste risposte
- \[ ] archiviazione persistente
- \[ ] Oggetti ViewModel

[Rifrazione](https://developer.android.com/topic/libraries/architecture/saving-states)

#### D17. Data la definizione di seguito. come si otterrebbe l'accesso a un TextView con un ID di text_home contenuto nel file di layout thr di una classe Fragment?

- \[ ] root.find(R.id.text_home)
- \[ ] findViewById(R.id.text_home)
- \[ ] root.getById(R.id.text_home)
- \[x] root.findViewById(R.id.text_home)

#### D18. SE il thread principale è bloccato per troppo tempo, il sistema visualizza la finestra di dialogo \_?

- \[ ] Thread non risponde
- \[ ] Applicazione in pausa
- \[x] Applicazione non risponde
- \[ ] Applicazione bloccata

#### D19. Come si recupera il valore dell'e-mail di un utente da SharedPreferences assicurando al contempo che il valore restituito non sia null?

- \[ ] getPreferances(this).getString(Email,"")
- \[ ] getDefaultSharedPrefarances(this).getString(EMAIL,null)
- \[x] getDefaultSharedPreferances(this).getString(EMAIL,"")
- \[ ] getPreferances(this).getString(EMAIL,null)

**Spiegazione:** Nel metodo "getDefaultSharedPrefarances(this).getString()" viene passato il secondo parametro in modo che possa essere restituito, nel caso in cui la chiave non esista. Quindi dobbiamo passare una stringa vuota da restituire nel caso in cui la chiave non esista.

#### D20. Perché è problematico definire le dimensioni utilizzando i pixel su Android?

- \[ ] Sebbene la densità dei pixel dello schermo vari, ciò non influisce sull'uso dei pixel per definire le dimensioni.
- \[ ] I dispositivi di grandi dimensioni hanno sempre più pixel, quindi gli elementi dell'interfaccia utente saranno e=interessati se li definisci con pixel.
- \[x] Lo stesso numero di pixel può corrispondere a dimensioni fisiche diverse, influenzando l'aspetto degli elementi dell'interfaccia utente.
- \[ ] Diversi dispositivi hanno una diversa comprensione di cosa sia un pixel , influenzando l'aspetto degli elementi dell'interfaccia utente

[Riferimento](https://developer.android.com/training/multiscreen/screendensities#:~:text=The%20first%20pitfall%20you%20must,physical%20sizes%20on%20different%20devices.)

#### D21. È necessario ottenere un elenco di dispositivi collegati al computer con l'abilitazione del debug USB. Quale comando verrebbe eseguito utilizzando Android Debug Bridge?

- \[ ] elenca i dispositivi
- \[x] dispositivi adb
- \[ ] lista avd
- \[ ] dispositivi dir

#### D22. Quale definizione disegnabile ti consente di ottenere la forma sottostante?

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

#### D23. Per mantenere una piccola raccolta di dati chiave-valore, cosa dovresti usare?

- \[ ] archiviazione file esterna
- \[x] SharedPereferences
- \[ ] SQLite
- \[ ] memoria file interna

#### D24. È necessario recuperare un elenco di foto da un'API. Quale frammento di codice definisce una richiesta HTML GET in Retrofit?

- \[ ] @GET("photo/{id}"}
  fun listPhotos(@Path("id") id:Long?) : Chiama<Photo>
- \[ ] @LIST("foto")
  fun listPhotos() : Call\<List<Photo>>
- \[ ] @GET("foto")
  fun listPhotos() : Chiama<Photo>
- \[x] @GET("foto")
  fun listPhotos() : Call\<List<Photo>>

#### D25. Data la classe di test riportata di seguito, quale frammento di codice sarebbe un'asserzione corretta?

- \[ ] assertThat(resultAdd).is(2.0)
- \[x] assertNotNull(resultAdd)
- \[ ] assertThat(resultAdd).isWqualTo(2.0)
- \[ ] assertThat(resultAdd)

#### D26. Quale tag è necessario utilizzare per aggiungere un componente di visualizzazione riutilizzabile a un file di layout?

- \[ ] `<merge/>`
- \[x] `<include/>`
- \[ ] `<layout/>`
- \[ ] `<add/>`

#### D27. Si desidera fornire un drawable diverso per i dispositivi che sono in modalità orizzontale e la cui lingua è impostata su francese. quale directory è denominata correttamente?

- \[ ] fr-land-drawable
- \[x] drawable-fr-land
- \[ ] drawable-french-land
- \[ ] francese-terra-disegnabile

#### D28. Perché potrebbe essere necessario includere l'autorizzazione seguente per la tua app?

`android.permission.ACCESS_NETWORK_STATE`

- \[ ] per monitorare la posizione dei dispositivi in modo da non tentare di effettuare chiamate di rete quando l'utente è fermo
- \[ ] per richiedere la possibilità di effettuare chiamate di rete dalla tua app
- \[ ] per monitorare lo stato della rete del dispositivo in modo da poter visualizzare un banner in-app per l'utente
- \[x] per monitorare lo stato della rete dei dispositivi in modo da non tentare di effettuare chiamate di rete quando la rete non è disponibile

#### D29. Quale immagine corrisponde meglio alla seguente `LinearLayout`?

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

#### D30. Si desidera aprire l'app Dialer predefinita su un dispositivo. Cosa c'è di sbagliato in questo codice?

```java
  val dialerIntent = Intent()
  val et = findViewById(R.id.some_edit_text)
  dialerIntent.action = Intent.ACTION_DIAL
  dialerIntent.data = Uri.parse("tel:" + et.getText()?.toString())
  startActivity(dialerIntent)
```

- \[x] `startActivityWithResult()` dovrebbe essere usato al posto di `startActivity()` quando si utilizza `Intent.ACTION_DIAL`.
- \[ ] Per `Intent.ACTION_DIAL`Le `Intent` opzione `Intent.FLAG_ACTIVITY_NEW_TASK` deve essere aggiunto quando si utilizza questo `dialerIntent`.
- \[ ] Il `dialerIntent` causerà la visualizzazione di un'eccezione ActivityNotFoundException su dispositivi che non supportano `Intent.ACTION_DIAL`.
- \[ ] Il permesso `android.permission.CALL_PHONE` deve essere richiesto prima `Intent.ACTION_DIAL` può essere utilizzato.

#### D31. Quando è necessario archiviare i file nella finestra di dialogo `/assets` directory?

- \[x] quando è necessario accedere ai nomi dei file e alla gerarchia di file originali [(Riferimento)](https://medium.com/mobile-app-development-publication/assets-or-resource-raw-folder-of-android-5bdc042570e0)
- \[ ] quando è necessario accedere al file con il suo `resource ID`come `R.assets.filename`
- \[ ] quando si dispone di file XML che definiscono animazioni di interpolazione
- \[ ] quando è necessario accedere al file nella sua forma grezza utilizzando `Resources.openRawResource()`

#### D32. Vuoi consentire agli utenti di scattare foto nella tua app. Che è _non_ un vantaggio della creazione di un appropriato `intent`, invece di richiedere direttamente l'autorizzazione della fotocamera?

- \[ ] Gli utenti possono selezionare le loro app fotografiche preferite per scattare foto.
- \[ ] Non è necessario effettuare una richiesta di autorizzazione nell'app per scattare una foto.
- \[x] Hai il pieno controllo sull'esperienza utente. L'app che gestisce la fotocamera `intent` rispetterà le tue scelte progettuali.
- \[ ] Non è necessario progettare l'interfaccia utente. L'app che gestisce la fotocamera `intent` fornirà l'interfaccia utente.

#### D33. Quando useresti il `ActivityCompat.shouldShowRequestPermissionRationale()` funzione?

- \[ ] quando un utente apre per la prima volta la tua app e vuoi fornire una spiegazione per l'uso di una determinata autorizzazione
- \[ ] quando un utente ha precedentemente negato la richiesta di una determinata autorizzazione e seleziona "Dimmi di più"
- \[ ] quando un utente ha precedentemente negato la richiesta di una determinata autorizzazione e si desidera fornire una spiegazione per il suo utilizzo
- \[x] quando un utente ha precedentemente negato la richiesta di una determinata autorizzazione e ha selezionato "Non chiedere più", ma è necessaria l'autorizzazione per il funzionamento dell'app

#### D34. Desideri abilitare il monitoraggio analitico solo in `release` costruisce. Come è possibile creare un nuovo campo nel generato `BuildConfig` per memorizzare quel valore?

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

#### D35. Per ottimizzare le dimensioni dell'APK, quale codec immagine dovresti usare?

- \[ ] JPG
- \[ ] PNG
- \[ ] MPEG
- \[x] WebP [(Riferimento)](https://developer.android.com/topic/performance/reduce-apk-size#:~:text=packJPG%20and%20guetzli.-,Use%20WebP%20file%20format,than%20either%20JPEG%20or%20PNG.)

#### D36. È stato creato il codice per effettuare una chiamata di rete e si è verificato che funzioni nell'ambiente di sviluppo. Tuttavia, quando lo si pubblica nella console di riproduzione, la chiamata di rete non funziona. Cosa sarà _non_ aiutarti a risolvere questo problema?

- \[ ] verifica se `ProGuard` -keepclassmembers sono stati aggiunti agli oggetti di trasferimento dati di rete (DTO) in questione
- \[x] utilizzando gli strumenti profiler in Android Studio per rilevare anomalie nell'utilizzo della CPU, della memoria e della rete
- \[ ] verifica della presenza di eccezioni nei registri del server o nella console del server
- \[ ] verifica che l'oggetto di trasferimento dati di rete abbia `@SerizlizedName` applicato alle relative proprietà membro

#### D37. Quale snippet di codice raggiungerebbe il layout visualizzato di seguito?

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

#### D38. Quale set di origine è `_not_` disponibile per impostazione predefinita quando Android Studio crea un nuovo progetto?

- \[ ] test
- \[ ] androidTest
- \[ ] app
- \[x] principale

#### D39. Quale definizione impedirà ad altre app di accedere al tuo `Activity` tramite un `intent`?

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

**Spiegazione:** I filtri intento vengono usati per rendere le attività accessibili ad altre app usando gli intenti. Quindi dobbiamo scegliere l'opzione che non ha alcun filtro intento per assicurarci che non sia accessibile dall'intento

#### D40. Per preservare la memoria sul dispositivo, come è possibile determinare che il dispositivo dell'utente dispone di funzionalità di archiviazione limitate?

- \[x] Utilizzare il comando `ActivityManager.isLowRamDevice()` per scoprire se un dispositivo si definisce come "RAM insufficiente".
- \[ ] Utilizzare il comando `Activity.islowRam()` per scoprire se un dispositivo si definisce come "RAM insufficiente".
- \[ ] Utilizzare il comando `ConnectivityManager.hasLowMemory()` per scoprire se un dispositivo si definisce come "RAM insufficiente".
- \[ ] Effettuare una richiesta di download di immagini e controllare l'utilizzo rimanente della memoria del dispositivo.

#### D41. Cos'è `_not_` un buon modo per riutilizzare il codice Android?

- \[ ] Utilizzare un modulo Gradle comune condiviso da diversi progetti Android.
- \[ ] Preferisci creare visualizzazioni o frammenti personalizzati rispetto alle attività.
- \[x] Preferisci costruire attività invece di frammenti.
- \[ ] Suddividi i layout dell'interfaccia utente in elementi comuni e usa `<include/>` per includerli in altri file XML di layout.

#### D42. Qual è il layout migliore per gerarchie grandi e complesse?

- \[ ] LinearLayout
- \[x] VincoloLayout
- \[ ] FrameLayout
- \[ ] RelativeLayout

#### D43. È necessario eseguire l'aggiornamento all'ultima versione del plug-in Gradle per Android. Quale file modificare?

- \[ ] root_project_dir/app/build.gradle.
- \[ ] root_project_dir/settings.gradle.
- \[x] root_project_dir/build.gradle.
- \[ ] root_project_dir/app/gradle.properties.

[riferimento](https://developer.android.com/studio/releases/gradle-plugin#updating-plugin)

#### D44. Perché gli sviluppatori inseriscono spesso il codice di inizializzazione dell'app nella classe Application?

- \[x] La classe Application viene creata un'istanza prima di qualsiasi altra classe quando viene creato il processo per l'applicazione.
- \[ ] La classe Application viene creata un'istanza dopo eventuali richieste di autorizzazioni quando viene creato il processo per l'applicazione.
- \[ ] La classe Application viene creata ogni volta che viene avviata una nuova Attività, rendendola ideale per il codice di inizializzazione.
- \[ ] La classe Application viene creata ogni volta che viene chiamato un servizio in background, rendendola ideale per il codice di inizializzazione.

[riferimento](https://developer.android.com/reference/android/app/Application)

#### D45. Quale cartella usare per le icone di avvio dell'app?

- \[ ] /disegnabile
- \[ ] /icona
- \[x] /mipmap
- \[ ] /launcher

#### D46. Quale definizione disegnabile ti consente di ottenere la forma sottostante?

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

#### D47. Dato il ConstraintLayout di seguito, quale affermazione è vera?

![img](image/44.jpeg)

- \[ ] La vista B non è vincolata orizzontalmente.
- \[ ] View C ha troppi vincoli.
- \[x] La vista B non è vincolata verticalmente.
- \[ ] La vista C è vincolata al padre.

#### D48. Dato questo codice snippey da un file build.gradle, quale scelta non è una possibile variante di compilazione?

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

- \[ ] produzioneDebug.
- \[x] sviluppoDebug.
- \[ ] stagingDebug.
- \[ ] stagingRelease.

[Riferimento](https://developer.android.com/studio/build/build-variants#flavor-dimensions)

#### D49. Quando dovresti usare la directory androidTest per archiviare le tue classi di test?

- \[ ] quando i test consistono solo in unit test.
- \[ ] quando il numero di test da eseguire è elevato (500+).
- \[ ] quando i test devono essere eseguiti sul computer locale.
- \[x] quando i test devono essere eseguiti su dispositivi reali o virtuali.

[Riferimento](https://developer.android.com/studio/test#test_types_and_location)

#### D50. Dato un APK chiamato app-internal-debug.apk prodotto dal processo di compilazione, quale affermazione è probabile che sia vera?

- \[ ] Questo APK viene creato su una macchina per sviluppatori dal sapore del prodotto di debug.
- \[ ] Questo APK è stato creato dal sapore del prodotto internalDebug.
- \[ ] Questo APK creato dal sapore del prodotto di debug e dal tipo di build interno.
- \[x] Questo APK viene creato dal tipo di build di debug e dal sapore interno del prodotto.

#### D51. Quando si tenta di compilare il progetto, cosa potrebbe indicare il seguente errore?

`Conversion to Dalvik format filed: Unable to execute dex: method ID not in [0, 0xffff]: 65536`

- \[ ] Sono state incluse informazioni in formato incorect nel file build.gradle.
- \[ ] Sono state aggiunte più di 20 dipendenze al file build.gradle.
- \[x] È stato superato il numero totale di metodi a cui è possibile fare riferimento all'interno di un singolo file DEX.
- \[ ] Nel codice è presente un'eccezione NullPointerException.

#### D52. Quale affermazione, nel file build.gradle, indica correttamente che il modulo corrispondente è un modulo di libreria Android?

- \[ ] apply plugin: 'com.module.library'
- \[x] applica il plugin: 'com.android.library'
- \[ ] apply plugin: 'com.module.library'
- \[ ] include plugin: 'com.module.library'

#### D53. Dato il seguente file .xml, come definiresti un ImageView con spaziatura media nella parte inferiore?

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

#### D54. Qual è il vantaggio di esternalizzare le risorse dell'app, ad esempio immagine e stringa, da un codice?

- \[ ] Consente ad Android di scegliere la risorsa appropriata in base alla configurazione corrente durante il runtime.
- \[x] Consente di avere applicazioni più performanti perché il codice e le risorse sono separati.
- \[ ] Ti consente di fornire un'esperienza Ul diversa in base alle impostazioni della lingua dell'utente.
- \[ ] Consente di fornire un'esperienza Ul diversa in base alle dimensioni del dispositivo dell'utente.

#### D55. Qual è lo scopo principale della quinta riga in questo frammento di codice?

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

- \[ ] per assicurarsi che l'attività finisca quando savedInstanceState non è null
- \[x] per assicurarsi che l'attività crei un nuovo frammento ogni volta che viene ripristinata da uno stato precedente
- \[ ] per impedire la visualizzazione di due frammenti affiancati nei casi in cui l'attività viene ripristinata da uno stato precedente
- \[ ] per impedire la creazione di frammenti sovrapposti nei casi in cui l'attività viene ripristinata da uno stato precedente

#### D56. Quale componente non è un punto di ingresso attraverso il quale il sistema o un utente possono accedere all'app?

- \[ ] attività
- \[ ] fornitore di contenuti
- \[x] frammento
- \[ ] servizio

#### D57. Cosa usare per visualizzare un ampio elenco di elementi a scorrimento?

- \[ ] ListView
- \[x] Vista Riciclatore
- \[ ] LinearLayout
- \[ ] Scrollview

#### D58. Hai creato una classe AboutActivity che visualizza i dettagli sulla tua app. Quale snippet di codice ti consente di avviare la tua attività?

- \[ ] Intent(this, AboutActivity::class).also { intent ->
  startService(intento)
  }

- \[x] Intent(this, AboutActivity::class.java).also { intent ->
  startActivity(intento)
  }

- \[ ] Intent(this, AboutActivity::class).also { intent ->
  attività(intento)
  }

- \[ ] Intent(this, AboutActivity::class).also { intent ->
  startActivity(intento)
  }
  Spiegazione: Intent(Context packageContext, Class\<?> cls)
  Avviso: Classe non KClass

#### D59. Qual è l'uso del file AndroidManifest.xml?

- \[x] Descrive il componente dell'applicazione
- \[ ] Dichiara il livello minimo dell'API Android richiesta dall'applicazione
- \[ ] Facilita la fornitura di un nome univoco per l'applicazione specificando il nome del pacchetto
- \[ ] Tutto quanto sopra

#### D60. Quale attributo dell'elemento <uses-sdk> viene utilizzato per specificare il livello API minimo richiesto per l'esecuzione dell'applicazione?

- \[ ] android:targetSdkVersion
- \[x] androide: minSdkVersion
- \[ ] androide:maxSdkVersion
- \[ ] Nessuno dei precedenti

#### D61. Per ridurre il codice nelle build di rilascio, quale strumento utilizza Android Studio?

- \[x] R8
- \[ ] ProGuard
- \[ ] Termoretraitore
- \[ ] D8
  Spiegazione: Quando si compila il progetto utilizzando il plug-in Android Gradle 3.4.0 o versione successiva, il plug-in non utilizza più ProGuard per eseguire l'ottimizzazione del codice in fase di compilazione. Invece, il plugin funziona con il compilatore R8 per gestire

[Riferimento](https://developer.android.com/studio/build/shrink-code)

#### D62. Quale gerarchia di layout è probabile che venga disegnata più rapidamente?

- \[x] A
  ![img](https://i.imgur.com/mT08jag.png?raw=png)

- \[ ] B
  ![img](https://i.imgur.com/rz9eKYc.png?raw=png)

- \[ ] C
  ![img](https://i.imgur.com/ETaHhaS.png?raw=png)

- \[ ] D
  ![img](https://i.imgur.com/1QBrTwR.png?raw=png)

#### D63. Qual è il modo attualmente consigliato per gestire le attività in background a esecuzione prolungata?

- \[x] WorkManager
- \[ ] AsyncTask
- \[ ] IntentService
- \[ ] Discussione

[Riferimento](https://developer.android.com/guide/background)

#### D64. Devi fornire agli utenti alcune funzionalità della tua app on-demand o come esperienze istantanee tramite Google Play. Che tipo di modulo dovresti creare?

- \[ ] modulo libreria
- \[x] modulo di funzionalità dinamiche
- \[ ] Modulo app Android
- \[ ] Modulo Google Cloud

1.  [Riferimento](https://youtu.be/QdfStuj-MuA?t=86)
2.  [Riferimento](https://developer.android.com/guide/playcore/feature-delivery/on-demand)

#### D65. Quale approccio non è consigliato per fornire uno stato offline utile nella tua app?

- \[ ] memorizzazione dei dati nella cache
- \[ ] memorizzazione dei dati in locale
- \[ ] accodamento delle richieste in uscita all'azione quando la connettività è stata persa
- \[ ] notifica sempre agli utenti che la connettività è stata persa

#### D66. Se hai bisogno del codice dell'app per ispezionare le informazioni sulla compilazione corrente, quale classe usare?

- \[x] `BuildConfig`
- \[ ] `BuildInfo`
- \[ ] `ConfigParams`
- \[ ] `ConfigInfo`

#### D67. Nel constraintLayout riportato di seguito, perché il pulsante non dovrebbe espandersi per riempire la larghezza del padre?

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

#### D68. Cosa non è un caso d'uso per le risorse inattive nei test Espresso?

- \[ ] `managing system services`
- \[x] `processing user input events`
- \[ ] `loading data from the internet or a local data source`
- \[ ] `perfoming bitmap transformatinos`

#### D69. Che cos'è un tipo di risorsa per fornire stringhe all'app?

- \[ ] `String`
- \[x] `Text`
- \[ ] `String-array`
- \[ ] `Plurals`
