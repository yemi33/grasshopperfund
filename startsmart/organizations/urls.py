from django.urls import path, include
from . import views

urlpatterns = [
    path('create/', views.create_organization, name='create-organization'),
]
