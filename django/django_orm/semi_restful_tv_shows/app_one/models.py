from django.db import models
import datetime
class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateTimeField(blank = True,null=True, default=datetime.datetime.now)
    desc = models.TextField(null=True)
    last_uploaded = models.DateTimeField(auto_now_add=True)
# Create your models here.
