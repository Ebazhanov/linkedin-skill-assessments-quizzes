## Flutter Quiz

### Q1. Which programming language is commonly used for Flutter app development?
- [ ] Java
- [ ] C#
- [ ] Kotlin
- [x] Dart

### Q2. In Flutter, what is the primary function of a "Widget"?
- [ ] Handle network requests
- [x] Define the app's user interface elements
- [ ] Manage app navigation
- [ ] Store app data

### Q3. What is the primary purpose of the Flutter "pubspec.yaml" file?
- [x] To declare the app's dependencies
- [ ] To define the app's layout
- [ ] To configure the app's theme
- [ ] To specify the app's entry point

### Q4. Which widget in Flutter is used to create a scrollable list of items?
- [ ] ListTile
- [ ] GridView
- [x] SingleChildScrollView
- [ ] Text

### Q5. What is "State" in Flutter, and how is it different from "Stateless" widgets?
- [ ] State is the same as StatelessWidget.
- [ ] State is used for handling user input, while StatelessWidget is for displaying static content.
- [x] State represents mutable data that can change over time, while StatelessWidget is immutable.
- [ ] Stateless widgets are only used for animations.

### Q6. Which Flutter widget is used to create a bottom navigation bar with multiple tabs?
- [x] TabBar
- [ ] BottomAppBar
- [ ] NavigationBar
- [ ] AppBar

### Q7. What is the purpose of the "setState" method in Flutter?
- [ ] To reload the entire app
- [x] To update the state of a widget and trigger a rebuild
- [ ] To navigate to a new screen
- [ ] To perform asynchronous tasks

### Q8. What is the widget that allows you to overlay content on top of other widgets in Flutter?
- [ ] Overlay
- [ ] Popup
- [x] Stack
- [ ] OverlayStack

### Q9. Which package is commonly used for making HTTP requests in Flutter?
- [ ] retrofit
- [x] http
- [ ] network
- [ ] dio

### Q10. What is the purpose of the "BuildContext" parameter in Flutter, and why is it important?
- [ ] It is used to define the layout of widgets.
- [ ] It is used to specify the animation duration.
- [x] It provides information about the location of a widget in the widget tree and is essential for building correct widget trees.
- [ ] None Of the above

### Q11. What is the purpose of "keys" in Flutter widgets, and when should they be used?
- [ ] Keys are used for encryption in Flutter apps.
- [x] Keys are used to identify widgets and improve performance in situations where the widget tree changes dynamically.
- [ ] Keys are used to set the text for widgets.
- [ ] Keys are used to control animations.

### Q12. In Flutter, what is the difference between "Stateful" and "Stateless" widgets in terms of lifecycle methods?
- [ ] Stateful widgets have a "build" method, while StatelessWidget does not.
- [ ] StatelessWidget has a "dispose" method, while Stateful widgets do not.
- [x] Stateful widgets have "initState" and "dispose" methods for initialization and cleanup, while StatelessWidget does not.
- [ ] All of the above

### Q13. What is the purpose of the "Navigator" widget in Flutter, and how does it manage app navigation?
- [ ] The Navigator widget is used for rendering images in Flutter.
- [x] The Navigator widget manages a stack of "Route" objects, allowing users to navigate between different screens or pages.
- [ ] The Navigator widget is used for handling user input events.
- [ ] The Navigator widget is used to load web pages.

### Q14. Which widget is used for creating complex and custom layouts in Flutter by allowing multiple child widgets to be arranged in a two-dimensional grid?
- [ ] Column
- [ ] Row
- [ ] Flex
- [x] GridView

### Q15. Which Flutter widget is used for efficiently rendering a large list of items lazily as the user scrolls through the list?

- [x] ListView.builder
- [ ] ListView
- [ ] ScrollableList
- [ ] ListTile

### Q16. Which widget is commonly used for creating responsive layouts in Flutter to adapt to different screen sizes and orientations?

- [ ] Column
- [ ] Row
- [ ] Flexible
- [x] MediaQuery

### Q17. Which Flutter package is commonly used for managing state persistence, such as storing user choices and app settings?

- [ ] provider
- [ ] sqflite
- [x] shared_preferences
- [ ] hive

### Q18. In Flutter, which code sample illustrates the correct way to define a StatefulWidget class with its associated State class?

- [ ]:
```dart
class MyWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Container();
  }
}
```

- [ ]:
```dart
class MyWidget extends StatefulWidget {
  @override
  _MyWidgetState createState() => _MyWidgetState();
}
```

- [ ]:
```dart
class MyWidgetState extends State<MyWidget> {
  @override
  Widget build(BuildContext context) {
    return Container();
  }
}
```

-[x]:
```dart
class MyWidget extends StatefulWidget {
  @override
  _MyWidgetState createState() => _MyWidgetState();
}

class _MyWidgetState extends State<MyWidget> {
  @override
  Widget build(BuildContext context) {
    return Container();
  }
}
```

### Q19. Which code sample in Flutter demonstrates the correct way to navigate to a new screen using the Navigator when a button is pressed?

- [ ]:
```dart
RaisedButton(
  onPressed: () {
    Navigator.push(context, MaterialPageRoute(builder: (context) => NewScreen()));
  },
  child: Text('Go to New Screen'),
)
```

- [ ]:
```dart
FlatButton(
  onPressed: () {
    Navigator.push(context, MaterialPageRoute(builder: (context) => NewScreen()));
  },
  child: Text('Go to New Screen'),
)
```

- [x]:
```dart
ElevatedButton(
  onPressed: () {
    Navigator.push(context, MaterialPageRoute(builder: (context) => NewScreen()));
  },
  child: Text('Go to New Screen'),
)
```

- [ ]:
```dart
InkWell(
  onTap: () {
    Navigator.push(context, MaterialPageRoute(builder: (context) => NewScreen()));
  },
  child: Text('Go to New Screen'),
)
```

### Q20. Which code sample in Flutter demonstrates the correct way to create a list of items using a ListView.builder widget?

-  [ ]:
```dart
ListView(
  children: List.generate(10, (index) => ListTile(title: Text('Item $index'))),
)
```

- [x]:
```dart
ListView.builder(
  itemCount: 10,
  itemBuilder: (context, index) {
    return ListTile(title: Text('Item $index'));
  },
)
```

- [ ]:
```dart
Column(
  children: List.generate(10, (index) => ListTile(title: Text('Item $index'))),
)
```

- [ ]:
```dart
GridView.builder(
  itemCount: 10,
  itemBuilder: (context, index) {
    return ListTile(title: Text('Item $index'));
  },
)
```
