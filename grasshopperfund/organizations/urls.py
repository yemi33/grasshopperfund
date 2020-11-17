from django.urls import path, include
from . import views

urlpatterns = [
    path('browse/', views.browse_organizations, name='browse-organizations'),
    path('create/', views.create_organization, name='create-organization'),
    path('view/<str:organization_name>', views.view_organization, name='view-organization'),
    path('update/<str:organization_name>', views.update_organization, name='update-organization'),
    path('delete/<str:organization_name>', views.delete_organization, name='delete-organization'),
]
