from django.urls import path, include
from . import views

urlpatterns = [
    path('<str:organization_name>/create/', views.create_campaign, name='create-campaign'),
    path('update/<str:pk>/', views.update_campaign, name='update-campaign'),
    path('delete/<str:pk>/', views.delete_campaign, name='delete-campaign'),
    path('view/<str:username>/<str:campaign_title>', views.view_campaign, name='view-campaign'),
    path('make_donation/<str:pk>/', views.make_donation, name='make-donation'),
    path('search/', views.search_campaign, name='search-campaign'),
    path('browse/', views.browse_campaigns, name='browse-campaigns')
]
