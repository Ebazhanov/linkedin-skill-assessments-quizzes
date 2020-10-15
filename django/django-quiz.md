Q1. To cache your entire site for an application in Django, you add all except which of these settings?

	- django.middleware.common.CommonMiddleware
	- django.middleware.cache.UpdateCacheMiddleware
	- django.middleware.cache.FetchFromCacheMiddleware
	👍 - django.middleware.cache.AcceleratedCacheMiddleware



Q2. In which programming language is Django written?

	- C++
	- Java
	👍 - Python
	- Ruby



Q3. To automatically provide a value for a field, or to do validation that requires access to more than a single field, you should override the_____ method in the_____ class.

	- validate(); Model
	- group(); Model
	- validate(); Form
	👍 - clean(); Field



Q4. A client wants their site to be able to load "Rick & Morty" episodes by number or by title—e.g., shows/3/3 or shows/picklerick. Which URL pattern do you recommend?

	- url(r'shows/<int:season>/<int:episode>/', views.episode_number)
	👍 - path('shows/<int:season>/<int:episode>/', views.episode_number),
	- path('shows/<int:season>/<int:episode>', views.episode_number), 
	- url(r'^show/(?P<season>[0-9]+)/(?P<episode>[0-9]+)/$', views.episode_number), 



Q5. How do you determine at startup time if a piece of middleware should be used?

	👍 - Raise MiddlewareNotUsed in the __init__ function of your middleware.
	- Implement the not_used method in your middleware class.
	- List the middleware beneath an entry of django.middleware.IgnoredMiddleware.
	- Write code to remove the middleware from the settings in [app]/__init__.py.

Q6. How do you turn off Django’s automatic HTML escaping for part of a web page?

	- Place that section between paragraph tags containing the autoescape=off switch.
	- Wrap that section between { percentage mark autoescape off percentage mark} and {percentage mark endautoescape percentage mark} tags.
	- Wrap that section between {percentage mark autoescapeoff percentage mark} and {percentage mark endautoescapeoff percentage mark} tags.
	👍 - You don't need to do anything—autoescaping is off by default.

Q7. Which step would NOT help you troubleshoot the error "django-admin: command not found"?

	- Check that the bin folder inside your Django directory is on your system path.
	- Make sure you have activated the virtual environment you have set up containing Django.
	- Check that you have installed Django.
	👍 - Make sure that you have created a Django project.



Q8. Every time a user is saved, their quiz_score needs to be recalculated. Where might be an ideal place to add this logic?

	- template
	👍 - model
	- database
	- view



Q9. What is the correct way to begin a class called "Rainbow" in Python?

	- Rainbow {}
	- export Rainbow:
	👍 - class Rainbow:
	- def Rainbow:



Q10. You have inherited a Django project and need to get it running locally. It comes with a requirements.txt file containing all its dependencies. Which command should you use?

	- django-admin startproject requirements.txt
	- python install -r requirements.txt
	👍 - pip install -r requirements.txt
	- pip install Django


Q11. Which best practice is NOT relevant to migrations?

	👍 - To make sure that your migrations are up to date, you should run updatemigrations before running your tests.
	- You should back up your production database before running a migration.
	- Your migration code should be under source control.
	- If a project has a lot of data, you should test against a staging copy before running the migration on production.



Q12. What will this URL pattern match? url(r'^$', views.hello)

	- a string beginning with the letter Ra string beginning with the letter R
	👍 - an empty string at the server root
	- a string containing ^ and $a string containing ^ and $
	- an empty string anywhere in the URLan empty string anywhere in the URL



Q13. What is the typical order of an HTTP request/response cycle in Django?

	👍 - URL > view > template
	- form > model > view
	- template > view > model
	- URL > template > view > model


Q14. Django's class-based generic views provide which classes that implement common web development tasks?

	- concrete
	- thread-safe
	👍 - abstract
	- dynamic



Q15. Which skills do you need to maintain a set of Django templates?

	- template syntax
	👍 - HTML and template syntax
	- Python, HTML, and template syntax
	- Python and template syntax



