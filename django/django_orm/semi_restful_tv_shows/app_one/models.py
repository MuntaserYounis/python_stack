from django.db import models
import datetime

class ShowManager(models.Manager):
    def validator(self,postData):
        errors = {}
        if len(postData['title'])< 2:
            errors['title'] = "Title should be more than 2 characters"
        if len(postData['network']) < 3:
            errors['network'] = "Network should be at least 3 characters"
        if len(postData['desc']) < 10:
            errors['desc'] = 'Description should be more than 10 characters'
        return errors
    

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateTimeField(blank = True,null=True, default=datetime.datetime.now)
    desc = models.TextField(null=True)
    last_uploaded = models.DateTimeField(auto_now_add=True)
    objects = ShowManager()
# Create your models here.
