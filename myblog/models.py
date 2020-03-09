from django.db import models

class Blog(models.Model):
  title = models.CharField(max_length=100)
  body = models.CharField(max_length=100)
  time =models.DateTimeField(auto_now_add=True)
  
  
