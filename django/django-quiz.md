## Django

#### Q1. To cache your entire site for an application in Django, you add all except which of these settings?

- [ ] django.middleware.common.CommonMiddleware
- [ ] django.middleware.cache.UpdateCacheMiddleware
- [ ] django.middleware.cache.FetchFromCacheMiddleware
- [x] django.middleware.cache.AcceleratedCacheMiddleware

**Reference:**
Django comes with a robust cache system that lets you save dynamic pages, so they don’t have to be computed for each request. For convenience, Django offers cache with different granularity — from entire website to pages to part of pages to DB query results to any objects in memory. Cache middleware. If enabled, each Django-powered page will be cached based on URL.

#### Q2. In which programming language is Django written?

- [ ] C++
- [ ] Java
- [x] Python
- [ ] Ruby

#### Q3. To automatically provide a value for a field, or to do validation that requires access to more than a single field, you should override the `___` method in the `___` class.

- [ ] validate(); Model
- [ ] group(); Model
- [ ] validate(); Form
- [x] clean(); Field

#### Q4. A client wants their site to be able to load "Rick & Morty" episodes by number or by title—e.g., shows/3/3 or shows/picklerick. Which URL pattern do you recommend?

- [ ] A

```python
url(r'shows/<int:season>/<int:episode>/', views.episode_number),
url(r'shows/<slug:episode_name>/', views.episode_name)
```

- [x] B

```python
path('shows/<int:season>/<int:episode>/', views.episode_number),
path('shows/<slug:episode_name>/', views.episode_name)
```

- [ ] C

```python
path('shows/<int:season>/<int:episode>', views.episode_number),
path('shows/<slug:episode_name>/', views.episode_number)
```

- [ ] D

```python
url(r'^show/(?P<season>[0-9]+)/(?P<episode>[0-9]+)/$', views.episode_number),
url(r'^show/(?P<episode_name>[\w-]+)/', views.episode_name
```

#### Q5. How do you determine at startup time if a piece of middleware should be used?

