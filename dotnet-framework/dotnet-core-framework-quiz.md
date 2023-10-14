## .NET Core Framework Questions

#### Q1. What is the key difference between .NET Core and the .NET Framework?

- [x] .NET Core is cross-platform, while .NET Framework is Windows-only. 
- [ ] .NET Framework is open-source, while .NET Core is proprietary.
- [ ] .NET Core is primarily used for web development, while .NET Framework is for desktop applications.
- [ ] There is no significant difference between them.

#### Q2. In .NET Core, which file is used to define project dependencies and settings?

- [ ] .json
- [ ] .sln
- [ ] .config
- [x] .csproj 

#### Q3. What is the purpose of the "dotnet ef" tool in .NET Core?

- [ ] To create Entity Framework models.
- [x] To run Entity Framework migrations. 
- [ ] To manage environment variables.
- [ ] To publish a .NET Core application.

#### Q4. Which of the following is NOT a valid .NET Core hosting model?

- [ ] In-Process Hosting
- [ ] Out-of-Process Hosting
- [ ] Self-Hosting
- [x] Cloud Hosting 

#### Q5. What is the purpose of the "Startup.cs" file in an ASP.NET Core application?

- [x] To configure services and middleware for the application. 
- [ ] To define the main entry point of the application.
- [ ] To configure the database connection string.
- [ ] To store user authentication data.

#### Q6.Which of the following authentication mechanisms is NOT supported by ASP.NET Core?

- [ ] JWT Authentication
- [ ] Windows Authentication
- [ ] OAuth 2.0
- [x] Basic Authentication  

#### Q7. In .NET Core, what is the role of the "IServiceCollection" interface in the dependency injection container?

- [ ] It represents the concrete service implementations.
- [x] It defines a contract for registering and resolving services.
- [ ] It is used for database connections.
- [ ] It handles configuration settings.

#### Q8. What is the purpose of the "appsettings.json" file in an ASP.NET Core application?

- [x] To store application configuration settings. 
- [ ] To define routing rules for the application.
- [ ] To configure the application's authentication settings.
- [ ] To define the application's entry point.

#### Q9.Which .NET Core tool is used to create and manage migrations in Entity Framework Core?

- [ ] dotnet publish
- [x] dotnet ef 
- [ ] dotnet restore
- [ ] dotnet build

#### Q10. What is Kestrel in the context of ASP.NET Core?

- [ ] A database management system.
- [x] An HTTP server for hosting ASP.NET Core applications. 
- [ ] A client-side JavaScript framework.
- [ ] A testing framework for ASP.NET Core.

#### Q11.Which of the following is NOT a valid option for deploying a .NET Core application?

- [ ] Docker containers
- [ ] Azure App Service
- [ ] AWS Lambda
- [x] Apache Tomcat

#### Q12. What is the purpose of "Middleware" in ASP.NET Core?

- [ ] It is a design pattern used for data access.
- [ ] It defines the data models for the application.
- [x] It handles HTTP requests and responses in the request pipeline. 
- [ ] It is a way to define database migrations.

#### Q13. In .NET Core, what is the difference between "FirstOrDefault" and "FirstOrDefaultAsync" when querying a database?

- [ ] "FirstOrDefault" is synchronous, and "FirstOrDefaultAsync" is asynchronous. 
- [x] "FirstOrDefault" returns multiple results, while "FirstOrDefaultAsync" returns a single result.
- [ ] "FirstOrDefault" is used for SQL databases, and "FirstOrDefaultAsync" is for NoSQL databases.
- [ ] There is no difference between them.

#### Q14. Which of the following is a valid way to handle asynchronous operations in .NET Core?

- [ ] Synchronous methods with locks.
- [x] Using the "async" and "await" keywords. 
- [ ] Multithreading without synchronization.
- [ ] Creating a separate thread for each operation.

#### Q15. What is the difference between a SDK (software development kit) and runtime in .NET Core?

- [ ] The SDK is the "virtual machine" that hosts and runs the application and abstracts all the interaction with the operating system; the runtime usually includes documentation and other help files.
- [x] The runtime is the virtual machine that hosts and runs the application and abstracts all the interaction with the operating system; the SDK usually includes documentation and other help files.
- [ ] The runtime compiles code along with the CLR; the SDK usually includes documentation and other help files.
- [ ] The SDK compiles code along with the CLR; the runtime usually includes documentation and other help files.

#### Q16. What is the purpose of the "UseIISIntegration" method in an ASP.NET Core application's startup configuration?

- [x] To enable integration with Internet Information Services (IIS). 
- [ ] To configure custom error pages.
- [ ] To enable session state management.
- [ ] To set up automatic API documentation generation.


#### Q17.Which .NET Core component is used for managing cross-cutting concerns such as logging, validation, and security?

