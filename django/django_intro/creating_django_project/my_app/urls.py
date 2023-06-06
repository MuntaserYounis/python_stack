from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index), #added name="index"
]
