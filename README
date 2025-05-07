### starting a server instead of django-admin :

python -m django startproject myproject

### running the development server :

py manage.py runserver

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

## admin

python manage.py createsuperuse
admin, admin@example.com, password

## views

a type of web page that serves a specific function & has a specific template (this is so the items are not hard coded)

the render page can use a loader, or use the render through shortcut for templates

### generic views

built in common views -> don't need to hard code them with the python
a generic view needs to know what model it will be using

### templates

"dot-lookup syntax to access variable attributes"
{%  python code %} + regular html code
