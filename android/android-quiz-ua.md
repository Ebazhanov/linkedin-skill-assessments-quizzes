# Андроїд

#### Питання 1. Який файл потрібно відредагувати, щоб додати функції, компоненти та дозволи до вашого Android-додатку?

- [x] AndroidManifest.xml
- [ ] Components.xml
- [ ] AppManifest.xml
- [ ] ComponentManifest.xml

#### Питання 2. Який XML-атрибут слід використовувати, щоб зробити ImageView доступним?

- [ ] android:talkBack
- [ ] android:labelFor
- [ ] android:hint
- [x] android:contentDescription

#### Питання 3. Ви запускаєте свій додаток, і коли переходите на новий екран, він падає. Яка дія НЕ допоможе вам діагностувати проблему?

- [ ] Встановити точки зупинки та пройти код рядок за рядком
- [ ] Використовувати інструменти профілювання в Android Studio для виявлення аномалій у використанні CPU та мережі
- [x] Додати виклик Thread.sleep() перед запуском нової активності
- [ ] Перевірити логи в Logcat

#### Питання 4. Чому push-повідомлення можуть перестати працювати?

- [x] усі ці відповіді
- [ ] Токен пристрою не надсилається правильно постачальнику push-повідомлень
- [ ] Google Play Services не встановлено на пристрої/емуляторі
- [ ] Оптимізація батареї увімкнена на пристрої

#### Питання 5. Який правильний набір класів компонентів потрібен для реалізації RecyclerView елементів, що відображає список віджетів вертикально?

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

#### Питання 6. Система Android знищує процес, коли потрібно звільнити пам'ять. Ймовірність знищення системою даного процесу залежить від стану процесу та активності в даний момент. При якій комбінації стану процесу та активності найбільш ймовірно буде знищено?

- [x] Процес: У фоні; Активність: Зупинена
- [ ] Процес: У фоні; Активність: Призупинена
- [ ] Процес: На передньому плані; Активність: Запущена
- [ ] Процес: На передньому плані; Активність: Призупинена

#### Питання 7. Ви створили клас NextActivity, який залежить від рядка з деякими даними, що передаються всередині intent. Який фрагмент коду дозволяє запустити вашу активність?

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

#### Питання 8. Ви хочете включити модулі about та settings у свій проект. Які файли точно відображають їх включення?

- [ ] `в build.gradle: include ':app',':about' ':settings'`
- [x] `в settings.gradle: include ':app',':about' ':settings'`
- [ ] `в settings.gradle: include ':about',':settings'`
- [ ] `в gradle.properties: include ':app',':about' ':settings'`

#### Питання 9. Яка перевага використання анотації @VisibleForTesting?

- [x] позначити, що клас, метод або поле має послаблену видимість для можливості тестування коду
- [ ] позначити, що клас, метод або поле видимі тільки в тестовому коді
- [ ] позначити, що клас, метод або поле має підвищену видимість, щоб зробити код менш тестованим
- [ ] викликати помилку часу виконання, якщо до класу, методу або поля з цією анотацією здійснюється неправильний доступ

#### Питання 10. Як би ви вказали у вашому файлі build.gradle, що ваш додаток вимагає принаймні рівень API 21 для запуску, але може бути протестований на рівні API 28?

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

#### Питання 11. Коли буде викликано onActivityResult() активності?

- [ ] при виклику finish() у батьківській активності
- [ ] при переведенні додатку у фоновий режим шляхом перемикання на інший додаток
- [ ] коли викликається onStop() у цільовій активності
- [x] при виклику finish() у цільовій активності