- [x] Raise MiddlewareNotUsed in the **init** function of your middleware.
- [ ] Implement the not_used method in your middleware class.
- [ ] List the middleware beneath an entry of django.middleware.IgnoredMiddleware.
- [ ] Write code to remove the middleware from the settings in [app]/**init**.py.

#### Q6. How do you turn off Django’s automatic HTML escaping for part of a web page?

- [ ] Place that section between paragraph tags containing the autoescape=off switch.
- [ ] Wrap that section between { percentage mark autoescape off percentage mark} and {percentage mark endautoescape percentage mark} tags.
- [ ] Wrap that section between {percentage mark autoescapeoff percentage mark} and {percentage mark endautoescapeoff percentage mark} tags.
- [x] You don't need to do anything—autoescaping is off by default.

#### Q7. Which step would NOT help you troubleshoot the error "django-admin: command not found"?

- [ ] Check that the bin folder inside your Django directory is on your system path.
- [ ] Make sure you have activated the virtual environment you have set up containing Django.
- [ ] Check that you have installed Django.
- [x] Make sure that you have created a Django project.

#### Q8. Every time a user is saved, their quiz_score needs to be recalculated. Where might be an ideal place to add this logic?

- [ ] template
- [x] model
- [ ] database
- [ ] view

#### Q9. What is the correct way to begin a class called "Rainbow" in Python?

- [ ] Rainbow {}
- [ ] export Rainbow:
- [x] class Rainbow:
- [ ] def Rainbow:

#### Q10. You have inherited a Django project and need to get it running locally. It comes with a requirements.txt file containing all its dependencies. Which command should you use?

- [ ] django-admin startproject requirements.txt
- [ ] python install -r requirements.txt
- [x] pip install -r requirements.txt
- [ ] pip install Django

#### Q11. Which best practice is NOT relevant to migrations?

- [x] To make sure that your migrations are up to date, you should run updatemigrations before running your tests.
- [ ] You should back up your production database before running a migration.
- [ ] Your migration code should be under source control.
- [ ] If a project has a lot of data, you should test against a staging copy before running the migration on production.

#### Q12. What will this URL pattern match? url(r'^\$', views.hello)

- [ ] a string beginning with the letter Ra string beginning with the letter R
- [x] an empty string at the server root
- [ ] a string containing ^ and $a string containing ^ and $
- [ ] an empty string anywhere in the URLan empty string anywhere in the URL

#### Q13. What is the typical order of an HTTP request/response cycle in Django?

- [x] URL > view > template
- [ ] form > model > view
- [ ] template > view > model
- [ ] URL > template > view > model

#### Q14. Django's class-based generic views provide which classes that implement common web development tasks?

- [ ] concrete
- [ ] thread-safe
- [x] abstract
- [ ] dynamic

#### Q15. Which skills do you need to maintain a set of Django templates?

- [ ] template syntax
- [x] HTML and template syntax
- [ ] Python, HTML, and template syntax
- [ ] Python and template syntax

#### Q16. How would you define the relationship between a star and a constellation in a Django model?

- [x] A

```python
class Star(models.Model):
name = models.CharField(max_length=100)
class Constellation(models.Model):
stars = models.ManyToManyField(Star)
```

- [ ] B

```python
class Star(models.Model):
constellation = models.ForeignKey(Constellation, on_delete=models.CASCADE)
class Constellation(models.Model):
stars = models.ForeignKey(Star, on_delete=models.CASCADE)
```

- [ ] C

```python
class Star(models.Model):
name = models.CharField(max_length=100)
class Constellation(models.Model):
stars = models.OneToManyField(Star)
```

- [ ] D

```python
class Star(models.Model):
constellation = models.ManyToManyField(Constellation)
class Constellation(models.Model):
name = models.CharField(max_length=100)
```

#### Q17. Which is NOT a valid step in configuring your Django 2.x instance to serve up static files such as images or CSS?

- [x] In your urls file, add a pattern that includes the name of your static directory.
- [ ] Create a directory named static inside your app directory.
- [ ] Create a directory named after the app under the static directory, and place static files inside.
- [ ] Use the template tag {percentage mark load static percentage mark}.

#### Q18. What is the correct way to make a variable available to all of your templates?

- [ ] Set a session variable.
- [ ] Use a global variable.
- [ ] Add a dictionary to the template context.
- [x] Use RequestContext.

#### Q19. Should you create a custom user model for new projects?

- [ ] No. Using a custom user model could break the admin interface and some third-party apps.
- [x] Yes. It is easier to make changes once it goes into production.
- [ ] No. Django's built-in models.User class has been tried and tested—no point in reinventing the wheel.
- [ ] Yes, as there is no other option.

#### Q20. You want to create a page that allows editing of two classes connected by a foreign key (e.g., a question and answer that reside in separate tables). What Django feature can you use?

- [x] actions
- [ ] admin
- [ ] mezcal
- [ ] inlines

#### Q21. Why are QuerySets considered "lazy"?

- [ ] The results of a QuerySet are not ordered.
- [x] QuerySets do not create any database activity until they are evaluated.
- [ ] QuerySets do not load objects into memory until they are needed.
- [ ] Using QuerySets, you cannot execute more complex queries.

#### Q22. You receive a `MultiValueDictKeyError` when trying to access a request parameter with the following code: request.GET['search_term']. Which solution will NOT help you in this scenario?

- [x] Switch to using POST instead of GET as the request method.
- [ ] Make sure the input field in your form is also named "search_term".
- [ ] Use MultiValueDict's GET method instead of hitting the dictionary directly like this: request.GET.get('search_term', '').
- [ ] Check if the search_term parameter is present in the request before attempting to access it.

#### Q23. Which function of Django's Form class will render a form's fields as a series of <p> tags?

- [ ] show_fields()
- [x] as_p()
- [ ] as_table()
- [ ] fields()

#### Q24. You have found a bug in Django and you want to submit a patch. Which is the correct procedure?

- [ ] Fork the Django repository GitHub.
- [ ] Submit a pull request.
- [x] all of these answers.
- [ ] Run Django's test suite.

#### Q25. Django supplies sensible default values for settings. In which Python module can you find these settings?

- [ ] `django.utils.default_settings.py`
- [ ] `django.utils.global_settings.py`
- [ ] `django.conf.default_settings.py`
- [x] `django.conf.global_settings.py`

#### Q26. Which variable name is best according to PEP 8 guidelines?

- [ ] numFingers
- [ ] number-of-Fingers
- [x] number_of_fingers
- [ ] finger_num

#### Q27. A project has accumulated 500 migrations. Which course of action would you pursue?

- [ ] Manually merge your migration files to reduce the number
- [ ] Don't worry about the number
- [ ] Try to minimize the number of migrations
- [x] Use squashmigrations to reduce the number

#### Q28. What does an F() object allow you when dealing with models?

- [x] perform db operations without fetching a model object
- [ ] define db transaction isolation levels
- [ ] use aggregate functions more easily
- [ ] build reusable QuerySets

#### Q29. Which is not a Django field type for holding integers?

- [ ] SmallIntegerField
- [x] NegativeIntegerField
- [ ] BigAutoField
- [ ] PositiveIntegerField

#### Q30. Which will show the currently installed version?

- [ ] print (django.version)
- [ ] import django django.getVersion()
- [x] import django django.get_version()
- [ ] python -c django --version

#### Q31. You should use the http method `___` to read data and `___` to update or create data

- [ ] READ; WRITE
- [x] GET; POST
- [ ] POST; GET
- [ ] GET; PATCH

#### Q32. When should you employ the POST method over GET for submitting data?

- [ ] when efficiency is important
- [ ] when you want the data to be cached
- [ ] when you want to use your browser to help with debugging
- [x] when the data in the form may be sensitive

#### Q33. When to use the Django sites framework?

- [x] if your single installation powers more than one site
- [ ] if you need to serve static as well as dynamic content
- [ ] if you want your app have a fully qualified domain name
- [ ] if you are expecting more than 10.000 users

#### Q34. Which infrastructure do you need:

`title=models.charfield(max_length=100, validators=[validate_spelling])`

- [ ] inizialized array called validators
- [x] a validators file containing a function called validate_spelling imported at the top of model
- [ ] a validators file containing a function called validate imported at the top of model
- [ ] spelling package imported at the top of model

#### Q35. What decorator is used to require that a view accepts only the get and head methods?

- [x] require_safe()
- [ ] require_put()
- [ ] require_post()
- [ ] require_get()

#### Q36. How would you define the relation between a book and an author - book has only one author.

```python
class Author (models.model):
book=models.foreignkey(Book,on_delete=models.cascade)
class Book(models.model):
name=models.charfield(max_length=100)
```

- [ ] A

```python
class Author (models.model):
name=models.charfield(max_length=100)
class Book(models.model):
author=models.foreignkey(Author,on_delete=models.cascade)
```

- [x] B

```python
class Author (models.model):
name=models.charfield(max_length=100)
class Book(models.model):
author=models.foreignkey(Author)
```

- [ ] C

```python
class Author (models.model):
name=models.charfield(max_length=100)
class Book(models.model):
author=models.foreignkey(Author,on_delete=models.cascade)
```

- [ ] D

```python
class Author (models.model):
name=models.charfield(max_length=100)
class Book(models.model):
author=Author.name
```

#### Q37. What is a callable that takes a value and raises an error if the value fails?

- [x] validator
- [ ] deodorizer
- [ ] mediator
- [ ] regular expression

#### Q38. To secure an API endpoint, making it accessible to registered users only, you can replace the rest_framework.permissions.allowAny value in the default_permissions section of your settings.py to

- [ ] rest_framework.permissions.IsAdminUser
- [x] rest_framework.permissions.IsAuthenticated
- [ ] rest_framework.permissions.IsAuthorized
- [ ] rest_framework.permissions.IsRegistered

#### Q39. Which command would you use to apply a migration?

- [ ] makemigration
- [ ] update_db
- [ ] applymigration
- [x] migrate

#### Q40. Which type of class allows QuerySets and model instances to be converted to native Python data types for use in APIs?

- [ ] objectwriters
- [x] serializers
- [ ] picklers
- [ ] viewsets

#### Q41. How should the code end?

```python
{ percentage if spark >= 50 percentage }
Lots of spark
{percentage elif spark == 42 percentage}
```

- [ ] { percentage else percentage}
- [x] {percentage endif percentage}
- [ ] Nothing needed
- [ ] {percentage end percentage}

#### Q42. Which code block will create a serializer?

```python
from rest_framework import serializers
from .models import Planet
```

- [x] A

```python
class PlanetSerializer(serializers.ModelSerializer):
class Meta:
model=Planet
fields=('name','position', 'mass', 'rings')
```

- [ ] B

```python
from rest_framework import serializers
from .models import Planet
class PlanetSerializer():
class Meta:
fields=('name','position', 'mass', 'rings')
model=Planet
```

- [ ] C

```python
from django.db import serializers
from .models import Planet
class PlanetSerializer(serializers.ModelSerializer):
fields=('name','position', 'mass', 'rings')
model=Sandwich
```

- [ ] D

```python
from django.db import serializers
from .models import Planet
class PlanetSerializer(serializers.ModelSerializer):
class Meta:
fields=('name')
model=Planet
```

#### Q43. Which class allows you to automatically create a Serializer class with fields and validators that correspond to your model's fields?

- [x] ModelSerializer
- [ ] Model
- [ ] DataSerializer
- [ ] ModelToSerializer

#### Q44. Which command to access the built-in admin tool for the first time?

- [ ] django-admin setup
- [ ] django-admin runserver
- [ ] python manage.py createuser
- [x] python manage.py createsuperuser

#### Q45. Virtual environments are for managing dependencies. Which granularity works best?

- [x] you should set up a new virtualenv for each Django project
- [ ] They should not be used
- [ ] Use the same venv for all your Django work
- [ ] Use a new venv for each Django app

#### Q46. What executes various Django commands such as running a webserver or creating an app?

- [ ] migrate.py
- [ ] wsgi.py
- [x] manage.py
- [ ] runserver

#### Q47. What do Django best practice suggest should be "fat"?

- [x] models
- [ ] controllers
- [ ] programmers
- [ ] clients

#### Q48. Which is not part of Django's design philosophy?

- [ ] Loose Coupling
- [ ] Less Code
- [ ] Fast Development
- [x] Implicit over explicit

#### Q49. What is the result of this template code?

{{"live long and prosper"|truncatewords:3}}

- [x] live long and ...
- [ ] live long and
- [ ] a compilation error
- [ ] liv

#### Q50. When does this code load data into memory?

```
1 sandwiches = Sandwich.objects.filter(is_vegan=True)
2 for sandwich in sandwiches:
3   print(sandwich.name + " - " + sandwich.spice_level)
```

- [ ] line 1
- [x] It depends on how many results return by query.
- [ ] It depends on cache.
- [ ] line 2

#### Q51. You are building a web application using a React front end and a Django back end. For what will you need to provision?\*\*

- [ ] an NGINX web server
- [ ] a NoSQL database
- [ ] a larger hard drive
- [x] CORS middleware

#### Q52. To expose an existing model via an API endpoint, what do you need to implement?\*\*

- [ ] an HTTP request
- [ ] a JSON object
- [ ] a query
- [x] a serializer

#### Q53. How would you stop Django from performing database table creation or deletion operations via migrations for a particular model?

- [ ] Run the `migrate` command with `--exclude=[model_name]`.
- [ ] Move the model definition from `models.py` into its own file.
- [x] Set `managed=False` inside the model.
- [ ] Don't run the `migrate` command.

#### Q54. what method can you use to check if form data has changed when using a form instance?

- [x] has_changed()
- [ ] its_changed()
- [ ] has_updated()
- [ ] None of This

#### Q55. What is WSGI?

- [ ] a server
- [x] an interface specifications
- [ ] a Python module
- [ ] a framework

Reference link:- https://wsgi.tutorial.codepoint.net/intro

#### Q56. Which generic view should be used for displaying the titles of all Django Reinhardt's songs?

- [ ] DetailView
- [ ] TittleView
- [ ] SongView
- [x] ListView

#### Q57. Which statement is most accurate, regarding using the default SQLite database on your local/development machine but Postgres in production

- [x] There's less chance of introducing bugs since SQLite already works out the box
- [ ] It's fine, you just need to keep both instances synchronized
- [ ] It's a bad idea and could lead to issues down the road
- [ ] It's the most efficient way to build a project

#### Q58. Why might you want to write a custom model Manager?

- [ ] to perform database queries
- [ ] to set up a database for testing
- [x] to modify the initial QuerySet that the Manager returns
- [ ] to filter the results that a database query returns

#### Q59. In Django, what are used to customize the data that is sent to the templates?

- [ ] models
- [x] views
- [ ] forms
- [ ] serializers

#### Q60. To complete the conditional, what should this block of code end with?

```shell
% if sparles >= 50 %
  Lots of sparkles!
% elif sparkles == 42 %
  The answer to life, the universe, and everything!
```

- [x] `% endif %`
- [ ] Nothing else is needed.
- [ ] `% end%`
- [ ] `% else %`

#### Q61. When should you employ the POST method over the GET method for submitting data from a form?

- [x] when the data in the form may be sensitive
- [ ] when you want the data to be cached
- [ ] when you want to use your browser to help with debugging
- [ ] when efficiency is important

#### Q62. What is a callable that takes a value and raises an error if the value fails to meet some criteria?

- [ ] mediator
- [x] validator
- [ ] regular expression
- [ ] deodorizer

#### Q63. You are uploading a file to Django from a form and you want to save the received file as a field on a model object. You can simply assign the file object from**\_to a field of type\_\_**in the model.

- [ ] request.META; FileField
- [ ] request.FILES; BLOBField
- [x] request.FILES; FileField
- [ ] request.META.Files; CLOBField

#### Q64. What python module might be used to store the current state of a Django model in a file?

- [x] pickle
- [ ] struct
- [ ] marshal
- [ ] serialize

#### Q65. To add a new app to an existing Django project, you must edit the **_ section of the _** file.

- [ ] ALLOWED_HOSTS; settings.py
- [ ] APPS; manage.py
- [x] INSTALLED_APPS; settings.py
- [ ] TEMPLATES; urls.py

#### Q66. Which is not a third-party package commonly used for authentication?

- [ ] django-guardian
- [ ] django-rest-auth
- [ ] authtoken
- [x] django-rest-framework-jwt

#### Q67. Which function in the django.urls package can help you avoid hardcoding URLS by generating a URL given the name of a view?

- [ ] get_script_prefix()
- [ ] redirect()
- [x] reverse()
- [ ] resolve()

#### Q68. Which is Fictional HTTP request method?

- [ ] POST
- [ ] PUT
- [x] PAUSE
- [ ] PATCH

#### Q69. Which helper function is not provided as a part of django.shortcuts package? ref-

- [x] render_to_request()
- [ ] render()
- [ ] redirect()
- [ ] get_object_or_404()

[Reference](https://docs.djangoproject.com/en/4.0/topics/http/shortcuts/#:~:text=The%20package%20django.,controlled%20coupling%20for%20convenience's%20sake)

#### Q70. Which is a nonstandard place to store templates?

- [x] at the root level of a project
- [ ] inside the application
- [ ] in the database
- [ ] on Github

#### Q71. If you left the 8080 off the command python manage.py runserver 8080 what port would Django use as default?

- [x] 8080
- [ ] 80
- [ ] 8000
- [ ] It would fail to start

#### Q72. Which statement about Django apps is false?

- [x] A Django app is the top-level container for a web application powered by Django.
- [ ] Django apps are small libraries designed to represent a single aspect of a project.
- [ ] Each Django app should do one thing, and one thing alone.
- [ ] A Django project is made up of many apps.

#### Q73. Which characters are illegal in template variable names?

- [ ] underscores.
- [ ] uppercase letters.
- [x] punctuation marks .
- [ ] numbers.

[Reference](https://docs.djangoproject.com/en/4.1/ref/templates/language/#:~:text=Variable%20names%20consist%20of%20any,may%20not%20be%20a%20number.)

#### Q74. Which is not a valid closing template tag?

- [ ] `% endautoescape %`
- [x] `% endifempty %`
- [ ] `% endcomment %`
- [ ] `% endfilter %`

#### Q75. When would you need to use the reverse_lazy utility function instead of reverse?

- [ ] when you want to provide a reverse URL as a default value for a parameter in a function's signature
- [x] all of the these answers
- [ ] when you want to provide a reverse URL as the url attribute of a class-based generic view
- [ ] when you want to provide a URL to a decorator, such as the login_url argument for the permission_required() decorator

#### Q76. What is the purpose of the \_\_init\_\_.py file?

- [ ] to extend the set of modules found in a package
- [ ] to allow compiled modules from different releases and different versions of Python to coexist
- [ ] to initialize project settings
- [x] to declare the directory contents as a Python module

[Reference](<https://docs.djangoproject.com/en/4.1/ref/urlresolvers/#:~:text=reverse_lazy()&text=It%20is%20useful%20for%20when,a%20generic%20class%2Dbased%20view>)

#### Q77. What python package can be used to edit numbers into more readable form like "1200000" to "1.2 million"?

- [ ] black
- [ ] puffer
- [ ] pitch
- [x] humanize

#### Q78. Where would you find the settings.py file?

- [x] \[projectname\]/settings.py
- [ ] \[projectname\]/\[projectname\]/settings.py
- [ ] \[PYTHON_ROOT\]/settings.py
- [ ] \[DJANGO_ROOT]/settings.py

#### Q79. What would you write to define the relationship between a book and an author--assuming a book has only one author-in a Django model?

- [x] A

```python
class Author (models.Model):
  name = models. CharField (max_length=100)
class Book(models .Model):
  author = models. ForeignKey (Author, on_delete=models. CASCADE)
```

- [ ] B

```python
class Author (models.Model):
  name = models. CharField(max length=100)
class Book(models .Model):
  author = models. ForeignKey (Author)
```

- [ ] C

```python
class Author (models .Model):
  name = models.CharField (max_length=100)
class Book (models .Author) :
  author = Author. name
```

- [ ] D

```python
class Author (models. Model):
  book = models. ForeignKey (Book, on_delete=models.CASCADE)
class Book(models.Model):
  name = models. CharField (max length=100)
```

#### Q80. What method can you use to check if form data has been changed when using a Form instance?

- [x] changed_data()
- [ ] has changed()
- [ ] has_updated()
- [ ] is_modified()

#### Q81. Which statement is most accurate, regarding using the default SQLite database on your local/development machine but Postgres in production?

- [ ] It's the most efficient way to build a project
- [ ] There's less chance of introducing bugs since SQLite already works out of the box
- [ ] It's a bad idea and could lead to issues down the road
- [x] It's fine, you just need to keep both instances synchronized

#### Q82. How does Django handle URL routing?

- [ ] by using classes
- [ ] by using functiones
- [x] by using regular expressions
- [ ] by using fixed path

#### Q83. What is the purpose of Django's middleware?

- [ ] To define the database schema
- [ ] To manage URL routing
- [x] To handle HTTP requests and responses globally
- [ ] To create user interfaces

[Reference](https://medium.com/scalereal/everything-you-need-to-know-about-middleware-in-django-2a3bd3853cd6)

#### Q84. Which of the following is true about Django's Object-Relational Mapping (ORM)?

- [ ] It's used to define URL routing in a Django application.
- [x] It allows you to query the database using Python code.
- [ ] It's used to define the structure of HTML templates.
- [ ] It's responsible for managing user authentication.

#### Q85. Which of the following is true about Django's "many-to-many" field in a model?

- [ ] It's used to define a one-to-one relationship between two models.
- [ ] It creates a foreign key relationship between two models.
- [x] It allows multiple objects to be associated with each other.
- [ ] It enforces unique constraints on a field.

#### Q86. Django's class-based generic views provide which classes that implement common web development tasks?

- [ ] concrete
- [ ] thread-safe
- [x] abstract
- [ ] dynamic

#### Q87. Which skills do you need to maintain a set of Django templates?

- [ ] template syntax
- [x] HTML and template syntax
- [ ] Python, HTML, and template syntax
- [ ] Python and template syntax

#### Q88. Which is a nonstandard place to store templates?

- [x] at the root level of a project
- [ ] inside the application
- [ ] in the database
- [ ] on Github

#### Q89. If you left the 8080 off the command python manage.py runserver 8080 what port would Django use as default?

- [x] 8080
- [ ] 80
- [ ] 8000
- [ ] It would fail to start

#### Q90. What is the purpose of Django's Object-Relational Mapping (ORM)?

- [ ] To define URL routing in a Django application.
- [ ] To handle HTTP requests and responses globally.
- [x] To map Python objects to database tables and simplify database operations.
- [ ] To create user interfaces.

#### Q91. In Django, what does the term "migration" refer to?

- [ ] A change in URL routing configuration.
- [x] The process of propagating changes you make to your models (adding a field, deleting a model, etc.) into your database schema.
- [ ] A way to define custom middleware.
- [ ] The process of creating HTML templates for your application.

#### Q92. What is the purpose of Django's "context" in the context of rendering templates?

- [x] To pass data from your views to your templates so that the data can be rendered dynamically.
- [ ] To define URL patterns for your application.
- [ ] To manage HTTP requests and responses.
- [ ] To create user interfaces.

#### Q93. What does the Django `QuerySet` class represent?

- [ ] A Python class used for defining URL routing in Django.
- [ ] A class for managing HTTP requests and responses.
- [x] A database query made by Django, represented in Python.
- [ ] A class for defining HTML templates.

#### Q94. In Django, what is the purpose of the "collectstatic" management command?

- [ ] To collect user data for analytics.
- [ ] To collect database records from multiple sources.
- [x] To collect all static files (CSS, JavaScript, images) from each of your applications into a single location.
- [ ] To collect logs for debugging purposes.

#### Q95. What is the Django Admin site used for?

- [ ] To manage user authentication.
- [ ] To define URL routing for Django applications.
- [x] To provide an automatically generated admin interface for your models.
- [ ] To write and run database queries.

#### Q96. What does Django's "middleware" refer to?

- [ ] A way to create user interfaces.
- [ ] A database query in Django.
- [x] A way to process HTTP requests and responses globally before they reach the view or after they leave the view.
- [ ] A way to configure URL routing in Django.

#### Q97. What is the primary purpose of Django's "migration files"?

- [x] To define and store changes to the database schema over time.
- [ ] To manage static files like CSS and JavaScript.
- [ ] To configure URL patterns.
- [ ] To create HTML templates.

#### Q98. Which authentication system does Django provide out of the box?

- [ ] OAuth 2.0
- [x] User authentication with built-in user models and views.
- [ ] JWT (JSON Web Tokens)
- [ ] SAML (Security Assertion Markup Language)

#### Q99. In Django, what does the "Model-View-Controller" (MVC) architectural pattern refer to?

- [ ] A pattern for defining URL routing.
- [ ] A pattern for creating HTML templates.
- [x] A pattern that divides the application into three interconnected components: Model, View, and Controller (Django often refers to it as MTV, Model-View-Template).
- [ ] A pattern for user authentication.

#### Q100. What is the purpose of Django's "templates"?

- [ ] To define database schema and model relationships.
- [x] To define the structure and layout of HTML pages to be served to the user.
- [ ] To configure URL patterns for your application.
- [ ] To store and serve static files like images and JavaScript.
