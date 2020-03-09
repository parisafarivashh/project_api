from django.shortcuts import render
from .serializer import blogserializer
from .models import Blog
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter,OrderingFilter

class Blog_apiview(ListAPIView):
  serializer_class =blogserializer
  queryset = Blog.objects.all()
  filter_backends = (SearchFilter,OrderingFilter)
  search_fields =('title','body')
