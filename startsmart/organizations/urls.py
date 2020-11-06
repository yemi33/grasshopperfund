from django.urls import path, include
from . import views

urlpatterns = [
    path('create/', views.create_organization, name='create-organization'),
    path('view/<str:organization_name>', views.view_organization, name='view-organization'),
]
