from django.urls import path
from .views import Blog_apiview

urlpatterns = [
    path('',Blog_apiview.as_view())
]
