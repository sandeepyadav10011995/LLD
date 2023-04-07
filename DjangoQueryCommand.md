# What Is The Command To Install Django & To Know About It’s Version?
* __Command To Install Django__:
    pip  install  django

* __Command To Check Django Version__:
    python  -m  django  --version

* __Command To Check all the versions of installed modules__:
    pip  freeze

# What Is The Command To Create A Project & An App In Django?
* __Command To Create A Project:__
    django-admin startproject nitman
* __Command To Create An App:__
    python manage.py startapp nitapp
where nitman is project name & nitapp is app name.

# What Is The Command To Run A Project In Django?
__Command To Run A Project:__
    python manage.py runserver
    
By default, this command starts the development server on the internal IP at port 8000.

    If you want to change the server's port, pass it as a command-line argument. 
    For instance, this command starts the server on port 8080:
        python manage.py runserver 8080

    If you want to change the server's IP, pass it along with the port, use:
        python manage.py runserver 0.0.0.0:8000

# What Is The Command For Migrations In Django?
__Command to create a migration file inside the migration folder:__
    python  manage.py  makemigrations

After creating a migration, to reflect changes in the database permanently execute migrate command:
        python  manage.py  migrate

    To see raw SQL query executing behind applied migration execute the command:
        python  manage.py  sqlmigrate  app_name  migration_name
        python  manage.py  sqlmigrate  nitapp  0001 

    To see all migrations, execute the command:
        python  manage.py  showmigrations

    To see app-specific migrations by specifying app-name, execute the command:
        python  manage.py  showmigrations  nitapp

# What Is The Command To Create A Superuser In Django?
__Command To Create A SuperUser:__
    python manage.py createsuperuser

    Enter your desired username and press enter.
        Username: admin
    You will then be prompted for your desired email address:
        Email address: admin@example.com
    The final step is to enter your password twice, 
    the second time as a confirmation of the first.
        Password: **********
        Password (again): *********
    Superuser created successfully.
    
# What Is The Django Command To View A Database Schema Of An Existing (Or Legacy) Database?
__Command to view a database schema of an existing (or legacy) database:__
    python manage.py inspectdb
       
# How To View All Items In The Model Using Django QuerySet?
    Django Command To View All Items In A Model:
        Users.objects.all()
    where  “User” is a model name
# How To Filter Items In The Model Using Django QuerySet?
    Django Command To Filter Items In A Model:
        Users.objects.filter(name="Nitin")
    where  “User” is a model name.
# How To Get A Particular Item In The Model Using Django QuerySet?
    Django Command To Get A Particular Item In A Model:
        Users.objects.get(id=25)
    where  “User” is a model name.
# How to Delete/Insert/Update An Object Using QuerySet In Django?
    QuerySet To Delete An Object:
        Users.objects.filter(id= 54).delete()

    QuerySet To Update An Object:
        user_to_be_modify = User.objects.get(pk = 3)
        user_to_be_modify.city = "Pune"
        user_to_be_modify.save()

    QuerySet To Insert/Add An Object:
        new_user = User(name = "Nitin Mangotra", city="Gurgaon")
        new_user.save()
# How Can You Combine Multiple QuerySets In A View?
Let's suppose the following two models in Django.
```
class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
class Email(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
```
Let's suppose the following three querysets generated from above models, that you want to combine.

* >>> query_set_1 = Blog.objects.filter(id__gte=3)
* >>> query_set_2 = Email.objects.filter(id__lte=11)
* >>> query_set_3 = Blog.objects.filter(id__lte=2)

1. __Using Union Operator:__  
    If both querysets belong to the same model, such as query_set_1 & query_set_3 above, 
    then you can use union operator "|" to easily combine those querysets.
        query_set_result = query_set_1 | query_set_3

    You can use the union operator to combine two or more querysets as shown below.
        combined_result= query_set_1 | query_set_3 | query_set_4 ...

2. __Using Itertools:__
    If both querysets belong to the different  model, such as query_set_1 & query_set_2 above, 
    then you can use itertools combine those querysets.
        from itertools import chain 
        combined_list = list(chain(query_set_1,query_set_2))
    You just need to mention the querysets you want to combine in a comma-separated manner in chain function. You can also use it 
    to combine more than two querysets.
    combined_list = list(chain(query_set_1, query_set_2, query_set_3))
    There is an issue with this approach, you won't get a queryset, you’ll get a list containing instances.
