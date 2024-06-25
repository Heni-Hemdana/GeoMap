from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # name ma aando hata indication juste lia 
    ]