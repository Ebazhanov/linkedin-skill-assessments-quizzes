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
- [ ] 1. afterPropertiesSet()
       2. init-method
       3. @PostConstruct
- [x] 1. @PostConstruct
       2. afterPropertiesSet()
       3. init-method
- [ ] 1. init-method
       2. afterPropertiesSet()
       3. @PostConstruct
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