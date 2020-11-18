from django.urls import path, include
from . import views


urlpatterns = [
    path('view/<str:organization_name>/<str:post_id>', views.view_post, name='view-post'),
]
