# random django notes as I'm going
## `python manage.py` and `django-admin`
- They can be used to do the same things
- `manage.py` doesn't exist in a project until `django-admin startproject name` is ran and it bootstraps a project 
- after that though, `manage.py` is recommended for most cases because it takes `settings.py` into account ([docs src](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-and-manage-py))

### `python manage.py runserver <port>`
Run the development server, by default it supports auto-reloading on changes