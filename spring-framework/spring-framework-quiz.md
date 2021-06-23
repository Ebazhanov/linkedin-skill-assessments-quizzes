## Spring Framework

#### Q1. How filters are used in Spring Web?

- [ ] Filters are called before a request hits the DispatcherServlet.They allow for interception-style, chained processing of web requests for security, timeouts, and other purposes.
- [ ] Filters are used with a checksum algorithm that will filter invalid bytes out of a byte stream request body and allow for processing of HTTP requests from the DispatcherRequestServlet.
- [ ] Filters are used with a checksum algorithm that will filter invalid bytes out of an octet stream a multipart upload and allow for chained processing of WebDispatcherServlet requests.
- [x] Filters are used to validate request parameters out of the byte stream request body and allow for processing of requests from the DispatcherRequestServlet.

#### Q2. How is a resource defined in the context of a REST service?

- [ ] A resource is the actual String literal that composes a URI that is accessed on a RESTful web service.
- [x] It is an abstract concept that represents a typed object, data, relationships, and a set of methods that operate on it that is accessed via a URI.
- [ ] A REST service has a pool of resources composed of allocations of memory that allow a request to be processed.
- [ ] A resource for a REST service is an explicit allocation of a thread or CPU cycles to allow a request to be processed.

#### Q3. Which of these is a valid Advice annotation?

- [ ] @AfterError
- [x] @AfterReturning
- [ ] @AfterException
- [ ] @AfterExecution

#### Q4. What does a ViewResolver do?

- [ ] It supports internationalization of web applications by detecting a user's locale.
- [x] It generates a view by mapping a logical view name returned by a controller method to a view technology.
- [ ] It creates a unique view determined by the uers's browser type,supporting cross-browser compatibility.
- [ ] It maps custom parameters to SQL views in the database, allowing for dynamic content to be created in the response.

#### Q5. How are Spring Data repositories implemented by Spring at runtime?

- [ ] Spring automatically generated code for you based on your YAML config that defined a MethodInterceptor chain that intercept calls to the instance and computed SQL on the fly.
- [x] A JDK proxy instance is created, which backs the repository interface, and a MethodInterceptor intercepts calls to the instance and routes as required.
- [ ] The Spring JDK proxy creates a separate runtime process that acts as an intermediary between the database and the Web server, and intercepts calls to the instance and handles requests.
- [ ] Spring automatically generated code for you based on your XML config files that define a SpringMethodAutoGeneration factory that intercepts calls to the instance and creates dynamic method that computer SQL on the fly.

#### Q6. What is SpEL and how is it used in Spring?

- [ ] SpEL(Spring Expression Language) runs in the JVM and can act as a drop-in replacement for Groovy or other languages.
- [x] SpEL(Spring Expression Language) supports boolean and relational operators and regular expressions, and is used for querying a graph of objects at runtime.
- [ ] SpEL(Spring Expression Language) allows you to build, configure,and execute tasks such as building artifacts and downloading object dependencies.
- [ ] SpEL(Spring Expression Language) natively transpiles one JVM language to another, allowing for greater flexibility.

#### Q7. The process of linking aspects with other objects to create an advised object is called

- [ ] dynamic chaining
- [ ] banding
- [x] weaving
- [ ] interleaving

#### Q8. How are JDK Dynamic proxies and CGLIB proxies used in Spring?

- [x] JDK Dynamic proxy can proxy only interface, so it is used if the target implements at least one interface. A CGLIB proxy can create a proxy by subclassing and is used if the target does not implement an interface.
- [ ] Only JDK Dynamic proxies are used in the Spring Bean Lifecycle. CGLIB proxies are used only for integrating with other frameworks.
- [ ] Only CGLIB proxies are used in the Spring Bean Lifecycle. JDK Dynamic proxies are used only for integrating with other frameworks.
- [ ] JDK Dynamic proxy can only using an abstract class extended by a target. A CGLIB proxy can create a proxy through bytecode interweaving and is used if the target does not extend an abstract class.

