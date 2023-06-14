from rest_framework import serializers
from .models import ProfileModel

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ('__all__')
        extra_kwargs = {
         'name': {'write_only': True},
         'bio': {'write_only': True},
         'picture':{'write_only': True}
     }