## Unity (Animation, Asset Management, C# Scripting, Gameplay, Programming)

#### Q1. What can you use to visually distinguish between Play mode and Design mode in the editor?

- [ ] The object inspector
- [ ] Handles
- [ ] Gizmos
- [x] Play mode tint

#### Q2. A developer executes the C# code below, which finds any game objects tagged as “enemy” in a start event. But the developer notices that, when executed, FindGameObjectsWithTag returns NULL even though the scene contains objects tagged as “Enemy”. What is a possible cause?

`GameObject[] MyEnemies = GameObject.FindGameObjectsWithTag(“Enemy”);`

- [ ] The objects are animated
- [ ] The objects are on the UI layer
- [ ] The objects are not named “Enemy”
- [x] The objects are deactivated

#### Q3. What does this code sample achieve? Float Answer = Random.value \* 10f;

- [ ] It selects a random number that is less than 10
- [ ] It selects a random number greater than 10
- [x] It selects a random number between 0 and 10
- [ ] It selects a random number that is multiple of 10

#### Q4. Unity scenes may be saved entirely in the YAML format. Why might you do this?

- [ ] To reduce scene file size
- [ ] To externally parse a scene and its objects
- [ ] To optimize scene loading and unloading
- [ ] To improve platform compatibility

#### Q5. Orthographic cameras remove which visual effect?

- [ ] Gamma color space
- [ ] Depth of field
- [ ] Foreshortening
- [ ] Bloom

#### Q6. What is Cinemachine Virtual Camera used for?

- [ ] To override standard scene cameras with cinematic behaviours
- [ ] To determine what cameras will see when arriving at specific locations
- [ ] To create predefined camera presets to apply on standard cameras
- [ ] To act as dummy cameras for fooling meshes into thinking they are being seen

#### Q7. What does the Microphone class save captured audio data as?

- [ ] An audio clip asset
- [ ] An MP3 file
- [ ] A WAV file
- [ ] An OGG file

#### Q8. Cinemachine offers tools for building gameplay behaviours. Which component makes spline based paths for moving objects?

- [ ] Cinemachine Target Group
- [ ] Cinemachine Smooth Path
- [ ] Cinemachine Free Look
- [ ] Cinemachine Brain

#### Q9. When building assets like meshes for Unity. It is good practice to use which measurement unit?

- [ ] Cubits
- [ ] Feet
- [ ] Inches
- [ ] Meters

#### Q10. The Collaborate feature of Unity Teams empowers whom to do what?

- [ ] Developers to contribute to the unity source code
- [ ] Companies to raise money for projects through crowdfunding
- [x] Team members to save, share, and sync unity projects
- [ ] Developers to integrate version control systems, like git, into projects

#### Q11. The Clear Flags property of the Camera components affects which behaviour?

- [ ] How the camera renders UI objects on top of the scene
- [ ] How the camera renders transparent objects by default
- [ ] How the camera renders its background on each frame
- [ ] How the camera occludes background objects

#### Q12. What is the OnAnimatorMove event on MonoBehaviour objects commonly used for?

- [ ] Detecting when an object moves
- [ ] Updating a navigation agent in response to keyframe data
- [ ] Replaying an animation when it has completed
- [ ] Modifying the root motion of an animated object

#### Q13. Which MonoBehaviour method runs by default in Editor mode?

- [ ] OnBecameInvisible
- [ ] OnAnimatorMove
- [ ] Reset
- [ ] OnTriggerEnter

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
- [ ] T:texture
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

#### Q23. What is a technique for optimizing Unity UI elements?

- [ ] Group static UI elements on one canvas, and dynamic elements on a separate canvas
- [ ] Position all canvas objects to the world origin
- [ ] Group as many UI elements as possible onto only one canvas
- [ ] Divide the screen into multiple canvas objects, each sized to a quarter of the screen size

#### Q24. What does the C# Space attribute used below achieved?

    [Space(20)]
    Public string PlayerName;

- [ ] It inserts 20 space characters as a default value into the string variable below
- [ ] It inserts 20 pixels of margin on all edges around the variable inside the Object Inspector
- [ ] It inserts 20 pixels of empty space above the variable inside the Object Inspector
- [x] It inserts 20 pixels of empty space below the variable inside the Object Inspector

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
- [ ] Sprites using the same color palette
- [ ] Sprites of the same dimensions

#### Q28. You are making a game where you need to execute your own functions in response to critical animation events for a rigged character. Specifically, there are two events you must handle: when an animation state is entered and when it is exited in the Animator graph. Which class may be used to invoke your code when those two events happen?

- [ ] AnimatorClipInfo
- [ ] StateMachineBehaviour
- [ ] AnimationInfo
- [ ] AnimatorUtility

#### Q29. How can you change the unique bundle identifier for a mobile build?

- [ ] Select Assets > import Package, and then import the Cross-Platform Input Asset Package
- [ ] Select Windows > Asset Management > Version Control, and then enter an identifier in the Source field
- [ ] Select File > Build Settings. Then from the Build dialog box, select Android or iOS, and select the Bundle Identifier from the Compression Method drop down menu.
- [ ] Select Edit > Project Settings > Player from the menu, and then expand the Other Settings tab

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

```
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
- [ ] Photogrammetry

#### Q38. Humanoid character assets, like NPCs and the player character, feature on Avatar object. Which statement best describes its purpose?

- [ ] Avatars define parameter sets for facial muscle blendshapes
- [x] Avatar facilitate animation retargeting across different humanoid characters
- [ ] Avatar define IK data for animated characters
- [ ] Avatars describe how textures map on deforming objects during animation