#### Q9. Which of these is not a valid method on the JoinPoint interface?

- [ ] getArgs()
- [x] getExceptions()
- [ ] getSignature()
- [ ] getTarget()

#### Q10. In what order do the @PostConstruct annotated method, the init-method parameter method on beans and the afterPropertiesSet() method execute?

- [ ] 1. afterPropertiesSet() 2. init-method 3. @PostConstruct
- [x] 1. @PostConstruct 2. afterPropertiesSet() 3. init-method
- [ ] 1. init-method 2. afterPropertiesSet() 3. @PostConstruct
- [ ] You cannot use these methods together-you must choose only one.

#### Q11. What is the function of the @Transactional annotation at the class level?

- [ ] It's a transaction attribute configured by spring.security.transactions.xml config file that uses Spring's transaction implementation and validation code.
- [ ] It's a transaction must actively validate by the bytecode of a transaction using Spring's TransactionBytecodeValidator class. Default Transaction behavior rolls back on validation exception but commits on proper validation
- [x] It creates a proxy that implements the same interface(s) as the annotated class, allowing Spring to inject behaviors before, after, or around method calls into the object being proxied.
- [ ] It's a transaction that must be actively validated by Spring's TransactionValidator class using Spring's transaction validation code. Default Transaction behavior rolls back on validation exception.

#### Q12. Which is a valid example of the output from this code (ignoring logging statements) ?

```java
@SpringBootApplication
public class App {
     public static void main(String args[]) {
          SpringApplication.run(App.class, args);
          System.out.println("startup");
     }
}

public class Print implements InitializingBean {
     @Override
     public void afterPropertiesSet() throws Exception {
          System.out.println("init");
     }
}
```

- [x] Nothing will print
- [ ] startup
      init
- [ ] init
- [ ] startup

#### Q13. Which println statement would you remove to stop this code throwing a null pointer exception?

```java
@Component
public class Test implements InitializingBean {
     @Autowired
     ApplicationContext context;
     @Autowired
     static SimpleDateFormt formatter;

     @Override
     public void afterPropertiesSet() throws Exception {
          System.out.println(context.containsBean("formatter") + " ");
          System.out.println(context.getBean("formatter").getClass());
          System.out.println(formatter.getClass());
          System.out.println(context.getClass());
     }
}

@Configuration
class TestConfig {
     @Bean
     public SimpleDateFormat formatter() {
          return new SimpleDateFormat();
     }
}
```

- [x] formatter.getClass()
- [ ] context.getClass()
- [ ] context.getBean("formatter").getClass()
- [ ] context.containsBean("formatter")

#### Q14. What is the root interface for accessing a Spring bean container?

- [ ] SpringInitContainer
- [ ] ResourceLoader
- [ ] ApplicationEventPublisher
- [x] BeanFactory

#### Q15. Which annotation can be used within Spring Security to apply method level security?

- [x] @Secured
- [ ] @RequiresRole
- [ ] @RestrictedTo
- [ ] @SecurePath

#### Q16. What is the result of calling the map controller method using the HTTP request GET localhost:8080/map?foo=foo&bar=bar ?

```java
@RestController
public class SampleController {

     @RequestMapping("/map")
     public String map(@RequestParam("bar") String foo, @RequestParam("foo") String bar) {
          return bar + foo;
     }
}
```

- [ ] An InvalidParameterNameMappingException is thrown at runtime.
- [ ] barfoo
- [x] foobar
- [ ] A status code of 400 Bad Request is returned.

#### Q17. What is the purpose of the @Lazy annotation and why would you use it?

- [ ] It prevents a bean from being created and injected until you run a specific CLI command. It reduces complexity in the application.
- [ ] It can be applied to a bean so that the bean is not persisted in the database. It reduces the number of database operations.
- [x] It can be applied to a bean so that the bean is not created and injected until it is needed. It can help speed up startup time for your application.
- [ ] It prevents a bean from being created and injected until it receives a HTTP request to a callback hook. It reduces disk footprint.

