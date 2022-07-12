from django.urls import path
from . import views


urlpatterns = [
    path('/accounts/login/', views.home_page_view, name='home'),
    path('about/', views.about_page_view, name='about'),
    path('contact/', views.contact_page_view, name='contact'),
    path('design/', views.design_page_view, name='design'),
    path('<int:pk>/', views.detail_design_page_view, name='detail_design'),
]

