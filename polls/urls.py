from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mywork/', views.mywork, name='mywork'),
    path('contact/', views.contact, name='contact'),
]
