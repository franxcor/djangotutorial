# Important commands

### starting a server instead of django-admin :

python -m django startproject myproject

### running the development server :

py manage.py runserver

### running tests:

py manage.py test (appname)

# Important information

## migrations are how Django stores changes to your models

python manage.py makemigrations polls

python manage.py sqlmigrate polls 0001 -> sql migrations
--> then run migrate again to create the model tables in database (synchronizes the unapplied migrations to the database)

## in python shell (python manage.py shell) (exit() to exit)

make new objects/classes liek varName=Classname(classvar1 = value, classvar2 = value2)
must save after each creation & edit
to view -> Classname.objects.all()
to filter -> Classname.objects.filter(classvar=value);
search by value -> Classname.objects.filter(classvar\_\_startswith="What")

## Automated Testing

This is important for efficiecy when apps get more complex and manual testing may not be reliable/practical

Writing a test will have what you are testing + the expected results (using assertIs)

test name functions must begin with "test"

good practices: descriptive naming, separate testclasses for each model/view

Selenium -> tests whether the html renders in a browser
continuous integration (automated testing)
django testing link : https://docs.djangoproject.com/en/5.2/topics/testing/

### Client Testing

client simulates a user interacting with code
setup the test environment (template renderer) by importing it and running

## admin

python manage.py createsuperuse
admin, admin@example.com, password

## views

a type of web page that serves a specific function & has a specific template (this is so the items are not hard coded)

the render page can use a loader, or use the render through shortcut for templates

### generic views

built in common views -> don't need to hard code them with the python
a generic view needs to know what model it will be using
then the template name is used to show what format it should display it in

## templates

"dot-lookup syntax to access variable attributes"
{%  python code %} + regular html code (models will fill them in)

## static

built in django like templates
