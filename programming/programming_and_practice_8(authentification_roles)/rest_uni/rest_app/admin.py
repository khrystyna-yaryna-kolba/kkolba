from django.contrib import admin
from .models import Containers, UserData, ContainerOrder

# Register your models here.
admin.site.register(Containers)
admin.site.register(UserData)
admin.site.register(ContainerOrder)