- [ ] Entity Framework Core
- [ ] Dependency Injection
- [ ] Middleware
- [x] Aspect-Oriented Programming (AOP) 

#### Q18. What is the primary role of the Entity Framework in .NET Core?

- [x] To provide data access and object-relational mapping (ORM) capabilities.
- [ ] To create and manage databases.
- [ ] To handle user authentication and authorization.
- [ ] To define routes for web applications.

#### Q19. What is the main benefit of using a reverse proxy server, like Nginx or Apache, in front of an ASP.NET Core application?

- [x] Improved application performance.
- [ ] Enabling WebSocket communication.
- [ ] Simplifying API documentation.
- [ ] Enhanced security.

#### Q20. Which hosting environment variable is typically used to specify the environment in ASP.NET Core?

- [x] ASPNETCORE_ENVIRONMENT 
- [ ] APPLICATION_ENV
- [ ] HOST_ENV
- [ ] DEPLOY_ENV

#### Q21. What is the purpose of "Globalization" and "Localization" in ASP.NET Core?

- [ ] To create global-scale applications.
- [ ] To control the visibility of API endpoints.
- [x] To handle language and culture-specific content in an application.
- [ ] To optimize database queries.

#### Q22. Which of the following is NOT a key feature of .NET Core?

- [ ] Cross-platform support
- [ ] Open-source
- [ ] Unified class libraries
- [x] Support for Silverlight

#### Q23. What is the role of the "dotnet watch" tool in .NET Core development?

- [x] To watch and recompile code on file changes
- [ ] To create database migrations
- [ ] To manage NuGet packages
- [ ] To publish the application 

#### Q24. In .NET Core, which attribute is used to specify the route for a controller action?

- [x] [Route]
- [ ] [RouteAttribute]
- [ ] [ActionRoute]
- [ ] [HttpRoute]

#### Q25. What is the purpose of the "dotnet new" command in .NET Core?

- [ ] To create a new ASP.NET Core application
- [ ] To generate a new migration in Entity Framework
- [ ] To add a new dependency to a project
- [x] To create a new project or file from a template

#### Q26. In ASP.NET Core, what is the default file extension for view files?

- [ ] .html
- [x] .cshtml
- [ ] .aspx
- [ ] .razor

#### Q27. What is SignalR in the context of ASP.NET Core?

- [ ] A web server for serving static files
- [x] A library for real-time communication 
- [ ] A database management system
- [ ] A client-side JavaScript framework

#### Q28. What is SignalR in the context of ASP.NET Core?
- [ ] A web server for serving static files
- [x] A library for real-time communication 
- [ ] A database management system
- [ ] A client-side JavaScript framework

#### Q29. What does the "Entity Framework Core" use to represent the database schema in code?

- [ ] Data models
- [ ] Migrations
- [ ] DbContext
- [x] Code-first approach 

#### Q30. Which of the following is NOT a supported database provider in Entity Framework Core?

- [x] SQL Server 
- [ ] MySQL
- [ ] SQLite
- [ ] MongoDB 

#### Q31. What is the purpose of the "Startup.cs" file's "ConfigureServices" method in an ASP.NET Core application?

- [ ] To define the routing for the application
- [x] To configure the application's services and dependencies 
- [ ] To handle HTTP requests
- [ ] To set up authentication and authorization

#### Q32. In ASP.NET Core, which middleware is responsible for routing HTTP requests to controller actions?

- [ ] UseMvc
- [x] UseRouting 
- [ ] UseEndpoints
- [ ] UseAuthentication

#### Q33. What is the main purpose of the "ASP.NET Core Identity" framework?

- [x] To provide authentication and identity services 
- [ ] To create Entity Framework migrations
- [ ] To serve static files
- [ ] To manage database connections

#### Q34. Which of the following database providers is not officially supported by Entity Framework Core but can be used with third-party providers?

- [ ] SQL Server
- [ ] MySQL
- [ ] PostgreSQL
- [x] Oracle 

#### Q35. In .NET Core, which tool is used to add or update NuGet packages in a project?

- [ ] dotnet publish
- [ ] dotnet nuget
- [ ] dotnet package
- [x] dotnet add package 

#### Q36. What is the primary role of the "appsettings.Development.json" configuration file in an ASP.NET Core application?

- [ ] To store production environment settings
- [x] To store settings for the development environment 
- [ ] To store database connection strings
- [ ] To configure authentication

#### Q37. What is the purpose of "Model Binding" in ASP.NET Core?

- [ ] To define data models for the application
- [x] To bind data from HTTP requests to action parameters 
- [ ] To validate models in the application
- [ ] To create database migrations 

#### Q38. Which of the following is NOT a valid response type for an ASP.NET Core controller action?

