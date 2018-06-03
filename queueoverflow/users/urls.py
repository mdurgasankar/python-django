from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [

    path('index/',views.IndexView.as_view()),
    path('home/',views.HomeView.as_view())

]
