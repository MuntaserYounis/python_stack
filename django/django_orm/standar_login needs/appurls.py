from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('register',views.register),
    path('login',views.login),
    path('logout',views.logout),
    path('wall',views.wall, name='wall'),
    path('add_message',views.add_message),
    path('comment/<int:id>',views.add_comment),
]