- [ ] IActionResult
- [ ] JsonResult
- [ ] FileStreamResult
- [x] DataModelResult 
 
#### Q39. What is the purpose of "Dependency Injection" in .NET Core?

- [ ] To add external dependencies to the project
- [ ] To manage database connections
- [x] To inject services and dependencies into components 
- [ ] To create a Singleton pattern for the application

#### Q40. Which of the following is NOT a valid HTTP status code in ASP.NET Core?

- [ ] 200 (OK)
- [ ] 404 (Not Found)
- [ ] 500 (Internal Server Error)
- [x] 700 

#### Q41. What is the role of the "dotnet ef database update" command in Entity Framework Core?

- [ ] To create a new database
- [x] To apply pending migrations and update the database schema 
- [ ] To roll back a migration
- [ ] To generate a new migration

#### Q42. In ASP.NET Core, what is the purpose of the "UseExceptionHandler" middleware?

- [ ] To handle HTTP requests for static files
- [ ] To configure routing for the application
- [x] To handle exceptions and errors in the application 
- [ ] To enable authentication and authorization

#### Q43. Which attribute is used to specify that a method in a controller should only accept HTTP POST requests?

- [x] [HttpPost] 
- [ ] [Route]
- [ ] [HttpGet]
- [ ] [HttpPut]

#### Q44. What is the role of the "app.UseHttpsRedirection()" middleware in an ASP.NET Core application?

- [ ] To enable HTTP/2 support
- [x] To enforce HTTPS for all requests 
- [ ] To handle WebSocket communication
- [ ] To serve static files

#### Q45. In Entity Framework Core, what is the purpose of the "InverseProperty" attribute?

- [ ] To specify primary key columns
- [x] To define relationships between entities (Correct)
- [ ] To configure the database connection
- [ ] To specify foreign key constraints

#### Q46. What is the purpose of "Singleton" and "Transient" lifetimes in .NET Core dependency injection?

- [ ] To configure authentication
- [ ] To specify database connections
- [x] To control the lifetime and scope of services 
- [ ] To define routing rules

#### Q47. Which .NET Core tool is used to create unit tests for your application?

- [x] dotnet test 
- [ ] dotnet build
- [ ] dotnet publish
- [ ] dotnet migrate

#### Q48. In ASP.NET Core, which attribute is used to specify that a controller or action should require authorization for access?

- [x] [Authorize] 
- [ ] [AllowAnonymous]
- [ ] [Role]
- [ ] [Authenticate]

#### Q49. What is the role of the "Content Negotiation" feature in ASP.NET Core?

- [ ] To negotiate database connections
- [ ] To optimize application performance
- [x] To select the appropriate response format based on client preferences
- [ ] To manage middleware components

#### Q50. In .NET Core, what is the purpose of the "dotnet publish" command?

- [ ] To create Entity Framework migrations
- [x] To build the application for deployment
- [ ] To watch for file changes in development mode
- [ ] To add NuGet packages to the project

#### Q51. In .NET Core, what is the purpose of the "dotnet CLI"?

- [ ] To create and manage databases
- [ ] To manage NuGet packages
- [x] To build, run, and manage .NET Core applications from the command line 
- [ ] To configure routing in ASP.NET Core


#### Q52. What is a "Razor Page" in ASP.NET Core?

- [ ] A middleware for handling HTTP requests
- [x] A type of view used for building web pages with Razor syntax 
- [ ] A component for dependency injection
- [ ] A type of model in Entity Framework Core

#### Q53. What is "Entity Framework Core Code-First" approach?

- [ ] Designing the database schema first and then generating code entities
- [x] Creating code entities first and generating the database schema 
- [ ] A way to perform CRUD operations without code
- [ ] A pattern for handling HTTP requests

#### Q54. Which .NET Core component is responsible for managing database connections and data access?

- [x] Entity Framework Core 
- [ ] Identity Framework
- [ ] Razor Pages
- [ ] Kestrel

#### Q55. In ASP.NET Core, what is the purpose of "Razor View Components"?

- [ ] To define routing for the application
- [ ] To handle HTTP requests
- [x] To encapsulate complex rendering logic into reusable components 
- [ ] To create and manage databases

#### Q56. What is "Entity Framework Core Lazy Loading"?

- [x] A technique for deferring the loading of related entities until they are explicitly accessed 
- [ ] A mechanism for optimizing database queries
- [ ] A feature to load all entities eagerly
- [ ] A way to manage connections to databases

#### Q57. In ASP.NET Core, what is the purpose of "Model Validation"?

- [ ] To validate database connections
- [ ] To validate user authentication
- [x] To ensure that data in model objects is valid before processing it 
- [ ] To manage services and dependencies

#### Q58. Which .NET Core tool is used for generating API documentation for your application?

