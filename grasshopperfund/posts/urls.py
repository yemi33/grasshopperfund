from django.urls import path, include
from . import views


urlpatterns = [
    path('view/<str:organization_name>/<str:pk>', views.view_post, name='view-post'),
    path('create/<str:organization_name>', views.CreatePostView.as_view(), name='create-post'),
    path('update/<str:organization_name>/<str:pk>', views.UpdatePostView.as_view(), name='update-post'),

]
