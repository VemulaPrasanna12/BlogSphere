from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('admin-login/', views.admin_login, name='admin_login'),
    path('admin-logout/', views.admin_logout, name='admin_logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/new/', views.post_new, name='post_new'),
    path('dashboard/edit/<int:pk>/', views.post_edit, name='post_edit'),
    path('dashboard/delete/<int:pk>/', views.post_delete, name='post_delete'),
]
