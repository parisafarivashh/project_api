from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import Account_viewset

router = DefaultRouter()
router.register('register',Account_viewset)

urlpatterns =[
  path('',include(router.urls)),
  
]
