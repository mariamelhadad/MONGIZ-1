from rest_framework import serializers
from .models import *


class msg_serializer(serializers.ModelSerializer):
    class meta:
        model = message
        fields = '__all__'
