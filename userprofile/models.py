from django.db import models

# Create your models here.
class ProfileModel(models.Model):
    name = models.CharField(max_length=100, null=False, blank= False) 
    email = models.EmailField(max_length = 254, unique=True, null=False, blank=False)
    bio = models.TextField(null=False, blank=False)
    picture = models.ImageField(upload_to='static/profile_images/')