#### Q18. What is dependency injection?

- [x] a method by which objects define dependencies they need as abstractions that allows the framework to instantiate and configure them in a central location at runtime.
- [ ] a paradigm where dependent code is injected into the bytecode of a Java application on a remote server.
- [ ] a way of injecting remote dependencies into a pre-packaged JAR file from the file system.
- [ ] a way of injecting remote dependencies into a pre-packaged WAR file from the file system.

#### Q19. What is a RESTful web service?

- [ ] Reactive Enterprise Status Transfer is a web service comprising a set of guidelines and technical constraints for web services that monitor and alert of a set of mission-critical resources.
- [x] Representational State Transfer an architectural style for creating web services that includes client-server architecture, statelessness, cacheability, a layered system, and a uniform interface.
- [ ] Redundant Enumerated State Transfer is a web service that provides redundancy in the case of failure and outlines technical constraints for web services that have access to resources.
- [ ] Reactive Enterprise State Transfer is a web service comprising a set of guidelines and technical constraints for web services y that have access to resources and are async in nature.

#### Q20. What happens when a class is annotated with the @Controller annotation?

- [x] A controller bean definition is defined in the servlet's WebApplicationContext. The class is marked as a web component, and you can map requests to controller methods.
- [ ] A controller bean definition is defined in the Web Context, and Web Servlet is marked as a component that reads mapped controller requests from an XML config file.
- [ ] A controller bean definition is defined in the Tomcat Context, and the Controller Servlet is marked as a web component that reads mapped controller requests from a YAML config file.
- [ ] A controller bean definition is defined in the Servlet Context, and the Controller Servlet is marked as a component that reads mapped controller requests from an XML config file.

#### Q21. Which property can be used to change the port of a Spring application?

- [ ] Port
- [ ] spring.port
- [ ] spring.settings.port
- [x] server.port

#### Q22. What is the purpose of the @ResponseBody annotation?

- [ ] to validate the char array contained in a response to ensure that it is a valid character encoding
- [ ] to generate a local byte stream from the body of a response that allows a request to be scanned for security risks
- [x] to indicate whether a handler method return value should be bound to the web response body in servlet environments
- [ ] to ensure a ThreadLocal byte stream that allows a response to be encoded for reading directly into a socket stream

#### Q23. How are mocking frameworks such as Mockito used with Spring?

- [ ] Mockito will spin up a mock web service hosted in a Docker container that can respond to HTTP requests to mock out third-party APIs.
- [x] Mockito can use annotations or factory methods to create mock objects that may be injected into tests in place of dependencies. The behavior of mocks can be explicitly configured.
- [ ] Mockito will create mock users to repeatedly perform requests against your Spring application to test your app's ability to take load.
- [ ] Mockito will spin up a mock web service hosted in a Docker container that can respond to RPC calls to mock out remote resources.

#### Q24. What is the name of the central servlet that dispatches requests to controllers?

- [ ] DispatchingDelegatorServlet
- [x] DispatcherServlet
- [ ] Router
- [ ] FrontControllerServlet

#### Q25. What is the purpose of the Spring IoC (Inversion of Control) container?

- [x] It instantiates and configures objects, supplied at runtime, to classes that define them as a dependency.
- [ ] It allows the front-end code to manage the ResponseBody objects provided by a back-end REST API.
- [ ] It allows a database to define business objects via a shared schema at compile time.
- [ ] It facilitates a remote server to configure a local application.

#### Q26. What is component scanning?

- [x] feature that scans packages for classes with specific annotations and, when found, creates their bean definitions within the IoC container
- [ ] paradigm where bytecode is actively scanned to identify additional optimizations to inject into components in the application context
- [ ] a method by which cloud repositories are scanned to identify components for injection into an IoC container
- [ ] a method by which binary data in a database is searched to identify components for injection into the IoC container

