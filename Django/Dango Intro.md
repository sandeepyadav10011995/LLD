# Explain Django Architecture? Also Explain Model, Template And Views.
    * Django follows a software design pattern called as MVT (Model View Template) Architecture.
    * It is based on the Model View Controller architecture (MVC). But is slightly different from the MVC pattern as it maintains its 
      own conventions, so, the controller is handled by the framework itself.
    * Model: It helps in handling the database (Models). They provide the options to create, edit and query data records in the database
    * Template: The template is a presentation layer. It defines the structure of file layout to represent data in a web page. It is an 
      HTML file mixed with Django Template Language (DTL).
    * View: The View is used to execute the business logic and interact with a model to carry data and renders a template.

The developer provides the model, the view, and the template then maps it to a URL, and finally, Django serves it to the user.
For Example:
 * Here, a user requests for a resource to the Django, Django works as a controller and check to the available resource in URL. 
   (urls.py file)
 * If URL maps, a view is called that interact with model and template, it renders a template.
 * Django responds back to the user and sends a template as a response.

# Explain How A Request Is Processed In Django?
  * Here, a user requests for a resource to the Django, Django works as a controller and check to the available resource in URL.
  * When Django server is started, the manage.py file searches for settings.py file, which contains information of all the 
    applications installed in the project, middleware used, database connections and path to the main urls config.
    ![image](https://user-images.githubusercontent.com/22426280/230561740-cdc3c5d2-bbef-4e26-af2f-49d80c6b67fb.png)

  #### Manage.py >> Setting.py >> urls.py >> views.py >> models.py >> templates
      Django first determines which root URLconf or URL configuration module is to be used
      Then, that particular Python module urls is loaded and then Django looks for the variable urlpatterns
      Then check each URL patterns in urls.py file, and it stops at the first match of the requested URL
      Once that is done, the Django then imports and calls the given view.
      In case none of the URLs match the requested URL, Django invokes an error-handling view
      If URL maps, a view is called that interact with model and template, it renders a template.
      Django responds back to the user and sends a template as a response.

###  Important Info --> Project
  * manage.py: A command-line utility that allows you to interact with your Django project & this file is used to control your 
               Django project on the server or even to begin one.
  * __init__.py: An empty file that tells Python that the current directory should be considered as a Python package
  * settings.py: Comprises the configurations of the current project like DB connections, middlewares etc
  * urls.py: All the URLs of the project are present here
  * wsgi.py: This is an entry point for your application which is used by the web servers to serve the project you have created.

### Important Info --> App
  * __init__.py - An empty file that tells Python that the current directory should be considered as a Python package
  * admin.py: Reads model metadata and provides an interface to manage app content
  * app.py: Application configuration details for the app are included e.g custom app name.
  * migrations/: Contains migrated model details with the corresponding database table structure
  * models.py: A class for each model is defined with the model structure layout
  * tests.py: App unit test automation classes are included in this
  * views.py: Web based requests and response is configured in this file

# Why Is Django Called A Loosely Coupled Framework?
  * Django is called a loosely coupled framework because of its MVT architecture, which is a variant of the MVC architecture. 
  * MVT helps in separating the server code from the client-related code. 
    Django’s Models and Views are present on the client machine and only templates return to the client, which are essentially HTML, 
  * CSS code and contains the required data from the models.
  * These components are totally independent of each other and therefore, front-end developers and backend developers can work 
    simultaneously on the project as these two parts changing will have little to no effect on each other when changed.
  #### Therefore, Django is a loosely coupled framework.

# Explain The Migration In Django.
    There are several commands you use to interact with Migrations In Django:
      * makemigration - This command is used to create a migration file.
      * migrate - This command creates a table according to the schema defined in migration file.
      * showmigrations - This command list all the migrations and their status.
      * sqlmigrate - This command is used to show a raw SQL query of the applied migration.

# What is Django ORM?
    ORM stands for Object-relational Mapper.
    This ORM enables us to interact with databases in a more pythonic way like we can avoid writing raw queries.
    It is possible to retrieve, save, delete and perform other operations over the database without ever writing any SQL query.
    It helps us with working with data in a more object-oriented way.
# How You Can Set Up The Database In Django?
    To set up a database in Django, you can find its configurations in setting.py  file that representing Django settings.

    By default, Django uses SQLite database. It is easy for Django users because it doesn’t require any other type of installation. 

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
    
    In the case of other database you have to the following keys in the DATABASE ‘default’ item to match your database connection settings.
    Engines: you can change database by using ‘django.db.backends.sqlite3’ , ‘django.db.backeneds.mysql’, ‘django.db.backends.postgresql_psycopg2’, ‘django.db.backends.oracle’ and so on

    'ENGINE': 'django.db.backends.postgresql_psycopg2',

    Now we should replace the above code with our connection credentials to Mysql. The updated code should look like the code below.

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'helloworld',
            'USER': '<yourname>',
            'PASSWORD': 'password',
            'HOST': 'localhost',
            'PORT': '',
        }
    }

