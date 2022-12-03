from rest_framework import serializers

from .models import CustomUser



class UserListSerializer(serializers.ModelSerializer):
   class Meta:
      model = CustomUser
      fields = ('__all__')

class UserRegistrationSerializer(serializers.ModelSerializer):
   class Meta:
      model = CustomUser
      fields = ('__all__')

   def create(self, validated_data):
        user = CustomUser.objects.create(
            email = validated_data['email'],
            password = validated_data['password'],
            date_of_birth = validated_data['date_of_birth'],
        )

        user.set_password(validated_data['password'])

        user.save()

        return user