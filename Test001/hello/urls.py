from django.urls import path
from .import views
urlpatterns = [
    path("",views.index, name="index"),
    path("siyam",views.siyam, name="siyam"),
    path("another",views.another, name="antoher"),
    path("<str:name>",views.greet,name="greet")
]
