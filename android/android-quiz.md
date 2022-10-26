## Android

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
- [x] Add a Thread.sleep() call before you start the new activity.
- [ ] inspect the logs in Logcat.

#### Q4. Why might push notifications stop working?

- [x] all of these answers
- [ ] The device token is not being sent to push provider correctly.
- [ ] Google Play Services is not installed on the deivce/emulator.
- [ ] Battery optimization is turned on on the device.

#### Q5. What is the correct set of component classes needed to implement a RecyclerView of items that displays a list of widgets vertically?

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

#### Q6. The Android system kills process when it needs to free up memory. The likelihood of the system killing a given process depends on the state of the process and the activity at the time. With combination of process and activity state is most likely to be killed?

- [x] Process:In the background;Activity:Is stopped
- [ ] Process:In the background;Activity:Is paused
- [ ] Process:In the foreground;Activity:Is started
- [ ] Process:In the foreground;Activity:Is paused

#### Q7. You have created a NextActivity class that relies on a string containing some data that pass inside the intent Which code snippet allows you to launch your activity?

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

#### Q8. You want to include about and setting modules in your project. Which files accurately reflects their inclusion?

- [ ] `in build.gradle:include ':app',':about' ':settings'`
- [x] `in settings.gradle:include ':app',':about' ':settings'`
- [ ] `in settings.gradle:include ':about',':settings'`
- [ ] `in gradle.properties:include ':app',':about' ':settings'`

#### Q9. What is the benefit of using @VisibleForTesting annotation?

- [x] to denote that a class, methods, or field has its visibility relaxed to make code testable
- [ ] to denote that a class, method, or field is visible only in the test code
- [ ] to denote that a class, method, or field has its visibility increased to make code less testable
- [ ] to throw a run-time error if a class, methods, or field with this annotation is accessed improperly

#### Q10. How would you specify in your build.gradle file that your app required at least API level 21 to run, but that it can be tested on API level 28?

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

#### Q11. When will an activity's onActivityResult()be called?

- [ ] when calling finish()in the parent activity
- [ ] when placing an app into the background by sitching to another app
- [ ] When onStop() is called in the target activity
- [x] when calling finish() in the target activity

