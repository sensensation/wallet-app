from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import CustomUser

# class UserModel:
#    def __init__(self, title, content) -> None:
#       self.title = title
#       self.content = content

class UserSerializer(serializers.ModelSerializer):

   class Meta:
      model = CustomUser
      fields = ('__all__')