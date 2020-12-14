#### Q1. To add features, components, and permissions to your Android app, which file needs to be edited?

- [x] AndroidManifest.xml
- [ ] Components.xml
- [ ] AppManifest.xml
- [ ] ComponentManifest.xml

#### Q2. Which XML attribute should be used to make an Image View accessible?

- [ ] android:talkBack
- [ ] android:labelFor
- [ ] android:hint
- [x] android:contentDescription

#### Q3. You launch your app, and when you navigate to a new screen it crashes, Which action will NOT help you diagnose the issue?

- [ ] Set breakpoints and then step through the code line by line
- [ ] Use the profiler tools in Android Studio to detect anomalies CPU, and network usage.
- [x] Add a Thread.sleep()call before you start the new activity.
- [ ] inspect the logs in Logcat.

#### Q4. Why might push notifications stop working?

- [x] all of these answers
- [ ] The device token is not being sent to push provider correctly.
- [ ] Google Play Services is not installed on the deivce/emulator.
- [ ] Battery optimization is turned on on the device.

#### Q5. What is correct set of classes needed to implement a RecyclerView of items that displays a list of widgets vertically?

```
      RecycleView
      RecyclerView.Adapter
      RecyclerView.ViewHolder<T extends BaseViewHolder>
      LinearLayoutManager
```

```
      RecycleView
      RecyclerView.Adapter
      RecyclerView.ViewHolder
      LinearLayoutManager
```

```
      RecycleView
x    RecyclerView.Adapter<VH extends ViewHolder>
      RecyclerView.ViewHolder
      LinearLayoutManager
```

#### Q6. The Android system kills process when it needs to free up memory. The likelihood of the system killing a given process depends on the state of the process and the activity at the time. With combination of process and activity state is most likely to be killed?

- [x] Process:In the background;Activity:Is stopped
- [ ] Process:In the background;Activity:Is paused
- [ ] Process:In the foreground;Activity:Is started
- [ ] Process:In the foreground;Activity:Is paused

#### Q7. You have created a NextActivity class that relies on a string containing some data that pass inside the intent Which code snippet allows you to launch your activity?

```kotlin
        Intent(this, NextActivity::class.java).also { intent ->
            startActivity(intent)
        }
```

```kotlin
        Intent(this, NextActivity::class.java).apply {
            put(EXTRA_NEXT, "some data")
        }.also { intent ->
            activityStart(intent)
        }
```

```kotlin
        Intent(this, NextActivity::class.java).apply {
            putExtra(EXTRA_NEXT, "some data")
x      }.also { intent ->
            startActivity(intent)
        }
```

```kotlin
        Intent(this, NextActivity::class.java).apply {
            put(EXTRA_NEXT, "some data")
        }.also { intent ->
            activityStart(intent)
        }

```

#### Q8. You want to include about and setting modules in your project. Which files accurately reflects their inclusion?

- [ ] in build.gradle:include ':app',':about' ':settings'
- [x] in settings.gradle:include ':app',':about' ':settings'
- [ ] in settings.gradle:include ':about',':settings'
- [ ] in gradle.properties:include ':app',':about' ':settings'

#### Q9. What is the benifit of using @VisibleForTesting annotation?

- [x] to denote that a class, methos, or field has its visibility relaxed to make code testable
- [ ] to denote that a class, method, or field is visible only in the test code
- [ ] to denote that a class, method, or field has its visibility increased to make code less testable
- [ ] to throw a run-time error if a class, methos, or field with this annotation is accessed improperly

#### Q10. How would you specify in your build.gradle file that your app required at least API level 21 to run, but that it can be tested on API level 28?

```gradle
      defaultConfig {
        ...
        minApiVersion 21
        targetApiVersion 28
      }
```

```gradle
      defaultConfig {
        ...
        targetSdkVersion 21
        testSdkVersion 28
      }
```

```gradle
      defaultConfig {
        ...
        minSdkVersion 21
        testApiVersion 28
      }
```

```gradle
      defaultConfig {
        ...
x      minSdkVersion 21
        targetSdkVersion 28
      }
```

#### Q11. When will an activity's onActivityResult()be called?

- [ ] when calling finish()in the parent activity
- [ ] when placing an app into the background by sitching to another app
- [ ] When onStop() is called in the target activity
- [x] when calling finish() in the target activity

#### Q12. You need to remove an Event based on it;s id from your API, Which code snippet defines that request in Retrofit?