Q17. How would you define the relationship between a star and a constellation in a Django model?

	👍-	class Star(models.Model): 
			name = models.CharField(max_length=100) 
		class Constellation(models.Model): 
			stars = models.ManyToManyField(Star)

	- 	class Star(models.Model): 
			constellation = models.ForeignKey(Constellation, on_delete=models.CASCADE) 
		class Constellation(models.Model): 
			stars = models.ForeignKey(Star, on_delete=models.CASCADE)

	- 	class Star(models.Model): 
			name = models.CharField(max_length=100) 
		class Constellation(models.Model): 
			stars = models.OneToManyField(Star)

	- 	class Star(models.Model): 
			constellation = models.ManyToManyField(Constellation) 
		class Constellation(models.Model): 
			name = models.CharField(max_length=100)



Q18. Which is NOT a valid step in configuring your Django 2.x instance to serve up static files such as images or CSS?

	👍 - In your urls file, add a pattern that includes the name of your static directory.
	- Create a directory named static inside your app directory.
	- Create a directory named after the app under the static directory, and place static files inside.
	- Use the template tag {percentage mark load static percentage mark}.



Q19. What is the correct way to make a variable available to all of your templates?

	- Set a session variable.
	- Use a global variable.
	- Add a dictionary to the template context.
	👍 - Use RequestContext.



Q20. Should you create a custom user model for new projects?

	- No. Using a custom user model could break the admin interface and some third-party apps.
	- Yes. It is easier to make changes once it goes into production.
	👍 - No. Django's built-in models.User class has been tried and tested—no point in reinventing the wheel.
	- Yes, as there is no other option.



Q21. You want to create a page that allows editing of two classes connected by a foreign key (e.g., a question and answer that reside in separate tables). What Django feature can you use?

	👍 - actions
	- admin
	- mezcal
	- inlines



Q22. Why are QuerySets considered "lazy"?

	- The results of a QuerySet are not ordered.
	👍 - QuerySets do not create any database activity until they are evaluated.
	- QuerySets do not load objects into memory until they are needed.
	- Using QuerySets, you cannot execute more complex queries.



Q23. You receive a `MultiValueDictKeyError` when trying to access a request parameter with the following code: request.GET['search_term']. Which solution will NOT help you in this scenario?

	👍 - Switch to using POST instead of GET as the request method.
	- Make sure the input field in your form is also named "search_term".
	- Use MultiValueDict's GET method instead of hitting the dictionary directly like this: request.GET.get('search_term', '').
	- Check if the search_term parameter is present in the request before attempting to access it.



Q24. Which function of Django's Form class will render a form's fields as a series of <p> tags?

	- show_fields()
	👍 - as_p()
	- as_table()
	- fields()



Q25. You have found a bug in Django and you want to submit a patch. Which is the correct procedure?

	- Fork the Django repository GitHub.
	- Submit a pull request.
	👍 - all of these answers.
	- Run Django's test suite.

Q26. Django supplies sensible default values for settings. In which Python module can you find these settings?
- django.utils.default_settings.py
- django.utils.global_settings.py
- django.conf.default_settings.py
👍 - django.conf.global_settings.py

Q27. Which variable name is best according to PEP 8 guidelines?
- numFingers
- number-of-Fingers
👍 - number_of_fingers
- finger_num

Q28. A project has accumulated 500 migrations. Which course of action would you pursue?
- Manually merge your migration files to reduce the number
- Don't worry about the number
- Try to minimize the number of migrations
👍 - Use squashmigrations to reduce the number

Q29. What does an F() object allow you when dealing with models?
👍 - perform db operations without fetching a model object
- define db transaction isolation levels
- use aggregate functions more easily
- build reusable QuerySets

Q30. Which is not a django filed type for integers?
- SmallIntegerField
👍 - NegativeIntegerField
- BigAutoField
- PositiveIntegerField

Q31. Which will show the currently installed version?
- print (django.version)
- import django
django.getVersion()
👍 - import django
django.get_version()
- python -c django --version
