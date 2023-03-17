## Spring Boot Intro
    Spring Boot is a project that is built on the top of the Spring Framework. 
    It provides an easier and faster way to set up, configure, and run both simple and web-based applications.
    It is a Spring module that provides the RAD (Rapid Application Development) feature to the Spring Framework. 
    It is used to create a stand-alone Spring-based application that you can just run because it needs minimal Spring configuration.

![image](https://user-images.githubusercontent.com/22426280/225797032-354aac21-8849-461c-8205-1290df9723a1.png)

## Spring IOC resolves such dependencies with Dependency Injection, which makes the code easier to test and reuse.Loose coupling between classes can be possible by defining interfaces for common functionality and the injector will instantiate the objects of required implementation.

#### Types of Spring Dependency Injection: 

1. Setter Dependency Injection (SDI): This is the simpler of the two DI methods. In this, the DI will be injected with the help of setter and/or getter methods. Now to set the DI as SDI in the bean, it is done through the bean-configuration file For this, the property to be set with the SDI is declared under the <property> tag in the bean-config file.
2. Constructor Dependency Injection (CDI): In this, the DI will be injected with the help of constructors. Now to set the DI as CDI in bean, it is done through the bean-configuration file For this, the property to be set with the CDI is declared under the <constructor-arg> tag in the bean-config file.

#### Note -: Use constructor injection for the mandatory dependencies and setter injection for optional dependencies. (Here mandatory dependency is the one without which the main business logic wouldn’t work and optional dependencies are the ones which if null doesn’t hamper the main business logic.)
