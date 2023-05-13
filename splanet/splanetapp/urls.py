from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('splogin/', views.login, name='login'),
    path('spadmin/', views.spadmin, name='spadmin')
]