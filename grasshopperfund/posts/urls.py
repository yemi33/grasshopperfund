from django.urls import path, include
from . import views


urlpatterns = [
    path('view/<str:organization_name>/<str:post_id>', views.view_post, name='view-post'),
    path('create/<str:organization_name>', views.CreatePostView.as_view(), name='create-post'),

]
