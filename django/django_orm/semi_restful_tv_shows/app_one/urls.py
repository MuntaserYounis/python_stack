from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shows',views.all_shows,name='shows'),
    path('shows/new',views.new, name='new'),
    path('shows/create',views.create),
    path('shows/<int:id>',views.shows),
    path('shows/<int:id>/edit',views.edit,name='the_edit'),
    path('shows/<int:id>/update',views.update, name='update'),
    path('shows/<int:id>/destroy',views.destroy,name='destroy'),]