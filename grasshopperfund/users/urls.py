from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_page, name='startsmart-home'),
    path('faq/', views.faq, name='faq'),
    path('register/', views.register_page, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),

    path('update_profile/', views.update_profile, name='update-profile'),
    path('delete_profile/', views.delete_profile, name='delete-profile'),
    path('profile/<str:pk>/', views.view_profile, name='profile'),


]
