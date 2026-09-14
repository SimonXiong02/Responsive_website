from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('reference/', views.reference, name='reference'),
    path('gallery/', views.gallery, name='gallery'),
    path('faq/', views.faq, name='faq'),
    path('contact/', views.contact, name='contact'),
]
