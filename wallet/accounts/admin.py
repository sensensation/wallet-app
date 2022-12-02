from django.contrib import admin

# Register your models here.
from .models import CustomUser 
admin.site.register(CustomUser)

#Регистрация приложения явно в django admin на сайте отладки



