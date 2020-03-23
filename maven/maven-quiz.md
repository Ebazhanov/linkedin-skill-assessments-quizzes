Maven Assessment
-----------------

#### Q1. What element in the pom.xml file allows you to provide values that can be reused in other elements of the pom.xml?
- Plugins
- Build
- Properties
- Parent

#### Q2. If you wish to build and package your artifact using the Maven package goal but don't want to execute the unit tests, which environment variable and value would you use?
- `maven.test.ignore=TRUE`
- `maven.test.run=FALSE`
- `maven.test.skip=TRUE`
- `maven.verify.execute=FALSE`

#### Q3. When building a Maven EAR project and specifying the configuration of which projects to include, what is the element in the plugin configuration that contains Enterprise Java Bean projects?
- modules/webModules
- modules/ejbModules
- modules/enterpriseModules
- modules/services

#### Q4. The goal that is executed to generate and deploy a documentation website is ___.
- deliver
- site
- doc
- deploy

#### Q5. What does the `mvn -version` command do?
- It builds your Maven project.
- It installs Maven on your computer.
- It updates Maven to the latest version.
- It print out your installed version of Maven.

#### Q6. There are several properties available for use in a pom.xml file that refer to details of the project, such as groupId and version. What do all of these properties start with?
- pom
- maven
- jar
- project

#### Q7. What directory structure contains the source code of your artifact?
- src/code
- src/test/java
- src/main/java
- src/main/resources

#### Q8. Which command is used to run the clean lifecyle followed by verify, install, and package with Maven?
- `mvn clean istall package`
- `mvn package`
- `mvn clean install`
- 
```shell script
mvn clean
mvn package
mvn verify
mvn install
```

#### Q9. Which goal would you use with the Dependency plugin to determine which included dependencies are not used, as well as those you are using that you have not defined?
- `dependency:tree`
- `dependency:properties`
- `dependency:evaluate`
- `dependency:analyze`

#### Q10. In a multimodule project, if you have a plugin bound to a phase in the parent, it will be bound to the same phase in the module. What strategy could you employ to prevent the plugin from executing in the module?
- In the excluded element of the build section of the POM, list the plugin you do not want to run.
- Set the phase in the module to none.
- Set a value in the configuration of the plugin in the module to be excluded like this: TRUE.
- Do not specify the plugin in the module.

#### Q11. When building a web application with a WAR type project, which project directory should contain the style sheet, JavaScript, and other static file?
- src/main/static
- src/main/web
- src/main/resources
- src/main/webapp

#### Q12. When performing a build, which Maven plugin will allow you to set the specific version of the artifact to be built without manual modifying the pom.xml file?
- Compiler
- Surefire
- Versions
- Javadoc

#### Q13. When building a Maven Archetype, what is the filepath and file of the archetype descriptor that specifies how to lay out the prototype files?
- `src/main/template/descriptor.xml`
- `src/main/resources/META-INF/maven/archetype-descriptor.xml`
- `src/main/archetype/descriptor.xml`
- `src/main/resources/META-INF/maven/maven-archetype.xml`

#### Q14. What is a valid packaging type for a Maven project?
- WAR
- all of these answers
- POM
- EAR

#### Q15. When two dependencies of your Maven project introduce the same transitive dependency with different versions, which one(s) will be included in the dependency list for your project?
- the dependency with the higher version
- the transitive dependency that comes from the dependency listed first in the pom.xml file
- the transitive dependency that comes from the dependency listed last in the pom.xml file
- the transitive dependency version of the artifact that is closest to your project
