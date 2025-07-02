from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('education/', views.education, name='education'),
    path('tools/', views.tools, name='tools'),
    path('whatisforex/', views.whatisforex, name='whatisforex'),
    path('currency/', views.currency, name='currency'),
]
