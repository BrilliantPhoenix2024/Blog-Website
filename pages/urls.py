from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('about/', views.about_page_view, name='about'),
    path('contact/', views.contact_page_view, name='contact'),
    path('design/', views.design_page_view, name='design'),
    path('services/', views.services_page_view, name='services'),
]

