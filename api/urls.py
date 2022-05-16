from django.urls import path
from .views import BlogApiListView


urlpatterns = [
    path('bloglist/', BlogApiListView.as_view(), name = 'bloglist'),
]