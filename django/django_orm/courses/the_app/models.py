from django.db import models

class CourseManager(models.Manager):
    def validator(self,postData):
        errors = {}
        if len(postData['name']) < 5:
            errors['name'] = 'Name should be more than 5 characters'
        if len(postData['desc']) < 15:
            errors['desc'] = 'Description should be more than 15 characters'
        return errors

class Course(models.Model):
    name = models.CharField(max_length=45)
    desc = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()
