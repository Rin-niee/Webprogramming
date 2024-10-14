from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("name/", views.name, name= "name"),
    path("group/", views.group, name= "group"),
    path("age/", views.age, name= "age"),
    path("common/", views.common, name= "common"),
]
