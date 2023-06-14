from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('authors',views.authors),
    path('add_book',views.add_book),
    path('books/<id>',views.view),
]