#### Q27. What does @SpringBootApplication do?

- [ ] This annotation takes the String literal passed into the annotation as a parameter and automatically generates all the code for your application as per the passed in template parameter.
- [x] This compound annotation applies the @Bootable, @Springify, and @StandardConfig annotations that launch a CLI tool after launching the Spring Boot WAR file that will guide you through a series of prompts to set up your app.
- [ ] This annotation scans the provided spring-boot-config-construction.yaml file in your root directory and automatically generates all the code for your application as defined in the YAML file.

#### Q28. How does Spring Data facilitate queries against a datastore?

- [ ] Queries are explicitly coded in repository implementations using the Spring Data CriteriaBuilder.
- [ ] Query metadata is stored in the underlying datastore and retrieved at runtime per repository.
- [x] Queries are derived from the signatures of methods on a Spring Data repository that contain keywords in their name for constructing the query logic.
- [ ] A spring-data-queries.xml file contains queries within entity tags that specify the query logic for each repository.

#### Q29. How does Spring generate bean names for classes annotated with @Component that do not specify a name?

- [x] It uses the short name of the class with the first letter in lowercase.
- [ ] It uses the short name of the class.
- [ ] It uses the short name of the class in uppercase.
- [ ] It uses the canonical name of the class in lowercase.

#### Q30. What is the delegating filter proxy?

- [ ] It's the servlet filter chain proxy that handles all requests to the route defined in spring.security.xml. All calls to the filter proxy are forwarded to the ErrorDispatcherServlet.
- [ ] It's the servlet filter chain that handles requests to the route defined in spring.security.factories. All calls to the filter proxy y are forwarded to the ErrorServlet.
- [x] It's the servlet filter proxy delegating to a filter bean specified in web.xml. All calls to the filter proxy will be delegated to that servlet filter bean.
- [ ] It's the web servlet daemon filter proxy that delegates to a bean specified in spring.security.factories. All calls to the filter proxy that do not contain a proper route will return an error.

#### Q31. What value does Spring Boot Actuator provide?

- [x] It helps monitor and manage a Spring Boot application by providing endpoints such as health checks, auditing, metrics gathering, and HTTP tracing.
- [ ] It provides out-of-the-box functionality that integrates with third-party metrics platforms to automatically scale up and down the number of threads in threadpools.
- [ ] It's a CLI that allows you to modify the configuration of a running Spring Boot application without the need for restarting or downtime.
- [ ] It provides out-of-the-box functionality that integrates wiltr?third-party metrics platforms to automatically scale up and down the number of instances of the Spring Boot application.

#### Q32. What is the purpose of the @ContextConfiguration annotation in a JUnit Test?

- [ ] It introspects the local machine and automatically provisions resources based on certain contextual configuration files.
- [ ] It automatically generates comments for annotated classes on autowired dependencies to provide additional context about dependencies.
- [x] It defines metadata at the class-level to determine how to load or configure an ApplicationContext in Spring integration tests.
- [ ] It automatically generates JavaDocs for annotated classes to provide additional context about the purpose of the class.

#### Q33. How are authentication and authorization different?

- [ ] Authentication is the act of granting access to specific resources and functions based on config settings. Authorization is the act of introspecting a user's credentials to ensure they are not impersonating another user.
- [ ] Authentication is the act of verifying certain resources and functions are actually valid. Authorization is the act of verifying a user's credentials have not expired.
- [ ] Authentication is the act of verifying that certain resources and functions actually exist in the database. Authorization is the act of verifying a user's credentials to ensure they are valid.
- [x] Authentication is validating that users are who they claim to be. Authorization is granting access to specific resources and functions.

#### Q34. What is the purpose of the @RequestBody annotation?