- [ ] @DELETE("events)
      fun deleteEvent(@Path("id") id: Long): Call<Unit>
- [ ] @DELETE("events/{id}")
      fun deleteEvent(@Path("id") id: Long): Call<Unit> (correct)
- [ ] @REMOVE("events/{id}")
      fun deleteEvent(@Path("id") id: Long): Call<Unit>
- [ ] @DELETE("events/{id}")
      fun deleteEvent(@Path("id") id: Long): Call<Unit> (correct)

#### Q13. When would you use a product flavour in your build setup?

- [ ] when you need to have the app's strings present in multiple lanuages
- [ ] when you have to provide different versions of your app based on the physical device size
- [ ] when you want to provide different versions of your app based on the device screen density
- [x] when you want to provide different version of your app with custom configuration and resources

#### Q14. Given the fragment below, how would you get access to a TextView with an ID of text_home contained in the layout file of a Fragment class?

```kotlin
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

#### Q15. Why do you use the AndroidJUnitRunner when running UI tests?

- [x] The test runner facilitates loading your test package and the app under test onto a device or emulator, runs the test, and reports the results.
- [ ] The test runner creating screenshots of each screen that displayed while tests are executed.
- [ ] The test runner facilitates parallelization of test classes by providing for each test class.
- [ ] The test runner facilitates interacting with visible elements on a device, regardless of the activity or fragment that has focus.

#### Q16. WWhat allows you to properly restore a user's state when an activity is restarted?

- [ ] the onSaveInstance()method
- [ ] all of these answers
- [ ] persistent storage
- [ ] ViewModel objects

#### Q17. Given the defination below. how would you get access a TextView with an ID of text_home contained in thr layout file of a Fragment class?

- [ ] root.find(R.id.text_home)
- [ ] findViewById(R.id.text_home)
- [ ] root.getById(R.id.text_home)
- [x] root.findViewById(R.id.text_home)

#### Q18. IF the main thread is blocked for too long, the system displays the\_\_\_dialog?

- [ ] Thread Not Responding
- [ ] Application Paused
- [x] Application Not Responding
- [ ] Application Blocked

#### Q19. How would you retrive the value of a user's email from SharedPreferances while ensuring that the returned value is not null?

- [ ] getPreferances(this).getString(Email,"")
- [ ] getDefaultSharedPrefarances(this).getString(EMAIL,null)
- [ ] getDefaultSharedPreferances(this).getString(EMAIL,"")
- [ ] getPreferances(this).getString(EMAIL,null)

#### Q20. Why is it problematic to define sizes using pixels on Android?

- [ ] Although screen pixel density vary,this does not impact the use of pixels to define sizes.
- [ ] Large devices always have more pixels so your UI elements will be effected if you define them with pixels.
- [ ] The same number of pixels may corresponds to different physical sizes, affecting the appearance of your UI elements.
- [x] Different devices have different understanding of what a pixel is , affecting the appearance of your UI elements

#### Q20. You need to get a listing devices that are attached to your computer with USB debugging enable. Which command would execute using the Android Debug Bridge?

- [ ] list devices
- [x] adb devices
- [ ] list avd
- [ ] dir devices

#### Q21. Which drawable defination allows you to achieve the shape below?

![img](image/shape.png)

```xml
      <shape xmlns:android="http://schemas.android.com/apk/res/android"
          android:shape="oval">
          <stroke
              android:width="4dp"
              android:color="@android:color/white" />
          <solid android:color="@android:color/black" />
      </shape>
```

```xml
      <oval xmlns:android="http://schemas.android.com/apk/res/android">
          <stroke android:width="4dp" android:color="@android:color/black"/>
          <solid android:color="@android:color/white"/>
      </oval>
```

```xml
      <shape xmlns:android="http://schemas.android.com/apk/res/android"
          android:shape="oval">
          <stroke
x            android:width="4dp"
              android:color="@android:color/black" />
          <solid android:color="@android:color/white" />
      </shape>
```

```xml
      <shape xmlns:android="http://schemas.android.com/apk/res/android"
          android:shape="oval">
          <stroke
              android:width="4dp"
              android:color="@android:color/white" />
          <solid android:color="@android:color/white" />
      </shape>
```

#### Q22. To persist a small collection of key-value data, what should you use?

- [ ] external file storage
- [x] SharedPereferences
- [ ] SQLite
- [ ] internal file storage

#### Q22. You need to retrive a list of photos from an API. Which code snippet defines an HTML GET request in Retrofit?

- [ ] @GET("photo/{id}"}
      fun listPhotos(@Path("id") id:Long?) : Call<Photo>
- [ ] @LIST("photo")
      fun listPhotos() : Call<List<Photo>>
- [ ] @GET("photo")
      fun listPhotos() : Call<Photo>
- [x] @GET("photo")
      fun listPhotos() : Call<List<Photo>>

#### Q23. Given the test class below, which code snippet would be a correct assertion?

- [ ] assertThat(resultAdd).is(2.0)
- [x] assertNotNull(resultAdd)
- [ ] assertThat(resultAdd).isWqualTo(2.0)
- [ ] assertThat(resultAdd)

#### Q24. What tag should you use to add a reusable view component to a layour file?

- [ ] `<merge/>`
- [x] `<include/>`
- [ ] `<layout/>`
- [ ] `<add/>`

#### Q25. You want to provide a different drawable for devices that are in landscape mode and whose language is set to French. which directory is named correctly?

- [ ] fr-land-drawable
- [x] drawable-fr-land
- [ ] drawable-french-land
- [ ] french-land-drawable

#### Q26. Why might you need to include the following permission to your app?

android.permission.ACCESS_NETWORK_STATE

- [ ] to monitor the location of the devices so that you don't attempt to make network calls when the user is stationary
- [x] to request the ability to make network calls from your app
- [ ] to monitor the network state of the device so that you can display an in-app banner to the user
- [ ] to monitor the network state of the devices so that you don't attempt to make network calls when the network is unavailable

#### Q27. Which image best corresponds to the following `LinearLayout`?

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
- [ ] B
      ![img](image/01.jpeg)
- [x] C
      ![img](image/02.jpeg)
- [ ] D
      ![img](image/03.jpeg)

#### Q28. You want to open the default Dialer app on a device. What is wrong with this code?

```java
val dialerIntent = Intent()
val et = findViewById(R.id.some_edit_text)
dialerIntent.action = Intent.ACTION_DIAL
dialerIntent.data = Uri.parse("tel:" + et.getText()?.toString())
startActivity(dialerIntent)
```

- [x] `startActivityWithResult()` should be used instead of `startActivity()` when using `Intent.ACTION_DIAL`.
- [ ] For `Intent.ACTION_DIAL`, the `Intent` option `Intent.FLAG_ACTIVITY_NEW_TASK` must be added when using this `dialerIntent`.
- [ ] The `dialerIntent` will cause an ActivityNotFoundException to be thrown on devices that do not support `Intent.ACTION_DIAL`.
- [ ] The permission `android.permission.CALL_PHONE` must be requested first before `Intent.ACTION_DIAL` can be used.

#### Q29. When should you store files in the `/assets` directory?

- [x] when you need access to the original file names and file hierarchy
- [ ] when you need access to the file with its `resource ID`, like `R.assets.filename`
- [ ] when you have XML files that define tween animations
- [ ] when you need to access the file in its raw form using `Resources.openRawResource()`

#### Q30. You want to allow users to take pictures in your app. Which is _not_ an advantage of creating an appropriate `intent`, instead of requesting the camera permission directly?

- [ ] Users can select their favorite photo apps to take pictures.
- [ ] You do not have to make a permission request in your app to take a picture.
- [x] You have full control over the user experience. The app that handles the camera `intent` will respect your design choices.
- [ ] You do not have to design the UI. The app that handles the camera `intent` will provide the UI.

#### Q31. When would you use the `ActivityCompat.shouldShowRequestPermissionRationale()` function?

- [ ] when a user first opens your app and you want to provide an explanation for the use of a given permission
- [ ] when a user has previously denied the request for a given permission and selects "Tell me more"
- [ ] when a user has previously denied the request for a given permission and you want to provide an explanation for its use
- [x] when a user has previously denied the request for a given permission and selected "Don't ask again," but you need the permission for your app to function

#### Q32. You would like to enable analytics tracking only in `release` builds. How can you create a new field in the generated `BuildConfig` class to store that value?

- [ ]

```xml
buildTypes {
	debug {
		buildConfig 'boolean', 'ENABLE_ANALYTICS', 'false'
	}
	release {
		buildConfig 'boolean', 'ENABLE_ANALYTICS', 'true'
	}
}
```

- [ ]

```xml
buildTypes {
	debug {
		buildConfig 'String', 'ENABLE_ANALYTICS', 'false'
	}
	release {
		buildConfig 'String', 'ENABLE_ANALYTICS', 'true'
	}
}
```

- [x]

```xml
buildTypes {
	debug {
		buildConfigField 'boolean', 'ENABLE_ANALYTICS', 'false'
	}
	release {
		buildConfigField 'boolean', 'ENABLE_ANALYTICS', 'true'
	}
}
```

- [ ]

```xml
buildTypes {
	debug {
		buildConfigField 'boolean', 'ENABLE_ANALYTICS', 'true'
	}
	release {
		buildConfigField 'boolean', 'ENABLE_ANALYTICS', 'false'
	}
}
```

#### Q33. To optimize your APK size, what image codec should you use?

- [ ] JPG
- [ ] PNG
- [ ] MPEG
- [x] WebP

#### Q34. You have built code to make a network call and tested that it works in your development environment. However, when you publish it to the Play console, the networking call fails to work. What will _not_ help you troubleshoot this issue?

- [ ] checking whether `ProGuard` -keepclassmembers have been added to the network data transfer objects (DTOs) in question
- [x] using the profiler tools in Android Studio to detect anomalies in CPU, memory, and network usage
- [ ] checking for exceptions in the sever logs or server console
- [ ] checking that the network data transfer object has `@SerizlizedName` applied to its member properties

#### Q35. Which code snippet would achieve the layout displayed below?

![img](image/04.jpeg)

- [ ]

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

- [x]

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

- [ ]

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

- [ ]

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

#### Q36. Which source set is _not_ available to you by default when Android Studio creates a new project?

- [ ] test
- [ ] androidTest
- [ ] app
- [x] main

#### Q37. Which definition will prevent other apps from accessing your `Activity` class via an `intent`?

- [ ]

```xml
	<activity android:name=".ExampleActivity" />
```

- [x]

```xml
	<activity android:name=".ExampleActivity">
		<intent-filter>
			<action android:name="android.intent.action.SEND" />
		</intent-filter>
	</activity>
```

- [ ]

```xml
	<activity android:name=".ExampleActivity">
		<intent-filter>
			<action android:name="android.intent.action.MAIN" />
			<category android:name="android.intent.category.LAUNCHER" />
		</intent-filter>
	</activity>
```

- [ ]

```xml
	<activity android:name=".ExampleActivity">
		<intent-filter>
			<action android:name="android.intent.action.VIEW" />
		</intent-filter>
	</activity>
```

#### Q38. To preserve on-device memory, how might you determine that the user's device has limited storage capabilities?

- [x] Use the `ActivityManager.isLowRamDevice()` method to find out whether a device defines itself as "low RAM."
- [ ] Use the `Activity.islowRam()` method to find out whether a device defines itself as "low RAM."
- [ ] Use the `ConnectivityManager.hasLowMemory()` method to find out whether a device defines itself as "low RAM."
- [ ] Make an image download request and check the remaining device storage usage.

#### Q39. What is _not_ a good way to reuse Android code?

- [ ] Use a common Gradle module shared by different Android projects.
- [ ] Prefer to build custom views or fragments over activities.
- [ ] Prefer to build activities instead of fragments.
- [x] Break down UI layouts into common elements and use `<include/>` to include them in other layout XML files.

#### Q40. Which layout is best for large, complex hierarchies?

- [ ] LinearLayout
- [ ] ConstraintLayout
- [ ] FrameLayout
- [ ] RelativeLayout

#### Q41. Why do developers often put app initialization code in the Application class?

- [ ] The Application class is instantiated before any other class when the process for the application is created.
- [ ] The Application class is instantiated after any permissions requests when the process for the application is created.
- [ ] The Application class is created each time a new Activity is launched, making it ideal for initialization code.
- [ ] The Application class is created each time a background service is called, making it ideal for initialization code.

#### Q42. What folder should you use for your app's launcher icons?

- [ ] /drawable
- [ ] /icon
- [ ] /mipmap
- [ ] /launcher

#### Q43. Which drawable definition allows you to achieve the shape below?

![img](image/43.jpeg)

- [ ]

```xml
	<shape xmlns:android-"http://schemas.android.com/apk/res/android"
	    android:shape-"oval">
	    <gradient
               android:startColor-"@android:color/white"
               android:endColor-"@android:color/black"
               android:angle-"45"/>
	</shape>
```

- [ ]

```xml
	<rectangle xmlns:android-"http://schemas.android.com/apk/res/android">
	   <gradient
	      android:startColor-"@android:color/white"
	      android:endColor-"android:color/black"
	      android:angle-"135"/>
	</rectangle>
```

- [ ]

```xml
	<shape xmlns:android-"http://schemas.android.com/apk/res/android"
	   android:shape-"rectangle">
	   <gradient
	      android:startColor-"@android:color/white"
	      android:endColor-"@android:color/black"
	      android:angle-"135"/>
	</shape>
```

- [ ]

```xml
	<shape xmlns:android-"http://schemas.android.com/apk/res/android"
	   android:shape-"rectangle">
	   <gradient
	      android:startColor-"@android:color/white"
	      android:endColor-"@android:color/black"
	      android:angle-"98"/>
	</shape>
```

#### Q44. Given the ConstraintLayout below, which statement is true?

![img](image/44.jpeg)

- [ ] View B is not horizontally constrained.
- [ ] View C has too many constraints.
- [ ] View B is not vertically constrained.
- [ ] View C is constrained to the parent.
