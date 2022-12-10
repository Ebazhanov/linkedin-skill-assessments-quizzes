## Unity (Animation, Asset Management, C# Scripting, Gameplay, Programming)

#### Q1. What can you use to visually distinguish between Play mode and Design mode in the editor?

- [ ] The object inspector
- [ ] Handles
- [ ] Gizmos
- [x] Play mode tint

#### Q2. A developer executes the C# code below, which finds any game objects tagged as "enemy" in a start event. But the developer notices that, when executed, FindGameObjectsWithTag returns NULL even though the scene contains objects tagged as "Enemy". What is a possible cause?

`GameObject[] MyEnemies = GameObject.FindGameObjectsWithTag("Enemy");`

- [ ] The objects are animated
- [ ] The objects are on the UI layer
- [ ] The objects are not named "Enemy"
- [x] The objects are deactivated

#### Q3. What does this code sample achieve? Float Answer = Random.value \* 10f;

- [ ] It selects a random number that is less than 10
- [ ] It selects a random number greater than 10
- [x] It selects a random number between 0 and 10
- [ ] It selects a random number that is multiple of 10

#### Q4. Unity scenes may be saved entirely in the YAML format. Why might you do this?

- [ ] To reduce scene file size
- [x] To externally parse a scene and its objects
- [ ] To optimize scene loading and unloading
- [ ] To improve platform compatibility

