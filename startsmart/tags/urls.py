from django.urls import path, include
from . import views

urlpatterns = [
path('filter/<str:tagname>', views.filter_campaigns_from_tags, name='filter-campaigns-from-tags')]