[Reference](https://developer.android.com/reference/android/app/Activity)

#### Q12. You need to remove an Event based on it;s id from your API, Which code snippet defines that request in Retrofit?

- [ ] @DELETE("events)
      fun deleteEvent(@Path("id") id: Long): Call<Unit>
- [x] @DELETE("events/{id}")
      fun deleteEvent(@Path("id") id: Long): Call<Unit>
- [ ] @REMOVE("events/{id}")
      fun deleteEvent(@Path("id") id: Long): Call<Unit>
- [x] @DELETE("events/{id}")
      fun deleteEvent(@Path("id") id: Long): Call<Unit>

#### Q13. When would you use a product flavour in your build setup?

- [ ] when you need to have the app's strings present in multiple lanuages
- [ ] when you have to provide different versions of your app based on the physical device size
- [ ] when you want to provide different versions of your app based on the device screen density
- [x] when you want to provide different version of your app with custom configuration and resources

#### Q14. Given the fragment below, how would you get access to a TextView with an ID of text_home contained in the layout file of a Fragment class?

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

#### Q15. Why do you use the AndroidJUnitRunner when running UI tests?

Notice: AndroidJUnitRunner lets us run JUnit3/4-style tests on Android Devices

- [x] The test runner facilitates loading your test package and the app under test onto a device or emulator, runs the test, and reports the results.
- [ ] The test runner creating screenshots of each screen that displayed while tests are executed.
- [ ] The test runner facilitates parallelization of test classes by providing for each test class.
- [ ] The test runner facilitates interacting with visible elements on a device, regardless of the activity or fragment that has focus.

#### Q16. What allows you to properly restore a user's state when an activity is restarted?

- [ ] the onSaveInstance()method
- [x] all of these answers
- [ ] persistent storage
- [ ] ViewModel objects

[Refrence](https://developer.android.com/topic/libraries/architecture/saving-states)

#### Q17. Given the definition below. how would you get access a TextView with an ID of text_home contained in thr layout file of a Fragment class?

- [ ] root.find(R.id.text_home)
- [ ] findViewById(R.id.text_home)
- [ ] root.getById(R.id.text_home)
- [x] root.findViewById(R.id.text_home)

#### Q18. IF the main thread is blocked for too long, the system displays the \_ dialog?

- [ ] Thread Not Responding
- [ ] Application Paused
- [x] Application Not Responding
- [ ] Application Blocked

#### Q19. How would you retrieve the value of a user's email from SharedPreferences while ensuring that the returned value is not null?

- [ ] getPreferances(this).getString(Email,"")
- [ ] getDefaultSharedPrefarances(this).getString(EMAIL,null)
- [x] getDefaultSharedPreferances(this).getString(EMAIL,"")
- [ ] getPreferances(this).getString(EMAIL,null)

**Explanation:** `In Method "getDefaultSharedPrefarances(this).getString()" Second parameter is passed so that it can be returned, in case key doesn't exist. So we need to pass an empty string to be returned in case key doesn't exist.`

#### Q20. Why is it problematic to define sizes using pixels on Android?

- [ ] Although screen pixel density varies, this does not impact the use of pixels to define sizes.
- [ ] Large devices always have more pixels, so your UI elements will be e=affected if you define them with pixels.
- [x] The same number of pixels may correspond to different physical sizes, affecting the appearance of your UI elements.
- [ ] Different devices have different understanding of what a pixel is , affecting the appearance of your UI elements

[Reference](https://developer.android.com/training/multiscreen/screendensities#:~:text=The%20first%20pitfall%20you%20must,physical%20sizes%20on%20different%20devices.)

#### Q21. You need to get a list of devices that are attached to your computer with USB debugging enable. Which command would execute using the Android Debug Bridge?

- [ ] list devices
- [x] adb devices
- [ ] list avd
- [ ] dir devices

#### Q22. Which drawable definition allows you to achieve the shape below?

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

#### Q23. To persist a small collection of key-value data, what should you use?

- [ ] external file storage
- [x] SharedPereferences
- [ ] SQLite
- [ ] internal file storage

#### Q24. You need to retrieve a list of photos from an API. Which code snippet defines an HTML GET request in Retrofit?

- [ ] @GET("photo/{id}"}
      fun listPhotos(@Path("id") id:Long?) : Call<Photo>
- [ ] @LIST("photo")
      fun listPhotos() : Call<List<Photo>>
- [ ] @GET("photo")
      fun listPhotos() : Call<Photo>
- [x] @GET("photo")
      fun listPhotos() : Call<List<Photo>>

#### Q25. Given the test class below, which code snippet would be a correct assertion?

- [ ] assertThat(resultAdd).is(2.0)
- [x] assertNotNull(resultAdd)
- [ ] assertThat(resultAdd).isWqualTo(2.0)
- [ ] assertThat(resultAdd)

#### Q26. What tag should you use to add a reusable view component to a layout file?

- [ ] `<merge/>`
- [x] `<include/>`
- [ ] `<layout/>`
- [ ] `<add/>`

#### Q27. You want to provide a different drawable for devices that are in landscape mode and whose language is set to French. which directory is named correctly?

- [ ] fr-land-drawable
- [x] drawable-fr-land
- [ ] drawable-french-land
- [ ] french-land-drawable

#### Q28. Why might you need to include the following permission to your app?

`android.permission.ACCESS_NETWORK_STATE`

- [ ] to monitor the location of the devices so that you don't attempt to make network calls when the user is stationary
- [ ] to request the ability to make network calls from your app
- [ ] to monitor the network state of the device so that you can display an in-app banner to the user
- [x] to monitor the network state of the devices so that you don't attempt to make network calls when the network is unavailable

#### Q29. Which image best corresponds to the following `LinearLayout`?

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

#### Q30. You want to open the default Dialer app on a device. What is wrong with this code?

```
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

#### Q31. When should you store files in the `/assets` directory?

- [x] when you need access to the original file names and file hierarchy
- [ ] when you need access to the file with its `resource ID`, like `R.assets.filename`
- [ ] when you have XML files that define tween animations
- [ ] when you need to access the file in its raw form using `Resources.openRawResource()`

[Reference](https://medium.com/mobile-app-development-publication/assets-or-resource-raw-folder-of-android-5bdc042570e0)

#### Q32. You want to allow users to take pictures in your app. Which is _not_ an advantage of creating an appropriate `intent`, instead of requesting the camera permission directly?

- [ ] Users can select their favorite photo apps to take pictures.
- [ ] You do not have to make a permission request in your app to take a picture.
- [x] You have full control over the user experience. The app that handles the camera `intent` will respect your design choices.
- [ ] You do not have to design the UI. The app that handles the camera `intent` will provide the UI.

#### Q33. When would you use the `ActivityCompat.shouldShowRequestPermissionRationale()` function?

- [ ] when a user first opens your app and you want to provide an explanation for the use of a given permission
- [ ] when a user has previously denied the request for a given permission and selects "Tell me more"
- [ ] when a user has previously denied the request for a given permission and you want to provide an explanation for its use
- [x] when a user has previously denied the request for a given permission and selected "Don't ask again," but you need the permission for your app to function

#### Q34. You would like to enable analytics tracking only in `release` builds. How can you create a new field in the generated `BuildConfig` class to store that value?

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

#### Q35. To optimize your APK size, what image codec should you use?

- [ ] JPG
- [ ] PNG
- [ ] MPEG
- [x] WebP

[Reference](https://developer.android.com/topic/performance/reduce-apk-size#:~:text=packJPG%20and%20guetzli.-,Use%20WebP%20file%20format,than%20either%20JPEG%20or%20PNG.)

#### Q36. You have built code to make a network call and tested that it works in your development environment. However, when you publish it to the Play console, the networking call fails to work. What will _not_ help you troubleshoot this issue?

- [ ] checking whether `ProGuard` -keepclassmembers have been added to the network data transfer objects (DTOs) in question
- [x] using the profiler tools in Android Studio to detect anomalies in CPU, memory, and network usage
- [ ] checking for exceptions in the server logs or server console
- [ ] checking that the network data transfer object has `@SerizlizedName` applied to its member properties

#### Q37. Which code snippet would achieve the layout displayed below?

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

#### Q38. Which source set is `_not_` available to you by default when Android Studio creates a new project?

- [ ] test
- [ ] androidTest
- [ ] app
- [x] main

#### Q39. Which definition will prevent other apps from accessing your `Activity` class via an `intent`?

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

**Explanation:** `Intent filters are used to make activities accessible to other apps using intents. So we have to choose option which have no intent filter to make sure it is not accessible by intent`

#### Q40. To preserve on-device memory, how might you determine that the user's device has limited storage capabilities?

- [x] Use the `ActivityManager.isLowRamDevice()` method to find out whether a device defines itself as "low RAM."
- [ ] Use the `Activity.islowRam()` method to find out whether a device defines itself as "low RAM."
- [ ] Use the `ConnectivityManager.hasLowMemory()` method to find out whether a device defines itself as "low RAM."
- [ ] Make an image download request and check the remaining device storage usage.

#### Q41. What is `_not_` a good way to reuse Android code?

- [ ] Use a common Gradle module shared by different Android projects.
- [ ] Prefer to build custom views or fragments over activities.
- [x] Prefer to build activities instead of fragments.
- [ ] Break down UI layouts into common elements and use `<include/>` to include them in other layout XML files.

#### Q42. Which layout is best for large, complex hierarchies?

- [ ] LinearLayout
- [x] ConstraintLayout
- [ ] FrameLayout
- [ ] RelativeLayout

#### Q43. You need to upgrade to the latest version of the Android Gradle plugin. Which file should you modify?

- [ ] root_project_dir/app/build.gradle.
- [ ] root_project_dir/settings.gradle.
- [x] root_project_dir/build.gradle.
- [ ] root_project_dir/app/gradle.properties.

[reference](https://developer.android.com/studio/releases/gradle-plugin#updating-plugin)

#### Q44. Why do developers often put app initialization code in the Application class?

- [x] The Application class is instantiated before any other class when the process for the application is created.
- [ ] The Application class is instantiated after any permissions requests when the process for the application is created.
- [ ] The Application class is created each time a new Activity is launched, making it ideal for initialization code.
- [ ] The Application class is created each time a background service is called, making it ideal for initialization code.

[reference](https://developer.android.com/reference/android/app/Application)

#### Q45. What folder should you use for your app's launcher icons?

- [ ] /drawable
- [ ] /icon
- [x] /mipmap
- [ ] /launcher

#### Q46. Which drawable definition allows you to achieve the shape below?

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

#### Q47. Given the ConstraintLayout below, which statement is true?

![img](image/44.jpeg)

- [ ] View B is not horizontally constrained.
- [ ] View C has too many constraints.
- [x] View B is not vertically constrained.
- [ ] View C is constrained to the parent.

#### Q48. Given this code snippey from a build.gradle file, which choice is not a possible build variant?

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

[Reference](https://developer.android.com/studio/build/build-variants#flavor-dimensions)

#### Q49. When should you use the androidTest directory to store your test classes?

- [ ] when the tests consist only of unit tests.
- [ ] when the number of tests to run is large(500+).
- [ ] when the tests need to run on your local machine.
- [x] when the tests need to run on real or virtual devices.

[Reference](https://developer.android.com/studio/test#test_types_and_location)

#### Q50. Given an APK named app-internal-debug.apk produced from the build process, which statement is likely to be true?

- [ ] This APK is created on a developer machine from the debug product flavor.
- [ ] This APK is created from the internalDebug product flavor.
- [ ] This APK created from the debug product flavor and internal build type.
- [x] This APK is created from the debug build type and internal product flavor.

#### Q51. When attempting to build your project, what might the following error indicate?

`Conversion to Dalvik format filed: Unable to execute dex: method ID not in [0, 0xffff]: 65536`

- [ ] You have included incorect format information in your build.gradle file.
- [ ] You have added more than 20 dependencies to your build.gradle.
- [x] You have exceeded the total number of methods that can be referenced within a single DEX file.
- [ ] You have a NullPointerException in your code.

#### Q52. Which statement, in build.gradle file, correctly denotes that the corresponding module is an Android library module?

- [ ] apply plugin: 'com.module.library'
- [x] apply plugin: 'com.android.library'
- [ ] apply plugin: 'com.module.library'
- [ ] include plugin: 'com.module.library'

#### Q53. Given the following dimens.xml file, how would you define an ImageView with medium spacing at the bottom?

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

#### Q54. what is not a benefit of externalizing app resources such as image and string from a code?

- [ ] It allows Android to choose the appropriate resource based on the current configuration during runtime.
- [x] It allows you to have more performant applications because the code and resources are separated.
- [ ] It allows you to provide a different Ul experience based on the user's language settings.
- [ ] It allows you to provide a different Ul experience based on the user's device size.

#### Q55. What is the chief purpose of line five in this code snippet?

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

- [ ] to make sure that the activity finishes when the savedInstanceState is not null
- [x] to make sure that the activity creates a new fragment each time it is restored from a previous state
- [ ] to prevent the display of two fragments side by side in cases where the activity is restored from a previous state
- [ ] to prevent the creation of overlapping fragments in cases where the activity is restored from a previous state

#### Q56. Which component is not an entry point through which the system or a user can enter your app?

- [ ] activity
- [ ] content provider
- [x] fragment
- [ ] service

#### Q57. What should you use to display a large, scrolling list of elements?

- [ ] ListView
- [x] Recycler View
- [ ] LinearLayout
- [ ] Scrollview

#### Q58. You have created an AboutActivity class that displays details about your app. Which code snippet allows you to launch your activity?

- [ ] `Intent(this, AboutActivity::class).also { intent -> startService(intent)}`
- [x] `Intent(this, AboutActivity::class.java).also { intent -> startActivity(intent)}`
- [ ] `Intent(this, AboutActivity::class).also { intent -> activity(intent)}`
- [ ] `Intent(this, AboutActivity::class).also { intent -> startActivity(intent)}`

**Explanation**: `Intent(Context packageContext, Class<?> cls) Notice: Class not KClass`

#### Q59. What is the use of AndroidManifest.xml file?

- [x] It describes the component of the application
- [ ] It declares the minimum level of the android API that the application requires
- [ ] It facilitates to provide a uinque name for the application by specifying package name
- [ ] All of the above

#### Q60. Which attribute of the element <uses-sdk> is used to specify the minimum API Level required for the application to run?

- [ ] android:targetSdkVersion
- [x] android:minSdkVersion
- [ ] android:maxSdkVersion
- [ ] None of the above

#### Q61. To shrink your code in release builds, what tool does Android Studio use?

- [x] R8
- [ ] ProGuard
- [ ] Shrinker
- [ ] D8

**Explanation**: `When you build your project using Android Gradle plugin 3.4.0 or higher, the plugin no longer uses ProGuard to perform compile-time code optimization. Instead, the plugin works with the R8 compiler to handle`

[Reference](https://developer.android.com/studio/build/shrink-code)

#### Q62. Which layout hierarchy is likely to be drawn the most quickly?

- [x] A
      ![img](https://i.imgur.com/mT08jag.png?raw=png)

- [ ] B
      ![img](https://i.imgur.com/rz9eKYc.png?raw=png)

- [ ] C
      ![img](https://i.imgur.com/ETaHhaS.png?raw=png)

- [ ] D
      ![img](https://i.imgur.com/1QBrTwR.png?raw=png)

#### Q63. What is the current recommended way to handle long-running background tasks?

- [x] WorkManager
- [ ] AsyncTask
- [ ] IntentService
- [ ] Thread

[Reference](https://developer.android.com/guide/background)

#### Q64. You need to provide your users with certain features of your app on-demand or as instant experiences through Google Play. Which type of module should you create?

- [ ] library module
- [x] dynamic feature module
- [ ] Android app module
- [ ] Google Cloud module

1. [Reference](https://youtu.be/QdfStuj-MuA?t=86)
2. [Reference](https://developer.android.com/guidgite/playcore/feature-delivery/on-demand)

#### Q65. Which approach is not recommended for providing a useful offline state in your app?

- [ ] caching data
- [ ] storing data locally
- [ ] queuing outbound requests to action when connectivity has been lost
- [x] always notifying users that connectivity has been lost

[Reference](https://developer.android.com/docs/quality-guidelines/build-for-billions/connectivity#network-offline)

#### Q66. If you need your app code to inspect information about the current build, which class should you use?

- [x] `BuildConfig`
- [ ] `BuildInfo`
- [ ] `ConfigParams`
- [ ] `ConfigInfo`

#### Q67. In the ConstraintLayout below, why wouldn't button expand to fill the width of parent?

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

- [ ] `The button does not have a size`
- [x] `The button is not constrained to the end of the parent container`
- [ ] `Buttons cannot expand beyond their default size`
- [ ] `The button should have its height set to 0dp as well`

#### Q68. What is not a use case for idling resources in your Espresso tests?

- [ ] `managing system services`
- [x] `processing user input events`
- [ ] `loading data from the internet or a local data source`
- [ ] `perfoming bitmap transformatinos`

#### Q69. What is not a type of resource for providing your app with strings?

- [ ] `String`
- [x] `Text`
- [ ] `String-array`
- [ ] `Plurals`

#### Q70. What is not in the activity lifecycle?

- [ ] `onPause()`
- [ ] `onResume()`
- [x] `onOpen()`
- [ ] `onStart()`

#### Q71. You want to allow users to take a picture in your app. Which code snippet is the correct approach?

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
