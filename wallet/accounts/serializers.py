from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import CustomUser
User = get_user_model()


class UserListSerializer(serializers.ModelSerializer):
   class Meta:
      model = CustomUser
      fields = ('__all__')

class UserRegistrationSerializer(serializers.ModelSerializer):
   class Meta:
      model = CustomUser
      fields = ('__all__')

   def create(self, validated_data):
        user = User.objects.create(
            email = validated_data['email'],
            password = validated_data['password'],
            date_of_birth = validated_data['date_of_birth'],
        )

        user.set_password(validated_data['password'])

        user.save()

        return user

class UserLoginSerializer(serializers.ModelSerializer):
   pass