- [ ] to create a ThreadLocal byte stream that allows a request to be encoded for reading directly into a database
- [ ] to automatically generate a ThreadLocal byte stream from the body of a request that allows a request to scanned for security risks
- [x] to indicate whether an annotated handler method parameter should be bound to the web request body, which is converted by an HttpMessageConverter
- [ ] to automatically validate the characters contained in a request to ensure that they are a valid character encoding

#### Q35. What is the DispatcherServlet and what is its function?

- [ ] The DispatcherServlet process daemon assigns a separate Web Servlet Container process to each HTTP request that comes into the web server.
- [x] It is a servlet that dispatches HTTP requests to registered handlers/controllers for processing.
- [ ] The DispatcherServlet API assigns a separate Web Servlet Node process to each additional HTTP request that comes into the web server.
- [ ] It is a servlet that dispatches an array of background daemon processes that allocate memory and CPU cycles to each request.

#### Q36. What is Spring Boot autoconfiguration?

- [ ] It triggers a local automated review of configuration files such as web.xml and detects possible security issues or automatically resolves circular dependencies.
- [ ] It triggers an automated review of configuration by a web-based agent that reviews your existing web.xml file and detects possible security issues.
- [x] It's an opinionated, intelligent method of introspecting an app to configure beans that are likely to be needed. This configuration can be overridden over time with manual configuration.
- [ ] It provides plug-in functionality while editing your web.xml and other config files that will autocomplete common dependencies while typing.

#### Q37. Which are valid steps to take to enable JPA in Spring Boot?

- [x] Add an @EnableJpaRepositories annotation to your configuration class and create a Spring Data Repository.
- [ ] Add an @EnableJpaEntities annotation to your configuration class, create a Spring Data YAML configuration file, and manually update the Spring XML config files to define your repository locations.
- [ ] Add an @EnableDbFunctionality annotation to your configuration class, create a Spring Data XML configuration file, and manually update the Spring factories file to define your repositories.
- [ ] Add an @InitJpaEntities annotation to your configuration class, create a Spring Data properties configuration file, and manually update the Spring startup parameters to define your repository locations.

#### Q38. What is a transaction in the context of Spring Data?

- [ ] a version-controlled schema change that is applied to a database
- [x] a sequence of actions representing a single unit of work managed as a single operation that can be either committed or rolled back
- [ ] an encoded message and response between various shards of a database
- [ ] an exchange or interaction between various worker nodes in a multithreaded environment

#### Q39. Modularization of a concern that cuts across multiple classes is known as a(n)\_\_\_.

- [ ] multiclass
- [x] aspect
- [ ] crosscut
- [ ] sidecut

#### Q40. How do you inject a dependency into a Spring bean?

- [x] any of these answers
- [ ] Annotate a Setter method with the @Autowired annotation.
- [ ] Specify parameters in the constructor with an optional @Autowired annotation.
- [ ] Use field injection.

#### Q41. Consider the properties file application.properties. How would you load the property my.property?

```java
my.property=Test
```

- [ ] A

```java
@Prop("${my.property}")
private String val;
```

- [ ] B

```java
@GetVal("my.property")
private String val;
```

- [ ] C

```java
@GetProperty("${my.property}")
private String val;
```

- [x] D

```java
@Value("${my.property}")
private String val;
```

#### Q42. What is a bean in the context of Spring?

- [x] a managed dependency defined by configuration metadata that can be injected into downstream classes
- [ ] a binary-encoded, agnostic, named entity that is translatable between different data formats
- [ ] a payload that is transferable between different services in a Service-Oriented Architecture (SOA)
- [ ] a discrete piece of data that is encoded in a binary format for persisting to a file system

#### Q43. Which property is given precedence by Spring?

- [ ] application properties located in an application.properties file outside the application.jar
- [ ] @PropertySource annotations on configuration classes
- [x] profile-specific application-{profile}.properties files
- [ ] application properties located in an application.properties file inside the application.jar
