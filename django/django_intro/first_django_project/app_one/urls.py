from django.urls import path
from . import views

urlpatterns = [
path('',views.root),
path('blogs/',views.index),
path('blogs/new/',views.new), #the redirect path didn't accept the / at the start of the route but it should be at the end
path('blogs/create/',views.create),
path('blogs/<int:number>',views.show),
path('blogs/<number>/edit',views.edit),
path('blogs/<number>/delete',views.destroy),
path('blogs/json',views.json),
]