# What do you mean by the CSRF Token?
    * CSRF stands for Cross Site Request Forgery. 
    * The csrf_token is used for protection against Cross-Site Request Forgeries. 
    * This kind of attack takes place when a malicious website consists of a link, some JavaScript or a form whose aim is to perform 
      some action on your website by using the login credentials of a genuine user.
    * CSRF tokens can prevent CSRF attacks by making it impossible for an attacker to construct a fully valid HTTP request suitable for 
      feeding to a victim user. 
    * A CSRF token is a unique, secret, unpredictable value that is generated by the server-side application and transmitted to the client 
      in such a way that it is included in a subsequent HTTP request made by the client. 
    * When the later request is made, the server-side application validates that the request includes the expected token and rejects the 
      request if the token is missing or invalid.
      
# What Is The Difference Between select_related & prefetch_related?
### select_related:
  * Returns a QuerySet that will “follow” foreign-key relationships, selecting additional related-object data when it executes its query. 
  * This is a performance booster which results in a single more complex query but means later use of foreign-key relationships won’t 
    require database queries.
### prefetch_related:
  * We use prefetch_related when we’re going to get a set of things.
  * That means forward ManyToMany and backward ManyToMany, ForeignKey. 
  * prefetch_related does a separate lookup for each relationship, and performs the “joining” in Python.

# What Is The Difference Between Emp.object.filter(), Emp.object.get() & Emp.objects.all() in Django Queryset?

#### Emp.object.filter() & Emp.object.get(): 
  * To filter out some element from the database, you either use the get() method or the filter() method as follows:
  * Users.objects.filter(name="Nitin")
  * Users.objects.get(name="Nitin")
#### Basically use get() when you want to get a single unique object, &
  * filter() when you want to get all objects that match your lookup parameters

#### get() throws an error if there’s no object matching the query. 
  * filter() will return an empty queryset.
  * get() raises MultipleObjectsReturned if more than one object was found. The MultipleObjectsReturned exception is an attribute of 
    the model class.
  * get() raises a DoesNotExist exception if an object wasn't found for the given parameters. This exception is also an attribute of 
    the model class.
# How Static Files Are Defined In Django? Explain Its Configuration & It’s Uses.
    Websites generally need to serve additional files such as images. Javascript or CSS. In Django, these files are referred to as 
    “static files”, Apart from that Django provides django.contrib.staticfiles to manage these static files.
    These files are created within the project app directory by creating a subdirectory named as static.
    Static files are stored in the folder called static in the Django app.
#### How to configure static files?
  * Ensure that django.contrib.staticfiles is added to your INSTALLED_APPS
  * In your settings file. define STATIC_URL for ex.
    STATIC_URL = '/static/'
  * In your Django templates, use the static template tag to create the URL for the given relative path using the configured 
    STATICFILES_STORAGE.
  * Store your static files in a folder called static in your app. For example -: my_app/static/my_app/example.jpg

#### How can you set up static files in Django?
There are three main things required to set up static files in Django:
  1) Set the STATIC_ROOT setting to the directory from which you’d like to serve these files, e.g:
      STATIC_ROOT = "/var/www/example.com/static/"
  2) Run the collectstatic management command:
      python manage.py collectstatic
      This will copy all files from your static folders into the STATIC_ROOT directory.
  3) set up a Static Files entry on the PythonAnywhere web tab

