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

















