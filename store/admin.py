from django.contrib import admin
from . import models


# Register your models here.
# Every django app has admin.py file to customize the models registering

admin.site.register(models.Collection)
admin.site.register(models.Product)