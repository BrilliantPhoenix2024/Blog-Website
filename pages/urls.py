from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('about/', views.about_page_view, name='about'),
    path('contact/', views.contact_page_view, name='contact'),
    path('design/', views.DesignListView.as_view(), name='design'),
    path('<int:pk>/', views.DesignDetailView.as_view(), name='detail_design'),
    path('create/', views.DesignCreateView.as_view(), name='create_design'),
    path('<int:pk>/update/', views.DesignUpdateView.as_view(), name='design_update'),
    path('<int:pk>/delete/', views.DesignDeleteView.as_view(), name='design_delete'),
]

