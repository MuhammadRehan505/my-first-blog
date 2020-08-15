from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),  #we're now assigning a view called post_list to the root URL.This URL pattern will match an empty string and the Django URL resolver will ignore the domain name. name='post_list', is the name of the URL that will be used to identify the view.
]