from django.contrib import admin
from django.urls import include, path
from .views import home_page
from .views import upload_file
from myapp import views
from . import views

urlpatterns = [
    path('',views.home_page),
    path('upload', upload_file, name='upload')
]