# What Are The Advantages And Disadvantages Of Using Django?
   * Django is a Python's framework which is easy to learn.
   * Django follows the DRY or the Don’t Repeat Yourself Principle which means, one concept or a piece of data should live in just 
     one place
   * Django Offers Better CDN connectivity and Content Management
   * Django is a Batteries Included Framework
   * Django Offers Rapid-development
   * Django is highly Scalable
   * Django provide high Security
   * Django facilitates you to divide code modules into logical groups to make it flexible to change.
   * Django provides auto-generated web admin to make website administration easy.
   * Django provides template system to define HTML template for your web page to avoid code duplication.
   * Django enables you to separate business logic from the HTML.

# What Are The Advantages And Disadvantages Of Using Django?
   * Django is Monolithic. You must know the full system to work with it.
   * Django's monolithic size makes it unsuitable for smaller projects
   * Everything must be explicitly defined due to a lack of convention.
   * Django's modules are bulky.
   * Django is completely based on Django ORM.
   * Components are deployed together.

# What is django.shortcuts.render function?
* The basic syntax:
    render(request, template_name, context=None, content_type=None, status=None, using=None)

      The request is the parameter that generates the response. 
      The template name is the HTML template used.
      The context is a dict of the data passed on the page from the python.
      You can also specify the content type, 
      The status of the data you passed, 
      And the render you are returning.

# What Is The Significance Of manage.py File In Django?
   * The manage.py file is automatically generated whenever you create a project. 
   * This is basically a command-line utility that helps you to interact with your Django project in various ways. 
   * It does the same things as django-admin but along with that, it also sets the DJANGO_SETTINGS_MODULE environment variable in order to       point to your project’s settings. 
   * When Django server is started, the manage.py file searches for settings.py file, which contains information of all the applications         installed in the project, middleware used, database connections and path to the main urls config

# What Is The Use Of The “include” Function In The urls.py File In Django?
   * As in Django there can be many apps, each app may have some URLs that it responds to. 
   * Rather than registering all URLs for all apps in a single urls.py file, each app maintains its own urls.py file, and in 
     the project’s urls.py file we use each individual urls.py file of each app by using the include function.
#### Example:
```
nitman -- urls.py

    from django.contrib import admin  
    from django.urls import path, include

    urlpatterns = [  
        path('admin/', admin.site.urls),  
        path('nitapp/', include('nitapp.urls')),  
        path('myapp/', include('myapp.urls')),  
    ]  
```
```
nitapp -- urls.py

    from django.urls import path
    from . import views

    urlpatterns = [  
        path('', views.index),  # nitapp homepage
    ]     

```
```
myapp -- urls.py

    from django.urls import path
    from . import views

    urlpatterns = [  
        path('', views.index),  # myapp homepage
    ]  

```

# What Is Context In Django?
   * A context in Django is a dictionary, in which keys represent variable names and values represent their values. This dictionary              (context) is passed to the template which then uses the variables to output the dynamic content.
   * A context is a variable name -> variable value mapping that is passed to a template.
   * Context processors let you specify a number of variables that get set in each context automatically – without you having to specify        the variables in each render() call.
   
# What Is The Difference Between Django OneToOneField & ForeignKey Field?
   * __ForeignKey Field__: A many-to-one relationship. Requires two positional arguments: the class to which the model is related and the on_delete option.

   * __OneToOneField__: A one-to-one relationship. Conceptually, this is similar to a ForeignKey with unique=True, but the “reverse” side of the relation will directly return a single object.


# What Is A Middleware In Django?
   * Middleware is something that executes between the request and response. 
   * In simple words, you can say it acts as a bridge between the request and response. 
   * Middleware in the Django framework is the component that operates on request and transfers it to the view and before passing it to the     template engine, it starts operating on a response. 
   * Django provides various built-in middleware and also allows us to write our own middleware. 

            // settings.py
            MIDDLEWARE = [  
                'django.middleware.security.SecurityMiddleware',  
                'django.contrib.sessions.middleware.SessionMiddleware',  
                'django.middleware.common.CommonMiddleware',  
                'django.middleware.csrf.CsrfViewMiddleware',  
                'django.contrib.auth.middleware.AuthenticationMiddleware',  
                'django.contrib.messages.middleware.MessageMiddleware',  
                'django.middleware.clickjacking.XFrameOptionsMiddleware',  
            ] 
 ####  Some usage of Middlewares in Django is:
         Session management,
         Use authentication
         Cross-site request forgery protection(CSRF)
         Content Gzipping

