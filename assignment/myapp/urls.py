from django.contrib import admin
from django.urls import include, path
from .views import home_page
# from .views import upload_file
from myapp import views
from . import views
# from .views import download_file

urlpatterns = [
    path('',views.home_page),
    path('upload', views.upload_file),
    # path('<slug:short_link>', views.generate_short_link),
    # path('download/<file_id>/', views.download_file, name='download_file')
]