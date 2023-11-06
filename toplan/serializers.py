from rest_framework import serializers
from .models import Toplan


class ToplanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Toplan
        fields = '__all__'