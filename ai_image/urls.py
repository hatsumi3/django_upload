from django.contrib import admin
from django.urls import include, path

from . import views

app_name='ai_image'

urlpatterns = [
    path('', views.index, name="post"),
]