> Also, the text data can be generated and parsed by tools, making it possible to create and analyze scenes automatically.
> [Reference](https://docs.unity3d.com/2021.2/Documentation/Manual/TextSceneFormat.html)

#### Q5. Orthographic cameras remove which visual effect?

- [ ] Gamma color space
- [ ] Depth of field
- [x] Foreshortening
- [ ] Bloom

Gamma color space and bloom are related to graphics. Depth of field is related to objects bluring when at a certain distance from the camera.

1. [Reference](https://docs.unity3d.com/2019.3/Documentation/Manual/CamerasOverview.html)
2. [Reference](https://pbr-book.org/3ed-2018/Camera_Models/Projective_Camera_Models#OrthographicCamera)

#### Q6. What is Cinemachine Virtual Camera used for?

- [ ] To override standard scene cameras with cinematic behaviours
- [ ] To determine what cameras will see when arriving at specific locations
- [x] To create predefined camera presets to apply on standard cameras
- [ ] To act as dummy cameras for fooling meshes into thinking they are being seen

> Use the Aim, Body, and Noise properties to specify how the Virtual Camera animates position, rotation, and other properties. The Virtual Camera applies these settings to the Unity Camera when Cinemachine Brain or Timeline transfers control of the Unity camera to the Virtual Camera.
> [Reference](https://docs.unity3d.com/Packages/com.unity.cinemachine@2.9/manual/CinemachineVirtualCamera.html)

#### Q7. What does the Microphone class save captured audio data as?

- [x] An audio clip asset
- [ ] An MP3 file
- [ ] A WAV file
- [ ] An OGG file

The Microphone class saves captured audio as an audio clip asset, which may then be stored as a OGG file.
[Reference](https://docs.unity3d.com/ScriptReference/Microphone.html)

#### Q8. Cinemachine offers tools for building gameplay behaviours. Which component makes spline based paths for moving objects?

- [ ] Cinemachine Target Group
- [x] Cinemachine Smooth Path
- [ ] Cinemachine Free Look
- [ ] Cinemachine Brain

#### Q9. When building assets like meshes for Unity. It is good practice to use which measurement unit?

- [ ] Cubits
- [ ] Feet
- [ ] Inches
- [x] Meters

[Reference](https://docs.unity3d.com/2019.3/Documentation/Manual/BestPracticeMakingBelievableVisuals1.html)Unity's default units are in meters (Unreal Engine too). If you keep this in mind and model with your units alined to meters, the lighting system will work minimal artifacting.

#### Q10. The Collaborate feature of Unity Teams empowers whom to do what?

- [ ] Developers to contribute to the unity source code
- [ ] Companies to raise money for projects through crowdfunding
- [x] Team members to save, share, and sync unity projects
- [ ] Developers to integrate version control systems, like git, into projects

#### Q11. The Clear Flags property of the Camera components affects which behaviour?

- [ ] How the camera renders UI objects on top of the scene
- [ ] How the camera renders transparent objects by default
- [x] How the camera renders its background on each frame
- [ ] How the camera occludes background objects

#### Q12. What is the OnAnimatorMove event on MonoBehaviour objects commonly used for?

- [ ] Detecting when an object moves
- [ ] Updating a navigation agent in response to keyframe data
- [ ] Replaying an animation when it has completed
- [x] Modifying the root motion of an animated object

#### Q13. Which MonoBehaviour method runs by default in Editor mode?

- [ ] OnBecameInvisible
- [ ] OnAnimatorMove
- [ ] Reset
- [x] OnTriggerEnter

#### Q14. For the OnTriggerEnter function to invoke successfully on a collision between two objects, at least one must have which two components?

- [ ] A Collider and a MeshRenderer
- [ ] A Collider and a MeshFilter
- [x] A Rigidbody and a Collider
- [ ] A MeshRenderer and a MeshFilter

#### Q15. UI elements, such as images and buttons, may be fixed at specific screen positions to build responsive interfaces. Which Unity features help achieve this?

- [ ] Events and raycasts
- [ ] Quaternions and Euler angles
- [ ] Opacity and transparency
- [x] Anchors and pivots

#### Q16. The occlusion map of a material is often a grayscale image with pixels ranging between black and white. What does this map contribute to an object’s material?

- [ ] White pixels reveal the detail map and black pixels reveal none
- [ ] White pixels allow emission and black pixels allow none
- [ ] White pixels receive shadows and black pixels receive none
- [x] White pixels receive full indirect illumination and black pixels receive none

#### Q17. What can you use to organize different game objects into groups inside the Hierarchy panel?

- [ ] Canvas objects
- [ ] Event systems
- [x] Empty objects
- [ ] Mesh renderers

#### Q18. The Project windows search box can filter the display of assets with text commands. Which command displays only texture assets?

- [ ] T:mesh
- [x] T:texture
- [ ] T:mesh
- [ ] Show textures

#### Q19. A bullet game object is fired from a weapon and travels quickly through the scene using a RigidBody component. It sometimes passes through solid objects even though they have colliders. What is a reasonable strategy for correcting this?

- [ ] Expand the collider size of all scene objects and the bullets to detect collisions with better time
- [ ] Increase the Fixed Time Step value from the Project Settings dialog to change the frequency of the FixedUpdate event
- [x] Change the Collision Detection property of the Rigidbody to Continuous Dynamic or Continous Speculative
- [ ] Enable the IsKinematic property of the Rigidbody

#### Q20. Some material types may include normal map textures. What does a normal map achieve?

- [ ] It programmatically reduced the polycount of your meshes.
- [ ] It displaces mesh geometry with extrusion and bevels to generate higher-poly versions.
- [x] It creates the appearance of surface detail on mesh - like bumps, dents, and scratches
- [ ] It is a level-of-detail system that progressively reduces a mesh’s polygons as a scene camera moves farther away from it

#### Q21. A SkinnedMeshRenderer component is attached automatically by Unity to some mesh objects when they are added to a scene. Which reason best explains why?

- [x] The mesh file contains bones and rig data
- [ ] The game object also features an animator component
- [ ] The game object is a Player-Controlled character
- [ ] The mesh file contains a humanoid character

#### Q22. Which C# attribute can show a private variable in the object inspector?

- [ ] Range
- [ ] HideInInspector
- [ ] Serializable
- [x] SerializedField

[Reference](https://docs.unity3d.com/ScriptReference/SerializeField.html)

#### Q23. What is a technique for optimizing Unity UI elements?

- [x] Group static UI elements on one canvas, and dynamic elements on a separate canvas
- [ ] Position all canvas objects to the world origin
- [ ] Group as many UI elements as possible onto only one canvas
- [ ] Divide the screen into multiple canvas objects, each sized to a quarter of the screen size

[Reference](https://unity.com/how-to/unity-ui-optimization-tips) Every time an element on a canvas is updated, the whole canvas is redrawn. If elements are never being updated, keeping them on a single canvas is ideal.

#### Q24. What does the C# Space attribute used below achieved?

```c#
[Space(20)]
Public string PlayerName;
```

- [ ] It inserts 20 space characters as a default value into the string variable below
- [ ] It inserts 20 pixels of margin on all edges around the variable inside the Object Inspector
- [x] It inserts 20 pixels of empty space above the variable inside the Object Inspector
- [ ] It inserts 20 pixels of empty space below the variable inside the Object Inspector

[Reference](https://docs.unity3d.com/ScriptReference/SpaceAttribute.html) This is a great way to customize your inspector without writing a new inspector script for it.

#### Q25. Every time you double-click a C# script file from the Project window, Unity prints the message below (or something very similar) to the console. What is a reasonable step in trying to solve this? Cannot start process because a file name has not been provided

- [ ] Search the Project windows for all script files and then rename all of them
- [x] Set Visual Studio as the code default editor via the External Tools tab of the Preferences menu
- [ ] Ensure you have specified a Play mode tint color from the Colors tab of the Preferences menu
- [ ] Select the Script file, and then select Assets > Find references in Scene from the Application menu

#### Q26. What is the Console windows useful for?

- [ ] Viewing and editing text files
- [ ] Downloading data packets and asset packages
- [ ] Typing and executing command line instructions through a shell interface
- [x] Identifying errors in your script files and project

#### Q27. Sprite atlas assets, large textures containing many smaller sprites, can be optimized by batching together what?

- [ ] Sprites that are non animated
- [ ] Sprites that appear together in game
- [x] Sprites using the same color palette
- [ ] Sprites of the same dimensions

#### Q28. You are making a game where you need to execute your own functions in response to critical animation events for a rigged character. Specifically, there are two events you must handle: when an animation state is entered and when it is exited in the Animator graph. Which class may be used to invoke your code when those two events happen?

- [ ] AnimatorClipInfo
- [x] StateMachineBehaviour
- [ ] AnimationInfo
- [ ] AnimatorUtility

[Reference](https://docs.unity3d.com/ScriptReference/StateMachineBehaviour.html) `OnStateMachineEnter()` and `OnStateMachineExit()` are the methods of the StateMachineBehavior class that handle this. AnimatorClipInfo displays information about the current clip being played, AnimatiorUtility deals with transform hierarchy, and AnimationInfo was removed in version 5.0.

#### Q29. How can you change the unique bundle identifier for a mobile build?

- [ ] Select Assets > import Package, and then import the Cross-Platform Input Asset Package
- [ ] Select Windows > Asset Management > Version Control, and then enter an identifier in the Source field
- [ ] Select File > Build Settings. Then from the Build dialog box, select Android or iOS, and select the Bundle Identifier from the Compression Method drop down menu.
- [x] Select Edit > Project Settings > Player from the menu, and then expand the Other Settings tab

#### Q30. Rigidbody components may be added to objects with colliders to make them affected by physical forces. What does the IsKinematic property achieve?

- [ ] It removes gravity from an object but retains all other forces
- [ ] It removes all physical forces from the object, except gravity
- [ ] It converts the object into physical forces that affect other objects
- [x] It suspends physical forces on the object, allowing manual transofrmations

#### Q31. The primary directional light in a scene is linked by default to a procedural scene Skybox. What does the rotation of this light control?

- [ ] The orientation of the Skybox
- [x] The night and day status of the skybox
- [ ] The acoustics of all audio sources
- [ ] The resolution of the skybox

#### Q32. You can combine quaternions together through which arithmetic operation?

- [x] Multiplication
- [ ] Division
- [ ] Addition
- [ ] Subtraction

#### Q33. Which feature generates binary tree data to optimize camera rendering in a scene?

- [ ] Render textures
- [ ] Navigation mesh
- [ ] Profiler
- [x] Occlusion Culling

#### Q34. How does the Range C# attribute control the interaction behavior of numerical variables in the Object Inspector?

- [x] It restricts the variable value using a slider widget
- [ ] It validates the variable values through a text box widget
- [ ] It restricts the variable values using a color picker widget
- [ ] It presents valid options in a drop down list

#### Q35. What does this code fragment do when attached to a rigged character?

```c#
    public Animator avatar;
    public Transform lookAtObj;
    void OnAnimatorIK(int layerIndex)
    {
        avatar.SetLookAtPosition(lookAtObj).position;
        avatar.SetLookAtWeight(If);
    }
```

- [ ] It blends the characters head animation with a second predefined animation
- [ ] It makes the characters head face toward the specified target
- [ ] It returns the characters head back to a neutral position
- [ ] It makes a game object face toward the characters head

#### Q36. The variable Transform.forward is a Vector3 measured in what?

- [x] Local space
- [ ] Innerspace
- [ ] Normal space
- [ ] World space

#### Q37. De-lighting is associated with which technology?

- [ ] Virtual reality
- [ ] Augmented reality
- [ ] Motion capture
- [x] Photogrammetry

`When you use photogrammetry to scan in models from the real world, and bring in those models into Unity (or any renderer), you will notice that the lighting information is baked into the texture. You can remove the baked in lighting information with various tools online, but even Unity themeless wrote a custom tool for just this; check it out!`

1. [Reference](https://github.com/Unity-Technologies/DeLightingTool)
2. [Reference](https://github.com/Unity-Technologies/DeLightingTool/blob/master/Assets/DeLightingTool/Documentation/De-LightingTool.pdf)

#### Q38. Humanoid character assets, like NPCs and the player character, feature on Avatar object. Which statement best describes its purpose?

- [ ] Avatars define parameter sets for facial muscle blendshapes
- [x] Avatar facilitate animation retargeting across different humanoid characters
- [ ] Avatar define IK data for animated characters
- [ ] Avatars describe how textures map on deforming objects during animation

#### Q39. You can perfectly align two mesh objects together at the vertices by using vertex snapping. How do you best access this tool?

![Vertex](images/Q39.png?raw=true)

- [ ] Select a mesh object and press the W key over the destination vertex
- [ ] While holding down the C key, click and drag from the source to the destination mesh
- [ ] Select **Edit > Enable Vertex Snap** from the menu, and then select your object
- [x] While holding down the V key, click and drag your object from a corner vertex to its destination

[Reference](https://docs.unity3d.com/Manual/PositioningGameObjects.html#VtxSnapping)

#### Q40. Which statement best descibes the function Quaternion.Euler?

- [ ] It prints a Quaternion to a string that shows its X, Y, and Z rotation in degrees
- [ ] It converts a 3D orientation from Radiens to a Quaternion
- [x] It converts a 3D orientation that is measured in degrees into a Quaternion
- [ ] It converts a Quaternion into a Vector3 in which X, Y, and Z are measured in degrees

Simplfying the math: Unity uses Quaternions internally to avoid Gimbal lock.
The Euler XYZ (Pitch, Yaw, and Roll) axises can lock up when two axies are aligned.
Quaternion.Euler converts the Euler number provided to the internally used Quarternion, to prevent this problem.
[Reference](https://docs.unity3d.com/ScriptReference/Quaternion.Euler.html)

#### Q41. What does the Destroy function do?

- [ ] It deactivates the specified game object immidiately
- [x] It deletes the specified game object after the current update loop
- [ ] It deletes the specified game object when the application terminates
- [ ] It deletes the specified game object immidaitely

[Reference](https://docs.unity3d.com/ScriptReference/Object.Destroy.html)`The object obj is destroyed immediately after the current Update loop, or t seconds from now if a time is specified.`

#### Q42. You can programmatically control audio effects, like Pitch and Reverb, from C# scripts using which feature of an Audio Mixer asset?

- [ ] audio attenuation
- [x] exposed parameters
- [ ] ParamEQ
- [ ] Audio Mixer groups

[Official Unity Tutorial:](https://www.youtube.com/watch?v=9tqi1aXlcpE)`Audio attenuation is about energy loss, commonly refered to as "gain". ParamEQ allows you to change the frequency of the audio - "pitch", with no C# support. Audio Mixer groups do allow you to control audio effects, but not through C#.`

#### Q43. Multiple animations may be mixed together on a single character, selectively on different limbs. Which Mecanim feature supports this?

- [ ] Mip Maps
- [x] avatar masks
- [ ] StateMachineBehaviour scripts
- [ ] animation events

[Reference](https://docs.unity3d.com/Manual/class-AvatarMask.html)`Mip Maps are a technique that improves image quality and reduces rendering speed, at the cost of storage space, by including smaller copies of the image in the same file. Animation events allow you to call functions at points in the timeline.`

#### Q44. What does the PlayableDirector component allow you to do?

- [ ] run multiple functions on different game objects in parallel
- [ ] switch between different scene cameras on demand
- [x] control the playback of a timeline instance in the scene
- [ ] record a gameplay session to a video file

[Reference](https://docs.unity3d.com/2019.2/Documentation/Manual/class-PlayableDirector.html)`The PlayableDirector component stores the link between a Timeline instance and a Timeline Asset.`

#### Q45. What does the Grid component do?

- [ ] generate a grid sprite at world origin
- [x] helps you move objects to fixed grid increments
- [ ] reders and isometric grid in the scene during gameplay
- [ ] generates a grid mesh at the world origin

#### Q46. Timeline sequences can initiate code during an animation using which feature?

- [ ] EventSystem
- [x] markers
- [ ] signals
- [ ] packets

`EventSystem is not a timeline feature, neither are packets. Timeline signals are a subfeature of the markers, markers can directly initiate code, while a signal can only send the signal to a reciver.`

1. [Reference](https://forum.unity.com/threads/new-in-2019-1-marker-customization.594712)
2. [Reference](https://blog.unity.com/technology/how-to-create-custom-timeline-markers)

#### Q47. Which code sample uses C# properties for creating the health functionality?

- [ ] A

```c#
public class Health : MonoBehavior
{
    private float HealthPoints = 100f;

    public float GetHealth()
    {
        return HealthPoints;
    }

    public void SetHealth(float Change)
    {
        HealthPoints += Change;

        if (HealthPoints <= 0)
            Destroy(gameObject);
     }
}
```

- [ ] B

```c#
public class Health : MonoBehavior
{
    public UnityEvent OnHealthChanged;

    private float HealthPoints = 100f;

    public void SetHealth(float Change)
    {
        HealthPoints += Change;
        OnHealthChanged.Invoke();
    }

    public void Die()
    {
        Destroy(gameObject);
    }
}
```

- [x] C

```c#
public class Health : MonoBehavior
{
    public float HealthPoints
    {
        get { return _healthpoints; }
        set
        {
            _healthpoints = value;

            if(_healthpoints <= 0 )
            {
                Destroy(gameObjects);
            }
        }
    }

    private float _healthpoints = 100f;
}
```

- [ ] D

```c#
public class Health : MonoBehaviour
{
    public float HealthPoints = 100f;

    private void Update()
    {
        if (HealthPoints <- 0)
            Destroy(gameObject);
    }
}
```

`get` and `set` are the clear indicators that a C# property is being used.
[Reference](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/properties)

#### Q48. Which statement is not true?

- [ ] A Coroutines will continue running on deactivated objects
- [ ] B All component scripts inherit from `MonoBehaviour`
- [x] C Only humanoid characters feature bones
- [ ] D The `Update` function is never called automatically while an object is deactivated

[Reference](https://docs.unity3d.com/2017.3/Documentation/Manual/GenericAnimations.html)

#### Q49. When is the `Reset` method of `MonoBehaviour` invoked automatially?

- [ ] A When a game object moves from one scene to another
- [x] B When adding a component to an object or resetting its values in Edit mode
- [ ] C When a scene begins or is restarted
- [ ] D When the scene begins or restarts for a deactivated game object

[Reference](https://docs.unity3d.com/ScriptReference/MonoBehaviour.Reset.html)`Reset` is called when the user hits the Reset button in the Inspector's context menu or when adding the component the first time. This function is only called in editor mode.

#### Q50. Which C# attribute allows a class and its methods to run inside the editor during Edit mode?

- [ ] A [Range(0,10)]
- [ ] B [Live]
- [ ] C [RunInEditor]
- [x] D [ExecuteAlways]

`ExecuteAlways` makes instances of a script always execute, both as part of Play Mode and when editing. By default, MonoBehaviours are only executed in Play Mode and only if they are on GameObjects in the main stage containing the user Scenes. By adding this attribute, any instance of the MonoBehaviour will have its callback functions executed at all times.

1. [Reference](https://docs.unity3d.com/ScriptReference/ExecuteAlways.html)
   Do not fall for `[RunInEditor]`! It looks similar to `MonoBehaviour.runInEditMode` and `[ExecuteInEditMode]` both of which are legit but not mentioned as possible answers.
2. [Reference](https://docs.unity3d.com/ScriptReference/MonoBehaviour-runInEditMode.html)

#### Q51. The `IsPointerOverGameObject` static function of the `EventSystem` class is useful for creating which behaviour?

- [ ] A moving UI elements in sync with the cursor as it drags across the screen
- [ ] B changing the highlight of buttons as the cursor moves over them
- [x] C preventing mouse clicks on game objects behind the UI canvas <- i believe this is the correct answer but supervision would be helpful
- [ ] D identifying which 3D object the cursor is hovering over

#### Q52. Which C# code fragment continuously updates an object's yaw (Y rotation)?

- [ ] `c# transform.localRotation *= Quaternion.Euler(0f, RotSpeed * Time.deltaTime, 0f);`
- [x] `c# transform.Rotate(Vector3.right, RotSpeed * Time.deltaTime);`
- [ ] `c# transform.RotateAround(Vector3.up, RotSpeed * Time.deltaTime);`
- [ ] `c# transform.SetParent(null);`
