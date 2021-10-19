from django.db import models

"""
Problem 1

Create a Human model. It has name, surname, year_of_birth, and gender (can be Male or Female). 
Create a migration and syncronize with the db.
"""
class Human(models.Model):
    genchoices = (
        ('m','male'),
        ('f','female')
    )
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=50)
    year_of_birth = models.IntegerField()
    gender = models.CharField(max_length=1,choices=genchoices)

"""
Problem 2

In the terminal, set DJANGO_SETTINGS_MODULE to your project settings. Open the shell. 
and create some Human objects.
"""


"""
Problem 3

We want to see the Human model in the admin panel. Create a HumanAdmin class in admin.py
We want to display human's name, surname and age (*note, Human class has no field age) on the admin panel.
"""

