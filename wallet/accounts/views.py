# from django.shortcuts import redirect, render
# # from .forms import UserRegistrationForm
# from django.contrib import messages
from .serializers import UserSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


from .models import CustomUser
# Create your views here.

@api_view(['POST'])
def register(request):
   serializer = UserSerializer(data=request.data)
   if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
   else:
      return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)


   #  form = UserRegistrationForm(request.POST or None)
   #  if request.method == 'POST':
   #      if form.is_valid():
   #          new_user = form.save()
   #          messages.success(request, 'Account succesfully created!')
   #          return redirect('accounts:register')

   #  return render(request, "register.html", context = {"form":form})
      