from django.shortcuts import render

from .serializer import AccountSerializer
from rest_framework import viewsets
from accunt_api.models import Account


class Account_viewset(viewsets.ModelViewSet):
  serializer_class = AccountSerializer
  queryset =Account.objects.all()