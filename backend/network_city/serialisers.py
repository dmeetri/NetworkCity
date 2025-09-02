from rest_framework import serializers
from users.models import *

class UserstSerialiser(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        models = Users
        fields = '__all__'