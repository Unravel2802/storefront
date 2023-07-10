from django.urls import path
from . import views

# URL configuration or URLConf
urlpatterns = [
    path('hello/', views.say_hello)
]