## Spring Boot Intro
    Spring Boot is a project that is built on the top of the Spring Framework. 
    It provides an easier and faster way to set up, configure, and run both simple and web-based applications.
    It is a Spring module that provides the RAD (Rapid Application Development) feature to the Spring Framework. 
    It is used to create a stand-alone Spring-based application that you can just run because it needs minimal Spring configuration.

![image](https://user-images.githubusercontent.com/22426280/225797032-354aac21-8849-461c-8205-1290df9723a1.png)


## Spring Boot Architecture
Spring Boot follows a layered architecture in which each layer communicates with the layer directly below or above (hierarchical structure) it.

#### Presentation Layer: 
The presentation layer handles the HTTP requests, translates the JSON parameter to object, and authenticates the request and transfer it to the business layer. In short, it consists of views i.e., frontend part.
Play Video

#### Business Layer: 
The business layer handles all the business logic. It consists of service classes and uses services provided by data access layers. It also performs authorization and validation.

#### Persistence Layer: 
The persistence layer contains all the storage logic and translates business objects from and to database rows.

#### Database Layer: 
In the database layer, CRUD (create, retrieve, update, delete) operations are performed.

![image](https://user-images.githubusercontent.com/22426280/225797340-ebff18ab-1450-43bd-823e-a1a1e1eb7b98.png)


## Spring Boot Flow Architecture
![image](https://user-images.githubusercontent.com/22426280/225797838-2ae458e5-eea9-4b21-a16d-4f7b313f0589.png)

    Now we have validator classes, view classes, and utility classes.
    Spring Boot uses all the modules of Spring-like Spring MVC, Spring Data, etc. 
    The architecture of Spring Boot is the same as the architecture of Spring MVC, except one thing: there is no need for DAO and DAOImpl classes in Spring boot.
    Creates a data access layer and performs CRUD operation.
    The client makes the HTTP requests (PUT or GET).
    The request goes to the controller, and the controller maps that request and handles it. After that, it calls the service logic if required.
    In the service layer, all the business logic performs. It performs the logic on the data that is mapped to JPA with model classes.
    A JSP page is returned to the user if no error occurred.
    
### Spring Annotations -: https://www.javatpoint.com/spring-boot-annotations

    @Component: It is a class-level annotation. It is used to mark a Java class as a bean. A Java class annotated with @Component is found during the classpath. The Spring Framework pick it up and configure it in the application context as a Spring Bean.
    
    @Controller: The @Controller is a class-level annotation. It is a specialization of @Component. It marks a class as a web request handler. It is often used to serve web pages. By default, it returns a string that indicates which route to redirect. It is mostly used with @RequestMapping annotation.
    
    @Service: It is also used at class level. It tells the Spring that class contains the business logic.

    @Repository: It is a class-level annotation. The repository is a DAOs (Data Access Object) that access the database directly. The repository does all the operations related to the database.
    
    @SpringBootApplication: It is a combination of three annotations @EnableAutoConfiguration, @ComponentScan, and @Configuration.


### Spring IOC resolves such dependencies with Dependency Injection, which makes the code easier to test and reuse.Loose coupling between classes can be possible by defining interfaces for common functionality and the injector will instantiate the objects of required implementation.

#### Types of Spring Dependency Injection: 

1. Setter Dependency Injection (SDI): This is the simpler of the two DI methods. In this, the DI will be injected with the help of setter and/or getter methods. Now to set the DI as SDI in the bean, it is done through the bean-configuration file For this, the property to be set with the SDI is declared under the <property> tag in the bean-config file.
2. Constructor Dependency Injection (CDI): In this, the DI will be injected with the help of constructors. Now to set the DI as CDI in bean, it is done through the bean-configuration file For this, the property to be set with the CDI is declared under the <constructor-arg> tag in the bean-config file.

#### Note -: Use constructor injection for the mandatory dependencies and setter injection for optional dependencies. (Here mandatory dependency is the one without which the main business logic wouldn’t work and optional dependencies are the ones which if null doesn’t hamper the main business logic.)
    
#### Common Questions -: https://www.javatpoint.com/spring-interview-questions
