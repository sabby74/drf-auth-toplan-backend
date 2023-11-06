from rest_framework import serializers
from .models import Toplan


class ToplanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Toplan
        fields = ['id','subject', 'details', 'date', 'time', 'is_completed', 'created_at', 'updated_at']