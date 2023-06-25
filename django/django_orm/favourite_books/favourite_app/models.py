from django.db import models
import bcrypt
import re
import datetime

class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['first_name'])< 2 or not postData['first_name'].isalpha():
            errors['first_name'] = 'first name should be more than 2 characters'
        if len(postData['last_name'])< 2 or not postData['last_name'].isalpha():
            errors['last_name'] = 'first name should be more than 2 characters'
        if len(postData['password']) < 8:
            errors['password'] = 'password should be at least 8 characters'
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address!"
        if postData['password'] != postData['confirm']:
            errors['password'] = 'Passwords are not matching '
        return errors
    def login_validator(self,postData):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        errors2={}
        email2= postData['email2']
        password2 = postData['password2']
        usr = User.objects.filter(email=email2)
        if len(email2)<1:
            errors2['email2'] = 'Email cannot be empty'
        elif not EMAIL_REGEX.match(email2):
            errors2['email2'] = 'Invalid email'
        elif not bcrypt.checkpw(password2.encode(), usr[0].password.encode()):
            errors2['password'] = 'incorrect password'
        return errors2

class BookManager(models.Manager):
    def book_validator(self,postData):
        errors = {}
        if len(postData['title']) <1:
            errors['title'] = 'Title cannot be empty'
        if len(postData['desc'])<5:
            errors['desc'] = 'Description must at least have 5 characters'
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    uploaded_by = models.ForeignKey(User,related_name='books_uploaded',on_delete=models.CASCADE)
    users_who_like = models.ManyToManyField(User,related_name='liked_books')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()