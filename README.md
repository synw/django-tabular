# Django Tabular

Display tabular data in Django. This module was designed to integrate tabular data in 
[django-chartflo](https://github.com/synw/django-chartflo) dashboards.

## Install

Clone the repository and add `"tabular"` to installed apps

## Usage

This will save an Table instance in the database and generate a chunk of html to be displayed. In a Chartflo generator 
(or in any function):

   ```python
   from django.contrib.auth.model import User
   from tabular.models import Table
   from tabular.factory import table
   
   def run(events=None):
      slug = "all_users"
      q = User.objects.all()
      instance, _ = Table.objects.get_or_create(slug=slug)
      instance.name = "All users"
      instance.generator = "auth"
      instance.modelnames = "User"
      fields = ["date_created", "username", "first_name", "last_name", "email"]
      instance.html = table.generate(slug, q, fields)
      # save the instance in db
      instance.save()
      # generate the html
      instance.generate()
   ``` 

This will generate a `templates/tabular/tables/all_users.html` file

In a template:

   ```django
   {% include "tabular/tables/all_users.html" %}
   {% include "tabular/script.html" %}
   ```
   
## Credits

[Tablefilter.js](https://github.com/koalyptus/TableFilter)
   ```