- [x] Swashbuckle 
- [ ] Postman
- [ ] Swagger
- [ ] Fiddlerx

#### Q59. What is "Entity Framework Core Shadow Properties" used for?

- [ ] To create virtual entities
- [ ] To store sensitive data securely
- [x] To store additional data in the database without adding it to the entity class 
- [ ] To encrypt data

#### Q60. In ASP.NET Core, what is "Response Compression" middleware used for?

- [ ] To compress HTTP requests
- [x] To compress HTTP responses to reduce bandwidth 
- [ ] To handle WebSocket communication
- [ ] To manage database connections

#### Q61. What is "Entity Framework Core Value Conversions" used for?

- [x] To convert values between different data types for database storage and retrieval 
- [ ] To create virtual properties in entity classes
- [ ] To serialize and deserialize JSON data
- [ ] To define routing rules for the application

#### Q62. In ASP.NET Core, what is the "Content Security Policy (CSP)" used for?

- [ ] To define routes for API endpoints
- [ ] To handle database connections
- [x] To control the sources from which content can be loaded 
- [ ] To create test cases

#### Q63. What is "Entity Framework Core Table Splitting" used for?

- [ ] To optimize database queries
- [ ] To store database schemas as tables
- [x] To map a single entity to multiple database tables 
- [ ] To perform server-side rendering

#### Q64. In ASP.NET Core, what is the purpose of the "ResponseCache" middleware?

- [ ] To manage authentication and authorization
- [x] To cache HTTP responses to improve performance
- [ ] To handle routing and URL generation
- [ ] To create WebSocket connections

#### Q65. In ASP.NET Core, what is the purpose of "Cross-Site Request Forgery (CSRF) protection"?

- [ ] To handle WebSocket communication
- [ ] To validate model data
- [x] To prevent CSRF attacks by validating and generating anti-forgery tokens 
- [ ] To manage database connections

#### Q66. What is the role of the "Startup.cs" file's "Configure" method in an ASP.NET Core application?

- [ ] To define routing rules
- [ ] To configure the application's services and dependencies
- [ ] To handle HTTP requests
- [x] To define the request pipeline and how the application responds to requests (Correct)

#### Q67. What is "Entity Framework Core Owned Entity Types" used for?

- [ ] To create complex data models
- [ ] To define a one-to-many relationship between entities
- [ ] To include one entity type within another
- [x] To specify that an entity type is part of another entity type and share its table 

#### Q68. In ASP.NET Core, what is the "Anti-Forgery Token" used for?

- [x] To protect against Cross-Site Request Forgery (CSRF) attacks by validating and generating tokens 
- [ ] To handle WebSockets
- [ ] To manage authentication
- [ ] To optimize database queries

#### Q69. What is "Entity Framework Core Change Tracking" used for?

- [ ] To track changes to the source code
- [ ] To keep a record of the database schema changes
- [x] To track changes to entity objects and determine what needs to be updated in the database 
- [ ] To configure caching in ASP.NET Core

#### Q70. In ASP.NET Core, what is "Model Metadata" used for?

- [ ] To define routing rules
- [ ] To generate API documentation
- [x] To provide additional information about model properties for validation and display purposes 
- [ ] To create database indexes

#### Q71. In ASP.NET Core, what is "Custom Tag Helpers" used for?

- [ ] To create custom routing rules
- [ ] To define services and dependencies
- [x] To extend HTML tags with custom attributes and behaviors
- [ ] To perform database migrations

#### Q72. What is the default port number used by ASP.NET Core applications?

- [ ] 80
- [ ] 443
- [x] 5000
- [ ] 8080

#### Q73. What is the role of Views in ASP.NET Core?

- [ ] To handle HTTP requests and return responses
- [ ] To configure the application’s routing
- [ ] To store and retrieve data from a database
- [x] To generate HTML responses to be sent to the client

#### Q74. What is the purpose of the [Route] attribute in ASP.NET Core?

- [ ] To specify the HTTP verb that a controller or action responds to
- [x] To specify the URL path for a controller or action
- [ ] To enable caching for a controller or action
- [ ] To restrict access to a controller or action to authorized users only

#### Q75. What is the purpose of the [HttpGet], [HttpPost], [HttpPut], and [HttpDelete] attributes in ASP.NET Core?

- [x] To specify the HTTP verb that a controller or action responds to
- [ ] To specify the URL path for a controller or action
- [ ] To enable caching for a controller or action
- [ ] To restrict access to a controller or action to authorized users only

#### Q76: What is the purpose of the HttpClient class in ASP.NET Core?

- [x] To handle HTTP requests and responses
- [ ] To manage database connections
- [ ] To handle authentication and authorization
- [ ] To generate PDF documents+
