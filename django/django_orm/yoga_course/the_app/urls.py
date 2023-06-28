from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('register',views.register),
    path('login',views.login),
    path('logout',views.logout),
    path('classes',views.classes),
    path('classes/new',views.new),
    path('cancel',views.cancel),
    path('process',views.process),
    path('classes/<int:id>/edit',views.edit),
    path('process_edit',views.process_edit),
    path('destroy',views.destroy),
    path('classes/<int:id>',views.display),
]