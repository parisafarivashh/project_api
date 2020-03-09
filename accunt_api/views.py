from django.shortcuts import render

from .serializer import AccountSerializer
from rest_framework import viewsets
from accunt_api.models import Account
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination 
from rest_framework.filters import SearchFilter,OrderingFilter

class Account_viewset(viewsets.ModelViewSet):
  serializer_class = AccountSerializer
  queryset =Account.objects.all()









    