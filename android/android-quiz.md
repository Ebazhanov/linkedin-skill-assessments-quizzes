#### Q1. To add features, components, and permissions to your Android app, which file needs to be edited?

- [x] AndroidManifest.xml
- [ ] Components.xml
- [ ] AppManifest.xml
- [ ] ComponentManifest.xml

#### Q2. Which XML attribute should be used to make an Image View accessible?

- [ ] android:talkBack
- [ ] android:labelFor
- [ ] android:hint
- [ ] android:contentDescription

#### Q3. You launch your app, and when you navigate to a new screen it crashes, Which action will NOT help you diagnose the issue?

- [ ] Set breakpoints and then step through the code line by line
- [ ] Use the profiler tools in Android Studio to detect anomalies CPU, and network usage.
- [ ] Add a Thread.sleep()call before you start the new activity.
- [ ] inspect the logs in Logcat.

#### Q4. Why might push notifications stop working?

- [ ] all of these answers
- [ ] The device token is not being sent to push provider correctly.
- [ ] Google Play Services is not installed on the deivce/emulator.
- [ ] Battery optimization is turned on on the device.

#### Q5. What is correct set of classes needed to implement a RecyclerView of items that displays a list of widgets vertically?

      RecycleView
- [ ] RecyclerView.Adapter
      RecyclerView.ViewHolder<T extends BaseViewHolder>
      LinearLAyoutManager
      
      RecycleView
- [ ] RecyclerView.Adapter
      RecyclerView.ViewHolder
      LinearLAyoutManager
      
#### Q6. The Android system kills process when it needs to free up memory. The likelihood of the system killing a given process depends on the state of the process and the activity at the time. With combination of process and activity state is most likely to be killed?

- [ ] Process:In the background;Activity:Is stopped
- [ ] Process:In the background;Activity:Is paused
- [ ] Process:In the foreground;Activity:Is started
- [ ] Process:In the foreground;Activity:Is paused

#### Q7. You have created a NextActivity class that relies on a string containing some data that pass inside the intent Which code snippt allows you to launch your activity?

      Intent(this, NextActivity::class.java).also { intent ->
- [ ] startActivity(intent)
      }
      
      Intent(this, NextActivity::class.java).apply {
      put(EXTRA_NEXT, "some data")
- [ ] }.also { intent ->
      activityStart(intent)
      }
      
      Intent(this, NextActivity::class.java).apply {
      putExtra(EXTRA_NEXT, "some data")
- [ ] }.also { intent ->
      startActivity(intent)
      }
      
      Intent(this, NextActivity::class.java).apply {
      put(EXTRA_NEXT, "some data")
- [ ] }.also { intent ->
      activityStart(intent)
      }
      
#### Q8. You want to include about and setting modules in your project. Which files accurately reflects their inclusion?

- [ ] in build.gradle:include ':app',':about' ':seetings'
- [ ] in settings.gradle:include ':app',':about' ':seetings'
- [ ] in settings.gradle:include ':about',':seeting'
- [ ] in gradle.properties:include ':app',':about' ':seetings'

#### Q9. What is the benifit of using @VisibleForTesting annotation?

- [ ] to denote that a class, methos, or field has its visibility relaxed to make code testable
- [ ] to denote that a class, method, or field is visible only in the test code
- [ ] to denote that a class, method, or field has its visibility increased to make code less testable
- [ ] to throw a run-time error if a class, methos, or field with this annotation is accessed improperly

#### Q10. How would you specify in your build.gradle file that your app required at least API level 21 to run, but that it can be tested on API level 28?

      defaultConfig {
        ...
- [ ]   minApiVersion 21
        targetApiVersion 28
        }

      defaultConfig {
        ...
- [ ]   targetSdkVersion 21
        testSdkVersion 28
        }
        
      defaultConfig {
        ...
- [ ]   minApiVersion 21
        testApiVersion 28
        }
        
      defaultConfig {
        ...
- [ ]   minApiVersion 21
        targetSdkVersion 28
        }
        
#### Q11. When will an activity's onActivityResult()be called?

- [ ] when calling finish()in the parent activity
- [ ] when placing an app into the background by sitching to another app
- [ ] When onStop() is called in the target activity
- [ ] when calling finish() in the target activity

#### Q12. You need to remove an Event based on it;s id from your API, Which code snippet defines that request in Retrofit?

- [ ] @DELETE("events)
      fun deleteEvent(@Path("id") id: Long): Call<Unit>
- [ ] @DELETE("events/{id}")
      fun deleteEvent(@Path("id") id: Long): Call<Unit>
- [ ] @REMOVE("events/{id}")
      fun deleteEvent(@Path("id") id: Long): Call<Unit>
- [ ] @DELETE("events/{id}")
      fun deleteEvent(@Path("id") id: Long): Call<Unit>
      
#### Q13. When would you use a product flavour in your build setup?

- [ ] when you need to have the app's strings present in multiple lanuages
- [ ] when you have to provide different versions of your app based on the physical device size
- [ ] when you want to provide different versions of your app based on the device screen density
- [ ] when you want to provide different version of your app with custom configuration and resources

#### Q14. Given the fragment below, how would you get access to a TextView with an ID of text_home contained in the layout file of a Fragment class?

 private lateinit var textView: TextView
 
 override fun onCreateView(...): View? {
    val root = inflator.inflator(R>layout.fragment_home, container, false)
    textView = ??
    
    return root
    }
    
- [ ] root.getById(R.id.text_home)
- [ ] findViewByID(R.id.text_home)
- [ ] root.findViewById(R.id.text_home)
- [ ] root.find(R.id.text_home)

#### Q15. Why do you use the Android JUnitRunner when runnig UI tests?

- [ ] The test facilitates loading your test package and the app under test onto a device or emulator, runs the test, and report the results.
- [ ] The test runner creating screenshots of each screen that displayed while tests are executed.
- [ ] The test runner facilitates parallelization of test classes by providing for each test class.
- [ ] The test runner facilitates interacting with visible elements on a device, regardless of the activity or fragment that has focus.

#### Q16. WWhat allows you to properly restore a user's state when an activity is restarted?

- [ ] the onSaveInstance()method
- [ ] all of these answers
- [ ] persistent storage
- [ ] ViewModel objects