[Посилання](https://developer.android.com/reference/android/app/Activity)

#### Питання 12. Вам потрібно видалити подію на основі її ID з вашого API. Який фрагмент коду визначає цей запит у Retrofit?

- [ ] @DELETE("events)
      fun deleteEvent(@Path("id") id: Long): Call<Unit>
- [x] @DELETE("events/{id}")
      fun deleteEvent(@Path("id") id: Long): Call<Unit>
- [ ] @REMOVE("events/{id}")
      fun deleteEvent(@Path("id") id: Long): Call<Unit>
- [x] @DELETE("events/{id}")
      fun deleteEvent(@Path("id") id: Long): Call<Unit>

#### Питання 13. Коли ви б використовували product flavor у налаштуваннях збірки?

- [ ] коли потрібно мати рядки додатку, присутні на декількох мовах
- [ ] коли потрібно надати різні версії вашого додатку на основі фізичного розміру пристрою
- [ ] коли потрібно надати різні версії вашого додатку на основі щільності екрану пристрою
- [x] коли потрібно надати іншу версію вашого додатку з індивідуальною конфігурацією та ресурсами

#### Питання 14. За умови фрагмента нижче, як би ви отримали доступ до TextView з ID text_home, що міститься у файлі макета класу Fragment?

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

#### Питання 15. Чому ви використовуєте AndroidJUnitRunner при запуску UI-тестів?

Примітка: AndroidJUnitRunner дозволяє нам запускати тести в стилі JUnit3/4 на Android-пристроях

- [x] Тестовий виконавець полегшує завантаження вашого тестового пакету та додатку під тестування на пристрій або емулятор, запускає тест і повідомляє про результати
- [ ] Тестовий виконавець створює скріншоти кожного екрану, що відображається під час виконання тестів
- [ ] Тестовий виконавець полегшує паралелізацію тестових класів, надаючи для кожного тестового класу
- [ ] Тестовий виконавець полегшує взаємодію з видимими елементами на пристрої, незалежно від активності або фрагмента, що має фокус

#### Питання 16. Що дозволяє вам правильно відновити стан користувача при перезапуску активності?

- [ ] метод onSaveInstance()
- [x] усі ці відповіді
- [ ] постійне сховище
- [ ] об'єкти ViewModel

[Посилання](https://developer.android.com/topic/libraries/architecture/saving-states)

#### Питання 17. Якщо головний потік заблокований занадто довго, система відображає діалог \_.

- [ ] Thread Not Responding
- [ ] Application Paused
- [x] Application Not Responding
- [ ] Application Blocked

#### Питання 18. Як би ви отримали значення електронної пошти користувача з SharedPreferences, переконавшись, що повернене значення не є null?

- [ ] getPreferances(this).getString(Email,"")
- [ ] getDefaultSharedPrefarances(this).getString(EMAIL,null)
- [x] getDefaultSharedPreferances(this).getString(EMAIL,"")
- [ ] getPreferances(this).getString(EMAIL,null)

**Пояснення:** `У методі "getDefaultSharedPrefarances(this).getString()" другий параметр передається так, щоб він міг бути повернений, якщо ключ не існує. Тому нам потрібно передати порожній рядок для повернення у випадку, якщо ключ не існує.`

#### Питання 19. Чому проблематично визначати розміри, використовуючи пікселі на Android?

- [ ] Хоча щільність пікселів екрану варіюється, це не впливає на використання пікселів для визначення розмірів
- [ ] Великі пристрої завжди мають більше пікселів, тому ваші елементи UI будуть порушені, якщо ви визначите їх за допомогою пікселів
- [x] Та сама кількість пікселів може відповідати різним фізичним розмірам, що впливає на вигляд ваших елементів UI
- [ ] Різні пристрої мають різне розуміння того, що таке піксель, що впливає на вигляд ваших елементів UI

[Посилання](https://developer.android.com/training/multiscreen/screendensities#:~:text=The%20first%20pitfall%20you%20must,physical%20sizes%20on%20different%20devices.)

#### Питання 20. Вам потрібно отримати список пристроїв, підключених до вашого комп'ютера з увімкненим налагодженням USB. Яка команда виконається за допомогою Android Debug Bridge?

- [ ] list devices
- [x] adb devices
- [ ] list avd
- [ ] dir devices

#### Питання 21. Яке визначення drawable дозволяє досягти форми нижче?

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

#### Питання 22. Для збереження невеликої колекції даних ключ-значення, що слід використовувати?

- [ ] зовнішнє файлове сховище
- [x] SharedPereferences
- [ ] SQLite
- [ ] внутрішнє файлове сховище

#### Питання 23. Вам потрібно отримати список фотографій з API. Який фрагмент коду визначає HTTP GET-запит у Retrofit?

- [ ] @GET("photo/{id}"}
      fun listPhotos(@Path("id") id:Long?) : Call<Photo>
- [ ] @LIST("photo")
      fun listPhotos() : Call<List<Photo>>
- [ ] @GET("photo")
      fun listPhotos() : Call<Photo>
- [x] @GET("photo")
      fun listPhotos() : Call<List<Photo>>

#### Питання 24. За умови тестового класу нижче, який фрагмент коду буде правильним твердженням?

- [ ] assertThat(resultAdd).is(2.0)
- [x] assertNotNull(resultAdd)
- [ ] assertThat(resultAdd).isWqualTo(2.0)
- [ ] assertThat(resultAdd)

#### Питання 25. Який тег слід використовувати для додавання компонента багаторазового використання до файлу макета?

- [ ] `<merge/>`
- [x] `<include/>`
- [ ] `<layout/>`
- [ ] `<add/>`

#### Питання 26. Ви хочете надати інший drawable для пристроїв, що знаходяться в альбомному режимі і мова яких встановлена на французьку. який каталог названо правильно?

- [ ] fr-land-drawable
- [x] drawable-fr-land
- [ ] drawable-french-land
- [ ] french-land-drawable

#### Питання 27. Чому вам може знадобитися включити наступний дозвіл до вашого додатку?

`android.permission.ACCESS_NETWORK_STATE`

- [ ] для моніторингу місцезнаходження пристроїв, щоб ви не намагалися здійснювати мережеві виклики, коли користувач нерухомий
- [ ] для запиту можливості здійснювати мережеві виклики з вашого додатку
- [ ] для моніторингу мережевого стану пристрою, щоб ви могли відображати банер у додатку для користувача
- [x] для моніторингу мережевого стану пристроїв, щоб ви не намагалися здійснювати мережеві виклики, коли мережа недоступна

#### Питання 28. Яке зображення найкраще відповідає наступному `LinearLayout`?

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

#### Питання 29. Ви хочете відкрити стандартний додаток Dialer на пристрої. Що не так з цим кодом?

```
val dialerIntent = Intent()
val et = findViewById(R.id.some_edit_text)
dialerIntent.action = Intent.ACTION_DIAL
dialerIntent.data = Uri.parse("tel:" + et.getText()?.toString())
startActivity(dialerIntent)
```

- [x] `startActivityWithResult()` слід використовувати замість `startActivity()` при використанні `Intent.ACTION_DIAL`
- [ ] Для `Intent.ACTION_DIAL`, опція `Intent` `Intent.FLAG_ACTIVITY_NEW_TASK` має бути додана при використанні цього `dialerIntent`
- [ ] `dialerIntent` викличе ActivityNotFoundException на пристроях, які не підтримують `Intent.ACTION_DIAL`
- [ ] Дозвіл `android.permission.CALL_PHONE` повинен бути запитаний спочатку, перш ніж можна буде використовувати `Intent.ACTION_DIAL`

#### Питання 30. Коли слід зберігати файли в каталозі `/assets`?

- [x] коли потрібен доступ до оригінальних імен файлів та ієрархії файлів
- [ ] коли потрібен доступ до файлу з його `resource ID`, наприклад `R.assets.filename`
- [ ] коли у вас є XML-файли, які визначають tween-анімації
- [ ] коли потрібно отримати доступ до файлу в його необробленій формі, використовуючи `Resources.openRawResource()`

[Посилання](https://medium.com/mobile-app-development-publication/assets-or-resource-raw-folder-of-android-5bdc042570e0)

#### Питання 31. Ви хочете дозволити користувачам робити фотографії у вашому додатку. Що _не є_ перевагою створення відповідного `intent`, замість прямого запиту дозволу камери?

- [ ] Користувачі можуть вибрати свої улюблені фотододатки для фотографування
- [ ] Вам не потрібно робити запит на дозвіл у вашому додатку, щоб зробити фотографію
- [x] Ви маєте повний контроль над досвідом користувача. Додаток, що обробляє `intent` камери, поважатиме ваші рішення щодо дизайну
- [ ] Вам не потрібно проектувати UI. Додаток, що обробляє `intent` камери, надасть UI

#### Питання 32. Коли б ви використовували функцію `ActivityCompat.shouldShowRequestPermissionRationale()`?

- [ ] коли користувач вперше відкриває ваш додаток і ви хочете пояснити використання даного дозволу
- [ ] коли користувач раніше відхилив запит на даний дозвіл і вибирає "Розкажіть мені більше"
- [ ] коли користувач раніше відхилив запит на даний дозвіл і ви хочете пояснити його використання
- [x] коли користувач раніше відхилив запит на даний дозвіл і вибрав "Не питати знову", але вам потрібен дозвіл для функціонування вашого додатку

#### Питання 33. Ви хотіли б увімкнути відстеження аналітики лише у `release` збірках. Як ви можете створити нове поле у згенерованому класі `BuildConfig` для зберігання цього значення?

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

#### Питання 34. Для оптимізації розміру APK, який кодек зображень слід використовувати?

- [ ] JPG
- [ ] PNG
- [ ] MPEG
- [x] WebP

[Посилання](https://developer.android.com/topic/performance/reduce-apk-size#:~:text=packJPG%20and%20guetzli.-,Use%20WebP%20file%20format,than%20either%20JPEG%20or%20PNG.)

#### Питання 35. Ви створили код для здійснення мережевого виклику і протестували, що він працює у вашому середовищі розробки. Однак, коли ви публікуєте його в консолі Play, мережевий виклик не працює. Що _не_ допоможе вам усунути цю проблему?

- [ ] перевірка, чи були додані -keepclassmembers `ProGuard` до об'єктів передачі мережевих даних (DTO)
- [x] використання інструментів профілювання в Android Studio для виявлення аномалій у використанні CPU, пам'яті та мережі
- [ ] перевірка виключень у логах сервера або консолі сервера
- [ ] перевірка, що об'єкт передачі мережевих даних має `@SerizlizedName`, застосований до його властивостей-членів

#### Питання 36. Який фрагмент коду досягне макету, показаного нижче?

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

#### Питання 37. Який набір джерел _не_ доступний вам за замовчуванням, коли Android Studio створює новий проект?

- [ ] test
- [ ] androidTest
- [ ] app
- [x] main

#### Питання 38. Яке визначення запобіжить доступу інших додатків до вашого класу `Activity` через `intent`?

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

**Пояснення:** `Intent-фільтри використовуються для забезпечення доступності активностей іншим додаткам за допомогою intent. Тому ми повинні вибрати варіант, у якому немає intent-фільтра, щоб переконатися, що він недоступний через intent`

#### Питання 39. Для збереження пам'яті на пристрої, як ви можете визначити, що пристрій користувача має обмежені можливості зберігання?

- [x] Використовуйте метод `ActivityManager.isLowRamDevice()`, щоб дізнатися, чи визначає себе пристрій як "низька оперативна пам'ять"
- [ ] Використовуйте метод `Activity.islowRam()`, щоб дізнатися, чи визначає себе пристрій як "низька оперативна пам'ять"
- [ ] Використовуйте метод `ConnectivityManager.hasLowMemory()`, щоб дізнатися, чи визначає себе пристрій як "низька оперативна пам'ять"
- [ ] Зробіть запит на завантаження зображення і перевірте залишок використання сховища пристрою

#### Питання 40. Що _не є_ хорошим способом повторного використання коду Android?

- [ ] Використовувати спільний модуль Gradle, що використовується різними проектами Android
- [ ] Віддавати перевагу створенню власних представлень або фрагментів над активностями
- [x] Віддавати перевагу створенню активностей замість фрагментів
- [ ] Розбивати макети UI на загальні елементи та використовувати `<include/>` для їх включення в інші XML-файли макетів

#### Питання 41. Який макет найкращий для великих, складних ієрархій?

- [ ] LinearLayout
- [x] ConstraintLayout
- [ ] FrameLayout
- [ ] RelativeLayout

#### Питання 42. Вам потрібно оновитися до останньої версії плагіна Android Gradle. Який файл слід змінити?

- [ ] root_project_dir/app/build.gradle
- [ ] root_project_dir/settings.gradle
- [x] root_project_dir/build.gradle
- [ ] root_project_dir/app/gradle.properties

[посилання](https://developer.android.com/studio/releases/gradle-plugin#updating-plugin)

#### Питання 43. Чому розробники часто розміщують код ініціалізації додатку в класі Application?

- [x] Клас Application створюється раніше за будь-який інший клас, коли процес для додатку створюється
- [ ] Клас Application створюється після будь-яких запитів дозволів, коли процес для додатку створюється
- [ ] Клас Application створюється кожного разу, коли запускається нова Activity, що робить його ідеальним для коду ініціалізації
- [ ] Клас Application створюється кожного разу, коли викликається фонова служба, що робить його ідеальним для коду ініціалізації

[посилання](https://developer.android.com/reference/android/app/Application)

#### Питання 44. Яку папку слід використовувати для іконок запуску вашого додатку?

- [ ] /drawable
- [ ] /icon
- [x] /mipmap
- [ ] /launcher

#### Питання 45. Яке визначення drawable дозволяє досягти форми нижче?

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

#### Питання 46. За умови ConstraintLayout нижче, яке твердження є правильним?

![img](image/44.jpeg)

- [ ] View B не має горизонтальних обмежень
- [ ] View C має занадто багато обмежень
- [x] View B не має вертикальних обмежень
- [ ] View C обмежено до батьківського елемента

#### Питання 47. За умови цього фрагмента коду з файлу build.gradle, який вибір не є можливим варіантом збірки?

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

- [ ] productionDebug
- [x] developmentDebug
- [ ] stagingDebug
- [ ] stagingRelease

[Посилання](https://developer.android.com/studio/build/build-variants#flavor-dimensions)

#### Питання 48. Коли слід використовувати каталог androidTest для зберігання ваших тестових класів?

- [ ] коли тести складаються лише з unit-тестів
- [ ] коли кількість тестів для запуску велика (500+)
- [ ] коли тести повинні запускатися на вашій локальній машині
- [x] коли тести повинні запускатися на реальних або віртуальних пристроях

[Посилання](https://developer.android.com/studio/test#test_types_and_location)

#### Питання 49. За умови APK з назвою app-internal-debug.apk, створеного з процесу збірки, яке твердження, ймовірно, є правильним?

- [ ] Цей APK створено на машині розробника з debug product flavor
- [ ] Цей APK створено з internalDebug product flavor
- [ ] Цей APK створено з debug product flavor та internal build type
- [x] Цей APK створено з debug build type та internal product flavor

#### Питання 50. При спробі збірки вашого проекту, що може вказувати наступна помилка?

`Conversion to Dalvik format filed: Unable to execute dex: method ID not in [0, 0xffff]: 65536`

- [ ] Ви включили неправильну інформацію про формат у ваш файл build.gradle
- [ ] Ви додали більше 20 залежностей до вашого build.gradle
- [x] Ви перевищили загальну кількість методів, на які можна посилатися в одному файлі DEX
- [ ] У вас є NullPointerException у вашому коді

#### Питання 51. Яке твердження у файлі build.gradle правильно вказує, що відповідний модуль є модулем бібліотеки Android?

- [ ] apply plugin: 'com.module.library'
- [x] apply plugin: 'com.android.library'
- [ ] apply plugin: 'com.module.library'
- [ ] include plugin: 'com.module.library'

#### Питання 52. За умови наступного файлу dimens.xml, як би ви визначили ImageView з середнім інтервалом знизу?

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

#### Питання 53. Що не є перевагою винесення ресурсів додатку, таких як зображення та рядки, з коду?

- [ ] Це дозволяє Android вибирати відповідний ресурс на основі поточної конфігурації під час виконання
- [x] Це дозволяє мати більш продуктивні додатки, оскільки код і ресурси розділені
- [ ] Це дозволяє надавати інший досвід UI на основі мовних налаштувань користувача
- [ ] Це дозволяє надавати інший досвід UI на основі розміру пристрою користувача

#### Питання 54. Яка головна мета п'ятого рядка в цьому фрагменті коду?

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

- [ ] переконатися, що активність завершується, коли savedInstanceState не є null
- [x] переконатися, що активність створює новий фрагмент кожного разу, коли вона відновлюється з попереднього стану
- [ ] запобігти відображенню двох фрагментів поруч у випадках, коли активність відновлюється з попереднього стану
- [ ] запобігти створенню перекриваючихся фрагментів у випадках, коли активність відновлюється з попереднього стану

#### Питання 55. Який компонент не є точкою входу, через яку система або користувач можуть увійти у ваш додаток?

- [ ] activity
- [ ] content provider
- [x] fragment
- [ ] service

#### Питання 56. Що слід використовувати для відображення великого прокручуваного списку елементів?

- [ ] ListView
- [x] RecyclerView
- [ ] LinearLayout
- [ ] Scrollview

#### Питання 57. Ви створили клас AboutActivity, який відображає деталі про ваш додаток. Який фрагмент коду дозволяє вам запустити вашу активність?

- [ ] `Intent(this, AboutActivity::class).also { intent -> startService(intent)}`
- [x] `Intent(this, AboutActivity::class.java).also { intent -> startActivity(intent)}`
- [ ] `Intent(this, AboutActivity::class).also { intent -> activity(intent)}`
- [ ] `Intent(this, AboutActivity::class).also { intent -> startActivity(intent)}`

**Пояснення**: `Intent(Context packageContext, Class<?> cls) Примітка: Class, а не KClass`

#### Питання 58. Яке призначення файлу AndroidManifest.xml?

- [x] Він описує компонент додатку
- [ ] Він оголошує мінімальний рівень Android API, який вимагає додаток
- [ ] Він полегшує надання унікального імені додатку шляхом вказівки імені пакета
- [ ] Усе вищезазначене

#### Питання 59. Який атрибут елемента <uses-sdk> використовується для вказівки мінімального рівня API, необхідного для запуску додатку?

- [ ] android:targetSdkVersion
- [x] android:minSdkVersion
- [ ] android:maxSdkVersion
- [ ] Жоден з наведених вище

#### Питання 60. Для зменшення вашого коду в release-збірках, який інструмент використовує Android Studio?

- [x] R8
- [ ] ProGuard
- [ ] Shrinker
- [ ] D8

**Пояснення**: `Коли ви збираєте свій проект, використовуючи плагін Android Gradle 3.4.0 або вище, плагін більше не використовує ProGuard для виконання оптимізації коду під час компіляції. Натомість плагін працює з компілятором R8 для обробки`

[Посилання](https://developer.android.com/studio/build/shrink-code)

#### Питання 61. Яка ієрархія макетів, ймовірно, буде намальована найшвидше?

- [x] A
      ![img](https://i.imgur.com/mT08jag.png?raw=png)

- [ ] B
      ![img](https://i.imgur.com/rz9eKYc.png?raw=png)

- [ ] C
      ![img](https://i.imgur.com/ETaHhaS.png?raw=png)

- [ ] D
      ![img](https://i.imgur.com/1QBrTwR.png?raw=png)

#### Питання 62. Який поточний рекомендований спосіб обробки довгих фонових завдань?

- [x] WorkManager
- [ ] AsyncTask
- [ ] IntentService
- [ ] Thread

[Посилання](https://developer.android.com/guide/background)

#### Питання 63. Вам потрібно надати вашим користувачам певні функції вашого додатку на вимогу або як миттєві враження через Google Play. Який тип модуля слід створити?

- [ ] модуль бібліотеки
- [x] модуль динамічної функції
- [ ] модуль додатку Android
- [ ] модуль Google Cloud

1. [Посилання](https://youtu.be/QdfStuj-MuA?t=86)
2. [Посилання](https://developer.android.com/guidgite/playcore/feature-delivery/on-demand)

#### Питання 64. Який підхід не рекомендується для забезпечення корисного офлайн-стану у вашому додатку?

- [ ] кешування даних
- [ ] локальне зберігання даних
- [ ] постановка в чергу вихідних запитів для дії при втраті зв'язку
- [x] завжди сповіщати користувачів про втрату зв'язку

[Посилання](https://developer.android.com/docs/quality-guidelines/build-for-billions/connectivity#network-offline)

#### Питання 65. Якщо вам потрібно, щоб код вашого додатку перевіряв інформацію про поточну збірку, який клас слід використовувати?

- [x] `BuildConfig`
- [ ] `BuildInfo`
- [ ] `ConfigParams`
- [ ] `ConfigInfo`

#### Питання 66. У ConstraintLayout нижче, чому кнопка не розширюється, щоб заповнити ширину батьківського елемента?

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

- [ ] `Кнопка не має розміру`
- [x] `Кнопка не обмежена до кінця батьківського контейнера`
- [ ] `Кнопки не можуть розширюватися за межі їхнього розміру за замовчуванням`
- [ ] `Висота кнопки також повинна бути встановлена на 0dp`

#### Питання 67. Що не є випадком використання для idling resources у ваших Espresso-тестах?

- [ ] `керування системними службами`
- [x] `обробка подій введення користувача`
- [ ] `завантаження даних з Інтернету або локального джерела даних`
- [ ] `виконання перетворень bitmap`

#### Питання 68. Що не є типом ресурсу для надання вашому додатку рядків?

- [ ] `String`
- [x] `Text`
- [ ] `String-array`
- [ ] `Plurals`

#### Питання 69. Що не входить у життєвий цикл активності?

- [ ] `onPause()`
- [ ] `onResume()`
- [x] `onOpen()`
- [ ] `onStart()`

#### Питання 70. Ви хочете дозволити користувачам робити фотографії у вашому додатку. Який фрагмент коду є правильним підходом?

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

#### Питання 71. За умови рядкового ресурсу нижче, який фрагмент коду є дійсним?

```
<string name="upload_photo_notification">%1$d of %2$d photos uploaded</string>
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

[Посилання](https://developer.android.com/guide/topics/resources/string-resource#formatting-strings)

#### Питання 72. Різні мови мають різні правила граматичної угоди з кількістю. Для підтримки наступних двох рядків кількома мовами у вашому додатку, яке ідеальне визначення ресурсу?

```
"You have 1 day remaining"
"You have 2 days remaining"
```

- [ ] A

```
<string name="trial_days_left_one"> You have %1$d day remaining</string>
<string name="trial_days_left_other">You have %1$d days remaining</string>
```

- [ ] B

```
<plurals name="trial days left">
    <plural quantity="one">You have %1$d day remaining</plural>
    <plural quantity="other">You have %1$d days remaining</plural>
</plurals>
```

- [x] C

```
<plurals name="trial_days_left">
    <item quantity="one">You have %1$d day remaining</item>
    <item quantity="other">You have %1$d days remaining</item>
</plurals>
```

- [ ] D

```
<string name="trial_days_left">
    <plural quantity="one">You have %1$d day remaining</plural>
    <plural quantity="other">You have &1$d days remaining</plural>
</string>
```

#### Питання 73. Коли операційна система використовує метод onTrimMemory()?

- [ ] `коли додаток видаляється`
- [x] `коли додаток переходить у фоновий режим`
- [ ] `коли пристрій знаходиться в режимі оптимізації батареї`
- [ ] `коли мережеві запити виконуються в головному потоці`

[Посилання](https://developer.android.com/guide/topics/resources/string-resource#Plurals)

#### Питання 74. У вашому додатку є RecyclerView елементів. Ви хочете мати різну конфігурацію для портретного та альбомного режимів. який фрагмент коду дозволить вам найкраще підтримати макет нижче?

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

#### Питання 75. Вам потрібно видалити подію на основі її ID з вашого API. Який фрагмент коду визначає цей запит у Retrofit?

- [ ] @DELETE("events)
      fun deleteEvent(@Path("id") id: Long): Call<Unit>
- [x] @DELETE("events/{id}")
      fun deleteEvent(@Path("id") id: Long): Call<Unit>
- [ ] @REMOVE("events/{id}")
      fun deleteEvent(@Path("id") id: Long): Call<Unit>
- [x] @DELETE("events/{id}")
      fun deleteEvent(@Path("id") id: Long): Call<Unit>

#### Питання 76. Ви хочете дозволити користувачам робити фотографії у вашому додатку. Що _не є_ перевагою створення відповідного `intent`, замість прямого запиту дозволу камери?

- [ ] Користувачі можуть вибрати свої улюблені фотододатки для фотографування
- [ ] Вам не потрібно робити запит на дозвіл у вашому додатку, щоб зробити фотографію
- [x] Ви маєте повний контроль над досвідом користувача. Додаток, що обробляє `intent` камери, поважатиме ваші рішення щодо дизайну
- [ ] Вам не потрібно проектувати UI. Додаток, що обробляє `intent` камери, надасть UI

#### Питання 77. Який поточний рекомендований спосіб обробки довгих фонових завдань?

- [x] WorkManager
- [ ] AsyncTask
- [ ] IntentService
- [ ] Thread
