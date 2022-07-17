from django.urls import path
from . import views


urlpatterns = [
    path('/accounts/login/', views.home_page_view, name='home'),
    path('about/', views.about_page_view, name='about'),
    path('contact/', views.contact_page_view, name='contact'),
    path('design/', views.DesignListView.as_view(), name='design'),
    path('<int:pk>/', views.detail_design_page_view, name='detail_design'),
    path('create/', views.create_design_page_view, name='create_design'),
    path('<int:pk>/update/', views.design_update_view, name='design_update'),
    path('<int:pk>/delete/', views.design_delete_view, name='design_delete'),
]

