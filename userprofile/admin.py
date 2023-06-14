from django.contrib import admin
from .models import ProfileModel

# Register your models here.
@admin.register(ProfileModel)
class ProfileAdmin(admin.ModelAdmin):
    pass