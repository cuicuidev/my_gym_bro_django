from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Exercise)
admin.site.register(models.SetEntry)
admin.site.register(models.Workout)
admin.site.register(models.Session)