from .serializers import UserRegistrationSerializer, UserListSerializer
from rest_framework import viewsets, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


from .models import CustomUser
# Create your views here.

@api_view(['POST'])
def register(request):
   serializer = UserRegistrationSerializer(data=request.data)
   if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
   else:
      return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
   serializer = UserLoginSerializer(data=request.data)

class UserAPIList(generics.ListCreateAPIView):
   """
   Use GET http://127.0.0.1:8000/account/api/userlist/ to see all users
   """
   queryset = CustomUser.objects.all()
   serializer_class = UserListSerializer
   # permission_classes = (IsAuthenticatedOrReadOnly, )