# What Is Sessions In Django?
   * Sessions are fully supported in Django.
   * Using the session framework, you can easily store and retrieve arbitrary data based on the per-site-visitors.
   * This framework basically stores data on the server-side and takes care of sending and receiving cookies. 
   * These cookies consist of a session ID but not the actual data itself unless you explicitly use a cookie-based backend.
   * A session is a mechanism to store information on the server side during the interaction with the web application. 
   * By default, session stores in the database and also allows file-based and cache based sessions.

# What Are Django Signals?
      Django consists of a signal dispatcher that helps allow decoupled applications to get notified when actions occur elsewhere in the framework. 
      Django provides a set of built-in signals that basically allow senders to notify a set of receivers when some action is executed.
      They’re especially useful when many pieces of code may be interested in the same events.

      Two important parameters in signals are as follows:

      Receiver: It specifies the callback function which connected to the signal.
      Sender: It specifies a particular sender from where a signal is received.
#### List of built-in signals in the models:
<img width="500" alt="Screenshot 2023-04-07 at 12 47 49 PM" src="https://user-images.githubusercontent.com/22426280/230561594-91b21e4c-06e6-4921-9db7-b94abf3d5e11.png">



# Explain Q objects in Django ORM?
   * Q object django.db.models.Q is an object to encapsulate a collection of keyword arguments specified as FIELD LOOKUPS.
   * Q objects are used to write complex queries, as in filter() functions just "AND" the conditions while if you want to "OR" the conditions   you can use Q objects. 
   * Let’s see an example:
   ```
         from django.db import models
         from django.db.models import Q
         Models.objects.get( Q(question__startswith='When'), Q(answer__startswith='On')  | Q(answer__startswith='At') )
   ```
   * [Q Objects can be combined with the help of the | and & operators to get a new Q Object]
   * This is equivalent to the following SQL WHERE Clause:
         SELECT * FROM Model WHERE question LIKE ‘When%’ And (answer="On%" OR answer="At%")

# What Is Serialization In Django?
__Serialization__ is the process of converting Django models into other formats such as XML, JSON, etc.

# What Is Mixin?
__Mixin__ is a type of multiple inheritance wherein you can combine behaviors and attributes of more than one parent class.
Django provides a number of mixins that provide more discrete functionality. 
Different type of mixins are -
* __ContextMixin__ - A dictionary to include in the context and is a convenient way of specifying the simple context in as_view().
* __TemplateResponseMixin__ - Given a suitable context, TemplateResponseMixin provides a mechanism to construct a TemplateRespons and the     template to use is configurable and can be further customized by a subclass.
* __SingleObjectMixin__ - SingleObjetMixin provides a mechanism for looking up an object associated with the current HTTP request.
* __SingleObjectTemplateMixin__ - SingleObjetTemplateMixin performs template base response rendering for view that operate upon a single     object instance. 
* __MutlipleObjectMixin__ - MultipleObjectMixin used to display list of objects

# Explain all the process behind delete a row in a web app using Django.
To delete a row in a web app using Django, you need to follow these general steps:
* Create a view for the delete operation
   * To create a view for deleting a row, you need to import the necessary modules and define a function that handles the delete operation.
   * The function should take the primary key (PK) of the row to be deleted as a parameter.
* Create a template for the delete confirmation page
   * Create a template for the delete confirmation page where the user can confirm the deletion. 
   * The template should display the row data to be deleted and prompt the user to confirm the deletion.
* Add a URL pattern for the delete view
   * In your urls.py file, add a URL pattern for the delete view. 
   * The URL pattern should include the PK of the row to be deleted.
* Implement the delete operation in the view 
   * In the MyModelDeleteView class defined in step 1, the DeleteView class handles the delete operation. 
   * The success_url attribute specifies the URL to redirect to after a successful deletion. 
   * If you need to perform additional operations before or after the deletion, you can override the delete method in the MyModelDeleteView      class. 

