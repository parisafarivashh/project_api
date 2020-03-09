from rest_framework import serializers
from .models import Blog

class blogserializer(serializers.ModelSerializer):

  class Meta:
    model =Blog
    fields =('title','body','time')

  def save(self):
    user = Blog(
      title = self.validated_data['title'],
      body = self.validated_data['body'],
      
    )
    return user
