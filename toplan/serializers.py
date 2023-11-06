from .models import Toplan
from django.contrib.auth.models import User, Group
from rest_framework import serializers


class ToplanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Toplan
        fields = ['id','subject', 'details', 'date', 'time', 'is_completed', 'created_at', 'updated_at']