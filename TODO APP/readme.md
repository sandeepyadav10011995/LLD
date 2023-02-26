
"""
What are Frameworks?
    A framework is collection of modules or packages which helps in writing web applications. It provides
    functionalities to perform operations for developing web applications
        * Faster
        * Easier
        * Reliable
        * Maintainable
        * Scalable
    As we don't have to worry about the low-level details such as protocols, sockets or thread management when we are
    working with a framework. It makes the life developer life easier by giving them a structure for app development,
    they automate the implementations of common solutions which gives the flexibility to developer  to focus only on the
    application logic instead of the routine processes. They provide common patters for faster, reliable, scalable and
    easily maintainable web applications.


        URL Routing ===>> Input Form Handling and Validation ===>> Output Formats with Templating Engine -: HTML, XML, JSON ==>>
        Database Connection, Manipulation using ORM Mappers ===>> Web Security ===>> Session Storage and Retrieval


Template Engine -: It allows the developers to generate a desired content types for example HTML, XML or JSON.

ORM (Object Relational Mapper) -: It is a code library that automates the transfer of data stored in a relational
database into the objects that are most commonly used in an application code.

Web Security -: We also have the web security against cross-site request forgery also known as CSRF, SQL injection,
cross-site scripting and common malicious attacks as well.

Python Frameworks -:

1. DJANGO -:
    * Full Stack Framework
    * Open Source
    * DRY principle( Don't Repeat Yourself)
    * ORM Mappers
    * Authentication
    * URL Routing
    * Template Engine
    * Database Schema Migrations
    * Common DB's -: POSTgre, MySQL, SQLite, Oracle etc.
    * Follow MVC-MVT Architecture

    What is MVC-MVT Architecture?


       USER        <<=========>>      django
                                        ||
                                        ||
                                        ||
          VIEW      <<=========>>      URL
        ||     ||
        ||     ||
        ||     ||
      MODEL  TEMPLATE

        * It is slightly different from MVC, in fact the main difference between the two is that Django takes care of
          the Controller part itself.
        * The Controller is the software code that controls the interaction between the model and the view.


2. FLASK -:
    * Microframework - light weight
    * Built-in development server
    * Fast Debugger
    * REST-ful request dispatching
    * Jinja2 Templating -: Nothing but a modern day templating language made after the Django's template langauge.
    * Unicode Based
    * HTTP request handling
    * Ability to plug any ORM
    * WSGI (Web Server Gateway Interface) -: It actually implements the web server side of the wsgi for running the
                                             python applications that we are making.

    What is Microframework?
    * Full-stack framework does the heavy lifting for the application that we are making but the latter is small and
      very easy to use, also when we are using microframework, the URL Routing is going to be restful for many of the
      occasions.

3. FAST API -:
    *
    *
    *
    *

4. SANIC -:
    *
    *
    *
    *

"""
