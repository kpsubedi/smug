from django.db import models

# Create your models here.

class NewCase(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    start_date = models.DateTimeField('date started')

#class ListCase(models.Model):
#    def list():
        
